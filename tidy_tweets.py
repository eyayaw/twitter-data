import json
import os
import pandas as pd
from utils import get_handles

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"


# Loads the twitter data for a user
# Returns the tweets, and user_info about the user
def load_tweets(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Combine chunks, ignore "meta" and "includes" objects
    tweets = []
    for item in data:
        tweets.extend(item.get("data", []))
    # Some info about the user
    user_info = data[0].get("includes", {}).get("users", [])[0]
    return tweets, user_info


def tidy_data(handle: str):
    handle = handle.removeprefix("@")
    tweets, _ = load_tweets(f"data/twitter-data/{handle}.json")
    data = []
    for tweet in tweets:
        tidy_tweet = {
            "tweet_link": f'https://twitter.com/{handle}/status/{tweet.get("id", "")}',
            "created_at": tweet.get("created_at", ""),
            "text": tweet.get("text", ""),
        }

        # Flatten public metrics
        public_metrics = tweet.get("public_metrics", {})
        tidy_tweet.update(public_metrics)

        # Process hashtags if present
        if "entities" in tweet:
            hashtags = [
                hashtag["tag"]
                for hashtag in tweet.get("entities", {}).get("hashtags", [])
            ]
            tidy_tweet["hashtags"] = ",".join(hashtags)

        # Tweet with media attachments
        if "attachments" in tidy_tweet:
            tidy_tweet["attachments"] = len(tweet["attachments"]["media_keys"])
        # Mentions
        tidy_tweet["mentions"] = ",".join(
            [
                mention["username"]
                for mention in tweet.get("entities", {}).get("mentions", [])
            ]
        )

        data.append(tidy_tweet)
    return data


if __name__ == "__main__":
    data_dir = "data/twitter-data/"
    tidy_data_dir = f"{data_dir}/tidy"
    handles = get_handles(data_dir)
    os.makedirs(tidy_data_dir, exist_ok=True)
    for handle in handles:
        _, user_info = load_tweets(f"{data_dir}/{handle}.json")
        tweets_df = pd.DataFrame(tidy_data(handle))
        tweets_df.to_csv(f"{tidy_data_dir}/{handle}.csv", index=False)