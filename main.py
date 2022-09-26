import requests
from bs4 import BeautifulSoup as soup

filename = "products.csv"
f = open(filename, "w")

headers = "product_brand, product_name, product_price \n"

f.write(headers)

site_url = "https://www.jumia.com.ng/laptops"

rsp = requests.get(site_url)
page_html = rsp.text

# Html parser
page_soup = soup(page_html, "html.parser")
product_container = page_soup.find_all("a", {"class": "core"})

for products in product_container:
    product_brand = products.get("data-brand")
    product_name = products.find_all(name="h3", class_="name")[0].getText()
    product_price = products.find_all(name="div", class_="prc")[0].getText()

    if product_brand is not None:
        print(product_brand)
        print(product_name)
        print(product_price)
        f.write(product_brand + "" + product_name + "" + product_price.replace("₦", "N") + "\n")

f.close()
