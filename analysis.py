def load_text(file_path):
    """
    Load the content of a text file.
    :param file_path: Path to the text file.
    :return: String content of the file.
    """
    with open(file_path, 'r') as file:
        return file.read()

text = load_text('./texts/undisputed/romans.txt')
print(text)
