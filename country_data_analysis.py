import numpy as np
import pandas as pd

# Path to your CSV file in the Download folder
file_path = '/storage/emulated/0/Download/Countries.csv'

try:
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Print rows to check if it loaded correctly
    print(df)
    #Tell how many row and columns are there
    print(df.shape)
    #Give the information of readed csv file 
    print(df.info())
    #Give count,mean,std,min,25%,50%,75%,max
    print(df.describe())
    #which country have the highest population
    print(df[df['population'] == df['population'].max()]['country'])
    #what is the capital of the country with highrst population 
     print(df[df['population'] == df['population'].max()]['capital_city'])
    #which country had the least population 
    print(df[df['population'] == df['population'].min()]['country'])
    #which is the capital of the country with least population
    print(df[df['population'] == df['population'].min()]['capital_city'])
    #head() function
    print(df.head())
    #give me top 5 countries with highest democratic score 
    df.sort_values(by='democracy_score',ascending=False,inplace=True)
    print(df['country'].head())
    #how many total regions are there 
    print(df['region'].value_counts().count())
    #how many countries lie in Eastern Europe region
    print(df[df['region'] == "Eastern Europe"]['country'])
    #who is the political leader of the 2nd highest popuated country 
    print(df[df['population'] == df['population'].nlargest(2).iloc[1]]['political_leader'])
    #how many countries are there whoes political leaders are unknown 
    print(df[df['political_leader'].isna()]['country'].count())
    #how many country have Repulic in their full name 
    count=0
    def counting(txt):
    	global count 
    	if 'republic' in txt.lower():
    		count+=1
    df['country_long'] = df['country_long'].apply(counting)
    print(count)
    

except FileNotFoundError:
    print(f"Error: Could not find the file at: {file_path}")
    print("Please double-check that 'Countries.csv' is in your Download folder and that Pydroid has storage permission.")
except Exception as e:
    print(f"An error occurred: {e}")
    

