from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_csv("Housing.csv")
print(df.columns)

#Convert categorical columns to numeric using one-hot encoding
categorical_cols = df.select_dtypes(include=['object']).columns
df=pd.get_dummies(df, columns=categorical_cols, drop_first=True)


X=df[['area']]
y=df['price']

X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=42)
model=LinearRegression()
model.fit(X_train, y_train)

y_pred=model.predict(X_test)
rmse=np.sqrt(mean_squared_error(y_test, y_pred))
print("RMSE:", rmse)

sns.pairplot(df[['price', 'area', 'bedrooms', 'bathrooms', 'stories']])
plt.show()

sns.histplot(df['price'], kde=True)
plt.show()

plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), annot=False, cmap='plasma')
plt.title('Correlation Heatmap of Housing Data')
plt.show()
