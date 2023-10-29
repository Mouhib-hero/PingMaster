import subprocess

# Define the path to your requirements.txt file
requirements_file = "requirements.txt"

# Install missing libraries from requirements.txt
try:
    subprocess.check_call(["pip", "install", "-r", requirements_file])
    print("Successfully installed missing libraries.")
except subprocess.CalledProcessError as e:
    print(f"Error installing missing libraries: {e}")
