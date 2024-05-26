import streamlit as st
import pandas as pd


# TEXT INPUT
first_name = st.text_input('What is first name? ')
last_name = st.text_input('What is your last name? ')
age = st.text_input('Your Age: ')



if first_name and last_name and age: 
    st.write(f' Hello Mr {last_name} {first_name}. We are happy to see you. Your age is {age}')
st.divider()

# NUMBER INPUT

number =st.number_input('Enter your number ',  min_value=0, max_value=100, step =5)
st.write(f'The winning number is {number}')

st.divider()
# BUTTON

click = st.button('Click me!')
if click:
    st.write(' :ghost:' * 10)
st.divider()

# CHECKBOX
check = st.checkbox('agree')
if check:
    st.write('You agreed!')
st.divider()

# IN the case we want the box checked
checked = st.checkbox('Contine', value=True)
if checked:
    st.write(':+1' * 5)


df = pd.DataFrame({'Name': ['John', 'Charles','Joy','Jessica'], 
                   'Score': [1,2,3,4]})


if st.checkbox('show data'):
    st.write(df)

st.divider()

# RADIO BUTOON

pets = ['cat', 'dog', 'fish']
pet = st.radio('Favorite', pets)
st.write(f'Your favorite pet is {pet}')


st.radio('Favorite', pets, index=1, key='Your_pet')
st.write(f'Your favorite pet is {st.session_state.Your_pet *2}')
st.divider()

# SELECT BOX
cities = ['london', 'paris','lagos']
city = st.selectbox('Your city', cities)   # if i want paris to be selected automatically, use index=1
st.write(f'you live in {city}')

st.divider()

# SLIDER
x = st.slider('Select a rank', value=20, min_value=10, max_value=40, step=5)
st.write(f'Your rank is {x}')
st.divider()


# FILE UPLOADER

uploaded_file = st.file_uploader('Attach a file: ', type=['txt','csv','xlsx']) # the file size limit is 200mb. to allow ext use type=
if uploaded_file:
    st.write(uploaded_file)  # display the name of the file
    if uploaded_file.type == 'text/plain':
        from io import StringIO
        Stringio = StringIO(uploaded_file.getvalue().decode('utf-8'))
        string_data = Stringio.read()
        st.write(string_data) # display the content of the file
    elif uploaded_file.type == 'text/csv':
        import pandas as pd
        df = pd.read_csv(uploaded_file)
        st.write(df)
    else:
        df = pd.read_excel(uploaded_file)
        st.write(df)

st.divider()

# CAMERA INPUT
camera_photo = st.camera_input('Take a photo')
if camera_photo:
    st.image(camera_photo)

#st.image('link\url.jpg') # if the image is a remote file

st.divider()