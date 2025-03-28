import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Declaring variable 
class Config:
    # Base URL for the test site
    BASE_URL = "https://the-internet.herokuapp.com"

    # Browser configuration
    BROWSER = os.getenv("BROWSER", "chrome") # Default browser is Chrome if not specified
    HEADLESS = os.getenv("HEADLESS", "FALSE").lower() == "true" # Default is False if not specified

    # timeout (in seconds) for waiting for elements to appear on the page
    IMPLICIT_WAIT = 10 # Default wait time is 10 seconds if not specified
    EXPLICIT_WAIT = 10 # Default wait time is 10 seconds if not specified
    PAGE_LOAD_TIMEOUT = 30 # Default wait time is 10 seconds if not specified

    # Test data
    VALID_USERNAME = os.getenv("VALID_USERNAME", "admin") # Default username is admin
    VALID_PASSWORD = os.getenv("VALID_PASSWORD", "admin") # Default password is admin

    # Reporting 
    SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports", "screenshots") # Screenshot and report directory

    # Ensure directories exist
    @staticmethod
    def ensure_directories_exist(directory): # Create directory if it does not exist
        if not os.path.exists(directory):# Check if directory exists
            os.makedirs(directory)# Create directory if it does not exist

@classmethod
def initialize(cls):
    cls.ensure_directories_exist(cls.SCREENSHOT_DIR)