#Decision Tree — Classify a Fruit

from sklearn.tree import DecisionTreeClassifier

# Features: [weight, size]
X = [
    [150, 7],
    [160, 7],
    [180, 8],
    [200, 9],
    [220, 9]
]

# 0 = Apple, 1 = Orange
y = [0, 0, 0, 1, 1]

# Create and train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict a new fruit
prediction = model.predict([[190, 8]])

if prediction[0] == 0:
    print("The fruit is an Apple")
else:
    print("The fruit is an Orange")
