import csv
import requests
from bs4 import BeautifulSoup

# read urls into a list and return it
def read_urls():
    urls = []
    with open('urls.txt', 'r') as f:
        data = f.read()
    urls = data.split('\n')
    f.close()
    return urls

# build a dictionary of product names and prices
def buildDictionary(productName, productPrice, mainDic):
    mainDic[productName] = productPrice
    return mainDic
    
# write data to a file
def write(url):
    mainDic = scrape(url) # noqa: F405
    with open('data.csv', 'a', newline='') as f:
        f.write(url + '\n')
        writer = csv.writer(f)
        for key, value in mainDic.items():
            writer.writerow([key, value])
        f.write('\n' + "-"*15 + " end of section " + "-"*15 + '\n\n')
    f.close()

# get the product names and prices from a website
def scrape(url):
    
    mainDic = {}
    
    # Send a GET request to the website
    #url = "https://www.africanhut.com/collections/confectionary"
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the relevant elements containing product names and prices
    product_elements = soup.find_all("div", class_="exs-coll-list-prod-desc")

    # Extract the product name and price for each element
    for product in product_elements:
        name = product.find("h3").text.strip()
        priceElement = product.find("span", class_="product__price")
        
        if priceElement:
            priceText = priceElement.contents[-1].strip()
        else:
            priceElementNew = product.find("span", class_="product__price--on-sale")
            priceText = priceElementNew.contents[-1].strip()
        
        buildDictionary(name, priceText, mainDic)  # noqa: F405
    return mainDic

# send file with email
def sendEmail(sender_email, sender_password, receiver_email, subject, message, attachment_path):  # noqa: E501
    # imports
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(message, 'plain'))
    
    with open(attachment_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        
    encoders.encode_base64(part)
    
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachment_path}",
    )
    
    msg.attach(part)
    text = msg.as_string()
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    server.login(sender_email, sender_password)
    
    server.sendmail(sender_email, receiver_email, text)
    server.quit()
    print("Email sent successfully")
    
    