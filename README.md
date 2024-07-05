# Word Counter/Checker

## Overview

This Streamlit application counts the occurrences of predefined words in uploaded text files. Users can either upload a text file containing predefined words or manually input them as comma-separated values. The application is useful for quickly assessing the presence and frequency of specific terms across multiple documents.

## Installation

To run this Streamlit application, Python is need installed on the system. The application depends on several Python libraries, including Streamlit.

### Prerequisites

Ensure Python 3.6 or later installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Steps

1. **Clone or download this repository** to local machine.

2. **Navigate to project directory** where the `ui_solution.py` file is located.

3. **Install required Python libraries**. Run the following command to install dependencies:

    ```bash
    pip install streamlit
    ```

4. **Run the application**. Execute the following command in your terminal:

    ```bash
    streamlit run ui_solution.py
    ```

5. **Access the application**. Open your web browser and go to `http://localhost:8501` to use the application. Sample predefined files (10k.txt and 20k.xt) and input file (book.txt) is present in data directory in the project file.

## Usage

- **Upload Predefined Words**: You can upload a `.txt` file with predefined words listed one per line, or you can enter the words manually as comma-separated values in the provided text input field.

- **Upload Text Files**: Upload one or more `.txt` input files that you want to analyze. The application will count the occurrences of each predefined word in these files.

- **View Results**: After uploading the files and clicking on "Count Words", the application will display the counts for each predefined word found in the uploaded text files. If a word is not found, it will be indicated.

## Additional Implementations

### Simple Word Counter (`solution.py`)

A basic Python script that counts occurrences of predefined words in text files without concurrency or distributed processing frameworks.

### Multithreaded Word Counter (`multiThread_solution.py`)

Enhances the basic word counting functionality by utilizing Python's `concurrent.futures` module to process text data in parallel across multiple threads. This approach is beneficial for processing larger files more quickly on systems with multiple CPU cores.

### PySpark Word Counter (`pySpark_solution.py`)

Leverages Apache Hadoop and PySpark for distributed data processing, enabling scalable and efficient word counting across very large datasets or multiple files. This implementation is ideal for enterprise-level applications where data volume exceeds the memory capacity of a single machine.

## Sample screenshots:
![img1](https://github.com/dhayanesh/word-counter/assets/63561465/30660a5b-f23d-4fdf-bad3-08bb2cd7c45f)
![img2](https://github.com/dhayanesh/word-counter/assets/63561465/934cab12-e75a-4ee7-a71b-dc36edca851d)
![img3](https://github.com/dhayanesh/word-counter/assets/63561465/c50cc275-fcb8-447a-9530-d8dc94434d20)


