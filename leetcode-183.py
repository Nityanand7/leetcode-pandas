import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(customers, orders, left_on = 'id', right_on = 'customerId', how = 'left', suffixes = ('_cust', '_ord'))
    return df[df['id_ord'].isnull() == True][['name']].rename(columns = {'name': 'customers'})
