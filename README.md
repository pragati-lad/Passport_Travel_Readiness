# Passport Travel Readiness System

A data science application for managing travel data with sentiment analysis, entity extraction, and visualizations. Focuses on inclusive travel experiences.

## Features

- **Passenger Entry** - Collect traveler information including accessibility needs, medical conditions, dietary requirements
- **Feedback Analysis** - Sentiment analysis using TextBlob
- **Named Entity Recognition** - Extract entities from travel feedback using SpaCy
- **Visual Insights** - 4-plot dashboard showing traveler composition, baggage load, experience levels, and accessibility needs
- **Text Summarization** - Automated feedback summarization
- **Home Dashboard** - Easy navigation interface

## Technologies

- **Python 3.13** - Core language
- **Tkinter** - Desktop GUI framework
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization and plotting
- **SpaCy** - Natural Language Processing (NLP) and entity recognition
- **TextBlob** - Sentiment analysis and text processing
- **NumPy** - Numerical computing
- **Git** - Version control

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/pragati-lad/Passport_Travel_Readiness.git
   cd Passport_Travel_Readiness
   ```

2. Create virtual environment
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux
   ```

3. Install dependencies
   ```bash
   pip install pandas matplotlib spacy textblob
   python -m spacy download en_core_web_sm
   ```

## Usage

```bash
python home.py
```

## Project Structure

```
Passport_Travel_Readiness/
├── home.py                           # Main dashboard
├── registration.py                   # Passenger entry form
├── feedback_gui.py                   # Sentiment analysis
├── ner_gui.py                        # Entity extraction
├── summary_gui.py                    # Text summarization
├── plot_gui.py                       # Data visualization
├── passenger_registration.csv        # Main dataset (auto-generated)
├── sentiment_analysis.csv            # Sentiment analysis results
├── entity_extraction.csv             # Named entity extraction results
├── feedback_summary.csv              # Text summarization results
├── README.md                         # Project documentation
└── venv/                             # Virtual environment
```

## CSV Files Generated

The application automatically creates and updates the following CSV files:

- **passenger_registration.csv** - Main dataset containing all passenger information
  - Columns: Full_Name, Passport_Number, Date_of_Birth, Destination_Country, Travel_Purpose, Group_Size, Number_of_Bags, Children_Count, Elderly_Count, Accessibility_Needs, Medical_Conditions, Dietary_Requirements, Language_Preference, First_Time_Traveler, Emergency_Contact, Travel_Insurance, Vaccination_Status, Travel_Feedback

- **sentiment_analysis.csv** - Sentiment analysis results
  - Columns: Full_Name, Destination_Country, Travel_Feedback, Sentiment (Positive/Negative/Neutral)

- **entity_extraction.csv** - Named Entity Recognition results
  - Columns: Entity, Type (PERSON, LOCATION, ORG, PASSPORT_NUMBER, etc.)

- **feedback_summary.csv** - Text summarization results
  - Contains summarized versions of travel feedback




