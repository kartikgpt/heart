# importing the packages
import streamlit as st
from PIL import Image


# importingthe files
from eda import eda
from ml import ml

def main():

	menu = ["Home", "Exploratory Data Analysis Section", "Prediction Section"]

	choice = st.sidebar.selectbox("Menu", menu)

	if choice=="Home":

		st.write("# Heart Health Prediction App")
		img = Image.open('pulse.png').convert('RGB')
		st.image(img)


		st.write("""

The data used in this particular app contain the features of a newly heart disease patient 
or a diabetic patient.

### DataScource

	- https://archive.ics.uci.edu/ml/datasets/heart+disease

### App Content

	- This app has four sections
	1) Home Page - The page you are currently in

	2) Exploratory Data Analysis - The page in which you will find all the Data Analysis and Visualization Parts

	3) Prediction- The page in which you will be asked to give the information on all the medical aspects
		and we will predict the desired the output
			""")
	elif choice=="Exploratory Data Analysis Section":
		eda()
	elif choice == "Prediction Section":
		ml()
main()
