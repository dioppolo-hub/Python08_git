import sys
import site


def main():
    print("=== Enter the Matrix ===")
    print("Python version: ", sys.version)
    print("Executable: ", sys.executable)
    print("Prefix: ", sys.prefix)
    print("Base prefix: ", sys.base_prefix)
    if sys.prefix != sys.base_prefix:
        print(
            "\nVirtual envirorment detected!\n"
            "\nMATRIX STATUS: Welcome to the construct\n"
            "\nSUCCESS: you're in an isolated enviroment!\n"
            "Safe to install packages without affecting ", end=""
            "the global system\n"
            "\nPackage installation path:\n"
            )
        for path in site.getsitepackages():
            print(path)
    else:
        print("\nNo virtual envirorment detected")
        print("\nMATRIX STATUS: you're still plugged in")
        print("\nWARNING: You're in the global environment!")
        print("The machine cansee everything you install")
        print("\n=== Instruction ===")
        print("Create VE with:")
        print("python3 -m venv 'Nome_Dir'")
        print("\nActivate it:")
        print("Linux/macOS: source Nome_Dir/bin/activate")
        print("Windows: Nome_Dir\\scripts\\activate")
        print("\nThen run this program again")


if __name__ == "__main__":
    main()
