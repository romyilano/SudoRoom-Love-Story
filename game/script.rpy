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
define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
label start:

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    return
