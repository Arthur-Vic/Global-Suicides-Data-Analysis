import pandas as pd
import os

data = pd.DataFrame()

male_path = './MortalityData/Male/'
female_path = './MortalityData/Female/'
unknown_path = './MortalityData/Unknown/'

male_files = os.listdir(male_path)
female_files = os.listdir(female_path)
unknown_files = os.listdir(unknown_path)

male_csvs = [f'{male_path}{file}' for file in male_files if file.endswith('.csv')]
female_csvs = [f'{female_path}{file}' for file in female_files if file.endswith('.csv')]
unknown_csvs = [f'{unknown_path}{file}' for file in unknown_files if file.endswith('.csv')]

#Listing all files (with respective paths) to be processed by pandas
all_csvs = [*male_csvs, *female_csvs, *unknown_csvs]
# print(all_csvs) #Debugging

all_data = []

for csv in all_csvs:
    data = pd.read_csv(csv)
    all_data.append(data)

data_frame = pd.concat(all_data, ignore_index=True)
# print(data_frame)

data_frame.to_csv('complete-data.csv', index=False)