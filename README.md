# RagAgent

A sophisticated RAG (Retrieval-Augmented Generation) agent built with LlamaIndex that combines multiple data sources to provide comprehensive answers to user queries.

## Overview

RagAgent is an AI assistant that can:
- Query tabular data from Ordway customer CSV files
- Extract and provide information from PDF documents
- Save notes during conversations
- Combine information from multiple sources to provide comprehensive answers

The agent uses OpenAI's GPT-4o model with a ReAct agent pattern to determine which tools to use based on user queries.

## Project Structure

```
RagAgent/
├── main.py                # Entry point for the application
├── notes_engine.py        # Functionality for saving notes
├── pdf.py                 # PDF processing and indexing functionality
├── prompts.py             # Custom prompts for the agent
├── requirements.txt       # Project dependencies
└── data/                  # Data directory
    ├── customer.csv       # Ordway customer data
    ├── India.pdf          # PDF document
    ├── Metadata.pdf       # Metadata PDF document
    └── notes.txt          # User notes storage
```

## Features

- **Multi-source RAG**: Combines different data sources (CSV, PDF) into a unified agent
- **Note-taking capability**: Saves important information during conversations
- **Custom query engines**: Specialized engines for different data types
- **Interactive command-line interface**: Easy-to-use interface for querying the agent

## Setup

### Prerequisites

- Python 3.12+
- Virtual environment (recommended)

### Installation

1. Clone the repository
2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv ai
   source ai/bin/activate  # On Windows: ai\Scripts\activate
   ```
3. Install required packages:
   ```
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

Run the main script to start the interactive agent:

```
python main.py
```

Enter your queries when prompted. Type 'exit' to quit the application.

Example queries:
- "What's the customer with the highest contracted MRR?"
- "Tell me about the metadata in the PDF document"
- "Save a note that we need to follow up with client X"

## Components

- **PandasQueryEngine**: Processes tabular data from CSV files
- **PDF Query Engine**: Extracts and processes information from PDF documents
- **Notes Tool**: Saves user notes to a file
- **ReActAgent**: Coordinates between different tools based on user queries

## Dependencies

- llama-index & llama-index-experimental
- pandas
- python-dotenv
- openai
- pypdf
- numpy

## License

[Your license information here]

## Contact

[Your contact information here]
