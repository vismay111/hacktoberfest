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
