import discord
import openai
import json
openai.api_key = "openai key here"
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')




@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!bot"):
        prompt = message.content[5:]
        print(prompt)
        response = openai.Completion.create(engine="text-davinci-003", prompt= prompt, max_tokens=144, temperature=0.1, top_p=1, frequency_penalty=0,presence_penalty=0)
        choice = response.choices[0]
        reply_json = json.loads(str(choice))
        reply = reply_json["text"]
        with open("dialog.txt", "a") as f:
            f.write(f"{message.author}: {prompt}\n")
            f.write(f"Bot: {reply}\n")
        print(reply)
        await message.channel.send(reply)

client.run("discordbotkeyhere")
