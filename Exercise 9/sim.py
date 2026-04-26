import random
def coin_toss_probability():
    n = int(input("Enter no of coin tosses: "))
    heads = 0
    tails = 0
    for i in range(n):
        toss = random.choice(['H', 'T'])
        print(f"Toss Number {i+1}: {toss}")

        if toss == 'H':
            heads += 1
        else:
            tails += 1

    print("\nResults:")
    print("No. of Heads:", heads)
    print("No. of Tails:", tails)

    print("\n-------------------------\nProbability of tosses:\n-------------------------\n")
    print("P(H) =", heads / n)
    print("P(T) =", tails / n)
coin_toss_probability()