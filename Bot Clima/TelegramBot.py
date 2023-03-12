import logging
import requests
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from Funciones import *

#crea un log de los fallos y excepciones
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Buenas!! Te voy a tirar el clima cada x")

if __name__ == '__main__':
    #crea el bot
    application = ApplicationBuilder().token('6124422376:AAGvV95nIq_JUyf_3mFVRPjiSa6Hyz8Td7w').build()
    
    #escucha el comando /start
    start_handler = CommandHandler('start', start) 
    application.add_handler(start_handler)



#corre el codigo hasta que hagas control c
application.run_polling()

