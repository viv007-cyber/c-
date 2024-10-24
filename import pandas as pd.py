import pandas as pd 
reviews=pd.read_csv("C:\Users\Vijay jain\Desktop\Housing.csv")
#CREATING A LIST OF THE COLUMNS THAT HAVE CATEGORICAL VARIABLES 
s=reviews.dtypes=="object"
d=list(s[s].index)

#ORDINAL ENCODING
reviews.d[0].replace("u",0)
reviews.d[0].replace("h",1)

#ONE HOT ENCODING
def func(row):
    if row=="u":
        return 1
    else:
        return 0
    
def func2(row):
 if row=="h":
    return 1
 else:
    return 0

column1=reviews.d[0].map(func)
column2=reviews.d[0].map(func2)

column1.rename(columns={"type":"u"},inplace=True)
column1.rename(columns={"type":"h"},inplace=True)

reviews.drop("type",axis="1")
