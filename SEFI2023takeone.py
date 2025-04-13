import os
from bs4 import BeautifulSoup
import re
import csv

file_path = "Proceedings of 51st Annual Conference of European Society for Engineering Education.html"

with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Parameters
institution_keywords = ["university", "institute", "school", "college", "faculty", "polytechnic", "academy"]
banned_name_words = {"abstract", "introduction", "methodology", "references", "acknowledgments", "respondents", "context elements"}
MAX_INSTITUTION_WORDS = 12

def clean_text(text):
    # Remove emails and superscripts
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'\d+', '', text)
    return text.strip()

p_tags = soup.find_all("p")
presenters = set()
i = 0

while i < len(p_tags) - 1:
    name_raw = clean_text(p_tags[i].get_text(strip=True))
    inst_raw = clean_text(p_tags[i + 1].get_text(strip=True))

    # Filter: skip generic section titles
    if name_raw.lower() in banned_name_words:
        i += 1
        continue

    is_name_like = (
        len(name_raw.split()) <= 5 and
        any(c.isupper() for c in name_raw)
    )

    is_inst_like = (
        any(k in inst_raw.lower() for k in institution_keywords) and
        len(inst_raw.split()) <= MAX_INSTITUTION_WORDS
    )

    if is_name_like and is_inst_like:
        presenters.add((name_raw, inst_raw))
        i += 2
    else:
        i += 1

# Also scan for "Name, Institution" lines
for p in p_tags:
    text = clean_text(p.get_text(strip=True))
    if text.count(",") == 1:
        name_part, inst_part = map(str.strip, text.split(",", 1))
        if (
            name_part.lower() not in banned_name_words and
            len(name_part.split()) <= 5 and
            any(k in inst_part.lower() for k in institution_keywords) and
            len(inst_part.split()) <= MAX_INSTITUTION_WORDS
        ):
            presenters.add((name_part, inst_part))

# Output
with open("SEFI2023.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Presenter Name", "Institution"])
    writer.writerows(sorted(presenters))

print(f"✅ Finished! Extracted {len(presenters)} presenter-institution pairs.")
