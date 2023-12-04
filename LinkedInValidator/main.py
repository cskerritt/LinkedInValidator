import pandas as pd
import re

def validate_linkedin_url(url):
    """ Validates LinkedIn URL using regex. """
    pattern = r'^https?://((www|\w\w)\.)?linkedin.com/((in/[^/]+/?)|(pub/[^/]+/((\w|\d)+/?){3}))$'
    return bool(re.match(pattern, url))

def validate_excel_file(file_path):
    """ Reads an Excel file, validates LinkedIn URLs, and adds a 'Valid' column. """
    try:
        # Read Excel file
        df = pd.read_excel(file_path)

        # Assuming the column with LinkedIn URLs is named 'LinkedIn_URL'
        # Update the column name as per your Excel file
        if 'LinkedIn_URL' in df.columns:
            # Validate LinkedIn URLs
            df['Valid'] = df['LinkedIn_URL'].apply(validate_linkedin_url)
        else:
            print("Column 'LinkedIn_URL' not found in the Excel file.")
            return

        # Save the updated dataframe to a new Excel file
        output_file_path = file_path.replace('.xlsx', '_validated.xlsx')
        df.to_excel(output_file_path, index=False)
        print(f"Updated file saved as '{output_file_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_excel_file.xlsx' with the path to your Excel file
validate_excel_file('/Users/chrisskerritt/Dropbox/My Mac (chriss-MacBook-Pro.local)/Desktop/LinkedIn-MA.xlsx')
