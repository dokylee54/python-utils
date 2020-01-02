'''
    write csv
'''
# if append_check=1 -> append, else just override
def write_list_to_csv(colname_names, row_list, filename, append_check):
    import csv
    
    ## check append_check parameter
    if(append_check): append_check = 'a'
    else: append_check = 'w'
    
    ## open file
    with open(filename, append_check, newline='') as file: 
        
        writer = csv.writer(file) 

        ## column names
        if row_list != '': 
            writer.writerow(colname_names)

        ## rows
        writer.writerows(row_list)


'''
    example
'''
if __name__ == "__main__":
    
    # data
    row_list = [[5,'abc',3],[5,'werew',4, 3, 3],[5,'qew', 2]]
    colname_list = ['a','b','test','d']

    # write csv
    write_list_to_csv(colname_list, row_list, 'test.csv', 0)

    import pandas
 
    # read csv file
    df = pandas.read_csv('test.csv', header=0)
    df = df.fillna(0) # change NaN value into '0'
    print(df.to_string(index=False))