# News Summarizer and Tweeter

This projects uses OpenAI and Twitter APIs to generate and post summaries of news articles from different countries and categories.

## Features

- Fetch news articles from the NewsData API, which provides access to over 30,000 sources from 200 countries.
- Store the title, link, date, content and summary of each article in a Firebase database.
- Generate summaries of the content using OpenAI's text-babbage-001 engine.
- Post summaries and links on Twitter using the Twitter API.
- Handle different status codes from the Twitter API such as 200 (success), 401 (token expired), 400 (text too long) and others.
- Obtain new access token and refresh token from Twitter if the token expires.
- Reduce the length of the text if it is too long for a tweet.

## Technologies

- Python 3.9
- Requests
- NLTK
- Hashlib
- Base64
- Urllib
- JSON
- OS
- OpenAI
- Firebase Admin
