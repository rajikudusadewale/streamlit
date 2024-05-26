import streamlit as st
import time

# its useful to indicate whether the code is running or stucking a loop due to error

st.write("starting an entensive computation...")
latest_iteration = st.empty()


progress_text = 'Operation in progress, Please wait!!!...'
my_bar = st.progress(0, progress_text)
time.sleep(2)

for i in range(100):
    my_bar.progress(i+1)

    latest_iteration.text(f'Iteration {i+1}')
    time.sleep(0.1)

st.write('We are done!')