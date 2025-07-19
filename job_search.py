import requests
from bs4 import BeautifulSoup

def search_role(query, location="Bengaluru"):
    url = f"https://www.indeed.com/jobs?q={query.replace(' ', '+')}&l={location.replace(' ', '+')}&fromage=1&limit=25&remotejob=1"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    jobs = []
    for card in soup.select(".job_seen_beacon")[:10]:
        title = card.select_one("h2.jobTitle").text.strip()
        company = card.select_one("span.companyName").text.strip()
        link = "https://www.indeed.com" + card.select_one("a")["href"]
        jobs.append(f"{title} at {company}\n{link}")
    return jobs

def main():
    queries = ["junior qa engineer", "automation test engineer", "networking engineer"]
    results = []
    for q in queries:
        results += search_role(q, location="Bengaluru")
        results += search_role(q, location="Remote")
    with open("jobs.txt", "w", encoding="utf-8") as f:
        if results:
            f.write("\n\n".join(results))
        else:
            f.write("No new jobs found today.")

if __name__ == "__main__":
    main()
