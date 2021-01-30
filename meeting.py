from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from credential import email_id,password,chromedriver_path,meeting_code
from text_process import Node, process_data, process_caption
from key import get_score
from bs4 import BeautifulSoup
from multiprocessing import Process

def enter_meeting(browser,email_id,password,meeting_code):
    '''
    Input
    Browser Object
    Email ID
    Password
    Meeting Code 
    
    Description:
    This function helps to join the meeting in Google Meet
    
    '''
    browser.get('https://meet.google.com/')
    browser.find_element_by_xpath('/html/body/header/div[1]/div/div[3]/div[1]/div/span[1]/a').click()
    login_element = browser.find_element_by_xpath('//*[@id="identifierId"]')
    login_element.send_keys(email_id)
    browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
    time.sleep(10)
    password_element = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    password_element.send_keys(password)
    browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
    time.sleep(5)
    try :
        print("First Entering Method")
        browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]/div').click()
        time.sleep(10)
        meeting_element = browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input')
        meeting_element.send_keys(meeting_code)
        browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[4]/div[2]/div/span/span').click()
    except:
        print('Another Entering Method')
        meeting_element = browser.find_element_by_xpath('//*[@id="i3"]')
        meeting_element.click()
        time.sleep(3)
        meeting_element.send_keys(meeting_code)
        browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div[2]/div[2]/button/div[2]').click()
    time.sleep(10)
    browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div').click()
    browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div').click()
    browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()
    time.sleep(30)
    
    return browser

def count_meeting(browser):
    '''
    Input
    Browser object
    
    Output
    
    Count of People attending the meeting
    
    Description
    This function will helps to know the people in the meeting
    
    '''
    
    count_element = browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[4]/div/div[2]/div[2]/div[1]/div[1]/span/div/span[2]')
    
    return int(count_element.text.strip('()')) 


def captions(browser, adminUsername, offenders_count):
    # caption_element = browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]')

    # browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[3]/div[2]/div/span/span/div').click()
    # soup = BeautifulSoup(browser.page_source, 'html.parser')
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    mydivs = soup.findAll("div", {"class": "a4cQT xiCV9b"})

    try:
        for i in range(len(mydivs)):
            username = mydivs[i].find('div',{'class':'zs7s8d jxFHg'}).get_text()

            if username == adminUsername:
                continue

            print(username)
            print('*'*20)
            for k in range(len(mydivs[i].findAll('span',{'class':'CNusmb'}))):
                sentence = mydivs[i].findAll('span',{'class':'CNusmb'})[k].get_text()
                print(sentence)
                res, offenders_count = process_caption(browser, username, sentence, offenders_count)
                if res == True:
                    break
    except:
        print('Attribute Error')
    time.sleep(8) 
    
    return offenders_count

def chat_detect(browser, adminUsername):
    '''
    Input
    Browser Object
    
    Description:
    This function helps to detect chat messages more functionalities have to be added
        
    '''

    print("This is Chat Detect Function")
    node = Node()
    offenders_count = {}

    while(count_meeting(browser) > 1):
        offenders_count = captions(browser, adminUsername, offenders_count)
        browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[4]/div/div[2]/div[2]/div[1]/div[2]').click()
        node, offenders_count = process_data(browser, node, offenders_count)
        browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[4]/div/div[2]/div[2]/div[1]/div[2]').click()
        time.sleep(30)
    browser.quit()    
    return 

def extract_username(browser):

    browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[1]/div[3]/div/div[2]/div[1]').click()
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    adminUsername = soup.find('span', {'class' : 'ZjFb7c'}).get_text()
    return adminUsername
    
if __name__ == "__main__":
        
    chrome_options = Options()
    chrome_options.add_argument('use-fake-ui-for-media-stream')
    chrome_options.add_argument('use-fake-device-for-media-stream')
    chrome_options.add_argument('allow-file-access-from-files')
    
    browser = webdriver.Chrome(chromedriver_path,chrome_options=chrome_options)
    
    browser = enter_meeting(browser,email_id,password,'dii-svvp-zni')

    adminUsername = extract_username(browser)
    print(adminUsername)

    time.sleep(5)
    browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[4]/div/div[2]/div[2]/div[1]/div[2]').click()
    time.sleep(5)
    browser.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[3]/div[2]/div/span/span/div').click()
    #chat_detect(browser)
    chat_detect(browser, adminUsername)
    
