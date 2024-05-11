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


# sheety_url = "https://api.sheety.co/8b0bf0b843f7affcb6b787aab08d47ed/generalLeaderboard/"
# sheetnames = ["backEnd", "dataAnalytics", "dataScience", "dsa", "frontEnd", "python"]
# tracknames = ['Back-End', 'Data Analytics', 'Data Science', 'DSA', 'Front-End', 'Python']

# df_list = []

# # Fetching data from Sheety API and processing it
# for index, sheet_name in enumerate(sheetnames):
#   response = requests.get(sheety_url+sheet_name)
#   data = response.json()
#   df = pd.DataFrame.from_dict(data[sheet_name])
#   df['Track'] = tracknames[index]
#   df.drop(columns=['id'], inplace=True)
#   df.columns = ['Email', 'Name', 'Score', 'Track']
#   df = df[['Name', 'Email', 'Track', 'Score']]
#   df = df.iloc[1:-1, :]
#   df_list.append(df)


# # Combining the processed data into a single leaderboard
# combined_leaderboard = pd.concat(
#     df_list,
#     ignore_index=True
# )
# combined_leaderboard['Score'] = combined_leaderboard['Score'].astype('int64')


# # Handling rows without email by adding their scores to the rows above them
# indices_without_email = combined_leaderboard[combined_leaderboard['Email']==''].index
# for index in indices_without_email:
#     combined_leaderboard.loc[index - 1, 'Score'] += combined_leaderboard.loc[index, 'Score']


# # Dropping the rows without emails
# combined_leaderboard = combined_leaderboard.drop(indices_without_email).reset_index(drop=True)

combined_leaderboard = pd.read_csv('Combined_leaderboard (1).csv')

# Sorting the combined leaderboard by score in descending order
combined_leaderboard=combined_leaderboard.drop(columns=['Email'])
combined_leaderboard=combined_leaderboard.drop(columns=['Unnamed: 0'])
combined_leaderboard = combined_leaderboard.sort_values('Score', ascending=False).reset_index(drop=True)


view = combined_leaderboard.style \
  .set_properties(align='center') \
  .set_table_styles([
    {'selector': 'th', 'props': [('background-color', 'lightblue')]},
    {'selector': 'td', 'props': [('font-style', 'italic')]}
  ])


st.dataframe(view)


st.markdown('''
Created By Abatan Ayodeji (Agroall)
''')

