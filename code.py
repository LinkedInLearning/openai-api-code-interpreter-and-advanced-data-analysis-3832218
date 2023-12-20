
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from the file
file_path = 'your_file_path.csv'
data = pd.read_csv(file_path)

# Parse the 'Purchase Date' column to datetime
data['Purchase Date'] = pd.to_datetime(data['Purchase Date'])

# Extract year and month from the 'Purchase Date'
data['Year'] = data['Purchase Date'].dt.year
data['Month'] = data['Purchase Date'].dt.month

# Calculate the average rating for each month and year combination
avg_ratings = data.groupby(['Year', 'Month'])['Rating'].mean().unstack(level=0)

# Create the heatmap
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(avg_ratings, annot=True, fmt=".2f", cmap="YlGnBu")

# Set the labels and title of the heatmap
plt.xlabel("Year")
plt.ylabel("Month")
plt.title("Average Customer Ratings by Month and Year")

# Save the heatmap image
heatmap_image_path = 'heatmap_customer_ratings.png'
plt.savefig(heatmap_image_path)
