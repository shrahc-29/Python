import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

#Load dataset
df = pd.read_csv("diabetes.csv")

#Features and target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

#Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#Build Logistic Regression model
model=LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

#Predictions
y_pred=model.predict(X_test)

#Evaluation
print("Accuracy:", round(accuracy_score(y_test, y_pred), 2))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

plt.figure(figsize=(12,5))
sns.heatmap(df.corr(), annot=True, cmap='plasma') #Replaced 'data' with 'df'
plt.title("Feature Correlation")
plt.show()

sns.countplot(x='Outcome', data=df) #Replaced 'data' with 'df'
plt.title("Diabetes Outcome Distribution")
plt.show()

df.hist(bins=20, figsize=(12,10)) #Replaced 'data' with 'df'
plt.show()

X=df.drop("Outcome", axis=1) #Replaced 'data' with 'df'
y=df["Outcome"] #Replaced 'data' with 'df'
