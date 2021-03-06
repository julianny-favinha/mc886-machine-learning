import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

# Load the diabetes dataset
diabetes = datasets.load_diabetes()

# Print the diabetes dimension
#print("Diabetes dataset dimensions:", diabetes.data.shape)

# Print the diabetes data (features and target)
diabetes_features_df = pd.DataFrame(diabetes.data)
#print("Diabetes dataset features:")
#print(diabetes_features_df)
diabetes_target_df = pd.DataFrame(diabetes.target)
#print("Diabetes dataset target:")
#print(diabetes_target_df)

# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Use all features
#diabetes_X = diabetes.data

diabetes_X_df = pd.DataFrame(diabetes_X)
print("Diabetes X data frame (coluna 2 das features):")
print(diabetes_X_df)

# Split the data into training/validation sets\n",
diabetes_X_train = diabetes_X[:-20]
diabetes_X_validation = diabetes_X[-20:]

# Print the diabetes train dimension
print("Diabetes X train dimension:", diabetes_X_train.data.shape)

# Print the diabetes validation dimension
print("Diabetes X validation dimension:", diabetes_X_validation.data.shape)
print()

# nao sei pra que isso serve
diabetes_X_train_df = pd.DataFrame(diabetes_X_train)
diabetes_X_validation_df = pd.DataFrame(diabetes_X_validation)
#print(diabetes_X_train_df)
#print(diabetes_X_validation_df)

# Split the targets into training/validation sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_validation = diabetes.target[-20:]

# Print the diabetes train dimension\n",
#print("Diabetes y train dimension:", diabetes_y_train.data.shape)

# Print the diabetes validation dimension
#print("Diabetes y validation dimension:", diabetes_y_validation.data.shape)

diabetes_y_train_df = pd.DataFrame(diabetes_y_train)
diabetes_y_validation_df = pd.DataFrame(diabetes_y_validation)
#print(diabetes_y_train_df)
#print(diabetes_y_validation_df)

# Create linear regression object ***** USING SGD REGRESSOR *****
regr = linear_model.SGDRegressor(max_iter=10000, eta0=0.01)

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the validation set
diabetes_y_pred = regr.predict(diabetes_X_validation)

# Print predictions
print(diabetes_y_pred)

# The coefficients
print('Coefficients: ', regr.coef_)
print('Intercept: ', regr.intercept_)

# The mean squared error
print("Mean squared error: {}".format(mean_squared_error(diabetes_y_validation, diabetes_y_pred)))

# Plot outputs
# pontos do conjunto de treinamento
plt.scatter(diabetes_X_train, diabetes_y_train, color='gray')
# pontos do conjunto de validacao
plt.scatter(diabetes_X_validation, diabetes_y_validation, color='black')
# reta (hipotese)
plt.plot(diabetes_X_validation, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks()
plt.yticks()

plt.show()