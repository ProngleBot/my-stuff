import time
from python_omegle import ChatEvent
from python_omegle import InterestsChat

def chat_loop(chat):
    while True:
        # Start a new chat every time the old one ends
        print("- Starting chat -")
        chat.start()
        chat.send('https://discord.gg/UKTxcfk 13+ SFW, Join us! ')
        time.sleep(5)
        chat.end()
if __name__ == "__main__":
    chat = InterestsChat(["Discord"])
    chat_loop(chat=chat)
chat = InterestsChat(["Discord","Positivity","Hello","Talk","Music","Therapy"])
chat_loop(chat = chat)