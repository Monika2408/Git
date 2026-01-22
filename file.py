def count(file_path):
    """Counts the number of lines, words, and characters in a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        tuple: A tuple containing the number of lines, words, and characters.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        lines = content.splitlines()
        num_lines = len(lines)
        num_words = len(content.split())
        num_characters = len(content)
    return num_lines, num_words, num_characters