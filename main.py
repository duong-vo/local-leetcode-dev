from dotenv import load_dotenv
import os
import requests

load_dotenv()

TOKEN = os.getenv("CSRF_TOKEN")
SESSION = os.getenv("LEETCODE_SESSION")
BASE_URL = 'https://leetcode.com/problems/'

COOKIE = f"csrftoken={TOKEN}; LEETCODE_SESSION={SESSION}"
print(COOKIE)
HEADERS = {"Referer": BASE_URL + 'two-sum/',
           "Content-type": "application/json",
           "X-Requested-With": "XMLHttpRequest",
           "X-CSRFToken": TOKEN,
           "Cookie": COOKIE
}

data = {
    "lang": "python3",
    "question_id": "1",
    "typed_code": "class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        # O(n) idea: check if the difference exist\n        # within the nums using a map\n        map = dict()\n        for i in range(len(nums)):\n            # check if the difference is already\n            # in the map\n            diff = target - nums[i]\n            if diff in map:\n                return [map[diff], i]\n            # if we cannot find,\n            # map the current number to its index"
}
res = requests.post(BASE_URL + 'two-sum/submit/', headers=HEADERS, json=data)
print(res.json())
