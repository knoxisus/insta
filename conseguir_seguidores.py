#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import os

from random import randint

import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

# ==========================================
from keys import USERNAME, PASSWORD 
# ==========================================

TIMEOUT = 6


# In[ ]:


edge_driver_path = os.path.join(os.getcwd(), 'msedgedriver.exe')
edge_service = Service(edge_driver_path)

options = Options()
options.add_argument('--no-sandbox')
options.add_argument("--log-level=3")
mobile_emulation = {
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
options.add_experimental_option("mobileEmulation", mobile_emulation)

bot = webdriver.Edge(service=edge_service, options=options)


# In[ ]:


bot.get('https://www.instagram.com/accounts/login/')

username = WebDriverWait(bot, TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
username.clear()
username.send_keys(USERNAME)

password = WebDriverWait(bot, TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
password.clear()
password.send_keys(PASSWORD)

log_in = WebDriverWait(bot, TIMEOUT).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

time.sleep(randint(9,12))


# In[ ]:

# Usuarios de los que se quiere sacar los seguidores.
usernames = ["streamingkingchile", "arteyperfumesamatista"]

database = []
for user in usernames:
    bot.get('https://www.instagram.com/{}/'.format(user))

    time.sleep(3.5)
    
    WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, "//a[contains(@href, '/followers')]"))).click()
    
    try:
        ver_todo = WebDriverWait(bot, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/followers/mutualFirst')]")))
        if ver_todo:
            ver_todo.click()
    except TimeoutException:
        pass
    
    time.sleep(randint(2,3))

    for _ in range(5):
        ActionChains(bot).send_keys(Keys.END).perform()
        time.sleep(2)
    
    followers = bot.find_elements(By.XPATH, "//a[contains(@href, '/')]")
    
    for i in followers:
        if i.get_attribute('href'):
            database.append(i.get_attribute('href').split("/")[3])
        else:
            continue


# In[ ]:


usernames = list(dict.fromkeys(database))

usernames.remove(USERNAME)
usernames.remove("explore")
usernames.remove("reels")
usernames.remove("direct")


# In[ ]:


print('[Info] - Saving...')

with open('historial.txt', 'a') as file:
    file.write('\n'.join(usernames))

print('[DONE] - Your followers are saved in followers.txt file!')


# In[ ]:




