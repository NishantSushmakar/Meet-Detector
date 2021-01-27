from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from key import get_score
from remove_user import remove_user
from language import cvt_to_en

class Node:
    def __init__(self):
        self.prev = 0
        self.sents = 0

def process_data(browser, node) -> Node:
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    mydivs = soup.findAll("div", {"class": "GDhqjd"})
    try :
        for k in range(node.prev, len(mydivs)):
            username = mydivs[k].find("div",{"class":"YTbUzc"}).get_text()
            print(username)
    
            arr = mydivs[k].find_all("div",{'class':'oIy2qc'})
    
            start = (node.sents) if (k == node.prev) else 0 
    
            for ind in range(start, len(arr)):
                try :
                    score = get_score(arr[ind].get_text())
                    print(arr[ind].get_text(),score)
                    if score >= 0.9:
                        remove_user(username, browser)
                        
                except :
                    try:
                       text = cvt_to_en(arr[ind].get_text()) 
                       score = get_score(text)
                       print(text,score)
                       if score >= 0.9:
                          remove_user(username, browser)
                    except:   
                        print('Not Supported error')
            print("*"*20)
    
        node.prev = len(mydivs) - 1
        if (len(mydivs) != 0):
            node.sents = len(mydivs[-1].find_all("div",{'class':'oIy2qc'}))
    except :
         print('Index Error')           
    time.sleep(30)
    return node