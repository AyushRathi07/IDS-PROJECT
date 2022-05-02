# Import libraries 
from matplotlib import pyplot as plt 
import numpy as np 
import pandas as pd

df = pd.read_csv("dataset1.csv")

cnt1=0
cnt2=0

for i, j in df.iterrows(): 
    if(j["Gender"] == "Male" and j["class"] == "Positive"):
    	cnt1 = cnt1 + 1
    else:
    	if(j["Gender"] == "Female" and j["class"] == "Positive"):
    		cnt2 = cnt2 + 1

label_data = ["Male", "Female"]
explode = (0.02, 0)  
num_data = [cnt1, cnt2]
plt.pie(num_data, labels=label_data, explode=explode, startangle=100, autopct='%1.2f%%')
plt.title("Gender wise positive cases of diabetes")
plt.show()

 