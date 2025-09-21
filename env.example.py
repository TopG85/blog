import os

# Environment configuration template
# Copy this file to env.py and fill in your actual values
# NEVER commit env.py to git!

# Database Configuration
# Replace with your actual database URL
os.environ.setdefault(
    "DATABASE_URL", "postgresql://username:password@host:port/database_name"
)

# Example for local development:
# os.environ.setdefault(
#     "DATABASE_URL", "postgresql://localhost:5432/myapp_dev"
# )

# Other common environment variables you might need:
# os.environ.setdefault("SECRET_KEY", "your-secret-key-here")
# os.environ.setdefault("DEBUG", "True")
# os.environ.setdefault("ALLOWED_HOSTS", "localhost,127.0.0.1")