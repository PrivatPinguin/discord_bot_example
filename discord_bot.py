import discord
import os
import requests
import json

# init bot
client = discord.Client()

# API request
def get_json():
	response = requests.get('api_request_goes_here') 
	jSon_data = json.loads{response} #alternate json data here

# console:: bot ready
@client.event
async def on_ready():
	print('Logged in as {0.user}'.format(client))


# responses
@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	# std bot msg
	if message.content.startwith('$pinguin'):
		await message.channel.send('Pinguin hat dich lieb.♥')
	
  # std api request
	if message.content.startswith('$api_request'):
        	j_link = 'json goes here: ' + get_json()
        	await message.channel.send(j_link)

# edit bot token here
client.run('TOKEN')
