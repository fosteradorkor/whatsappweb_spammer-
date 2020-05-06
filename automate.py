from selenium import webdriver
import time

number = 1000000000
count = 1

driver_path ='chromedriver.exe'
recipient_name = 'recipient_name'

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(driver_path, options=options)

driver.get('https://web.whatsapp.com/')

input('Press enter after you scan the qr:')

sb = driver.find_element_by_xpath('//span[@title = "{}"]'.format(recipient_name))

sb.click()


def sendMsg():
    msg_box = driver.find_element_by_class_name('_1Plpp')
    msg_box.send_keys('message {}: TELL MEEEE!!!!!!'.format(str(count)))
    send_btn = driver.find_element_by_class_name('_35EW6')
    send_btn.click()


while count <= number:
    try:
        sendMsg()
        print(1)
        count = count + 1
        time.sleep(1)
    except:
        print('new exception')
