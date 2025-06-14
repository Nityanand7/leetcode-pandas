import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    area = 3000000
    pop = 25000000
    return world[(world['area'] >= area) | (world['population'] >= pop)][['name', 'population', 'area']]
