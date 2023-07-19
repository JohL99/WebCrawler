from helpers import *  # noqa: F403
import config as cf  # noqa: F403
        
    
def main():
    """ with open('urls.txt', 'r') as f:
        for url in f:
            write(url) # noqa: F405
    f.close() """
    write("https://www.africanhut.com/collections/confectionary") # noqa: F405
    write("https://www.africanhut.com/collections/biscuits-cookies-and-snacks") # noqa: F405
    write("https://www.africanhut.com/collections/beverages") # noqa: F405
    write("https://www.africanhut.com/collections/breakfast") # noqa: F405
    write("https://www.africanhut.com/collections/baking-cooking-and-desserts") # noqa: F405
    write("https://www.africanhut.com/collections/jams-and-spreads") # noqa: F405
    write("https://www.africanhut.com/collections/bottled-sauces-and-condiments") # noqa: F405, E501
    write("https://www.africanhut.com/collections/dry-sauces-gravy-herbs-and-spices") # noqa: F405, E501
    write("https://www.africanhut.com/collections/canned-and-packaged-goods") # noqa: F405
    write("https://www.africanhut.com/collections/household-and-beauty") # noqa: F405
    write("https://www.africanhut.com/collections/apparel-novelties-and-kitchen-accessories") # noqa: F405, E501
    write("https://www.africanhut.com/collections/products-of-interest-to-south-africans") # noqa: F405, E501
    
    # send file in email
    message = '''
    
    Attached is the price list for African Hut.
    - this is an automated email
    '''
    sendEmail(cf.senderEmail, cf.SenderPassword, cf.receiverEmail, "Price List", message, "data.csv") # noqa: F405, E501
    print("Done")

main()