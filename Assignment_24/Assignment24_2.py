import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def Dataframe():
    data = {'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82]}

    df = pd.DataFrame(data)
    print("Original Data is : ")
    print(df)

    df['Gender'] = ['Male','Male','Female'] 
    print("Updated Data : ")
    print(df)

    encoder= OneHotEncoder(sparse_output=False).set_output(transform='pandas')
    gender_enc=encoder.fit_transform(df[['Gender']])

    df = pd.concat([df,gender_enc],axis=1).drop(columns=['Gender'])
    print("Output : ")
    print(df)

def main():
    Dataframe()

if __name__ == "__main__":
    main()