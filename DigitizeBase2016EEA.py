import requests
from bs4 import BeautifulSoup
import csv

url = "https://editorialexpress.com/conference/EEAESEM2016/program/EEAESEM2016.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

presenters = []
names_seen = set()

# Loop through all left-aligned table cells
for td in soup.find_all("td", align="left"):
    text = td.get_text(strip=True)

    # Skip any line that contains "session chair:"
    if "session chair:" in text.lower():
        continue

    # Only extract if it says "presented by:"
    if "presented by:" in text.lower():
        # Remove the prefix
        text = text.replace("presented by:", "").replace("Presented by:", "").strip()

        # Expect a comma between name and institution
        if ',' not in text:
            continue  # Malformed row

        name_part, institution = map(str.strip, text.split(",", 1))

        # Validate the name and remove duplicates
        if len(name_part.split()) >= 2 and name_part not in names_seen:
            presenters.append([name_part, institution])
            names_seen.add(name_part)

# Write to CSV
with open("EEAESEM2016_clean_presenters.csv", mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Presenter Name", "Institution"])
    writer.writerows(presenters)

print(f"✅ Done! Scraped {len(presenters)} unique presenter entries (excluding session chairs).")
