def main():
    
    from nppes import nppes_df
    import csv
    import pandas as pd

    inputfilename = input("Enter CSV file here: ")
    
    run=True

    while run == True:
       
        #Df for storing data to write to and output
        df_for_parsing = pd.DataFrame()
        
        #turning input_csv into data frame for parsing & creating variables for number_lookup function
        try_file_name='{}.csv'.format(inputfilename)
        df = pd.read_csv(try_file_name, dtype=str)  

        #adding column in df for full name & applying capitalization
        df['full name']= (df['last name'] + ' ' + df['first name']).str.upper()

        #making df['full name'] into list for parsing
        list_of_fullnames= df['full name'].tolist()
        list_of_states=df['state'].tolist()
    
        count=0
        for ind in df.index:
            npi_df= nppes_df(last_name= df['last name'][ind], state= df['state'][ind])
            
            df_for_parsing= pd.concat([df_for_parsing, npi_df])
            count+=1

        run=False

        df_for_parsing.columns= ['number','basic.name','basic.name_prefix','basic.first_name','basic.last_name','basic.middle_name','basic.credential',\
                                 'basic.gender', 'country_code','country_name','address_purpose','address_type','address_1','address_2','city',\
                                 'state_x','postal_code', 'telephone_number','fax_number','code','desc','primary','state_y','license']

        #drop names of those not in full name list
        df_for_export= df_for_parsing[(df_for_parsing['basic.name'].isin(list_of_fullnames))& df_for_parsing['state_x'].isin(list_of_states)]

        print()
        print(str(count) + ' names searched')
        print('Returning results')
        
        #when all is complete save newly written csv file to desktop
        df_for_export.to_csv('newly_created_test.csv', index=False)

        return
        


main()



