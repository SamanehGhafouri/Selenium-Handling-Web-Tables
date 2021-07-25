import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test_url = "https://www.w3schools.com/html/html_tables.asp"


class WebTableTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_1_get_num_rows_(self):
        driver = self.driver
        driver.get(test_url)

        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "w3-example")))

        num_rows = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
        print("Rows in table are ", num_rows)

    def test_2_num_cols_(self):
        driver = self.driver
        driver.get(test_url)

        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "w3-example")))
        num_cols = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[2]/td"))
        print("Columns in table are ", num_cols)

    def test_get_row_col_info(self):
        driver = self.driver
        driver.get(test_url)

        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "w3-example")))

        rows = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
        columns = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[2]/td"))

        before_XPath = "//*[@id='customers']/tbody/tr["
        aftertd_XPath = "]/td["
        aftertr_XPath = "]"

        for t_row in range(2, (rows + 1)):
            for t_column in range(1, (columns + 1)):
                final_xpath = before_XPath + str(t_row) + aftertd_XPath + str(t_column) + aftertr_XPath
                cell_text = driver.find_element_by_xpath(final_xpath).text
                print(cell_text)
            print()



    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
