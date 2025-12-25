import requests
import os
import re

# GitHub username
USERNAME = "void0x11"
# GitHub Token (passed from GitHub Actions)
TOKEN = os.getenv("GITHUB_TOKEN")

def fetch_repositories(username, token):
    headers = {"Authorization": f"token {token}"} if token else {}
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/repos?per_page=100&page={page}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error fetching repos: {response.status_code}")
            break
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def fetch_language_stats(repos, token):
    headers = {"Authorization": f"token {token}"} if token else {}
    language_totals = {}
    
    for repo in repos:
        if repo["fork"]:
            continue
        
        lang_url = repo["languages_url"]
        response = requests.get(lang_url, headers=headers)
        if response.status_code == 200:
            languages = response.json()
            for lang, bytes_count in languages.items():
                language_totals[lang] = language_totals.get(lang, 0) + bytes_count
        else:
            print(f"Error fetching languages for {repo['name']}: {response.status_code}")
            
    return language_totals

def generate_stats_markdown(language_totals):
    total_bytes = sum(language_totals.values())
    if total_bytes == 0:
        return "No language data found."
    
    # Sort languages by bytes count
    sorted_languages = sorted(language_totals.items(), key=lambda x: x[1], reverse=True)
    
    lines = []
    lines.append("<table>")
    lines.append("  <tr>")
    lines.append("    <th align='left'>Language</th>")
    lines.append("    <th align='left'>Percentage</th>")
    lines.append("    <th align='left'>Bar Graph</th>")
    lines.append("  </tr>")
    
    for lang, bytes_count in sorted_languages:
        percentage = (bytes_count / total_bytes) * 100
        if percentage < 0.1: continue # Skip very small percentages
        
        # Simple bar graph using characters or HTML
        bar_length = int(percentage / 5) # 1 block per 5%
        bar = "█" * bar_length + "░" * (20 - bar_length)
        
        lines.append("  <tr>")
        lines.append(f"    <td><b>{lang}</b></td>")
        lines.append(f"    <td>{percentage:.1f}%</td>")
        lines.append(f"    <td><code>{bar}</code></td>")
        lines.append("  </tr>")
        
    lines.append("</table>")
    return "\n".join(lines)

def update_readme(stats_markdown):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    pattern = r"<!-- LANGUAGES_START -->.*?<!-- LANGUAGES_END -->"
    replacement = f"<!-- LANGUAGES_START -->\n{stats_markdown}\n<!-- LANGUAGES_END -->"
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    print("Fetching repositories...")
    repos = fetch_repositories(USERNAME, TOKEN)
    print(f"Found {len(repos)} repositories.")
    
    print("Fetching language stats...")
    language_totals = fetch_language_stats(repos, TOKEN)
    
    print("Generating markdown...")
    stats_md = generate_stats_markdown(language_totals)
    
    print("Updating README.md...")
    update_readme(stats_md)
    print("Done!")
