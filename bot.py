import os

# Fetch the token from environment variables
token = os.getenv("tgbot")

if not token:
    raise ValueError("Telegram bot token not found. Please check the environment variable.")
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio
import os

TOKEN = os.getenv(BOT_TOKEN)
IMAGE_URL = httpsyour-image-url.comimage.jpg  # OR use a local file on hosting

async def start(update Update, context ContextTypes.DEFAULT_TYPE)
    chat_id = update.effective_chat.id
    message = await context.bot.send_photo(chat_id=chat_id, photo=IMAGE_URL)
    await asyncio.sleep(300)
    await context.bot.delete_message(chat_id=chat_id, message_id=message.message_id)

if __name__ == __main__
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler(start, start))
    app.run_polling()
