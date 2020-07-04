#this program is to send the whats up messages automatically to a person 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome('C:\manual file\chromedriver') 
driver.implicitly_wait(120)

print('NOTE: enter the name as per your contact list else enter the contact number ')
name=input('input the name or number of the person ')
message=input('enter the message to be sent ')
number_of_messages = int(input('input how many copies of messages to be sent '))

driver.get("https://web.whatsapp.com/")
inputElement = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
inputElement.send_keys(name)
inputElement.send_keys(Keys.ENTER)

mesage_box = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
for i in range(1,number_of_messages):
    mesage_box.send_keys(message)
    mesage_box.send_keys(Keys.ENTER)