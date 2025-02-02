from alpineQuest.pages.gps_page import PositioningPage
from alpineQuest.utils.constants import GPS_PAGE


def test_get_current_location(application):
    # Step 1: Open the app.
    gps_page = PositioningPage(application)
    gps_page.open_app()
    # The app is successfully launched.

    # Step 2: Find GPS icon
    coordinates = gps_page.find_gps_button()

    # Step 3: Click GPS icon
    gps_page.click_button_at_coordinates(coordinates)
    modal_title = gps_page.find_modal_title()

    assert modal_title.text == GPS_PAGE.TITLE, f'The title of the modal is not {GPS_PAGE.TITLE}'

    # Step 4: Switch on GPS
    gps_switch = gps_page.find_switch_location_button()
    gps_switch.click()
    assert gps_switch.text != GPS_PAGE.TEXT_OFF, "First switch did not change state or was not clicked."
    switch_on = gps_page.find_and_click_location_gps_on_button()
    assert switch_on != "", "Real-time position is on"

    # Step 5: Click GPS button and close modal
    gps_page.close_gps_modal()
