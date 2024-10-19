import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import string
from collections import Counter
import matplotlib.pyplot as plt
# Punkt is a sentence tokenizer that has been trained on english enough to handle ambiguity
# like Dr. vs a . at the end of a sentence
nltk.download('punkt_tab')  # Download necessary resources
nltk.download('stopwords')

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
    stop_words = set(stopwords.words('english'))

    # Filter out stop words and punctuation
    words = [word.lower() for word in words if word.lower() not in stop_words and word not in string.punctuation]

    return words, sentences


def word_frequency_analysis(words):
    """
    Count the frequency of each word in the text.
    :param words: List of words.
    :return: Counter object with word frequencies.
    """
    return Counter(words)


def plot_word_frequency(word_freq, title):
    """
    Plot a bar chart of the most common words.
    :param word_freq: Counter object with word frequencies.
    :param title: Title of the plot.
    """
    words, counts = zip(*word_freq.most_common(10))  # Top 10 words
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts)
    plt.title(title)
    plt.xticks(rotation=45)

    # Save the plot to a file
    plt.savefig(f"{title.replace(' ', '_')}.png")
    print(f"Plot saved as {title.replace(' ', '_')}.png")

def sentence_length_analysis(sentences):
    """
    Calculate average sentence length.
    :param sentences: List of sentences.
    :return: Average sentence length in words.
    """
    sentence_lengths = [len(word_tokenize(sentence)) for sentence in sentences]
    avg_sentence_length = sum(sentence_lengths) / len(sentence_lengths)
    return avg_sentence_length


text = load_text('./texts/undisputed/romans.txt')
words, sentences = preprocess_text(text)
word_freq = word_frequency_analysis(words)
plot_word_frequency(word_freq, "Top 10 Words in Romans")
avg_length = sentence_length_analysis(sentences)
print(f"Average sentence length: {avg_length}")



