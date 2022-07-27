#https://gohorseprocess.com.br/wp-content/uploads/2017/05/horse21.png
#instalar pandas. pip install pandas. Deve instalar o openpyxl, pois o pandas precisa para
#instalar openpyxl. pip install openpyxl https://openpyxl.readthedocs.io/en/stable/
import pandas as pd

def read(path, columnName): 
    items = []
    data = pd.read_excel(path)
    # Read the values of the file in the dataframe
    # data = pd.DataFrame(df. ["column_name0", "column_name1"])
    df = pd.DataFrame(data)
    # Print the content
    print("The content of the file is:\n", df)
    df = df.reset_index()  # make sure indexes pair with number of rows
    for index, row in df.iterrows():
        print(row['Name'])
        items.append(row[columnName])
    return items