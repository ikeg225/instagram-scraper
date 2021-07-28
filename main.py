from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time

# Setting up Chrome Driver
chrome_options = Options()
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome("/Users/ethanikegami/desktop/Sports Quiz Revival/article-writer/chromedriver", options=chrome_options)
url = "https://instagram.com/"
driver.get(url)

# Login
time.sleep(3)
username = driver.find_element_by_css_selector("input[name='username']")
password = driver.find_element_by_css_selector("input[name='password']")
username.clear()
password.clear()
username.send_keys("ahakalsllskanabvw")
password.send_keys("taco4you")
login = driver.find_element_by_css_selector("button[type='submit']").click()

accounts = ["throwbackhoops",
"hoopsdirect",
"hoopingtalk",
"sway",
"timelesssports",
"mambahistory",
"raresports",
"airjordantalk",
"hoopmixtape",
"basketball_mecca",
"hoopsofgoats",
"theyear2003",
"blisteringnba",
"jumpmanhistory",
"slamrewind",
"hoopsoncourt",
"oldschool_hoops",
"timelessmamba",
"nbastateofmind",
"lbjhistory",
"lakersbackintime",
"lebron",
"oldskoolbball",
"theclassichoops",
"rumpelstiltsky"]

# Search and get account
time.sleep(5)
searchbox = driver.find_element_by_css_selector("input[placeholder='Search']")
searchbox.clear()
searchbox.send_keys("throwbackhoops")
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)

# Scroll
scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
match=False
while(match==False):
    last_count = scrolldown
    time.sleep(3)
    scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
    if last_count==scrolldown:
        match=True