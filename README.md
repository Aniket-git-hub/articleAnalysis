# Text Analysis Project - Assignment

## Overview

This project extracts article text from given URLs, performs text analysis, and computes various metrics. The results are saved in an Excel file named `analysis_result.xlsx` .

## Approach

The solution to this project was approached systematically, focusing on clarity, modularity, and efficiency of implementation. Here's a detailed overview of the approach:

1. **Understanding Requirements**: We began by carefully analyzing the project requirements, including the input data format, desired output variables, and the necessary textual analyses to be performed.

2. **Modular Design**: With a focus on maintainability and scalability, we designed the project with a modular structure. Each component, including data extraction, text analysis, and utility functions, was organized into separate modules for clarity and ease of maintenance.

3. **Data Extraction**: We implemented a robust data extraction module (`data_extraction.py`) responsible for retrieving article text from the provided URLs. Leveraging Python libraries such as Beautiful Soup and requests, this module ensures accurate extraction while handling various HTML structures.

4. **Text Analysis**: Our text analysis module (`text_analysis.py`) encompasses a comprehensive suite of analyses tailored to extract valuable insights from the article text. These analyses include sentiment analysis to gauge the emotional tone, readability metrics to assess the complexity of the text, and other textual metrics for deeper linguistic analysis.

5. **Utility Functions**: To streamline common tasks and ensure code reusability, we developed utility functions (`utils.py`). These functions handle tasks such as loading input data, managing stop words, and processing sentiment words.

6. **Logging**: Throughout the codebase, we integrated logging functionality to provide detailed visibility into the execution flow. Logging helps in tracking the progress of data extraction and analysis, as well as identifying and debugging any errors encountered during the process.

7. **Command-Line Interface**: We implemented a user-friendly command-line interface (`main.py`) to orchestrate the entire process. This interface allows users to easily execute data extraction and text analysis tasks with configurable options, such as enabling or disabling logging.

8. **Documentation**: To facilitate seamless collaboration and onboarding of new developers, we extensively documented the project. This includes a comprehensive README file with detailed setup instructions, usage guidelines, project structure overview, and licensing information.

## Project Structure

-   `main.py`: Main script to run the project.
-   `data_extraction.py`: Module for extracting and saving article text.
-   `text_analysis.py`: Module for computing text analysis metrics.
-   `utils.py`: Utility functions for loading resources and data.
-   `Input.xlsx`: Input file containing URLs and URL_IDs.
-   `StopWords/`: Folder containing stop words lists.
    -   `StopWords_Auditor.txt`
    -   `StopWords_Currencies.txt`
    -   `StopWords_DatesandNumbers.txt`
    -   `StopWords_Generic.txt`
    -   `StopWords_GenericLong.txt`
    -   `StopWords_Geographic.txt`
    -   `StopWords_Names.txt`
-   `MasterDictionary/`: Folder containing positive and negative words lists.
-   `articles/`: Folder where extracted articles are saved.
-   `analysis_result.xlsx`: Output file containing the computed metrics.

## How to Run

1. Ensure all necessary files (`Input.xlsx`, `positive-words.txt`, `negative-words.txt`, stop words files, etc.) are in the same directory.
2. Install required Python packages:

    ```cmd
    pip install pandas nltk beautifulsoup4 requests openpyxl
    ```

3. Run the main script with logging enabled (default):

    ```bash
    python main.py
    ```

    To disable logging, set the `enable_logging` parameter to `False`:

    ```bash
    python main.py false
    ```

## Dependencies

-   pandas
-   nltk
-   beautifulsoup4
-   requests
-   openpyxl

## Logging

The script includes optional logging to provide progress updates and help debug issues. By default, logging is enabled. To disable logging, set `enable_logging` to `False` in the `main()` function.
