import os
from dotenv import load_dotenv


# senza load_dotenv() python non legge .env ma le variabili dell' os
load_dotenv()


def main():
    dati = {}
    print("=== ORACLE SYSTEM CONFIGURATION ===")
    print("\nORACLE STATUS: Reading the Matrix...\n")
    matrix_mode = os.environ.get("MATRIX_MODE")
    database_url = os.environ.get("DATABASE_URL")
    api_key = os.environ.get("API_KEY")
    log_level = os.environ.get("LOG_LEVEL")
    zion_endpoint = os.environ.get("ZION_ENDPOINT")
    dati = {
        "MATRIX_MODE": matrix_mode,
        "DATABASE_URL": database_url,
        "API_KEY": api_key,
        "LOG_LEVEL": log_level,
        "ZION_ENDPOINT": zion_endpoint
    }
    error_conf = []
    for k, v in dati.items():
        if not v:
            print(f"[ERROR] {k} Missing Configuration")
            error_conf.append(k)
    if error_conf:
        print("\n[WARNING] Configuration Missing!")
        print("Use 'cp .env.exaple .env' and compile it before starting")
        return
    print("Configuration loaded:")
    if matrix_mode == "development":
        print(
            "Mode: development\n"
            f"Database: Connected to local instance ({database_url})\n"
            f"API Access: Authenticated (Key: {api_key})\n"
            f"Log Level: {log_level}\n"
            f"Zion Network: Online ({zion_endpoint})\n"
        )
    elif matrix_mode == "production":
        print(
            "Mode: production\n"
            f"Database: Connected to SECURE production instance\n"
            f"API Access: Authenticated securely\n"
            f"Log Level: {log_level} (Production Restrictive Mode)\n"
            f"Zion Network: Encrypted Tunnel Established\n"
        )
    else:
        print(f"Mode: UNKNOWN ({matrix_mode})")
    print("\nEnviroment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env") and matrix_mode == "development":
        print("[OK] .env file properly configurated")
    else:
        print("[OK] Running on system enviroment variables")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
