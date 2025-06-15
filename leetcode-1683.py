import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalid = tweets['content'].astype(str).str.len() > 15
    return tweets.loc[invalid, ['tweet_id']]
