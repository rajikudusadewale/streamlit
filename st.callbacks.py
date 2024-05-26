import streamlit as st

### CALLBACKS

st.title('Distance Converter')
st.subheader('Conversion widgets')

def miles_to_km():
    st.session_state.km = st.session_state.miles * 1.69

def km_to_miles():
    st.session_state.miles = st.session_state.km * 0.621

col1, buff, col2 = st.columns([4,2,4])
with col1:
    miles = st.number_input('Miles:', key='miles', on_change=miles_to_km) # on_change is the function

with col2:
    km = st.number_input('km:', key = 'km', on_change=km_to_miles)