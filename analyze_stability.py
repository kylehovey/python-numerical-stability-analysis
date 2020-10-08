from glob import glob
import json

'''
This is a separate script so that stability analysis can be done with one version
'''

def f(x):
    return x**3 + x**2 + x + 1

def df(x):
    return 3*x**2 + 2*x + 1

def ddf(x):
    return 6*x + 2

def MSE(A, B):
    if len(A) != len(B):
        raise Exception("Cannot calculate MSE with lists of different length")

    out = 0

    for (a, b) in zip(A, B):
        out += (a - b)**2

    return out / len(A)

for file in glob('./*.json'):
    with open(file) as json_file:
        data = json.load(json_file)

        print("Doing analysis for {}".format(file))

        x_vals = data["x_vals"]
        approx_df = data["approx_df"]
        approx_ddf = data["approx_ddf"]

        actual_df = list(map(df, x_vals))[1:-1]
        actual_ddf = list(map(ddf, x_vals))[2:-2]

        df_mse = MSE(approx_df, actual_df)
        ddf_mse = MSE(approx_ddf, actual_ddf)

        print("Mean-Squared Error for the derivative: {}".format(df_mse))
        print("Mean-Squared Error for the second derivative: {}".format(ddf_mse))
