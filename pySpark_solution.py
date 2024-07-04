import os
#set environment variable to use specific python version
os.environ['PYSPARK_PYTHON'] = "C:\\Users\\karth\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"
import shutil

import string
from pyspark import SparkConf
from pyspark.context import SparkContext

def read_predefined_Words(file_path):
    """
    Reads predefined words from a file.

    Parameters:
    - file_path (str): The path to the file containing predefined words.

    Returns:
    - list: A list of predefined words.
    """

    with open(file_path, 'r', encoding='utf-8') as file:
        predefined_Words = [line.strip() for line in file.readlines()]
    return predefined_Words

def count_words(sc, predefined_words_file, files):
    """
    Counts occurrences of predefined words in a list of files using PySpark.

    Parameters:
    - sc (SparkContext): The Spark context.
    - predefined_words_file (str): The path to the file containing predefined words.
    - files (list): A list of file paths to process.

    Returns:
    - RDD: An RDD of (word, count) tuples sorted by count in descending order.
    """

    #translator for removing punctuation
    translator = str.maketrans('', '', string.punctuation)
    
     #list of predefined words (hardcoded for demonstration. can be replaced with file reading)
    predefined_Words = ["a", "about", "above", "after", "again", "all", "almost", "also", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "between", "but", "by", "can", "could", "did", "do", "does", "each", "either", "else", "enough", "for", "from", "had", "has", "have", "he", "her", "here", "hers", "herself", "him", "himself", "his", "how", "i", "if", "in", "into", "is", "it", "its", "itself", "just", "may", "me", "might", "mine", "most", "must", "my", "myself", "no", "nor", "not", "now", "of", "off", "on", "only", "or", "other", "our", "ours", "ourselves", "out", "over", "own", "said", "same", "say", "see", "she", "should", "since", "so", "some", "such", "than", "that", "the", "their", "them", "themselves", "then", "there", "these", "they", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "were", "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "within", "without", "would", "you", "your", "yours", "yourself", "yourselves"]
    
    # Uncomment below line to read predefined words from file
    #predefined_Words = read_predefined_Words(predefined_words_file)

    results = None
    
    for file in files:
        lines = sc.textFile(file)
        counts = lines.flatMap(lambda x: x.lower().split(' ')) \
                      .map(lambda x: x.translate(translator)) \
                      .filter(lambda x: x != '') \
                      .filter(lambda x: x in predefined_Words) \
                      .map(lambda x: (x, 1)) \
                      .reduceByKey(lambda a,b: a + b)
        
        if results == None:
            results = counts
        else:
            #union the results if there are multiple input files
            results = results.union(counts)

    #aggregate and sort the final results in descending order 
    results = results.reduceByKey(lambda a,b: a + b).sortBy(lambda x: x[1], False)
    return results

if __name__ == '__main__':
    #application name and Spark configuration
    appName = "WordCount"
    conf = SparkConf().setAppName(appName)
    sc = SparkContext(conf = conf)
    predefined_words_file = "data\\10k.txt"
    
    results = count_words(sc, predefined_words_file, ["data\\book.txt"])
    
    if results:
        output_dir = "output"
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
        results.coalesce(1).saveAsTextFile(output_dir)
        logger.info("Results saved successfully.")
    else:
        logger.info("No results to save.")
