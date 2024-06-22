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
    wr = get_restarted()
    del_restarted() 
    client.start()
    await client.send_message(
            log_chat,
            "<b>Bot started</b>\n\n" f"<b>Version:</b> {version}",
        )
    print("Bot started\n" f"Version: {version}") 
    

    if wr:
        await client.edit_message_text(wr[0], wr[1], "Restarted successfully.")
        except BadRequest:
        logging.warning("Unable to send message to log_chat.")
    await pytgcalls.start()
    await idle()

if __name__ == "__main__":
    client.loop.run_until_complete(start_client())
