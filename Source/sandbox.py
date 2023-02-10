import os

# Access the secret stored in Github Actions
secret_value = os.environ.get("SERVICEACCOUNTKEY")

# Use the secret value in your code
print(secret_value)
