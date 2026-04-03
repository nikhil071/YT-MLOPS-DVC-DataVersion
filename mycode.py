import pandas as pd 
import os 

# create a sample DataFrames with coloumn names.
data = {
    "name" : ["Alice","bob","charlie"],
    "Age" : [20,30,35],
    "City" : ["NewYork", "losAngeles","chicago"]
}

df = pd.DataFrame(data)

# adding new row to df for v2
new_row_loc = {"name": "GF1", "Age" : 20, "City" : "city1"}
df.loc[len(df.index)] = new_row_loc

# Ensure the data directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

# Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a csv file, including coloumn names
df.to_csv(file_path,index=False)

print(f"csv file saved to {file_path}")
