# Data

The original Olist dataset contains nine related CSV files. Because GitHub's browser upload
limits and repository size make storing the complete raw dataset inconvenient, this repository
contains a smaller related sample in `data/sample/`.

For the full analysis, download the Brazilian E-Commerce Public Dataset by Olist and place the
original files in `data/raw/` using their original filenames:

- olist_customers_dataset.csv
- olist_geolocation_dataset.csv
- olist_order_items_dataset.csv
- olist_order_payments_dataset.csv
- olist_order_reviews_dataset.csv
- olist_orders_dataset.csv
- olist_products_dataset.csv
- olist_sellers_dataset.csv
- product_category_name_translation.csv

The source data is historical public data; it should be treated as a descriptive/historical
dataset rather than a live current e-commerce feed.

Important: the original Olist data does **not** contain a direct discount percentage/amount field.
This project therefore does not create a fake discount column and present it as source data.
