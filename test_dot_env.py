import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def print_env_value(key):
    """
    Prints the value of an environment variable
    
    Args:
        key (str): The environment variable key to look up
    """
    value = os.getenv(key)
    if value is not None:
        print(f"Value for {key}: {value}")
    else:
        print(f"Environment variable {key} is not set")

if __name__ == "__main__":
    # Get key from user input
    env_key = input("Enter environment variable key: ").strip()
    print_env_value(env_key)