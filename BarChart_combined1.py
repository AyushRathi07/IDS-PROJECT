import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
barWidth = 1
fig = plt.subplots(figsize =(12, 8)) 
df = pd.read_csv("dataset1.csv")
Dict1 = {"Polyuria":0, "Polydipsia":0, "sudden weight loss":0, "weakness":0,	"Polyphagia":0,	"Genital thrush":0,	"visual blurring":0, "Itching":0, "Irritability":0,	"delayed healing":0, "partial paresis":0, "muscle stiffness":0,	"Alopecia":0, "Obesity":0}
Dict2 = {"Polyuria":0, "Polydipsia":0, "sudden weight loss":0, "weakness":0,	"Polyphagia":0,	"Genital thrush":0,	"visual blurring":0, "Itching":0, "Irritability":0,	"delayed healing":0, "partial paresis":0, "muscle stiffness":0,	"Alopecia":0, "Obesity":0}
for i, j in df.iterrows():
	for key in Dict1:
	    if(j[key] == "Yes" and j["class"] == "Positive"):
	    	Dict1[key] = Dict1[key] + 1
	    else:
	    	if(j[key] == "Yes" and j["class"] == "Negative"):
	    		Dict2[key] = Dict2[key] + 1
x1 = []
x2 = []
for key in Dict1:
	x1.append(Dict1[key])
for key in Dict2:
	x2.append(Dict2[key])
br1 = [1,5,9,13,17,21,25,29,33,37,41,45,49,53] 
br2 = [x + barWidth for x in br1]
p1 = plt.bar(br1, x1, color ='r', width = barWidth, 
        edgecolor ='grey', label ='Positive') 
p2 = plt.bar(br2, x2, color ='g', width = barWidth, 
        edgecolor ='grey', label ='Negative') 
x3 = [1.5,5.5,9.5,13.5,17.5,21.5,25.5,29.5,33.5,37.5,41.5,45.5,49.5,53.5]  
plt.xlabel('Symptoms', fontweight ='bold') 
plt.ylabel('No of People', fontweight ='bold') 
plt.xticks(x3, 
       ["Polyuria","Polydipsia","sudden weight loss","weakness","Polyphagia","Genital thrush","visual blurring","Itching","Irritability","delayed healing","partial paresis","muscle stiffness","Alopecia","Obesity"],
       fontsize=5)
plt.legend(handles=[p1, p2], title='Color') 
plt.show()