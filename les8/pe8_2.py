import random

dobbelEen = random.randrange(1, 6)
dobbelTwee = random.randrange(1, 6)

def monopolyworp(dobbelEen, dobbelTwee):
    if dobbelEen == dobbelTwee:
        print(str(dobbelEen)+","+str(dobbelTwee)+" (dubbbel)")
        dobbelEenWorpTwee = random.choice(range(6))
        dobbelTweeWorpTwee = random.choice(range(6))
        if dobbelEenWorpTwee == dobbelTweeWorpTwee:
            print(str(dobbelEenWorpTwee) + "," + str(dobbelTweeWorpTwee) + " (dubbbel)")
            dobbelEenWorpDrie = random.choice(range(6))
            dobbelTweeWorpDrie = random.choice(range(6))
            if dobbelEenWorpDrie == dobbelTweeWorpDrie:
                print("Ga naar de gevangenis")

            else:
                print(dobbelEenWorpDrie, dobbelTweeWorpDrie)
        else:
            print(dobbelEenWorpTwee, dobbelTweeWorpTwee)


    else:
        print(dobbelEen, dobbelTwee)
    return

monopolyworp(dobbelEen, dobbelTwee)

