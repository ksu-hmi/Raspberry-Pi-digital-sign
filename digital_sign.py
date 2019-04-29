
#import GPIO library
import RPi.GPIO as gpio
# Import Time Library
import time
#import URL Library
import urllib
#Import OS Library
import os

#import WebBrowser
import webbrowser

#variable for OS
browser='chromium'
 
# Will need to test that the pins are connected properly prior to uncommenting the functionality
#set gpio numbering mode and define input pin
gpio.setmode(gpio.BCM)
button1 = 4
button2 = 17
button3 = 2
button4 = 3
gpio.setup(button1,gpio.IN,pull_up_down=gpio.PUD_UP)
gpio.setup(button2,gpio.IN,pull_up_down=gpio.PUD_UP)
gpio.setup(button3,gpio.IN,pull_up_down=gpio.PUD_UP)
gpio.setup(button4,gpio.IN,pull_up_down=gpio.PUD_UP)

#gpio.setcfg(port.1, gpio.INPUT)
#gpio.pullup(port.1, gpio.PULLUP)
    
try:
    print ("Please press a button (1-4) to pull up a report.")
    while True:
        if gpio.input(button1) == False:
            print("Button 1 was Pressed")
            time.sleep(2)
            os.system("pkill "+browser)
            webbrowser.open('http://www.yahoo.com')
    #       while true:
    #       time.sleep(300)
    #       driver.refresh()
        elif gpio.input(button2) == False:
            print("Button 2 was Pressed")
            time.sleep(2)
            os.system("pkill "+browser)
            webbrowser.open('http://www.cnn.com')
    #        while true:
    #            time.sleep(300)
    #            driver.refresh()
        elif gpio.input(button3) == False:
            print("Button 3 was Pressed")
            time.sleep(2)
            os.system("pkill "+browser)
            webbrowser.open('http://www.anotherwebsite.com')
    #        while true:
    #            time.sleep(300)
    #            driver.refresh()
        elif gpio.input(button4) == False:
            print("Button 4 was Pressed")
            time.sleep(2)
            os.system("pkill "+browser)
            webbrowser.open('http://www.alsoanotherwebsite.com')
    #        while true:
    #            time.sleep(300)
    #            driver.refresh()
    
    #driver.quit()

finally:
    # cleanup the GPIO pins before ending
    print("cleaning up")
    gpio.cleanup()





