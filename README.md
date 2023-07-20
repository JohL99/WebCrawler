# Web Crawler

Web crawler will go through the AfricanHut product pages and extract the names and prices of the products.
## Usage

1. Navigate to the folder `WebCrawler` in the terminal 
2. Run `pip install -r requirements.txt` from the directory WebCrawler
3. Run `python App/main.py` from the directory WebCrawler

## Secrets

In the `App` directory create a file called `config.py` with the following data:

{
    senderEmail = "Sender@mail.com"
    SenderPassword = "Sender password here"
    receiverEmail = "Receives@mail.com"
}

For the sender password field, when using gmail, generate a google app password.
Instructions can be found here: https://support.google.com/accounts/answer/185833

## Requirements

1. python
2. pip

## Sample launch.json

    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: launch",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal",
                "cwd": "${workspaceFolder}/App",
                "justMyCode": true
            }
        ]
    }
