import streamlit as st
import plotly.express as px
import glob
from backend import mood_analyzer

files= sorted(glob.glob("*/*.txt"))

diaries=[]
for file in files:
    with open(file, 'r') as f:
        diary = f.read()
        diaries.append(diary.rstrip('\n'))
st.title("Mood Tracker")
p,n = mood_analyzer(diaries)
date= list(p.keys())
positive= list(p.values())
negative= list(n.values())
figure1= px.line(x=date, y=positive,
                 labels= {'x':"days", 'y':'positivity'})
figure2= px.line(x=date, y=positive,
                 labels= {'x':"days", 'y':'negativity'})
st.subheader("positivity")
st.plotly_chart(figure1)
st.subheader("negativity")
st.plotly_chart(figure2)





