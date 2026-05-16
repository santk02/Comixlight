# 1. The Libraries
import requests
import pandas as pd
import sqlite3

# 2. The Handshake
source_url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(source_url)

# Audit the connection
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    # 3. The Extraction & Conversion
    raw_json_data = response.json()
    api_df = pd.DataFrame(raw_json_data)
    
    # Print the first 5 rows (The Python equivalent of PROC PRINT(OBS=5))
    print("\nData Preview:")
    print(api_df.head())

    # 4. The Database Bridge (The "Load" step)
    # This creates the file 'comixlight_vault.db' if it doesn't exist yet
    # Think of this as defining a permanent library path
    conn = sqlite3.connect('comixlight_vault.db')
    
    # Transfer the dataframe into the SQL vault
    # If we run this script twice, 'replace' prevents duplicate rows
    api_df.to_sql('raw_test_data', con=conn, if_exists='replace', index=False)
    
    # Close the vault door
    conn.close()
    
    print("\nSuccess: Data secured in Comixlight Vault.")

else:
    print("Error: The Waiter dropped the food (Connection Failed).")