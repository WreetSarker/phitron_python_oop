"""
    building a demo chatbot
"""

greet_words = ['hi', 'hello', 'hey']
bye_words = ['bye', 'tata', 'sayonara']

def listen():
    return input("Say your command: ")

def process(command):
    broken_words = command.split(' ')
    
    for word in broken_words:
        if word.lower() in greet_words:
            talkback("He said greetings")
        elif word.lower() in bye_words:
            talkback("He said bye")

def talkback(response):
    print(response)


command = listen()
process(command)