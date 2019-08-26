from datetime import date
import pytest

URL = "http://localhost:3000/"


class Patient:
    first_name = "Jodie"
    middle_name = "Connie"
    last_name = "Foster"
    phone_number = "0246628609"
    date_of_birth = date(2002, 2, 2)
    address = "355 Park Street.\nAccra, Ghana"


@pytest.mark.usefixtures("driver")
def test_happy_flow(driver):
    """

    :param selenium.webdriver.Chrome driver:
    :return:
    """
    # open url
    driver.get(URL)
