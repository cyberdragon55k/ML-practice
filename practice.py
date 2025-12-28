# import numpy as np
# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt
# # Generate some sample data
# X = np.array([1, 2, 3, 4, 5]).reshape((-1, 1))
# y = np.array([2, 3, 5, 7, 11])
# # Create a linear regression model
# model = LinearRegression()
# # Train the model
# model.fit(X, y)
# # Get the coefficients
# m = model.coef_[0]
# b = model.intercept_
# # Print the equation
# print(f"y = {m}x + {b}")
# # Predict some values
# y_pred = model.predict(X)
# # Plot the data
# plt.scatter(X, y)
# plt.plot(X, y_pred, color='red')
# plt.show()
