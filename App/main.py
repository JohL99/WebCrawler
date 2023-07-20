from helpers import *  # noqa: F403
import secret as cf  # noqa: F403


def main():
    with open("urls.txt", "r") as f:
        for line in f:
            url = line.strip()
            write(url)  # noqa: F405
    
    # send file in email
    message = '''
    
    Attached is the price list for African Hut.
    
    To run this program on your local machine see: https://github.com/JohL99/WebCrawler
    
    - this is an automated email
    
    '''
    sendEmail(cf.senderEmail, cf.SenderPassword, cf.receiverEmail, "Price List", message, "data.csv") # noqa: F405, E501
    print("Done")
    
if __name__ == "__main__":
    main()