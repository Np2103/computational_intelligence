def bayes_probability():
    print("------------------\nBayes Theorem\n-------------------\n")
    A = input("Enter event A: ")
    B = input("Enter event B: ")

    p_B_given_A = float(input(f"Enter P({B} | {A}): "))
    p_A = float(input(f"Enter P({A}): "))
    p_B = float(input(f"Enter P({B}): "))


    if p_B == 0:
        print("Error: P(B) cannot be zero.")
        return


    p_A_given_B = round((p_B_given_A * p_A) / p_B,4)

    print(f"\nP({A} | {B}) = {p_A_given_B}")

bayes_probability()