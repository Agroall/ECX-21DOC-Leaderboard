# Packages
import streamlit as st
import pandas as pd
import requests


# Configuration
st.set_page_config(layout='wide', initial_sidebar_state='expanded')
with open('style.css') as f:
    st.markdown(f'<style>(f.read())</style>', unsafe_allow_html=True)


# Streamlit app
st.title("`ECX | 21DOC | Leaderboard`")
st.markdown(' ')
st.markdown(' ')


# st.sidebar.header("`Dicey Tech Hackathon`")


sheety_url = "https://api.sheety.co/251448a2cce340bfd433a10be3a376c8/ecx21DocLeaderboard/"
sheetnames = ["backEnd", "dataAnalytics", "dataScience", "dsa", "frontEnd", "python"]

df_list = []

for sheet_name in sheetnames:
  response = requests.get(sheety_url+sheet_name)
  data = response.json()
  df = pd.DataFrame.from_dict(data[sheet_name])
  df['Track'] = sheet_name
  df.columns = ['Email', 'Name', 'Score', 'Track']
  df = df[['Name', 'Email', 'Track', 'Score']]
  df = df.iloc[2:-1, :]
  df_list.append(df)

combined_leaderboard = pd.concat(
    df_list,
    ignore_index=True
)

combined_leaderboard['Score'] = combined_leaderboard['Score'].astype('int64')

indices_without_email = combined_leaderboard[combined_leaderboard['Email']==''].index

# For each row without email, add its score to the row above it
for index in indices_without_email:
    combined_leaderboard.loc[index - 1, 'Score'] += combined_leaderboard.loc[index, 'Score']

# Drop the rows without emails
combined_leaderboard = combined_leaderboard.drop(indices_without_email).reset_index()

# Print the modified dataframe
combined_leaderboard = combined_leaderboard.sort_values('Score',ascending=False).reset_index()
combined_leaderboard = combined_leaderboard.drop(columns=['index','level_0'])
combined_leaderboard

# st.sidebar.markdown('''
# Created By Abatan Ayodeji (Agroall) For Dicey Tech Hackathon.
# ''')
