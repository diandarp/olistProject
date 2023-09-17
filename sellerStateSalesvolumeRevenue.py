# merge to data and stored df to seler_city_order
seller_city_order = olist_sellers.merge(olist_order_items, on='seller_id', how='inner')
seller_city_order

#add revenue collumn by multipling order item id and price
seller_city_order['revenue'] = seller_city_order['order_item_id'] * seller_city_order['price']
seller_city_order

#show missing value
seller_city_order.isna().sum()

# cek outlier
seller_city_order.describe()

# check outlier histogram in revenue collumn
sns.histplot(data=seller_city_order, x="revenue", bins=100)

# cek outlier with boxplot revenue
sns.boxplot(data=seller_city_order, x='revenue')

# change outlier value with median for revenue
upper_limit_revenue = seller_city_order['revenue'].quantile(q=0.75) * 1.5
median_revenue = seller_city_order['revenue'].median() # to find median
seller_city_order.loc[seller_city_order['revenue'] > upper_limit_revenue, 'revenue'] = median_revenue #replace new revenue
seller_city_order

#check duplicate
seller_city_order.duplicated(keep=False)

# check if any duplicate in collumn
seller_city_order[seller_city_order.duplicated(keep=False)]

# check unique value on seller city collumn
seller_city_order['seller_city'].unique()

# check unique value on seller state collumn
seller_city_order['seller_state'].unique()

#check value count for seller city
seller_city_order['seller_city'].value_counts()

#check value count for seller state
seller_city_order['seller_state'].value_counts()

# to show how many item sold as per seller city
city_order_item = seller_city_order.groupby('seller_city')['order_item_id'].sum().reset_index()
city_order_item = city_order_item.sort_values(by='order_item_id', ascending=False)
city_order_item

# to show how many item sold as per seller state
state_order_item = seller_city_order.groupby('seller_state')['order_item_id'].sum().reset_index()
state_order_item = state_order_item.sort_values(by='order_item_id', ascending=False)
state_order_item

# visualize top 5 seller city as per order item
top_5_city = city_order_item.head(5)
plt.figure(figsize=(10, 6))
plt.barh(top_5_city['seller_city'], top_5_city['order_item_id'], color='skyblue')
plt.xlabel('Total Quantity Sold')
plt.ylabel('Seller City')
plt.title('Top 5 Seller City by Total Quantity Sold')
plt.gca().invert_yaxis()  # Invert the y-axis for better readability
plt.show()

# visualize top 5 seller state as per order item
top_5_state = state_order_item.head(5)
plt.figure(figsize=(10, 6))
plt.barh(top_5_state['seller_state'], top_5_state['order_item_id'], color='skyblue')
plt.xlabel('Total Quantity Sold')
plt.ylabel('Seller state')
plt.title('Top 5 Seller State by Total Quantity Sold')
plt.gca().invert_yaxis()  # Invert the y-axis for better readability
plt.show()

# to show revenue as per cities
revenue_cities = seller_city_order.groupby('seller_city')['revenue'].sum().reset_index()
revenue_cities = revenue_cities.sort_values(by='revenue', ascending=False)
revenue_cities

# visualize top 10 cities as per revenue
revenue_cities_sorted = revenue_cities.sort_values(by='revenue', ascending=False)  # Sort by revenue
top_10_cities = revenue_cities_sorted.head(10)  # Select the top 10 cities with the highest revenue

# Further sort the top 10 cities by revenue in descending order
top_10_cities = top_10_cities.sort_values(by='revenue', ascending=True)

plt.figure(figsize=(12, 6))
plt.barh(top_10_cities['seller_city'], top_10_cities['revenue'], color='skyblue')
plt.xlabel('Total Revenue')
plt.ylabel('Seller City')
plt.title('Top 10 Cities by Total Revenue')

plt.show()

# to show revenue as per states
revenue_states = seller_city_order.groupby('seller_state')['revenue'].sum().reset_index()
revenue_states = revenue_states.sort_values(by='revenue', ascending=False)
revenue_states

# visualize top 10 states as per revenue
revenue_states_sorted = revenue_states.sort_values(by='revenue', ascending=False)  # Sort by revenue
top_10_states_revenue = revenue_states_sorted.head(10)  # Select the top 10 states with the highest revenue

# Further sort the top 10 cities by revenue in descending order
top_10_states_revenue = top_10_states_revenue.sort_values(by='revenue', ascending=True)

plt.figure(figsize=(12, 6))
plt.barh(top_10_states_revenue['seller_state'], top_10_states_revenue['revenue'], color='skyblue')
plt.xlabel('Total Revenue')
plt.ylabel('Seller State')
plt.title('Top 10 State by Total Revenue')

plt.show()