# Brazilian E-Commerce Sales & Customer Analysis — Olist

A Data Science portfolio project using the **Brazilian E-Commerce Public Dataset by Olist**.

The project demonstrates data preparation, exploratory analysis, business KPIs, visualization,
and an interactive Streamlit dashboard.

## Project Questions

- How are sales distributed over time?
- Which product categories generate the most item sales?
- Which customer states contribute the most orders?
- What does the review-score distribution look like?
- How long do deliveries take?
- How do freight costs compare with item sales?

## Dataset

The project is based on the Brazilian E-Commerce Public Dataset by Olist.

The original dataset contains related tables for:

- Customers
- Geolocation
- Orders
- Order Items
- Order Payments
- Order Reviews
- Products
- Sellers
- Product Category Translation

A smaller related sample is included in `data/sample/` so the GitHub repository remains practical
to upload and run.

## Important Data Note

The original Olist dataset **does not contain a direct discount field**. Therefore, this project
does not invent a discount percentage or claim that an observed value is an actual discount.

If discount strategy is required for a separate research project, a dataset containing actual
discount information should be used, or a clearly documented derived proxy should be justified.

## Tools

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Streamlit

## Repository Structure

```text
olist-ecommerce-analysis/
│
├── data/
│   ├── README.md
│   └── sample/
│
├── notebooks/
│   └── olist_eda.ipynb
│
├── outputs/
│   ├── summary_metrics.csv
│   ├── category_summary.csv
│   ├── monthly_sales.csv
│   ├── state_summary.csv
│   ├── review_summary.csv
│   └── charts
│
├── src/
│   └── analysis.py
│
├── app.py
├── requirements.txt
└── README.md
```

## How to Run

### Install packages

```bash
pip install -r requirements.txt
```

### Run the Python analysis

For the complete Olist dataset, put the original CSV files in `data/raw/` and run:

```bash
python src/analysis.py
```

### Run the dashboard

```bash
streamlit run app.py
```

## Key Metrics

The analysis produces:

- Total orders
- Total customers
- Total sellers
- Total products
- Total item sales
- Total freight
- Average order value
- Average review score
- Median delivery time
- Late-delivery rate

## Limitations

The dataset is historical and anonymized. The analysis is descriptive.
A relationship observed in the data should not automatically be interpreted as causal.

## Future Improvements

- Add customer segmentation
- Add predictive modeling
- Add delivery-time prediction
- Add review-score prediction
- Integrate the Power BI dashboard
- Add a separate real-world discount dataset for discount-strategy research

## Author

**Samiksha Shikhare**  
MSc Data Science
