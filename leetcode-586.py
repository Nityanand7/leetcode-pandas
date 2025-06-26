import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    cnt = orders['customer_number'].value_counts()
    top_cust = cnt[cnt == cnt.max()].index
    return pd.DataFrame({'customer_number': top_cust})

# Alternate way

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    order_count = orders.groupby('customer_number').size().reset_index(name='total_orders')
    return order_count.sort_values('total_orders', ascending=False).head(1)[['customer_number']]
