import streamlit as st
import pandas as pd

df1 = pd.read_csv("shiseki02.csv",encoding='shift-jis')
df2 = df1.rename(columns={"北緯": "latitude","東経":"longitude"})

df3 = pd.read_csv("shiro02.csv",encoding='shift-jis')
df4 = df3.rename(columns={"北緯": "latitude","東経":"longitude"})

st.title("国内観光")
st.header("~城・史跡~")
bot = st.radio(label="史跡か城か?",options=["史跡","城"])

if bot == "史跡":
  st.markdown("##### こちらは" + bot + "のデータフレームです。")
  st.write(df2[["名称","所在地"]])
  st.markdown("##### 以下のチェックボックスで地図を表示できます。")
  if st.checkbox("地図を表示"):
    st.balloons()
    st.map(df2)

else:
  st.markdown("##### こちらは" + bot + "のデータフレームです。")
  st.write(df4[["名称","所在地"]])
  st.markdown("##### 以下のチェックボックスで地図を表示できます。")
  if st.checkbox("地図を表示"):
    st.balloons()
    st.map(df4)
           
