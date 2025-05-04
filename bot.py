import os
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Fetch the token from the environment variable 'tgbot'
token = os.getenv("tgbot")

if not token:
    raise ValueError("Telegram bot token not found. Please check the environment variable.")

# Initialize the Updater with the token
updater = Updater(token=token, use_context=True)

# Define a simple /start command
def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the /start command is issued."""
    update.message.reply_text("Hello! I am your bot. How can I help you today?")

# Define a function to send an image
def send_image(update: Update, context: CallbackContext) -> None:
    """Send an image to the user."""
    image_path = "path/to/your/image.jpg"  # Change this to the path of your image
    update.message.reply_photo(photo=open(image_path, 'rb'))

# Set up the CommandHandler to trigger actions
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("send_image", send_image))

# Start the bot and listen for incoming messages
updater.start_polling()

# Run the bot until you stop it manually
updater.idle()
