import sys
import pandas as pd
import logging
import nltk
from data_extraction import extract_and_save_articles
from text_analysis import calculate_scores, calculate_readability_metrics, calculate_other_metrics
from utils import load_input, load_stop_words, load_sentiment_words

def main(enable_logging=True):
    if enable_logging:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(level=logging.CRITICAL)

    logger = logging.getLogger(__name__)

    # Download punkt
    logger.info("Downloading NLTK resources...")
    nltk.download('punkt')

    # Load input data
    logger.info("Loading input data...")
    urls, url_ids = load_input('Input.xlsx')
    
    # Extract and save articles
    logger.info("Extracting and saving articles...")
    extract_and_save_articles(urls, url_ids, logger)
    
    # Load resources
    logger.info("Loading stop words and sentiment words...")
    stop_words = load_stop_words()
    positive_words, negative_words = load_sentiment_words()
    
    results = []
    for url_id, article_urls in zip(url_ids, urls):
        logger.info(f"Processing article {url_id}...")
        try:
            with open(f'articles/{url_id}.txt', 'r', encoding='utf-8') as file:
                title = file.readline().strip()
                article = file.read().strip()
            
            # Perform text analysis
            logger.info(f"Calculating scores for article {url_id}...")
            pos_score, neg_score, polarity_score, subjectivity_score = calculate_scores(article, positive_words, negative_words, stop_words, logger)
            
            logger.info(f"Calculating readability metrics for article {url_id}...")
            avg_sentence_length, perc_complex_words, fog_index, complex_word_count, total_words = calculate_readability_metrics(article, logger)
            
            logger.info(f"Calculating other metrics for article {url_id}...")
            syllables_per_word, personal_pronouns, avg_word_length, avg_words_per_sentence = calculate_other_metrics(article, logger)
            
            results.append([
                url_id, article_urls, pos_score, neg_score, polarity_score, subjectivity_score,
                avg_sentence_length, perc_complex_words, fog_index, avg_words_per_sentence, complex_word_count,
                total_words, syllables_per_word, personal_pronouns, avg_word_length
            ])
        except Exception as e:
            logger.error(f"Error processing article {url_id} - {e}")
    
    # Save results to Excel
    logger.info("Saving results to Excel...")
    output_df = pd.DataFrame(results, columns=[
        'URL_ID', 'URL', 'POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE', 'SUBJECTIVITY SCORE',
        'AVG SENTENCE LENGTH', 'PERCENTAGE OF COMPLEX WORDS', 'FOG INDEX', 'AVG NUMBER OF WORDS PER SENTENCE', 'COMPLEX WORD COUNT',
        'WORD COUNT', 'SYLLABLE PER WORD', 'PERSONAL PRONOUNS', 'AVG WORD LENGTH'
    ])
    output_df.to_excel('analysis_result.xlsx', index=False)
    logger.info("Results saved successfully in analysis_result.xlsx")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'false':
        main(enable_logging=False)
    else:
        main(enable_logging=True)