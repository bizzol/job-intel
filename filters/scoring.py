# scoring.py
# Mike Bell
# 05/21/2026

KEYWORDS = [
    "penetration",
    "pentest",
    "security analyst",
    "red team",
    "vulnerability",
    "product security",
    "embedded security",
    "firmware security",
    "application security",
    "offensive security",
    "cybersecurity",
    "junior",
    "soc analyst"
]

STRONG_KEYWORDS = [
    "security engineer",
    "threat",
    "detection",
    "incident response",
    "siem",
    "blue team",
    "security operations",
    "application security",
    "cloud security",
    "devsecops",
    "adversary",
    "malware",
    "dfir",
    "forensics",
    "network security",
    "iam",
    "identity",
    "scada"
]
    
LOW_COMPETITION_KEYWORDS = [
    "hybrid",
    "clearance",
    "embedded",
    "firmware",
    "manufacturing",
    "ICS",
    "OT"
]

NEGATIVE_KEYWORDS = [
    "principal",
    "director",
    "manager",
    "staff engineer",
    "senior director",
    "vp",
    "chief"
]

def score_job(job_text):
    score = 0

    text = job_text.lower()

    for keyword in KEYWORDS:
        if keyword in text:
            score += 10

    for keyword in LOW_COMPETITION_KEYWORDS:
        if keyword.lower() in text:
            score += 15

    for keyword in STRONG_KEYWORDS:
        if keyword.lower() in text:
            score += 20
            
    for keyword in NEGATIVE_KEYWORDS:
        if keyword in text:
            score -= 25
            
    return score