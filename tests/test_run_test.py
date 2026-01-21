import os
from dotenv import load_dotenv
from engine.run_test import run_test

# Load environment variables from .env file
load_dotenv()

def test_run_test():
    run_test(
        base_url=os.getenv("TEST_BASE_URL", "https://practicetestautomation.com/practice-test-login/"),
        username=os.getenv("TEST_USERNAME", "student"),
        password=os.getenv("TEST_PASSWORD", "Password123")
    )
