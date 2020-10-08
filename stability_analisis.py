import json
from sys import version as long_version

version = long_version.split(" ")[0]

print("Stability Analysis for {}".format(version))
print("==========================================")

eps_guess = 1.0
eps = None

while 4 != (4 + eps_guess):
    eps = eps_guess
    eps_guess /= 2.0

print("Machine Epsilon");
print(eps)

def f(x):
    return x**3 + x**2 + x + 1

lhs = -10
rhs = 10

# 0.125 has an exact binary representation (less chance for FPE initially)
h = 0.125

x_vals = []
x = lhs

while (x <= rhs):
    x_vals.append(x)
    x += h

print()
print("Testing secant derivative approximation:")
print("Sampling f(x) = x^3 + x^2 + x + 1")
print("-> h={} from {} to {} ({} samples)".format(
    h,
    lhs,
    rhs,
    len(x_vals)
))

# Approximate the derivative using secant method (O(h^2))
def approx_deriv(samples):
    out = []
    i = 1

    while i < (len(samples) - 1):
        out.append(
            (samples[i+1] - samples[i-1]) / (2.0 * h)
        )
        i += 1

    return out

data = list(map(f, x_vals))
approx_df = approx_deriv(data)
approx_ddf = approx_deriv(approx_df)

data_file = "analysis_for_{}.json".format(version)

with open(data_file, "w") as outfile:
    json.dump({
        "x_vals": x_vals,
        "approx_df": approx_df,
        "approx_ddf" : approx_ddf
    }, outfile)

    print()
    print("Saved results to {}".format(data_file))
