import numpy as np
import pandas as pd

def gradient_descent(x,y,lr = 0.01,epochs = 10000):
    m , b = 0.0 , 0.0
    for epoch in range(epochs):
        y_predict =m*x + b
        error = y - y_predict
        cost = np.mean(error**2)

        dm = -2*np.mean(error*x)
        db = -2 * np.mean(error)

        b = b - db*lr
        m = m - lr*dm
        print(f"m = {m}, b = {b} , cost = {cost} , error = {error}, epoch = {epoch}")

if __name__ == "__main__":
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([5, 7, 9, 11, 13])

    gradient_descent(x, y)
