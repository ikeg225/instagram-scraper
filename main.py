from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time
import csv

# Global Variables
post_limit = 100
ig_username = "throwbackhoops"

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

# Search and get account
time.sleep(5)
searchbox = driver.find_element_by_css_selector("input[placeholder='Search']")
searchbox.clear()
searchbox.send_keys(ig_username)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)

# Scroll
scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
scroll = 0
scroll_limit = round(((post_limit - 12) / 12) + 0.5)
while(scroll < scroll_limit):
    time.sleep(3)
    scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
    scroll += 1

print("Finished Loading Posts")

#posts
time.sleep(3)
posts = []
links = driver.find_elements_by_tag_name('a')
post_count, count = 0, 0

while count < len(links) and post_count < post_limit:
    post = links[count].get_attribute('href')
    if '/p/' in post:
        posts.append(post)
        post_count += 1
    count += 1

print("Collected All Post URLs")
print(posts)

element = driver.find_element_by_class_name("nZSzR")
driver.execute_script("return arguments[0].scrollIntoView(true);", element)

# Hover and Collect Likes/Views and Comments For Each Post
time.sleep(3)
stats = []
post_count = 0
count = 0

while post_count < post_limit:
    ActionChains(driver).move_to_element(driver.find_elements_by_class_name('KL4Bh')[count]).perform()
    time.sleep(0.25)
    values = []

    for details in driver.find_elements_by_class_name("-V_eO"):
        data = details.find_elements_by_tag_name("span")
        text = data[0].text
        type_of = data[1].get_attribute("class")

        if "k" in text:
            text = float(text[0:-1]) * 1000
        elif "m" in text:
            text = float(text[0:-1]) * 1000000
        else:
            text = int(text.replace(",", ""))

        if "coreSpriteHeartSmall" in type_of:
            values.extend([text, "likes"])
        elif "coreSpriteSpeechBubbleSmall" in type_of:
            values.extend([text, "comments"])
        elif "coreSpritePlayIconSmall" in type_of:
            values.extend([text, "views"])
        else:
            values.extend([text, "unknown"])
    if len(values) != 4:
        values.extend([0, "no comments"])
    stats.append(values)
    post_count += 1
    count += 1
    if post_count % 25 == 0:
        print("Finished: " + str(post_count))


print("Found Data For All Posts")

# Adds Two Lists Into One
index = 0
all_data = []
while index < len(posts):
    next_data = stats[index]
    next_data.insert(0, posts[index])
    all_data.append(next_data)
    index += 1

all_data.insert(0, ["Post URL", "Count", "Likes or Views", "Comment Number", "Type"])
with open(ig_username + ".csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(all_data)

print("Finished!")