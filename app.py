# app.py
# Mike Bell
# 05/21/2026

from database.db import initialize_database
from database.db import insert_job
from database.db import job_exists

from scrapers.greenhouse import fetch_greenhouse_jobs
from scrapers.lever import fetch_lever_jobs

MINIMUM_SCORE = 20

def main():

    initialize_database()
    source_counts = {}
    duplicate_count = 0
    low_score_count = 0
    
    scrapers = [
        fetch_greenhouse_jobs,
        fetch_lever_jobs
    ]

    jobs = []

    filtered_jobs = []

    # Collect jobs from all scrapers
    for scraper in scrapers:

        try:
            jobs.extend(scraper())

        except Exception as error:
            print(f"Scraper failure: {error}")

    print(f"\nFound {len(jobs)} total jobs")

    # Process jobs
    for job in jobs:

        source = job["source"]

        if source not in source_counts:
            source_counts[source] = 0

        source_counts[source] += 1

        # Skip duplicates
        if job_exists(job["url"]):
            duplicate_count += 1
            continue

        # Skip low scoring jobs
        if job["score"] < MINIMUM_SCORE:
            low_score_count += 1
            continue

        insert_job(job)

        filtered_jobs.append(job)

    print("\nJobs by source:")

    for source, count in source_counts.items():
        print(f"{source}: {count}")

    print(f"\nStored {len(filtered_jobs)} high-value jobs")
    print(f"\nDuplicates skipped: {duplicate_count}")
    print(f"\nLow-score jobs skipped: {low_score_count}")

    # Display jobs
    for job in filtered_jobs:

        print("-" * 50)
        print(job["title"])
        print(job["company"])
        print(job["location"])
        print(job["url"])
        print(f"Score: {job['score']}")


if __name__ == "__main__":
    main()