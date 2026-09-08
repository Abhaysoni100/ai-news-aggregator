🤖 AI News Aggregator

An AI-powered news aggregation application that collects the latest technology and artificial intelligence news from multiple sources, scrapes article content, generates AI summaries using a local LLM, and stores everything in PostgreSQL.

🚀 Features
📰 Fetches AI and technology news using RSS feeds
🌐 Aggregates news from multiple sources
🕷️ Scrapes full article content
🤖 Generates AI-powered summaries using Ollama
💾 Stores articles and summaries in PostgreSQL
🔄 Prevents duplicate articles using unique URLs
🐳 Runs PostgreSQL using Docker
⚡ Uses SQLAlchemy ORM for database operations
🏗️ Architecture
RSS Feeds
    │
    ▼
RSS Service
    │
    ▼
Article Scraper
    │
    ▼
AI Summary Generator (Ollama)
    │
    ▼
PostgreSQL Database
🛠️ Tech Stack
Technology	Purpose
Python 3.12	Core application
UV	Python package and environment management
PostgreSQL 16	Database
Docker	PostgreSQL container
SQLAlchemy	ORM
Feedparser	RSS feed parsing
BeautifulSoup	Web scraping
Ollama	Local AI model execution
Gemma 3	AI summarization model
Requests	HTTP requests
📰 News Sources

The application currently collects news from:

MIT Technology Review
VentureBeat AI
TechCrunch AI
📁 Project Structure
ai-news-aggregator/
│
├── src/
│   └── ai_news_aggregator/
│       │
│       ├── ai/
│       │   └── ollama_service.py
│       │
│       ├── database/
│       │   └── connection.py
│       │
│       ├── models/
│       │   └── article.py
│       │
│       ├── scrapers/
│       │   └── article_scraper.py
│       │
│       ├── services/
│       │   ├── rss_service.py
│       │   └── article_service.py
│       │
│       └── main.py
│
├── README.md
├── pyproject.toml
└── uv.lock
⚙️ Prerequisites

Before running the project, make sure you have installed:

Python 3.12+
Docker Desktop
Ollama
UV
🐳 Database Setup

Run PostgreSQL using Docker:

docker run --name ai-news-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=ai_news \
  -p 5433:5432 \
  -d postgres:16

Check if the container is running:

docker ps
🤖 Ollama Setup

Make sure Ollama is installed and running.

Download the Gemma model:

ollama pull gemma3:4b

Verify the model:

ollama list

You can also test it:

ollama run gemma3:4b "Summarize artificial intelligence in one sentence."
🔧 Environment Configuration

Create a .env file in the project root:

DATABASE_URL=postgresql://postgres:postgres@localhost:5433/ai_news
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=gemma3:4b

Make sure .env is included in .gitignore so credentials are not uploaded to GitHub.

📦 Installation

Clone the repository:

git clone https://github.com/Abhaysoni100/ai-news-aggregator.git

Navigate into the project:

cd ai-news-aggregator

Install dependencies:

uv sync
▶️ Running the Application

Start the PostgreSQL Docker container:

docker start ai-news-postgres

Make sure Ollama is running.

Then run:

uv run ai-news-aggregator
🔄 Application Workflow

When the application runs:

Fetches the latest articles from RSS feeds
Extracts article titles and URLs
Checks if the article already exists in PostgreSQL
Scrapes the article content
Sends the content to the local Ollama model
Generates an AI summary
Stores the article, content, and summary in PostgreSQL
Skips duplicate articles
🗄️ Database Schema

The articles table contains:

Column	Description
id	Unique article ID
title	Article title
url	Original article URL
source	News source
content	Full scraped article content
summary	AI-generated summary
published_at	Article publication date
created_at	Database record creation timestamp
📊 Example Output
Starting AI News Aggregator...

Fetching news from: MIT Technology Review
Fetching news from: VentureBeat AI
Fetching news from: TechCrunch AI

Generating AI summary for:
Meta debuts its Muse AI agent. Will consumers trust it?

-----------------------------
New articles saved: 20
Duplicate articles skipped: 0
-----------------------------

AI News Aggregator finished successfully!
🚧 Future Improvements
 Build REST APIs using FastAPI
 Add article search functionality
 Add filtering by news source
 Add article categories
 Add scheduled news fetching
 Build a web dashboard
 Add authentication
 Add Docker Compose support
 Deploy the application to the cloud
🎯 What I Learned

Through this project, I gained hands-on experience with:

RSS feed aggregation
Web scraping with BeautifulSoup
PostgreSQL database integration
SQLAlchemy ORM
Docker containers
Local LLM integration using Ollama
AI-powered text summarization
Duplicate detection
Python project structure and dependency management
👨‍💻 Author

Abhay Soni

GitHub: github.com/Abhaysoni100

⭐ If you found this project interesting, consider giving the repository a star!

Then save and push it
git add README.md
git commit -m "Add professional project README"
git push
