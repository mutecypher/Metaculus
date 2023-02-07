from bs4 import BeautifulSoup
import requests
import urllib.request
import pandas as pd
import numpy as np
# The URL of the page we want to scrape
predictions = "https://www.metaculus.com/mutecypher/predictions/"

stuff = {"rankings": "https://www.metaculus.com/api2/rankings/",
         "users": "https://www.metaculus.com/api2/users/",
         "user-profiles": "https://www.metaculus.com/api2/user-profiles/",
         "notifications": "https://www.metaculus.com/api2/notifications/",
         "categories": "https://www.metaculus.com/api2/categories/",
         "questions": "https://www.metaculus.com/api2/questions/",
         "comments": "https://www.metaculus.com/api2/comments/",
         "predictions": "https://www.metaculus.com/api2/predictions/",
         "contests": "https://www.metaculus.com/api2/contests/",
         "reminders": "https://www.metaculus.com/api2/reminders/",
         "bulletins": "https://www.metaculus.com/api2/bulletins/",
         "tutorials": "https://www.metaculus.com/api2/tutorials/",
         "news-comments": "https://www.metaculus.com/api2/news-comments/",
         "projects": "https://www.metaculus.com/api2/projects/",
         "organizations": "https://www.metaculus.com/api2/organizations/",
         "projectstats": "https://www.metaculus.com/api2/projectstats/",
         "tezos": "https://www.metaculus.com/api2/tezos/"}


url = "https://www.metaculus.com/questions/"
values = {'username': 'mutecypher',
          'password': 'fytri8-zenkag-fixRer'}
# https://www.metaculus.com/questions/

# Make a request to the websitehttps://www.metaculus.com/questions/

##

# session = requests.Session()

# Retrieve the login page to get the authenticity_token
login_url = 'https://metaculus.com/questions/'
# login_page = session.get(login_url)

# Extract the authenticity_token from the login page
# authenticity_token = extract_token_from_login_page(login_page.text)

# Prepare the login credentials
payload = {
    'username': 'mutecypher',
    'password': 'fytri8-zenkag-fixRer'
    # 'authenticity_token': authenticity_token
}

# Send the POST request to login
# session.post(login_url, data=payload)

# Now you are logged in and can make authenticated requests
# response = session.get('https://metaculus.com/questions/')


response = requests.get(url)

# print("the response is ", response.content)
# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the question links on the page
np.savetxt("predictions.txt", soup, fmt="%s")


a_tags = soup.find_all("a")

print(a_tags)
for tag in a_tags:
    print(tag['href'])
