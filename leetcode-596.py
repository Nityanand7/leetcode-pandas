import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    cnt = courses.groupby('class', as_index=False)['student'].count()
    return cnt.loc[cnt['student']>4, ['class']]

# Using size()

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    res = courses.groupby('class').size().reset_index(name='students')
    return res.loc[res['students']>4, ['class']]


