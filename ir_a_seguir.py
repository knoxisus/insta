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


f = open("historial.txt", "r")
users = f.readlines()
f.close()


# In[ ]:


max_follow = randint(10,20)
remove_list = []
for user in users:
    bot.get('https://www.instagram.com/{}/'.format(user[:-1]))

    time.sleep(randint(4,6))
    
    if bot.find_elements(By.XPATH, "//div[contains(text(), 'Pendiente')]"):
        continue
    
    if not bot.find_elements(By.XPATH, "//div[contains(text(), 'Siguiendo')]"):
        print(f"{user[:-1]} no lalo sigo...")
        time.sleep(randint(1,2))
        button = WebDriverWait(bot,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"._acan")))
        if button:
            button.click()
            print("ahora si!")
            remove_list.append(user)
        
    if len(remove_list) > max_follow:
        break
    
    time.sleep(randint(1,3))


# In[ ]:


res = [i for i in users if i not in remove_list]

with open('historial.txt', 'w') as file:
    file.write(''.join(res))

with open('siguiendo.txt', 'a') as file:
    file.write(''.join(remove_list))


# In[ ]:




