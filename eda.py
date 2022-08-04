# importing packages

import streamlit as st 
import pandas as pd
from PIL import Image 
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

def eda():
	df = pd.read_csv("heart.csv")
	dt = pd.read_csv("renamed_data.csv")
	df.astype(str)
	submenu = ["Descriptive", "Plots"]
	choice = st.sidebar.selectbox("Submenu", submenu)

	if choice == "Descriptive":
		st.subheader("This is our data")
		st.dataframe(df)

		st.subheader("Here are the statistical values for all the numerical columns")
		st.dataframe(df.describe())

		col1, col2 = st.beta_columns(2)

		'''with col1: 
			st.subheader("Data Types")
			st.dataframe(df.dtypes)
'''
		with col2:
			st.subheader("Basic Information about the data")
			img = Image.open("info.jpeg")
			st.image(img)

		with col1:
			with st.beta_expander("Column Sex"):
				st.dataframe(dt["sex"].value_counts())

			with st.beta_expander("Rest ECG"):
				st.dataframe(dt["rest_ecg"].value_counts())

		with col2:
			with st.beta_expander("Chest Pain Type"):
				st.dataframe(dt["chest_pain_type"].value_counts())
			with st.beta_expander("Slope"):
				st.dataframe(dt["st_slope"].value_counts())
	
	else:

		i = Image.open("da.png")
		st.image(i)

		st.write("""

# EDA Using Plots 

""")


		with st.beta_expander("Based on Column Target"):
			choose = st.selectbox("Choose the plot you want to view", ["Target", "Target wrt SEX", 
	    		"Target wrt Fasting Blood Sugar", "Target wrt Exercise induced angina"])

			if choose == "Target":
				a = px.histogram(dt, x = "target", color = "target")
				st.plotly_chart(a)

			elif choose == "Target wrt SEX":
				b = px.histogram(dt, x = "target", color = "sex", barmode = "group")
				st.plotly_chart(b)

			elif choose == "Target wrt Fasting Blood Sugar":
				c = px.histogram(dt, x = "target", color = "fasting_blood_sugar")
				st.plotly_chart(c)

			elif choose == "Target wrt Exercise induced angina":
				d = px.histogram(dt, x = "target", color = "exercise_induced_angina", barmode = "group")
				st.plotly_chart(d)


		with st.beta_expander("Frequency Distibution Plots"):
			choose = st.selectbox("Choose the plot you want to view", ["Based on Chest Pain Type", 
	    		"Based on the Maximum heart rate achieved", "Based on the Age"])

			if choose == "Based on Chest Pain Type":
				e = px.pie(dt, names = "chest_pain_type")
				st.plotly_chart(e)

			elif choose == "Based on the Maximum heart rate achieved":
				f, ax = plt.subplots(figsize = (10,8))
				ax = sns.distplot(dt["max_heart_rate_achieved"], bins = 10)
				st.pyplot(f)

			elif choose == "Based on the Age":
				g, ax = plt.subplots(figsize = (10,8))
				ax = sns.distplot(dt["age"], bins = 10, color = "red")
				st.pyplot(g)

		with st.beta_expander("Scatter Plots"):
			choose = st.selectbox("Choose the plot you want to view", ["Age vs Resting Blood Pressure", 
	    		"Age vs Cholestrol", "Cholestrol vs Maximum heart rate achieved"])

			if choose == "Age vs Resting Blood Pressure":
				h, ax = plt.subplots(figsize = (10,8))
				ax = sns.scatterplot(x = "age", y = "resting_blood_pressure", data = dt)
				st.pyplot(h)

			elif choose == "Age vs Cholestrol":
				i = px.scatter(dt, x = "age", y = "cholesterol")
				st.plotly_chart(i)

			elif choose == "Cholestrol vs Maximum heart rate achieved":
				j = plt.figure()
				plt.scatter(dt["cholesterol"], dt["max_heart_rate_achieved"])
				st.pyplot(j)

		with st.beta_expander("Outlier Detection"):
			choose = st.selectbox("Choose the plot you want to view", ["Age", "Resting blood Pressure", 
	    		"Cholestrol", "Maximum Heart rate achieved", "St_depression"])

			if choose == "Age":
				k = px.box(dt, x = "age")
				st.plotly_chart(k)

			elif choose == "Resting blood Pressure":
				l = plt.figure()
				sns.boxplot(dt["resting_blood_pressure"])
				st.pyplot(l)

			elif choose == "Cholestrol":
				m = plt.figure()
				plt.boxplot(dt["cholesterol"])
				st.pyplot(m)

			elif choose == "Maximum Heart rate achieved":
				n = px.box(dt, x = "max_heart_rate_achieved")
				st.plotly_chart(n)

			else:
				o = plt.figure()
				sns.boxplot(dt["st_depression"])
				st.pyplot(o)

		with st.beta_expander("HatMaps and PairPlots"):
	    	
			choose = st.selectbox("Choose the plot you want to view", ["Heat Map", "Pair Plot"])

			if choose == "Heat Map":
				cor = df.corr()
				p = px.imshow(cor)
				st.plotly_chart(p)

			else:
				img = Image.open("pairplot.jpeg")
				st.image(img)
	    		
