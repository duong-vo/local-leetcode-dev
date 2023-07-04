from dotenv import load_dotenv
import os
import requests
import click

load_dotenv()

TOKEN = os.getenv("CSRF_TOKEN")
SESSION = os.getenv("LEETCODE_SESSION")
BASE_URL = 'https://leetcode.com/problems/'
COOKIE = f"csrftoken={TOKEN}; LEETCODE_SESSION={SESSION}"
CHECK_TOKEN = os.getenv("CHECK_CSRF_TOKEN")
CHECK_SESSION = os.getenv("CHECK_LEETCODE_SESSION")
CHECK_COOKIE = f"csrftoken={CHECK_TOKEN}; LEETCODE_SESSION={CHECK_SESSION}"
data = {
    "lang": "python3",
    "question_id": "1",
    "typed_code": "class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        # O(n) idea: check if the difference exist\n        # within the nums using a map\n        map = dict()\n        for i in range(len(nums)):\n            # check if the difference is already\n            # in the map\n            diff = target - nums[i]\n            if diff in map:\n                return [map[diff], i]\n            # if we cannot find,\n            # map the current number to its index"
}
def get_question_id(question):
    return "1"

def check_submission(submission_id):
    check_url = f"https://leetcode.com/submissions/detail/{submission_id}/check/"
    headers = {"Referer": BASE_URL + f"two-sum/submissions/{submission_id}/",
               "Content-type": "application/json",
               "X-Requested-With": "XMLHttpRequest",
               "COOKIE": CHECK_COOKIE
               }
    while True:
        print('Checking...')
        check_res = requests.get(check_url, headers=headers)
        if check_res.json()['state'] == 'SUCCESS':
            return check_res.json()
    return {'state': "PENDING"}

def submit_code(code, question):
    data = {
        "lang": "python3",
        "question_id": get_question_id(question),
        "typed_code": code
    }
    url = f"https://leetcode.com/problems/{question}/submit/"
    headers = {"Referer": f"https://leetcode.com/problems/{question}/",
               "Content-type": "application/json",
               "X-Requested-With": "XMLHttpRequest",
               "X-CSRFToken": TOKEN,
               "Cookie": COOKIE
               }
    res = requests.post(url, headers=headers, json=data)
    res_json = res.json()
    submission_id = res_json['submission_id']
    result = check_submission(submission_id)
    return result

def parse_file(filename):
    f = open(filename, 'r')
    return f.read()

def display_result(result):
    status = result["status_msg"]
    total = result["total_testcases"]
    correct = result["total_correct"]
    print(status)
    print(f"{correct}/{total}")

@click.group()
def cli():
    pass

@click.command('submit')
@click.argument('filename', type=click.Path(exists=True))
@click.argument('question_url')
def submit(filename, question_url):
    question_name = question_url.split("/")[-2]
    result = submit_code(parse_file(filename), question_name)
    display_result(result)

cli.add_command(submit)

if __name__=='__main__':
    cli()
