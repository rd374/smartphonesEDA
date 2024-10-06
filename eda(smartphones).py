## EDA on smartphone dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv("C:/Users/DELL/OneDrive/Desktop/SQL/smartphone_cleaned_v5.csv")
df.head()
df.shape
df.info()
# speculative model on basis of price
df['brand_name'].value_counts()
top_brands = df['brand_name'].value_counts().head(10)

# Create a bar chart with customized aesthetics
plt.figure(figsize=(8,6))  # Set figure size for a better aspect ratio
top_brands.plot(kind='bar', color='lightcoral', edgecolor='black', alpha=0.8)

# Adding a title and labels with a cute style
plt.title('Top 5 Brand Names', fontsize=18, fontweight='bold', color='teal')
plt.xlabel('Brand Name', fontsize=14, color='slategray')
plt.ylabel('Count', fontsize=14, color='slategray')

# Customize the ticks on x and y axes
plt.xticks(rotation=45, fontsize=12, color='purple')
plt.yticks(fontsize=12, color='purple')

# Add a grid for clarity
plt.grid(True, which='both', axis='y', linestyle='--', alpha=0.5)

# Show the plot
plt.tight_layout()  # Adjust layout to avoid clipping
plt.show()


top_brands.plot(kind='pie', autopct='%1.1f%%', figsize=(8,8), colors=['lightblue', 'lightcoral', 'lightgreen', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightgoldenrodyellow', 'lightcyan', 'lavender', 'peachpuff'], startangle=90)

# Customize the chart
plt.title('Top 10 Brand Names Distribution', fontsize=16, fontweight='bold', color='teal')
plt.ylabel('')  # Remove the y-label for better appearance
plt.axis('equal')  # Ensures the pie is drawn as a circle

# Show the plot
plt.tight_layout()
plt.show()

# price
df['price'].describe()
#  32520 avg is too much 
# not normal distribution
sns.displot(kind='hist',data=df,x='price',kde=True)
df['price'].skew()
# highly skewed
# huge outliers
sns.set(style="whitegrid")

# Create a boxplot for the 'price' column with some appealing customizations
plt.figure(figsize=(10,6))
sns.boxplot(x=df['price'], color='lightcoral', fliersize=5, linewidth=2)

# Adding a title and labels
plt.title('Price Distribution', fontsize=18, fontweight='bold', color='teal')
plt.xlabel('Price', fontsize=14, color='slategray')

# Customize the x-axis tick labels
plt.xticks(fontsize=12, color='purple')

# Add a grid for clarity
plt.grid(True, which='both', axis='y', linestyle='--', alpha=0.5)

# Show the plot
plt.tight_layout()
plt.show()
# lets study the outliers
df[df['price']<250000]
# for a speculative model (these outlier have no metrics acc to phone feature)
# we'd remove the outliers

df['price'].describe()
df['rating'].describe()
# rating (normal+ almost low skewness)
sns.displot(kind='hist',data=df,x='rating',kde=True)
df['rating'].skew()

df['rating'].isnull().sum()
# distribution is near to normal
#has_5G
has_5g_counts = df['has_5g'].value_counts()

# Create a pie chart with customizations
plt.figure(figsize=(8,8))
has_5g_counts.plot(kind='pie', 
                   autopct='%1.1f%%',  # Display percentage on the pie
                   colors=['lightgreen', 'lightblue'],  # Colors for the pie chart
                   startangle=90,  # Start the first wedge at 90 degrees
                   explode=[0.05, 0],  # Slightly "explode" the first slice for emphasis
                   shadow=True)  # Add a shadow for a 3D effect

# Adding a title and removing the y-label for a cleaner look
plt.title('5G Support Distribution', fontsize=16, fontweight='bold', color='teal')
plt.ylabel('')  # Remove the default y-label

# Ensuring the pie chart is a circle
plt.axis('equal')

# Display the plot
plt.tight_layout()
plt.show()


# has_nfc
has_nfc_counts = df['has_nfc'].value_counts()

# Create a pie chart with customizations
plt.figure(figsize=(8,8))
has_nfc_counts.plot(kind='pie', 
                   autopct='%1.1f%%',  # Display percentage on the pie
                   colors=['lightgreen', 'lightblue'],  # Colors for the pie chart
                   startangle=90,  # Start the first wedge at 90 degrees
                   explode=[0.05, 0],  # Slightly "explode" the first slice for emphasis
                   shadow=True)  # Add a shadow for a 3D effect

# Adding a title and removing the y-label for a cleaner look
plt.title('NFC Support Distribution', fontsize=16, fontweight='bold', color='teal')
plt.ylabel('')  # Remove the default y-label

# Ensuring the pie chart is a circle
plt.axis('equal')

# Display the plot
plt.tight_layout()
plt.show()

# has_ir_blaster
has_ir_blaster_counts = df['has_ir_blaster'].value_counts()

# Create a pie chart with customizations
plt.figure(figsize=(8,8))
has_ir_blaster_counts.plot(kind='pie', 
                           autopct='%1.1f%%',  # Display percentages on the chart
                           colors=['lightpink', 'lightsteelblue'],  # Choose soft colors
                           startangle=90,  # Start the first wedge at 90 degrees
                           explode=[0.05, 0],  # Slightly "explode" the first slice
                           shadow=True)  # Add a shadow for a 3D effect

# Adding a title and removing the y-label
plt.title('IR Blaster Availability', fontsize=16, fontweight='bold', color='darkblue')
plt.ylabel('')  # Remove the default y-label for a cleaner look

# Ensuring the pie chart is a perfect circle
plt.axis('equal')

# Display the plot
plt.tight_layout()
plt.show()
# mostly chinese phones has this feature of IR blaster(devices control)
df[df['has_ir_blaster']==True]['brand_name'].value_counts()

# Get the top 5 processor brands by their value counts
top_processor_brands = df['processor_brand'].value_counts().head()

# Create a pie chart with customizations
plt.figure(figsize=(8,8))
top_processor_brands.plot(kind='pie', 
                          autopct='%1.1f%%',  # Display percentages on the pie
                          colors=['lightcoral', 'lightblue', 'lightgreen', 'lightpink', 'lightskyblue'],  # Custom colors
                          startangle=90,  # Start the first wedge at 90 degrees
                          explode=[0.05, 0, 0, 0, 0],  # Explode the first slice slightly
                          shadow=True)  # Add a shadow for a 3D effect

# Adding a title and removing the y-label
plt.title('Top 5 Processor Brands Distribution', fontsize=16, fontweight='bold', color='teal')
plt.ylabel('')  # Remove the default y-label for a cleaner look

# Ensuring the pie chart is a perfect circle
plt.axis('equal')

# Display the plot
plt.tight_layout()
plt.show()

fast_charging_available = df['fast_charging_available'].value_counts()

plt.figure(figsize=(8,8))
fast_charging_available.plot(kind='pie', 
                             autopct='%1.1f%%',  # Show percentages on the chart
                             colors=['lightgreen', 'lightcoral'],  # Custom soft colors
                             startangle=90,  # Start the pie chart at 90 degrees
                             explode=[0.05, 0],  # Slightly explode the first slice
                             shadow=True)  # Add a shadow for a 3D effect

# Adding a title and removing the y-label
plt.title('Fast Charging Availability', fontsize=16, fontweight='bold', color='darkblue')
plt.ylabel('')  # Remove the default y-label

# Ensuring the pie chart is a circle
plt.axis('equal')

# Display the plot
plt.tight_layout()
plt.show()

# total cameras+
total_cameras = (df['num_rear_cameras'] + df['num_front_cameras'])

# Get the value counts for the total number of cameras
camera_counts = total_cameras.value_counts()

# Create a pie chart with customizations
plt.figure(figsize=(8,8))
camera_counts.plot(kind='pie', 
                   autopct='%1.1f%%',  # Display percentages on the chart
                   colors=['lightcoral', 'lightblue', 'lightgreen', 'lightpink', 'lightyellow'],  # Custom soft colors
                   startangle=90,  # Start the pie chart at 90 degrees
                   explode=[0.05] + [0] * (len(camera_counts) - 1),  # Explode the first slice slightly
                   shadow=True)  # Add a shadow for a 3D effect

# Adding a title and removing the y-label
plt.title('Distribution of Total Number of Cameras', fontsize=16, fontweight='bold', color='teal')
plt.ylabel('')  # Remove the default y-label

# Ensuring the pie chart is a circle
plt.axis('equal')

# Display the plot
plt.tight_layout()
plt.show()

# android is the dominant player

os_counts = df['os'].value_counts()

# Create a pie chart with customizations
plt.figure(figsize=(8,8))
os_counts.plot(kind='pie', 
               autopct='%1.1f%%',  # Display percentages on the chart
               colors=['lightblue', 'lightgreen', 'lightcoral', 'lightpink', 'lightskyblue'],  # Custom colors
               startangle=90,  # Start the pie chart at 90 degrees
               explode=[0.05] + [0] * (len(os_counts) - 1),  # Slightly explode the first slice
               shadow=True)  # Add a shadow for a 3D effect

# Adding a title and removing the y-label
plt.title('Operating System Distribution', fontsize=16, fontweight='bold', color='darkblue')
plt.ylabel('')  # Remove the default y-label

# Ensuring the pie chart is a circle
plt.axis('equal')

# Display the plot
plt.tight_layout()
plt.show()
# extended memory available in 64% phones
# Get the value counts for the 'extended_memory_available' column
extended_memory_counts = df['extended_memory_available'].value_counts()

# Create a pie chart with customizations
plt.figure(figsize=(8, 8))
extended_memory_counts.plot(kind='pie', 
                             autopct='%1.1f%%',  # Display percentages on the pie
                             colors=['lightgreen', 'lightcoral'],  # Choose soft colors
                             startangle=90,  # Start the first wedge at 90 degrees
                             explode=[0.05] + [0],  # Slightly explode the first slice
                             shadow=True)  # Add a shadow for a 3D effect

# Adding a title and removing the y-label
plt.title('Extended Memory Availability', fontsize=16, fontweight='bold', color='teal')
plt.ylabel('')  # Remove the default y-label for a cleaner look

# Ensuring the pie chart is a perfect circle
plt.axis('equal')

# Display the plot
plt.tight_layout()
plt.show()

## 
# numerical columns 
# def plot_graphs(column_name):
#     sns.displot(kind='hist',kde=True,data=df,x=column_name,label=column_name)
#     sns.catplot(kind='box',data=df,x= column_name)

# num_columns=df.select_dtypes(include=['float64','int64']).iloc[:,[3,4,6,9,13,14,16]].columns

# for col in num_columns:
#     plot_graphs(col)

# Define a function to plot histograms and boxplots
def plot_graphs(column_name):
    plt.figure(figsize=(12, 6))  # Set the figure size for better visibility

    # Histogram with KDE
    plt.subplot(1, 2, 1)  # Create a subplot for the histogram
    sns.histplot(data=df, x=column_name, kde=True)  # Use histplot for better compatibility
    plt.title(f'Histogram of {column_name}')  # Title for histogram
    plt.xlabel(column_name)  # X-axis label
    plt.ylabel('Frequency')  # Y-axis label

    # Boxplot
    plt.subplot(1, 2, 2)  # Create a subplot for the boxplot
    sns.boxplot(data=df, x=column_name)
    plt.title(f'Boxplot of {column_name}')  # Title for boxplot
    plt.xlabel(column_name)  # X-axis label

    # Adjust layout and show the plots
    plt.tight_layout()
    plt.show()

# Select numerical columns for plotting
num_columns = df.select_dtypes(include=['float64', 'int64']).iloc[:, [3, 4, 6, 9, 13, 14, 16]].columns

# Loop through each numerical column and plot graphs
for col in num_columns:
    plot_graphs(col)

#processor speed no outliers(i model)
#battery speed has outlier
#fast charging seems like shifted(outliers)
#
sns.heatmap(df.corr())
df.corr()['price']
#missing value
df.isnull().sum()
df.corr()['rating']
# knn imputer
x_df = df.select_dtypes(include=['int64','float64']).drop(columns='price')

from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=5)
x_df_values = imputer.fit_transform(x_df)
x_df = pd.DataFrame(x_df_values,columns=x_df.columns)
x_df['price'] = df['price']

a = x_df.corr()['price'].reset_index()
b = df.corr()['price'].reset_index()

b.merge(a,on='index')


#self

#self
#outliers: 
df= df[df['price']<200000]
pd.set_option('display.max_columns', None)

df['rating'].skew()
df[df['rating']<70].count()
df['processor_speed'].skew()

df['battery_capacity'].skew()




















