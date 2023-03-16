import openai
import argparse
import json
openai.api_key = "api key here"
parser = argparse.ArgumentParser(description='CLI_GPT4')
parser.add_argument("-s", type=str, help="System role", default="You are a happy idea bot, you give people ideas that make them happy", dest="sys")
parser.add_argument("-a", type=str, help="Assistant role", default="", dest="assist")
parser.add_argument("-u", type=str, help="User role", default="", dest="user")
args = parser.parse_args()
system=args.sys
assist=args.assist
user=args.user


class MessageBuilder:
    def __init__(self):
        self.msg = []

    def add_line(self, role, content):
        line = {"role": role, "content": content}
        self.msg.append(line)

    def get_message(self):
        return self.msg
    
    def clear(self):
        self.msg.clear()

builder = MessageBuilder()
if system is not None: builder.add_line("system", system)
if user is not None: builder.add_line("user", user)
if assist is not None: builder.add_line("assistant", assist)

msg=builder.get_message()
print(msg)
response = openai.ChatCompletion.create(model="gpt-4", messages=msg, max_tokens=79)
response_dict = dict(response)
reply = response_dict['choices'][0]['message']['content']
reply=reply.replace(f"\n", " ")
print(reply)