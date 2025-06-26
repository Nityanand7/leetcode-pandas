import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    cnt = orders['customer_number'].value_counts()
    top_cust = cnt[cnt == cnt.max()].index
    return pd.DataFrame({'customer_number': top_cust})
