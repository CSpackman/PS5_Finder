' #!/usr/bin/python3 '
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
import json
import time
import os
from twilio.rest import Client
from selenium.webdriver.chrome.options import Options
import sys


options = webdriver.ChromeOptions()
#options.add_argument('headless')


with open('/Users/connor/Documents/pS5_Finder/data.json') as f:
    data=json.load(f)

PhoneNumbers = ["+1 650-690-1491"]
finalMessege = "null"



client = Client(data['sid'], data["auth"])
driver = webdriver.Chrome(executable_path="//Users/connor/Documents/Ps5_Webscrapper/env/lib/python3.7/site-packages/chromium-browser/chromedriver", options=options)
#driver = webdriver.Chrome("//Users/connor/Documents/PS5_Webscrapper/env/lib/python3.7/site-packages/chromium-browser/chromedriver",)


def function_text(state):
    if state == True:
        if finalMessege != "null":
            for x in PhoneNumbers:
                message = client.messages.create(
                            body=finalMessege,
                            from_='+1 314 266 5161',
                            to=PhoneNumbers
                          )
    if state == False:
        print(finalMessege)


i = 1

while i<3:

    try:
        driver.get("https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG/ref=sr_1_3?dchild=1&keywords=ps5&qid=1607848248&sr=8-3")
        Amazon =  driver.find_element_by_xpath("//*[@id='availability']/span").text
        if Amazon != "Currently unavailable.":
            finalMessege = "\n Amazon status: "+Amazon
    except:
        finalMessege = "\nAmazon status: ERROR"
    try:
        driver.get("https://www.walmart.com/ip/Sony-PlayStation-5/363472942?irgwc=1&sourceid=imp_w-VV9Lz4TxyLU6-wUx0Mo36GUkE14GTJzTk%3AUw0&veh=aff&wmlspartner=imp_1719813&clickid=w-VV9Lz4TxyLU6-wUx0Mo36GUkE14GTJzTk%3AUw0&sharedid=&ad_id=565706&campaign_id=9383")
        Walmart =  driver.find_element_by_xpath("//*[@id='blitzitem-container']/div/div/div/div/text()[3]").text
        if Walmart != "While supplies last.":
            finalMessege = "\n Walmart status: "+Walmart
    except:
        finalMessege = "\nWalmart status: ERROR"

    try:
        driver.get("https://direct.playstation.com/en-us/hardware/ps5")
        PlayStationDirect = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[3]/hero-component/div/div/div[2]/hero-product-detail/div/div[3]/div[1]/p").text
        if PlayStationDirect != "Out of Stock":
            finalMessege = finalMessege+ "\nPlaystation status: "+PlayStationDirect
    except:
        #finalMessege = finalMessege+ " \nPlaystation status: ERROR"
        finalMessege=finalMessege

    try:
        driver.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149")
        BestBuy = driver.find_element_by_xpath("//*[@id='fulfillment-add-to-cart-button-34942baf-eed6-4550-a8fb-ceebfef765d2']/div/div/div/button").text
        if BestBuy != "Sold Out":
            finalMessege = finalMessege+ "\nBestBuy  status: "+BestBuy
    except:
       finalMessege = finalMessege+ " \nBestBuy: ERROR"
    try:
        driver.get("https://sites.google.com/view/connorstestsite/home")
        TestSite = driver.find_element_by_xpath("//*[@id='h.sxcc862lly1h']").text
        if TestSite == "My Test":
            finalMessege = finalMessege+ "\nTestSite  status: "+TestSite
    except:
        finalMessege = finalMessege+ " \nTestSite: ERROR"

   
    
    function_text(False)
        
    
    i +=1
    print("has run:")
    print(i)
    if i%10 == 0:
        runtime = "Program has run:"
        runtime = runtime + str(i)+ "times"

    
driver.close()
