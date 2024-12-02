# You can extract the Redirect URLs from Google Search Engine. Install the following mention module and follow the Code.
# pip install google

from googlesearch import search

query = "Medium.com"

for url in search(query):
    print(url)
