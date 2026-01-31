import pandas as pd

df = pd.read_csv("final_food_delivery_dataset.csv")
df["order_date"] = pd.to_datetime(df["order_date"], format="%d-%m-%Y")

# 1. City with highest total revenue from Gold members
gold_city_revenue = df[df["membership"] == "Gold"].groupby("city")["total_amount"].sum().sort_values(ascending=False)

# 2. Cuisine with highest average order value
avg_cuisine_value = df.groupby("cuisine")["total_amount"].mean().sort_values(ascending=False)

# 3. Distinct users with orders > 1000 total
user_spend = df.groupby("user_id")["total_amount"].sum()

# 4. Rating range with highest total revenue
bins = [3.0, 3.5, 4.0, 4.5, 5.0]
labels = ["3.0-3.5", "3.6-4.0", "4.1-4.5", "4.6-5.0"]
df["rating_range"] = pd.cut(df["rating"], bins=bins, labels=labels)
rating_revenue = df.groupby("rating_range")["total_amount"].sum().sort_values(ascending=False)

# 5. Gold members: city with highest avg order value
gold_city_avg = df[df["membership"] == "Gold"].groupby("city")["total_amount"].mean().sort_values(ascending=False)

# 6. Cuisine with lowest number of distinct restaurants but high revenue
restaurant_count = df.groupby("cuisine")["restaurant_id"].nunique()
revenue_by_cuisine = df.groupby("cuisine")["total_amount"].sum()
cuisine_analysis = pd.concat([restaurant_count, revenue_by_cuisine], axis=1)
cuisine_analysis.columns = ["restaurant_count", "total_revenue"]

# 7. Percentage of orders by Gold members
gold_percentage = round((df[df["membership"] == "Gold"].shape[0] / df.shape[0]) * 100)

# 8. Restaurant with highest avg order value but < 20 orders
restaurant_stats = df.groupby("restaurant_name_x").agg(avg_value=("total_amount", "mean"), count=("order_id", "count"))
filtered_restaurants = restaurant_stats[restaurant_stats["count"] < 20].sort_values("avg_value", ascending=False)

# 9. Combination contributing highest revenue
combo_revenue = df.groupby(["membership", "cuisine"])["total_amount"].sum().sort_values(ascending=False)
top_combo = combo_revenue.index[0]

# 10. Quarter with highest total revenue
df["quarter"] = df["order_date"].dt.to_period("Q")
quarter_revenue = df.groupby("quarter")["total_amount"].sum().sort_values(ascending=False)
top_quarter = str(quarter_revenue.index[0])

# 11-16: Numerical answers
gold_orders_total = df[df["membership"] == "Gold"].shape[0]
hyderabad_revenue = round(df[df["city"] == "Hyderabad"]["total_amount"].sum())
distinct_users = df["user_id"].nunique()
gold_avg_order = round(df[df["membership"] == "Gold"]["total_amount"].mean(), 2)
orders_rating_45 = df[df["rating"] >= 4.5].shape[0]
orders_top_gold_city = df[(df["membership"] == "Gold") & (df["city"] == gold_city_revenue.index[0])].shape[0]

# 17-25: Theory/fill-in answers
join_orders_users = "user_id"
cuisine_data_format = "SQL"
total_rows = df.shape[0]
no_matching_user = "NaN"
pandas_function = "merge"
membership_origin = "users.json"
join_orders_restaurant = "restaurant_id"
food_type_column = "cuisine"
user_multiple_orders = "multiple"

# Print all answers numbered
print("1.", gold_city_revenue.index[0])
print("2.", avg_cuisine_value.index[0])
print("3.", user_spend[user_spend > 1000].count())
print("4.", rating_revenue.index[0])
print("5.", gold_city_avg.index[0])
print("6.", cuisine_analysis.sort_values("restaurant_count").index[0])
print("7.", f"{gold_percentage}%")
print("8.", filtered_restaurants.index[0])
print("9.", f"{top_combo[0]} + {top_combo[1]} cuisine")
print("10.", "Q" + top_quarter[-1])
print("11.", gold_orders_total)
print("12.", hyderabad_revenue)
print("13.", distinct_users)
print("14.", gold_avg_order)
print("15.", orders_rating_45)
print("16.", orders_top_gold_city)
print("17.", join_orders_users)
print("18.", cuisine_data_format)
print("19.", total_rows)
print("20.", no_matching_user)
print("21.", pandas_function)
print("22.", membership_origin)
print("23.", join_orders_restaurant)
print("24.", food_type_column)
print("25.", user_multiple_orders)
