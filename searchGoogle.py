# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 09:50:04 2020

@author: Mai Van Hoa
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# Tải drive tương ứng của trình duyệt chrome
browser = webdriver.Chrome(executable_path="./chromedriver")

browser.get("https://www.google.com/")
sleep(3)

# click chuột phải vào inspect, chọn copy full xpath của thẻ tương ứng với ô nhập thông tin tìm kiếm
input = browser.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input")
# thông tin cần tìm kiếm
input.send_keys("convolutional neural network")
sleep(3)

input.send_keys(Keys.ENTER)

# Dừng chương trình 5s
sleep(5)

# Đóng trình duyệt
browser.close()


