
import pandas as pd
import string
from googlesearch import search
import jellyfish
from urllib.parse import urlparse



file_path='temp.csv'
df=pd.read_csv(file_path)
final_path='Final_data.csv'
Final_dataframe=pd.read_csv(final_path)


bad_websites=[
                'find-and-update.company-information.service.gov.uk',
                'www.companyinformation.co.uk',
                'www.companiesintheuk.co.uk',
                'opengovuk.com',
                'www.companysearchesmadesimple.com',
                'youcontrol.com.ua',
                'www.facebook.com',
                'suite.endole.co.uk',
                'www.dnb.com',
                'www.instagram.com',
                'www.addressadda.com',
                'companycheck.co.uk',
                'www.companysearchesmadesimple.com',
                'www.192.com',
                'www.companydirectorcheck.com',
                'vat-search.eu',
                'www.companiesdatabase.uk',
                'opencorporates.com',
                'find-and-update.company-information.service.gov.uk',
                'www.companieslist.co.uk',
                'suite.endole.co.uk',
                'www.companysearchesmadesimple.com',
                'uk.linkedin.com',
                'gb.kompass.com',
                'kingsbridge.cylex-uk.co.uk',
                'www.vat-check.co.uk',
                'beckenham.cylex-uk.co.uk',
                'b2bhint.com',
                'thegazette.co.uk',
                '1stdirectory.co.uk',
                'onlinefilings.co.uk',
                'checkcompany.co.uk',
                'getthedata.co.uk',
                'bizdb.co.uk',
                'britishowl.com',
                'datocapital.uk',
                'uk.globaldatabase.com'

                ] # bad websites list 

for index, row in df.iterrows():
    C_name=row["CompanyName"]
    print('Waiting for '+str(15)+' seconds')
    query = C_name # store 'Name' to search as query
    for char in string.punctuation: 
        query = query.replace(char, ' ') # remove punctuation in  the name  
    query= " ".join(query.split()) # remove extra spaces 
    
    print('Getting URL for :'+ query)
    urlList=list(search(query, num=2,stop=1, pause=15))
    print('Search Complete')

    True_websites=list(urlList)
    True_website=''

  

    for URL in urlList:
        
        for bad in bad_websites:
           
            if bad in URL:
                try:
                    True_websites.remove(URL)
                except:
                    pass


    if len(True_websites)<1:
        True_website='null'
    else:
        True_website=True_websites[0]

    web_hostname=urlparse(True_website).netloc
    
    web_hostname= web_hostname.replace('www.','')
    web_hostname= web_hostname.replace('.com', '')
    web_hostname = web_hostname.replace ('.co.uk', '')
    web_hostname = web_hostname.replace ('.org.uk', '')
    web_hostname = web_hostname.replace ('.ltd.uk', '')


    cmp_name=query.lower()
    cmp_name=cmp_name.replace(' ', '')

    print(cmp_name)
    print(web_hostname)
    Similarity_score=jellyfish.jaro_similarity(web_hostname, cmp_name)
    print(Similarity_score)

    if Similarity_score>0.6:
        print(True_website)
        row_value=row.to_frame().T
        row_value['URL']=[True_website]
        Final_dataframe.append(row_value)
        frames=[Final_dataframe,row_value]
        Final_dataframe=pd.concat(frames)
        Final_dataframe.to_csv('Final_data.csv',index=False)
        df.drop(index,axis=0, inplace=True)
        df.to_csv('temp.csv', index=False)
    else:
        df.drop(index,axis=0, inplace=True)
        df.to_csv('temp.csv', index=False)