# backend/ingestion/reddit_fetcher.py
import praw
import os
from dotenv import load_dotenv
from datetime import datetime
from .mongo_client import collection

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="social-pulse-ai"
)

def fetch_reddit_posts(subreddits: list[str], limit: int = 10):
    for sub in subreddits:
        subreddit = reddit.subreddit(sub)
        for post in subreddit.hot(limit=limit):
            doc = {
                "platform": "reddit",
                "text": post.title + "\n\n" + (post.selftext or ""),
                "user": str(post.author),
                "timestamp": datetime.utcfromtimestamp(post.created_utc).isoformat(),
                "location": None,
                "topic": sub,
            }
            collection.insert_one(doc)
            print(f"Inserted Reddit post: {doc['text'][:50]}...")

# Example usage:
if __name__ == "__main__":
    fetch_reddit_posts(["technology", "apple"], limit=5)
