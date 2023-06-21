from main import *

print('Бот запущен!')
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        if COMMANDS.get(event.text):
            COMMANDS[event.text](event.user_id)
        else:
            command_else(event.user_id)