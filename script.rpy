image background2:
    im.Scale("background2.png", 1100, 550)
    ypos 0.87

image loyal:
    im.Scale("images/loyal.png", 300, 300)
    xpos 250
    ypos 420

image loyal title:
    Text("LOYAL", size=27, bold=True)
    xpos 255 ypos 447

image loyal description:
    Text("I'm a loyal kinda guy, i like to be on my\n best behavior and i prefer to date one\n girl at a time", size=13, text_align=0.5)
    xpos 255 ypos 517

image pink button idle:
    im.Scale("images/pink_button_idle.png", 250, 50)

image pink button hover:
    im.Scale("images/pink_button_hover.png", 250, 50)

label start:
    scene background
    show background2
    call screen pink_button

label loyal:
    show loyal
    show loyal title as title
    show loyal description as description
    show screen pink_button

screen pink_button:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        ypos 0.5
        xpos 0.5
        idle "pink_button_idle.png"
        hover "pink_button_hover.png"
