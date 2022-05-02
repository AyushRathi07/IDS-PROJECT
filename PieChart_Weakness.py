# Import libraries 
from matplotlib import pyplot as plt 
import numpy as np 
import pandas as pd

df = pd.read_csv("dataset1.csv")
symptoms = ["Polyuria","Polydipsia","sudden weight loss","weakness","Polyphagia","Genital thrush","visual blurring","Itching","Irritability","delayed healing","partial paresis","muscle stiffness","Alopecia","Obesity"]

def fun(col):
	cnt1=0
	cnt2=0

	for i, j in df.iterrows(): 
	    if(j[col] == "Yes" and j["class"] == "Positive"):
	    	cnt1 = cnt1 + 1
	    else:
	    	if(j[col] == "No" and j["class"] == "Positive"):
	    		cnt2 = cnt2 + 1

	label_data = ["Yes", "No"]
	explode = (0.02, 0)
	colors = ["red","lime"]
	num_data = [cnt1, cnt2]
	plt.pie(num_data, labels=label_data, colors=colors, explode=explode, startangle=100, autopct='%1.2f%%')
	plt.title("Diabetic people showing symptom " + col)
	plt.show()

for s in symptoms:
	fun(s)