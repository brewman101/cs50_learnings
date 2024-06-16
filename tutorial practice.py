# Source: https://www.youtube.com/watch?v=JP7ITIXGpHk&t=3395s

# hard set name for testing loop
name = "     john smith    "

# request the name alternatively
# name=input("What's your name? ")
name=name.strip().title()
first, last=name.split(" ")
print(f"Hello, Agent {last}")

