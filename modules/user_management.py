def get_name():
    print("Template")


def load(listeners):
    listeners['message'].append(Template())


class Template:
    def unload(self, listeners):
        listeners['message'].remove(self)

    def handle_message(self, manager, bot, update):
        pass

    def handle_edited_message(self, manager, bot, update):
        pass

    def handle_callback_query(self, manager, bot, update):
        pass

    def handle_inline_callback(self, manager, bot, update):
        pass

    def handle_chosen_inline_result(self, manager, bot, update):
        pass
