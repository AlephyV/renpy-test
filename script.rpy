init python:
    class Reputation:
        def __init__(self):
            self.bro = 0
            self.boyfriend = 0
            self.troublemaker = 0

image loyal = im.Scale("images/loyal.png", 250, 250)
image popular = im.Scale("images/popular.png", 250, 250)
image confident = im.Scale("images/confident.png", 250, 250)

label start:
    $ reputation = Reputation()
    show screen loyalButton
    show screen popularButton
    show screen confidentButton
    "Buttons" "Click on me!"

screen loyalButton:
    imagebutton:
        xpos 200
        ypos 200
        idle "loyal"
        action [SetVariable("reputation.bro", "20"), SetVariable("reputation.boyfriend", "20"), SetVariable("reputation.troublemaker", "10"), MainMenu(False)]

screen popularButton:
    imagebutton:
        xpos 400
        ypos 200
        idle "popular"
        action [SetVariable("reputation.bro", "20"), SetVariable("reputation.boyfriend", "10"), SetVariable("reputation.troublemaker", "20"), MainMenu(False)]

screen confidentButton:
    imagebutton:
        xpos 600
        ypos 200
        idle "confident"
        action [SetVariable("reputation.bro", "10"), SetVariable("reputation.boyfriend", "20"), SetVariable("reputation.troublemaker", "20"), MainMenu(False)]
