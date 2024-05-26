import streamlit as st
import pandas as pd

# SIDEBAR
my_select_box = st.sidebar.selectbox('Select', [1,2,32,3,4,5,6,6,9])
my_slidebar = st.sidebar.slider('Rate', min_value=1, max_value=5, step=1, value=1)

# COLUMNS

left_col, right_col = st.columns(2)
import random
data = [random.random() for _ in range(100)]
with left_col:
    st.subheader('A linechart')
    st.line_chart(data)

with right_col:
    st.subheader('DATA')
    st.write(data[:5])
# 0r you use this: 

#right_col.subheader('Data')
#right_col.write(data[:10])


col1, col2, col3 = st.columns([0.2,0.5, 0.3]) # deciding the width size of the columns

col1.markdown('Hello Streamlit World')
col2.write(data[:10])

with col3:
    st.header('A Cat')
    st.image('https://static.streamlit.io/examples/cat.jpg')


### EXPANDER : It a multi element container that can be expanded or collapsed. It insert container into your app into the app to hold multiple elements. it can be exp


with st.expander('Click here to see more'):
    st.bar_chart({'Data': [random.randint(2,20) for _ in range(25)]})
    st.write('This is an image of a lion')
    st.image('https://static.streamlit.io/examples/dog.jpg')
