import sys
import site


def main():
    print("=== Enter the Matrix ===")
    print("Python version: ", sys.version)
    print("Executable: ", sys.executable)
    print("Prefix: ", sys.prefix)
    print("Base prefix: ", sys.base_prefix)
    if sys.prefix != sys.base_prefix:
        print("\nVirtual envirorment detected!")
    else:
        print("\nNo virtual envirorment detected")
        print("=== Instruction ===")
        print("Create VE with:")
        print("python3 -m venv 'Nome_Dir'")
        print("\nActivate it:")
        print("Linux/macOS: source Nome_Dir/bin/activate")
        print("Windows: 'Nome_File'\\scripts\\activate")
    print("\nCurrent site-packages:")
    for path in site.getsitepackages():
        print(path)
    print("\nUser site-packages:")
    print(site.getusersitepackages())


if __name__ == "__main__":
    main()
