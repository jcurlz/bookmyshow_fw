# environment.py
from features.pages.base_methods import BaseMethods
from features.pages.eventspage import EventsPage
from features.pages.homepage import HomePage
from features.pages.playpage import PlayPage
from features.utils.driver_initialization import initialize_driver
import logging, allure, os


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
def before_all(context):
    logging.info("************> Browser starts <************")
    context.env_driver = initialize_driver() #calls driver instance and get driver's state
    context.base = BaseMethods(context.env_driver) #inject drivers state in BaseMethod and create a reference object
    context.homepg = HomePage(context.base)
    context.playpg = PlayPage(context.base, context.homepg)
    context.eventpg = EventsPage(context.base)
    os.makedirs("screenshots", exist_ok=True)

def before_scenario(context, scenario):
    logging.info(f"\n{scenario.name} starts")


def after_scenario(context, scenario):
    if scenario.status == "failed":
        screenshot_path = f"screenshots/{scenario.status}.png"
        context.env_driver.save_screenshot(screenshot_path)

        with open(screenshot_path, "rb") as image_file:
            allure.attach(image_file.read(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
    logging.info(f"\nScenario ends")
    
def after_all(context):
    context.env_driver.quit()
    logging.info("************> Session ends <************")
