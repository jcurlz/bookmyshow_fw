# playpage_steps.py
import logging
import time


from behave import *

@given('I hit Chennai URL and click on Play tab')
def open_chennaipage_and_click_playtab(context):
     context.base.open_url(context.playpg.CHENNAI_URL)
     context.playpg.element_click(context.homepg.play_tab)
     time.sleep(0.5)


@given('I verify the play url')
def verify_the_play_url(context):
    context.base.open_url(context.playpg.PLAYS_URL)
    logging.info(f"DEBUG >> Play URL Verification")


@when('I click on Date option')
def click_on_date_option(context):
    context.playpg.element_click(context.playpg.date_filter)


@when('I verify the "{options}"')
def verify_the_options(context, options):
    logging.info(f"DEBUG >> Options: {options}")
    context.base.assert_the_options(context.playpg.date_filter_components, options)

@then('I click on the Date Range')
def click_on_the_date_range(context):
    context.base.click_on_element(context.playpg.date_range_checkbox)
    logging.info(f"DEBUG >> Options: Date range checked")

@then('I click the right arrow till I reach "{month_year}"')
def click_the_right_arrow(context, month_year):
    logging.info(f"DEBUG >> Month Year to search: {month_year}")
    context.playpg.click_right_arrow(month_year)

@then('I click and apply start date "{start_dt}" and end date "{end_dt}" of month "{month}"')
def click_and_apply_date(context, start_dt, end_dt, month):
    context.playpg.click_date(start_dt, month)
    logging.info(f"DEBUG >> Start Date: {start_dt}, {month}cicked")
    time.sleep(0.5)
    context.playpg.click_date(end_dt, month)
    logging.info(f"DEBUG >> End Date: {end_dt}, {month} cicked")
    time.sleep(0.5)
    logging.info(f"DEBUG >> Now lets apply date")
    time.sleep(1.5)
    context.base.click_on_element(context.playpg.date_range_apply_button)
    logging.info(f"DEBUG >> Apply button clicked")


@then('I verify the date selection confirmation {date_range_confirmation}')
def verify_date_range_confirmation(context, date_range_confirmation):
    logging.info(f"DEBUG >> Date range: {date_range_confirmation} to be asserted")
    context.playpg.assert_date_confirmation(date_range_confirmation)
