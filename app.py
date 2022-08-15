import pandas as pd 
import matplotlib.pyplot as plt 
import plotly.express as plt 
import streamlit as st

url = 'https://raw.githubusercontent.com/rfordatascience/' + \
'tidytuesday/master/data/2020/2020-07-07/coffee_ratings.csv'
df = pd.read_csv(url)

