# -*- coding: utf-8 -*-


import streamlit as st

def find_largest(a, b, c):
   
    return max(a, b, c)


def app():
    
    st.set_page_config(page_title='Find the Largest Number')
    st.title('Find the Largest Number')

   
    num1 = st.number_input('Enter the first number:')
    num2 = st.number_input('Enter the second number:')
    num3 = st.number_input('Enter the third number:')

 
    largest_num = find_largest(num1, num2, num3)

    
    st.write(f"The largest number is {largest_num}.")

if __name__ == '__main__':
    app()
