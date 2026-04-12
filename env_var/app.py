import os

db_password = os.getenv("DB_PASSWORD")

if not db_password:
    raise Exception("ENV variable DB_PASSWORD not set!")

print("App started successfully")
