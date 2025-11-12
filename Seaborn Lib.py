#importing required libraries
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb
import numpy as np

#Loading dataset
df = sb.load_dataset('tips')
print(df.head())

print (sb.get_dataset_names())

def sinplot(flip=1):
 x = np.linspace(0, 14, 100)
 for i in range(1, 5):
   plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
sinplot()
plt.show()
