
import os
import time
from datetime import datetime, timezone
from urllib.parse import quote_plus, urlsplit, urlunsplit
from pymongo import MongoClient
from pymongo.errors import PyMongoError


class UsageLogger:

    def __init__(self):
        mongo_uri = os.getenv("MONGODB_URI")

        if not mongo_uri:
            raise ValueError("MONGODB_URI not found in .env")

        # Encode username and password safely
        parsed = urlsplit(mongo_uri)

        if parsed.username is not None and parsed.password is not None:
            username = quote_plus(parsed.username)
            password = quote_plus(parsed.password)

            host = parsed.netloc.rsplit("@", 1)[-1]

            mongo_uri = urlunsplit((
                parsed.scheme,
                f"{username}:{password}@{host}",
                parsed.path,
                parsed.query,
                parsed.fragment
            ))

        self.client = MongoClient(
            mongo_uri,
            serverSelectionTimeoutMS=5000,
            connectTimeoutMS=5000,
            socketTimeoutMS=10000,
            retryWrites=True
        )

        # Check MongoDB connection
        self.client.admin.command("ping")
        print("MongoDB connected successfully!")

        db = self.client["llm_monitoring"]
        self.collection = db["api_usage"]

    def log_call(self, record):
        record["timestamp"] = datetime.now(timezone.utc)

        for attempt in range(3):
            try:
                self.collection.insert_one(record)
                print("Usage details saved to MongoDB.")
                return True

            except PyMongoError as error:
                print(f"MongoDB write attempt {attempt + 1} failed: {error}")

                if attempt < 2:
                    time.sleep(2 ** attempt)

        print("Warning: usage record could not be saved.")
        return False

    def close(self):
        self.client.close()
