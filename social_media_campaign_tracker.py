import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("cleaned_facebook_ads.csv")

# -------------------------------
# BASIC KPIs
# -------------------------------
total_spend = df['Amount Spent'].sum()
total_impressions = df['Impressions'].sum()
total_clicks = df['Link Clicks'].sum()
total_checkouts = df['Checkouts Initiated'].sum()
avg_ctr = df['CTR_Calc (%)'].mean()
avg_cpc = df['CPC_Calc'].mean()
avg_roi = df['ROI'].mean()

print("====== KPI SUMMARY ======")
print(f"Total Spend: ₹{total_spend:.2f}")
print(f"Total Impressions: {total_impressions}")
print(f"Total Clicks: {total_clicks}")
print(f"Total Checkouts: {total_checkouts}")
print(f"Average CTR: {avg_ctr:.2f}%")
print(f"Average CPC: ₹{avg_cpc:.2f}")
print(f"Average ROI: {avg_roi:.2f}")

# -------------------------------
# TREND ANALYSIS
# -------------------------------
df['Day'] = pd.to_datetime(df['Day'])

plt.figure()
plt.plot(df['Day'], df['Impressions'])
plt.title("Impressions Over Time")
plt.xlabel("Date")
plt.ylabel("Impressions")
plt.show()

plt.figure()
plt.plot(df['Day'], df['Link Clicks'])
plt.title("Clicks Over Time")
plt.xlabel("Date")
plt.ylabel("Clicks")
plt.show()

plt.figure()
plt.plot(df['Day'], df['Amount Spent'])
plt.title("Ad Spend Over Time")
plt.xlabel("Date")
plt.ylabel("Amount Spent")
plt.show()

# -------------------------------
# PERFORMANCE RELATIONSHIPS
# -------------------------------
plt.figure()
plt.scatter(df['Amount Spent'], df['Link Clicks'])
plt.title("Spend vs Clicks")
plt.xlabel("Amount Spent")
plt.ylabel("Clicks")
plt.show()

plt.figure()
plt.scatter(df['CPC_Calc'], df['CTR_Calc (%)'])
plt.title("CPC vs CTR")
plt.xlabel("CPC")
plt.ylabel("CTR (%)")
plt.show()
