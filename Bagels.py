import random
s = ''.join(random.sample('0123456789', 3))
for _ in range(10):
    g = input("Guess: ")
    if g == s: print("You win"); break
    h = ["Fermi" if g[i]==s[i] else "Pico" if g[i] in s else "" for i in range(3)]
    print(" ".join(h) if any(h) else "Bagels")
else:
    print("Number was", s)
