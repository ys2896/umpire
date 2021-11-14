import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver_path = '/app/.chromedriver/bin/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
#※headlessにしている
driver = webdriver.Chrome(options=options, executable_path=driver_path)
driver.implicitly_wait(10)
driver.set_window_size('1200', '1000')

url1 = "https://npb.jp/umpires/register/31133887.html"

driver.get(url1)

#driver.find_element(by=By.XPATH, value="//input[@type='text']")

umpire_name = driver.find_element(By.cssSelector,value="//input[#layout > div > div > div.detail_unit > div > dl > dt]".text)


message = umpire_name
access_token    = 'dCWCG2T3KsJk3zLMCWkOkxjn29RmPocQV7j94wKeFVt'
url             = "https://notify-api.line.me/api/notify"
headers         = {'Authorization': 'Bearer ' + access_token}
payload = {'message': message}
requests.post(url, headers=headers, params=payload,)

driver.quit()
