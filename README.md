# Twitch Clip Downloader
Simple script to download a clip from twitch.tv
The script will download the designed clip to the current folder

## Requirements

- Python 3.9+
- A Twitch Client ID, Client Secret and Access Token
-  ```pip install requirements.txt```

## Configuration
- Open ```keys.py``` and insert Client ID, Client Secret and Access Token
- If you need the Access Token, open ```main.py``` and call the function ```get_new_access_token()```

## Usage
- Open ```main.py``` and replace the current ```url``` value to the desired link