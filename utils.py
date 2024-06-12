import pandas as pd
import os
import logging

def load_input(file_path):
    """
    Load input data from the specified Excel file.

    Args:
        file_path (str): Path to the input Excel file.

    Returns:
        Tuple: Tuple containing:
            - DataFrame: DataFrame containing input data.
            - list: List of URL IDs.
    """
    logger = logging.getLogger(__name__)

    # Validate file path
    if not file_path.endswith('.xlsx'):
        logger.error("Invalid file format. Input file must be in Excel format (.xlsx).")
        raise ValueError("Invalid file format.")

    try:
        # Load input data from Excel file
        input_data = pd.read_excel(file_path)

        # Validate required columns
        required_columns = ['URL', 'URL_ID']
        missing_columns = [col for col in required_columns if col not in input_data.columns]
        if missing_columns:
            logger.error(f"Missing required columns in input file: {missing_columns}")
            raise ValueError("Missing required columns.")

        # Validate missing values
        missing_values = input_data.isnull().sum()
        if any(missing_values):
            logger.error(f"Missing values found in input data:\n{missing_values}")
            raise ValueError("Missing values in input data.")

        # Extract URLs and URL IDs
        urls = input_data['URL'].tolist()
        url_ids = input_data['URL_ID'].tolist()

        logger.info("Input data loaded successfully.")
        return urls, url_ids

    except Exception as e:
        logger.error(f"Error loading input data: {e}")
        raise



def load_stop_words(folder='StopWords'):
    """
    Loads stop words from text files in the specified folder.

    Args:
        folder (str, optional): The folder containing stop word files. Defaults to 'StopWords'.

    Returns:
        set: A set containing all the stop words.
    """
    stop_words = set()
    stop_files = [
        'StopWords_Auditor.txt',
        'StopWords_Currencies.txt',
        'StopWords_DatesandNumbers.txt',
        'StopWords_Generic.txt',
        'StopWords_GenericLong.txt',
        'StopWords_Geographic.txt',
        'StopWords_Names.txt'
    ]
    for file in stop_files:
        file_path = os.path.join(folder, file)
        with open(file_path, 'r', encoding='latin-1') as f:
            stop_words.update(f.read().splitlines())
    return stop_words




def load_sentiment_words(folder='MasterDictionary'):
    """
    Loads positive and negative sentiment words from text files in the specified folder.

    Args:
        folder (str, optional): The folder containing sentiment word files. Defaults to 'MasterDictionary'.

    Returns:
        tuple: A tuple containing two sets - positive words and negative words.
    """
    with open(os.path.join(folder, 'positive-words.txt'), 'r', encoding='latin-1') as f:
        positive_words = set(f.read().split())
    
    with open(os.path.join(folder, 'negative-words.txt'), 'r', encoding='latin-1') as f:
        negative_words = set(f.read().split())
    
    return positive_words, negative_words