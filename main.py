from haiku_bot import HaikuBot
import os

# importing, lower-casing and removing punctuation from text, tokenizing
if __name__ == '__main__':

    train_text = ''
    for text_file in os.listdir('text'):
        text = open('text/' + text_file).read()
        train_text += text

    haiku_bot = HaikuBot(0)
    haiku_bot.train(text)
    haiku = print(haiku_bot.make_haiku())
