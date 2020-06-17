import requests
from bs4 import BeautifulSoup
import smtplib # send emails
import time

URL = "https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q/ref=sr_1_1_sspa?dchild=1&keywords=apple+airpods&qid=1592364347&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNTlGS0xQTFFDSDlRJmVuY3J5cHRlZElkPUEwNTk3OTQ5MTgxRlE4V0ZGWVFaMiZlbmNyeXB0ZWRBZElkPUEwMzA4NzczMkMyM1hTQVYyRjFMVyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}


def checkPrice():
    page = requests.get(URL, headers=headers)
    # returns all the data from URL

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:])

    if (converted_price < 200):
        send_email()
    print(converted_price)
    print(title.strip())

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('hungjonathan@gmail.com', 'sghmgsiexkydlosn')
    subject = "Price fell down!"
    body = "Check the link: https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q/ref=sr_1_1_sspa?dchild=1&keywords=apple+airpods&qid=1592364347&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNTlGS0xQTFFDSDlRJmVuY3J5cHRlZElkPUEwNTk3OTQ5MTgxRlE4V0ZGWVFaMiZlbmNyeXB0ZWRBZElkPUEwMzA4NzczMkMyM1hTQVYyRjFMVyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

    msg = "Subject: %s\n\n%s"  % (subject, body)

    server.sendmail('hungjonathan@gmail.com', 'hungjonathan@gmail.com', msg)

    print("EMAIL HAS BEEN SENT")

    server.quit()

while(True):
    checkPrice()
    time.sleep(60 * 60 * 24)