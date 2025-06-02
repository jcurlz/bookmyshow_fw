import logging
import time

from behave import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

@given('I am in Price tab page')
def open_homepage(context):
    context.base.open_url(context.eventpg.EVENTSPG_CHENNAI)
    

@when('I select Price filter')
def select_price_filter(context):
    context.base.click_on_element(context.eventpg.price_filter)
    time.sleep(0.5)

@when('I verify the range values "{options}"')
def verify_the_options(context, options):
    logging.info(f"DEBUG >> Options: {options}")
    context.base.assert_the_options(context.eventpg.price_filter_component, options)
    time.sleep(2)

@then('I click on "0 - 500"')
def click_on_the_price_range(context):
    context.base.click_on_element(context.eventpg.price_exp_range)
    time.sleep(1)

@when('I click on the 3rd card')
def click_on_the_3rd_card(context):
    context.base.click_on_element(context.eventpg.card_3)
    logging.info(f"DEBUG >> Card_3 selected")

@when('I click on the card "Rambo Circus"')
def click_on_the_card_by_title(context):
    context.base.click_on_element(context.eventpg.card_by_title)
    logging.info(f"DEBUG >> Card By Title selected")

@when('I book it')
def click_on_the_book_button(context):
    context.base.click_on_element(context.eventpg.book_now_btn)
    logging.info(f"DEBUG >> Book Now selected")


@then('I click on the 2nd date')
def click_on_the_second_date(context):
    context.base.click_on_element(context.eventpg.select_date)
    logging.info(f"DEBUG >> 2nd date selected")

@then('I click on the 1st time slot')
def click_on_the_first_time_slot(context):
    context.base.click_on_element(context.eventpg.select_time)
    logging.info(f"DEBUG >> 1st time slot selected")
    time.sleep(1)


@then('I click on proceed button')
def click_on_proceed_button(context):
    context.base.click_on_element(context.eventpg.proceed_btn)
    logging.info(f"DEBUG >> Proceed button selected")
    time.sleep(1)

@when('I click on add tickets')
def click_on_add_tickets(context):
    context.base.click_on_element(context.eventpg.add_tickets_btn)
    logging.info(f"DEBUG >> Add tickets button selected")
    time.sleep(1)

@then('I add 2 tickets')
def add_tickets(context):
    element =  context.base.click_on_element_twice(context.eventpg.add_3_tickets)
    if not element:
        pass
    logging.info(f"DEBUG >> Add tickets clicked thrice")
    time.sleep(1)

@then('I click on "{seats}"')
def click_on_no_of_seats(context, seats):
    element =  context.eventpg.click_seats(seats)
    time.sleep(5)
