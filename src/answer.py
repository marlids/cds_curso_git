import pandas as pd
import plotly.express as px
import streamlit as st

def rd1_question_9(df):
    df_grouped = df[["id", "seller_type"]].groupby("seller_type")

    df_grouped = df_grouped.count().reset_index()

    df_grouped = df_grouped.rename(columns={"id": "count"})

    fig = px.bar(
        df_grouped,
        x = "seller_type",
        y = "count",
        labels={"seller_type":"Owner Type", "count":"Quantily"},
        color="seller_type",
        text="count",
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, use_contraine_width=True)

    return None

def rd1_question_13(df):
    df_grouped = (
        df.groupby("owner")
        .agg(qty = pd.NamedAgg("id", "count"))
        .sort_values("qty")
        .reset_index()
    )

    fig = px.bar(
        df_grouped,
        x = "owner",
        y = "qty",
        labels={"owner":"Owner Type", "qty":"Quantily"},
        color="owner",
        text="qty",
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, use_contraine_width=True)

    return None

def rd1_question_14(df):
    st.text("As we can see, bike with high kilometers have chapier prices")

    fig = px.scatter(
        df,
        x = "km_driven",
        y = "selling_price",
        labels={"km_drivenr":"kilometers", "selling_price":"Selling Price"},
    )

    st.plotly_chart(fig, use_contraine_width=True)

    return None 
