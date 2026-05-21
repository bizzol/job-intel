# greenhouse.py
# Mike Bell
# 05/21/2026

import requests
from datetime import datetime

from filters.scoring import score_job

GREENHOUSE_BOARDS = [
    "bishopfox",
    "praetorian",
    "coalfire",
    "netspi"
]

def fetch_greenhouse_jobs():
    jobs = []

    for board in GREENHOUSE_BOARDS:
        url = f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs"

        try:
            response = requests.get(url, timeout=15)
            data = response.json()

            for job in data.get("jobs", []):
                title = job.get("title", "")
                location = job.get("location", {}).get("name", "")
                absolute_url = job.get("absolute_url", "")

                combined_text = f"{title} {location}"

                jobs.append(
                    {
                        "title": title,
                        "company": board,
                        "location": location,
                        "url": absolute_url,
                        "source": "greenhouse",
                        "date_posted": "",
                        "discovered_at": datetime.utcnow().isoformat(),
                        "score": score_job(combined_text),
                        "description": combined_text
                    }
                )

        except Exception as error:
            print(f"Error with {board}: {error}")

    return jobs