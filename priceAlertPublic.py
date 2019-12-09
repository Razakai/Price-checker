import requests
from bs4 import BeautifulSoup
import time
import smtplib


def checkprice():

    URL = "https://www.amazon.co.uk/" \
          "Lacoste-2010871-Mens-Watch/dp/B01KNHQ4V8/ref=sr_1_5?keywords=mens+watch&qid=1568583110&sr=8-5"

    headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'} // firefox user agent info

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')  # retrieves html file of web page

    title = soup.find(id="productTitle").get_text()  # gets name of product
    priceStr = soup.find(id="priceblock_ourprice").get_text()  # gets price,
    priceInt = float(priceStr[1:6])
    print(title.strip(), priceInt, sep="\n")

    if priceInt < 90:  # if under 90 euro send email
        sendmail()


def sendmail():
    server = smtplib.SMTP("smtp.gmail.com", 587)  # creates a connection to use smpt protocol
    server.ehlo()  # initiate smpt conversation with server
    server.starttls()  # starts transport layer security

    server.login("bla@gmail.com", "app password")  # email and app password
    subject = "Price fell down"
    body = "You should buy this now: https://www.amazon.co.uk/Lacoste-2010871-Mens-Watch/dp/B01KNHQ4V8/ref=sr_1_5?keywords=mens+watch&qid=1568583110&sr=8-5"
    msg = f"Subject: {subject}\n\n{body}"  # formatting message
    server.sendmail(
        "bla@gmail.com",  # sender
        "bla@gmail.com",  # receiver
        msg  # message
    )
    print(msg)
    server.quit()


sendmail()



