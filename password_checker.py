import re
import msvcrt

def get_password(prompt="Enter your password: "):
    print(prompt, end="", flush=True)
    password = ""

    while True:
        ch = msvcrt.getch()

        # Enter key
        if ch == b'\r':
            print()
            break

        # Backspace
        elif ch == b'\x08':
            if len(password) > 0:
                password = password[:-1]
                print('\b \b', end='', flush=True)

        # Normal keys
        else:
            try:
                char = ch.decode("utf-8")
                password += char
                print("*", end="", flush=True)
            except:
                pass

    return password


print("=== Password Strength Checker ===")

password = get_password()

score = 0
max_score = 5

# Length check
if len(password) >= 8:
    score += 1

# Uppercase check
if re.search(r"[A-Z]", password):
    score += 1

# Lowercase check
if re.search(r"[a-z]", password):
    score += 1

# Number check
if re.search(r"[0-9]", password):
    score += 1

# Special character check
if re.search(r"[@$!%*?&]", password):
    score += 1

# Percentage score
percentage = (score / max_score) * 100

# Strength result
if score <= 2:
    strength = "Weak ❌"
elif score <= 4:
    strength = "Medium ⚠️"
else:
    strength = "Strong ✅"

print("\nPassword Strength:", strength)
print("Security Score:", score, "/", max_score)
print("Protection Level:", str(int(percentage)) + "%")