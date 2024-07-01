import requests as request
import pandas as pd

def get_links_product(page_1, id_category) :
    url = f"https://www.caretobeauty.com/us/catalog/api_category/?p={page_1}&id={id_category}" 
    print(url)
    response = request.get(url)
    rows = []
    data = response.json()

    # Lấy các sản phẩm
    list_data = data['data']['collection']['products']

    for data in list_data:
        link = data["url"]
        #brand = data["brandName"]
        product_name = data["name"]
        image_key = data["desktop_image"]
        price_usd = data["formatted_final_price"]
        category = id_category
        rows.append([link, product_name, image_key,price_usd, category])

    df = pd.DataFrame(rows, columns=['Link', 'productName', 'image_key','price_usd', 'id_category'])
    df.to_csv(f'in_put/link/link_product_caretobeauty_{id_category}_{page_1}.csv', index=False)


    return data

if __name__ == '__main__':
    for i in range(1, 2):
        get_links_product(i,106)

