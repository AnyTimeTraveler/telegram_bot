def get_name():
    print("Template")


def load(listeners):
    listeners['UPDATE_TYPE'].append(Template())


class Template:
    def unload(self, listeners):
        listeners['UPDATE_TYPE'].remove(self)

    def handle_message(self, manager, bot, message):
        pass

    def handle_edited_message(self, manager, bot, message):
        pass

    def handle_callback_query(self, manager, bot, query):
        pass

    def handle_inline_callback(self, manager, bot, callback):
        pass

    def handle_chosen_inline_result(self, manager, bot, result):
        pass
