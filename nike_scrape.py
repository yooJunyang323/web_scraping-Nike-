import requests
from bs4 import BeautifulSoup
import json


url = 'https://www.nike.com/my/w/new-upcoming-drops-k0gk'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

file_name = 'nike.json'
save_data = []

def save_to_json(save_data):
    with open(file_name,'w') as file:
        json.dump(save_data,file,indent=4)



response = requests.get(url, headers=headers)


if response.status_code != 200:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
else:
    soup = BeautifulSoup(response.text, 'html.parser')

   
    title = soup.find('div', class_='wall-header__content')
    if title and title.h1:
        print(f"Page Title: {title.h1.text.strip()}")

    
    product_container = soup.find_all('div', class_='product-card')

    if not product_container:
        print("No products found. The site may use JavaScript to load products dynamically.")

    for product in product_container:
        product_name_tag = product.find('div', class_='product-card__title')
        product_price_tag = product.find('div', class_='product-price')
        product_img_tag = product.find('img', class_='product-card__hero-image')

       
        product_name = product_name_tag.text.strip() if product_name_tag else "No name"
        product_price = product_price_tag.text.strip() if product_price_tag else "No price"
        product_img_url = product_img_tag['src'] if product_img_tag else "No image"
        save_data.append({
            'name': product_name,
            'price': product_price,
            'image_url': product_img_url
        })
        
        print(f"Product: {product_name}")
        print(f"Price: {product_price}")
        print(f"Image URL: {product_img_url}")
        print("-" * 50)

        save_to_json(save_data)