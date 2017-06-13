import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from urls import BASE_URL, ADMIN, THEME_IND, THEMES
from login_data import LOGIN, PASS


class Manegment(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(chrome_options=options)

    def test_1_create_manegment(self):
        driver = self.driver
        driver.get(BASE_URL + ADMIN)
        assert "Sign In" in driver.title
        elem = driver.find_element_by_name("LoginForm[email]")
        elem.clear()
        elem.send_keys(LOGIN)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_name("LoginForm[password]")
        elem.clear()
        elem.send_keys(PASS)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "No results found." not in driver.page_source
        elem = driver.find_element_by_xpath(
            '//*[@id="collapseTests"]/div/nav/ul/li[2]/a/span[2]')
        elem.click()
        time.sleep(3)
        assert driver.current_url == BASE_URL+ADMIN+THEMES
        elem = driver.find_element_by_xpath(
            '/html/body/section/main/div/div/div/a/span')
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_class_name('filter-option')
        elem.click()
        time.sleep(1)
        elems = driver.find_elements_by_class_name('text')
        category = False
        for item in elems:
            if item.text == 'IT':
                is_element_exist = True
                category = item
        assert is_element_exist == True
        category.click()
        time.sleep(1)
        elem = driver.find_element_by_id('themes-example_files')
        elem.send_keys('/home/stepan/virtualenvs/selenium_keycontent/text.txt')
        time.sleep(1)
        elem = driver.find_element_by_id('themes-topic')
        elem.clear()
        elem.send_keys('New Topic')
        time.sleep(1)
        elem = driver.find_element_by_id('themes-test_time')
        elem.clear()
        elem.send_keys('10')
        time.sleep(1)
        elem = driver.find_element_by_xpath(
            '//*[@id="themes-form"]/div[3]/div/div/ul/li[2]/span/label')
        elem.click()
        elem = driver.find_element_by_xpath(
            '//*[@id="themes-form"]/div[3]/div/div/ul/li[3]/span/label')
        elem.click()
        elem = driver.find_element_by_xpath(
            '//*[@id="themes-form"]/div[3]/div/div/ul/li[4]/span/label')
        elem.click()
        elem = driver.find_element_by_xpath(
            '//*[@id="themes-form"]/div[3]/div/div/ul/li[5]/span/label')
        elem.click()
        elem = driver.find_element_by_xpath(
            '//*[@id="themes-form"]/div[3]/div/div/ul/li[6]/span/label')
        elem.click()
        elem = driver.find_element_by_xpath(
            '//*[@id="themes-form"]/div[3]/div/div/ul/li[7]/span/label')
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_xpath(
            '//*[@id="themes-form"]/div[3]/div/div/div/button')
        elem.click()
        time.sleep(1)
        assert driver.current_url ==\
               BASE_URL+ADMIN+THEME_IND

    def test_2_check_created_manegment(self):
        driver = self.driver
        driver.get(BASE_URL+ADMIN)
        assert "Sign In" in driver.title
        elem = driver.find_element_by_name("LoginForm[email]")
        elem.clear()
        elem.send_keys(LOGIN)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_name("LoginForm[password]")
        elem.clear()
        elem.send_keys(PASS)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "No results found." not in driver.page_source
        elem = driver.find_element_by_xpath(
            '//*[@id="collapseTests"]/div/nav/ul/li[2]/a/span[2]')
        elem.click()
        time.sleep(3)
        assert driver.current_url == BASE_URL+ADMIN+THEMES
        elems = driver.find_elements_by_class_name('table-link')
        is_elem_exist = False
        elem = False
        for item in elems:
            if item.text == 'New Topic':
                is_elem_exist = True
                elem = item
                break
        assert is_elem_exist == True
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_class_name('top-title')
        assert elem.text == 'Tests management'
        elem = driver.find_element_by_xpath(
            '//*[@id="themes-form"]/div[1]/div[1]/div[1]/div/div/button/span[1]')
        assert elem.text == 'IT'
        elem = driver.find_element_by_xpath(
            '//*[@id="themes-form"]/div[1]/div[1]/div[3]/div/div/ul[1]/li/a')
        assert elem.text == 'text.txt'
        elem = driver.find_element_by_id('themes-topic')
        assert elem.text == 'New Topic'
        elem = driver.find_element_by_id('themes-test_time')
        assert elem.get_attribute('value') == '10'
        elem = driver.find_element_by_id('themes-exam_style')
        assert elem.get_attribute('value') == '1'
        elem = driver.find_element_by_id('themes-exam_grammar')
        assert elem.get_attribute('value') == '1'
        elem = driver.find_element_by_id('themes-exam_briefing')
        assert elem.get_attribute('value') == '1'
        elem = driver.find_element_by_id('themes-exam_information')
        assert elem.get_attribute('value') == '1'
        elem = driver.find_element_by_id('themes-exam_interest')
        assert elem.get_attribute('value') == '1'
        elem = driver.find_element_by_id('themes-exam_tone')
        assert elem.get_attribute('value') == '1'


    def test_3_edit_manegment(self):
        driver = self.driver
        driver.get(BASE_URL+ADMIN)
        assert "Sign In" in driver.title
        elem = driver.find_element_by_name("LoginForm[email]")
        elem.clear()
        elem.send_keys(LOGIN)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_name("LoginForm[password]")
        elem.clear()
        elem.send_keys(PASS)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "No results found." not in driver.page_source
        elem = driver.find_element_by_xpath(
            '//*[@id="collapseTests"]/div/nav/ul/li[2]/a/span[2]')
        elem.click()
        time.sleep(3)
        assert driver.current_url == BASE_URL+ADMIN+THEMES
        elems = driver.find_elements_by_class_name('table-link')
        is_elem_exist = False
        elem = False
        for item in elems:
            if item.text == 'New Topic':
                is_elem_exist = True
                elem = item
                break
        assert is_elem_exist == True
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_class_name('top-title')
        assert elem.text == 'Tests management'
        elem = driver.find_element_by_class_name('filter-option')
        elem.click()
        time.sleep(1)
        elems = driver.find_elements_by_class_name('text')
        category = False
        for item in elems:
            if item.text == 'Math':
                is_element_exist = True
                category = item
        assert is_element_exist == True
        category.click()
        time.sleep(1)
        elem = driver.find_element_by_id('themes-example_files')
        elem.send_keys(
            '/home/stepan/virtualenvs/selenium_keycontent/new_text.txt')
        time.sleep(1)
        elem = driver.find_element_by_id('themes-topic')
        elem.clear()
        elem.send_keys('New Topic Edited')
        time.sleep(1)
        elem = driver.find_element_by_id('themes-test_time')
        elem.clear()
        elem.send_keys('30')
        time.sleep(1)
        elem = driver.find_element_by_xpath(
            '//*[@id="themes-form"]/div[3]/div/div/ul/li[2]/span/label')
        elem.click()
        elem = driver.find_element_by_xpath(
            '//*[@id="themes-form"]/div[3]/div/div/ul/li[3]/span/label')
        elem.click()
        elem = driver.find_element_by_xpath(
            '//*[@id="themes-form"]/div[3]/div/div/ul/li[4]/span/label')
        elem.click()
        elem = driver.find_element_by_xpath(
            '//*[@id="themes-form"]/div[3]/div/div/ul/li[5]/span/label')
        elem.click()
        elem = driver.find_element_by_xpath(
            '//*[@id="themes-form"]/div[3]/div/div/ul/li[6]/span/label')
        elem.click()
        elem = driver.find_element_by_xpath(
            '//*[@id="themes-form"]/div[3]/div/div/ul/li[7]/span/label')
        elem.click()
        elem = driver.find_element_by_xpath(
            '//*[@id="themes-form"]/div[3]/div/div/ul/li[8]/span/label')
        elem.click()
        time.sleep(0.5)
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_xpath(
            '//*[@id="themes-form"]/div[3]/div/div/div/button')
        elem.click()
        time.sleep(1)
        assert driver.current_url == \
               BASE_URL+ADMIN+THEME_IND

    def test_4_check_created_manegment(self):
        driver = self.driver
        driver.get(BASE_URL+ADMIN+THEMES)
        assert "Sign In" in driver.title
        elem = driver.find_element_by_name("LoginForm[email]")
        elem.clear()
        elem.send_keys(LOGIN)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_name("LoginForm[password]")
        elem.clear()
        elem.send_keys(PASS)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "No results found." not in driver.page_source
        elem = driver.find_element_by_xpath(
            '//*[@id="collapseTests"]/div/nav/ul/li[2]/a/span[2]')
        elem.click()
        time.sleep(3)
        assert driver.current_url == BASE_URL+ADMIN+THEMES
        elems = driver.find_elements_by_class_name('table-link')
        is_elem_exist = False
        elem = False
        for item in elems:
            if item.text == 'New Topic Edited':
                is_elem_exist = True
                elem = item
                break
        assert is_elem_exist == True
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_class_name('top-title')
        assert elem.text == 'Tests management'
        elem = driver.find_element_by_xpath(
            '//*[@id="themes-form"]/div[1]/div[1]/div[1]/div/div/button/span[1]')
        assert elem.text == 'Math'
        elem = driver.find_element_by_xpath(
            '//*[@id="themes-form"]/div[1]/div[1]/div[3]/div/div/ul[1]/li[2]/a')
        assert elem.text == 'new_text.txt'
        elem = driver.find_element_by_id('themes-topic')
        assert elem.text == 'New Topic Edited'
        elem = driver.find_element_by_id('themes-test_time')
        assert elem.get_attribute('value') == '30'
        elem = driver.find_element_by_id('themes-exam_style')
        assert elem.get_attribute('value') == '1'
        elem = driver.find_element_by_id('themes-exam_grammar')
        assert elem.get_attribute('value') == '1'
        elem = driver.find_element_by_id('themes-exam_briefing')
        assert elem.get_attribute('value') == '1'
        elem = driver.find_element_by_id('themes-exam_information')
        assert elem.get_attribute('value') == '1'
        elem = driver.find_element_by_id('themes-exam_interest')
        assert elem.get_attribute('value') == '1'
        elem = driver.find_element_by_id('themes-exam_tone')
        assert elem.get_attribute('value') == '1'

    def test_5_delete_manegment(self):
        driver = self.driver
        driver.get(BASE_URL+ADMIN)
        assert "Sign In" in driver.title
        elem = driver.find_element_by_name("LoginForm[email]")
        elem.clear()
        elem.send_keys(LOGIN)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_name("LoginForm[password]")
        elem.clear()
        elem.send_keys(PASS)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "No results found." not in driver.page_source
        elem = driver.find_element_by_xpath(
            '//*[@id="collapseTests"]/div/nav/ul/li[2]/a/span[2]')
        elem.click()
        time.sleep(3)
        assert driver.current_url == BASE_URL+ADMIN+THEMES
        elems = driver.find_elements_by_class_name('table-link')
        is_elem_exist = False
        elem = False
        for item in elems:
            if item.text == 'New Topic Edited':
                is_elem_exist = True
                elem = item
                break
        assert is_elem_exist == True
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_class_name('top-title')
        assert elem.text == 'Tests management'
        elem = driver.find_element_by_class_name('btn-info')
        elem.click()
        time.sleep(0.5)
        elem = driver.find_element_by_xpath(
            '//*[@id="deleteTestModal"]/div/div/div[3]/div/a')
        elem.click()
        time.sleep(1)
        assert driver.current_url == \
               BASE_URL+ADMIN+THEME_IND
        elems = driver.find_elements_by_class_name('table-link')
        is_elem_exist = False
        for item in elems:
            if item.text == 'New Topic Edited':
                is_elem_exist = True
                break
        assert is_elem_exist == False

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()