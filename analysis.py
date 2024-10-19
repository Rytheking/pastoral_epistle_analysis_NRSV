import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt_tab')  # Download necessary resources

def load_text(file_path):
    """
    Load the content of a text file.
    :param file_path: Path to the text file.
    :return: String content of the file.
    """
    with open(file_path, 'r') as file:
        return file.read()

# Punkt is a sentence tokenizer that has been trained on english enough to handle ambiguity
# like Dr. vs a . at the end of a sentence


def preprocess_text(text):
    """
    Tokenize the text into words and sentences.
    :param text: String of text.
    :return: Tuple (list of words, list of sentences)
    """
    words = word_tokenize(text)
    sentences = sent_tokenize(text)
    return words, sentences

text = load_text('./texts/undisputed/romans.txt')
words, sentences = preprocess_text(text)
print(words)  # List of words
print(sentences)  # List of sentences
