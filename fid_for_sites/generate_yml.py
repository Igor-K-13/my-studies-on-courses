import pandas as pd
from lxml import etree

# Загрузка CSV с товарами
df = pd.read_csv('products.csv')

# Создаём корень документа
yml_catalog = etree.Element("yml_catalog", date="2025-06-04T12:00:00")
shop = etree.SubElement(yml_catalog, "shop")

# Основная инфа о магазине (замени на свои данные)
etree.SubElement(shop, "name").text = "Лесенка в доме"
etree.SubElement(shop, "company").text = "Лесенка в доме"
etree.SubElement(shop, "url").text = "https://lesenkavdome.ru"

# Категории (заполни или сделай динамически, если нужно)
categories = etree.SubElement(shop, "categories")
cat_ids = df['categoryId'].unique()
for cat_id in cat_ids:
    cat_name = "Лестницы"  # Можно добавить словарь с названиями категорий по id
    etree.SubElement(categories, "category", id=str(cat_id)).text = cat_name

# Офферы (товары)
offers = etree.SubElement(shop, "offers")

for _, row in df.iterrows():
    offer = etree.SubElement(offers, "offer", id=str(row['id']), available="true")
    etree.SubElement(offer, "name").text = str(row['name'])
    etree.SubElement(offer, "price").text = str(row['price'])
    etree.SubElement(offer, "currencyId").text = "RUR"
    etree.SubElement(offer, "categoryId").text = str(row['categoryId'])
    etree.SubElement(offer, "picture").text = str(row['picture'])
    etree.SubElement(offer, "url").text = str(row['url'])
    description = etree.SubElement(offer, "description")
    description.text = etree.CDATA(str(row['description']))

# Сохраняем в файл
tree = etree.ElementTree(yml_catalog)
tree.write("yml_feed.xml", encoding="utf-8", xml_declaration=True, pretty_print=True)

print("YML-фид успешно создан: yml_feed.xml")
