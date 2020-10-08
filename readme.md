# Numerical Stability Analysis for Different Python Versions

This is currently a very simple script. Steps to run:

1. Run `python run_derivative.py` for each python version you want to compare.
2. Run `analyze_stability.py` with any version of python. This is a separate script that analyzes the mean-squared error of the other runs using one python version to not pollute the analysis by having each python version analyze itself (this keeps the version doing the calculation of error constant).

Example:

```bash
python2 run_derivative.py
python3 run_derivative.py
python analyze_stability.py
```
