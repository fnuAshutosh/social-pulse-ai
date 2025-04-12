from fastapi import FastAPI
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from backend.ingestion.twitter_fetcher import TwitterFetcher

load_dotenv()

app = FastAPI()

client = MongoClient(os.getenv("MONGO_URI"))
db = client.social_pulse

tweets_collection = db.tweets


@app.get("/")
async def root():
    return {"message": "Social Pulse API"}



@app.get("/health")
def health_check():
    try:
        # Check if the database connection is alive
        client.admin.command('ping')
        return {"status": "OK"}
    except Exception as e:
        return {"status": "Error", "message": str(e)}
    

#Get lastest tweets
@app.get("/tweets/latest")
def get_latest_tweets(limit: int = 15):
    try:
        # Fetch the latest tweets from the collection
        latest_tweets = list(tweets_collection.find().sort("timestamp", -1).limit(limit))
        return {"latest_tweets": latest_tweets}
    except Exception as e:
        return {"status": "Error", "message": str(e)}
    


#Trigger tweet fetching (manual)
@app.post("/tweets/fetch") 
def fetch_tweets(keyword:str, max_results:int = 10):
    #Call the fetch_tweets function from the TwitterFetcher class
    new_tweets = TwitterFetcher().fetch_tweets(keyword, max_results)

    if new_tweets: 
        tweets_collection.insert_many(new_tweets)
        return {"status": "success", "message": f"Fetched {len(new_tweets)} new tweets."}
    else:
        return {"status": "error", "message": "No new tweets found."}
