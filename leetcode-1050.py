import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    cond = (
        actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='cooperated')
    )
    result = cond.loc[cond['cooperated'] >= 3, ['actor_id', 'director_id']]
    return result
    
