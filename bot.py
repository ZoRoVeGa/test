import logging
import asyncio
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


async def client_start():
    wr = get_restarted()
    del_restarted()
    try:
        await client.start()
        await client.send_message(
            log_chat,
            f"<b>Bot started</b>\n\n<b>Version:</b> {version}",
        )
        logging.info(f"Bot started\nVersion: {version}")

        if wr:
            await client.edit_message_text(wr[0], wr[1], "Restarted successfully.")
    except BadRequest as e:
        logging.warning(f"Unable to send message to log_chat: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(client_start())
