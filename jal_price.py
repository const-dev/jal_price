from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException
import datetime
import time
import re
import smtplib
import getpass


def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message, login, password, smtpserver):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems


class GMail_Notifier(object):
    def __init__(self,
                 gmail_account,
                 password,
                 to_addr,
                 cc_addr_list=(),
                 smtpserver='smtp.gmail.com:587'):
        self.login = gmail_account
        self.password = password
        self.from_addr = gmail_account
        self.to_addr_list = [to_addr]
        self.cc_addr_list = cc_addr_list
        self.smtpserver = smtpserver

    def email(self, subject='', message=''):
        sendemail(from_addr=self.from_addr,
                  to_addr_list=self.to_addr_list,
                  cc_addr_list=self.cc_addr_list,
                  subject=subject,
                  message=message,
                  login=self.login,
                  password=self.password,
                  smtpserver=self.smtpserver)


def main():
    gmail_account = raw_input('gmail account: ')
    password = getpass.getpass('password: ')
    to_addr = raw_input('send to email address: ')

    gmail_notifier = GMail_Notifier(gmail_account, password, to_addr)
    gmail_notifier.email('gmail test')

    driver = webdriver.Chrome()
    #driver = webdriver.PhantomJS('phantomjs')

    driver.get('http://www.tw.jal.com/twl/en/')

    xpath_one_way = './/input[@type="radio" and @value="O"]'
    WebDriverWait(driver, 180).until(
            EC.presence_of_element_located((By.XPATH, xpath_one_way)))

    driver.find_element_by_xpath(xpath_one_way).click()

    xpath_from = '//select[@name="B_LOCATION_1"]/option[@value="TPE"]'
    WebDriverWait(driver, 180).until(
            EC.presence_of_element_located((By.XPATH, xpath_from)))
    driver.find_element_by_xpath(xpath_from).click()

    xpath_to_country = '//select[@name="E_AREA"]/option[@value="USA_12"]'
    WebDriverWait(driver, 180).until(
            EC.presence_of_element_located((By.XPATH, xpath_to_country)))
    driver.find_element_by_xpath(xpath_to_country).click()

    xpath_to_city = '//select[@name="E_LOCATION_1"]/option[@value="BOS"]'
    WebDriverWait(driver, 180).until(
            EC.presence_of_element_located((By.XPATH, xpath_to_city)))
    driver.find_element_by_xpath(xpath_to_city).click()


    xpath_month = '//select[@name="B_MONTH"]/option[@value="8"]'
    WebDriverWait(driver, 180).until(
            EC.presence_of_element_located((By.XPATH, xpath_month)))
    driver.find_element_by_xpath(xpath_month).click()

    xpath_day = '//select[@name="B_DAY"]/option[@value="13"]'
    WebDriverWait(driver, 180).until(
            EC.presence_of_element_located((By.XPATH, xpath_day)))
    driver.find_element_by_xpath(xpath_day).click()

    main_window_handle = driver.current_window_handle

    while True:
        id_next = 'next0_2'
        WebDriverWait(driver, 180).until(
                EC.presence_of_element_located((By.ID, id_next)))
        driver.find_element_by_id(id_next).submit()

        WebDriverWait(driver, 180).until(
                lambda driver: len(driver.window_handles) > 1)

        for handle in driver.window_handles:
            if handle == main_window_handle:
                continue
            driver.switch_to_window(handle)
            xpath_table = '//table[@id="table0"]'
            WebDriverWait(driver, 180).until(
                    EC.presence_of_element_located((By.XPATH, xpath_table)))
            table = (driver.find_element_by_xpath(xpath_table)
                           .get_attribute('innerHTML'))

            print datetime.datetime.now()
            candidate = []
            for item in re.findall('<td.*?>(.*?)</td>', table):
                date, price = None, None
                m = re.search('<time class="date" datetime="">\s*(.*?)\s*</time>', item)
                if m:
                    date = m.group(1)
                m = re.search('<span class="number">\s*(.*?)\s*</span>', item)
                if m:
                    price = m.group(1)
                if date is not None and price is not None:
                    print date, price
                    try:
                        pricef = float(price.replace(',', ''))
                        if pricef < 40000:
                            candidate.append('%s: %s' % (date, price))
                    except:
                        pass

            if len(candidate) > 0:
                gmail_notifier.email('JAL price alert', '; '.join(candidate))

            driver.close()

        driver.switch_to_window(main_window_handle)
        time.sleep(1200)
        print


if __name__ == '__main__':
    main()
