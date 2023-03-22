from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Sauce:
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    sleep(5)
    
    def test_empty_login(self):
        
        usernameInput=self.driver.find_element(By.ID,"user-name")
        passwordInput=self.driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn=self.driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult=errorMessage.text == "Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")
        sleep(100)
    
    def test_empty_password(self):
        usernameInput=self.driver.find_element(By.ID,"user-name")
        passwordInput=self.driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("abcdsd")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn=self.driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult=errorMessage.text == "Epic sadface: Password is required"
        print(f"TEST SONUCU: {testResult}")
        sleep(100)
    
    def test_locked_user(self):
        usernameInput=self.driver.find_element(By.ID,"user-name")
        passwordInput=self.driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=self.driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult=errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")
        sleep(100)

    def close_red_icon(self):
        usernameInput=self.driver.find_element(By.ID,"user-name")
        passwordInput=self.driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn=self.driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        errorBtn=self.driver.find_element(By.CLASS_NAME,"error-button")
        sleep(2)
        errorBtn.click()
        print("Please, Try to login again!!")
        sleep(100)
    
    def test_redirect_to_website(self):
        usernameInput=self.driver.find_element(By.ID,"user-name")
        passwordInput=self.driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=self.driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        print("Redirected to 'https://www.saucedemo.com/inventory.html'")
        sleep(100)
    
    def test_count_products(self):
        usernameInput=self.driver.find_element(By.ID,"user-name")
        passwordInput=self.driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=self.driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        listOfProducts=self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"There are {len(listOfProducts)} products.")
        sleep(100)
        

testClass=Test_Sauce()
# testClass.test_empty_login()
# testClass.test_empty_password()
# testClass.test_locked_user()
# testClass.close_red_icon()
# testClass.test_redirect_to_website()
testClass.test_count_products()