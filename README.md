# Twitter Scraper for Endangered Species

This is a Python-based project designed to scrape Twitter data related to endangered species using the Tweepy library. This data can be used for sentiment analysis, social media monitoring, natural language processing tasks, and more.

## Features

    Fetches tweets for a given list of species.
    Extracts tweet content, user information, and hashtags from each tweet.
    Handles Twitter's rate limits and API exceptions.
    Exports tweets to a Pandas DataFrame for easy data manipulation.

## Dependencies

This project requires specific Python libraries. All dependencies can be found in the requirements.txt file.

    To install these libraries, you can use pip:

    bash

    pip install -r requirements.txt

## Configuration

Before you run the script, you need to set up your Twitter Developer account and get your API keys. Once you have your keys, save them in a .env file as shown below:

    env

    API_KEY=your_twitter_api_key
    API_KEY_SECRET=your_twitter_api_key_secret
    ACCESS_TOKEN=your_twitter_access_token
    ACCESS_TOKEN_SECRET=your_twitter_access_token_secret

    The script will load this .env file and use the keys to authenticate with the Twitter API.

## Usage

The script reads the names of species from text files (e.g., 'Critically Endangered Species.txt', 'Possibly Extinct.txt', 'Vulnerable Species.txt'). For each species, it fetches the latest tweets containing that species name, excludes retweets, and stores the tweet data in a DataFrame.

The following information is collected for each tweet:

    User name
    User description
    User location
    User verification status
    Tweet creation date
    Tweet text
    Hashtags
    Source

The function get_tweet_df(species) receives a list of species names and fetches the tweets for each species. It then pauses for 12 seconds between each request to avoid hitting Twitter's rate limits.


## Disclaimer

    This project is intended for educational purposes only. Please use it responsibly and respect the privacy of others. It's also important to keep in mind that scraping large amounts of data from Twitter may violate their Terms of Service.
