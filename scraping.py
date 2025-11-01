# --- Import library ---
from google_play_scraper import reviews
import pandas as pd
from pathlib import Path
import csv
import os
from dotenv import load_dotenv

# --- Load file .env ---
load_dotenv()

# --- Ambil app id dan total dari env ---
app_id = os.getenv("APP_ID")
count = int(os.getenv("REVIEW_COUNT", "10000"))

# --- Fungsi Scraping ---
def scrape_reviews(app_id, count=10000):
    result, _ = reviews(
        app_id,
        lang='id',      # bikin bahasa indo
        country='id',   # bikin region indo
        count=count
    )
    return result

# --- Proses scraping ---
print(f"📥 Mengambil {count} review dari aplikasi {app_id} ...")
reviews_data = scrape_reviews(app_id, count=count)

# --- Buat DataFrame ---
df = pd.DataFrame(reviews_data)
print(f"📊 Total review terkumpul: {len(df)}")

# --- Simpan ke CSV ---
output_file = 'dataset_apk.csv'

df.to_csv(output_file, index=False, encoding='utf-8', quoting=csv.QUOTE_ALL, escapechar='\\')

print(f"✅ {len(df)} reviews berhasil disimpan ke {output_file}")
