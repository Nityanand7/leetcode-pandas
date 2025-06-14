import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return (views[views['author_id'] == views['viewer_id']]
    .drop_duplicates(subset=['author_id'])
    .sort_values(by = 'author_id', ascending = True)[['author_id']]
    .rename(columns = {'author_id' : 'id' })
    )

// Alternate way

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    condition = views['author_id'] == views['viewer_id']
    df = list(views[condition]['author_id'].unique())
    df.sort()
    return pd.DataFrame({'id': df})
