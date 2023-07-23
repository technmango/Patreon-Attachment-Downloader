import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import account_info


def loginInformation() :#grab user sensitive info
    username=account_info.email #gets email info from py file
    password=account_info.password #gets password info from py file
    return username, password

#log into Patreon
def logInSession():
  time.sleep(2)
  driver.maximize_window
  username, password=loginInformation()
  driver.get(url1)
  driver.find_element(By.NAME,"email").send_keys(username)
  time.sleep(1)
  driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/main/div[1]/div/div/form/div[2]/button").click()
  time.sleep(3)
  driver.find_element(By.NAME,"current-password").send_keys(password)
  time.sleep(2)
  driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/main/div[1]/div/div/form/div[3]/button").click()
  time.sleep(3)

# set up webdriver and prepare to log in to chrome
url1='https://www.patreon.com/login'
driver=webdriver.Chrome
driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get(url1)
logInSession()

#get desired creator link
paetronLink=input("Which Paetron Link would you like to download from?\n")
print ("Checking.. Now")
driver.get(paetronLink)

#"import" website into beautfiul soup to scrape all file attachments
paetronLink = driver.page_source
soup = BeautifulSoup(paetronLink, 'html.parser')
attachments = soup.find_all('a', href=re.compile(r"^https://www.patreon.com/file"))

# user validation for documentation
count = 0
for attachment in attachments:
    download_link=(attachment['href'])
    count += 1

    driver.get(download_link)
    time.sleep(10)

print(f"Total attachments found: {count}")





  








  




   




 




