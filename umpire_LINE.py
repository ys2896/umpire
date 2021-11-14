import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url1 = "https://npb.jp/umpires/register/31133887.html"

driver.get(url1)

umpire_name = driver.find_element_by_css_selector("#layout > div > div > div.detail_unit > div > dl > dt").text


message = umpire_name
access_token    = 'dCWCG2T3KsJk3zLMCWkOkxjn29RmPocQV7j94wKeFVt'
url             = "https://notify-api.line.me/api/notify"
headers         = {'Authorization': 'Bearer ' + access_token}
payload = {'message': message}
requests.post(url, headers=headers, params=payload,)

driver.quit()
