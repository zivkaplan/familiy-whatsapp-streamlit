import streamlit as st
import pandas as pd
import json
from collections import defaultdict, Counter

with open("chat_statistics.json", "r") as f:
    data=json.load(f)

df = pd.DataFrame.from_dict(data , orient='columns')
df = df.rename_axis('שם השולח')

st.header("המשפוחה 💟😘")
st.subheader("מי חפר ומי שתק?")
st.caption("סטטיסטיקות החל מה-16/11/2022 ועד 30/04/2024")

st.bar_chart(df, y="הודעות שנשלחו")
