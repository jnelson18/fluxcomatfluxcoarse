import requests
import pandas as pd
import os

all_sites = sorted(pd.read_csv("data/sites_with_2018.csv")["site_id"].tolist())

if not os.path.isdir("data/sites"):
    os.makedirs("data/sites")

def download_site(site):
    response = requests.get(f'https://nextcloud.bgc-jena.mpg.de/public.php/dav/files/wjZzy8BCE7KagEQ/{site}.csv')
    
    with open(f'data/sites/{site}.csv.partial', 'wb') as f:
        f.write(response.content)
    
    os.rename(f'data/sites/{site}.csv.partial', f'data/sites/{site}.csv')

for site in all_sites:
    if os.path.isfile(f'data/sites/{site}.csv'):
        print("Already Downloaded " + site)
        continue
    else:
        print("Downloading " + site)
        download_site(site)