# Instagram-API-ETL
python-instagram

A Python 2/3 client for the Instagram REST API

# Script Objective:
The objective of this script was to scrape data via the recent media enpoint API and time stamp to append to a mysql database.

# Installation:

pip install python-instagram

Instagram API uses the OAuth2 protocol for authentication, but not all functionality requires authentication. See the docs for more information: http://instagram.com/developer/authentication/

# Obtaining an access token

If you're using a method that requires authentication and need an access token, you can 
use the URL in the Instagram API ETL Automation.ipynb file (listed below as well) to obtain an access token for yourself. 
It will require your app's Client ID and Redirect URI, which then will give you an access toke in the same broswer you used. 

```
Authorization URL to get access token: 'https://api.instagram.com/oauth/authorize/?client_id=[ENTER CLIEND ID HERE]&redirect_uri=[ENTER REDIRECT-URI HERE]&response_type=token'
```
