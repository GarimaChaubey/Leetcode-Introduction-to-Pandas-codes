import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    new_df=students[students['student_id']==101]
    
    res=new_df[['name','age']]
    
    return res