#python3 -m pip install --user selenium
#import GPIO library
import rpi.gpio as gpio
import time
#import URL Library
#import urllib

#import WebBrowser
#import webbrowser

# import Selenium
#from selenium import webdriver


# browser = webdriver.chrome(executable_path = 'filepathhere')
# browser.get('https://www.google.com')
# browser.close()
 
# Will need to test that the pins are connected properly prior to uncommenting the functionality
#set gpio numbering mode and define input pin
gpio.setmode(GPIO.BCM)
button1 = 17
button2 = 4
button3 = 3
button4 = 2
gpio.setup(button1,gpio.IN,pull_up_down=gpio.PUD_UP)
gpio.setup(button2,gpio.IN,pull_up_down=gpio.PUD_UP)
gpio.setup(button3,gpio.IN,pull_up_down=gpio.PUD_UP)
gpio.setup(button4,gpio.IN,pull_up_down=gpio.PUD_UP)

#gpio.setcfg(port.1, gpio.INPUT)
#gpio.pullup(port.1, gpio.PULLUP)
try:
    print "Please press a button (1-4) to pull up a report."
    while True:

        if gpio.input(button1) == False:
             print("Button 1 was Pressed")
    #        webbrowser.close()
    #        webbrowser.open('http://www.yahoo.com')
    #        while true:
    #            time.sleep(300)
    #            driver.refresh()
        elif gpio.input(button2) == False:
            print("Button 2 was Pressed")
    #        webbrowser.close()
    #        webbrowser.open('http://www.cnn.com')
    #        while true:
    #            time.sleep(300)
    #            driver.refresh()
        elif gpio.input(button3) == False:
            print("Button 3 was Pressed")
    #        webbrowser.close()
    #        webbrowser.open('http://www.anotherwebsite.com')
    #        while true:
    #            time.sleep(300)
    #            driver.refresh()
        elif gpio.input(button4) == False:
            print("Button 4 was Pressed")
    #        webbrowser.close()
    #        webbrowser.open('http://www.alsoanotherwebsite.com')
    #        while true:
    #            time.sleep(300)
    #            driver.refresh()
    
    #driver.quit()

finally:
    # cleanup the GPIO pins before ending
    print("cleaning up")
    gpio.cleanup()





