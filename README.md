# Headline Sentiment and Media Bias Analysis

This project explores the relationship between media source bias, reliability, and the sentiment of news headlines. Using a dataset of 2,000+ headlines pulled from popular media outlets, the goal is to determine whether headline tone correlates with political leaning or perceived reliability — and whether there are meaningful differences between left- and right-skewing sources.

## Motivation

With most news shared online being consumed based solely on its headline (often without even clicking through to read the linked information), it’s important to understand how tone, sentiment, and bias interact. This analysis investigates whether headlines from left- or right-skewing sources differ meaningfully in sentiment, and whether sentiment correlates with source bias or reliability ratings.

## Key Findings

- **Slight tone difference**: Left-skewing sources showed slightly more positive average sentiment than right-skewing sources (mean difference = 0.08)
- **Statistically significant, but small effect**: While this difference was significant (*p* < 0.001), it was **not practically meaningful** (*Cohen’s d* = 0.19)
- **Greater variability on the right**: Right-skewing headlines showed a broader spread of sentiment scores, with a higher frequency of negative values
- **No strong correlations**:
  - Sentiment vs. bias direction: *r* = –0.07
  - Sentiment vs. bias strength: *r* = –0.10
  - Sentiment vs. reliability: *r* = 0.07

## How to Run This Project

The full analysis is contained in `notebooks/headline_analysis.ipynb`. 

To explore or reproduce:

1. **Clone the repository**:
   ```bash
   git clone git@github.com:Joshua-Byrd/HeadlineAnalysis.git
   cd headline_analysis
   ``` 
2. **(Optional but recommended) Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ``` 

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Launch Jupyter Notebook:**
    ```bash
    cd notebooks
    jupyter notebook headline_analysis.ipynb
    ```
*Note: There are no API calls required to run this project, as the data has been prefetched and is included in `data/flattened_articles.csv`. However, the analysis notebook details which scripts to 
run and in what order, should you wish to reproduce everything from scratch.*

## Project Structure
```
/          - contains all Python scripts for retrieving and processing data

/data/raw  - contains various json files in different stages of processing

/data      - contains the flattened csv file of article data used for analysis

/logs      - contains the logs of both the API calls and executed cron jobs

/notebooks - contains the Jupyter Notebook used for analysis, headline_analysis.ipynb
```

## Tools & Libraries

- **Python 3.12.7**
- `pandas`, `seaborn`, `matplotlib` – data analysis and visualization
- `nltk`, `vaderSentiment` – sentiment scoring
- `scipy.stats` – t-test, Pearson correlation
- `NewsAPI` – headline and source data
- `Ad Fontes Media` – bias and reliability ratings

## Methodology Overview

1. **Data Collection**: Headlines were collected over a 5-day period using NewsAPI and enriched with Ad Fontes ratings.
2. **Cleaning & Merging**: Articles and source data were merged into a single flat file.
3. **Sentiment Scoring**: VADER sentiment analysis was applied to each headline.
4. **Statistical Analysis**: Correlation coefficients, t-tests, and effect sizes were calculated to evaluate relationships between sentiment, bias, and reliability.
5. **Visualization**: Distributions were visualized using pie charts, bar charts, scatter plots, and violin plots.

## Limitations

- The dataset was left-skewed in source representation (~75% of headlines)
- All sources were relatively moderate in bias and reliability, limiting generalizability
- Headlines only — article content was not analyzed
- Five-day snapshot may not reflect long-term trends
- Bias ratings were sourced from Ad Fontes Media and may reflect subjective evaluations

## Suggestions for Further Research

- Expand data collection across longer periods and more diverse sources
- Include media with more extreme bias or reliability scores
- Analyze full article content in addition to headlines

## Author

**Joshua Byrd**  
M.S. in Software Development | Aspiring Data Analyst / Data Engineer  
[Portfolio Site](https://joshua-byrd.github.io/projects.html) | [LinkedIn](https://www.linkedin.com/in/joshua-byrd-356b93184/) | [GitHub](https://github.com/Joshua-Byrd)

This project was developed for portfolio purposes to demonstrate exploratory data analysis, sentiment scoring, and statistical evaluation in Python.