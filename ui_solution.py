import streamlit as st
from collections import defaultdict
import os

def read_predefined_words(file=None, word_list=None):
    """
    Reads predefined words from an uploaded file or from a list of comma-separated values,
    returns a set of these words for efficient lookups.
    """
    predefined_words = set()
    if file:
        decoded_file = file.getvalue().decode("utf-8")
        predefined_words.update(line.strip() for line in decoded_file.splitlines())
    if word_list:
        predefined_words.update(word.strip() for word in word_list.split(','))
    return predefined_words

def count_words(predefined_words, input_files):
    """
    Reads input files, counts the occurrences of predefined words,
    and returns a dictionary with the counts.
    """
    word_count = defaultdict(int)
    for input_file in input_files:
        decoded_file = input_file.getvalue().decode("utf-8")
        for line in decoded_file.splitlines():
            words = line.strip().split()
            for word in words:
                if word in predefined_words:
                    word_count[word] += 1
    return dict(word_count)

st.markdown("<h1 style='text-align: center; color: #eb5715;'>Predefined Word Counter</h1>", unsafe_allow_html=True)


#upload predefined words file or enter manually
words_file = st.file_uploader("Upload a file with predefined words (one per line)", type=['txt'])
words_text = st.text_input("Or enter predefined words as comma-separated values")

#upload one or more input files to process
input_files = st.file_uploader("Upload text files to process", type=['txt'], accept_multiple_files=True)

if st.button("Count Words"):
    if not input_files:
        st.error("Please upload at least one text file.")
    else:
        #read predefined words from file or text input
        if words_file is not None:
            predefined_words = read_predefined_words(file=words_file)
        elif words_text:
            predefined_words = read_predefined_words(word_list=words_text)
        else:
            st.error("Please provide predefined words via file or text input.")
            st.stop()

        results = {}
        for uploaded_file in input_files:
            count = count_words(predefined_words, [uploaded_file])
            results[uploaded_file.name] = count

        for filename, counts in results.items():
            st.subheader(f"Word counts for {filename}:")
            found_any = False
            for word in predefined_words:
                word_count = counts.get(word, 0)
                if word_count > 0:
                    st.write(f"{word}: {word_count}")
                    found_any = True
                else:
                    st.write(f"{word}: Not found")
            if not found_any:
                st.write("No predefined words found in this file.")

