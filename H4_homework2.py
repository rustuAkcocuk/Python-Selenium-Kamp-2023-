from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_saucedemo:
    test=webdriver.Chrome(ChromeDriverManager().install())
    test.maximize_window()
    test.get("https://www.saucedemo.com/")
    sleep(2)
    testUsername=test.find_element(By.ID,"user-name")
    testPassword=test.find_element(By.ID,"password")
    loginButton=test.find_element(By.XPATH,"//*[@id='login-button']")
    
    def test_user_pass_null(self):
        #kullanıcı adı ve şifre boş olma durumu
        self.testUsername.clear()
        self.testPassword.clear()
        self.testUsername.send_keys()
        self.testPassword.send_keys()
        sleep(2)
        self.loginButton.click()
        sleep(2)
        errorMessage1=self.test.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        messageCheck1=errorMessage1.text=="Epic sadface: Username is required"
        print(f"Kullanıcı adı ve şifre boş bırakıldığında ki hata mesajı durumu : {messageCheck1}")
        sleep(2)

    def test_pass_null(self):
        # #sadece şifre boş olma durumu
        self.testUsername.clear()
        self.testPassword.clear()
        self.testUsername.send_keys("Pythone")
        self.testPassword.send_keys()
        sleep(2)
        self.loginButton.click()
        sleep(2)
        errorMessage2=self.test.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        messageCheck2=errorMessage2.text=="Epic sadface: Password is required" 
        print(f"Sadece şifre alanı boş bırakıldığında ki hata mesajı: {messageCheck2} ")
        sleep(2)

    def test_user_lock(self):
        # #kilitli kullanıcı durumu 
        self.testUsername.clear()
        self.testPassword.clear()
        self.testUsername.send_keys("locked_out_user")
        self.testPassword.send_keys("secret_sauce")
        sleep(2)
        self.loginButton.click()
        sleep(2)
        errorMessage3=self.test.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        messageCheck3=errorMessage3.text=="Epic sadface: Sorry, this user has been locked out."
        print(f"Belirtilen kullanıcı adı ve şifre kilitli kullanıcı  durumundaki mesaj: {messageCheck3}")
        sleep(2)

    def test_message_error_exit(self):
        #hata mesajı kapatma durumu///////////////////////////////////////////olmadı 
        userIcone1=False
        passIcone1=False
        userIcone2=False
        passIcone2=False
        self.testUsername.clear()
        self.testPassword.clear()
        sleep(2)
        
        self.loginButton.click()
        sleep(5)
        try:
           0!=len(self.test.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/svg"))
           userIcone1=True
        except:
         
         userIcone1=False
        try:
         0!=len(self.test.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/svg"))
         passIcone1=True
        except:
         passIcone1=False
         
        erroorIconeMsg=self.test.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        erroorIconeMsg.click()
        try:
           0!=len(self.test.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/svg"))
           userIcone2=True
        except:
         userIcone2=False
         
        try:
         0!=len(self.test.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/svg"))
         passIcone2=True
        except:
         passIcone2=False
        print(f"Kullanıcı adı ve şifre boş bırakılınca username kırmızı 'X' çıkması {userIcone1}, password kırmısı 'X' çıması {passIcone1}")
        print(f"Hata mesajı yanındaki kırmızı 'X' e tıklanınca username dekinin kaybolma durumu {userIcone2}, password dekinin kaybolma durumu {passIcone2}")
        sleep(2)

    def test_user_pass_orientation(self):
         #belirtilen kullanıcı adı ve şifre ile istenilen sayfaya yönlendirilme durumu
        desiredUrl="https://www.saucedemo.com/inventory.html"
        desiredState1=False
        self.testUsername.clear()
        self.testPassword.clear() 
        sleep(2)
        self.testUsername.send_keys("standard_user")
        self.testPassword.send_keys("secret_sauce")
        sleep(2)
        self.loginButton.click()
        sleep(3)
        testUrl=self.test.current_url
        if testUrl==desiredUrl:
           desiredState1=True
        print(f"İstenilen kullanıcı adı ve şifre sonucunda istenilen sayfa yönlendirme durumu : {desiredState1}")
        sleep(5)

    def test_desired_product(self):
         #Giriş yapıldıktan sonra kullanıcıya sınırlı ürün gösterme durumu
        desiredquantity=6
        desiredState2=False
        listOfProduct=self.test.find_elements(By.CLASS_NAME,"inventory_item")
        if len(listOfProduct)==desiredquantity:
            desiredState2=True
        print(f"Sayfada gösterilen ve istenen ürün sayısı durumu {desiredState2}")

        
test_Class=Test_saucedemo()

# test_Class.test_user_pass_null()
# test_Class.test_pass_null()
# test_Class.test_user_lock()
# test_Class.test_user_pass_orientation()
# test_Class.test_desired_product()
test_Class.test_message_error_exit() # bu kısımda kod çalışıyor fakat konturol de bi sıkıntı var yanlış okuyor
     