#
#       Automation of Membership Management for Socities of University College Dublin
#           By Hakeem Goloba
#               For the use of African Society(300+ members), Netsoc (400+ members) and C&E(3000+ members)

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import csv

def automate_society_members():

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    safe = True

    browser = webdriver.Chrome(executable_path='C:\Chrm\chromedriver.exe',chrome_options=options)
    browser.get('https://sisweb.ucd.ie/')

    #enter username with given key
    user=browser.find_element_by_css_selector('#UserName')
    user.send_keys('*******@ucdconnect.ie')

    #password
    password=browser.find_element_by_css_selector('#p_password')
    password.send_keys('********')

    #click the log in button
    login=browser.find_element_by_css_selector('input.menubutton')
    login.click()

    #click relevant navigations **UCD specific here but can be changed
    campus = browser.find_element_by_link_text('Campus')
    campus.click()

    club_management = browser.find_element_by_link_text('Club & Society Management')
    club_management.click()

    club_memebership = browser.find_element_by_link_text('Club & Society Membership')
    club_memebership.click()

    #csv file is opened and then used to load information
    with open("File.csv") as fil:
        reader = csv.reader(fil, delimiter=',')
        next(reader)

        print (reader)
        for x in reader:
            #socities were found by using the xpath on the Management page

            #Internet and Computer Science Socity
            #row = browser.find_element_by_xpath('//*[@id="SA200-1|2"]/td[5]/a')

            #C&E
            if(safe):
                row = browser.find_element_by_xpath('//*[@id="SA200-1|1"]/td[5]/a')
                row.click()

            #where student number will be entered

            student_number = browser.find_element_by_name('f_WSATMEMB_PIDM')
            student_number.send_keys(x)

            #name check must be clicked before student is saved to database
            check_name = browser.find_element_by_name('p_BUTTON')
            check_name.click()

            safe = True

            #save new member
            save = browser.find_element_by_css_selector('input.menubutton')
            save.click()

            #if member already exists in the SISWEB database clear the entry and run loop again
            try:
                browser.find_element_by_xpath('//*[@id="1"]/div[1]/div/input[3]').click()
                safe = False
            except NoSuchElementException:
                safe = True

#call function...sit back and relax
automate_society_members()
