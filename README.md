# Raspberry Pi digital sign
Purpose:The purpose of this project is to create a digital sign that will serve as a monitor in a business setting. 

Business Application: This digital sign will be displayed on a monitor or digital TV using an HDMI cable connected to a Raspberry Pi. This Raspberry Pi will have Ubutu loaded on it as an operating system. Connected to this Raspberry Pi will be a push button pad that will call a specific report in real time upon the button being pressed. Each of the four buttons will call a specific report from a web-based server that is needed for business purposes. The report will continue to pull at regular intervals (every 5-10 minutes) until the business day has ended (designed to run Mon - Fri 8A EST - 5 PM EST)

The Code:
There will need to be a Python program that is constantly listening for the input of a button to be pressed. Upon the pressing of a specific button, a pre-specified website will need to be called. This will allow the report to be displayed and regularly updated (at 5 minute intervals) until another button is pressed or the end of the business day arrives. 
Button 1  - will call a overall developers KanBan board
Button 2 - will call production volume processed for a pre-specified client. 
Button 3 - will call a health status report of common failure points of pre-specified client. 
Button 4 - Will call a report that allows management to see the overall status of current sites that are being implemented and are in the process of onboarding. 

There will be 4 tabs that are actively running in the background at all times. As part of this, the program will need to pull up a specific tab that corresponds to the button as definied above. 

Security:
Due to the nature of this information that will be displayed on this digital signage, there will need to be an RDP session that will be installed utilizing Ubuntu. This will help to keep the business sensitive information in a specific site. 

Hardware Requirements: 
In addition to the monitor to display, the Raspberry Pi will first need to have an operating system installed on a microSD chip. For testing, this is necessary to have a breadboard attached to properly restrict the power flow to the membranes. Although this can be done with built-in software on the Rasberry Pi, in order to prevent damage, we will install physical resistors just to ensure the longevity of the finished product. 
