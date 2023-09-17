import pandas as pd # for dataframe
import matplotlib.pyplot as plt # for visualization
import seaborn as sns

# merge product ordered df with order review to show average review in per category of product
product_ordered_review = product_ordered.merge(olist_order_review, on='order_id', how='inner')
product_ordered_review

# check missing value 
product_ordered_review.isna().sum()

# cek outlier with statistic descriptive
product_ordered_review.describe()

# to find average score for each product category
review_score_mean = product_ordered_review.groupby('product_category_name')['review_score'].mean().reset_index()
review_score_mean

# Select the top 5 review per category
top_5_review = review_score_mean.nlargest(5, 'review_score')
top_5_review

# Create a bar chart to visualize the top 5 review per category
plt.figure(figsize=(10, 6))
plt.barh(top_5_review['product_category_name'], top_5_review['review_score'])
plt.xlabel('Average Review Score')
plt.ylabel('Product Category')
plt.title('Top 5 Rated Product Category')
plt.gca().invert_yaxis()  # Invert the y-axis for better readability
plt.show()
