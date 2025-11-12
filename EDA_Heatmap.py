import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#load dataset
titanic = sns.load_dataset("titanic")

#basic info
print("Dataset Shape:", titanic.shape)
print("\nFirst 5 Rows:\n", titanic.head())
print("\nSummary Statistics:\n", titanic.describe(include='all'))

#Drop missing values
titanic = titanic.dropna(subset=["age", "fare", "sex", "class"])

#Histogram
plt.figure(figsize=(6, 4))
plt.hist(titanic["age"], bins=20, color="#7EC8E3", edgecolor="black")
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

#KDE plot
plt.figure(figsize=(6, 4))
sns.kdeplot(x=titanic["fare"], fill=True, color="#B565A7")
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Density")
plt.show()

#Boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(x="class", y="fare", data=titanic, palette="Set2")
plt.title("Fare by Passenger Class")
plt.xlabel("Class")
plt.ylabel("Fare")
plt.show()

#Countplot
plt.figure(figsize=(6, 4))
sns.countplot(x="sex", hue="survived", data=titanic, palette="pastel")
plt.title("Survival Count by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.show()

#scatter Plot
plt.figure(figsize=(6, 4))
sns.scatterplot(x="age", y="fare", hue="survived", data=titanic, palette="deep")
plt.title("Age vs Fare (Colored by Survival)")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()

#Select numeric columns for correlation
numeric_cols = titanic[["age", "fare", "pclass", "survived"]]
corr_matrix = numeric_cols.corr()

print("\nCorrelation Matrix:\n", corr_matrix)

#Heatmap for correlation
plt.figure(figsize=(6, 4))
sns.heatmap(corr_matrix, annot=True, cmap="viridis", linewidths=0.5)
plt.title("Correlation Heatmap - Titanic Dataset")
plt.show()
