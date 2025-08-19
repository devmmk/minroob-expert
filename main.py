from utils.bot import UserBot
from subprocess import check_output

if __name__ == "__main__":
    try:
        userbot = UserBot()
        userbot.start()
    except (EOFError, KeyboardInterrupt):
        userbot.client.disconnect()
    except BaseException as e:
        print("❌ Error occurred while running the userbot:", e)