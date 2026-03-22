import requests

API_KEY = "1dd560d4ff9808817b9d41b5ec81dae768d439bc9b29539850242c5bc2b12f88ac213dfc66f649b3"

def check_ip(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {"Key": API_KEY, "Accept": "application/json"}
    params = {"ipAddress": ip, "maxAgeInDays": 90}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()["data"]

    print(f"\nIP Address : {data['ipAddress']}")
    print(f"Country    : {data['countryCode']}")
    print(f"Abuse Score: {data['abuseConfidenceScore']}%")
    print(f"Total Reports: {data['totalReports']}")

    if data["abuseConfidenceScore"] > 50:
        print("STATUS     : ⚠️  SUSPICIOUS — investigate this IP")
    elif data["abuseConfidenceScore"] > 0:
        print("STATUS     : ⚠️  LOW RISK — some reports exist")
    else:
        print("STATUS     : ✅  CLEAN — no reports found")

ip = input("Enter IP address to check: ")
check_ip(ip)