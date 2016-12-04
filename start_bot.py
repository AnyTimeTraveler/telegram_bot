import twx.botapi
import os
import util
from time import sleep


class Main:
    config = util.load_config("telegram_bot.json")
    is_running = True
    bots = []

    """
    Load all modules
    """
    listeners = {
        'message': [],
        'edited_message': [],
        'inline_query': [],
        'chosen_inline_result': [],
        'callback_query': [],
    }

    def init(self):
        for module in os.listdir(self.config['modules_path']):
            if module[0] != '_':
                temp = util.import_file(self.config['modules_path'], module)
                if util.check_module(temp):
                    temp.load(self.listeners)

        print("Listeners loaded: ", self.listeners)

        """
        Setup the bots
        """
        for bot_settings in self.config['bots'].values():
            bot = twx.botapi.TelegramBot(bot_settings['api_key'])
            bot.update_bot_info().wait()
            print("Loaded bot: ", bot.username)
            self.bots.append(bot)

    """
    Get updates sent to the bot
    """

    def loop(self):
        while self.is_running:
            for bot in self.bots:
                updates = bot.get_updates(offset=self.config['bots'][bot.username]['offset']).wait()
                for update in updates:
                    self.config['bots'][bot.username]['offset'] = update.update_id + 1
                    if update.message:
                        print(update.message)
                        for module in self.listeners['message']:
                            module.handle_message(self, bot, update.message)
                    elif update.edited_message:
                        print(update.edited_message)
                        for module in self.listeners['edited_message']:
                            module.handle_edited_message(self, bot, update.edited_message)
                    elif update.inline_query:
                        print(update.inline_query)
                        for module in self.listeners['inline_query']:
                            module.handle_inline_query(self, bot, update.inline_query)
                    elif update.chosen_inline_result:
                        print(update.chosen_inline_result)
                        for module in self.listeners['chosen_inline_result']:
                            module.handle_chosen_inline_result(self, bot, update.chosen_inline_result)
                    elif update.callback_query:
                        print(update.callback_query)
                        for module in self.listeners['callback_query']:
                            module.handle_callback_query(self, bot, update.callback_query)
                    else:
                        print("Unhandled")
                if not updates:
                    sleep(1)

    """
    Save the config before exiting
    """

    def save(self):
        util.save_config("telegram_bot.json", self.config)

    def exit(self):
        self.is_running = False
        self.save()


main = Main()
main.init()
main.loop()
main.save()
