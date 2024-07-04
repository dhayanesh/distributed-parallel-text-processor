from collections import defaultdict

def read_predefined_words(file_path):
    """
    Reads a file containing predefined words, each on a new line,
    and returns a set of these words for efficient lookups.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        predefined_words = set(line.strip() for line in file)
    return predefined_words

def count_words(predefined_words_file, input_files):
    """
    Reads input files, counts the occurrences of predefined words,
    and returns a dictionary with the counts.
    """
    predefined_words = ["a", "about", "above", "after", "again", "all", "almost", "also", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "between", "but", "by", "can", "could", "did", "do", "does", "each", "either", "else", "enough", "for", "from", "had", "has", "have", "he", "her", "here", "hers", "herself", "him", "himself", "his", "how", "i", "if", "in", "into", "is", "it", "its", "itself", "just", "may", "me", "might", "mine", "most", "must", "my", "myself", "no", "nor", "not", "now", "of", "off", "on", "only", "or", "other", "our", "ours", "ourselves", "out", "over", "own", "said", "same", "say", "see", "she", "should", "since", "so", "some", "such", "than", "that", "the", "their", "them", "themselves", "then", "there", "these", "they", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "were", "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "within", "without", "would", "you", "your", "yours", "yourself", "yourselves"]

    # Uncomment below line to read predefined words from file
    #predefined_words = read_predefined_words(predefined_words_file)
    
    word_count = defaultdict(int)
    
    for input_file in input_files:
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    if word in predefined_words:
                        word_count[word] += 1
    
    word_count = dict(word_count)
    
    return word_count

def main():
    predefined_words_file = "data\\10k.txt"
    input_files = ["data\\book.txt"]
    
    results = count_words(predefined_words_file, input_files)

    print("Word counts for predefined words found in the input file:")
    for word, count in results.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
