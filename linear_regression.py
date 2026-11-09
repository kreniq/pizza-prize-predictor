from sklearn.linear_model import LinearRegression
import numpy as np
#training data
x=np.array([8,10,12]).reshape(-1,1)
y=np.array([10,13,16])

#we use concept of objects and classes here
model=LinearRegression()

#train the model
model.fit(x,y)

#display slope and intercept
print('Slope:',(round(model.coef_[0],2)))
print('Intercept:',round(model.intercept_))

#testing
#this is during testing (prediction=model.predict([[11]]))

#after testing
n=float(input(('enter the diameter of pizza in inches:')))
prediction=model.predict([[n]])


#display the test result
print('predicted price:',round(prediction[0],2))
