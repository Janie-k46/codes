from sklearn.tree import DecisionTreeClassifier
import pandas as pd

df = pd.DataFrame({
    'Feature1':[5.1,4.9,6.2,5.9],
    'Feature2':[3.5,3.0,3.4,3.0],
    'Feature3':[1.4,1.4,5.4,5.1],
    'Feature4':[0.2,0.2,2.3,1.8],
    'Label':['Setosa','Setosa','Virginica','Virginica']
})

X = df[['Feature1','Feature2','Feature3','Feature4']]
y = df['Label']

model = DecisionTreeClassifier()
model.fit(X, y)

predictions = model.predict(X)
print(predictions)
