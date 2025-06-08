import os
from telegram import Bot, InputFile
from telegram.ext import Updater, CommandHandler

BOT_TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Welcome to the Virtual ENT Ward Round Companion!")

    # Send welcome video
    video_path = "ENTify_welcoming_speech.mp4"
    with open(video_path, "rb") as video_file:
        context.bot.send_video(chat_id=chat_id, video=video_file, caption="Let’s get started with your first ENT ward round challenge!")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
