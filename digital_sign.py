python3 -m pip install --user selenium
#import GPIO library
import rpi.gpio as gpio

#import URL Library
import urllib

#import WebBrowser
import webbrowser

# import Selenium
from selenium import webdriver
import time

# browser = webdriver.chrome(executable_path = 'filepathhere')
# browser.get('https://www.google.com')
# browser.close()
 

#set gpio numbering mode and define input pin

gpio.setcfg(port.1, gpio.INPUT)
gpio.pullup(port.1, gpio.PULLUP)
while true:
    if gpio.input(1) != 0:
        webbrowser.close()
        webbrowser.open('http://www.yahoo.com')
        while true:
            time.sleep(300)
            driver.refresh()
    elif gpio.input(2) != 0:
        webbrowser.close()
        webbrowser.open('http://www.cnn.com')
        while true:
            time.sleep(300)
            driver.refresh()
    elif gpio.input(3) != 0:
        webbrowser.close()
        webbrowser.open('http://www.anotherwebsite.com')
        while true:
            time.sleep(300)
            driver.refresh()
    elif gpio.input(4) != 0:
        webbrowser.close()
        webbrowser.open('http://www.alsoanotherwebsite.com')
        while true:
            time.sleep(300)
            driver.refresh()
    else:
        print "Please press a button to pull up a report"
driver.quit()
# cleanup the GPIO pins before ending
GPIO.cleanup()





