import asyncio
import random
import sys
import time
from json import load as json_load

from telethon import TelegramClient, events

from utils.game import MinesweeperSolver


class UserBot:
    def __init__(self) -> None:
        self.config = {}
        self.load_config()
        self.API_ID = self.config.get("api_id")
        self.API_HASH = self.config.get("api_hash")
        self.session_name = self.config.get("session_name")
        self.min_delay = self.config.get("min_delay", 0)
        self.max_delay = self.config.get("max_delay", 0)
        self.client = TelegramClient(self.session_name, self.API_ID, self.API_HASH)
        self.solver = MinesweeperSolver()
        self._loop = None
        self.register_handlers()

    def load_config(self):
        try:
            with open("config.json", "r") as config_file:
                self.config = json_load(config_file)
        except FileNotFoundError:
            print("❌ Error: Config file not found!")
            sys.exit()

    def get_loop(self):
        if not self._loop:
            self._loop = asyncio.new_event_loop()
        return self._loop

    def run_async(self, coro):
        loop = self.get_loop()
        if loop.is_running():
            return asyncio.ensure_future(coro, loop=loop)
        else:
            return loop.run_until_complete(coro)

    def start(self):
        self.client.start()
        print("🚀 UserBot started successfully!")
        self.client.run_until_disconnected()

    async def get_game_board(self, message):
        board = ""
        rows = message.reply_markup.rows[:8]
        for row in rows:
            for button in row.buttons:
                board += button.text
            board += "\n"
        return board

    async def make_a_move(self, message):
        time.sleep(random.randint(self.min_delay, self.max_delay))
        board = await self.get_game_board(message)
        self.solver.parse_board(board)
        analyze = self.solver.analyze_board()
        move = [analyze["row"], analyze["col"]]
        print(f"🎯 Made a move at position {move}")
        await message.click(*move)

    def register_handlers(self):
        @self.client.on(events.MessageEdited())
        async def message_edit_handler(event):
            get_me = await self.client.get_me()
            first_name = get_me.first_name
            try:
                if "🏆" in event.message.text:
                    print("🎉 Game End!")
                    self.client.disconnect()
                    sys.exit()
                if first_name in event.message.text:
                    print("🎮 Your turn detected!")
                    await self.make_a_move(event.message)
            except BaseException as e:
                print(f"⚠️ Error: {e}")
