import sys
import openai

openai_api_key = sys.argv[1]
openai.api_key = openai_api_key

try:
    with open("diff.txt", "r") as file:
        code_diff = file.read()
except FileNotFoundError:
    code_diff = ""

if code_diff:
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo-16k-0613",#gpt-4
      messages=[
            {"role": "system", "content": "You are a code reviewer analyzing code diffs that specializes in responding in the requested format."},
            {"role": "user", "content": "Please review the following code changes. After confirming you understand, only respond with a github flavored markdown review outlining the code changes. Point out any potential bugs or poor code choices and suggest clearer code and use github markdown checkboxes for todo items."},
            {"role": "assistant", "content": "Understood, please provide the code and I will respond in the format you've requested. "},
            {"role": "user", "content": code_diff},
      ]
    )
    print(response['choices'][0]['message']['content'])
