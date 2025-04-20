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

    def store_tweets(self, tweets):
        if not tweets.data:
            print("No tweets found.")
            return

        for tweet in tweets.data:
            # Check if the tweet already exists in the database
            # existing_tweet = self.collection.find_one({"id": tweet.id})
            # if existing_tweet:
            #     print(f"Tweet {tweet.id} already exists in the database.")
            #     continue

            # Prepare the tweet data for storage
            tweet_data = {
                "id": tweet.id,
                "text": tweet.text,
                "created_at": tweet.created_at,
                "author_id": tweet.author_id,
                "geo": tweet.geo,
                "lang": tweet.lang,
                "place_id": tweet.place_id,
                "timestamp": datetime.utcnow()
            }

            # Insert the tweet into the database
            self.collection.insert_one(tweet_data)
        
        return f"{len(tweets.data)} Tweets stored successfully."