import pandas as pd
import sqlite3

# STEP 1: Load CSV data (Orders - Transactional Data)
orders_df = pd.read_csv("orders.csv")

# STEP 2: Load JSON data (Users - Master Data)
users_df = pd.read_json("users.json")

# STEP 3: Load SQL data (Restaurants - Master Data)
conn = sqlite3.connect("restaurants.db")   # database created from restaurants.sql
restaurants_df = pd.read_sql(
    "SELECT * FROM restaurants",
    conn
)

# STEP 4: Merge the Data
# Join orders with users (LEFT JOIN)
orders_users_df = pd.merge(
    orders_df,
    users_df,
    on="user_id",
    how="left"
)

# Join result with restaurants (LEFT JOIN)
final_df = pd.merge(
    orders_users_df,
    restaurants_df,
    on="restaurant_id",
    how="left"
)

# STEP 5: Create Final Dataset
print(final_df.head())

# Save final dataset
final_df.to_csv("final_food_delivery_dataset.csv", index=False)

# Close DB connection
conn.close()
