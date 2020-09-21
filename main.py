import os

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

email = 'winandiaris@gmail.com'
password = 'aris1985'

# menjalankan chromedriver.exe
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"))

# target url yang ingin di otomatisasi
driver.get("https://www.youtube.com/edit?video_id=D0_41NWqOxU&nps=1")
#memilih field email dan mengisikannya dengan var email
driver.find_element_by_id("identifierId").send_keys(email)
# klik tombol Next ------>SAMPAI DISINI GAGAL, KARENA KETIKA LOGIN DIHALANGI GOOGLE
driver.find_element_by_id("identifierNext").click()

#Tunggu loading sampai password muncul
element = WebDriverWait(driver, WAIT_TIME).until(
            EC.element_to_be_clickable( (By.NAME, "password") )
        )
#mengetikkan var password
element.send_keys(password)
# klik tombol Next
driver.find_element_by_id("passwordNext").click()

#use youtube as...(memilih akun yg aktif)
element = WebDriverWait(driver, WAIT_TIME).until(
            EC.element_to_be_clickable( (By.CSS_SELECTOR, "input[type='radio'][value='123456789']") )
        )
#klik akun
element.click()
driver.find_element_by_id("identity-prompt-confirm-button").click()

#tunggu sampai .yt-uix-form-input-textarea.metadata-share-contacts bisa di klik
element = WebDriverWait(driver, WAIT_TIME).until(
            EC.element_to_be_clickable( (By.CSS_SELECTOR, ".yt-uix-form-input-textarea.metadata-share-contacts") )

        )

#mnambahkan email yang ingin didaftarkan agar bisa nonton youtube
element.send_keys('winandiaris2@gmail.com')
#uncheck checkbox 'notify via email'
driver.find_element_by_css_selector(".yt-uix-form-input-textarea.metadata-share-contacts").click()
#klik tombol 'save and go back to Youtube Studio'
driver.find_element_by_css_selector(".yt-uix-button.yt-uix-button-primary.sharing-dialog-button.sharing-dialog-ok").click()

#tunggu proses sampai muncul kata-kata Saved, didalam element:.yt-dialog-working-bubble.yt-dialog-waiting-content
element = WebDriverWait(driver, WAIT_TIME).until(
            EC.text_to_be_present_in_element( (By.CSS_SELECTOR, ".yt-dialog-working-bubble.yt-dialog-waiting-content"), 'Saved' )

        )

#SELESAI, keluar
driver.quit()