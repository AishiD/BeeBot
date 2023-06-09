import random


def handle_response(message) -> str:
    p_message=message.lower()

    if p_message == 'hello' or p_message == 'hi':
        return "Hello there!"
    if p_message == 'roll':
        return str(random.randint(1, 6))
    if p_message == 'pick a number':
        return str(random.randint(1, 100))
    if p_message == 'rate me':
        rate = str(random.randint(1, 6))
        return "Umm..you're a " + rate
    if p_message == 'bye':
        return "Bye. See you later!"
    if p_message == '!help':
        return "`This is a help message that you can modify.`"

