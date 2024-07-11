import json
import os
from datetime import datetime, date as Date
from apify_client import ApifyClient
from glob import glob
from utils import validate_date, get_handles

# https://docs.apify.com/platform/actors/running


def get_last_date(handle: str):
    handle = handle.removeprefix("@")
    with open(f"./data/twitter-data/{handle}.json", "r") as f:
        data = json.load(f)
    try:
        created_at = data[0]["data"][0]["created_at"]
        created_at = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%fZ").date()
    except (KeyError, IndexError) as e:
        raise KeyError(f"Key or index error for handle: {handle}")
    return created_at


def scrape_posts(
    apify_client, page_name: str, start_date=None, end_date=None, limit=1000
):
    if start_date:
        start_date = validate_date(start_date)
    if end_date:
        end_date = validate_date(end_date)

    handle = ["@" + page_name.removeprefix("@")]
    input = {
        "addUserInfo": True,
        "handle": handle,
        "maxRequestRetries": 6,
        "maxTweets": limit,
        "maxTweetsPerQuery": 1000,
        "scrapeTweetReplies": True,
        "searchMode": "live",
        "sinceDate": validate_date(start_date),
        "untilDate": validate_date(end_date),
    }
    actor_run = apify_client.actor("microworlds/twitter-scraper").call(
        run_input={k: v for k, v in input.items() if v}
    )
    return actor_run


# Fetch scraped results from the Actor's dataset.
def fetch_dataset(apify_client, actor_run):
    dataset_items = (
        apify_client.dataset(actor_run["defaultDatasetId"]).list_items().items
    )
    return dataset_items


def main():
    api_key = os.environ["APIFY_API_TOKEN"]
    apify_client = ApifyClient(api_key)

    data_dir = os.path.join("./data/", "apify")
    os.makedirs(data_dir, exist_ok=True)

    handles = get_handles("data/twitter-data/")
    # done = get_handles("data/apify/")
    # done = [x.split("_tweets")[0] for x in done]
    # handles = [h for h in handles if h not in done]
    for handle in handles:
        start = get_last_date(handle)
        end = datetime.today().date()
        run = scrape_posts(
            apify_client, handle, start_date=start, end_date=end, limit=5000
        )

        dataset = fetch_dataset(apify_client, run)
        with open(f"{data_dir}/{handle}_tweets_{start}_{end}.json", "w") as f:
            json.dump(dataset, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
