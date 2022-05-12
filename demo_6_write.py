import numpy as np 
import pandas as pd 
import streamlit as st
import altair as alt

def main():
    st.header("How to use st.write")
    st.write("Hello, *World!*: sunglasses:" + "😎")

    df = pd.DataFrame({
        "first_name": ["John", "Mary", "Mark", "Bob"],
        "last_name": ["Doe", "Smith", "Johnson", "Jones"],
    })
    st.write(df)

    st.write('Below is a dataframe', df, 'Above is my dataframe')


    df2 = pd.DataFrame(
        np.random.randn(200, 3),
        columns=["a", "b", "c"],
    )
    c = alt.Chart(df2).mark_circle().encode(x='a', y='b', size='c', tooltip=['a', 'b', 'c'])
    st.write(df2)
    st.write(c)

if __name__ == '__main__':
    main()