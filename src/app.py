'''
Streamlit in python programming
Author: AEAhwazi
Date: 2026/07/31
Subjet: Codeing in streamlit
'''

#Import streamlit
import streamlit as st
import pandas as pd
import numpy as np

#Defile lists
name_food = ['Pasta', 'Pitza', 'Makaroni', 'Hamberger',\
           'Sosis', 'Kalbas', 'Kabab', 'Salad', 'Soop', 'Fish']
price_food = [10, 20, 5, 12, 10, 7, 15, 3, 3, 30]

st.title("Welcome to [Ahwazi Resturan]")
st.write("Please order your food...")
st.write("Input your info.")
name = st.text_input("", placeholder="Name")
lname = st.text_input("", placeholder="Last name")
tell = st.text_input("", placeholder="Phone number")
address = st.text_input("", placeholder="Address")

sum_price = 0

n_food =st.selectbox("Select Food:", name_food)
index_food = name_food.index(n_food)
p_food = price_food[index_food]
st.write(n_food, p_food)
qty_food = st.number_input("", placeholder="Qty of food")
sum_price = p_food * qty_food

if name != "" and lname != "":
    st.write("Information Order:")
    st.write(f"Name: {name} {lname}")
    st.write(f"Tell Number: {tell}")
    st.write(f"Address: {address}")
    st.write(f"Name food: {n_food}")
    st.write(f"Price: {p_food}")
    st.write(f"Sum of price: {sum_price}")
