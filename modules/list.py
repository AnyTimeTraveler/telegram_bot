def get_name():
    print("List")


def load(listeners):
    my_list = List()
    listeners['message'].append(my_list)
    listeners['edited_message'].append(my_list)


class List:
    def unload(self, listeners):
        listeners['message'].remove(self)
        listeners['edited_message'].remove(self)

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
