import pandas as pd

def category(dfs):
    f = {
        "Food": ["Jolibee", "Mcdo", "Pizza Hut", "Taco Bell", "KFC", "Starbucks", "7-Eleven"],
        "Clothing": ["Zara", "Gucci", "Louis Vuitton", "Prada", "Balenciaga","Shopee"],
        "Entertainment": ["Netflix", "Amazon Prime", "Disney", "Hulu", "Hbo"],
        "Transportation": ["Grab"],
        "Utilities": ["Electricity", "Gas", "Water", "Internet", "Phone"],
        "Cash Transfer": ["Paypal", "Transfer", "GCash", "Check", "Debit Card", "Maya"],
        "Others": ["Salary", "Load", "Drug"]
    }
    dfs["Categories"] = "Others" 
    for category, keywords in f.items():
        for word in keywords:
            match = df["Description"].str.contains(word, case=False)
            dfs.loc[match, "Categories"] = category
    return dfs

df = pd.read_csv('trial.csv', engine='python', on_bad_lines='skip')
df["Description"] = df["Description"].astype(str).str.strip()
df['Amount'] = df['Amount'].astype(str).str.replace(',', '', regex=False).str.strip().astype(float)
df['Date'] = pd.to_datetime(df['Date'])



total = df[df['Amount'] > 0]['Amount'].sum()
expense = df[df['Amount'] < 0]['Amount'].sum()
net = total + expense
 
df = category(df)

print("**SUMMARY OF MONTH EXPENSES**")
print()
print(f"Gross: {total}")
print(f"Expense: {expense}")
print(f"Net: {net}")    
print()
print("**TRANSACTIONS**")
print()
print(df.groupby("Categories")['Amount'].sum().sort_values())
    