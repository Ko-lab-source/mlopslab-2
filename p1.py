from sklearn.linear_model import LinearRegression

# Training data
X = [[500], [800], [1000], [1200], [1500]]
y = [100, 160, 200, 240, 300]

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict price for a 1100 sq ft house
prediction = model.predict([[1100]])

print("Predicted house price:", prediction[0])
