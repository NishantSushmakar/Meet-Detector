from selenium import webdriver
from bs4 import BeautifulSoup
import time


def issue_warning(username, browser):
    text_area = browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea')
    text_area.click()
    message = '{} please maintain the decorum of the meeting'.format(username)
    text_area.send_keys(message)
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[2]').click()
    return


def remove_user(name,browser):
    '''
    Description 
    
    Input : User Name to be removed
    
    Function removes the user 
    
    '''
    browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[4]/div/div[2]/div[2]/div[1]/div[1]').click()
    search = BeautifulSoup(browser.page_source, 'html.parser')
    users = search.find_all("div",{'class':'KV1GEc'})
    i = 1
    flag = False
    for user in users:

        user_name = user.find_all("span",{'class':'ZjFb7c'})
        print(user_name[0].get_text())
        if user_name[0].get_text()==name :
                   
            browser.find_element_by_xpath(f'//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[1]/div[2]/div[2]/div/div[{i}]/div[2]/div[2]').click()
            flag = True
            break
        i += 1
        
    if flag == True :
        time.sleep(8)
        browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[1]/div[4]/div/div/span[2]/div[3]/div').click()
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div[2]/span/span').click()
    
    
    return browser
