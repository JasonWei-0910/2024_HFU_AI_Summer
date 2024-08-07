import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium_cybersec_scraper_api import get_exd_detail 
from selenium_cybersec_scraper_api import create_webdriver
import time


def get_cybersec_exd_info(is_export_to_csv=True):
   
    url = "https://cybersec.ithome.com.tw/2024/exhibitionDirectory"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    exd_cards = soup.find_all("div", attrs={"class": "exd-card"})

    url_prefix = "https://cybersec.ithome.com.tw"
    exd_cards_info = list()
    test_driver = create_webdriver()

    for exd_card in exd_cards:
        # 找連結
        href = url_prefix + exd_card.a["href"]

        # 展攤名稱
        exd_name = exd_card.h5.text

        # 展攤位置編號
        if exd_card.h6: # 判斷是否為None
            exd_id = exd_card.h6.text.split("：")[1]
        else:
            exd_id = ""


        
      
        exd_data = get_exd_detail(
            url=href,
            driver=test_driver
        )

        exd_intro ={
            'exd_link': href,
            'exd_name': exd_name,
            'exd_id': exd_id
        }

        exd_data.update(exd_intro)
        

        # print(href, exd_name, exd_id)
        exd_cards_info.append(exd_data)

        time.close(5)

    test_driver.close()

    if is_export_to_csv:
        data = pd.DataFrame(exd_cards_info) # 轉換成DataFrame
        data.to_csv('cybersec_exd.csv')

    return   exd_cards_info


if __name__=='__main__':
    data = get_cybersec_exd_info(is_export_to_csv=False)
    print(data[:5])

