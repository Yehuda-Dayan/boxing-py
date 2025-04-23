import random
options = ["jab", "cross", "uppercut", "hook", "livershot", "lowkick", "headkick", "bodykick", "knee", "elbow", "slip",
            "bobandweave", "parry", "catch", "block", "leg_sweep"]
print("Choose an option:")
print("1.", options[0])
print("2.", options[1])
print("3.", options[2])
print("4.", options[3])
print("5.", options[4])
print("6.", options[5])
print("7.", options[6])
print("8.", options[7])
print("9.", options[8])
print("10.", options[9])
print("11.", options[10])
print("12.", options[11])
print("13.", options[12])
print("14.", options[13])
print("you can chuse a single punch or kick or a combination of 3 punches and kicks")
user_input = input("Enter your choices (e.g. 1,3,5): ")
choices = user_input.split(",")  
selected = []

if "1" in choices:
    selected.append(options[0])
if "2" in choices:
    selected.append(options[1])
if "3" in choices:
    selected.append(options[2])
if "4" in choices:
    selected.append(options[3])
if "5" in choices:
    selected.append(options[4])
if "6" in choices:
    selected.append(options[5])
if "7" in choices:
    selected.append(options[6])
if "8" in choices:
    selected.append(options[7])
if "9" in choices:
    selected.append(options[8])
if "10" in choices:
    selected.append(options[9])
if "11" in choices:
    selected.append(options[10])
if "12" in choices:
    selected.append(options[11])
if "13" in choices:
    selected.append(options[12])
if "14" in choices:
    selected.append(options[13])

print("You selected:", selected)
shadow = random.sample(options, 3)
print("your shadow:", shadow) 

power = {
    "jab": 1,
    "cross": 2,
    "uppercut": 3,
    "hook": 2,
    "livershot": 3,
    "lowkick": 3,
    "headkick": 5,
    "bodykick": 3,
    "knee": 5,
    "elbow": 4,
    "slip": 2,
    "bobandweave": 2,
    "parry": 1,
    "catch": 1,
    "block": 1,
    "leg_sweep": 5
}

player_score = 0
shadow_score = 0

p1 = selected[0]
s1 = shadow[0]
print(f"\nRound 1: You → {p1} ({power[p1]}) vs Shadow → {s1} ({power[s1]})")
if power[p1] > power[s1]:
    print("You win this round! 🟢")
    player_score += 1
elif power[p1] < power[s1]:
    print("Shadow wins this round! 🔴")
    shadow_score += 1
else:
    print("Draw! ⚪")

p2 = selected[1]
s2 = shadow[1]
print(f"\nRound 2: You → {p2} ({power[p2]}) vs Shadow → {s2} ({power[s2]})")
if power[p2] > power[s2]:
    print("You win this round! 🟢")
    player_score += 1
elif power[p2] < power[s2]:
    print("Shadow wins this round! 🔴")
    shadow_score += 1
else:
    print("Draw! ⚪")


p3 = selected[2]
s3 = shadow[2]
print(f"\nRound 3: You → {p3} ({power[p3]}) vs Shadow → {s3} ({power[s3]})")
if power[p3] > power[s3]:
    print("You win this round! 🟢")
    player_score += 1
elif power[p3] < power[s3]:
    print("Shadow wins this round! 🔴")
    shadow_score += 1
else:
    print("Draw! ⚪")


print("\n--- Final Result ---")
print(f"You: {player_score} | Shadow: {shadow_score}")

if player_score > shadow_score:
    print("🏆 You WIN the fight!")
elif player_score < shadow_score:
    print("😮 Shadow WINS the fight!")
else:
    print("🤝 It's a DRAW!")