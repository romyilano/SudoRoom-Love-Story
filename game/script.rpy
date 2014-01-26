# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# characters ##
### SudoCat ###
image sudocat faceleft normal = "images/characters/sudocat/sudocat-normal.png"
image sudocat faceleft normal tiltright = "images/characters/sudocat/sudocat-normal-tiltright.png"
image sudocat faceleft normal tiltleft = "images/characters/sudocat/sudocat-normal-tiltleft.png"
image sudocat faceleft eyesclosed normal = "images/characters/sudocat/sudocat-eyesclosed-normal.png"
image sudocat faceleft eyesclosed tiltleft = "images/characters/sudocat/sudocat-eyesclosed-normal-tiltleft.png"
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

image boxybox faceleft normal headup = "images/characters/boxybox/boxybox-normal-left-headup.png"
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
    
    # game variables
    $ hackertype = "generic"          # What kind of hacker?
    $ has_dreams = True               # Does character have dreams or not?
    $ first_time = True               # set to True after first visit to SudoRoom
    $ tour_first_time = True          # set for the Tour
    
    scene bg artmurmur cars 
    with dissolve 
    
    play music "assets/audio/crowd-drums.wav"

    "Another Oakland Art Murmur, with booming bass cars, sticky fingered tacos, and beers sipped in paper bags"
    "It's gorgeous out."
      
    scene bg artmurmur gallery
    with dissolve

    "You wander down the street passing by all the strutting peacocks, sexy ladies in their lovely mating dance. It's so hustling and bustling during the art mrumur!"

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

    m "Sudo... What is that?"

    show sudocat faceright normal at left
    s "SudoRoom! The sign. It's a hackerspace."
       
    menu:
        "What's a hackerspace?":
            
            jump starthackerspace
            
        "Hackers... aren't those people that break into things?":
        
            jump startbadhackers
            

label startbadhackers:
    scene bg artmurmur sign
    
    show sudocat faceleft eyesclosed tiltleft at left
    
    s "..."

    show sudocat faceright normal tiltforward at left
    s "Many people have very bad impressions of hackers. It's actually very complicated."
    
    menu:
        "I see all these bad reports about hackers on the news":
            s "And you believe everything that's on the news?"
            menu:
                "Yes":
                    s "Then you have a lot to learn!"
                    m "I was just kidding!"
                "No":
                    s "Good. That means you're not clueless."
        "Aren't those supernerds?":
            s "Why everyone's a nerd in their own special way. Maybe you have an inner nerd just dying to get out."
    
    show sudocat faceleft eyesclosed tiltright at left
    s "Hackers can be either for the forces of good... white hat hackers or bad... black hat hackers. Or sometimes they just like to prank for fun."
    s "A lot of what you hear on media about hackers is unnecessary and comes from media glorification."
    
    menu: 
        "What's a white hat hacker? A black hat hacker?":
            $ first_question = "hackertype"
            s "White hat hackers are ethical hackers. They use their powers to make the world a better place, rather than to steal things from people."
            m "And black hat hackers do the opposite?"
            s "Sometimes there's gray too.. say a hacker discovers a big security flaw in a bank. They break into the system, but not to steal anything. They just want to show the flaw."
        "Why does the media exaggerate?":
            $ first_question = "media"
            s "They exaggerate for all the same reasons anyone does. Complex topics are tough to boil down for the general public, and you get more ratings when you're sensational.s"
    
    if first_question == "media":
            s "Then there are so many differences between hackers. There are black hat and white hats..."
            s "White hat hackers are ethical hackers. They use their powers to make the world a better place, rather than to steal things from people."
            m "And black hat hackers do the opposite?"
            s "Sometimes there's gray too.. say a hacker discovers a big security flaw in a bank. They break into the system, but not to steal anything. They just want to show the flaw."
    
label starthackerspace:
    scene bg artmurmur sign
        
    show sudocat faceleft eyesclosed tiltleft at left
    m "And just what is a hackerspace, anyway?"
    show sudocat faceright normal tiltforward at left
    show sudocat faceright normal at left
    s "Hackerspaces are community-oriented physical places where people can meet and work on their projects"
    s "The term hackerspace is confusing, because it can mean many things to many people."
    s "The term hackerspace actually flexible and open-ended. It can be an artist's studio, it can be a sewing lab, it can be a biochemistry room, it can be ane ducational center..."
    
    m "So can someone who doesn't code be a hacker?"
    
    s "I believe so. Some people say that a hacker is an expert or enthusiast of any kind. You could be an astronomy hacker or an embroidery hacker."
    
    show sudocat faceright normal tiltback at left
    
    menu:
        "Dreams? I don't have any dreams.":
            $ has_dreams = False
        "How can SudoRoom help me build my dreams?":
            $ has_dreams = True
            
    if has_dreams:
        s "SudoRoom gives you a place to connect with other people and make your dreams real."
        show sudocat faceright normal at left
        s "There's also the equipment you need to build what you want. People share tools at SudoRoom..."
        show sudocat faceright normal tiltback at left
        s "And not only tools, they share their ideas and passions."
        show sudocat faceright normal at left
    else:
        s "If you don't have a dream, maybe you will find what you want there!"
        s "You can even find out what you want playing with the different making tools. It's such a relief instead of actually having to buy stuff all for yourself."
        m "But I'm not creative."
        s "Don't be silly. Everyone's creative. The act of living is one of creativity."
    
    s "There are so many different, interesting groups of people at SudoRoom. You'd be amazed at how your ideas can grow and change once you're there!"
    s "We have political groups like the Community Democracy Project, which helps concerned citizens better track what tax money is being spent on. It'sl ike a pun krock approach to democracy."
    s "There's a SudoMesh network, which is working to decentralize wifi and provide free internet connections, homegrown to everyday folks in Oakland."
    s "And even beyond SudoRoom... we're intimately connected to various worker's collectives and spaces throughout the Bay Area and beyond. We're thinking about unique ways to  d"
    s "I think it's the perfect place for you. Why don't you go around the corner? It's right on 22nd between Telegraph and Broadway. Boxy Box is there waiting for you."

    scene bg artmurmur crowd
    with dissolve
    
    "What a crazy furry cat! SudoRoom... hackerspaces..."
    
    if has_dreams:
        "Why would anyone care about my dreams?"
    else:
        "And why would this cat think I have any dreams anyway?"
        
    stop music
        
label sudoorganscene:
    
    scene bg outdoors piano
    play music "assets/audio/organ-loop.wav"
    
    "A curious character playing the organ, and more mysterious SudoRoom signs...and then:"
   
    show boxybox faceleft normal headup at right
    b "Why hello! I'm Boxy Box and this is Samz here playing the organ."
    show boxybox faceleft lookdown at right
    m "I was sent here by SudoCat. He was dancing on the street with a sign at the Art Murmur"
    show boxybox faceleft normal headup at right
    b "So I've heard."
    show boxybox faceleft lookdown at right
    m "What do I do next? I mean is SudoRoom open to people who aren't members or something? I am a total outsider."
    show boxybox faceleft normal headup at right
    b "Why yes. We are open to everyone, even nonmembers.  And our membership is free and open to everyone as well. We seek to be inclusive. We have dues, but they're on a sliding scale"
    m "Very weird. I'm not used to this."
    b "Let's go upstairs."
    
    stop music
    
label sudoroommainroom:
    
    scene bg sudoroom frontdoor
    with dissolve
    show boxybox faceleft normal headup at left
    
    if first_time:
        b "Welcome to the SudoRoom! Let me give you a tour."
        $ first_time = False
        jump tour
    else:
        b "What would you like to do?"
        menu:
            "Take a tour of SudoRoom again":
                jump tour
            "Learn how to use different parts of SudoRoom":
                jump tutorial
            "It's time to party!":
                jump party
    
label tour:
    scene bg sudoroom frontdoor
    show boxybox faceleft normal headup at right
    # boxybox gives a tour of the different areas of the SudoRoom
    
    scene bg mainroom workshop
    show boxybox faceright lookdown at right
    
    if tour_first_time:
        s "That's the SudoRoom itself. It was founded by a group of idealistic folks on a shoestring budget off the skin of their teeth"
        $ tour_first_time = False
        b "Turning around, you see our big common room. We share this main room with various other groups such as the Public School."
        b "You can see Maxximus teaching a 3D printing class right now"
        peeps "Hey! Welcome to SudoRoom!"
        m "Hi!"
        b "We have lectures here, talks, movie showings and even dance performances. I think there are even raves here sometimes."
        b "Our weekly meetings are held here. You can attend any which one, they're Wednesdays."
        peeps "Come by after the art murmur. We're having a big monster bash to celebrate and raise funds to save the space."
        b "In just a few hours this room is going to be completely transformed!"
    else:
        b "Let's take a whirl around this place again."
        b "As you see this is the main room. Meetings, films, you name it."
        
    scene bg sudoroom 3dprinter
    show boxybox faceleft normal headup at right
    
    b "Welcome to the SudoRoom itself! In this room are contained the wonders of life."
    b "You have 3D printers, electronics tools, a woodshop, a recording studio, a biohacking lab... and more!"
    b "And of course there are the books.. we have so, so many interesting books."
    
    jump sudoroommainroom

label tutorial:
    
    scene bg sudoroom 3dprinter
    show boxybox faceleft normal headup at right
    
    b "What would you like to learn?"
    
    menu:
        "3D Printing? What is that?":
            jump tutorial_3DPrinter
        "So I can get involved in the community and social movements too? It's just just tech? How?":
            jump tutorial_activism
        "Biohacking? What's that?":
            jump tutorial_biohacking
        "I love bicycles. Anything I can do to rig my bike?":
            jump tutorial_bikes


label tutorial_3DPrinter:
    # show how to use the 3D Printer
    
    menu:
        "I want to learn more stuff aout the SudoRoom!":
            jump tutorial
            
label tutorial_activism:
    # show how to use the 3D Printer
    
    menu:
        "I want to learn more stuff aout the SudoRoom!":
            jump tutorial
            
label tutorial_biohacking:
    # biohacking oerview
    
    menu:
        "I want to learn more stuff aout the SudoRoom!":
            jump tutorial

label tutorial_bikes:
    # talk about different bikes and the bike taxi union
    
    menu:
        "I want to learn more stuff aout the SudoRoom!":
            jump tutorial
           
label party:
    # start the sudoroom party
    # give an option to do the tutorial again
          
    menu:
        "I want to learn more stuff aout the SudoRoom!":
            jump tutorial
label end:
    
    m "And so begins an adventure..."
    s "And a love affair!"
    b "Let's change the world!"
    

return
