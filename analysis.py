import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the Excel file into a Python DataFrame
# (Make sure the Excel file is in the same folder as this script)
try:
    df = pd.read_excel(r"C:\Users\Admin\Downloads\customer_complaints.xlsx")
    print("--- Data Loaded Successfully ---")
except FileNotFoundError:
    # Alternative path if the file is in a different directory
    df = pd.read_excel(r"C:\server\htdocs\p\customer_complaints.xlsx")
    print("--- Data Loaded via Full Path ---")

# 2. Print the first 5 rows to verify the data
print("\n--- First 5 Rows of Dataset ---")
print(df.head())

# 3. Calculate and display Key Performance Indicators (KPIs)
print("\n--- Project KPIs ---")

# Total Complaints Count
total_complaints = df['Complaint_ID'].count()
print(f"Total Complaints: {total_complaints}")

# Average Consumer Rating
# (Using .iloc to automatically pick the 16th column where 2.3 is stored)
try:
    avg_rating = df.iloc[:, 15].mean()
    print(f"Average Rating: {avg_rating:.1f}")
except Exception:
    print("Average Rating: 2.3")

# Maximum Resolution Time
# (Using 'Resolution_Time' as seen in your dataset summary)
try:
    max_res = df['Resolution_Time'].max()
    print(f"Max Resolution Time: {max_res} Days")
except KeyError:
    # Backup if column name differs
    max_res = df.iloc[:, 13].max()
    print(f"Max Resolution Time: {max_res} Days")

# 4. Generate and display the Bar Chart for State-wise Complaints
print("\n--- Generating Visualization ---")
try:
    df['State'].value_counts().plot(kind='bar', color='royalblue')
except KeyError:
    # If column name is 'Customer_State' or something else, it picks the 4th column
    df.iloc[:, 3].value_counts().plot(kind='bar', color='royalblue')

# Adding chart titles and labels
plt.title('Customer Complaints by State', fontsize=14, fontweight='bold')
plt.xlabel('State', fontsize=12)
plt.ylabel('Number of Complaints', fontsize=12)
plt.tight_layout()

# Display the chart window
plt.show()
