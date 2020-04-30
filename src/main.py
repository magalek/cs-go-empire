#Importing packages
from selenium import webdriver
import pandas as pd
import time
import csv
from datetime import datetime
import os.path
from os import path
from sheet import Sheet

driver = webdriver.Chrome('C:/Users/Filip/Downloads/chromedriver_win32/chromedriver.exe')

driver.get('https://csgoempire.com/')

last_coins_element = driver.find_element_by_xpath('//*[@id="page-scroll"]/div/section/div/div/div[4]/div/div[1]/div[2]')

all_coins = driver.find_elements_by_class_name('previous-rolls-item')

background = driver.find_element_by_xpath('//*[@id="page-scroll"]/div/section/div/div/div[3]')

sheet = Sheet()

def get_timer():
    timer_buf = None
    
    #print('Searching for timer element')

    while timer_buf is None:
        try:
            timer_buf = background.find_element_by_xpath('//*[@id="page-scroll"]/div/section/div/div/div[3]/div[2]/div/div[2]')
        except:
            pass
    return background.find_element_by_xpath('//*[@id="page-scroll"]/div/section/div/div/div[3]/div[2]/div/div[2]')

def get_roll():
    bet_buf = None

    while bet_buf is None:
        try:
            bet_buf = background.find_element_by_xpath('//*[@id="page-scroll"]/div/section/div/div/div[4]/div/div[1]/div[2]/div[10]/div').get_attribute('class')
        except:
            pass

    return bet_buf

def get_roll_string(roll):
    if roll.find('coin-ct') != -1:
        return 'CT'
    if roll.find('coin-t') != -1:
        return 'T'
    if roll.find('coin-bonus') != -1:
        return 'MIDDLE'    
        

def write_roll_to_csv(roll):
    
    if path.exists('bets.csv'):
        with open('bets.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                    quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([datetime.now().strftime("%d/%m/%Y %H:%M:%S"),roll])
    else:
        with open('bets.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                    quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["Date", 'Roll'])
            values = [datetime.now().strftime("%d/%m/%Y %H:%M:%S"), roll]
            writer.writerow(values)
            

timer = get_timer()

while 1:
    if timer is not None:
        try:
            print('Time left:' + str(timer.text))
            # elapsed_time = timer.text
        except:
            print('Rolling')
            timer = get_timer()
            bet = get_roll_string(get_roll())
            print(bet)
            sheet.write([datetime.now().strftime("%d/%m/%Y %H:%M:%S"), bet])
            write_roll_to_csv(bet)

    #print(background.get_attribute('style'))
    time.sleep(1)
