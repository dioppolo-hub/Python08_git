import importlib
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import requests


def check_dependency(name):
    spec = importlib.util.find_spec(name)
    return spec is not None


def main():
    print("\nLOADING STATUS...\n")
    packages = {
        "pandas": pd,
        "numpy": np,
        "matplotlib": matplotlib,
        "requests": requests
    }
    print("Checking dependencies:")
    for name, module in packages.items():
        if check_dependency(name):
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {name} ({version}) ", end="")
        else:
            print(f"[KO] Error, {name} not found")
        if name == "pandas":
            print("- Data manipulation ready")
        elif name == "numpy":
            print("- Numerical computation ready")
        elif name == "requests":
            print("- Network access ready")
        elif name == "matplotlib":
            print("- Visualization ready")
    print("\n=== DATA GENERATION ===\n")
    arr = np.random.randint(0, 10, size=(50, 20))
    print("Generating Matrix Data...")
    df = pd.DataFrame(arr)
    print("Processing 1000 data points...")
    print("Generating visualization...\n")
    row_means = df.mean(axis=1)
    plt.figure(figsize=(8, 5))
    plt.plot(row_means, marker='o', linestyle='-', color='green')
    plt.title("Matrix Data Analysis")
    plt.xlabel("Time Step")
    plt.ylabel("Average Signal")
    plt.grid(True)
    outpu_file = "matrix_analysis.png"
    plt.savefig(outpu_file)
    plt.close()
    print("Analysis complete!")
    print(f"Results saved to: {outpu_file}")



if __name__ == "__main__":
    main()