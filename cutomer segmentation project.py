import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans


df = pd.read_csv(r"C:\Users\gneer\OneDrive\Pictures\Tài liệu\Desktop\HTML\.vscode\Mall_Customers.csv")

print(df.head())
print(df.columns)
print(df.head())
print(df.columns)
print(df.head())
X = df[['Annual Income (k$)',
        'Spending Score (1-100)']]
wcss = []

for i in range(1,11):
    kmeans = KMeans(
        n_clusters=i,
        random_state=42,
        n_init=10
    )

    kmeans.fit(X)

    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title('Elbow Method')
plt.xlabel('Clusters')
plt.ylabel('WCSS')
plt.show()
kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

df['Cluster'] = kmeans.fit_predict(X)
print(df.head())
plt.figure(figsize=(8,6))

plt.scatter(
    X.iloc[:,0],
    X.iloc[:,1],
    c=df['Cluster']
)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")

plt.title("Customer Segmentation")

plt.show()
print(
    df.groupby('Cluster')
      [['Annual Income (k$)',
        'Spending Score (1-100)']]
      .mean()
)
df.to_excel(
    "Customer_Segmentation_Output.xlsx",
    index=False
)
