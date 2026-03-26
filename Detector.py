import re
import sys
from collections import defaultdict

# CLI input
if len(sys.argv) > 1:
    log_file = sys.argv[1]
else:
    log_file = "logs/sample.log"

failed_logins = defaultdict(int)
successful_logins = []
total_logins = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:

        ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
        if ip_match:
            ip = ip_match.group(1)
            total_logins[ip] += 1

        if "Failed password" in line:
            if ip_match:
                failed_logins[ip] += 1

        if "Accepted password" in line:
            user_match = re.search(r'user (\w+)', line)
            if ip_match and user_match:
                user = user_match.group(1)
                successful_logins.append((ip, user))

print("\n=== Threat Detection Report ===\n")

THRESHOLD = 3
TOTAL_THRESHOLD = 5

alerts = []

# High severity: brute force
for ip, count in failed_logins.items():
    if count >= THRESHOLD:
        alert = f"[HIGH] Brute force suspected from {ip} ({count} failed attempts)"
        print(alert)
        alerts.append(alert)

# Medium: suspicious login after failures
for ip, user in successful_logins:
    if failed_logins[ip] >= THRESHOLD:
        alert = f"[MEDIUM] Possible account compromise: {user} from {ip}"
        print(alert)
        alerts.append(alert)

# Medium: high activity IP
for ip, count in total_logins.items():
    if count >= TOTAL_THRESHOLD:
        alert = f"[MEDIUM] High activity from {ip} ({count} total attempts)"
        print(alert)
        alerts.append(alert)

# Save to file
with open("alerts.txt", "w") as output:
    output.write("=== Threat Detection Report ===\n\n")
    for alert in alerts:
        output.write(alert + "\n")   
