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
res_json = res.json()
submission_id = res_json["submission_id"]

print(submission_id)

CHECK_TOKEN = os.getenv("CHECK_CSRF_TOKEN")
CHECK_SESSION = os.getenv("CHECK_LEETCODE_SESSION")


CHECK_COOKIE = f"csrftoken={CHECK_TOKEN}; LEETCODE_SESSION={CHECK_SESSION}"

CHECK_HEADERS = {"Referer": BASE_URL + f"two-sum/submissions/{submission_id}/",
                 "Content-type": "application/json",
                 "X-Requested-With": "XMLHttpRequest",
                 "COOKIE": CHECK_COOKIE
                 }
CHECK_URL = f"https://leetcode.com/submissions/detail/{submission_id}/check/"
print(CHECK_URL)
check_res = requests.get(CHECK_URL, headers=CHECK_HEADERS)
print(check_res.status_code)
print(check_res.json())

