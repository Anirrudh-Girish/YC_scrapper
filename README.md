
# YC Directory Scrapper (v1.0)

A Python-based automation tool designed to extract and organize startup data from the Y Combinator (YC) company directory. This project serves as a practical application of web automation, handling dynamic content, and data integrity principles.

## 🚀 Project Overview

This tool automates the process of navigating the YC directory, which utilizes an "Infinite Scroll" mechanism. It effectively loads all 1,000+ companies before extracting structured data into a portable JSON format.

## 📊 Data Points Collected

* **Company Name**: Extracted using targeted CSS selectors for accuracy.
* **Industry Categories**: Captured as a list of tags (pills) for each startup to allow for easy filtering and analysis.

## 🛠️ Technical Features & Skills Applied

### 1. Dynamic Content & Infinite Scroll

Standard scraping tools cannot "see" the full YC list because content only loads as the user scrolls.

* **Implementation**: I used Selenium to execute JavaScript commands (`window.scrollTo`).
* **Logic**: The script compares `scrollHeight` before and after scrolling to detect when the absolute bottom of the page has been reached.

### 2. Data Integrity & Unicode Safety

Scraping international startup names often involves special characters.

* **The Problem**: Default text writing can corrupt non-standard characters.
* **The Solution**: Following best practices for web data, I implemented `utf-8` encoding to maintain the **Unicode encoding** of the text, ensuring names are saved exactly as they appear on the server.

### 3. Environment & Dependency Management

* **Virtual Environments**: The project is built within a dedicated `.venv` to prevent library conflicts.
* **Automation Tools**: Utilized `webdriver-manager` to automatically handle Chrome driver binaries, ensuring the script runs on any machine without manual setup.

## 📂 Project Structure

* `main.py`: The core Selenium script for automation and extraction.
* `counter.py`: A utility script to verify the total count and integrity of the scraped data.
* `.gitignore`: Configured to exclude local environments (`.venv/`) and raw data caches.

## ⚙️ How to Run

1. **Clone the repository** to your local machine.
2. **Activate the virtual environment**:
```powershell
.\.venv\Scripts\activate

```


3. **Install dependencies**:
```bash
pip install selenium webdriver-manager

```


4. **Execute the scraper**:
```bash
python main.py

```



## 📈 Future Roadmap

* **Phase 2 (Deep Scraping)**: Enhance the script into a "Spider" that clicks into each company card to collect "Team Size," "Founded Year," and "Company Website."
* **Database Integration**: Migrate storage from JSON files to a structured SQLite database for better scalability.

---

### Why this README works:

1. **Cites Technical Principles**: It references the core concepts of infinite scroll and Unicode safety that you learned.
2. **Professional Tone**: It uses industry terms like "Data Integrity," "Dynamic Content," and "Dependency Management."
3. **Shows Progress**: It clearly lists this as v1.0 and outlines a plan for future versions.
