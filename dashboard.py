import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Social Media Campaign Tracker", layout="wide")

st.title("📊 Social Media Campaign Performance Tracker")

# -----------------------
# LOAD DATA SAFELY
# -----------------------
try:
    df = pd.read_csv("cleaned_facebook_ads.csv")  # ← IMPORTANT: use exact filename
    df['Day'] = pd.to_datetime(df['Day'])
    st.success("✅ Data loaded successfully")
except Exception as e:
    st.error("❌ Error loading data")
    st.code(e)
    st.stop()

# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------
st.sidebar.header("🔍 Filters")

start_date = st.sidebar.date_input(
    "Start Date", df['Day'].min()
)
end_date = st.sidebar.date_input(
    "End Date", df['Day'].max()
)

filtered_df = df[
    (df['Day'] >= pd.to_datetime(start_date)) &
    (df['Day'] <= pd.to_datetime(end_date))
]

# --------------------------------------------------
# DAILY AGGREGATION (IMPORTANT)
# --------------------------------------------------
daily = filtered_df.groupby('Day', as_index=False).sum()


# -----------------------
# SHOW RAW DATA (TEST)
# -----------------------
st.subheader("🔍 Sample Data")
st.dataframe(df.head())

# -----------------------
# KPI SECTION
# -----------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Spend (₹)", f"{df['Amount Spent'].sum():.2f}")
col2.metric("Total Impressions", int(df['Impressions'].sum()))
col3.metric("Total Clicks", int(df['Link Clicks'].sum()))
col4.metric("Total Checkouts", int(df['Checkouts Initiated'].sum()))

# -----------------------
# AGGREGATE DATA (FIX ZIG-ZAG)
# -----------------------
daily_df = df.groupby('Day', as_index=False).sum()

# -----------------------
# CHARTS
# -----------------------
st.subheader("📈 Performance Trends")

fig1 = px.line(daily_df, x='Day', y='Impressions', title='Daily Impressions')
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.line(daily_df, x='Day', y='Link Clicks', title='Daily Clicks')
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.line(daily_df, x='Day', y='Amount Spent', title='Daily Spend')
st.plotly_chart(fig3, use_container_width=True)


# --------------------------------------------------
# COST EFFICIENCY
# --------------------------------------------------
st.subheader("💰 Cost Efficiency")

fig4 = px.scatter(
    filtered_df,
    x="CPC_Calc",
    y="CTR_Calc (%)",
    size="Amount Spent",
    color="Checkouts Initiated",
    title="CPC vs CTR (Bubble Size = Spend)"
)

st.plotly_chart(fig4, use_container_width=True)


st.subheader("🚦 Performance Classification")

filtered_df['Performance'] = filtered_df['ROI'].apply(
    lambda x: "Good" if x > 0 else "Poor"
)

fig = px.bar(
    filtered_df,
    x='Day',
    y='Amount Spent',
    color='Performance',
    title='Spend by Performance'
)

st.plotly_chart(fig, use_container_width=True)



# --------------------------------------------------
# BUSINESS INSIGHTS
# --------------------------------------------------
st.subheader("🧠 Business Insights")

st.markdown("""
- 📉 High CPC with low CTR indicates inefficient targeting.
- 💡 Engagement is higher than conversions → landing page optimization needed.
- 🚀 Budget should be shifted to low CPC, high CTR days.
- ⛔ Poor ROI days should be paused or creatives improved.
""")