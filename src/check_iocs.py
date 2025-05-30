import os

# File paths
feeds_file = "../feeds/blacklisted_ips.txt"
log_file = "../logs/auth.log"
output_file = "../output/matched_iocs.txt"

# Load blacklisted IPs
with open(feeds_file, "r") as f:
    blacklisted_ips = set(line.strip() for line in f if line.strip())

# Read log and check for blacklisted IPs
matches = []

with open(log_file, "r") as f:
    for line in f:
        for ip in blacklisted_ips:
            if ip in line:
                matches.append(f"Match found: {ip} in log line: {line.strip()}")

# Write results to output
with open(output_file, "w") as f:
    if matches:
        for match in matches:
            f.write(match + "\n")
    else:
        f.write("No matches found.\n")

print("IOC check complete. Results saved to matched_iocs.txt")
