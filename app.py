import io

import streamlit as st
import pandas as pd
import duckdb

csv = '''
beverage,price
Orange juice, 2.5
Expresso, 2
Tea, 3
'''

beverages = pd.read_csv(io.StringIO(csv))

csv2 = '''
food_item,food_price
Cookie juice, 2.5
Chocolatine, 2
Muffin, 3
'''

food_items = pd.read_csv(io.StringIO(csv2))

answer = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution = duckdb.sql(answer).df()

st.write("""
SQL SRS
Spaced Repetition System SQL practice
""")
with st.sidebar:
    option = st.selectbox(
        'What would you like to review',
        ("Joins", "GroupBy", "Windows Functions"),
        index = None,
        placeholder="Select a theme..."
    )

    st.write('You selected: ', option)

st.header("Enter Your Code:")
sql_query = st.text_area(label="Entrez votre input :")
if sql_query:
    result = duckdb.query(sql_query).df()
    st.write(f"Vous avez entré la query suivante : {sql_query}")
    st.dataframe(result)

tab1, tab2 = st.tabs(["Tables", "Solution"])
with tab1:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected")
    st.dataframe(solution)

with tab2:
    st.write(answer)