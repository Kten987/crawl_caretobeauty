import pandas as pd
from crawl_product_detail import get_product_detail
import time


def input_product_name(source = "./in_put/link/link_product_caretobeauty_34_1.csv"):
    df = pd.read_csv(source) # giữ nguyên giá trị duplicate
    list_link = df["Link"].tolist()

    return list_link

# Create a semaphore with a maximum of 10 concurrent tasks


def get_output(list_link):
    list_output = []
    start_time = time.time()
    # Duyệt qua từng tên sản phẩm trong list
    len_list = len(list_link)
    for link in list_link:
        # Thứ tự prodcut hiện tại
        count_processing = list_link.index(link) + 1
        if count_processing % 10 == 0:
            time.sleep(3)
            print(f"estimated: {count_processing*100 /len_list}% -- products left: {len_list - count_processing}")
        
        # Lấy thông tin chi tiết sản phẩm
        try:
            out_put = get_product_detail(link) 
        except Exception as e:
            out_put = {
                'Link': link,
                'brand': "Error",
                'volume': "Error",
                'description': "Error",
                'ingredients': "Error",
                'how_to_use': "Error"
            }
            print(f"Error: {e} because of {link}")

        list_output.append(out_put)


    # Code to be timed
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

    df_output = pd.DataFrame(list_output)
    return df_output

if __name__ == "__main__":
    for i in range(1,2):
        product_name_list = input_product_name(f"./in_put/link/link_product_caretobeauty_2439_{i}.csv")
        df_output = get_output(product_name_list)
        df_output.to_csv(f"./out_put/output_caretobeauty_page_{i}_2439.csv", index=False)
        time.sleep(8)
