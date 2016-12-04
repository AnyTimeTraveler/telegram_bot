def get_name():
    return "CustomKeyboard"


def load(listeners):
    keyboard = CustomKeyboard()
    listeners['message'].append(keyboard)
    listeners['callback_query'].append(keyboard)


class CustomKeyboard:
    editable_messages = {}

    def unload(self, listeners):
        listeners['message'].remove(self)
        listeners['callback_query'].remove(self)

    def handle_message(self, manager, bot, message):
        if message.text and message.text[0] == '/' and "keyboard" in str(message.text).lower():
            from twx.botapi import InlineKeyboardMarkup
            from twx.botapi import InlineKeyboardButton
            keyboard = [
                ['ø', 'η', 'э'],
                ['x', 'Ø', 'Π'],
                ['Э', 'Х', '-'],
                ['<', ' ', '>']
            ]
            nkb = []
            for row in keyboard:
                nkb.append(
                    [InlineKeyboardButton(cell, callback_data="typed:" + cell + ":" + message.message_id) for
                     cell in row])

            self.editable_messages[message.message_id] = ""
            bot.send_message(chat_id=message.chat.id, text='Type here:_',
                             reply_markup=InlineKeyboardMarkup(nkb)).wait()

    def handle_callback_query(self, manager, bot, query):
        if query.data and query.data.startswith('typed'):
            args = query.data.split(':')
            if len(args) == 3 and self.editable_messages[args[1]]:
                print(args)
