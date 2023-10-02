import pandas as pd

data = pd.DataFrame()
data = pd.read_csv('complete-data.csv')

#selecting the data set I am interested in
cleaner_data = data[['Region Name', 'Country Name', 'Year', 'Sex', 'Age Group', 'Number', 'Percentage of cause-specific deaths out of total deaths', 'Death rate per 100 000 population']]

#removing rows where we had missing data
cleaner_data = cleaner_data.dropna()

cleaner_data.to_csv('cleaner-data.csv', index=False)
print(cleaner_data)