from pyexpat.errors import messages
from subprocess import call
from tabnanny import check
from timeit import repeat
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import requests
from credentials import bot_token, bot_user_name,URL

updater = Updater(bot_token,
				use_context=True)

jobqueue = updater.job_queue

txhash=''

print('Hi')


#start function

def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hello sir, Welcome to the Bot.Please write\
		/help to see the commands available.")


#help function		

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/motivate: get quotes""")
	
	
#unknown handler function	

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)


#motivation quote function		

def motivate(update, context):
    quote = requests.request(url='https://api.quotable.io/random',method='get')
    update.message.reply_text(quote.json()['content'])


# returns token price for fixed token address	

def tokenprice(update, context):
    quote = requests.request(url='https://api.covalenthq.com/v1/1/xy=k/uniswap_v2/pools/?quote-currency=USD&format=JSON&contract-addresses=0x4ae2cd1f5b8806a973953b76f9ce6d5fab9cdcfd&key=ckey_7e494e0bde414fd19967dfc3586',method='get')
    update.message.reply_text(quote.json()["data"]["items"][0]["token_0"]["quote_rate"])	
