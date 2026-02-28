magicians = ['alice', 'david', 'carolina', 'bob', 'eve'] 
for magician in magicians: 
    print(magician)  # Output: alice, david, carolina, bob, eve


magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

