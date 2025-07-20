import pandas as pd
from sklearn.preprocessing import MinMaxScaler 

def Dataframe():
    data = {'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]}
    
    df = pd.DataFrame(data)
    print(df)

    print("Shape of data : ",df.shape)

    print("Column in data : ")
    df.info()

    Math_org=df[['Math']]
    scaler=MinMaxScaler()
    Math_normalized=scaler.fit_transform(Math_org)
    print("scaling of column Math using sklearn is : ")
    print(Math_normalized)

    Math_normalized= (df['Math'] - df['Math'].min()) / (df['Math'].max() - df['Math'].min())
    print("scaling of column Math using pandas is : ")
    print(Math_normalized)

def main():
    Dataframe()

if __name__ == "__main__":
    main()