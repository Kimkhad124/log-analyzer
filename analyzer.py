def analyze_log(file):
    suspicious_keywords = ["failed", "error", "unauthorized", "attack"]

    with open(file, "r") as f:
        lines = f.readlines()

    print("\nSuspicious Log Entries:\n")

    for line in lines:
        for keyword in suspicious_keywords:
            if keyword in line.lower():
                print(line.strip())
                break

def main():
    file = input("Enter log file name: ")
    analyze_log(file)

if __name__ == "__main__":
