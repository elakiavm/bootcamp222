import pandas as pd 

def get_data():
    
    df = pd.read_csv('comedian_coding .csv')

    #print(df['states'].tolist())

    Comedian_name           = df['Comedian_name'].tolist()

    Film_no         = df['Film_no'].tolist()

    list_of_tuples = [tuple(row) for row in df.values]
  
    print(list_of_tuples)

    result_dict = {
        'Comedian_name'            : Comedian_name,
        'Film_no'         : Film_no,
        'data_list'         : list_of_tuples
    }

    #print(result_dict)

    return result_dict

def add_row(Comedian_name, Film_no):

    df = pd.read_csv('comedian_coding .csv') 

    new_row = {
    
        'Comedian_name'       : Comedian_name, 
        'Film_no'        : Film_no
    }

    print(df)

    df = df.append(new_row, ignore_index=True)

    print(df)

    df.to_csv('comedian_coding .csv')

if __name__ == "__main__":
    get_data()