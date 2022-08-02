from calendar import c
from email import header
from itertools import count
from multiprocessing.connection import wait
from time import sleep
import pandas as pd
import string
import re
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
import multiprocessing
import time
import signal
# from verify_email import verify_email
bad_domain=['wixpress.com','sentry.io']
file_path='temp_email.csv'
df=pd.read_csv(file_path)
final_path='Final_data_email.csv'
Final_dataframe=pd.read_csv(final_path)
def verify_email_add(email):
    split=email.split('.')
    last_word=split[-1]
    # print(la)
    if last_word == 'com' or last_word == 'uk'or last_word == 'net' or last_word == 'eco' or last_word == 'io':
        return True

    else:
        return False

def get_emails(webURLs):
    print(len(webURLs))
    unverify_emails=set()
    count=0
    for k in webURLs:
        if count >50:
            break
        count+=1
        print(count)
        try:
            weburl = urllib.request.urlopen(k,timeout=10)

            code = weburl.read().decode('utf-8')
            for e in re.findall(r'[\w\d_.-]+@[\w\d_.-]+',code):

                unverify_emails.add(e)
                
        except Exception as e:
            print('Cannot open hyperlink')

    return unverify_emails

for index, row in df.iterrows():
    C_url=row["URL"]

    websiteURLS = set()
    all_href=[]
    email_list=[]
    emails=set()
    unverify_emails=set()
    website_count=0

    URL=C_url
    websiteURLS.add(URL)
    parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
    try:
        print('Getting Email for: '+ URL)
        req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
        resp=urlopen(req,timeout=50)
        soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

        for link in soup.find_all( href=True):
            #emails.update(link['href']) 
            all_href.append(link['href'])

        # print(len(all_href))

        for i in all_href:

            if (i.startswith('http')):
                websiteURLS.add(i)
            
        print('Found '+str(len(websiteURLS))+ ' Hyperlinks')
        
        unverify_emails=get_emails(websiteURLS)
        

    except Exception as e:
        print(e)
        print('Cannot open website')
    
    temp_email=list(unverify_emails)

    for l in temp_email:
        for bad in bad_domain:
            if bad in l:
                try:
                    unverify_emails.remove(l)
                except:
                    pass
        # print(l)
    # for l in unverify_emails:
    #     print(l)
    #     print(verify_email_add(l))
        


    for l in unverify_emails:
        print(l)
        if verify_email_add(l):
            emails.add(l)
    email_list=sorted(emails)
    if len(email_list)==0:
        row_value=row.to_frame().T
        Final_dataframe.append(row_value)
        frames=[Final_dataframe,row_value]
        Final_dataframe=pd.concat(frames)
        Final_dataframe.to_csv('Final_data_email.csv',index=False)
        df.drop(index,axis=0, inplace=True)
        df.to_csv('temp_email.csv', index=False)
    elif len(email_list)==1:
        print(email_list[0])
        row_value=row.to_frame().T
        row_value['Email1']=[email_list[0]]
        Final_dataframe.append(row_value)
        frames=[Final_dataframe,row_value]
        Final_dataframe=pd.concat(frames)
        Final_dataframe.to_csv('Final_data_email.csv',index=False)
        df.drop(index,axis=0, inplace=True)
        df.to_csv('temp_email.csv', index=False)
    elif len(email_list)==2:
        print(email_list[0])
        print(email_list[1])
        row_value=row.to_frame().T
        row_value['Email1']=[email_list[0]]
        row_value['Email2']=[email_list[1]]
        Final_dataframe.append(row_value)
        frames=[Final_dataframe,row_value]
        Final_dataframe=pd.concat(frames)
        Final_dataframe.to_csv('Final_data_email.csv',index=False)
        df.drop(index,axis=0, inplace=True)
        df.to_csv('temp_email.csv', index=False)
    elif len(email_list)>2:
        print(email_list[0])
        print(email_list[1])
        print(email_list[2])
        row_value=row.to_frame().T
        row_value['Email1']=[email_list[0]]
        row_value['Email2']=[email_list[1]]
        row_value['Email3']=[email_list[2]]
        Final_dataframe.append(row_value)
        frames=[Final_dataframe,row_value]
        Final_dataframe=pd.concat(frames)
        Final_dataframe.to_csv('Final_data_email.csv',index=False)
        df.drop(index,axis=0, inplace=True)
        df.to_csv('temp_email.csv', index=False)

    