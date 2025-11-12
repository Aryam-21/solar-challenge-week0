import streamlit as st
import plotly.express as px
from utils import load_data, filter_by_country
st.set_page_config(page_title="Solar Dashboard", layout='wide')

data = load_data()

st.sidebar.title("Filters")
country_list = data['Country'].unique().tolist()
selected_country = st.sidebar.selectbox("Select Country", country_list)
metric = st.sidebar.radio("Select Metric for Boxplot", ['GHI', 'DNI', 'DHI'])
filtered_data = filter_by_country(data, selected_country)
st.title("🌞 Solar Data Dashboard")
st.markdown("---")
st.subheader(f'{metric} Distrbution - {selected_country}')
fig = px.box(filtered_data, y=metric, points='all', title=f'{metric} Boxplot for {selected_country}')
st.plotly_chart(fig, use_container_width=True)
st.markdown("---")
