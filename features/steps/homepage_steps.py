# homepage_steps.py
import time

from behave import *
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@given('I open the BookMyShow homepage')
def open_homepage(context):
    context.base.open_url(context.base.BASE_URL)


@then('I check if location box is open else open it')
def check_location_box(context):
    loc_box_presence = context.base.true_or_false(context.homepg.homepg_loc_box_search_field)
    if loc_box_presence:
        logging.info('✅ Location box is open and visible')
    else:
        context.homepg.click_on_location_box(context.homepg_loc_box_search_field)
        logging.info('Location box clicked')


@then('I enter "{locations}" in the search and assert the "{loc_suggestions}"')
def enter_location_suggestions(context, locations, loc_suggestions):
    logging.info(f"DEBUG >> locations: {locations}")
    context.base.click_on_element(context.homepg.homepg_loc_box_search_field)
    context.base.enter_text(context.homepg.homepg_loc_box_search_field, locations)
    logging.info(f"DEBUG >> location suggestions: {loc_suggestions}")
    context.homepg.assert_dropdown_list(loc_suggestions)


@then('I enter "{suggestion}" and I select Chennai from the dropdown')
def enter_and_choose_desired_option(context, suggestion):
    context.homepg.click_enter_and_choose_desired_option(suggestion)
    
    
@then('I land on Book my show chennai page')
def land_on_book_my_show_chennai_page(context):
    context.base.verify_the_url(context.homepg.HOMEPG_CHENNAI)
    logging.info(f"DEBUG >> location suggestions: {loc_suggestions}")
    