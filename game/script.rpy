# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# characters ##
### SudoCat ###
image sudocat faceleft normal = "images/characters/sudocat/sudocat-normal.png"
image sudocat faceleft normal tiltright = "images/characters/sudocat/sudocat-normal-tiltright.png"
image sudocat faceleft normal tiltleft = "images/characters/sudocat/sudocat-normal-tiltleft.png"
image sudocat faceleft eyesclosed normal = "images/characters/sudocat/sudocat-eyesclosed-normal.png"
image sudocat faceleft eyesclosed tiltleft = "images/characters/sudocat/sudocat-eyesclosed-normal-tiltleft.png "
image sudocat faceleft eyesclosed tiltright =  "images/characters/sudocat/sudocat-eyesclosed-normal-tiltright.png"

image sudocat faceright normal = "images/characters/sudocat/sudocat-rightfacing-normal.png"
image sudocat faceright normal tiltback = "images/characters/sudocat/sudocat-rightfacing-normal-tiltback.png"
image sudocat faceright normal tiltforward = "images/characters/sudocat/sudocat-rightfacing-normal-tiltforward.png"
image sudocat faceright eyesclosed normal = "images/characters/sudocat/sudocat-rightfacing-eyesclosed.png"
image sudocat faceright eyesclosed tiltdown = "images/characters/sudocat/sudocat-rightfacing-eyesclosed-tiltdown.png"

### BoxyBox ###
image boxybox faceright normal headup = "images/characters/boxybox/boxybox-normal-right-headup.png"
image boxybox faceright normal = "images/characters/boxybox/boxybox-normal-right.png"
image boxybox faceright lookdown = "images/characters/boxybox/boxybox-lookdown-right.png"

image boxybox faceleft normal headup = "images/characters/boxybox/boxybox-normal-left-headup.pngg"
image boxybox faceleft normal = "images/characters/boxybox/boxybox-normal-left.png"
image boxybox faceleft lookdown = "images/characters/boxybox/boxybox-lookdown-left.png"

### Greene ###
image greene faceright anxious = "images/characters/greene/doggy-anxious.png"
image greene faceright excited =  "images/characters/greene/doggy-excited.png"
image greene faceright smile = "images/characters/greene/doggy-smile.png"

# backgrounds ##
### art murmur mbackgrounds ###
image bg artmurmur cars = "images/backgrounds/artmurmur/cars.png"
image bg artmurmur crowd = "images/backgrounds/artmurmur/crowd.png"
image bg artmurmur gallery = "images/backgrounds/artmurmur/gallery.png"
image bg artmurmur sign = "images/backgrounds/artmurmur/sign.png"

image bg outdoors piano = "images/backgrounds/outdoors/piano.png"

### sudoroom backgrounds ###
image bg sudoroom 3dprinter = "images/backgrounds/sudoroom/3dprinterroom.jpg"
image bg sudoroom dark ="images/backgrounds/sudoroom/darksudoroom.jpg"
image bg sudoroom frontdoor ="images/backgrounds/sudoroom/frontdoor.jpg"

### mainroom backgrounds ###
image bg mainroom meeting = "images/backgrounds/mainroom/meeting.jpg"
image bg mainroom workshop = "images/backgrounds/mainroom/workshop3dprinting.png"

# Declare characters used by this game.
define m = Character('Me', color="#c8ffc8")
define s = Character('SudoCat', color="#c8ffc8")
define g = Character('Greene', color="#cccccc")
define b = Character('Boxy Box', color="#e5eeee")
define peeps = Character('SudoRoom People', color="#c8ffc8")

# The game starts here.
label start:
    
scene bg artmurmur cars 
with dissolve 

"Another Oakland Art Murmur, with booming bass cars, sticky fingered tacos, and beers sipped in paper bags"
  
scene bg artmurmur gallery
with dissolve

"You wander down the street passing by all the strutting peacocks, sexy ladies in their lovely mating dance. It's so hustling and bustling during the art mrumur!"
   
scene bg artmurmur crowd
with dissolve

"Still... something seems to be missing... some kind of purpose?"

scene bg artmurmur sign
with dissolve

m "SudoRoom? An afterparty? I wonder what that is."
m "What a weird little sign. Is this some kind of secret society?"

show sudocat faceright normal at left

s "Hey! Hey! Hey!"

show sudocat faceright normal tiltback at left

s "So you're interested in SudoRoom?" 

show sudocat faceright normal tiltforward at left

m "Sudo... What?"

show sudocat faceright normal at left
s "SudoRoom! The sign. See... it's a hackerspace. You're the only one of these people paying attention to that sign. That's what I call... a good sign!"
show sudocat faceright normal tiltforward at left
m "Yeah I was wondering what that is. What's a hackerspace?"
show sudocat faceright normal at left
s "What's a hackerspace? Well, that's actually both a simple and a complicated answer..."
show sudocat faceright normal tiltback at left
s "You really should drop by and see for yourself."
m "Oh, OK. But what is a hackerspace? I heard about them in the news. Aren't they places for people who hack into stuff? Steal government documents and credit cards?"
s "Wow! We have a lot to work on with you."


label end:
    
    

return
