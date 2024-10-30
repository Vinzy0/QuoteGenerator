import requests

category = 'happiness'
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)

#                                                       vvvvvvvvvvvvvvvvvvvvvvvvv
response = requests.get(api_url, headers={'X-Api-Key': 'PUT YOUR OWN API KEY HERE'})
#                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^

QuoteContainer = response.json()

quote = QuoteContainer[0]['quote']
author = QuoteContainer[0]['author']
category = QuoteContainer[0]['category']

print(f"Quote: {quote}")
print(f"Author: {author}")
print(f"Category: {category}")