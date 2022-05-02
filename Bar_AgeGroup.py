# Import libraries 
from matplotlib import pyplot as plt 
import numpy as np 
import pandas as pd
import math

df = pd.read_csv("dataset1.csv")

arrayx = [0] * 8

for i, j in df.iterrows(): 
    if(j["class"] == "Positive"):
    	index = math.ceil((j["Age"]-10)/10.0) - 1;
    	arrayx[index] = arrayx[index] + 1

print(arrayx)

fig = plt.figure(figsize = (10, 5))
groups = ['11-20', '21-30','31-40','41-50','51-60','61-70','71-80','81-90']
plt.bar(groups,arrayx,width=0.5,color="Maroon")
plt.xlabel("Age Groups")
plt.ylabel("No of Positive Cases")
plt.title("No of Positive Cases of Diabetes wrt Age Group")
plt.show()

 