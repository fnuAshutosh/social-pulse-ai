# backend/ingestion/twitter_fetcher.py
import tweepy
import os
from dotenv import load_dotenv
from datetime import datetime
from .mongo_client import collection
import backoff

load_dotenv()

BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

client = tweepy.Client(bearer_token=BEARER_TOKEN)

class TwitterFetcher:
    def __init__(self):
        self.client = client
        self.collection = collection
        self.collection_name = "tweets"

    @backoff.on_exception(backoff.expo, tweepy.TooManyRequests, max_tries=5, jitter=backoff.full_jitter)
    def fetch_tweets(self, keyword: str, max_results: int = 10):
        print(f"Fetching tweets for keyword: {keyword}")
        # This call may trigger 429 errors; backoff will handle retries.
        # Add try catch block to handle exceptions 
        
        return client.search_recent_tweets(
            query=keyword,
            tweet_fields=["created_at", "geo", "lang", "author_id"],
            expansions=["author_id", "geo.place_id"],
            max_results=max_results
        )
