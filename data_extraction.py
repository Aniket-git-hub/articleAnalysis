import requests
from bs4 import BeautifulSoup
import os
import logging

def extract_article_text(url, logger):
    """
    Extracts the article title and text from the given URL.

    Args:
        url (str): The URL of the webpage containing the article.
        logger (Logger): Logger object for logging.

    Returns:
        tuple: A tuple containing the title and text of the article.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('h1').get_text() if soup.find('h1') else "No Title"
    article = ' '.join([p.get_text() for p in soup.find_all('p')])
    
    return title, article

def extract_and_save_articles(urls, url_ids, logger):
    """
    Extracts and saves articles from the given list of URLs.

    Args:
        urls (list): List of URLs of the webpages containing articles.
        url_ids (list): List of unique IDs corresponding to each URL.
        logger (Logger): Logger object for logging.
    """
    if not os.path.exists('articles'):
        os.makedirs('articles')
    
    for url, url_id in zip(urls, url_ids):
        try:
            logger.info(f"Extracting article from {url}...")
            
            title, article = extract_article_text(url, logger)
            # Save the extracted article to a text file
            with open(f'articles/{url_id}.txt', 'w', encoding='utf-8') as file:
                file.write(f"{title}\n{article}")
            
            logger.info(f"Article {url_id} saved successfully.")
        except Exception as e:
            logger.error(f"Failed to extract article from {url} - {e}")
