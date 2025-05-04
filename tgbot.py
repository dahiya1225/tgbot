import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Fetch the token from the environment variable 'tgbot'
token = os.getenv("tgbot")

if not token:
    raise ValueError("Telegram bot token not found. Please check the environment variable.")

# Initialize the Application with the token
application = Application.builder().token(token).build()

# Define a simple /start command
async def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the /start command is issued."""
    await update.message.reply_text("Hello! I am your bot. How can I help you today?")

# Define a function to send an image
async def send_image(update: Update, context: CallbackContext) -> None:
    """Send an image to the user."""
    image_url = "https://i.ibb.co/QFsTxRHP/photo-2025-05-04-09-08-05.jpg"  # Direct image URL
    await update.message.reply_photo(photo=image_url)

# Add the command handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("send_image", send_image))

# Start the bot and listen for incoming messages
if __name__ == "__main__":
    application.run_polling()
