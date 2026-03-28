import datetime

# ---------------- CHECK URL FUNCTION ----------------
def check_url(url):
    score = 0
    reasons = []

    suspicious_keywords = ["login", "verify", "bank", "secure", "update"]

    url_lower = url.lower()

    for word in suspicious_keywords:
        if word in url_lower:
            score += 1
            reasons.append(f"Contains suspicious keyword: {word}")

    if "@" in url:
        score += 2
        reasons.append("Contains @ symbol (possible redirection)")

    if len(url) > 50:
        score += 1
        reasons.append("URL is unusually long")

    return score, reasons


# ---------------- LOG FUNCTION ----------------
def log_results(url, score, risk_level):
    now = datetime.datetime.now()
    time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")

    log_line = f"[{time_stamp}] | Score: {score} | {risk_level} | {url}\n"

    with open("phishing_log.txt", "a", encoding="utf-8") as file:
        file.write(log_line)


# ---------------- MAIN PROGRAM ----------------
url = input("Enter URL to check: ")

score, reasons = check_url(url)

print("\n----- RESULT -----")
print("Score:", score)

if score >= 4:
    risk_level = "HIGH RISK - Likely Phishing"
elif score >= 2:
    risk_level = "MEDIUM RISK - Be Careful"
else:
    risk_level = "LOW RISK - Seems Safe"

print("Risk Level:", risk_level)

if reasons:
    print("\nReasons:")
    for reason in reasons:
        print("-", reason)
else:
    print("\nNo suspicious indicators found.")

# Save result to log file
log_results(url, score, risk_level)

print("\nResult saved to phishing_log.txt")
