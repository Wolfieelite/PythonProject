from Lab3.lab_chat import get_channel, get_peer_node, join_group, chat_task

def text_reset(text):
    text = text.upper()
    text = text.strip()

def get_username():
    username = input("Ah, you're finally awake. Can I get your name \n")
    text_reset(username)
    return username

def get_group():
    group_name = input("Great! Welcome! What group are you looking for? \n")
    text_reset(group_name)
    return group_name

def get_message():
    message = input("What would you like me to say? \n")
    message = message.strip()
    return message

def initialize_chat():
    name = get_username()
    group = get_group()
    join_group(name, group)

    return get_channel(name, group)

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("finished")

start_chat()
