import streamlit as st
import pandas as pd


st.title('Hello Streamlit World :sparkles:')

# Displaying data on the screen
# 1. st.write() 2. magic

st.write('I love you')

l1 = [1,2,3,4,5,6]

st.write(l1)

l2 = list('abc')
d1 = dict(zip(l1, l2))

st.write(d1)


# Magic

'Displaying using Magic :smile: '

df = pd.DataFrame({'Name': ['John', 'Charles','Joy','Jessica'], 
                   'Score': [1,2,3,4]})

df # writing just the variable means st.write(df)