# UK-SME

# Extracting URLs using name of the company

## Step-1
Download the file all parts from https://essexuniversity-my.sharepoint.com/:u:/g/personal/ma22159_essex_ac_uk/Ed4s754BA4dCi0K9tEZM8qABNON3bvqdBTXFB6JKvAaRiA and extract it

## Step-2
Install requirements by using 
<br />
```pip install -r requirements.txt```

## Step-3
Copy a part(x) to temp.csv using *Reset_temp_csv.py*
<br />
Change ```file_path='100_chuncks_with_index\part-x.csv'``` to required part in *Reset_temp_csv.py*
<br />
** WARNING! ** 
<br />
Only run *Reset_temp_csv.py* once until you have not finished that part other wise it will reset the *temp.csv*

## Step-4
Run *Google_URL_extractor.py* to extract the URL of the companies using name

## Step-5
All the URLs will be stored in *Final_data.csv* 

# Extracting Email from URLs

## Step-1
Copy a data to temp_email.csv using *Reset_email_temp.py*
<br />
Change ```file_path='Data-sent\Mohsin_data_p2.csv'``` to required file name containing URLs in *Reset_email_temp.py*
<br />
** WARNING! ** 
<br />
Only run *Reset_email_temp.py* once until you have not finished that part other wise it will reset the *temp_email.csv*

## Step-2
Run *Email_extractor.py* to extract the Emails of the companies using URLs

## Step-3
All the URLs will be stored in *Final_data_email.csv* 

