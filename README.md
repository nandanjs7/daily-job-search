# Automated Daily Job Search

This GitHub Action searches for junior-level jobs (QA, Automation, Networking) in Bengaluru or remote and sends results via email every day at 7 AM IST.

## 📁 Files Included
- `job_search.py` — scrapes Indeed for fresh job listings.
- `send_email.py` — sends the result to your email.
- `.github/workflows/daily_jobs.yml` — automation scheduler.
- `jobs.txt` — generated daily.

## 🔒 Setup Instructions
1. Create a GitHub repo and push these files.
2. Go to `Settings > Secrets and variables > Actions` and add:
   - `EMAIL_USER`: your Gmail address
   - `EMAIL_PASS`: Gmail app password (required if 2FA is enabled)
   - `EMAIL_TO`: your destination email (`nandanjs2018@gmail.com`)
3. Done! Jobs will be emailed to you every morning.

## ✅ Notes
- Indeed blocks frequent scraping. This uses light requests with a user-agent.
- You can customize roles, locations, or add more job boards.

Happy job hunting! 🎯
