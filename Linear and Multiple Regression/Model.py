from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

df = pd.read_csv("Salary_dataset.csv")

X = np.array(df["YearsExperience"]).reshape(-1 , 1)
Y = np.array(df["Salary"]).reshape(-1 , 1)

print(X)
print(X.shape)

print(Y)
print(Y.shape)