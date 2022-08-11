import pandas as pd

def analyze(file):
    df = pd.read_excel(file)
    print(df)



if __name__ == "__main__":
    analyze("test.xlsx")
