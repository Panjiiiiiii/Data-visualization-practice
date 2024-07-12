import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

customers_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/customers.csv")
customers_df.head()

orders_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/orders.csv")
orders_df.head()

product_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/products.csv")
product_df.head()

sales_df = pd.read_csv("https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/DicodingCollection/sales.csv")
sales_df.head()

#EDA DATA CUSTOMER AND ORDERS
customers_df.describe(include="all")
orders_df.describe(include="all")

#EDA group by gender
group_by_gender = customers_df.groupby(by="gender").agg({
    "customer_id" : "nunique",
    "age" : ["max", "min", "mean", "std"]
})
# print(group_by_gender)

#EDA by group by city and state
group_by_city = customers_df.groupby(by="city").customer_id.nunique().sort_values(ascending=False)
group_by_state = customers_df.groupby(by="state").customer_id.nunique().sort_values(ascending=True)
# print(group_by_city)
# print(group_by_state)

#EDA by delivery time
# delivery_time = orders_df['delivery_date'] - orders_df['order_date']
# delivery_time = delivery_time.apply(lambda x: x.total_seconds())
# orders_df["delivery_time"] = round(delivery_time/86400)

#EDA by active user
customers_id_in_orders_df = orders_df.customer_id.tolist()
customers_df["status"] = customers_df["customer_id"].apply(lambda x: "Active" if x in customers_id_in_orders_df else "Non Active")
active_pivot_table = customers_df.groupby("status").customer_id.count()
# print(active_pivot_table)

#EDA JOIN ORDER_DF AND CUSTOMER_DF
order_customer_df = pd.merge(
    left=orders_df,
    right=customers_df,
    how="left",
    left_on="customer_id",
    right_on="customer_id"
)
# print(order_customer_df.head())

#EDA COUNT DATA ORDER BY CITY
group_by_city = order_customer_df.groupby(by="city").order_id.nunique().sort_values(ascending=False).reset_index().head(10)
#print(group_by_city)

#EDA COUNT DATA ORDER BY STATE
group_by_state = order_customer_df.groupby(by="state").order_id.nunique().sort_values(ascending=False)
# print(group_by_state)

#EDA COUNT DATA ORDER BY GENDER
group_by_gender = order_customer_df.groupby(by="gender").order_id.nunique().sort_values(ascending=False)
# print(group_by_gender)

#EDA COUNT DATA ORDER BY AGE
order_customer_df["age_group"] = order_customer_df.age.apply(lambda x: "Youth" if x <= 24 else ("Seniors" if x > 64 else "Adults"))
group_by_age = order_customer_df.groupby(by="age_group").order_id.nunique().sort_values(ascending=False)
# print(group_by_age)

#EDA DATA PRODUCT AND SALES
product_df.describe(include='all')
sales_df.describe(include='all')

#EDA sort price product
price_product = product_df.sort_values(by="price", ascending=False)
# print(price_product)

#EDA product and type
product_type = product_df.groupby(by="product_type").agg({
    "product_id" : "nunique",
    "quantity" : "sum",
    "price" : ["min", "max"]
})

product_name = product_df.groupby(by="product_name").agg({
    "product_id" : "nunique",
    "quantity" : "sum",
    "price" : ["min", "max"]
})
# print(product_type)
# print(product_name)

#EDA best selling product
sales_product_df = pd.merge(
    left=sales_df,
    right=product_df,
    how="left",
    left_on="product_id",
    right_on="product_id"
)
# print(sales_product_df.head())

#EDA sales basic on product
sales_product_type = sales_product_df.groupby(by="product_type").agg({
    'sales_id' : 'nunique',
    "quantity_x" : "sum",
    "total_price" : "sum"
})
# print(sales_product_type)
sales_product_name = sales_product_df.groupby(by="product_name").agg({
    'sales_id' : 'nunique',
    "quantity_x" : "sum",
    "total_price" : "sum"
}).sort_values(by="total_price", ascending=False).reset_index().head(6)
# print(sales_product_name)

#EDA all data
all_df = pd.merge(
    left=sales_product_df,
    right=order_customer_df,
    how="left",
    left_on="order_id",
    right_on="order_id"
)
# print(all_df.head())

#EDA preference by state
preference_state = all_df.groupby(by=["state", "product_type"]).agg({
    "quantity_x" : "sum",
    "total_price" : "sum"
})
# print(preference_state)

#EDA preference by gender
preference_gender = all_df.groupby(by=["gender", "product_type"]).agg({
    "quantity_x" : "sum",
    "total_price" : "sum"
})
# print(preference_gender)

#EDA preference by age
preference_age = all_df.groupby(by=["age_group", "product_type"]).agg({
    "quantity_x" : "sum",
    "total_price" : "sum"
})
# print(preference_age)

all_df['order_date'] = pd.to_datetime(all_df['order_date'])

#Explanatory DATA
monthly_orders_df = all_df.resample(rule='ME', on='order_date').agg({
    "order_id": "nunique",
    "total_price": "sum"
})
monthly_orders_df.index = monthly_orders_df.index.strftime('%Y-%m')
monthly_orders_df = monthly_orders_df.reset_index()
monthly_orders_df.rename(columns={
    "order_id": "order_count",
    "total_price": "revenue"
}, inplace=True)
# print(monthly_orders_df.head())

#order/month chart
plt.figure(figsize=(10, 5))
plt.plot(
    monthly_orders_df["order_date"],
    monthly_orders_df["order_count"],
    marker='o',
    linewidth=2,
    color="#72BCD4"
)
plt.title("Number of Orders per Month (2021)", loc="center", fontsize=20)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

#validate data
plt.figure(figsize=(10, 5))
plt.plot(
    monthly_orders_df["order_date"],
    monthly_orders_df["revenue"],
    marker='o',
    linewidth=2,
    color="#72BCD4"
)
plt.title("Number of Orders per Month (2021)", loc="center", fontsize=20)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

#make 2 charts best and worst products
sum_order_items_df = all_df.groupby("product_name")["quantity_x"].sum().sort_values(ascending=False).reset_index()
print(sum_order_items_df.head(15))
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
# Plotting best performing products
sns.barplot(x="quantity_x", y="product_name", data=sum_order_items_df.head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Best Performing Product", loc="center", fontsize=15)
ax[0].tick_params(axis='y', labelsize=12)
# Plotting worst performing products
sns.barplot(x="quantity_x", y="product_name", data=sum_order_items_df.sort_values(by="quantity_x", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Worst Performing Product", loc="center", fontsize=15)
ax[1].tick_params(axis='y', labelsize=12)
plt.suptitle("Best and Worst Performing Product by Number of Sales", fontsize=20)
plt.show()

#plotting by gender
bygender_df = all_df.groupby(by="gender").customer_id.nunique().reset_index()
bygender_df.rename(columns={
    "customer_id": "customer_count"
}, inplace=True)

plt.figure(figsize=(10, 5))

sns.barplot(
    y="customer_count",
    x="gender",
    data=bygender_df.sort_values(by="customer_count", ascending=False),
    palette=colors
)
plt.title("Number of Customer by Gender", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
plt.show()

#plotting by age
byage_df = all_df.groupby(by="age_group").customer_id.nunique().reset_index()
byage_df.rename(columns={
    "customer_id": "customer_count"
}, inplace=True)
byage_df
byage_df['age_group'] = pd.Categorical(byage_df['age_group'], ["Youth", "Adults", "Seniors"])
plt.figure(figsize=(10, 5))
colors_ = ["#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    y="customer_count",
    x="age_group",
    data=byage_df.sort_values(by="age_group", ascending=False),
    palette=colors_
)
plt.title("Number of Customer by Age", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
plt.show()

#plotting by states
bystate_df = all_df.groupby(by="state").customer_id.nunique().reset_index()
bystate_df.rename(columns={
    "customer_id": "customer_count"
}, inplace=True)
bystate_df
plt.figure(figsize=(10, 5))
colors_ = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x="customer_count",
    y="state",
    data=bystate_df.sort_values(by="customer_count", ascending=False),
    palette=colors_
)
plt.title("Number of Customer by States", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=12)
plt.show()

#rfm analysis
rfm_df = all_df.groupby(by="customer_id", as_index=False).agg({
    "order_date" : "max",
    "order_id" : "nunique",
    "total_price" : "sum"
})
rfm_df.columns = ["customer_id", "max_order_timestamp", "frequency", "monetary"]
orders_df['order_date'] = pd.to_datetime(orders_df['order_date'])
rfm_df["max_order_timestamp"] = rfm_df["max_order_timestamp"].dt.date
recent_date = orders_df["order_date"].dt.date.max()
rfm_df["recency"] = rfm_df["max_order_timestamp"].apply(lambda x: (recent_date - x).days)
rfm_df.drop("max_order_timestamp", axis=1, inplace=True)
print(rfm_df.head())

#best customer based on rfm
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(30, 6))

colors = ["#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4"]

sns.barplot(y="recency", x="customer_id", data=rfm_df.sort_values(by="recency", ascending=True).head(5), palette=colors,
            ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("By Recency (days)", loc="center", fontsize=18)
ax[0].tick_params(axis='x', labelsize=15)

sns.barplot(y="frequency", x="customer_id", data=rfm_df.sort_values(by="frequency", ascending=False).head(5),
            palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].set_title("By Frequency", loc="center", fontsize=18)
ax[1].tick_params(axis='x', labelsize=15)

sns.barplot(y="monetary", x="customer_id", data=rfm_df.sort_values(by="monetary", ascending=False).head(5),
            palette=colors, ax=ax[2])
ax[2].set_ylabel(None)
ax[2].set_xlabel(None)
ax[2].set_title("By Monetary", loc="center", fontsize=18)
ax[2].tick_params(axis='x', labelsize=15)

plt.suptitle("Best Customer Based on RFM Parameters (customer_id)", fontsize=20)
plt.show()