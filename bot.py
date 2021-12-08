import asyncio
import os
from time import time
import discord
from discord import message
from discord import channel
from discord.ext import commands
import tweepy

from dotenv import load_dotenv
from tweepy import auth
from tweepy import client
from tweepy import api

load_dotenv("local.env")


api_key = os.getenv('API_KEY')
api_key_secret = os.getenv('API_KEY_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

twitterLink = ''
t_found = False


class TweetPrinter(tweepy.Stream):

    def on_status(self, status):
        print("Tweet found!")
        print("twitter.com/twitter/statuses/" + status.id_str)
        global twitterLink
        global t_found
        twitterLink = "https://twitter.com/"+ status.user.screen_name + "/status/" + status.id_str
        t_found = True
        return False
        



def connectTwitter():
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

def startStream():
    stream = TweetPrinter(api_key, api_key_secret, access_token, access_token_secret)
    stream.filter(follow=["2965216593"], threaded=True)
    

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Discord Bot Running")

async def timer():
    print("Timer running")
    await bot.wait_until_ready()

    connectTwitter()
    startStream()
    print("Twitter Connected")
    
    

    channel = bot.get_channel(884708645835776012)
    msg_sent = False
    
    print("Before loop")
    while True:
        print("Loop running")
    
        global t_found
        global twitterLink
        if t_found:
            if not msg_sent:
                await channel.send(twitterLink)
                msg_sent = True
                t_found = False
        else:
            msg_sent = False
        
        await asyncio.sleep(5)

        

bot.loop.create_task(timer())
bot.run(os.getenv('DISCORD_TOKEN'))


# client = discord.Client()

# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))
#     auth = tweepy.OAuthHandler(api_key, api_key_secret)
#     auth.set_access_token(access_token, access_token_secret)
#     api = tweepy.API(auth, wait_on_rate_limit=True)
    

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('!run'):
#         await message.channel.send("Launching...")
#         stream = TweetPrinter(api_key, api_key_secret, access_token, access_token_secret)
#         stream.filter(follow=["2965216593"])
        




# client.run(os.getenv('DISCORD_TOKEN'))



# auth = tweepy.OAuthHandler(api_key, api_key_secret)
    # auth.set_access_token(access_token, access_token_secret)
    # api = tweepy.API(auth, wait_on_rate_limit=True)

#         stream = TweetPrinter(api_key, api_key_secret, access_token, access_token_secret)
#         stream.filter(follow=["2965216593"])
#         await message.channel.send(twitterLink)


# user = api.get_user(screen_name='theonlygoodjeff')
# print(user.id)


