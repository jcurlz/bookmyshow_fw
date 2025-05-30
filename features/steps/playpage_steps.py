# playpage_steps.py
import logging
import time

from behave import *

@given('I hit Chennai URL and click on Play tab')
def open_chennaipage_and_click_playtab(context):
     context.base.open_url(context.playpg.CHENNAI_URL)
     time.sleep(1)
     context.playpg.element_click(context.homepg.play_tab)
     time.sleep(1)


@given('I verify the play url')
def verify_the_play_url(context):
    context.base.open_url(context.playpg.PLAYS_URL)
    logging.info(f"DEBUG >> Play URL Verification")


@when('I click on Date option')
def click_on_date_option(context):
    context.playpg.element_click(context.playpg.date_filter)
    time.sleep(5)


@when('I verify the "{options}"')
def verify_the_options(context, options):
    logging.info(f"DEBUG >> Options: {options}")
    actual_options = context.base.assert_the_options(context.playpg.date_filter_components, options)

@then('I click on the Date Range')
def click_on_the_date_range(context):
    context.base.click_on_element(context.playpg.date_range_checkbox)
    logging.info(f"DEBUG >> Options: Date range checked")

@then('I click the right arrow till I reach "{month}"')
def click_the_right_arrow(context, month):
    context.playpg.click_right_arrow(month)
    time.sleep(5)