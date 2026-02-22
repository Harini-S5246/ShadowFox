justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Original Justice League:", justice_league)

num_members = len(justice_league)
print("\n1. Number of members:", num_members)

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\n2. After adding Batgirl and Nightwing:", justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\n3. Wonder Woman as leader (moved to front):", justice_league)

aquaman_index = justice_league.index("Aquaman")
flash_index = justice_league.index("Flash")
green_lantern_index = justice_league.index("Green Lantern")

justice_league.remove("Green Lantern")
justice_league.insert(flash_index, "Green Lantern")
print("\n4. After moving Green Lantern between Aquaman and Flash:", justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\n5. New Justice League team:", justice_league)

justice_league.sort()
print("\n6. Sorted alphabetically:", justice_league)

print("\nBONUS: New leader at index 0:", justice_league[0])