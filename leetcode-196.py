import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', inplace=True)
    person.drop_duplicates(subset=['email'], keep = 'first', inplace=True)

# Alternate method - without mutating the order

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    idx = person.groupby('email')['id'].idxmin()
    to_drop = person.index.difference(idx)
    person.drop(index=to_drop, inplace=True)
