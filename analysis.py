import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
# Punkt is a sentence tokenizer that has been trained on english enough to handle ambiguity
# like Dr. vs a . at the end of a sentence
nltk.download('punkt_tab')  # Download necessary resources

def load_text(file_path):
    """
    Load the content of a text file.
    :param file_path: Path to the text file.
    :return: String content of the file.
    """
    with open(file_path, 'r') as file:
        return file.read()




def preprocess_text(text):
    """
    Tokenize the text into words and sentences.
    :param text: String of text.
    :return: Tuple (list of words, list of sentences)
    """
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    return words, sentences

from collections import Counter

def word_frequency_analysis(words):
    """
    Count the frequency of each word in the text.
    :param words: List of words.
    :return: Counter object with word frequencies.
    """
    return Counter(words)

text = load_text('./texts/undisputed/romans.txt')
words, sentences = preprocess_text(text)
word_freq = word_frequency_analysis(words)
print(word_freq.most_common(10))  # Top 10 most frequent words

