import streamlit as st
import os
from sentiment_analyzer import mood_analyzer,mood_of_the_day
import glob
import plotly.express as px


date = st.date_input("Input date")
text = st.text_input("What's on your mind?")
result = mood_of_the_day(text)
if result:
    st.info(result)


if text:
    filename = f"diaries/{date}.txt"

    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("")
    with open(filename, "a") as file:
        file.write(f"{text}\n")

    st.success("Entry saved!")


files = sorted(glob.glob("diaries/*.txt"))


diaries = []
for file in files:
    with open(file, 'r') as f:
        diary = f.read()
        diaries.append(diary.rstrip('\n'))

p,n = mood_analyzer(diaries)
dates = [name.strip(".txt").strip("diaries/").lstrip('\\').replace('_', '-') for name in files]
positive = list(p.values())
negative = list(n.values())


figure1 = px.line(x=dates, y=positive, labels={'x': 'Date', 'y': 'Positivity'})
figure1.update_xaxes(type='category')
figure2 = px.line(x=dates, y=negative, labels={'x': 'Date', 'y': 'Negativity'})
figure2.update_xaxes(type='category')

st.title("Mood Tracker")
st.subheader("Positivity")
st.plotly_chart(figure1)
st.subheader("Negativity")
st.plotly_chart(figure2)

