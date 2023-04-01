from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date

class Test_Odev5_2:
    def setup_method(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        # günün tarihini al bu tarih ile bir klasör var mı kontrol et yoksa oluştur.
        self.folderPath=str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()
    
    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_all_elements_located(locator))

    def test_empty_login(self):
        # Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-for-empty-login.png")
        assert errorMessage.text == "Epic sadface: Username is required"
        sleep(5)
    
    def test_empty_password(self):
        # Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("abcdsd")
        passwordInput.send_keys("")
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-for-empty-password.png")
        assert errorMessage.text == "Epic sadface: Password is required"
    
    def test_locked_user(self):
        # Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde 
        # "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-locked-user.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

    def test_close_red_icon(self):
        # Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. 
        # Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        listOfXicon=self.driver.find_elements(By.XPATH,"//*[name()='svg']//*[local-name()='path']") #Designing XPATH for SVG elements
        self.driver.save_screenshot(f"{self.folderPath}/test-opened-red-icon.png")
        assert len(listOfXicon)==3 #ekrandaki X icon sayısı = username X icon + password X icon + errorBtn X icon = 3
        errorBtn=self.driver.find_element(By.CLASS_NAME,"error-button")
        errorBtn.click()       
        # errorbutonu tıkladıktan sonra ekrandaki tüm x iconlar gider. Bu nedenle yeniden ekrandaki X icon sayısına bakılmalı
        listOfXicon2=self.driver.find_elements(By.XPATH,"//*[name()='svg']//*[local-name()='path']")
        self.driver.save_screenshot(f"{self.folderPath}/test-closed-red-icon.png")
        assert len(listOfXicon2)==0
         

    def test_redirect_to_website(self):
        # Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-redirect-to-website.png")
        assert self.driver.current_url=="https://www.saucedemo.com/inventory.html"

    def test_count_products(self):
        # Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        listOfProducts=self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        self.driver.save_screenshot(f"{self.folderPath}/test-count-products.png")
        assert len(listOfProducts)==6

    def test_sort_product_price(self):
        # https://www.saucedemo.com/inventory.html sayfasında ürünleri düşük fiyattan yüksek fiyata doğru filtrele
        self.test_redirect_to_website() #https://www.saucedemo.com/inventory.html sayfasına gider
        filterBtn=self.driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select")
        filterBtn.click()
        priceToHighBtn=self.driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/div/span/select/option[3]")
        sleep(2)
        priceToHighBtn.click()
        listOfPrice=self.driver.find_elements(By.CLASS_NAME,"inventory_item_price")
        self.driver.save_screenshot(f"{self.folderPath}/test_sort_product_price.png")
        x=listOfPrice[0].text.replace("$","")
        y=listOfPrice[1].text.replace("$","")
        assert float(x) <= float(y)
    
    def test_redirect_to_cart(self):
        # Cart buttonuna basınca https://www.saucedemo.com/cart.html adresine gitmeli
        self.test_redirect_to_website()
        cartBtn=self.driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        cartBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-redirect-cart-url.png")
        assert self.driver.current_url=="https://www.saucedemo.com/cart.html"
    
    def test_remove_cart(self):
        # sepete eklenen ürünün silinmesi
        self.test_redirect_to_website()
        p1_addBTn=self.driver.find_element(By.NAME,"add-to-cart-sauce-labs-backpack")
        p1_addBTn.click() 
        cartBtn=self.driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        cartBtn.click()
        removeBtn=self.driver.find_element(By.NAME,"remove-sauce-labs-backpack")
        removeBtn.click()
        listOfCartItem=self.driver.find_elements(By.CLASS_NAME,"cart_item")
        self.driver.save_screenshot(f"{self.folderPath}/test-remove-cart-product.png")
        assert len(listOfCartItem)==0
    
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce"),("problem_user","secret_sauce"),("performance_glitch_user","secret_sauce")])
    def test_valid_login(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-valid-login-{username}-{password}.png")
        assert self.driver.current_url=="https://www.saucedemo.com/inventory.html"
        
        
        
        

