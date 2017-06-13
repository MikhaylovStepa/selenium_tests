import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from urls import BASE_URL, ADMIN, EXP
from login_data import LOGIN, PASS


class Categories(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(chrome_options=options)

    def test_1_create_category(self):
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
        elem = driver.find_element_by_xpath('//*[@id="collapseTests"]/div/nav/ul/li[1]/a')
        elem.click()
        time.sleep(3)
        assert driver.current_url == BASE_URL+ADMIN+EXP
        elem = driver.find_element_by_name('Experience[experience]')
        elem.clear()
        elem.send_keys('Test category')
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        elems = driver.find_elements_by_class_name('table-link')
        is_element_exist = False
        for item in elems:
            if item.text == 'Test category':
                is_element_exist = True
        assert is_element_exist == True

    def test_2_edit_category(self):
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
        elem = driver.find_element_by_xpath('//*[@id="collapseTests"]/div/nav/ul/li[1]/a')
        elem.click()
        time.sleep(3)
        assert driver.current_url == BASE_URL+ADMIN+EXP
        elems = driver.find_elements_by_class_name('table-link')
        is_element_exist = False
        edit_elem = False
        for item in elems:
            if item.text == 'Test category':
                is_element_exist = True
                edit_elem = item
        assert is_element_exist == True
        edit_elem.click()
        time.sleep(3)
        elem = driver.find_element_by_name('Experience[experience]')
        elem.clear()
        elem.send_keys('Edited category')
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        elems = driver.find_elements_by_class_name('table-link')
        is_element_exist = False
        for item in elems:
            if item.text == 'Edited category':
                is_element_exist = True
        assert is_element_exist == True

    def test_3_delete_category(self):
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
            '//*[@id="collapseTests"]/div/nav/ul/li[1]/a')
        elem.click()
        time.sleep(3)
        assert driver.current_url == BASE_URL+ADMIN+EXP
        elems = driver.find_elements_by_class_name('table-link')
        is_element_exist = False
        for item in elems:
            if item.text == 'Edited category':
                is_element_exist = True
        assert is_element_exist == True
        i = 0
        index = -1
        while i < len(elems):
            if elems[i].text == 'Edited category':
                is_element_exist = True
                index = i
                break
            i = i+1
        elems =driver.find_elements_by_class_name('btn-delete')
        i = 0
        while i < len(elems):
            if i==index:
                elems[i].click()
                time.sleep(3)
                elem = driver.find_element_by_xpath('//*[@id="deleteCategoryModal"]/div/div/div[3]/div/a')
                elem.click()
                time.sleep(3)
                break
            i = i + 1
        elems = driver.find_elements_by_class_name('table-link')
        is_element_exist = False
        for item in elems:
            if item.text == 'Edited category':
                is_element_exist = True
        assert is_element_exist == False

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()