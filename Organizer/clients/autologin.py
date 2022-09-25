from django.http import HttpResponseRedirect,HttpResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time

class AutoLogin: 
    def auto_login(selected_creden):
        for i in selected_creden:
                        onoma=i.user_name
                        kodikos=i.password
                        edge_options = Options()
                        edge_options.add_experimental_option("detach", True)
                        driver=webdriver.Edge(r"C:\Users\User\Documents\pske_system\Organizer\Organizer\msedgedriver.exe",options=edge_options)
                        # driver.maximize_window()
                        driver.get("https://www.ependyseis.gr/mis/(S(towin1m0zsp4ner5yxb5ofdw))/System/Login.aspx?ReturnUrl=%2fmis%2f")
                        username_input_box=driver.find_element(By.NAME,"LoginControl1$txtLoginName")
                        password_input_box=driver.find_element(By.NAME,"LoginControl1$txtPassword")
                        login_button=driver.find_element(By.NAME,"LoginControl1$btnLogin")
                        username_input_box.send_keys(onoma)
                        time.sleep(0.5)
                        password_input_box.send_keys(kodikos)
                        time.sleep(0.5)
                        login_button.click()
        return HttpResponse("{'status':'ok'}")