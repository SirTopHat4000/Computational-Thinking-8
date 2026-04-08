# Section 1 - Your code
from utils import *
player_name = input("What is your name?    ")

set_background("capybara_sunset")

s1 = create_sprite("shrimpgotdunk", -200, 0)
s2 = create_sprite("lebron(1)", 150, -100)
s3 = create_sprite("kirmit with bottle", -280, -250)

s1.color("blue")
s2.color("red")
s3.color("magenta")
time.sleep(5)

s1.write("Where are we?",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
window.update()
time.sleep(1)

s2.write("we are dead \nmen we are in \nthe",font = ("Arial", 20, "normal"))
window.update
time.sleep(1)

s2.clear()
window.update
time.sleep(1)

s2.write("capybara \ndomain \nexpantion ",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s2.clear()
window.update()
time.sleep(1)

s1.write(f"I'm looking for {player_name}",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)
s1.clear()

s1.write("Have you seen HIM?",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s3.write("wheeee areee sommheresh in ze rinbow", font = ("arial", 20, "normal"))
######################################################################
# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()