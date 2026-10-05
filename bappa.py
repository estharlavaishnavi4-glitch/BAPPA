import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("#FFF3E0")
screen.title("Cute Bappa ❤️ Ganpati Bappa Morya")

t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.hideturtle()

# ---------- Helper Functions ----------
def filled_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color("black", color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def ellipse(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color("black", color)
    t.begin_fill()
    for _ in range(2):
        t.circle(width, 90)
        t.circle(height, 90)
    t.end_fill()

# ---------- Body ----------
filled_circle(0, -80, 125, "#F4A261")

# ---------- Head ----------
filled_circle(0, 80, 105, "#F6B26B")

# ---------- Big Ears ----------
ellipse(-110, 75, 55, 30, "#F4A261")
ellipse(110, 75, 55, 30, "#F4A261")

# Inner ears
ellipse(-108, 75, 35, 18, "#FFD6A5")
ellipse(108, 75, 35, 18, "#FFD6A5")

# ---------- Crown ----------
t.penup()
t.goto(-65, 160)
t.pendown()
t.color("#B8860B", "#FFD700")
t.begin_fill()

points = [
    (-65, 160), (-40, 210), (-15, 175),
    (0, 220), (15, 175), (40, 210),
    (65, 160), (50, 145), (-50, 145)
]

for p in points:
    t.goto(p)

t.goto(-65, 160)
t.end_fill()

# Crown jewel
filled_circle(0, 190, 10, "#FF4D6D")

# ---------- Eyes ----------
filled_circle(-38, 105, 13, "white")
filled_circle(38, 105, 13, "white")

filled_circle(-38, 105, 6, "black")
filled_circle(38, 105, 6, "black")

# Cute eyebrows
t.penup()
t.goto(-52, 128)
t.setheading(15)
t.pendown()
t.forward(25)

t.penup()
t.goto(52, 135)
t.setheading(165)
t.pendown()
t.forward(25)

# ---------- Tilak ----------
t.penup()
t.goto(0, 140)
t.setheading(90)
t.color("#D62828")
t.pensize(5)
t.pendown()
t.forward(18)

# ---------- Trunk ----------
t.penup()
t.goto(0, 75)
t.setheading(-90)
t.color("black", "#F4A261")
t.begin_fill()

t.pendown()
t.forward(55)
t.right(35)
t.forward(35)
t.right(45)
t.forward(35)

# Curl trunk upward
t.right(70)
t.forward(30)
t.right(70)
t.forward(25)

t.end_fill()

# ---------- Smile ----------
t.penup()
t.goto(-25, 65)
t.setheading(-40)
t.pensize(3)
t.pendown()
t.color("#8B4513")
t.circle(30, 80)

# ---------- Modak ----------
filled_circle(-135, -135, 25, "#F4C95D")

t.penup()
t.goto(-150, -115)
t.pendown()
t.color("#B8860B")
t.goto(-140, -95)
t.goto(-125, -115)

# ---------- Right Hand ----------
filled_circle(105, -35, 38, "#F4A261")

# Fingers
for angle in [20, 40, 60]:
    t.penup()
    t.goto(110, -15)
    t.setheading(angle)
    t.pendown()
    t.forward(20)

# ---------- Left Hand ----------
filled_circle(-105, -35, 38, "#F4A261")

# ---------- Feet ----------
ellipse(-55, -185, 35, 20, "#F4A261")
ellipse(55, -185, 35, 20, "#F4A261")

# ---------- Necklace ----------
t.penup()
t.goto(-45, -5)
t.setheading(-60)
t.pensize(6)
t.color("#FFD700")
t.pendown()
t.circle(55, 120)

# Necklace beads
for x in [-35, -18, 0, 18, 35]:
    filled_circle(x, -38, 5, "#FFD700")

# ---------- Decorative Hearts ----------
def heart(x, y, size):
    t.penup()
    t.goto(x, y)
    t.color("#FF4D6D")
    t.pendown()

    t.begin_fill()
    t.left(50)
    t.forward(size)
    t.circle(size * 0.35, 200)
    t.right(140)
    t.circle(size * 0.35, 200)
    t.forward(size)
    t.end_fill()

heart(-190, 180, 18)
heart(175, 165, 15)
heart(-190, -40, 14)
heart(175, -50, 14)

# ---------- Message ----------
t.penup()
t.goto(0, -270)
t.color("#D35400")
t.write(
    "Ganpati Bappa Morya ❤️",
    align="center",
    font=("Arial", 22, "bold")
)

screen.mainloop()
