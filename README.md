# Web Crawler

Web crawler will go through the AfricanHut product pages and extract the names and prices of the products.
## Usage

1. Navigate to the folder 'WebCrawler' in the terminal 
2. Run 'pip install -r requirements.txt' from the directory WebCrawler
3. Run 'python App/main.py' from the directory WebCrawler

## Requirements

1. python
2. pip

## Sample launch.json

    {
        // Use IntelliSense to learn about possible attributes.
        // Hover to view descriptions of existing attributes.
        // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal",
                "cwd": "${workspaceFolder}/App",
                "justMyCode": true
            }
        ]
    }
