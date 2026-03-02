🚀 LinkedIn Job Scraper – Desktop Application

A modern desktop-based LinkedIn Job Scraper built using Python, Selenium and Tkinter.

This application allows users to search for jobs by title and location, scrape live job listings from LinkedIn, and export the results to a CSV file — all through a clean and responsive GUI.

📌 Features

✅ Search jobs by title and location
✅ Live web scraping using Selenium
✅ Modern GUI using ttkbootstrap
✅ Multi-threading (UI does not freeze during scraping)
✅ Displays results in an interactive table
✅ Automatically saves results to CSV (data.csv)
✅ Headless browser automation



🛠 Tech Stack

Python

Tkinter

ttkbootstrap (Modern UI styling)

Selenium WebDriver

ChromeDriver (webdriver-manager)

Pandas



🧠 Key Concepts Implemented

Headless browser automation

Dynamic web scraping

Structured data extraction

CSV file generation

Responsive desktop UI design



🖥️ How It Works

User enters:

Job Title

Location

Application launches a headless Chrome browser.

Selenium scrapes LinkedIn job results.

Extracted job details:

Job Title

Company

Location

Data is:

Displayed inside the GUI table

Saved automatically to data.csv



📂 Output

The scraped job data is saved in:

data.csv

Columns:

Job Title

Company

Location



▶️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/himanshu19704/Linkedin-Job-Scrapper-tool.git
2️⃣ Install Dependencies
pip install -r requirements.txt

If you don’t have requirements.txt, install manually:

pip install selenium pandas ttkbootstrap webdriver-manager
3️⃣ Run Application
python main.py



⚠️ Disclaimer

This project is developed for educational and demonstration purposes only.
LinkedIn's structure may change, which could affect scraping functionality.



📈 What I Learned

Real-world Selenium automation

GUI development with Python

Managing web drivers dynamically

Structured data storage

Creating user-friendly desktop applications



👨‍💻 Author

Developed by Himanshu
Passionate about Backend Development, Automation, and Full Stack Engineering.
