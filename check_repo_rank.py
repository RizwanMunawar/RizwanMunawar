import requests
import re

# Repository details
repo_owner = "ultralytics"
repo_name = "ultralytics"
your_username = "RizwanMunawar"  # https://github.com/RizwanMunawar/
github_api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contributors"

# Fetch contributors data
headers = {"Authorization": f"token {YOUR_GITHUB_TOKEN}"}
response = requests.get(github_api_url, headers=headers)

if response.status_code != 200:
    raise Exception("Failed to fetch contributors data")

# Parse contributors to find your rank
contributors = response.json()
your_rank = None # initialize rank
your_contributions = 0

for index, contributor in enumerate(contributors):
    if contributor['login'] == your_username:
        your_rank = index + 1
        your_contributions = contributor['contributions']
        break

if your_rank is None:
    raise ValueError("Your username was not found in the contributors list.")

# Step 2: Generate a Shields.io URL for the badge
badge_url = f"https://img.shields.io/badge/Your_Rank-{your_rank}_({your_contributions}_contributions)-brightgreen"

# Step 3: Update README.md
with open("README.md", "r") as file:
    content = file.read()

# Replace the badge URL using regex to find and replace the previous rank badge
new_content = re.sub(
    r"!\[Your Rank\]\(https://img\.shields\.io/badge/Your_Rank-[\w\d_\(\)]+-brightgreen\)",
    f"![Your Rank]({badge_url})",
    content
)

with open("README.md", "w") as file:
    file.write(new_content)

print("Updated your rank badge in README.md")
