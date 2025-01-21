# NLP Influencers Network Analysis

Analyze YouTube influencer networks and content using NLP techniques. Extract video data, analyze relationships, and generate insights from Spanish-speaking influencers' content.

## Quick Start

```bash
# Clone the repository
git clone [repository-url]
cd NLP_influencers

# Install dependencies
pip install -r requirements.txt

# Set up YouTube API
# 1. Get API key from Google Cloud Console
# 2. Replace API_KEY in ETL_video_1.py and Comments_extraction.py

# Run data collection
python ETL_video_1.py
python Comments_extraction.py
```

## Overview

This project analyzes Spanish-speaking YouTube influencers through:
- Content analysis using NLP
- Network relationship mapping
- Engagement metrics analysis
- Named Entity Recognition for person mentions
- Interactive visualizations

## Project Structure

```
.
├── Data Collection Scripts
│   ├── ETL_video_1.py              # Video metadata and transcript extraction
│   └── Comments_extraction.py       # Comments data extraction
│
├── Network Analysis
│   ├── network_influencers.ipynb    # Cross-influencer network analysis
│   ├── network.html                 # Basic network visualization
│   └── enhanced_network.html        # Enhanced network with metrics
│
├── Influencer Folders               # Individual analysis per influencer
│   ├── [influencer]/               # Repeated for each influencer below
│   │   ├── Data/
│   │   │   ├── [influencer]_videos.csv     # Raw video data
│   │   │   ├── [influencer]_comments.csv   # Raw comments
│   │   │   ├── preprocessed_data.csv       # Cleaned text data
│   │   │   ├── refined_per_data.csv        # Processed mentions
│   │   │   ├── PER_filtered_data.csv       # Filtered entities
│   │   │   └── PER2_token.csv             # Tokenized mentions
│   │   │
│   │   ├── Analysis/
│   │   │   ├── EDA_[influencer].ipynb      # Exploratory analysis
│   │   │   ├── preprocessing_text.ipynb     # Text preprocessing
│   │   │   ├── transcript_NLP_test.ipynb    # NLP analysis
│   │   │   ├── transcript_NLP_lemma.ipynb   # Lemmatization
│   │   │   ├── network.ipynb               # Network analysis
│   │   │   ├── PER.ipynb                   # Entity recognition
│   │   │   ├── per_clean.ipynb             # Entity cleaning
│   │   │   └── horastrabajo.ipynb          # Work hours analysis
│   │   │
│   │   └── Visualizations/
│   │       ├── Network/
│   │       │   ├── network.html            # Basic network
│   │       │   └── network_preprocessed.html # Processed network
│   │       │
│   │       └── WordClouds/
│   │           ├── title_wordcloud.png      # Title analysis
│   │           ├── description_wordcloud.png # Description analysis
│   │           ├── transcript_wordcloud.png  # Transcript analysis
│   │           ├── *_preprocessed.png       # Processed versions
│   │           └── all_words.png            # Combined analysis
│   │
│   ├── auronplay/                  # Spanish streamer
│   ├── ElRubius/                   # Gaming content creator
│   ├── Ibai/                       # Sports and entertainment
│   ├── Vegetta/                    # Gaming content
│   ├── DjMario/                    # Music and gaming
│   ├── Orslok/                     # Variety content
│   ├── Mostopapi/                  # Entertainment
│   ├── MartaDiaz/                  # Lifestyle content
│   ├── Malbert/                    # Comedy content
│   ├── EmmaChamberlain/            # English content (comparison)
│   └── clakovi/                    # Gaming content
│
├── lib/                            # Shared utilities and functions
│   └── [shared python modules]
│
├── requirements.txt                # Project dependencies
└── memoria_TFM_versionfinal.pdf    # Detailed project documentation
```

## Analysis Pipeline

1. **Data Collection & ETL**
   - Extract video metadata using YouTube API (`ETL_video_1.py`)
     - Video titles, descriptions, statistics
     - View counts, likes, comments
     - Video transcripts (when available)
   - Collect comments data (`Comments_extraction.py`)
     - Comment text and metadata
     - Comment statistics
     - User interaction data

2. **Exploratory Data Analysis**
   - Per-influencer analysis (`EDA_[influencer].ipynb`)
     - Posting patterns and frequency
     - Engagement metrics analysis
     - Content type distribution
     - Temporal trends
   - Data quality assessment
     - Missing data handling
     - Outlier detection
     - Data validation

3. **Text Processing & NLP**
   - Text preprocessing (`preprocessing_text.ipynb`)
     - Tokenization and normalization
     - Stop word removal
     - Special character handling
     - Language detection and filtering
   - Named Entity Recognition (`PER.ipynb`)
     - Person name extraction
     - Entity standardization (`per_clean.ipynb`)
     - Name variant mapping
   - Content Analysis
     - Word frequency analysis
     - Topic extraction
     - Keyword identification
     - Word cloud generation

4. **Network Analysis**
   - Individual Network Analysis (`network.ipynb`)
     - Per-influencer connection mapping
     - Local community detection
     - Influence metrics calculation
   - Cross-influencer Analysis (`network_influencers.ipynb`)
     - Relationship network construction
     - Community detection
     - Centrality analysis
     - Influence flow mapping

5. **Visualization & Reporting**
   - Network Visualizations
     - Basic network graphs (`network.html`)
     - Enhanced network visualization (`enhanced_network.html`)
     - Interactive network exploration
   - Content Insights
     - Word clouds for different text fields
     - Temporal pattern visualizations
     - Engagement metric charts
   - Final Analysis
     - Key findings documentation
     - Pattern identification
     - Insight generation

## Key Features

- **Content Analysis**
  - Multi-language support (ES/EN)
  - Topic modeling
  - Person mention detection
  - Temporal patterns

- **Network Analysis**
  - Relationship mapping
  - Community detection
  - Influence measurement

- **Visualization**
  - Interactive networks
  - Word clouds
  - Engagement metrics

## Requirements

See `requirements.txt` for full list of dependencies.

Main requirements:
- Python 3.x
- YouTube Data API credentials
- 2GB+ RAM for NLP processing

## Data Files

- **Input**
  - YouTube API credentials
  - List of influencer channels

- **Output**
  - **Raw Data**
    - `[influencer]_videos.csv`: Video metadata
    - `[influencer]_comments.csv`: Comment data
  
  - **Processed Data**
    - `refined_per_data.csv`: Processed person mentions
    - `preprocessed_data.csv`: Cleaned text data
    - `PER_filtered_data.csv`: Filtered person entities
    - `PER2_token.csv`: Tokenized person mentions

  - **Network Visualizations**
    - `network.html`: Basic network graph
    - `enhanced_network.html`: Detailed network visualization
    - `network_preprocessed.html`: Network with preprocessed data

  - **Word Clouds**
    - `title_wordcloud.png`: Most frequent words in video titles
    - `description_wordcloud.png`: Key terms from video descriptions
    - `transcript_wordcloud.png`: Common words from video transcripts
    - `title_preprocessed.png`: Processed title word frequencies
    - `description_preprocessed.png`: Processed description terms
    - `transcript_preprocessed.png`: Processed transcript analysis
    - `all_words.png`: Combined word frequency visualization

## Notes

- Data collection configured until April 1, 2023
- Optimized for Spanish content analysis
- Handles API rate limits automatically
- Parallel processing support

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT License

Copyright (c) 2024 NLP Influencers Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 