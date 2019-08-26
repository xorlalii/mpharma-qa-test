from datetime import date
import pytest

URL = "http://localhost:3000/"


class Patient:
    first_name = "Jodie"
    middle_name = "Connie"
    last_name = "Foster"
    phone_number = "0246628609"
    date_of_birth = date(2002, 2, 2)
    address = "355 Park Street. Accra, Ghana"

    @classmethod
    def get_initial(cls):
        return f"{cls.first_name[0]}{cls.last_name[0]}"

    @classmethod
    def get_full_name(cls):
        return f"{cls.first_name} {cls.middle_name} {cls.last_name}"


@pytest.mark.usefixtures("driver")
def test_happy_flow(driver):
    """

    :param selenium.webdriver.Chrome driver:
    :return:
    """
    # open url
    driver.get(URL)

    # fill form
    first_name = driver.find_element_by_name("firstName")
    first_name.send_keys(Patient.first_name)

    middle_name = driver.find_element_by_name("middleName")
    middle_name.send_keys(Patient.middle_name)

    last_name = driver.find_element_by_name("lastName")
    last_name.send_keys(Patient.last_name)

    phone = driver.find_element_by_name("phoneNumber")
    phone.send_keys(Patient.phone_number)

    dob = driver.find_element_by_name("dob")
    dob.send_keys(str(Patient.date_of_birth))

    address = driver.find_element_by_name("address")
    address.send_keys(Patient.address)
    # submit form
    btn = driver.find_element_by_xpath("//a[@type='sumbit']")
    btn.click()

    # check created data in user list section
    card = driver.find_element_by_xpath("//div[@id='root']/div/div[2]/main/div")
    assert card.is_displayed()

    icon = driver.find_element_by_xpath("//div[@id='root']/div/div[2]/main/div/div")
    assert icon.text == Patient.get_initial()

    name = driver.find_element_by_xpath("//div[@id='root']/div/div[2]/main/div/div[2]/h4")
    assert name.text == Patient.get_full_name()

    address_display = driver.find_element_by_xpath("//div[@id='root']/div/div[2]/main/div/div[2]/p")
    assert Patient.address in address_display.text

    dob_display = driver.find_element_by_xpath("//div[@id='root']/div/div[2]/main/div/div[2]/p[2]")
    assert dob_display.is_displayed()
