# pylint: disable=missing-module-docstring

import io

import duckdb
import pandas as pd
import streamlit as st

CSV = """
beverage,price
Orange juice, 2.5
Expresso, 2
Tea, 3
"""

beverages = pd.read_csv(io.StringIO(CSV))

CSV2 = """
food_item,food_price
Cookie juice, 2.5
Chocolatine, 2
Muffin, 3
"""

food_items = pd.read_csv(io.StringIO(CSV2))

ANSWER_STR = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution_df = duckdb.sql(ANSWER_STR).df()

st.write(
    """
SQL SRS
Spaced Repetition System SQL practice
"""
)
with st.sidebar:
    option = st.selectbox(
        "What would you like to review",
        ("Joins", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="Select a theme...",
    )

    st.write("You selected: ", option)

st.header("Enter Your Code:")
sql_query = st.text_area(label="Entrez votre input :")
if sql_query:
    result = duckdb.query(sql_query).df()
    st.write(f"Vous avez entré la query suivante : {sql_query}")
    st.dataframe(result)

    if len(result.columns) != len(solution_df.columns):
        st.write("Some columns are missing")
    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Some columns are missing")

    n_lines_difference = result.shape[0] - solution_df.shape[0]

    if n_lines_difference != 0:
        st.write(
            f"result has a {n_lines_difference} lines differences with the solution_df"
        )


tab1, tab2 = st.tabs(["Tables", "Solution"])
with tab1:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected")
    st.dataframe(solution_df)

with tab2:
    st.write(ANSWER_STR)
