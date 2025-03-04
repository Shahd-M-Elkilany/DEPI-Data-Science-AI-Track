import pandas as pd
import numpy as np 
df=pd.read_csv(r"F:\AI Courses material\Numpy\googleplaystore.csv")

print(df.size)
print(df.head()) # I checked that the data has been successfully loaded by displaying the first 5 rows using .head()
print(df.describe()) # Checkimg the statics summary of the data and trying to detect visible outliers
print(df.info()) # checking the data types and the null values
print(df.isnull())
#Checking what needs cleaning in each column
print(df['Category'].unique()) # Got 1 null (get rid of '_' , '1.9')
print(df['Rating'].unique()) # Got null values and one outlier (19.)
print(df['Reviews'].unique()) # The wrong data type
print(df['Reviews'].str.isnumeric().sum() )
print(df['Size'].unique()) # The wrong data type (get rid of M, and k)
print(df['Installs'].unique()) # The wrond data type (get rid of + , Free)
print(df['Type'].unique()) # Got 1 null and get rid of (0)
print(df['Price'].unique()) # The wrong data type (get rid of '$', 'Everyone')
print(df['Content Rating'].unique()) # Got 1 null
print(df['Last Updated'].unique()) #Convert to datetime
print(df['Current Ver'].unique()) 
print(df['Current Ver'].str.isnumeric().sum()) # Got null values, The wrong datatype (get rid of 'Varies with device')
print(df['Android Ver'].unique())  # Got null values, The wrong data type ( get rid of "and up",'Varies with device')

#Clean 'Category' column 
df['Category']=df['Category'].str.replace('_',' ').replace('1.9',np.nan) 
df['Category']=df['Category'].fillna(df['Category'].mode()[0])
print('Cleaned Category',df['Category'].unique()) # The cleaned Category column doesnt have _ in between the words, doesnt have numeric values and doesnt have nulls

# Clean 'Rating' column
df['Rating']=df['Rating'].fillna(df['Rating'].median()) 
q1=df['Rating'].quantile(0.25)
q3=df['Rating'].quantile(0.75)
iqr= q3-q1
lower_bound= q1-1.5*iqr
upper_bound= q3+1.5*iqr 
df=df[(df['Rating']>=lower_bound)& (df['Rating']<= upper_bound)]
print('Cleaned Rating',df['Rating'].unique()) # the cleaned dataset doesnt have outliers in rating column nor null values
print(df.size)

# Clean 'Review' column
df['Reviews']= pd.to_numeric(df['Reviews'], errors='coerce')
print('Cleaned Review',df['Reviews'].dtype) # Converted to int 

# Clean 'Size'
def convert_size (size):
   if 'M' in (size):
      return float (size.replace ('M',''))*1024
   elif 'k' in (size):
      return float (size.replace ('k',''))
   else:
      return np.nan if size == 'Varies with device'  else np.nan 

df['Size']= df['Size'].fillna('Varies with device').apply(convert_size)
df['Size'] = df['Size'].fillna(df['Size'].mean())
print('Cleaned Size',df['Size'].unique())
# the cleaned 'Size' column doesnt have null values and is float 


#Clean 'Installs' column
df['Installs']=df['Installs'].str.replace('[+,]', '', regex=True).replace('Free', np.nan).astype(float)
df['Installs']=df['Installs'].fillna(df['Installs'].median())
print('Cleaned Installs',df['Installs'].unique())
print(df['Installs'].dtype)
# the cleaned Installs column is float and doesnt have nulls

#Clean 'Type' column
df['Type']=df['Type'].fillna(df['Type'].mode() [0])
print('Cleaned Type',df['Type'].unique())

# Clean 'Price' column  
df['Price']=df['Price'].str.replace('$','').replace('Everyone', np.nan).astype(float)
print('Cleaned Price',df['Price'].unique())
print(df['Price'].dtype)

#Clean 'Content Rating' column
df = df.dropna(subset=['Content Rating'])



#Clean 'Last Updated' column
df['Last Updated']=pd.to_datetime(df['Last Updated'], errors='coerce')
print(df['Last Updated'].dtype)


# Clean 'Current Ver' 
df['Current Ver'] = df['Current Ver'].replace('Varies with device', np.nan)
df['Current Ver']= df['Current Ver'].fillna(df['Current Ver'].mode())
print(df['Current Ver'].dtype)
print('Cleaned Current Ver',df['Current Ver'].unique())


# Clean 'Android Ver' column get rid of "and up",'Varies with device'
df['Android Ver']= df['Android Ver'].str.replace ('and up','').replace('W','', regex=True).replace ('Varies with device', np.nan)
df['Android Ver']=df['Android Ver'].fillna(df['Android Ver'].mode()[0])
print('Cleaned Andriod Ver',df['Android Ver'].unique())


# Extract the major and minor parts (e.g., '4.0' from '4.0.3 and up')
df['Android Ver'] = df['Android Ver'].str.extract(r'(\d+\.\d+|\d+)')[0]

# What is the most expensive app on the Play Store?
df['Android Ver'] = pd.to_numeric(df['Android Ver'], errors='coerce') 
most_expensive_app = df.loc[df['Price'].idxmax()]
print(most_expensive_app)

#Which genre has the highest number of apps?
highest_genre = df['Category'].value_counts().idxmax()
print(highest_genre)

#What is the average size of free vs. paid apps?
Average_size_vs_type= df.groupby('Type')['Size'].mean()
print(Average_size_vs_type)

#What are the top 5 most expensive apps with a perfect rating (5)?
Perfect_rating= df[df['Rating']==5]
Perfect_most_expencive = Perfect_rating.sort_values('Price',ascending=False).head(5)
print(Perfect_most_expencive)

#How many apps have received more than 50K reviews?
Over_50K_reviews= df[df['Reviews']>50000]
print(Over_50K_reviews)

#What is the average price of apps, grouped by genre and number of installs?
avg_price_genre_installs= df.groupby(['Category','Installs'])['Price'].mean().reset_index()
print('avg_price_genre_installs',avg_price_genre_installs)

#How many apps have a rating higher than 4.7, and what is their average price?
Rating_higher_than4_7= df[df['Rating']>4.7]
Average_price= Rating_higher_than4_7['Price'].mean()
print(Rating_higher_than4_7)
print(Average_price)

#What is Google&#39;s estimated revenue from apps with 5,000,000+ installs?
print(df['Installs'].dtype)
Over_5M_Installs=df[df['Installs']>5000000]
print('Over_5M_Installs',Over_5M_Installs)
Over_5M_Installs['Revenue']= Over_5M_Installs['Price']*Over_5M_Installs['Installs']*0.30
print('Apps with Over 5M Installs:')
print(Over_5M_Installs[['App', 'Price', 'Installs', 'Revenue']])

#What are the maximum and minimum sizes of free vs. paid apps?
print('FreeApps',df[df['Type']=='Free'])
FreeApps_min_size = df['Size'].min()
FreeApps_max_size = df['Size'].max()
print(f"Free Apps Minimum Size: {FreeApps_min_size}")
print(f"Free Apps Maximum Size: {FreeApps_max_size}")


print('PaidApps',df[df['Type']=='Paid'])
PaidApps= df[df['Type']=='Paid']
PaidApps_min_size = PaidApps['Size'].min()
PaidApps_max_size= PaidApps['Size'].max()
print('Paid Apps Minimum Size',PaidApps_min_size)
print('Paid Apps Maximum Size', PaidApps_max_size)

#Is there a correlation between an app’s rating, number of reviews, size, and its price?
correlation_data = df[['Rating', 'Reviews', 'Size', 'Price']]
correlation_data = correlation_data.dropna()
correlation_matrix = correlation_data.corr()
print("Correlation matrix:")
print(correlation_matrix)

#How many apps exist for each type (free/paid) across different content ratings?
apps_per_type_content = df.groupby(['Type', 'Content Rating']).size() #.size() gets the number of rows in a grouped dataframe
print("Apps count for each type across content ratings:")
print(apps_per_type_content)

#How many apps are compatible with Android version 4.x?
android_4x_apps = df[df['Android Ver'].astype(str).str.startswith('4.')]
num_android_4x_apps = android_4x_apps.shape[0]  # Get the number of rows in the filtered DataFrame
print(f"Number of apps compatible with Android version 4.x: {num_android_4x_apps}")


# Export cleaned data 
cleaned_file_path = r"F:\AI Courses material\Numpy\cleanedgoogleplay_data_final.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"Cleaned data saved to {cleaned_file_path}")