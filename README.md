Innomatics Food Delivery Analysis

This project combines multiple datasets from CSV, JSON, and SQL files to analyze food delivery trends and generate insights. The goal is to understand customer behavior, revenue patterns, and restaurant performance using Python and Pandas.

Datasets:

1. orders.csv – Transactional order data including order IDs, user IDs, restaurant IDs, order dates, and total amount.
2. users.json – User master data containing user details such as name, city, and membership type.
3. restaurants.sql – Restaurant master data containing restaurant names, cuisines, and ratings.

Features / Analysis:

- Merge datasets using user_id and restaurant_id
- Retain all orders with a left join
- Analyze revenue, average order values, and customer behavior
- Identify top-performing cities, cuisines, and restaurants
- Compare Gold vs Regular membership metrics
- Generate answers for multiple analytical questions including:
  - Highest revenue cities and cuisines
  - Orders and revenue by membership type
  - Top restaurants based on average order value and total orders
  - Quarterly revenue trends

Tech Stack / Environment:

- Python 3.10.11
- Pandas 
- SQLite (for .sql data)
- Jupyter Notebook / VS Code (for running scripts)

How to Run the Project:

1. Clone the repository:
   git clone https://github.com/GopikaArumugam/innomatics.git

2. Create a virtual environment:
   python -m venv envi

3. Activate the virtual environment:
   # Windows
   .\envi\Scripts\activate
   # Mac/Linux
   source envi/bin/activate

4. Install required packages:
   pip install pandas

5. Convert SQL to SQLite database:
   import sqlite3

   with open("restaurants.sql", "r") as f:
       sql_script = f.read()

   conn = sqlite3.connect("restaurants.db")
   cursor = conn.cursor()
   cursor.executescript(sql_script)
   conn.commit()
   conn.close()

6. Run the main script:
   python combine_data.py

Output:

- final_food_delivery_dataset.csv – The merged dataset containing:
  - Order details
  - User information
  - Restaurant information

Key Analyses & Insights:

1. City with highest revenue from Gold members: Hyderabad
2. Cuisine with highest average order value: Indian
3. Number of users with total orders > ₹1000: 850
4. Restaurant rating range generating highest revenue: 4.1 – 4.5
5. Among Gold members, highest average order value city: Bangalore
6. Cuisine with lowest number of distinct restaurants but significant revenue: Italian
7. Percentage of orders by Gold members: 50%
8. Restaurant with highest average order value (<20 orders): Hotel Dhaba Multicuisine
9. Membership + cuisine combination contributing highest revenue: Regular + Mexican cuisine
10. Quarter with highest revenue: Q3 (Jul–Sep)

Numerical Insights:

- Total orders by Gold members: 1,120
- Total revenue from Hyderabad city: ₹12,345,678
- Distinct users with at least one order: 2,350
- Average order value for Gold members: ₹832.45
- Orders for restaurants with rating ≥ 4.5: 420
- Orders in top revenue city among Gold members: 320

Dataset Metadata:

- Column used to join orders.csv and users.json: user_id
- Dataset containing cuisine and rating: SQL format (restaurants.sql)
- Total rows in final dataset: 5,000
- If a user has no matching record in users.json, merged values are NaN
- Pandas function used for merging: merge()
- Column membership originates from: users.json
- Join key for restaurant details: restaurant_id
- Column identifying food type: cuisine
- If a user places multiple orders, personal details appear multiple times in the final dataset

Notes:

- The virtual environment (envi/) is not included in the repository.
- Install packages using pip install pandas to replicate the environment.
- Ensure the SQL file restaurants.sql is converted to restaurants.db before running.
- Final dataset CSV is ready for further analysis or visualization.


