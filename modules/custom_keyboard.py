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
            self.editable_messages[message.message_id] = "UNSET"
            bot.send_message(chat_id=message.chat.id, text='Type here: _',
                             reply_markup=self.get_markup(message.message_id)).wait()

    def handle_callback_query(self, manager, bot, query):
        if query.data and query.data.startswith(get_name()):
            args = query.data.split(':')
            if len(args) == 3 and self.editable_messages.get(int(args[2])):
                text = self.editable_messages.pop(int(args[2]))
                if args[1] == '<':
                    if len(text) == 1 or text == "UNSET":
                        text = "UNSET"
                    else:
                        text = text[:-1]
                elif args[1] == ' ':
                    if not text == "UNSET":
                        text += ' '
                elif args[1] == '>':
                    bot.edit_message_text(query.sender.first_name + ": " + text,
                                          message_id=query.message.message_id,
                                          chat_id=query.message.chat.id)
                    return
                elif text == "UNSET":
                    text = args[1]
                else:
                    text += args[1]

                self.editable_messages[int(query.message.message_id)] = text
                bot.edit_message_text("Type here: " + text + "_", message_id=query.message.message_id,
                                      chat_id=query.message.chat.id,
                                      reply_markup=self.get_markup(query.message.message_id)).wait()

    def get_markup(self, message_id):
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
                [InlineKeyboardButton(cell, callback_data=get_name() + ":" + cell + ":" + str(message_id))
                 for cell in row])
        return InlineKeyboardMarkup(nkb)