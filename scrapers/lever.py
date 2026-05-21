# lever.py
# Mike Bell
# 05/21/2026

import requests

from datetime import datetime
from filters.scoring import score_job

LEVER_COMPANIES = [
    "netskope",
    "snyk",
    "chainguard",
    "huntress"
]

def fetch_lever_jobs():
    jobs = []

    for company in LEVER_COMPANIES:

        url = f"https://api.lever.co/v0/postings/{company}?mode=json"

        try:
            response = requests.get(url, timeout=15)
            if response.status_code != 200:
                print(f"Bad response from {company}: {response.status_code}")
                continue
            try:
                data = response.json()
            except Exception as error:
                print(f"Invalid JSON from {company}: {error}")
                continue
            #print(type(data))
            #print(data)

            #for job in data:
            for job in data.get("data",[]):

                title = job.get("text", "")
                location = job.get("categories", {}).get("location", "")
                description = job.get("descriptionPlain", "")
                apply_url = job.get("hostedUrl", "")

                combined_text = f"{title} {location} {description}"

                jobs.append(
                    {
                        "title": title,
                        "company": company,
                        "location": location,
                        "url": apply_url,
                        "source": "lever",
                        "date_posted": "",
                        "discovered_at": datetime.utcnow().isoformat(),
                        "score": score_job(combined_text),
                        "description": combined_text
                    }
                )

        except Exception as error:
            print(f"Lever error for {company}: {error}")

    return jobs