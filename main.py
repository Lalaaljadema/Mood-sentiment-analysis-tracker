import streamlit as st
import glob
from sentiment_analyzer import mood_analyzer, mood_of_the_day
import plotly.express as px
import os
import datetime

files = sorted(glob.glob("diary/*.txt"))

diaries = []
for file in files:
    with open(file, 'r') as f:
        diary = f.read()
        diaries.append(diary.rstrip('\n'))

p,n = mood_analyzer(diaries)
date = [name.strip(".txt").strip("diary/").lstrip('\\') for name in files]
positive = list(p.values())
negative = list(n.values())
figure1 = px.line(x = date, y = positive,
                 labels = {'x':"days", 'y':'positivity'})
figure2 = px.line(x = date, y = negative,
                 labels = {'x':"days", 'y':'negativity'})


st.title("Mood Tracker")
st.subheader("Positivity")
st.plotly_chart(figure1)
st.subheader("Negativity")
st.plotly_chart(figure2)








