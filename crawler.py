import requests
import datetime
import os
from bs4 import BeautifulSoup
import random
import time
import zipfile

futures_base_url="https://www.taifex.com.tw/cht/3/futPrevious30DaysSalesData"
futures_download_url="https://www.taifex.com.tw/file/taifex/Dailydownload/DailydownloadCSV/Daily_{year}_{month}_{day}.zip"

options_base_url="https://www.taifex.com.tw/cht/3/optPrevious30DaysSalesData"
options_download_url="https://www.taifex.com.tw/file/taifex/Dailydownload/OptionsDailydownloadCSV/OptionsDaily_{year}_{month}_{day}.zip"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def rename_in_zip(zip_path: str, old_name: str, new_name: str):
    tmp_zip = zip_path + '.tmp'

    with zipfile.ZipFile(zip_path, 'r') as zin, \
         zipfile.ZipFile(tmp_zip,   'w', compression=zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            arcname = new_name if item.filename == old_name else item.filename
            zout.writestr(arcname, data, compress_type=item.compress_type)
    os.replace(tmp_zip, zip_path)


def download_futures_data(year, month, day):
    url = futures_download_url.format(year=year, month=month, day=day)
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        filename = f"./fut/Fut_{year}_{month}_{day}.zip"
        
        with open(filename, 'wb') as file:
            file.write(response.content)
        rename_in_zip(filename, f'Daily_{year}_{month}_{day}.csv', f'Fut_{year}_{month}_{day}.csv')
        print(f"Downloaded futures data for {year}-{month}-{day} to {filename}")
    else:
        print(f"Failed to download futures data for {year}-{month}-{day}")

def download_options_data(year, month, day):
    url = options_download_url.format(year=year, month=month, day=day)
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        filename = f"./opt/Opt_{year}_{month}_{day}.zip"
        with open(filename, 'wb') as file:
            file.write(response.content)
        rename_in_zip(filename, f'OptionsDaily_{year}_{month}_{day}.csv', f'Opt_{year}_{month}_{day}.csv')
        print(f"Downloaded options data for {year}-{month}-{day} to {filename}")
    else:
        print(f"Failed to download options data for {year}-{month}-{day}")
        

def main():
    base_response = requests.get(futures_base_url, headers=headers)
    dates=[]
    if base_response.status_code == 200:
        soup = BeautifulSoup(base_response.content, 'html.parser')
        sidebar_right= soup.find('div', class_='sidebar_right')
        tobdys = sidebar_right.find_all('tbody')
        for tbody in tobdys:
            tds=tbody.find_all('td')
            for td in tds:
                if len(td.text.strip())!=10:
                    continue
                date = td.text.strip()             
                dates.append(date)
    else:
        print("Failed to retrieve the base page for futures data.")
        return
    
    for date in dates:
        year, month, day = date.split('/')
        fut_path=f'./fut/Fut_{year}_{month}_{day}.zip'
        opt_path=f'./opt/Opt_{year}_{month}_{day}.zip'
        fut_checker=True
        opt_checker=True
        #if its today
        if date == time.strftime("%Y/%m/%d"):
            if os.path.exists(fut_path):
                if os.path.getctime(fut_path) < datetime.combine(datetime.today().date(), time(hour=18)).timestamp():
                    fut_checker=False
            if os.path.exists(opt_path):
                if os.path.getctime(opt_path) < datetime.combine(datetime.today().date(), time(hour=18)).timestamp():
                    opt_checker=False
        
        if os.path.exists(fut_path) and fut_checker:
            print(f"Futures data for {year}-{month}-{day} already exists, skipping download.")
        else:
            download_futures_data(year, month, day)
            time.sleep(random.uniform(3, 5))
            
            
        if os.path.exists(opt_path) and opt_checker:
            print(f"Options data for {year}-{month}-{day} already exists, skipping download.")
        else:
            download_options_data(year, month, day)
            time.sleep(random.uniform(3, 5))
                   
if __name__ == "__main__":
    if not os.path.exists('./fut'):
        os.makedirs('./fut')
    if not os.path.exists('./opt'):
        os.makedirs('./opt')
    main()