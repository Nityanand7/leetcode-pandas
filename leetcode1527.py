import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    diab1 = patients['conditions'].str.contains(r'(?<!\S)DIAB1\d+\b')
    return patients.loc[diab1]
    
