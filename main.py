from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("CSRF_TOKEN")
SESSION = os.getenv("LEETCODE_SESSION")
BASE_URL = 'https://leetcode.com/problems'

print(SESSION)
