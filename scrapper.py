import requests
from bs4 import BeautifulSoup
import smtplib # send emails
import time

#URL = "https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q/ref=sr_1_1_sspa?dchild=1&keywords=apple+airpods&qid=1592364347&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNTlGS0xQTFFDSDlRJmVuY3J5cHRlZElkPUEwNTk3OTQ5MTgxRlE4V0ZGWVFaMiZlbmNyeXB0ZWRBZElkPUEwMzA4NzczMkMyM1hTQVYyRjFMVyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

URL = input("Link of the Amazon product you want to price track: \n")
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find(id="productTitle").get_text()
print("\n" + title.strip() + "\n")

targetPrice = int(input("Your Budget: "))

emailSent = 1

def checkPrice():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:])

    if (converted_price <= targetPrice):
        send_email()

def send_email():
    global emailSent
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text() # get title of item

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('abc@gmail.com', 'sghmgsiexkydlosn')
    subject = "Price fell down!"
    body = "Item (%s) is within your budget! \n\nCheck the link: %s" % (title.strip(), URL)

    msg = "Subject: %s\n\n%s"  % (subject, body)

    server.sendmail('abc@gmail.com', 'hungjonathan@gmail.com', msg)

    print("Check your email!")
    emailSent = 0

    server.quit()


while(True):
    checkPrice()
    if (emailSent == 0): #if email has already been sent
        break
    else:
        print("Sorry! Not within budget. Will Try tomorrow.")
        time.sleep(60 * 60 * 24)
