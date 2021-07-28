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
scroll = 0
while(scroll < 0):
    time.sleep(3)
    scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
    scroll += 1

#posts
time.sleep(3)
posts = []
links = driver.find_elements_by_tag_name('a')
for link in links:
    post = link.get_attribute('href')
    if '/p/' in post:
      posts.append(post)

print(posts)

# Hover and Collect Likes/Views and Comments For Each Post
time.sleep(3)
stats = []
classes = driver.find_elements_by_class_name('_9AhH0')
action = ActionChains(driver)
i = 0

while i < len(classes):
    action.move_to_element(classes[i])
    time.sleep(1)
    for details in driver.find_elements_by_class_name("-V_eO"):
        print("hi")
    i += 1
a.preform()