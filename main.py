import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import TOKEN
from server import *

vk = vk_api.VkApi(token=TOKEN)

longpoll = VkLongPoll(vk)


COMMANDS = {
    'привет': command_hello,
    'как дела?': command_how_you,
}