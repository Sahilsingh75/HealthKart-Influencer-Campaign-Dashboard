#!/usr/bin/env python
# coding: utf-8

# In[1]:


# data_simulation.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)

# Influencer Data
platforms = ['Instagram', 'YouTube', 'Twitter']
categories = ['Fitness', 'Nutrition', 'Lifestyle']
genders = ['Male', 'Female', 'Other']

influencers = pd.DataFrame({
    'ID': range(1, 21),
    'name': [f'Influencer_{i}' for i in range(1, 21)],
    'category': np.random.choice(categories, 20),
    'gender': np.random.choice(genders, 20),
    'follower_count': np.random.randint(10000, 500000, 20),
    'platform': np.random.choice(platforms, 20)
})

influencers.to_csv("influencers.csv", index=False)

# Posts Data
posts = []
for _ in range(100):
    influencer_id = np.random.randint(1, 21)
    date = datetime.now() - timedelta(days=np.random.randint(1, 100))
    posts.append({
        'influencer_id': influencer_id,
        'platform': random.choice(platforms),
        'date': date.strftime('%Y-%m-%d'),
        'URL': f'https://social.com/post/{random.randint(1000, 9999)}',
        'caption': f'Post by influencer {influencer_id}',
        'reach': np.random.randint(5000, 100000),
        'likes': np.random.randint(500, 10000),
        'comments': np.random.randint(10, 500)
    })

posts_df = pd.DataFrame(posts)
posts_df.to_csv("posts.csv", index=False)

# Tracking Data
products = ['Protein Powder', 'Multivitamin', 'Gainer', 'Omega 3', 'Creatine']
tracking_data = []
for _ in range(200):
    influencer_id = np.random.randint(1, 21)
    user_id = np.random.randint(10000, 99999)
    tracking_data.append({
        'source': 'influencer',
        'campaign': f'Campaign_{np.random.randint(1, 5)}',
        'influencer_id': influencer_id,
        'user_id': user_id,
        'product': random.choice(products),
        'date': (datetime.now() - timedelta(days=np.random.randint(1, 100))).strftime('%Y-%m-%d'),
        'orders': np.random.randint(1, 5),
        'revenue': round(np.random.uniform(300, 3000), 2)
    })

tracking_df = pd.DataFrame(tracking_data)
tracking_df.to_csv("tracking_data.csv", index=False)

# Payouts Data
basis_options = ['post', 'order']
payouts = []
for i in range(1, 21):
    basis = random.choice(basis_options)
    rate = round(np.random.uniform(100, 1000), 2) if basis == 'post' else round(np.random.uniform(10, 100), 2)
    orders = np.random.randint(5, 50)
    total_payout = rate * (1 if basis == 'post' else orders)
    payouts.append({
        'influencer_id': i,
        'basis': basis,
        'rate': rate,
        'orders': orders,
        'total_payout': round(total_payout, 2)
    })

payouts_df = pd.DataFrame(payouts)
payouts_df.to_csv("payouts.csv", index=False)

