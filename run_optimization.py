import pandas as pd
import numpy as np
from scipy.optimize import minimize
df = pd.read_csv('xy_data.csv')
t_values = np.linspace(6, 60, 1500)
df.insert(0, 't', t_values)
t1 = df['t'].values
x1= df['x'].values
y1= df['y'].values
def predict_curve(params, t):
    theta_deg, M, X = params
    theta_rad = theta_deg * (np.pi / 180.0)
    x_pred = (t * np.cos(theta_rad) - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta_rad) + X)
    y_pred = (42 + t * np.sin(theta_rad) + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta_rad))
    return x_pred, y_pred
def mae_loss(params):
    x_pred, y_pred = predict_curve(params, t1)
    x_error = np.mean(np.abs(x1 - x_pred))
    y_error = np.mean(np.abs(y1- y_pred))
    total_error = x_error + y_error
    return total_error
bounds = [(0.01, 49.99), (-0.0499, 0.0499), (0.01, 99.99)]
initial_guess = [25.0, 0.0, 50.0]
result = minimize(mae_loss, initial_guess, method='L-BFGS-B', bounds=bounds, options={'disp': False})
if result.success:
    found_params = result.x
    print(f"theta= {found_params[0]}")
    print(f"M= {found_params[1]}")
    print(f"X = {found_params[2]}")
    print(f"L1 Error= {result.fun}")
else:
    print("Optimization failed!!")
