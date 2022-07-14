# Import Libararies 

from time import sleep
import pandas as pd
from googlesearch import search
import string
import random
import jellyfish
from urllib.parse import urlparse

# Load File 

file_path='100_chuncks_with_ID/100_chuncks_with_index/part-1.csv'
df=pd.read_csv(file_path)

# Get Company name column in the CSV file

C_name=df["CompanyName"]
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
                ] # bad websites list 

# Iterate through the column
for i in C_name:
    
    waiting=round(random.uniform(5, 50)) # Get random number to waiting 
    print('Waiting for '+str(waiting)+' seconds')
    sleep(waiting) # Pause for 'some' seconds  
    query = i # store 'Name' to search as query 
    
    for char in string.punctuation: 
        query = query.replace(char, ' ') # remove punctuation in  the name  
    
    query= " ".join(query.split()) # remove extra spaces 
    
    #print(query) # name to search by Google search engine 
    
    urlList=list(search(query, num_results=1))

    True_websites=list(urlList)
    True_website=''
    
    

    for URL in urlList:
        
        for bad in bad_websites:
           
            if bad in URL:
                #print('Found'+ URL)
                try:
                    True_websites.remove(URL)
                except:
                    pass

    
    if len(True_websites)<1:
        True_website='null'
    else:
        True_website=True_websites[0]
    
    #print(True_website)

    web_hostname=urlparse(True_website).netloc
    
    web_hostname= web_hostname.replace('www.','')
    web_hostname= web_hostname.replace('.com', '')
    web_hostname = web_hostname.replace ('.co.uk', '')
    web_hostname = web_hostname.replace ('.org.uk', '')
    web_hostname = web_hostname.replace ('.ltd.uk', '')
    

    cmp_name=query.replace(' ', '')
    cmp_name=query.lower()
    
    print(cmp_name)
    print(web_hostname)
    Similarity_score=jellyfish.jaro_similarity(web_hostname, cmp_name)
    
    print(Similarity_score)



    
