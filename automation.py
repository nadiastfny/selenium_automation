import unittest
import time
from urllib import response
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(executable_path='C:/Users/Gamatechno/.wdm/drivers/chromedriver/win32/103.0.5060.53/chromedriver.exe')
        
    # test case : login success
    def test_success_login(self): 
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("nadiastfny@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("nadia170699") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data, 'Welcome nadiastfny')
        self.assertEqual(response_message, 'Anda Berhasil Login')

        driver.find_element_by_css_selector("button.swal2-confirm.swal2-styled")
        self.driver.close()

    # test case : register with existing account
    def test_register_existing_account(self):
        driver = self.driver
        driver.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        driver.find_element(By.ID, "signUp").click()
        time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys("nadiastfny") 
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys("nadiastfny@gmail.com") 
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("nadia170699") 
        time.sleep(1)
        driver.find_element(By.ID,"signup_register").click()
        time.sleep(1)

        response_data = driver.find_element(By.ID, "swal2-title").text
        response_message = driver.find_element(By.ID, "swal2-content").text

        self.assertEqual(response_data, 'Email sudah terdaftar, gunakan Email lain')
        self.assertEqual(response_message, 'Gagal Registrasi')

        driver.find_element_by_css_selector("button.swal2-confirm.swal2-styled")
        time.sleep(1)
        self.driver.close()

    # test case : register with new account 
    def test_register_success(self):
        driver = self.driver
        driver.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(3)
        driver.find_element(By.ID, "signUp").click()
        time.sleep(1)
        driver.find_element(By.ID,"name_register").send_keys("adi") 
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys("adi@gmail.com") 
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("1234567") 
        time.sleep(1)
        driver.find_element(By.ID,"signup_register").click()
        time.sleep(1)

        response_data = driver.find_element(By.ID, "swal2-title").text
        response_message = driver.find_element(By.ID, "swal2-content").text

        self.assertEqual(response_data, 'berhasil')
        self.assertEqual(response_message, 'created user!')

        driver.find_element_by_css_selector("button.swal2-confirm.swal2-styled")
        time.sleep(1)
        self.driver.close()

    # test case : login with wrong password
    def test_failed_login(self):
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("nadiastfny@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = driver.find_element(By.ID,"swal2-title").text
        response_message = driver.find_element(By.ID,"swal2-content").text

        self.assertEqual(response_data, "User's not found")
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

        driver.find_element_by_css_selector("button.swal2-confirm.swal2-styled")
        self.driver.close()

    # test case : registrasi di website myapp
    def test_register_myapp(self):
        driver = self.driver
        driver.get("https://myappventure.herokuapp.com/registration") # buka situs
        time.sleep(2)
        driver.find_element(By.NAME, "username").send_keys("azam")
        time.sleep(1)
        driver.find_element(By.NAME, "email").send_keys("azam@yahoo.com") 
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("12345678")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/main/div/div/form/div[5]/button").click()
        time.sleep(2)
        self.driver.close()

    # test case : login di website myapp
    def test_success_login_myapp(self):
        driver = self.driver
        driver.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(2)
        driver.find_element(By.NAME, "email").send_keys("bayuu@yahoo.com") # isi password
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("12345678")
        time.sleep(1)
        driver.find_element_by_css_selector("#__next > main > div > div > form > div.mt-8 > button").click()
        time.sleep(5)
        self.driver.close()

    # test case : login di website myapp with wrong password
    def test_failed_login_myapp(self):
        driver = self.driver
        driver.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(2)
        driver.find_element(By.NAME, "email").send_keys("bayuu@yahoo.com") # isi password
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("123")
        time.sleep(1)
        driver.find_element_by_css_selector("#__next > main > div > div > form > div.mt-8 > button").click()
        time.sleep(5)

        response = driver.find_element_by_css_selector("#__next > main > div > div > form > div.flex.items-center.justify-center.text-xs.font-semibold.text-\[\#FF8181\].pb-4 > p").text
        self.assertEqual(response, "Kata Sandi Salah")
        self.driver.close()

if __name__ == "__main__": 
    unittest.main()