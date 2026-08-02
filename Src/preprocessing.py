import pandas as pd

def dataset_info(df):
    print("\n .............first 5 rows........ ")
    print(df.head())

    print("\n ............Last 5 rows............")
    print(df.tail())


    print("\n..............data_set indo..........")
    print(df.info())

    print("\n ............shape of data set.........")
    print(df.shape)

    print("\n............... colummns...............")
    print(df.columns)

    print("\n ...............data type...........")
    print(df.dtypes)

    print("\n..........summary of data set...........")
    print(df.describe())

def check_missing_values(df):
    print("\n............. missing values.............")
    print(df.isnull().sum())


def check_duplicates(df):
    print("\n.............. duplicate value.................")
    print(df.duplicated().sum)



def remove_duplicates(df):
    df = df.drop_duplicates()
    return df

def save_clean_data(df):
    df.to_csv("data/employee_cleaned.csv",index=False)
    print("\n cleaned dataset sucessfully")
    
    
