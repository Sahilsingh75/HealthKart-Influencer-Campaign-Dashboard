import streamlit as st
import pandas as pd

st.set_page_config(page_title="HealthKart Influencer Dashboard", layout="wide")
st.title("📊 HealthKart Influencer Campaign Dashboard")

# Load CSVs directly from directory
inf_df = pd.read_csv("influencers.csv")
post_df = pd.read_csv("posts.csv")
track_df = pd.read_csv("tracking_data.csv")
payout_df = pd.read_csv("payouts.csv")

# Merge datasets
merged_df = track_df.merge(inf_df, left_on='influencer_id', right_on='ID', how='left')
merged_df = merged_df.merge(payout_df[['influencer_id', 'total_payout']], on='influencer_id', how='left')
merged_df['total_payout'] = merged_df['total_payout'].fillna(0)
merged_df['ROAS'] = merged_df['revenue'] / merged_df['total_payout'].replace(0, 1)

# Grouped metrics
grouped = merged_df.groupby('name').agg({
    'orders': 'sum',
    'revenue': 'sum',
    'total_payout': 'sum',
    'ROAS': 'mean'
}).reset_index()

# Display
st.subheader("Top Influencers by ROAS")
st.dataframe(grouped.sort_values(by='ROAS', ascending=False).head(10))

# Filters
st.sidebar.subheader("Filters")
platform_filter = st.sidebar.multiselect("Platform", options=inf_df['platform'].unique(), default=list(inf_df['platform'].unique()))
gender_filter = st.sidebar.multiselect("Gender", options=inf_df['gender'].unique(), default=list(inf_df['gender'].unique()))

filtered = merged_df[(merged_df['platform'].isin(platform_filter)) & (merged_df['gender'].isin(gender_filter))]

st.subheader("Filtered Influencer Performance")
st.dataframe(filtered[['name', 'platform', 'gender', 'follower_count', 'orders', 'revenue', 'total_payout', 'ROAS']].sort_values(by='ROAS', ascending=False))

# Payouts bar chart
st.subheader("Total Payouts by Influencer")
st.bar_chart(payout_df.set_index('influencer_id')['total_payout'])

# Download
st.download_button("📥 Download Filtered Data", filtered.to_csv(index=False), "filtered_data.csv", "text/csv")
