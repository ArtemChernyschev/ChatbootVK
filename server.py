import random

def send_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(1, 999999)})


def command_hello(user_id):
    send_msg(user_id, 'Добрый вечер!')


def command_how_you(user_id):
    send_msg(user_id, 'Всё окей, вы как? Погнали отдыхать!!!')


def command_else(user_id):
    send_msg(user_id, 'Чтот не понял...!')