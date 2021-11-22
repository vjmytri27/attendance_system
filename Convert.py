import pandas as pd

def main():
    df = pd.read_csv('Records.csv')

    writer = pd.ExcelWriter('Records.xlsx')
    df.to_excel(writer, index=False)
    writer.save()
