import streamlit as st
import helper

st.header('Book Recomander📚')

option = st.selectbox(
    'which Book you Like it',
    helper.title())

if option!='Select Title':
   st.write('We Recamand these Books for you')

   a=helper.books(option)
   col1,col2,col3,col4= st.columns(4,gap='large')

   with col1:
      st.header(a[0])
      
      


   with col2:
      st.header(a[1])
      

   with col3:
      st.header(a[2])
      

   with col4:
      st.header(a[3])
      

