from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from key import get_score
from remove_user import remove_user, issue_warning
from language import cvt_to_en

class Node:
    def __init__(self):
        self.prev = 0
        self.sents = 0

def process_caption(browser, username, sentence, offenders_count):

    ''' This will process each caption '''
    try :
        score = get_score(sentence)
        
        if score >= 0.9:
            remove_user(username, browser)
            return True, offenders_count
        elif score >= 0.85:
            if username not in offenders_count.keys():
                offenders_count[username] = 1
                issue_warning(username, browser)
            else:
                remove_user(username, browser)
                return True, offenders_count
    except :
        try:
            text = cvt_to_en(sentence) 
            score = get_score(text)
            print(text,score)
            if score >= 0.9:
                remove_user(username, browser)
                return True, offenders_count
            elif score >= 0.85:
                if username not in offenders_count.keys():
                    offenders_count[username] = 1
                    issue_warning(username, browser)
                else:
                    remove_user(username, browser)
                    return True, offenders_count
        except:   
            print('Not Supported error')

    return False, offenders_count
    
def process_data(browser, node, offenders_count) -> Node:
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
                    elif score >= 0.85:
                        if username not in offenders_count.keys():
                            offenders_count[username] = 1
                            issue_warning(username, browser)
                        else:
                            remove_user(username, browser)
                except :
                    try:
                        text = cvt_to_en(arr[ind].get_text()) 
                        score = get_score(text)
                        print(text,score)
                        if score >= 0.9:
                            remove_user(username, browser)
                        elif score >= 0.85:
                            if username not in offenders_count.keys():
                                offenders_count[username] = 1
                                issue_warning(username, browser)
                            else:
                                remove_user(username, browser)
                    except:   
                        print('Not Supported error')
            print("*"*20)
    
        node.prev = len(mydivs) - 1
        if (len(mydivs) != 0):
            node.sents = len(mydivs[-1].find_all("div",{'class':'oIy2qc'}))
    except :
         print('Index Error')           
    
    return node, offenders_count
