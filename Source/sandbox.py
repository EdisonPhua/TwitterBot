import os

# Access the secret stored in Github Actions
secret_value = os.environ.get("ServiceAccountKey")

# Use the secret value in your code
print(secret_value)
