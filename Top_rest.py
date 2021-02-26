import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.offline as pyo
import plotly.graph_objects as go
import plotly.express as px
# Set notebook mode to work in offline
pyo.init_notebook_mode()

#data_url = "https://drive.google.com/file/d/1jJOFfcLoRmY8VsH9V0QZe-90C1dGISkS/view?usp=sharing"
#path = 'https://drive.google.com/uc?export=download&id='+data_url.split('/')[-2]
df = pd.read_csv("Top50.csv", index_col=0)
#df = pd.read_csv(path, index_col=0)

#rename YOY_sales col
df['YOY_Sales%'] = df['YOY_Sales']
#remove the %sign in rows
df['YOY_Sales%'] = df['YOY_Sales%'].str.replace('%','')
#convert column to numeric
pd.to_numeric(df['YOY_Sales%'])

st.title("Top Restaurants in 2019")
st.header("Let's explore the top restauarnts as ranked by yearly sales")
st.subheader("Being a food fanatic, anything related to food catches my eye. This website gives a closer look at the top food chains and how they stack up next to each other")
st.subheader("This data is from 2019. Yet, it would be interesting to examine the effect of COVID-19 on the restaurant scene!")
cols = ["Restaurant", "Content", "Sales_mn", "YOY_Sales%", "Units", "YOY_Units", "Headquarters", "Segment_Category"]
st_ms = st.multiselect("Columns", df.columns.tolist(), default=cols)


df_user_cols = df[st_ms]   #new df only with cols that user specifies

st.subheader("View the Top Restaurants")
#use slider to check how many restaurants the user wants to see
view_df = st.slider(
    "How many restaurants would you like to view?", 1, 25,50)

if view_df==1:
	st.balloons()
#use selected nb of rows to display the new df with the previously specified cols
df_user_final = df_user_cols.iloc[0:view_df]

st.write("The top ", view_df, " restaurants are:")
st.write(df_user_final.head(view_df))

#save new df with only needed rows for visualizations; keeping all cols
df_user_rows = df.iloc[0:view_df]

#viz 1
st.subheader("Examine the top restaurants by sales in millions of USD")
option_viz1 = st.selectbox("Show Graph?", ("Yes", "No, hide graph."))

data = [go.Bar(x=df_user_final['Restaurant'],
            y=df_user_final['Sales_mn'],marker=dict(color='#F04265'))]

if option_viz1 == "Yes":
	#st.bar_chart(df_user_rows["Sales_mn"])
	st.write(data)


#viz2
st.subheader("Examine the top restaurants by number of branches")
option_viz2 = st.selectbox("Show Graph?", ("Yes", "No. Hide graph"))
data2 = [go.Bar(x=df_user_final['Restaurant'],
            y=df_user_final['Units'], marker=dict(color='#F04265'))]

if option_viz2 == "Yes":
	#st.bar_chart(df_user_rows["Units"])
	st.write(data2)


#viz3
st.subheader("Examine the change in sales from in 2019")

fig3 = px.scatter(df_user_final, x="Restaurant", y="YOY_Sales%", color = "Restaurant")

option_viz3 = st.selectbox("Show Graph?", ("Yes", "No. Hide graph."))

if option_viz3 == "Yes":
	st.write(fig3)


#viz4
st.subheader("Examine the cuisine categories")

fig = px.scatter(df_user_final, x="Restaurant", y="Segment_Category", color = "Segment_Category")

option_viz4 = st.selectbox("Show Graph?", ("Yes", "No, hide graph"))

if option_viz4 == "Yes":
	st.write(fig)


st.subheader("Did you get hungry yet?")

IMAGE_URL = "https://bgr.com/wp-content/uploads/2020/09/bgrpic-copy-19.jpg?resize=1200,767"

st.image(IMAGE_URL, use_column_width=True)
