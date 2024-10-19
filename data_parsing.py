import nltk
import os
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import string
from collections import Counter
import matplotlib.pyplot as plt
import textstat
import pandas as pd
from matplotlib_venn import venn2
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


def readability_analysis(text):
    flesch_score = textstat.flesch_reading_ease(text)
    gunning_fog = textstat.gunning_fog(text)
    return flesch_score, gunning_fog


def process_directory(directory, label):
    """
    Process all text files in a directory.
    :param directory: Directory containing text files.
    :param label: Label for the type of epistle (e.g., "Undisputed" or "Pastoral").
    :return: List of dictionaries with the data for each epistle.
    """
    files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.txt')]
    data = []

    for file in files:
        epistle_name = os.path.basename(file).replace('.txt', '')

        # Load and preprocess the text
        text = load_text(file)
        words, sentences = preprocess_text(text)

        # Perform analyses
        word_freq = word_frequency_analysis(words)
        avg_sentence_length = sentence_length_analysis(sentences)

        # Add data to a list
        data.append({
            'epistle': epistle_name,
            'label': label,
            'word_count': len(words),
            'avg_sentence_length': avg_sentence_length,
            'top_10_words': word_freq.most_common(10)
        })

    return data
# Process both directories
undisputed_data = process_directory('./texts/undisputed', 'Undisputed')
pastoral_data = process_directory('./texts/pastorals', 'Pastoral')

combined_undisputed_counter = Counter()
for words in undisputed_data:
    combined_undisputed_counter.update(Counter(words))

# Get unique words from the undisputed epistles
undisputed_words = set(combined_undisputed_counter.keys())

# Merge all word frequencies for pastoral epistles
combined_pastoral_counter = Counter()
for words in pastoral_data:
    combined_pastoral_counter.update(Counter(words))

# Get unique words from the pastoral epistles
pastoral_words = set(combined_pastoral_counter.keys())

# Now you can calculate the unique and shared words
unique_to_pastoral = pastoral_words - undisputed_words
unique_to_undisputed = undisputed_words - pastoral_words
shared_words = pastoral_words & undisputed_words

# Create a Venn Diagram
plt.figure(figsize=(8, 8))
venn = venn2([undisputed_words, pastoral_words], set_labels=('Undisputed', 'Pastoral'))
venn.get_label_by_id('10').set_text(f"Unique to Undisputed\n({len(unique_to_undisputed)})")
venn.get_label_by_id('01').set_text(f"Unique to Pastoral\n({len(unique_to_pastoral)})")
venn.get_label_by_id('11').set_text(f"Shared\n({len(shared_words)})")

plt.savefig(f"{'Unique and Shared Words in Undisputed and Pastoral Epistles'.replace(' ', '_')}.png")

# Combine the data
all_data = undisputed_data + pastoral_data

# Convert the data into a Pandas DataFrame for easier analysis
df = pd.DataFrame(all_data)

# Save to CSV for further analysis
df.to_csv('epistle_analysis.csv', index=False)

# Display the DataFrame
print(df)



