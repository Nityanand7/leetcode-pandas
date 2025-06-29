import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = (accounts['income'] < 20000).sum()
    avg = ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum()
    high = (accounts['income'] > 50000).sum()

    return pd.DataFrame(
        {
            'category':       ['Low Salary', 'Average Salary', 'High Salary'],
            'accounts_count': [low, avg, high]
        }
    )

# using len

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = len(accounts[accounts['income'] < 20000])
    avg = len(accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)])
    high = len(accounts[accounts['income'] > 50000])

    return pd.DataFrame(
        {
            'category':       ['Low Salary', 'Average Salary', 'High Salary'],
            'accounts_count': [low, avg, high]
        }
    )
