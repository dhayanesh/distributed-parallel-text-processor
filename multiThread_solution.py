import concurrent.futures
from collections import defaultdict

def read_predefined_words(file_path):
    """
    Reads a file containing predefined words, each on a new line,
    and returns a set of these words for efficient lookups.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        predefined_words = set(line.strip() for line in file)
    return predefined_words

def count_words_in_chunk(chunk, predefined_words):
    """
    Counts occurrences of predefined words in a chunk of text.
    """
    word_count = defaultdict(int)
    for line in chunk:
        words = line.strip().split()
        for word in words:
            if word in predefined_words:
                word_count[word] += 1
    return word_count

def merge_dictionaries(dicts):
    """
    Merges a list of dictionaries by summing values of common keys.
    """
    final_count = defaultdict(int)
    for d in dicts:
        for key, value in d.items():
            final_count[key] += value
    return final_count

def count_words(predefined_words_file, input_files, chunk_size=10240):
    """
    Reads input files, counts the occurrences of predefined words,
    and returns a dictionary with the counts.
    """
    predefined_words = ["a", "about", "above", "after", "again", "all", "almost", "also", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "between", "but", "by", "can", "could", "did", "do", "does", "each", "either", "else", "enough", "for", "from", "had", "has", "have", "he", "her", "here", "hers", "herself", "him", "himself", "his", "how", "i", "if", "in", "into", "is", "it", "its", "itself", "just", "may", "me", "might", "mine", "most", "must", "my", "myself", "no", "nor", "not", "now", "of", "off", "on", "only", "or", "other", "our", "ours", "ourselves", "out", "over", "own", "said", "same", "say", "see", "she", "should", "since", "so", "some", "such", "than", "that", "the", "their", "them", "themselves", "then", "there", "these", "they", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "were", "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "within", "without", "would", "you", "your", "yours", "yourself", "yourselves"]

    # Uncomment below line to read predefined words from file
    #predefined_words = read_predefined_words(predefined_words_file)
    
    word_counts = []
    
    for input_file in input_files:
        with open(input_file, 'r', encoding='utf-8') as file:
            chunk = []
            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
                futures = []
                
                for line in file:
                    chunk.append(line)
                    if len(chunk) >= chunk_size:
                        futures.append(executor.submit(count_words_in_chunk, chunk, predefined_words))
                        chunk = []
                
                #process any remaining lines in the last chunk
                if chunk:
                    futures.append(executor.submit(count_words_in_chunk, chunk, predefined_words))
                
                for future in concurrent.futures.as_completed(futures):
                    word_counts.append(future.result())
    
    final_count = merge_dictionaries(word_counts)
    return final_count

def main():
    predefined_words_file = "data\\10k.txt"
    input_files = ["data\\book.txt"]
    
    results = count_words(predefined_words_file, input_files)

    print("Word counts for predefined words found in the input file:")
    for word, count in results.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
