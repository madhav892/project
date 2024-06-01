import os
import random
import datetime

# Define start and end dates for the year 2024
start_date = datetime.datetime(2024, 1, 1)
end_date = datetime.datetime(2024, 12, 31)

days_range = (end_date - start_date).days + 1  # Ensure the last day is included
total_commits = 304  # Required number of commits

# Generate 304 commits, allowing multiple commits on some days
commit_days = [random.randint(0, days_range - 1) for _ in range(total_commits)]

for day_offset in commit_days:
    commit_date = start_date + datetime.timedelta(days=day_offset)
    formatted_date = commit_date.strftime('%Y-%m-%d %H:%M:%S')

    with open("file.txt", "a") as file:
        file.write(f"Commit on {formatted_date}\n")

    os.system('git add .')
    os.system(f'git commit --date="{formatted_date}" -m "Commit on {formatted_date}"')

# Push all commits at once
os.system("git push origin main")

print("✅ 304 commits created and pushed in 2024!")
