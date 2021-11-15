# Name: Blake Mann
# PSID: 1832387
# 12.7

def get_age():
    age = int(input())
    if 18<= age <= 75:
        return age
    raise ValueError("Invalid age.")

def fat_burning_heart_rate(age):
    return (220-age)*.7

if __name__ == "__main__":
    try:
        age = get_age()
        print("Fat burning heart rate for a", age,"year-old:", fat_burning_heart_rate(age),"bpm")
    except ValueError as a:
        print(a)
        print("Could not calculate heart rate info.\n")