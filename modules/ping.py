def get_name():
    print("Ping")


def load(listeners):
    ping = Ping()
    listeners['message'].append(ping)
    listeners['edited_message'].append(ping)


class Ping:
    def unload(self, listeners):
        listeners['message'].remove(self)
        listeners['edited_message'].remove(self)

    def handle_message(self, manager, bot, message):
        bot.send_message(chat_id=message.chat.id, text='Pong!', reply_to_message=message)

    def handle_edited_message(self, manager, bot, message):
        self.handle_message(manager, bot, message)
