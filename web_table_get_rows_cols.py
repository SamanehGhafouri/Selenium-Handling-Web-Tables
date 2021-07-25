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

    def test_read_data_in_rows(self):
        driver = self.driver
        driver.get(test_url)

        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "w3-example")))

        rows = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
        columns = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[2]/td"))

        before_xpath = "//*[@id='customers']/tbody/tr["
        aftertr_xpath = "]/td["
        aftertd_xpath = "]"

        for c in range(1, (columns + 1)):
            for r in range(2, (rows + 1)):
                final_xpath = before_xpath + str(r) + aftertr_xpath + str(c) + aftertd_xpath
                rows_text = driver.find_element_by_xpath(final_xpath).text
                print(rows_text)
            print(f"Data present in Rows, col {c}")
            print()

    def test_locating_an_element(self):
        driver = self.driver
        driver.get(test_url)

        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "w3-example")))

        rows = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
        columns = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[2]/td"))

        before_xpath = "//*[@id='customers']/tbody/tr["
        aftertr_xpath = "]/td["
        aftertd_xpath = "]"

        search_text = "mAgazzini Alimentari rIUniti"
        element_found = False

        for r in range(2, (rows + 1)):
            for c in range(1, (columns + 1)):
                final_xpath = before_xpath + str(r) + aftertr_xpath + str(c) + aftertd_xpath
                cell_text = driver.find_element_by_xpath(final_xpath).text
                if cell_text.casefold() == search_text.casefold():
                    print(f"Search Text {search_text} is present at row {str(r)} and column {str(c)}")
                    element_found = True
                    break
        if not element_found:
            print(f"Search Text {search_text} not found")

    def test_locating_an_element_2(self):
        driver = self.driver
        driver.get(test_url)

        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "w3-example")))

        search_text = "Roland Mendel"

        rows = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
        columns = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[2]/td"))

        before_xpath = "//*[@id='customers']/tbody/tr["
        aftertr_xpath = "]/td["
        aftertd_xpath = "]"

        elem_found = False

        for r in range(2, (rows + 1)):
            for c in range(1, (columns + 1)):
                final_xpath = before_xpath + str(r) + aftertr_xpath + str(c) + aftertd_xpath
                element_txt = driver.find_element_by_xpath(final_xpath).text
                if element_txt.casefold() == search_text.casefold():
                    print(f"Search Text {search_text} is present at row {str(r)} and column {str(c)}")
                    elem_found = True
                    break
        if not elem_found:
            print(f"Search Text {search_text} not found in this table.")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
