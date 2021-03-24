import re
import random
import nltk

class HaikuBot:
    """
    Class to generate markov chains from text
    """

    def __init__(self, ngram_size=3):
        self.ngram_size = ngram_size
        self.ngrams = {}
        self.tokens = []

    def train(self, text):
        train_text = text.lower()
        train_text = re.sub(r"[,.';\"?!]+\ *", " ", train_text)
        train_text = re.sub("\n", " ", text)
        self.tokens = nltk.word_tokenize(train_text)
        for i in range(len(self.tokens) - self.ngram_size):
            sequence = ' '.join(self.tokens[i:i+self.ngram_size])
            if sequence not in self.ngrams.keys():
                self.ngrams[sequence] = [self.tokens[i+self.ngram_size]]
            else:
                self.ngrams[sequence].append(self.tokens[i+self.ngram_size])

    def output(self):
        start_position = random.randint(0, len(self.tokens) - self.ngram_size)
        output = ' '.join(self.tokens[start_position:start_position + self.ngram_size])
        current_sequence = output
        while not self.stop_condition(output):
            possible_words = self.ngrams[current_sequence]
            possible_words = sorted(possible_words, key = possible_words.count, reverse = True)
            output += ' ' + possible_words[0]
            seq_words = nltk.word_tokenize(output)
            curr_sequence = ' '.join(seq_words[len(seq_words)-self.ngram_size:len(seq_words)])
        return output

    def stop_condition(self, sentence):
        return len(sentence) > 100
