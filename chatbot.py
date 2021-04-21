from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from  chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot(name="IntelliBot",
                  read_only=True,  # to learn new
                  logic_adapters=["chatterbot.logic.MathematicalEvaluation","chatterbot.logic.BestMatch"])

import generaltalk


conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

math_talk1 = [
    'pythagorean theorem',
    'a squared plus b squared equals c squared',
    'pie value',
    '3.14'
]


general_talk = ['what is your name','My name is IntelliBot',
                'code',' 229 ']

list_trainer = ListTrainer(chatbot)

# training everything
for item in (conversation,math_talk1,general_talk,generaltalk.general_que1):
    list_trainer.train(item)

corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train('chatterbot.corpus.english')


