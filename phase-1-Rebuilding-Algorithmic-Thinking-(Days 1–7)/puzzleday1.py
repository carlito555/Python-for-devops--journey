ports = [80, 443, 3306, 8080, 9090, 15, 22, 3000, 5000, 30]

for port in ports:
    if port % 3 == 0 and port % 5 == 0:
        print("Offline")
    elif port % 5 == 0:
        print("Throttled")
    elif port % 3 == 0:
        print("Maintenance")
    else:
        print(f"Active: {port}")