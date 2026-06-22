# 📚 Book Price Tracker

A web scraper and interactive Streamlit application that fetches and displays 1,000 books from [Books to Scrape](https://books.toscrape.com/).

## 🚀 Features
- **Scraper**: Crawls all 50 pages of the catalogue to collect details on 1,000 books (Title, Price, Availability, and Rating).
- **Interactive UI**: Search and filter books by title dynamically.
- **Fast Performance**: Uses Streamlit's `@st.cache_data` to cache scraping results so it doesn't slow down on subsequent queries.
- **Pagination**: Displays 20 books per page with Previous/Next buttons for comfortable reading.
- **CSV Download**: Export your searched/filtered books to a CSV file.

## 📂 Project Structure
- `app.py`: Streamlit frontend application.
- `scraper.py`: Core web scraper using BeautifulSoup4.
- `requirements.txt`: Python dependencies.
- `.gitignore`: Configured to ignore virtual environments, cache files, and OS files.

**Project link**https://bookapp-mrnhvkfedymx6vuumuqerl.streamlit.app/
