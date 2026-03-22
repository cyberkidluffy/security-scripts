log_file = "test_log.txt"

suspicious_keywords = ["FAILED", "ERROR", "UNAUTHORIZED", "DENIED"]

with open(log_file, "r") as file:
    for line in file:
        for keyword in suspicious_keywords:
            if keyword in line:
                print("ALERT:", line.strip())
                break