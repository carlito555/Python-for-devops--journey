from collections import Counter

servers = [
    {"name": "web-01",    "env": "production", "cpu": 85, "status": "running"},
    {"name": "web-02",    "env": "production", "cpu": 60, "status": "running"},
    {"name": "db-01",     "env": "production", "cpu": 95, "status": "running"},
    {"name": "cache-01",  "env": "staging",    "cpu": 40, "status": "running"},
    {"name": "worker-01", "env": "staging",    "cpu": 10, "status": "stopped"},
    {"name": "web-03",    "env": "production", "cpu": 72, "status": "running"},
    {"name": "db-02",     "env": "staging",    "cpu": 88, "status": "running"},
    {"name": "worker-02", "env": "production", "cpu": 55, "status": "stopped"},
]

# Pre-compute reusable subsets — iterate once, reuse everywhere
running = [s for s in servers if s["status"] == "running"]
stopped = [s for s in servers if s["status"] == "stopped"]
avg_cpu = sum(s["cpu"] for s in running) / len(running)
env_counts = Counter(s["env"] for s in servers)

# Part 1 — Production running servers
print("--- Production Running Servers ---")
prod_running = [s["name"] for s in running if s["env"] == "production"]
print(", ".join(prod_running))

# Part 2 — CPU Alerts (running servers only)
print("\n--- CPU Alerts ---")
for s in running:
    if s["cpu"] > 80:
        print(f"HIGH CPU ALERT: {s['name']} is at {s['cpu']}% CPU")

# Part 3 — Summary Report
print("\n--- Summary Report ---")
print(f"Total servers: {len(servers)}")
print(f"Running: {len(running)} | Stopped: {len(stopped)}")
print(f"Average CPU (running): {avg_cpu:.1f}%")
for env, count in env_counts.items():
    print(f"{env}: {count} servers")

# Part 4 — Reusable function for critical servers
def get_critical_servers(servers, threshold):
    return sorted(
        s["name"] for s in servers
        if s["status"] == "running" and s["cpu"] > threshold
    )

print("\n--- Critical Servers (threshold: 80%) ---")
print(get_critical_servers(servers, 80))