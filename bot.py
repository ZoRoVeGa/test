import logging

from pyrogram import Client, idle
from pyrogram.errors.exceptions.bad_request_400 import BadRequest

from config import TOKEN, disabled_plugins, log_chat, API_ID, API_HASH
from utils import get_restarted, del_restarted

with open("version.txt") as f:
    version = f.read().strip()


client = Client("leomedo", API_ID, API_HASH,
                bot_token=TOKEN,
                workers=24,
                parse_mode="html",
                plugins=dict(root="plugins", exclude=disabled_plugins))

async def start_client():
    """
    Start the client and send a startup message to the log chat.
    """
    # Get the restarted message and delete it
    wr = get_restarted()
    del_restarted()

    try:
        # Start the client
        client.start()

        # Send a startup message to the log chat
        startup_message = f"<b>Bot started</b>\n\n<b>Version:</b> {version}"
        await client.send_message(log_chat, startup_message)
        print(startup_message)

        # If the bot was restarted, edit the previous message
        if wr:
            await client.edit_message_text(wr[0], wr[1], "Restarted successfully.")
    except BadRequest as e:
        logging.warning(f"Unable to send message to log_chat: {e}")

    # Start the PyTgCalls instance
    await pytgcalls.start()

    # Idle until the bot is stopped
    await idle()

if __name__ == "__main__":
    client.loop.run_until_complete(start_client())
