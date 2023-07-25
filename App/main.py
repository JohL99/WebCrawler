from helpers import *  # noqa: F403
import config as cf  # noqa: F403
import os



def main():
    filePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "urls.txt")
    with open(filePath, "r") as f:
        for line in f:
            url = line.strip()
            write(url)  # noqa: F405
    
    # send file in email
    message = '''
    
    Attached is the price list for African Hut.
    
    To run this program on your local machine see: https://github.com/JohL99/WebCrawler
    
    - this is an automated email
    
    '''
    sendEmail(cf.senderEmail, cf.senderPassword, cf.receiverEmail, "Price List", message, "data.csv") # noqa: F405, E501
    print("Done")
    
if __name__ == "__main__":
    main()