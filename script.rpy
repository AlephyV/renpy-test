image background2:
    im.Scale("background2.png", 1100, 550)
    ypos 0.87

#icons
image loyal:
    im.Scale("images/loyal.png", 300, 300)
    xpos 250
    ypos 420

image popular:
    im.Scale("images/popular.png", 300, 300)
    xpos 650
    ypos 380

image confident:
    im.Scale("images/confident.png", 300, 300)
    xpos 1015
    ypos 380

#titles
image loyal title:
    Text("LOYAL", size=27, bold=True)
    xpos 255 ypos 447

image popular title:
    Text("POPULAR", size=27, bold=True)
    xpos 640 ypos 447

image confident title:
    Text("CONFIDENT", size=27, bold=True)
    xpos 1015 ypos 447

#descriptions
image loyal description:
    Text("I'm a loyal kinda guy, i like to be on my\n best behavior and i prefer to date one\n girl at a time.", size=13, text_align=0.5)
    xpos 255 ypos 517

image popular description:
    Text("I'm popular. People respond to my\n natural charisma. They all want to\n know me. They all want to be me.", size=13, text_align=0.5)
    xpos 640 ypos 517

image confident description:
    Text("I'm confident. I'm an alpha\n male. I do what i want,\n when i want.", size=14, text_align=0.5)
    xpos 1020 ypos 517

#hover buttons images
image pink button hover:
    im.Scale("images/pink_button_hover.png", 280, 75)
    xpos -15
    ypos -13

image yellow button hover:
    im.Scale("images/yellow_button_hover.png", 280, 75)
    xpos -15
    ypos -13

image blue button hover:
    im.Scale("images/blue_button_hover.png", 340, 140)
    xpos -45
    ypos -42

#screen buttons
screen pink_button:
    imagebutton:
        xpos 135
        ypos 540
        idle im.Scale("images/pink_button_idle.png", 250, 50)
        hover "pink button hover"
        #variables in variables.rpy
        action [SetVariable("reputations.bro", 20),SetVariable("reputations.boyfriend", 20),SetVariable("reputations.troublemaker", 10), MainMenu(False)]

screen yellow_button:
    imagebutton:
        xpos 515
        ypos 540
        idle im.Scale("images/yellow_button_idle.png", 250, 50)
        hover "yellow button hover"
        #variables in variables.rpy
        action [SetVariable("reputations.bro", 20),SetVariable("reputations.boyfriend", 10),SetVariable("reputations.troublemaker", 20), MainMenu(False)]

screen blue_button:
    imagebutton:
        xpos 890
        ypos 540
        idle im.Scale("images/blue_button_idle.png", 250, 50)
        hover "blue button hover"
        #variables in variables.rpy
        action [SetVariable("reputations.bro", 10),SetVariable("reputations.boyfriend", 20),SetVariable("reputations.troublemaker", 20), MainMenu(False)]

#labels
label start:
    scene background
    show background2
    call loyal
    call popular
    call confident
    $ ui.saybehavior()
    $ ui.interact()

label loyal:
    show loyal
    show loyal title as loyal_title
    show loyal description as loyal_description
    show screen pink_button

label popular:
    show popular
    show popular title as popular_title
    show popular description as popular_description
    show screen yellow_button

label confident:
    show confident
    show confident title as confident_title
    show confident description as confident_description
    show screen blue_button
