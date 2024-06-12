import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import re


def calculate_scores(article, positive_words, negative_words, stop_words, logger):
    """
    Calculate sentiment analysis scores for the given article.

    Args:
        article (str): The text of the article.
        positive_words (set): Set of positive words.
        negative_words (set): Set of negative words.
        stop_words (set): Set of stop words.
        logger (Logger): Logger object for logging.

    Returns:
        tuple: A tuple containing the positive score, negative score, polarity score, and subjectivity score.
    """
    logger.info("Tokenizing words for sentiment analysis...")
    words = word_tokenize(article)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    logger.info("Calculating positive and negative scores...")
    pos_score = sum(1 for word in filtered_words if word in positive_words)
    neg_score = sum(1 for word in filtered_words if word in negative_words) * -1
    
    logger.info("Calculating polarity and subjectivity scores...")
    polarity_score = (pos_score - neg_score) / ((pos_score + neg_score) + 0.000001)
    subjectivity_score = (pos_score + neg_score) / (len(filtered_words) + 0.000001)
    
    return pos_score, neg_score, polarity_score, subjectivity_score

def calculate_readability_metrics(article, logger):
    """
    Calculate readability metrics for the given article.

    Args:
        article (str): The text of the article.
        logger (Logger): Logger object for logging.

    Returns:
        tuple: A tuple containing the average sentence length, percentage of complex words, fog index,
               count of complex words, and total word count.
    """
    logger.info("Tokenizing sentences for readability metrics...")
    sentences = sent_tokenize(article)
    words = word_tokenize(article)
    total_words = len(words)
    
    logger.info("Calculating average sentence length...")
    avg_sentence_length = total_words / len(sentences)
    
    logger.info("Identifying complex words...")
    complex_words = [word for word in words if count_syllables(word) > 2]
    
    logger.info("Calculating percentage of complex words and Fog Index...")
    perc_complex_words = len(complex_words) / total_words
    fog_index = 0.4 * (avg_sentence_length + perc_complex_words)
    complex_word_count = len(complex_words)
    
    return avg_sentence_length, perc_complex_words, fog_index, complex_word_count, total_words


def count_syllables(word):
    """
    Count the number of syllables in a word.

    Args:
        word (str): The word to count syllables for.

    Returns:
        int: The number of syllables in the word.
    """
    word = word.lower()
    syllables = len(re.findall(r'[aeiouy]+', word))
    if word.endswith('es') or word.endswith('ed'):
        syllables -= 1
    return max(1, syllables)


def calculate_other_metrics(article, logger):
    """
    Calculate other metrics for the given article.

    Args:
        article (str): The text of the article.
        logger (Logger): Logger object for logging.

    Returns:
        tuple: A tuple containing the syllables per word, count of personal pronouns, average word length,
               and average number of words per sentence.
    """
    logger.info("Calculating syllables per word...")
    words = word_tokenize(article)
    syllables_per_word = sum(count_syllables(word) for word in words) / len(words)
    
    logger.info("Counting personal pronouns...")
    personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', article, re.IGNORECASE))
    
    logger.info("Calculating average word length...")
    avg_word_length = sum(len(word) for word in words) / len(words)

    logger.info("Calculating average number of words per sentence...")
    sentences = sent_tokenize(article)
    total_words = sum(len(word_tokenize(sentence)) for sentence in sentences)
    avg_words_per_sentence = total_words / len(sentences) if len(sentences) > 0 else 0
    
    return syllables_per_word, personal_pronouns, avg_word_length, avg_words_per_sentence
