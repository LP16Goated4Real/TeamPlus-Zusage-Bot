from playwright.sync_api import sync_playwright
import time
import random
from datetime import datetime, timedelta
import logging
import traceback
import yaml
from pathlib import Path
from src.sprueche import FUNNY_PARTICIPATION_SIGNATURE, MOTIVATIONAL_PARTICIPATION_SIGNATURE

now = datetime.now()
time_range = 7 - now.weekday()

event_status = {
  "Confirmed": "bestaetigt",
  "Unsure": "abgesagt",
  "Declined / Absent": "unsicher"
}

src_dir = Path(__file__).resolve().parent
log_path = src_dir.parent / "Log" / "bot.log"
config_path = src_dir.parent / "config.yaml"

logging.basicConfig(
  filename=log_path,
  level=logging.INFO,
  format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
  with open (config_path)as f:
    config = yaml.safe_load(f)
  user_info = {
    "EMAIL": config["user"]["email"],
    "PASSWORD": config["user"]["passwort"],
    "NAME": config["user"]["spitzname"]
  }
  missing_variables = [k for k, v in user_info.items() if not v]
  if missing_variables:
    raise ValueError(f"Fehlende Werte in der config.yaml Datei: {' ,'.join(missing_variables)}")
except Exception as e:
  logging.error(f"Fehler: {e}")
  logging.error(traceback.format_exc())
  raise

try:
  with sync_playwright() as p:
    logging.info("Startet auto Zusage Bot...")
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://www.spielerplus.de/site/login")

    try: # Accept cookies
      page.locator("a.cmpboxbtnyes").click(timeout=5000)
    except:
      pass

    page.fill("input[type=email]", user_info["EMAIL"])
    page.fill("input[type=password]", user_info["PASSWORD"])
    page.click("button[type=submit]")
    time.sleep(3)
    
    page.goto("https://www.spielerplus.de/en-gb/events")
    time.sleep(3)
    
    events = page.locator("div.list.event")
    for i in range(events.count()):
      event = events.nth(i)
      
      event_date = event.locator(".panel-heading-info .panel-subtitle").inner_text().strip()
      event_title = event.locator(".panel-heading-text .panel-title").inner_text().strip()
      subtitle = event.locator(".panel-heading-text .panel-subtitle")
      event_subtitle = subtitle.inner_text().strip() if subtitle.count() > 0 else ""
      event_profile = f"{event_title} {event_subtitle} am {event_date}"
      
      selected_buttons = event.locator("button.participation-button.selected")
      if selected_buttons.count() == 1:
        status = selected_buttons.nth(0).get_attribute("title")
        logging.info(f"{event_profile}: Bereits {event_status[status]} -> ueberspringen")
        continue
      elif selected_buttons.count() > 1:
        logging.warning("Mehr als ein Knopf wurde ausgewaehlt")
        continue
      
      confirm_button = event.locator('button.participation-button[title="Confirmed"]')
      if confirm_button.count() == 1:
        year = now.year
        day, month = map(int, event_date.split("/"))
        target_date = datetime(year, month, day)
        if target_date - now < timedelta(days=time_range):    
          confirm_button.click()
          logging.info(f"{event_profile}: Zusage automatisch gesetzt")
          time.sleep(0.5)
          
          spruch = random.choice(FUNNY_PARTICIPATION_SIGNATURE)
          lp_spruch =  f"\u201C{spruch}\u201D - {user_info["NAME"]}"
          page.fill("input[type=text]", lp_spruch, timeout=2000)
          page.click("button.submit-participation")
          logging.info(fr"Spruch des Tages: {lp_spruch}")
          time.sleep(3)
        else:
          logging.info(f"{event_profile} findet nicht diese Woche statt -> ueberspringen")
      elif confirm_button.count() == 0:
        logging.warning(f"{event_profile}: Kein Zusage Knopf gefunden")
      elif confirm_button.count() > 1:
        logging.warning(f"{event_profile}: Mehr als ein Zusage Knopf gefunden")
        
    logging.info("Beendet auto Zusage Bot...")
    try:
      with open (log_path, "a") as f:
        f.write("\n")
    except FileNotFoundError:
      logging.error("bot.log Datei wurde nicht gefunden")
      print("Fehler: bot.log Datei wurde nicht gefunden")
    browser.close()
    print("TeamPlus-Zusage-Skript erfolgreich abgeschlossen.")
    
except Exception as e:
  logging.error("Skript abgestuerzt!")
  logging.error(f"Fehler: {e}")
  logging.error(traceback.format_exc())
