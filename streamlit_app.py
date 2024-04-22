# Packages
import streamlit as st
import pandas as pd


# Configuration
st.set_page_config(layout='wide', initial_sidebar_state='expanded')
with open('style.css') as f:
    st.markdown(f'<style>(f.read())</style>', unsafe_allow_html=True)


# Streamlit app
st.title("`ECX | 21DOC | Leaderboard`")
st.markdown(' ')
st.markdown(' ')

# st.sidebar.header("`Dicey Tech Hackathon`")


# Platform Metrics Per Year
st.sidebar.subheader('Yearly Performance Review')
bar_choice = st.sidebar.selectbox('Select metric', [
    'Number of Posts',
    'Impressions',
    'Engagements'
])


st.sidebar.markdown('---')


# Metrics
st.markdown('### Performance Summary')
col1, col2, col3 = st.columns(3)
col1.metric("Most Used Platform", "Instagram", "27% of posts")
col2.metric("Most Viewed Platform", "Facebook", "5400 Average Impressions Per Post")
col3.metric("Most Engaging Platform", "Facebook", "3% Average Engagement Rate Per Post")


st.markdown('---')


# Bar_chart_Section
st.markdown('### Yearly Performance Review')
if bar_choice == 'Number of Posts':

    for media in mediums:
        media['year'] = media.Date.apply(lambda x: x.strftime('%Y'))
        media.sort_values('Date', inplace=True)
    
    post_counts = {}
    for index, media in enumerate(mediums):
        post_count_temp = media.value_counts('year').sort_index()
        post_counts[mediums_list[index]] = post_count_temp
    
    media_post_count = pd.DataFrame(post_counts)
    media_post_count['year'] = media_post_count.index
    
    colors = ['rgb(31, 119, 180)', 'rgb(255, 127, 14)', 'rgb(44, 160, 44)',
              'rgb(214, 39, 40)', 'rgb(148, 103, 189)', 'rgb(140, 86, 75)']
    
    data = []
    for i, medium in enumerate(mediums_list):
        trace = go.Bar(x=media_post_count['year'], y=media_post_count[medium], name=medium,
                       marker_color=colors[i % len(colors)])
        data.append(trace)
    
    layout = go.Layout(title='Total Yearly Amount Of Posts For All Media Groups',
                       xaxis=dict(title='Year'),
                       yaxis=dict(title='Post Count'),
                       barmode='group',
                       legend=dict(
                            x=0,
                            y=1.0,
                            bgcolor='rgba(255, 255, 255, 0)',
                            bordercolor='rgba(255, 255, 255, 0)'
                        ),
                        height=800, # Increase the height of the chart
                        width=1000 # Increase the width of the chart
                                      )
    
    fig = go.Figure(data=data, layout=layout)
    fig.show()


st.plotly_chart(fig)


# st.sidebar.markdown('''
# Created By Abatan Ayodeji (Agroall) For Dicey Tech Hackathon.
# ''')
