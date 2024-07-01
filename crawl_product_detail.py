from botasaurus.request import request, Request
from botasaurus.soupify import soupify
from bs4 import BeautifulSoup
import pandas as pd
import json
from get_description import get_description_
import re

@request
def get_product_detail(request: Request, Link):

    # Navigate to the Omkar Cloud website
    response = request.get(Link)

    rows = {}
    list_description = []

    rows["Link"] = Link
    # Create a BeautifulSoup object    
    soup = soupify(response)
    #Lưu ra file để xem cấu trúc html
    with open('caretobeauty_1.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

    # Lấy thông tin sản phẩm
    try:
        brand = soup.find("div", class_="product-view__title").find("a").text.strip()
    except:
        brand = "Not found"
    rows["brand"] = brand

    # description = soup.find("div", class_="product-view__description")
    # for i in description.find_all("details", class_="accordion__item"):
    #     list_description.append(i.text.strip())

    # rows["description"] = [list_description]

    # Extract the volume from the link
    volume_match = re.search(r'(\d+ml|\d+g|\d+-pair|x\d+)', Link)
    if volume_match:
        volume = volume_match.group()
    else:
        try:
            volume = soup.find_all("div", class_="product-configurations__name__item")[-1].text.strip()
        except:
            volume = "Not found"

    rows["volume"] = volume

    list_description = soup.find('script', {'type': 'application/ld+json'})

    list_description = json.loads(list_description.text)

    description = list_description["description"]

    desc = get_description_(description)
    try:
        rows["description"] = desc["Description"]
    except:
        rows["description"] = "Not found"
    try:
        rows["ingredients"] = desc["Main Ingredients"]
    except:
        rows["ingredients"] = "Not found"
    try:
        rows["how_to_use"] = desc["How to use"]
    except:
        rows["how_to_use"] = "Not found"
    #rows["ingredients"] = desc["Ingredients"]


    #df = pd.DataFrame(rows, index=[0], columns=['Link','brand', 'volume' ,'description','ingredients','how_to_use'])
    #df.to_csv('test_product_4.csv', index=False)
    # Save the data as a JSON file in output/scrape_heading_task.json
    return rows  

if __name__ == "__main__":
    print(get_product_detail("https://www.caretobeauty.com/us/neutrogena-hydro-boost-water-gel-50ml-eye-contour-15ml/"))

