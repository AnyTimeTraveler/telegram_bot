def get_name():
    return "Exit"


def load(listeners):
    listeners['message'].append(Exit())


class Exit:
    def unload(self, listeners):
        listeners['message'].remove(self)

    def handle_message(self, manager, bot, message):
        if message.text and message.text.startswith('/shutdown') and message.sender.username == "simon_struck":
            manager.exit()