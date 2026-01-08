import pandas as pd
import json
file_path = "yc_top_20.json"

with open(file_path, 'r') as f:
    raw_data = json.load(f)

print(f"Successfully loaded {len(raw_data)} startups from {file_path}")

df = pd.DataFrame(raw_data)

print(f"DataFrame created with shape: {df.shape}")

print(df.head())

df['batch'] = df['categories'].apply(lambda x: x[0] if len(x) > 0 else "Unknown")

df['industries'] = df['categories'].apply(lambda x: x[1:] if len(x) > 1 else [])

df_clean = df.drop(columns=['categories'])




df_clean['industries'] = df_clean['industries'].apply(
    lambda industry_list: [i.strip().upper() for i in industry_list]
)
print("\n--- NEW SHAPE AND DATA ---")
print(df_clean.shape) 
print(df_clean.head())

def validate_data(df):
    print("\n--- RUNNING DATA QUALITY CHECKS ---")
    
    #  Check for empty data
    if df.empty:
        raise ValueError("FATAL: Scraper returned 0 rows. Pipeline stopped.")
    
    #  Check for null names
    null_names = df['company_name'].isnull().sum()
    if null_names > 0:
        print(f"WARNING: Found {null_names} startups with missing names.")
    
    # Check for the '1000' row expectation
    if len(df) < 1000:
        print(f"NOTICE: Dataset contains {len(df)} rows. Expected ~1000.")

    print("Quality Check Passed: Data is safe to save.")

validate_data(df_clean)

final_command = input("\nType 'yes' to save the cleaned data as a Parquet file: ")
if final_command.lower() == 'yes':
    df_clean.to_parquet("yc_startups_cleaned.parquet", index=False)
    print("\nSuccess! 'yc_startups_cleaned.parquet' is now in your folder.")
else :
    print("\nNo file saved. You can run the script again to save later.")
