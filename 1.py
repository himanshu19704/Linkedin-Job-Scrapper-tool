import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as tb  # Modern UI for Tkinter
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import threading

# Function to fetch jobs (Runs in a separate thread)
def fetch_jobs():
    job_title = job_entry.get()
    location = location_entry.get()

    if not job_title or not location:
        messagebox.showwarning("Input Error", "Please enter both job title and location.")
        return

    status_label.config(text="Fetching jobs... Please wait.", foreground="blue")
    progress_bar.start()  # Start progress bar animation

    def scrape_data():
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        linkedin_url = f"https://www.linkedin.com/jobs/search/?keywords={job_title}&location={location}"
        driver.get(linkedin_url)
        time.sleep(5)

        try:
            count_element = driver.find_element(By.CLASS_NAME, 'results-context-header__job-count')
            count_text = count_element.text.replace(',', '').replace('+', '')
            count = int(count_text)
        except:
            count = 10  # Default value if count not found

        job_listings = driver.find_elements(By.CLASS_NAME, "base-search-card__info")
        jobs = []

        for job in job_listings[:count]:
            try:
                title = job.find_element(By.TAG_NAME, "h3").text
                company = job.find_element(By.CLASS_NAME, "hidden-nested-link").text
                job_location = job.find_element(By.CLASS_NAME, "job-search-card__location").text
                jobs.append([title, company, job_location])
            except:
                continue

        driver.quit()

        # Save to CSV
        df = pd.DataFrame(jobs, columns=['Job Title', 'Company', 'Location'])
        df.to_csv('data.csv', index=False)

        # Update UI
        progress_bar.stop()  # Stop progress animation
        status_label.config(text=f"Found {len(jobs)} jobs.", foreground="green")

        # Clear previous data
        for row in tree.get_children():
            tree.delete(row)

        # Insert new data
        for job in jobs:
            tree.insert("", "end", values=job)

    # Run scraping in a separate thread to avoid UI freezing
    threading.Thread(target=scrape_data, daemon=True).start()

# Setup Modern Themed GUI
root = tb.Window(themename="superhero")  # Change theme: "cosmo", "flatly", "superhero", etc.
root.title("LinkedIn Job Scraper")
root.geometry("700x500")
root.resizable(False, False)

frame = tb.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

tb.Label(frame, text="Job Title:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
job_entry = tb.Entry(frame, width=40)
job_entry.grid(row=0, column=1, pady=5, padx=10)

tb.Label(frame, text="Location:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", pady=5)
location_entry = tb.Entry(frame, width=40)
location_entry.grid(row=1, column=1, pady=5, padx=10)

search_button = tb.Button(frame, text="Search Jobs", bootstyle="primary", command=fetch_jobs)
search_button.grid(row=2, column=0, columnspan=2, pady=10)

status_label = tb.Label(frame, text="", font=("Arial", 10), foreground="gray")
status_label.grid(row=3, column=0, columnspan=2)

progress_bar = tb.Progressbar(frame, mode="indeterminate", length=200)
progress_bar.grid(row=4, column=0, columnspan=2, pady=5)

# Table for displaying jobs
columns = ("Job Title", "Company", "Location")
tree_frame = tb.Frame(root)
tree_frame.pack(fill="both", expand=True, padx=10, pady=10)

tree_scroll = tb.Scrollbar(tree_frame, orient="vertical")
tree_scroll.pack(side="right", fill="y")

tree = ttk.Treeview(tree_frame, columns=columns, show="headings", yscrollcommand=tree_scroll.set)
tree_scroll.config(command=tree.yview)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=200)

tree.pack(fill="both", expand=True)

root.mainloop()
