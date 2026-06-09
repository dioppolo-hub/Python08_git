import importlib, pandas, numpy, matplotlib, requests


def main():
    packages = {
        "pandas": pandas,
        "numpy": numpy,
        "matplotlib": matplotlib,
        "requests": requests
    }
    for name, module in packages:
        if importlib.util.find_spec(name):
            print(f"[OK] pandas ({module.__version__}) ", end="")
        if name == "pandas":
            print("Data manipulation ready")
        elif name == "numpy":
            print("Numerical computation ready")
        elif name == "requests":
            print("Network access ready")
        elif name == "matplotlib":
            print("Visualization ready")



if __name__ == "__main__":
    main()