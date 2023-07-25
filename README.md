# Web Crawler

Web crawler will go through the AfricanHut product pages and extract the names and prices of the products.
## Usage

1. Navigate to the folder `WebCrawler/` in the terminal 
2. Run `docker build -t <image name here> .` from the directory WebCrawler
3. Run `docker run --env-file .env test` from the directory WebCrawler

## Secrets

In the `WebCrawler` directory create and modify a file called `.env` with the following data format:

    SENDER_EMAIL=sender@mail.com
    SENDER_PASSWORD=password here
    RECEIVER_EMAIL=receiver@mail.com

For the sender password field, when using gmail, generate a google app password.<br>
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
