import re
import random
import nltk
import pronouncing
from nltk.corpus import cmudict

class HaikuBot():
    """Class to generate haikus using restricted markov chains"""

    def __init__(self, ngram_size=2):
        """
        Basic initialisation, takes:
        ngam_size (int): size of ngrams to be used for markov chains

        No returns (void)
        """
        self.ngram_size = ngram_size
        self.ngrams = {}
        self.tokens = []

    def train(self, text):
        """
        Loads text into model, can be used  takes:
        text (str): test to be loaded into model

        No returns (void)
        """
        # training text is lowercased and only alphabetic characters
        train_text = text.lower()
        train_text = re.sub("\n", " ", train_text)
        train_text = re.sub("[^a-zA-Z]", " ", train_text)
        self.tokens = nltk.word_tokenize(train_text)
        # splitting into ngram sequences
        for i in range(len(self.tokens) - self.ngram_size):
            sequence = ' '.join(self.tokens[i:i+self.ngram_size])
            if sequence not in self.ngrams.keys():
                self.ngrams[sequence] = [self.tokens[i+self.ngram_size]]
            else:
                self.ngrams[sequence].append(self.tokens[i+self.ngram_size])

    def make_haiku(self):
        """
        Will attempt to generate a markov chain haiku, follows a few simple rules:

        1. selects random starting point, from training text
        2. will try to restict lines based on stresses in word
        3. if not possible (because correctly sylabbled following word
            not in training text) then will overspill

        Takes no arguments.
        Returns haiku in form of string.
        """
        # picking random ngram group as start point
        start_position = random.randint(0, len(self.tokens) - self.ngram_size)
        current_sequence = ' '.join(self.tokens[start_position:start_position + self.ngram_size])
        output = current_sequence + ' '

        # looping through each haiku line
        haiku_counts = [5 - self.count_syllables(output), 7, 5]

        for syllables in haiku_counts:
            while syllables > 0:
                possible_words = self.ngrams[current_sequence]
                possible_words = sorted(possible_words, key=possible_words.count, reverse=True)
                # attempting to restrict based on syllable
                right_stress_words = [word for word in possible_words if self.count_syllables(word) <= syllables]
                if len(right_stress_words) != 0:
                    possible_words = right_stress_words
                else:
                    possible_words = sorted(possible_words, key=self.count_syllables)
                # random selection of possible words, weighted by ngram frequency
                weights = [1/(i+1) for i in range(len(possible_words))]
                next_word = random.choices(possible_words, weights)[0]
                output += next_word + ' '
                seq_words = nltk.word_tokenize(output)
                current_sequence = ' '.join(seq_words[len(seq_words)-self.ngram_size:len(seq_words)])
                syllables -= self.count_syllables(next_word)

            output += '\n'

        return output

    def count_syllables(self, string):
        """
        Returns syllables of a string using regex vowel/dipthong search, takes:

        string (string): string to count syllables of

        Returns int
        """
        return len(
            re.findall('(?!e$)[aeiouy]+', string, re.I) +
            re.findall('^[^aeiouy]*e$', string, re.I)
        )
