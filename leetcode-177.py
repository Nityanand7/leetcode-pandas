import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee['rank'] = (
                        employee['salary']
                        .rank(method = 'dense', ascending = False)
                        .astype(int)
                        )
    candidates = employee.loc[employee['rank'] == N, 'salary'].unique()

    nth_sal = candidates[0] if len(candidates) > 0 else None

    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_sal]})

# Alternate

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee['rank'] = employee['salary'].rank(method='dense', ascending=False)
    nthsal = employee[employee['rank']==N]
    return pd.DataFrame({f'getNthHighestSalary({N})': [None if len(nthsal) == 0 
                                                else nthsal['salary'].iloc[0]]})
