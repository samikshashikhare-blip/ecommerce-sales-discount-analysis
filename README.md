# E-Commerce Sales & Discount Analysis

A beginner-friendly Data Science portfolio project that analyzes e-commerce sales, profitability, and discount strategies.

## Project Objective

The project answers questions such as:

- How much sales and profit are generated?
- Which product categories generate the most sales?
- How do different discount levels relate to profit?
- How do sales change over time?
- Which regions and categories contribute to performance?

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit

## Project Structure

```text
ecommerce-sales-discount-analysis/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── sample_sales.csv
│
├── src/
│   └── analysis.py
│
├── outputs/
│   └── generated charts and CSV summaries
│
└── notebooks/
```

## How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ecommerce-sales-discount-analysis
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the analysis

```bash
python src/analysis.py
```

The generated CSV summaries and charts will appear in `outputs/`.

### 4. Run the interactive dashboard

```bash
streamlit run app.py
```

## Dataset

The repository contains a small sample dataset created for demonstration so that the project can be run immediately.

For a college/research version, replace it with a properly licensed real-world dataset and document the source and license in this README.

## Important Note About Discount Analysis

This project is intended to explore relationships in sales data. A higher or lower profit observed for a discount band does **not by itself prove that the discount caused the change**. A stronger research project could control for product category, price, seasonality, region, and other factors.

## Possible Future Improvements

- Add customer segmentation
- Add sales forecasting
- Compare machine-learning models
- Add correlation analysis
- Add Power BI dashboard
- Use a larger real-world e-commerce dataset
- Add automated data validation
- Deploy the Streamlit dashboard

## Author

Add your name and MSc Data Science details here.
