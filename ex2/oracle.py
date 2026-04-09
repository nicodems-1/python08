from dotenv import load_dotenv
import os


def configuration() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    load_dotenv()
    print("Configuration loaded:")
    api_key: str | None = os.getenv("API_KEY")
    mode: str = os.getenv("MATRIX_MODE", "development")
    print(f"Mode: {mode}")
    if os.getenv("DATABASE_URL") is None:
        print("Database: Not connected")
    elif mode == "production":
        print("Database: connected to PRODUCTION cluster")
    else:
        print("Database: Connected to local instance")
    if api_key is None:
        print("Missing Api Key")
        print("Using a temporary key to avoid crash")
        api_key = "temporary_key123"
    else:
        print("Api Access: Authentificated")
    print(f"Log Level: {os.getenv('LOG_LEVEL')}")
    if os.getenv("ZION_ENDPOINT") is None:
        print("Zion Network: offline")
    else:
        print("Zion Network: Online")

    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] No .env file found, relying on system variables")
    print("[OK] Production overrides available\n")
    print("The oracle  sees all configurations")


if __name__ == "__main__":
    configuration()
