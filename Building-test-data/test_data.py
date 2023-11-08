import numpy as np # import numpy for high level numerical python
import pandas as pd # import pandas library dataframe
import random # import random module for implementing pseudo-random number generators for various distributions

# Create empty lists for indepedent variabes (will hold our random data)
X1 = [] # note we will use list data-structure to keep our data ordered 
X2 = []
X3 = []
X4 = []
X5 = []
categories = []

# Initiate for loop to generate random data
for n in range(0,1000): # range method - (start, stop, step)
    number1 = random.randint(0,50) # randint () method returns an integer number selected element from the specified range
    X1.append(number1)
    number2 = random.randint(0,500)
    X2.append(number2)
    number3 = random.randint(250,500)
    X3.append(number3)
    number4 = random.randint(0,1500)
    X4.append(number4)
    number5 = random.randint(0,100)
    X5.append(number5)
    number6 = random.randint(1,5000)
    categories.append(number6)
    
# Create DataFrame including all above features + randomly generated data
df = pd.DataFrame ({'X1':X1,'X2':X2,'X3':X3,'X4':X4,'X5':X5,'Categories':categories})
# Create a copy of original dataframe ...(good practice)
original_dataframe = df.copy(deep = True)

# Build categorical data in df
range = [0,300,850,1500,2500,np.inf] # note -> list data strucuture ORDERED
category_names = ['Amazon','Google','Microsoft','BabylonAI','BenevelonAI'] 
df['Categories'] = pd.cut(df['Categories'], bins = range, labels = category_names)

# Dataframe
print(df.head()) # head of dataframe
print(df.describe()) # descriptional statistics (data type objects included)
print(df.shape) # shape of dataframe
print(df.info()) # dataframe info