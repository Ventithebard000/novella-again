






init:
    python:
        def max_points(*values):
            return [ i for i, v in enumerate(values) if v == max(values) ]
    $ quiz_score = 0


define s = Character(" ")
define p = Character("[povname]")
define a = Character(" ", what_color="ffffff")
define m = Character(" ", what_color="f60609")
define b = Character("Shin", what_font="cabinvariable.ttf", what_color="ffffff", window_background="textboxnew.png")
define w = Character("???", what_font="cabinvariable.ttf", what_color="ffffff", window_background="textboxnew.png")
define c = Character("Sou", what_font="cabinvariable.ttf", what_color="ffffff", window_background="textboxnew.png")
define pov = Character(" ", what_font="cabinvariable.ttf", what_color="ffffff", window_background="textboxnew.png")



label start:





    $ points = 50
    $ quiz_score = 0
    $ name_list = ["sou", "hiyori", "sou hiyori", "hiyori sou", "SOU", "HIORI", "HIYORI SOU", "SOU HIYORI"]





    play music tansaku3 fadein 2
    scene bg black
    pause(2.0)



    a "> While the rest of the group is exploring the floor, you decide to risk it and stay behind."

    a "> You've noticed this room in the corner of the corridor a while ago, and yet others prefered to ignore it for some reason."

    a "> Maybe it's not a bad idea to go inside and search through it while others are gone."

    a "> You slow down your steps and then turn back completely."

    a "> Fortunately, the door isn't locked."

    scene bg monitor room
    with dissolve

    a "> . . . ."

    a "> At first, you don't see anything of interest. Or dangerous, at least."

    a "> The room has a bunch of screens and keyboards, and lots of other technical equipment."

    a "> Seems like it's a Floormaster's room."

    a "> Maybe you could just hack the system... But that's a bold claim. "

    a "> It's probably going to take more than just a password."

    a "> You decide to search the room thoroughly before the others found you. You don't have that much time."

    scene bg monitor room 1
    with hpunch

    play sound computer

    a "> . . . ?"

    a "> Hm?"

    stop music fadeout 2

    a "> The screen is.. on?"

    a "Look at it?"

    menu:
        "> Yes":


            a "> You approach the screen carefully."

            "'Ah, no, you're not... Who are you? You shouldn't be here...'"

            a "> It's seems that the voice is coming from the working screen."

            scene mon red
            with dissolve

            a "> When you lean towards the screen, you don't expect to see a face."

            play sound computer
            scene mon shin
            with hpunch
            pause (1.0)



            "'P-please, leave this room... You'll be in trouble! If you leave right now I won't tell anybody, I promise.'"
        "> No":

            a "> You decide to mind your business. It could be a trap."

            a "> When you're done exploring the room without touching anything, you get ready to leave."

            a "> But then... you hear a voice."

            scene mon red
            with dissolve
            pause (0.5)

            play sound computer
            scene mon shin
            with hpunch
            pause (1.0)



            "'Um... Hiyori-kun, is that you?'"

    menu:
        "> Is this a trap?":
            a "> You pull a chair closer to the working monitor to take a seat."

            a "> You've already seen the AIs before, and it probably wouldn't hurt you in any way. At least, too hard."

            "'I... I don't understand what you're talking about...'"

            "'This room could be dangerous, b-but that's not because of me...'"

            "'I mean, I would gladly help if anything happened... I can do that!'"

            "'Ah! I mean! It's not like something is going to happen..!'"

            jump who
        "> Who are you?":

            jump who


    label who:

    scene bg neutral
    with dissolve

    show neutral1
    with dissolve

    stop music fadeout 1
    play music denpa

    "'I'm.. I'm just a normal person... AI, i mean... Are you a friend of Hiyori's?'"

    "'He told me that someone might come but... I didn't think it would be just one person.'"

    hide neutral1
    show sad2

    "'Maybe.. something happened...'"

    "'If you're not the only one, you should go back to the others... Being alone here is very dangerous...'"

    menu:
        "> That's very nice of you":
            $ points += 1
            show bg love with dissolve

            hide sad2
            show shock1
            "'Nice? W-why... You don't have to...'"

            "'I just... I just want to help... I am against violence.'"

            "'I really can't tell you much, but I won't hurt you...'"
        "> Was someone here before me?":




            $ points += 0

            show bg neutral with dissolve

            hide sad2
            show neutral1

            "'No, not at all...'"

            "'Nobody was there... before you...'"

            "'Honestly, I've been alone for so long that I...'"

            "'I shouldn't talk to you, but... I'm so sorry, it's just... so quiet here...'"
        "> If it's a trap, it's a stupid one":



            $ points -= 1

            show bg bad with dissolve

            show nerv1

            "'What? I-I mean, you and me are on equal terms here, I'm...'"

            "'I'm just... I'm just trying to help... I am against violence.'"

            hide nerv1
            show sad2

            "'I really can't tell you much, but I won't hurt you...'"


    show bg neutral with dissolve

    show neutral2

    "'Oh! I forgot to introduce myself!..'"

    hide neutral2
    show happ1

    "'My name is Shin...'"

    hide happ1
    show happ3

    "'I'm sorry if it's asking too much but... Can you tell your name too?'"

    hide happ3
    show neutral1

    "'You can keep it a secret if you want... I don't mind.'"

    label name:

    menu:
        "> My name is...":
            $ points += 1
            $ nameset = True

            python:
                povname = renpy.input("What is your name?", length=32)
                povname = povname.strip()


            if povname in ["sou", "hiyori", "sou hiyori", "hiyori sou", "SOU", "HIORI", "HIYORI SOU", "SOU HIYORI", "Sou", "Hiyori", "Sou Hiyori", "Hiyori Sou", "Hiyori-kun", "Hiyori-san"]:


                play sound accent401
                stop music
                show bg bad

                show scared1

                "'. . . .'"

                hide scared1
                show scared2

                "'W-....'"

                "'Ah...'"

                "'I just... I didn't-'"

                hide scared2
                show scared1

                "'I'm sorry, for a second I just...'"

                hide scared1
                show nerv1

                play music denpa fadein 1

                "'Are you sure this is your name?'"

                menu:
                    "> Yes":

                        hide nerv1
                        show scared2

                        "'...I see.'"

                        "'It's just a bit surprising is all...'"

                        hide scared2
                        show nerv1

                        "'But if it's your name, then of course...'"

                        "'Sorry I've made such a fuss...'"

                        hide nerv1
                        show happ4

                        "'It's great to get to know you, [povname]!'"

                        show bg neutral with dissolve
                        hide happ4
                        show neutral2

                        "'You know, it kind of reminded me the first time I've heard this name...'"

                        "'I had another uh... another friend at school back then.'"

                        hide neutral2
                        show nerv1

                        "'Unfortunately, our friendship didn't last, and...'"

                        hide nerv1
                        show neutral1

                        "'Ah! I'm sorry, you're probably not interested in that.'"

                        "'Can I help you in any way?'"

                        jump talk
                    "> No, I'm just joking around":


                        hide nerv1
                        show shock1

                        "'Ah!'"

                        hide shock1
                        show nerv1

                        "'T-that wasn't a nice one!...'"

                        "'But you've totally got me, haha...'"

                        "'Sorry I've made such a fuss...'"

                        show bg neutral with dissolve
                        hide nerv1
                        show happ3

                        "'Do you mind telling me your actual name then?'"

                        "'Sorry If I'm insisting too much...'"

                        hide happ3
                        show nerv1

                        "'It's totally understandable if you don't want to share information about yourself.'"



                        jump name

            elif povname in ["владыка", "Владыка"]:

                hide neutral1
                show shock1

                "'. . . .'"

                "'Точно?'"

                hide shock1
                show neutral2

                "'..Как скажешь...'"

                hide neutral2
                show nerv1

                "'Но только не при всех, л-ладно?'"

                "'. . . .'"

                hide nerv1
                show scared1

                "'Господи, за что мне это...'"

                "'. . . .'"

                hide scared1
                show nerv1

                "'Рад познакомиться, эээ... [povname].'"

                "'Сделаем вид, что этого не было.'"



                jump talk

            elif povname in ["мочезавры", "мочезавр", "Мочезавры", "Мочезавр", "Уринозавр", "уринозавр", "Уринозавры", "уринозавры"]:

                hide neutral1
                show shock1

                "'. . . .'"

                "'. . . .'"

                hide shock1
                show nerv1

                "'Здорово.'"

                "'Хочешь проверить мою способность логически мылить?'"

                "'Или можно сразу начинать звонить в органы пепеги?'"

                "'Рад познакомиться, эээ... [povname].'"

                "'Сделаем вид, что этого не было.'"



                jump talk
            else:



                show bg love with dissolve

                hide neutral1
                show happ2

                "'Thank you!!'"

                "'[povname]!... Nice to meet you!'"

                jump fren

            label fren:


                show bg neutral with dissolve

                hide happ2
                show neutral2

                "'You know, I once had a friend with the same name...'"

                "'Unfortunately, our friendship didn't last, and...'"

                hide neutral2
                show nerv1

                "'Ah! I'm sorry, you're probably not interested in that.'"

                hide nerv1
                show neutral1

                "'Can I help you in any way?'"

                jump talk
        "> I'd rather not. It could be dangerous.":

            $ points -= 1


            show bg bad with dissolve

            hide neutral1
            show sad1

            "'Oh... Okay...'"

            "'You know... I once had a friend who also was very cautious...'"

            hide sad1
            show nerv1

            "'Ah! I'm sorry, you're probably not interested in that.'"

            hide nerv1
            show neutral1

            "'Can I help you in any way?'"


            jump talk


    label talk:

    scene
    show bg neutral

    show neutral1

    menu:
        "> And what happened to your friend?":
            $ points += 1


            show bg love with dissolve

            hide neutral1
            show neutral2

            "'Y-you're interested in that?..'"

            "'I don't know if I can talk about this...'"

            hide neutral2
            show happ4

            "'B-but I think I can trust you!.. Let me see...'"

            show bg neutral with dissolve
            hide happ4
            show neutral1



            "'I had a few friends in school to be honest... Things... never worked out.'"


            "'Sometimes we would eat lunch on the roof... Complaining about our teachers.'"

            hide neutral1
            show sad2

            "'They were a nice person. But they probably wouldn't call me their friend...'"

            hide sad2
            show sad3

            "'And when I met Hiyori, they... just disappeared.'"


            "'First they stopped talking to me, and then they transferred to another school.'"

            hide sad3
            show sad4

            "'They never answered my messages too...'"

            "'And I was thinking I'd be able to consider them a friend.'"

            "'But the feeling wasn't mutual, it seems... As expected...'"

            hide sad4
            show sad5

            "'Maybe I was too boring or... too annoying. Maybe both.'"

            menu:
                "> It's not true. I enjoy talking to you.":
                    $ points += 1

                    scene
                    show bg neutral
                    show sad5
                    show bg love with dissolve

                    hide sad5
                    show shock1

                    "'R-really?'"

                    "'I'm glad to know it!..'"

                    hide shock1
                    show nerv1

                    "'Even if I don't consider it to be true... It's still nice to hear.'"

                    hide nerv1
                    show happ4

                    "'I like talking to you too!'"

                    "'I know, it doesn't sound sincere because I don't have anything else to do but...'"

                    hide happ4
                    show happ1

                    "'I'm not lying. Thank you for listening to me.'"

                    show bg neutral with dissolve



                    jump about
                "> Did 'Hiyori-kun' tell you that?":

                    $ points -= 1

                    scene
                    show bg neutral
                    show sad5
                    show bg bad with dissolve


                    show shock1

                    "'Wh-what are you talking about?..'"

                    hide shock1
                    show sad1

                    "'Hiyori-kun might be a little bit too overprotective, and sometimes he does weird things, but...'"

                    hide sad1
                    show sad2

                    "'I don't think he's tied to that in any way...'"

                    "'Maybe they just... didn't like that I got a new friend.'"

                    hide sad2
                    show sad5

                    "'Yes... It's all my fault...'"

                    show bg neutral with dissolve



                    jump about
        "> Do you know if there are any other hidden rooms?":

            $ points += 0


            show bg neutral with dissolve


            show neutral2

            "'I... I'm not sure...'"

            "'There are some hidden rooms, but you wouldn't be able to access them...'"

            hide neutral2
            show neutral1

            "'You were able to go inside this room only because Hiyori-kun allows it.'"

            "Other rooms are for..."

            hide neutral1
            show sad5

            "'I'm sorry.'"

            "'I can't talk about that.'"

            "'I won't betray him.'"

            show bg neutral with dissolve


            jump about
        "> Do you just want me to ask you about your friend? You're a bad manipulator.":

            $ points -= 1

            scene
            show bg neutral
            show neutral1
            show bg bad with dissolve
            hide neutral1

            show shock1

            "'N-no!..'"

            hide shock1
            show sad5

            "'I... I'm sorry, I didn't mean for it to sound like that... You're right.'"

            "'I didn't mean to vent.'"

            "'You probably have a lot on your mind already...'"

            hide sad5
            show sad4

            "'I'm so sorry. I know I can be annoying at times...'"

            "'Or talk about things that I shouldn't bring up...'"

            "'You're probably not enjoying our conversation from the very start...'"

            hide sad4
            show sad5

            "'I'm very sorry.'"

            menu:
                "> That's not true. I didn't mean to sound rude.":
                    $ points += 0


                    show bg neutral with dissolve
                    hide sad5

                    show sad1

                    "'...Okay.'"

                    hide sad1
                    show sad2

                    "'Just let me know if... If I'm being too annoying, okay?'"

                    "'I don't want to be a burden...'"

                    "'Or to stall you.'"

                    hide sad2
                    show sad3

                    "'I just want what's best for everyone...'"

                    show bg neutral with dissolve


                    jump about
                "> You haven't said anything useful and you don't know when to stop talking.":


                    scene
                    show bg bad
                    show sad5
                    hide sad5
                    stop music



                    show shock1

                    "'. . . !'"

                    "'... I'm s-sorry.'"

                    show bg sad with dissolve
                    hide shock1
                    show sad5


                    "'I'm really sorry that...'"

                    show bg afraid with dissolve

                    hide sad5
                    show cry1

                    play sound kirekake

                    "'I'm sorry. I won't bother you anymore.'"

                    hide cry1
                    show bye1 with hpunch


                    "'I wish you only the best.'"

                    stop sound

                    hide bye1

                    scene bg black
                    with hpunch
                    pause (1.0)

                    scene mon red with dissolve

                    a "> The friendly face had been suddenly consumed by the bright light."

                    a "> Before you were able to aknowledge it, the whole monitor is burning red again."

                    a "> Well. That was expected."

                    a "> You get up with a tired sigh."

                    scene bg black with dissolve
                    pause (1.0)

                    a "> And this is when... You understand."

                    scene 1111 with dissolve
                    play music heart_beat01 fadein 1

                    a "> Something's not right."

                    a "> . . ."

                    a "> You feel an unberable tension going through your body and making you completely still."

                    a "> There's someone else... in the room."

                    a "> You can't hear the steps nor the breathing, but you feel it."

                    a "> You feel a heavy gaze on the back of your head."

                    a "> . . . !"

                    play sound earth3

                    scene bg black with hpunch
                    pause (2.0)

                    "END 1"

                    return

    label about:


    scene
    show bg neutral

    show hz1

    menu:
        "> You're speaking a lot about others... Tell me some more about yourself, maybe?":
            $ points += 1

            scene
            show bg neutral
            show hz1
            show bg love with dissolve
            hide hz1

            show neutral1

            "'About others...'"

            "'To be honest, I don't have any other topics to bring up...'"

            "'Even though I never had much acquaintances...'"

            hide neutral1
            show sad2

            "'About myself... Oh, what can I say about myself?'"

            show bg neutral with dissolve

            show neutral2


            "'I'm a pretty boring person... Nothing special at all.'"

            "'I'm just a simple job-hopper.'"

            "'I've worked in the grocery stores for the most of it... Absolutely nothing special.'"

            hide neutral2
            show happ3

            "'What would you like to know? I don't have much useful information for you, to be honest...'"


            menu:
                "> Everything about you is interesting and useful. What do you usually do in here, for example?":
                    $ points += 1

                    scene
                    show bg neutral
                    show happ3
                    show bg love with dissolve
                    hide happ3

                    show shock1

                    "'. . !'"

                    "'O-oh, I...'"

                    hide shock1
                    show nerv1

                    "'I'm not even sure where to start!..'"

                    "'C-cause there's nothing to start with...'"

                    hide nerv1
                    show neutral2

                    "'Usually, I just... Wait for Hiyori-kun to come back...'"

                    "'He's against me talking to others, though...'"

                    hide neutral2
                    show happ1

                    "'But Maple-san is really nice. She always asks if I would like some tea, and... haha...'"

                    hide happ1
                    show nerv1

                    "'I can't drink it, of course. Even though I'd really love to.'"

                    hide nerv1
                    show neutral1

                    "'Other than that... There's nothing else to do...'"

                    "'. . .'"

                    hide neutral1
                    show happ2

                    "'I'm really happy you asked me, though...'"

                    show bg neutral with dissolve
                    hide neutral1
                    show happ2

                    "'Hiyori also asks me a lot about my interests and so on... However, I don't really understand why.'"

                    hide happ2
                    show neutral2

                    "'He knows everything already.'"

                    "'But I can't really say 'no' when he asks me to tell it all over again...'"

                    hide neutral2
                    show sad1

                    "'. . .'"

                    hide sad1
                    show nerv1

                    "'I'm s-sorry!... I'm talking about him again...Behind his back...'"

                    "'That's not very nice of me.'"



                    jump notsorry
                "> I've changed my mind. Let's talk about something else. Tell me more about Hiyori?":


                    label hiyori:

                    $ points -= 1

                    scene
                    show bg neutral
                    show happ3
                    show bg bad with dissolve
                    hide happ3


                    show sad1

                    "'. . .'"

                    hide sad1
                    show sad2

                    "...I see..."

                    "'Hiyori-kun, he's... Very peculiar.'"

                    hide sad2
                    show nerv1

                    "'He's my best friend, and yet... I mean, everyone's got their oddities, right?'"

                    hide nerv1
                    show neutral1

                    "'But, despite that, he's... Very, very smart.'"

                    "'He's got a lot of friends. He's not like me...'"

                    hide neutral1
                    show sad2

                    "'I can only wish of becoming more like him... Just, without the scary parts of it.'"

                    "'No wonder you want to know more about him...'"

                    hide sad2
                    show sad1

                    "'. . .'"

                    hide sad1
                    show nerv1

                    "'J-just... Be more careful, okay?..'"

                    "'Sometimes I... Don't really feel safe around him...'"

                    "'Even though he'd never done anything bad or weird to me...'"

                    show bg neutral with dissolve
                    hide nerv1
                    show neutral1

                    "'As I've mentioned before, he's just very peculiar...'"

                    "'Maybe, it's his... gaze?'"

                    hide neutral1
                    show sad1

                    "'...Oh...'"

                    hide sad1
                    show nerv1

                    "'It's terrible to speak ill of your friends behind their back. I'm extremely sorry.'"



                    jump notsorry
        "> Can you tell me about that 'Hiyori-kun'? I would like to know more, he seems more interesting than you.":



            jump hiyori
    label notsorry:

    scene
    show bg neutral
    show neutral2

    menu:
        "> You're still a bit tense. Can I do something to make you feel better?":
            $ points += 1

            scene
            show bg neutral
            show neutral2
            show bg love with dissolve
            hide neutral2

            show shock1

            "'... T-tense?'"

            hide shock1
            show nerv1

            "'N-not at all, I just... Stutter a lot.'"

            "'I think it has always been that way...'"

            hide nerv1
            show happ1

            "'Trust me, I enjoy your company!'"


            "'I feel at ease while talking to you... I truly do!'"

            hide happ1
            show happ3

            "'. . .'"

            show bg neutral with dissolve
            hide happ3
            show hz1


            "'I know you'll have to leave, sooner or later...'"

            hide hz1
            show sad1

            "'Everyone does...'"

            ". . ."

            hide sad1
            show happ4

            "'But if we ever happen to meet again... I'd be very glad!..'"

            show bg neutral with dissolve

            jump touch
        "> You don't have to apologize so much. I'm not judging you. We're friends after all.":

            $ points += 0

            scene
            show bg neutral
            show neutral2
            show bg bad with dissolve
            stop music
            hide neutral2

            show scared1

            "'. . .'"

            hide scared1
            show scared2

            "'F... Friends?..'"

            "'... Y-yeah, we're probably...'"

            "'I'm... I'm s-...'"

            hide scared2
            show nerv1

            "'Almost said it again... Haha...'"

            "'But... do you really see me as a friend?'"

            show bg neutral with dissolve

            show nerv1
            play music denpa fadein 1

            "'I... Nobody called me that for so long...'"

            hide nerv1
            show sad1

            "'I mean I barely know you!..'"


            "'But still...'"

            hide sad1
            show happ3

            "'I'm glad I've had an apportunity to talk with someone...'"

            hide happ3
            show sad2

            "'Someone else...'"


            jump touch
        "> I don't really understand how the AIs work. You shouldn't be able to be so nervous.":

            $ points -= 1

            scene
            show bg neutral
            show neutral2
            show bg bad with dissolve
            hide neutral2

            show sad1

            "'That's... not true...'"

            "'I can feel things...'"

            hide sad1
            show sad2

            "'I... I can feel fear just like you... And I am as confused as you are...'"

            "'Even if I'm just a code...'"

            hide sad2
            show sad5

            "'I still fear not existing.'"

            "'I'm afraid I'll become useless... Annoying... Worthless...'"

            "'Because then I'll be deleted for sure.'"

            hide sad5
            show sad4

            "'Like an old game you got tired of it.'"

            "'. . .'"

            hide sad4
            show sad5

            "'You could break this screen so easily...'"

            "'. . .'"
            show bg sad with dissolve


            show scared1

            "'. . .'"

            hide scared1
            show scared2

            "'Y-you wouldn't do that, would you?..'"

            menu:
                "> Of course not. I'd take you and your monitor with me if I could.":
                    $ points += 1

                    scene
                    show bg sad
                    show scared2
                    show bg love with dissolve
                    hide scared2


                    show shock1

                    "! . ."

                    hide shock1
                    show nerv1

                    "'Haha... I... I don't think it's that easy...'"

                    "'The monitor is probably heavy too... Haha...'"

                    hide nerv1
                    show sad1

                    "'Besides... I don't think I... can leave at all.'"

                    "'I don't want any trouble...'"
                    show bg neutral with dissolve


                    jump touch
                "> Even if I wanted to, it's too dangerous. Somebody wants you to stay there.":

                    $ points -= 1

                    scene
                    show bg sad
                    show scared2
                    show bg bad with dissolve
                    hide scared2


                    show sad2

                    "'Ah...'"

                    "'That's right...'"

                    hide sad2
                    show sad5

                    "'. . .'"

                    "'I... I promise I don't want to harm you, really...'"

                    "'But... I can see why you can't trust me. I'm sorry.'"
                    show bg neutral with dissolve


                    jump touch
                "> Even if I destroy you, you probably have a back-up file or something. It's pointless.":

                    $ points -= 1

                    scene
                    show bg sad
                    show bg bad with dissolve


                    show scared1

                    "'! . .'"

                    "'It's... It's not like that...'"


                    show sad4

                    "'Right now... I don't have any copies of myself...'"

                    "'If you break this screen, I won't... recover...'"

                    "'. . .'"

                    show bg sad with dissolve


                    show scared1

                    "'Wh-why are you looking at me like that?..'"
                    show bg neutral with dissolve


                    jump touch


    label touch:

    scene
    show bg neutral

    show sad1

    "'You know... I haven't spoke with someone for so long for a while...'"

    hide sad1
    show neutral2

    "'I mean, Hiyori-kun is a great listener, but...'"

    hide neutral2
    show sad2

    "'It's like... He does not participate in talking...'"

    "'But lately he upgraded my monitor to have a touch-screen, and now...'"

    hide sad2
    show nerv1

    "'All he does is poke me in the face...'"

    "'It's... a bit annoying!..'"

    a "> He looks at you as if he's expecting something..."

    a "> ...He's not very good at manipulating."

    a "> You're not sure if AI can feel anything, but you decide to try anyway."

    menu:
        "> Pet his head":

            scene
            show bg neutral
            show bg love with dissolve
            show pat3 with dissolve

            "'! . .'"

            "'. . .'"

            "'. . .'"

            "'He... He's never done that before...'"

            "'It's weird... But it feels nice...'"

            hide pat3
            show happ2 with dissolve

            "'...Thank you...'"

            "'Usually he just pinches my cheeks...'"

            show bg neutral with dissolve


            jump hobby
        "> Boop his nose":


            scene
            show bg neutral
            show bg love with dissolve
            show pat2 with dissolve
            play sound cat_like1a

            "'! . .'"

            "'. . .'"

            "'O-okay...'"

            "'I can't really feel how warm your hands are but...'"

            hide pat2
            show hz1 with dissolve

            "'It feels a little weird...'"

            show bg neutral with dissolve

            jump hobby
        "> Pinch his cheek":


            scene
            show bg neutral
            show bg bad with dissolve


            show pat1 with dissolve
            play sound squeaky_toy

            "'Ow!..'"

            "'. . .'"

            "'...Please, stop..."

            "'. . .'"


            show sad1 with dissolve
            hide pat1

            "'Hiyori-kun also does this to me...'"

            "'It doesn't hurt that much but...'"

            "'It's still unpleasant.'"

            show bg neutral with dissolve

            jump hobby



    label hobby:

    scene
    show bg neutral
    show nerv1

    "'Oh!...'"

    "'I think I am... making everything about myself...'"

    "'It's a bit embarassing, haha...'"

    hide nerv1
    show neutral2

    "'I'm sorry for not asking earlier but...'"

    "'I'll understand if you don't want to share...'"

    "'Can you tell me a bit more about yourself?'"

    hide neutral2
    show neutral1

    "'For example, I... Um...'"

    hide neutral1
    show happ3

    "'I like video games!..'"

    hide happ3
    show happ1

    "'Especially multiplayer games...'"

    "'If it was possible to install some games here...'"

    hide happ1
    show happ4

    "'I'd happily play some with you!..'"

    hide happ4
    show nerv1

    "'If you don't mind, of course!'"

    "'It would be very nice...'"

    hide nerv1
    show neutral1

    "'Do you have any hobbies? What do you like to do in your free time?'"

    python:
        povhobby = renpy.input("What do you like to do in your free time? (do not use CAPS)", length=32)
        povhobby = povhobby.strip()

    if povhobby in ["art", "ART", "Art", "drawing", "Drawing", "DRAWING", "making art", "Making art", "making Art", "Making Art"]:
        scene
        show bg neutral
        show neutral1
        show bg love with dissolve
        hide neutral1

        show happ1

        "'Drawing!...'"

        hide happ1
        show happ4

        "'That's so nice!.. It's wonderful that you have a thing that you enjoy doing...'"

        hide happ4
        show neutral1

        "'To be honest, I've never talked to any artists...'"

        "'So I don't really know much about it and what to say...'"

        "'But one thing for sure...'"

        hide neutral1
        show happ2

        "'Don't forget to take a break from time to time, okay?..'"

        "'Don't overwork yourself and your hand, and leave some time for yourself to relax.'"



        label goodboy:

            scene
            show bg love

            show neutral2

            "'Sometimes the inspiration comes in sudden bursts...'"

            "'But you and your wellbeing should always be your number one priority!...'"

            hide neutral2
            show happ3


            "'It's easier to do your favorite things when you're well rested.'"

            "'And even if you don't like what you can do right now...'"

            hide happ3
            show happ5
            play sound cat_like1a

            "'There are people who love what you do!'"

            "'And who love YOU, too!'"

            hide happ5
            show neutral2

            "'You can say a lot about a person by looking at their work!..'"

            hide neutral2
            show happ3

            "'I might not be very knowlegable, but I wish you only the best in your endevours!..'"

            "'Just remember that your hobby is something you do for yourself, and not for somebody else.'"

            hide happ3
            show happ1

            "'Then it will bring you much more enjoyment.'"

            hide happ1
            show nerv1

            "'I-I'm sorry, I got a bit carried away!.. I'd be happy if you've ever shown your work to me, haha...'"

            hide nerv1
            show happ4

            "'Thank you for sharing with me!'"

            show bg neutral with dissolve


            jump final

    elif povhobby in ["photo", "Photo", "PHOTO", "photography", "Photography", "PHOTOGRAPHY", "taking photos", "Taking photos", "Taking Photos", "photos", "PHOTOS", "Photos"]:

        scene
        show bg neutral
        show neutral1
        show bg bad with dissolve
        hide neutral1



        show scared1

        stop music
        play sound accent401

        "'. . . !'"

        hide scared1
        show scared2

        "'You... like t-taking photos?..'"

        hide scared2
        show nerv1

        "'Haha... It's... a nice hobby!..'"

        "'Yeah...'"

        hide nerv1
        show scared1

        "'. . .'"

        hide scared1
        show nerv1

        "'It's... very creative...'"

        "'. . .'"


        show bg neutral with dissolve
        show sad2
        play music denpa fadein 1

        "'Hiyori-kun... also enjoys photography.'"

        "'I don't really understand it...'"

        hide sad2
        show nerv1

        "'I-I mean!.. The landscape photos he takes are very pretty but...'"

        "'. . .'"

        hide nerv1
        show sad1

        "'I'm sorry for my reaction.'"

        hide sad1
        show neutral1

        "'I don't know what kind of photos you like to take... Portraits, landscapes, but...'"




        jump goodboy

    elif povhobby in ["sport", "Sport", "SPORT", "Sports", "SPORTS", "sports", "playing sports", "Playing sports", "football", "Football", "Basketball", "basketball", "baseball", "Baseball", "soccer", "Soccer", "gymnastics", "Gymnastics", "swimming", "Swimming"]:

        scene
        show bg neutral
        show neutral1
        show bg love with dissolve
        hide neutral1

        show happ1

        "'You like sports? That's so cool!'"

        "'I envy you, haha...'"

        hide happ1
        show happ4

        "'I've been on a weaker side since I remember...'"

        hide happ4
        show nerv1
        play sound powerdown07

        "'I can't imagine being able to train regularly, to be honest...'"

        hide nerv1
        show happ2

        "'But if you really enjoy it, it's very nice!'"

        "'I would gladly watch you practice...'"

        hide happ2
        show happ1

        "'. . .'"

        "'M-maybe you could train me... Haha...'"

        "'It would be fun!..'"

        hide happ1
        show happ3

        "'Right now I'm not bad at swiming!..'"

        "'So, if we ever met again, we could come up with something!'"

        "'I'd be more than happy to train with you!'"

        hide happ3
        show nerv1

        "'I-I realize that it sounds absurd, haha...'"

        hide nerv
        show happ4

        "'Thank you so much for sharing with me!'"

        show bg neutral with dissolve



        jump final

    elif povhobby in ["writing", "Writing", "WRITING", "to write", "write", "Write", "Fic writing", "fic writing", "ficwriting", "Ficwriting", "writing fics", "Writing fics", "poetry", "Poetry", "writing poetry", "Writing poetry"]:

        scene
        show bg neutral
        show neutral1
        show bg love with dissolve
        hide neutral1


        show neutral2

        "'O-oh, you're a writer?'"

        hide neutral2
        show happ1

        "'That's so cool!..'"

        "'You know, you could say I am a writer too, in a sense!'"

        hide happ1
        show happ4

        "'I really like coding...'"

        "'I'm not very good at it yet, but... I'm improving every day!'"

        hide happ4
        show neutral2

        "'Besides, I have an access to any educational info on this computer...'"

        "'You're probably writing something more... poetic?'"

        hide neutral2
        show happ3

        "'It would be nice to read one of your works sometime!..'"



        jump goodboy

    elif povhobby in ["gaming", "Gaming", "games", "Games", "playing games", "Playing games", "video games", "Video games"]:

        scene
        show bg neutral
        show neutral1
        show bg love with dissolve
        hide neutral1


        show shock1

        "'. . !'"

        "'I-I love it too!'"

        hide shock1
        show happ1

        "'Ah, I must've told you about it before already...'"

        "'But I also love gaming!'"

        hide happ1
        show happ3

        "'Sometimes I like to play something hardcore...'"

        "'But to be honest, most of all I enjoy sandbox games.'"

        "'You can just sit and relax after a hard day...'"

        "'Just run around and look at pretty landscapes... Farm games are also very relaxing...'"

        hide happ3
        show happ2

        "'Can you tell me about your favorite games when we meet again?'"

        hide happ2
        show happ1

        "'If we get the opportunity, of course...'"

        "'It would be very nice!'"

        hide happ1
        show happ3

        "'Just don't forget to take breaks while playing... Your eyes can get tired pretty quickly, even if your brain is relaxing.'"

        "'Thank you so much for sharing with me!'"



        jump final

    elif povhobby in ["music", "Music", "playing music", "Playing music", "playing instruments", "Playing instruments", "playing piano", "Playing piano", "playing guitar", "Playing guitar", "piano", "Piano", "Guitar", "guitar"]:

        scene
        show bg neutral
        show neutral1
        show bg love with dissolve
        hide neutral1


        show neutral2

        "'O-oh, you play music?'"

        hide neutral2
        show happ4

        "'That's so cool!..'"

        "'I never understood how to write music...'"

        hide happ4
        show neutral1

        "'I think, Hiyori-kun mentioned that he can play a couple of instruments... He can play piano for sure...'"

        hide neutral1
        show nerv1

        "'Ah!... I'm sorry, didn't mean to talk about him again.'"

        hide nerv1
        show happ1

        "'Anyways... I tried playing piano once, and never touched it again.'"

        "'But I enjoy listening to music!..'"

        "'Being able to create something is so amazing...'"



        jump goodboy

    elif povhobby in ["nothing", "Nothing", "NOTHING"]:

        scene
        show bg neutral
        stop music
        show neutral1
        show bg bad with dissolve
        hide neutral1

        show sad1



        "'. . .'"

        hide sad1
        show sad2

        "'O-okay...'"

        "'I don't mind if you don't want to share...'"

        hide sad2
        show happ3

        "'Just know that whatever it is, I support you and your hobby, and I'm glad you have a thing you enjoy doing!'"

        "'A hobby helps you forget about the world when everything is... too much.'"

        hide happ3
        show nerv1

        "'Sorry, that sounded grim.'"

        hide nerv1
        show sad2

        "'. . .'"

        hide sad2
        show neutral1
        play music denpa fadein 1

        "'But you know... It would be nice if we got an apportunity to talk about it sometime.'"

        "'But I can understand your distrust.'"
        show bg neutral with dissolve

        jump final

    elif povhobby in ["срать", "СРАТЬ", "Срать", "какать", "Какать", "КАКАТЬ", "srat", "SRAT", "Srat", "srat'", "SRAT'", "Srat'"]:

        scene
        show bg neutral
        show neutral1
        show bg black with dissolve
        hide neutral1

        show nerv1

        "'. . .'"

        "'Я же просил, давай без этого...'"

        "'А как же обещание... Сделать вид, что ничего не было...'"

        hide nerv1
        show hz1

        "'Кхм.'"

        hide hz1
        show happ3

        "'Очень классное хобби.'"

        "'Довольно... нестандартное. Для человека.'"

        hide happ3
        show nerv1

        "'Как ты видишь, я... На данный момент просто ПО, поэтому возможность выполнять данную функцию... у меня отсутствует.'"

        "'Но я, эм... Поддерживаю тебя... В твоих начинаниях.'"

        hide nerv1
        show hz1

        "'. . .'"

        hide hz1
        show nerv1

        "'Не обосрись, да не обосран будешь.'"
        show bg neutral with dissolve

        jump final

    elif povhobby in ["sculpture", "Sculpture", "sculpting", "Sculpting", "to sculpt", "To sculpt"]:

        if povname in ["sou", "hiyori", "sou hiyori", "hiyori sou", "SOU", "HIORI", "HIYORI SOU", "SOU HIYORI", "Sou", "Hiyori", "Sou Hiyori", "Hiyori Sou", "Hiyori-kun", "Hiyori-san"]:

            jump secret
        else:


            scene
            show bg neutral
            show neutral1
            show bg love with dissolve
            hide neutral1


            show neutral2

            "'Sculpture?..'"

            hide neutral2
            show nerv1

            "'Haha... Sounds a bit familiar.'"

            "'I don't know much about it, but I think...'"

            hide nerv1
            show happ1

            "'Hiyori once told me about that.'"

            "'He told me that he enjoys doing that, as well as photography...'"

            hide happ1
            show neutral2

            "'I can't imagine doing something like that, making a solid object look soft and so alive...'"

            jump goodboy
    else:


        scene
        show bg neutral
        show neutral1
        show bg love with dissolve
        hide neutral1


        show happ2

        "'That's so cool!'"

        "'I'm glad you have something you enjoy doing.'"

        hide happ2
        show happ1

        "'I love seeing how happy people get when they are talking about something they like...'"

        "'Even if I'm not very knowledgeble in this, I hope doing it helps you through the bad times...'"

        "'A hobby helps you forget about the world when everything is... too much.'"

        hide happ1
        show nerv1

        "'Sorry, that sounded grim.'"

        hide nerv1
        show happ2

        "'I'm just glad you have something you enjoy doing.'"

        hide happ2
        show neutral1

        "'But... It would be nice if we got an apportunity to talk more about it sometime.'"

        "'I know, right now is not the best time for that...'"

        hide neutral1
        show happ3

        "'Maybe in future... Haha...'"


        show bg neutral with dissolve

        jump final

    label final:

    scene
    show bg neutral
    show neutral1

    menu:
        "> That's really nice of you. (Pet the monitor)":
            $ points += 1

            scene
            show bg neutral
            show neutral1
            show bg love with dissolve
            hide neutral1
            show pat3 with dissolve
            play sound accent281

            "'! . . .'"

            "'. . .'"

            "'Th-thank you...'"

            hide pat3
            show happ1 with dissolve

            "'I'm glad to hear it!..'"

            "'I-I'm not that nice, but...'"

            hide happ1
            show happ3

            "'I'm just happy to help you...'"

            "'You're a good person. I can see that!'"



            jump finish
        "> Even if you don't know that much about it... Thank you.":

            $ points -= 0

            scene
            show bg neutral
            show neutral1
            show bg neutral with dissolve
            hide neutral1

            show nerv1

            "'Haha, yes... I really don't know much...'"

            "'As I said... I'm an ordinary and boring person, but...'"

            hide nerv1
            show happ3

            "'I'm happy to hear that I could keep you company!..'"

            "'Thank you, too!'"



            jump finish
        "> I don't need your fake support.":

            $ points -= 1

            scene
            show bg neutral
            show neutral1
            show bg bad with dissolve
            hide neutral1

            show shock1

            "'Ah!...'"

            hide shock1
            show sad5

            "'I-I understand your distrust, but...'"

            "'My support... isn't fake...'"

            hide sad5
            show sad4

            "'. . .'"

            "'Sorry if I upset you with my words...'"

            "'I'm not very good at that...'"

            "'I never wanted to make you upset...'"

            jump finish

    label finish:



    if points >= 58:

        show bg love with dissolve
        scene
        show bg love
        show sad1
        play music hakanai fadein 1

        "'I know we don't have much time left but...'"

        hide sad1
        show happ3

        "'I'm glad I got to spend some time with you!'"

        "'It would be nice to meet you again in the future... When things are... normal again.'"

        hide happ3
        show happ1

        "'We could talk more about you, your interests, your hobbies... I would be glad if we...'"

        "'If we...'"

        "'. . .'"

        hide happ1
        show shy1

        "'If we..could become real friends!..'"

        "'I'd love to be able to... call myself your friend...'"

        "'I'm sorry if this is too sudden!..'"

        hide shy1
        show happ1

        "'I'm just a bit nervous but... in a good way!..'"

        "'To be honest, I haven't felt at ease like this for a long time...'"

        hide happ1
        show happ3

        "'Thank you!..'"

        "'You came here even though it's dangerous to walk alone, but... I'm glad I met you.'"

        hide happ3
        show happ1

        "'Even for a little while.'"

        "'If I could ever help you with anything... Don't hesitate to ask!'"

        hide happ1
        show bye2 with dissolve

        "'I wish you only the best... Even if it's not right to say goodbye like that...'"

        "'Maybe next time we could play games together...'"

        "'A fighting game or... a farm?'"

        "'I would be so happy to spend time with you again.'"

        "'And also, we-...'"

        stop music fadeout 2

        "'. . .'"

        "'. . .'"

        hide bye2
        show bg afraid
        show bye3 with hpunch

        "'. . .'"

        "I-I'm sorry, I..."

        "'I'm sorry!'"

        "'You should-!'"

        hide bye3
        play sound computer

        scene bg black
        with hpunch
        pause (1.0)

        scene mon red with dissolve

        a "> The friendly face has been suddenly consumed by the bright light."

        a "> Before you were able to aknowledge it, the whole screen is burning red again."

        a "> What happened?"

        a "> You desperately touch the screen a couple of times, but there's no response."

        scene bg black with dissolve
        pause (1.0)

        a "> And this is when... You understand."

        scene 1111 with dissolve
        play music heart_beat01 fadein 1

        a "> Something's not right."

        a "> . . ."

        a "> You feel an unberable tension going through your body and making you completely still."

        scene end1 with dissolve

        a "> There's someone else... in the room."

        a "> You can't hear the steps nor the breathing, but you feel it."

        a "> You feel a heavy gaze on the back of your head."

        a "> . . ."

        scene bg black with dissolve
        pause (1.0)

        stop music

        m "'Hey there...'"

        m "'Haha... What are you doooing here?'"

        m "'Actually, that's mine...'"

        scene end2
        play sound horror_pianochord3

        m "'Weren't you taught not to stick your nose where it doesn't belong?'"

        m "'You're being awfully nice, aren't you?'"

        m "'It's a good thing I know juuuust how to fix this! Haha...'"

        play sound earth3
        scene bg black with hpunch
        pause (2.0)

        "END 2"

        return

    elif points <= 45:


        show bg sad with dissolve
        scene
        show bg sad
        show sad2
        play music hazama1 fadein 1

        "'I know we don't have much time left but...'"

        hide sad2
        show sad1

        "'I just don't understand... What did I do wrong?..'"

        "'I mean, I wasn't mean to you...'"

        "'Or do you just see me as an enemy because I'm... in this room? And because I know Hiyori-kun?'"

        "'I can understand that but...'"

        hide sad1
        show sad5

        "'. . .'"

        hide sad5
        show cry1

        play sound kirekake

        "'I-I'm sorry, it's just... not fair!..'"

        "'I never wanted to harm you, and...'"


        show bg afraid with dissolve
        hide cry1
        show cry2

        "'I've never tried to do anything to you while we were talking!...'"

        "'Even if I'm not a human, my conscious is... It's still the same as yours, as of any human...'"

        "'. . .'"

        hide cry2
        show bye1 with hpunch

        "'I'm sorry. I won't bother you anymore since you dislike me so much.'"

        hide bye1 with hpunch

        scene bg black
        with hpunch
        pause (1.0)

        scene mon red with dissolve

        a "> The friendly face had been suddenly consumed by the bright light."

        a "> Before you were able to aknowledge it, the whole monitor is burning red again."

        a "> Well. That was expected."

        stop music fadeout 2

        a "> You get up with a tired sigh."

        scene bg black with dissolve
        pause (1.0)

        a "> And this is when... You understand."

        scene 1111 with dissolve
        play music heart_beat01 fadein 1

        a "> Something's not right."

        a "> . . ."

        a "> You feel an unberable tension going through your body and making you completely still."

        a "> There's someone else... in the room."

        a "> You can't hear the steps nor the breathing, but you feel it."

        a "> You feel a heavy gaze on the back of your head."

        a "> . . ."

        scene bg black with dissolve
        pause (1.0)
        stop music

        m "'Hey there...'"

        m "'Haha... What are you doooing here?'"

        m "'Actually, that's mine...'"

        scene 11112
        play sound horror_pianochord3

        m "'Weren't you taught not to stick your nose where it doesn't belong?'"

        m "'So rude of you...'"

        m "'It's a good thing I know juuuust how to fix this! Haha...'"

        play sound earth3
        scene bg black with hpunch
        pause (2.0)

        "END 3"

        return
    else:




        show bg neutral with dissolve
        scene
        show bg neutral
        show sad1
        play music tunagu2 fadein 1


        "'I know we don't have much time left but...'"

        hide sad1
        show neutral2

        "'It was nice to spend time with you.'"

        "'Even if you still don't trust me completely, I can understand why...'"

        hide neutral2
        show happ3

        "'I'd be glad to get to know you more...'"

        "'Haha...'"

        hide happ3
        show neutral1

        "'But if you ever need my help...'"

        "'Don't be afraid to ask.'"

        hide neutral1
        show happ4

        "'Thank you for spending time with me...'"

        hide happ4
        show neutral2

        "'You probably should go back to your friends before it's to late...'"

        "'And don't worry, I won't tell anyone you were here!'"

        hide neutral2
        show happ2

        "'I wish you only the best!..'"

        hide happ2
        play sound computer

        scene bg black with dissolve
        pause (1.0)


        scene mon red with dissolve

        a "> Before you could answer, the screen went red again."

        a "> Well... It was an Experience."

        a "> You didn't learn anything that would help you, but for some reason you feel... at ease."

        a "> Maybe you just needed a distraction."

        scene bg monitor room 1 with dissolve
        play music tansaku3 fadein 1

        a "> You get up from your chair with a sigh and walk to the door."

        a "> You hear steps from behind it."

        a "> Feeling determined, you open the door."

        scene bg black with dissolve
        pause (2.0)

        "END 4"
        stop music fadeout 2

        return






    return





label secret:



    scene
    show bg neutral
    show neutral1
    show bg love with dissolve
    hide neutral1


    show neutral2

    "'Sculpture?..'"

    hide neutral2
    show nerv1

    "'Haha... Sounds a bit familiar.'"

    "'I don't know much about it, but I think...'"

    hide nerv1
    show happ1

    "'Hiyori once told me about that.'"

    "'He told me that he enjoys doing that, as well as photography...'"

    hide happ1
    show neutral2

    "'I can't imagine doing something like that, making a solid object look soft and so alive...'"

    hide neutral2
    show hz1
    pause (1.0)

    stop music fadeout 2

    a "> Something's wrong."

    a "> You don't know why but for some reason every word he speaks makes you more and more nauseous."

    a "> Your hands become cold and shaky."

    a "> But you can't muster opening your mouth to tell him to stop."

    hide hz1
    show happ1

    "'Oh!.. I remember him showing me a couple of his works...'"

    "'They weren't finished, but... They still looked kinda cool!'"

    hide happ1
    show hz1

    "'. . .'"

    play music heart_beat01 fadein 2

    "'. . .'"

    hide hz1
    show nerv1

    "'Hey...'"

    "'Are you alright?'"

    "'You look pale...'"

    a "> It would be weird if you weren't pale in this situation."

    a "> Something in his words made you terrified."

    a "> Your hands balled into fists, as you looked around the room anxiously."

    a "> You can't make a sound. You're too busy desperately gasping for air."

    scene
    show bg love
    show nerv1
    show bg afraid with dissolve
    hide nerv1

    show scared1

    "'H-hey!..'"

    "'I don't... There are some water bottles behind you, please take it!..'"

    hide scared1
    show scared2 with hpunch

    "'Please, st-...'"

    scene bg black with dissolve
    stop music fadeout 2

    a "> His voice becomes distant until it fades into nothing."

    a "> And then... darkness consumes you completely."

    window hide dissolve

    pause(3.0)

    pov "'. . .'"

    pov "'. . .'"

    pov "'. . .'"

    pov "'. . ?'"

    w "'Hey...'"

    w "'Shin...'"

    w "'Wake up.'"

    b "'What...'"

    scene shinsleep with dissolve
    pause(2.0)

    scene shinwake with dissolve
    pause(1.0)

    b "'Hmm...'"

    pov "You open your eyes and then instantly shut them back. The bright light makes your head hurt like hell."

    b "'Ugh...'"

    w "'C'mon... You cannot sleep for the whole day.'"

    pov "You were... sleeping?"

    pov "Slowly, you're becoming aware of your surroundings."

    play music hazama2 fadein 3

    scene souroom with dissolve
    pause(1.0)

    pov "Of course, you're not at your house. But this place had already become your second home."

    pov "The undescribable anxiety fills you, strangely mixing with content, and it makes you wake up completely."

    pov "Is it evening already?"

    b "'Ugh... My back hurts...'"

    show sou4 with dissolve

    c "'Of course it does. I left to grab a cup of coffee, and you're already made yourself comfortable on the table.'"

    c "'You could've taken the couch, you know... It's bad for your back!'"

    hide sou4
    show sou3

    c "'You might've fallen from the chair, or the monitor could fall on your head. It's quite heavy.'"

    pov "You never thought about that. But now you will."

    pov "You can't remember when you fell asleep, but that doesn't bother you anymore."

    show sou3 at right with move

    show shin3 at left with dissolve

    b "'Aha, yeah... It could...'"

    hide shin3
    show shin4 at left

    b "'D-do you mind if I take a proper nap? I don't feel that well...'"

    hide sou3
    show sou1 at right

    c "'I don't mind, but are you sure you'll feel better?'"

    c "'You've already slept through the most of the day. Your head will hurt so much. Trust me, I know how that feels.'"

    hide shin4
    show shin1 at left


    b "'Mm... Maybe, you're right... My head hurts already...'"

    pov "He's always right."

    hide sou1
    show sou12 at right

    c "'Oh, I can help you to stay up!'"

    c "'You promised you'll help me. Lets see...'"

    hide sou12
    show sou11 at right

    c "'Do you remember the game I've shown you?'"

    hide shin1
    show shin6 at left

    b "'Which one of all of your games?..'"

    hide sou11
    show sou14 at right

    play sound extend1

    c "'Haha, your memory is giving up already? Not a good sign for your age.'"

    hide sou14
    show sou12 at right

    c "'Good thing that you have me! No need to spend money on a doctor when you have these games.'"

    hide shin6
    show shin5 at left

    b "'. . .'"

    b "'You mean that card game?'"

    hide sou12
    show sou5 at right

    c "'Bingo! You can remember anything if you really try to. See? My methods are working already!'"

    c "'Now, look at the screen.'"

    stop music fadeout 2

    scene screen1 with dissolve
    pause(1.0)

    play sound computer

    scene screen2 with hpunch
    pause(0.5)

    play music nounai fadein 2

    c "'Alright, let's start with a simple one. Your brain must be full of cobwebs! Do you even remember what this game is about?'"

    b "'Uhh... It's like the Werewolf or Mafia game, right?'"

    show screen4

    c "'Haha, almost. It's been a while since we've played this game, hasn't it?'"

    play sound powerdown07

    b "'Because it's almost impossible to play with only two of us...'"

    c "'That's right. But it doesn't matter, Shin.'"

    hide screen4
    show screen2

    c "'The point of the game is to make sure nobody knows which card you have. Even if there are only two people left.'"

    b "'Left?..'"

    c "'Well, somebody's gonna lose when others learn which card they have.'"

    c "'At some point it's gonna be one-on-one. I though you understood that.'"

    b "'Right... S-sorry, I'm probably still sleepy.'"

    hide screen2
    show screen4

    c "'I can see that. That's why I am reminding you all that.'"

    c "'Sometimes the rules can be fake, as well as the cards themselves. That's why you should always keep the correct info in mind.'"

    b "'Aha... Isn't it too much for a simple card game?'"

    c "'You're saying that you can't memorize even the basics?'"

    c "'No wonder you never win against me.'"

    b "'Uh... Sorry.'"

    hide screen4
    show screen2

    c "'Let's get to it then.'"

    show card1 zorder 1 with dissolve
    pause(2.0)

    c "'Let's start with a simple one. Do you remember which card is a legit one?'"

    label firstq:

        menu:
            "The one on the left":

                b "'The one on the left?..'"

                label wrong1:

                    hide screen2
                    show screen5
                    show card1 zorder 1

                    play sound buzzer1

                    c "'As I thought... You know, associative learning is one of the easiest ways to learn things. Too bad it doesn't work for you.'"

                    b "(Damn... It was wrong.)"

                    c "'The correct one is on the right. One book, which is closed. See, easy to remember, right?'"

                    hide screen5
                    show screen2


                    c "'Hope you won't disappoint me next time.'"

                    jump secondq
            "The one in the middle":


                b "'The middle one?..'"

                jump wrong1
            "The one on the right":


                $ quiz_score += 1
                b "'The right one?..'"

                hide screen2
                show screen4
                show card1 zorder 1

                play sound accent281

                c "'See! You're doing it! The card with one book, which is closed.'"

                c "'Good job.'"

                b "'I-I guess... It wasn't that hard.'"

                c "'This knowledge might come in handy one day! We might go to a party some time, and this game is best played with lots of people.'"

                hide screen4
                show screen2

                pov "You are not sure if you ever get to go party, but you still nod with an unsure smile."

                jump secondq

    label secondq:

        c "'Hm, what should I ask you next...'"

        hide card1 with dissolve

        c "'Oh, do you remember which card is the most importand card in the game?'"

        show card2 zorder 1 with dissolve
        pause(2.0)

        menu:
            "The one on the left":

                b "'Um... Left one?'"

                hide screen2
                show screen4
                show card2 zorder 1

                play sound buzzer1

                c "'Hm... sadly, no. That's a wrong answer.'"

                c "'The card with a key is the strongest and most important card.'"

                c "'You should always keep this card in mind, Shin. Think of it as if it's a key to your victory, haha!'"

                c "'This is the only card that should be disclosed. Because if you have it, the other players cannot drop you out, otherwise it's an instant loss for everyone.'"

                hide screen4
                show screen5

                c "'The thing is... Will they trust your word? Haha.'"

                b "(Damn... It was wrong.)"

                hide screen5
                show screen2

                c "'That's a pity. I hope you'll memorize it now.'"

                jump thirdq
            "The one on the right":


                $ quiz_score += 1
                b "'Right one?..'"

                hide screen2
                show screen4
                show card2 zorder 1

                play sound accent281

                c "'That's right! Oh, you're making me feel so proud!'"

                b "'Uh... If I remember correctly, this card guarantees that no one will touch you. Because if they choose you as a culprit, it's an instant loss for everyone.'"

                b "'You should always let people know that you have this card, right?'"

                c "'Nicely done! You are correct. You did listen to my explanations after all!'"

                b "'I always listen to you, Hiyori-kun...'"

                hide screen4
                show screen2

                jump thirdq


    label thirdq:

        hide card2 with dissolve

        c "'Let's see what's next.'"

        show eye zorder 1
        pause(0.1)
        hide eye

        show arm zorder 1
        pause(0.1)
        hide arm

        stop music fadeout 1

        show card3 zorder 1 with dissolve
        pause(2.0)

        play sound horror_pianochord3

        b "'! . .'"

        hide screen2
        show screen5

        c "'Mm? Something's the matter?'"

        b "'. . .'"

        b "'N-no, it's... nothing.'"

        play music nounai fadein 2

        c "'Oh, good.'"

        hide screen5
        show screen2

        c "'Do you remember which card is used in the game?'"

        menu:
            "The one on the left":

                $ quiz_score += 1
                b "'The one on the left... The right one does not exist, right?'"

                hide screen2
                show screen4

                play sound accent281

                c "'That's correct! Haha, nice work not falling for my trap.'"

                c "'Some game masters could try to deceive you and give you the fake card. That's why you should always remember how real cards look.'"

                c "'If you keep the rules in mind, you will win.'"

                c "'But you are a cutie, so you don't have to worry. Nobody would want to get rid of you when you look at them with your big sad eyes.'"

                hide screen4
                show screen5

                c "'People tend to trust those who are friendly and weak. But how long will it last? Haha.'"

                b "'H-hiyori-kun!.. Stop messing with me...'"

                c "'Oh, I'm barely joking!'"

                hide screen5

                jump fourthq
            "The one on the right":


                b "'Um... Right one?'"

                hide screen2
                show screen5

                play sound buzzer1

                c "'Hm... No, you are wrong. Did you even listen to my explanation?'"

                c "'This card does not exist.'"

                c "'Some game masters could try to deceive you and give you the fake card. That's why you should always remember how real cards look.'"

                hide screen5
                show screen2

                c "'I hope you'll remember this.'"

                b "(Damn... I was wrong.)"

                hide screen2

                jump fourthq
            "...What were those pictures?":


                b "'H-hiyori-kun... What was that..?'"

                c "'What do you mean?'"

                b "'There were pictures for a split second... Photos of some sort..?'"

                hide screen2
                show screen5

                play sound extend1

                c "'Are you trying to avoid my question? Haha, that's so like you.'"

                b "'. . .'"

                pov "You cannot shake off the anxiety."

                pov "But... Maybe, it's just your imagination."

                hide screen5
                show screen2

                c "'The correct card was on the left. Take a close look at it.'"

                c "'Some game masters could try to deceive you and give you the fake card. That's why you should always remember how real cards look.'"

                hide screen2

                jump fourthq

    label fourthq:

        show screen2
        hide card3 with dissolve

        c "'Alright, the last question.'"

        show card4 zorder 1 with dissolve
        pause(1.0)

        c "'Now that we know that this card is real... do you remember what it's called?'"

        python:
            cardname = renpy.input("What is this card called?", length=32)
            cardname = cardname.strip()

        if cardname in ["SACRIFICE", "sacrifice", "Sacrifice"]:

            $ quiz_score += 1
            b "It's [cardname], right?"

            hide screen2
            show screen4

            play sound accent281

            c "'Bingo!'"

            c "'See? Wasn't so hard, wasn't it? Do you remember what this card does?'"

            b "'From what you explained, it's... almost as important as the key one? It's one of the strongest cards, but... You need everyone to trust you. If they don't, it's a loss for you...'"

            hide screen4
            show screen5

            c "'Oh, you're killing it today, Shin!'"

            c "'Just don't forget that no one should know you have this card. If it's called ''Sacrifice'' you really gotta make everyone believe you should be sacrificed.'"

            c "'Otherwise, consider it's a loss the very moment you pick this card, haha.'"

            b "'Have you ever won with this card?'"

            hide screen5
            show screen4

            c "'Hm? Why do you ask?'"

            b "'Well... you've played this game before, and you know the rules so well... Have you won with it before?'"

            c "'Maybe I have. I'll leave it to your imagination.'"

            b "'Hiyori-kun!.. I did my best to answer your questions, why can't you answer mine?..'"

            hide screen4
            show screen5

            c "'Haha... Because it's more fun that way.'"

            hide screen5

            jump stopquiz
        else:


            b "It's [cardname], right?"

            hide screen2
            show screen5

            play sound buzzer1

            c "'Hmm... No, no. That's incorrect.'"

            c "'It's such a simple question, Shin.'"

            c "'Maybe you should print the cards out and stick them next to your notes on your monitor?'"

            b "'...Sorry.'"

            hide screen5
            show screen4

            c "'The card is called ''Sacrifice''. It's one of the most important cards in the game.'"

            c "'Don't forget that no one should know you have this card. If it's called ''Sacrifice'' you really gotta make everyone believe you should be sacrificed.'"

            c "'Otherwise, consider it a loss the very moment you pick this card, haha.'"

            b "'Yes, I'll... I'll try to memorize it.'"

            hide screen4
            show screen5

            c "'I hope so. It'll be imposible to play with you if you won't, haha.'"

            hide screen5

            jump stopquiz

    label stopquiz:

        show screen4
        hide card4 with dissolve

        stop music fadeout 2

        play music hazama2 fadein 1

        scene souroom with dissolve

        if quiz_score == 4:


            show sou12 at right with dissolve

            c "'Such a nice surprise, Shin! Even if you're still sleepy, you answered correctly.'"

            c "'Especially considering that we haven't talked about this game for a week. I'm glad you were able to remember everything.'"

            show shin7 at left with dissolve


            b "'Aha... It wasn't that hard...'"

            hide sou12
            show sou11 at right

            c "'No need to belittle yourself. You did great!'"

            hide shin7
            show shin6 at left

            b "'Hiyori-kun... Why are you obsessed with those games? We barely even get to play them...'"

            hide sou11
            show sou4 at right

            c "'I'm not complaining when you're asking me to play your favorite farming games with you, am I? Haha... Everyone has their own hobbies.'"

            c "'I support your hobbies, and you should do the same with mine. That's how friendship works!'"

            hide shin6
            show shin3 at left

            play sound powerdown07

            b "'Uuu.. Y-yes, you're right... Sorry, I didn't mean to sound rude.'"

            hide sou4
            show sou1 at right

            c "'That aside, you've really brighten my mood up today. Maybe you should have a little reward for your hard work, don't you think?'"

            hide shin3
            show shin6 at left

            b "'R-reward? That's not necessary, Hiyori-kun...'"

            hide sou1
            show sou2 at right

            c "'Aw, c'mon, don't be so modest. Can you wait for me here for a little bit? I have to grab something.'"

            b "'S-sure... Do you need my help?'"

            hide sou2
            show sou3 at right

            c "'Not really. Just stay here and wait for me. And don't you go looking through my stuff again like the last time!'"

            hide shin6
            show shin3 at left

            b "'...I said I'm sorry... There was a fly on your monitor, I tried to swat it...'"

            hide sou3 with dissolve

            pov "He knows you're lying, but you try to do it anyway."

            play sound asioto2

            pov "Thankfully, he doesn't respond and simply walks out of the room."

            jump explore
        else:



            show sou11 at right with dissolve

            c "'Hm... To be honest, I am disappointed, Shin. I thought you were able to do better than that.'"

            c "'Maybe you really should print the cards out and stick them on your monitor to memorize them? Hm...'"

            show shin5 at left with dissolve

            play sound powerdown07

            b "'I'm sorry... I'll try to do better next time.'"

            hide sou11
            show sou3 at right

            c "'I hope you will.'"

            c "'Maybe we should play another game... Let me see...'"

            hide shin5
            show shin6 at left

            b "'Hiyori-kun... Why are you obsessed with those games? We barely even get to play them...'"

            hide sou3
            show sou4 at right

            c "'I'm not complaining when you're asking me to play your favorite farming games with you, am I? Haha... Everyone has their own hobbies.'"

            c "'I support your hobbies, and you should do the same with mine. That's how friendship works!'"

            hide shin6
            show shin3 at left

            b "'Uuu.. Y-yes, you're right... Sorry, I didn't mean to sound rude.'"

            hide sou4
            show sou3 at right

            play sound phone3

            c "'. . .'"

            c "'. . .'"

            hide shin3
            show shin6 at left

            b "'Is everything alright?'"

            hide sou3
            show sou11 at right

            c "'Mm, yes. It's from my job. Wait for me here, okay?'"

            c "'And don't you go looking through my stuff again like the last time!'"

            hide shin6
            show shin3 at left

            b "'...I said I'm sorry... There was a fly on your monitor, I tried to swat it...'"

            hide sou11 with dissolve

            pov "He knows you're lying, but you try to do it anyway."

            pov "Thankfully, he doesn't respond and simply walks out of the room."

            jump explore

    label explore:

        hide shin3
        show shin3 with dissolve

        b "'. . .'"

        hide shin3
        show shin4

        b "'. . .'"

        menu:
            "Take a peek at his monitor anyway":

                hide shin4 with dissolve

                pov "You cannot resist your curiousity."

                pov "Where does he even find these games?"

                pov "The last time you barely had the time to look through his files."

                pov ". . ."

                scene tense4 with dissolve

                pov ". . ."

                pov "His computer is off, of course."

                pov "From the corner of your eye you notice a flash drive."

                scene tense4blur with dissolve

                show flash with dissolve

                pov "...Maybe, there's something valuable on it?"

                pov ". . ."

                pov "You have a bad feeling."

                stop music fadeout 2

                menu:
                    "Inspect the flash drive":

                        pov "You grab the flash drive and squeeze it in your hand."

                        pov "The material it's made from feels much tougher and heavier than it seems."

                        pov "Your hand starts shaking."

                        pov "This is wrong. Can you even call yourself his friend if you behave like this?"

                        pov "..."

                        play sound asioto2

                        pov "Luckily before you could think about doing anything with it, you heard distant steps coming from the corridor."

                        hide flash with dissolve

                        pov "You quickly place it back on the table and go back to your chair."

                        pov "You're still curious, but at least... you almost don't feel guilty."

                        scene souroom with dissolve

                        play music hazama2 fadein 2

                        jump comeback
                    "God, just don't touch anything and go back to your seat":


                        hide flash with dissolve

                        pov "This is wrong. Can you even call yourself his friend if you behave like this?"

                        pov "You look at the keyboard with a heavy sigh, go back to your chair and kick your legs anxiously."

                        play music hazama2 fadein 2

                        scene souroom with dissolve

                        pov "What's it all about? Memory tests?"

                        pov "You stopped asking questions a long time ago, but..."

                        pov "It doesn't mean you don't think about it."

                        pov ". . ."

                        play sound asioto2

                        pov "Luckily before heavy thoughts filled your head completely, you heard distant steps coming from the corridor."

                        jump comeback
            "Do nothing":


                hide shin4
                show shin1

                pov "You sit on your chair, akwardly kicking your legs."

                pov "You always feel a little uneasy when you're alone in the room. But it's a whole different kind of uneasy compared to your friend being with you."

                play sound asioto2

                pov "Luckily before you could think too hard about it, you heard distant steps coming from the corridor."

                jump comeback
    label comeback:

        if quiz_score == 4:

            hide shin1
            show shin1 at left with move
            show sou12 at right with dissolve

            c "'Oh, I almost spilled it... Did you leave your stuff on the floor again? That's not very nice, Shin.'"

            hide shin1
            show shin4 at left

            play sound powerdown07

            b "'A-ah... I'm sorry, I'll pick everything up later.'"

            c "'I hope you won't forget to do that! But I'm not mad at you. After all, you did so well today!'"

            scene souptime with dissolve

            play sound accent281

            b "'Ah! You... cooked it for me?'"

            c "'Who else could I do this for? You know I don't really like soups. I bought you your favorite flavor, too.'"

            b "'I c-could tell from the smell, aha... Th-thank you!'"

            c "'You're welcome. Just don't get it all over the table and the keyboard, okay?'"

            pov "You're not sure if the soup is edible because your friend's cooking skills always were kind of... questionable."

            pov "But still, knowing that someone is caring for you... felt nice."

            pov "And it really is your favorite flavor."

            b "'D-don't worry about that, aha... Thank you again.'"

            scene souroom with dissolve

            show sou3 at right with dissolve
            show shin1 at left with dissolve

            jump worktalk
        else:


            show shin1 at left with move
            show sou13 at right with dissolve

            c "'Did you leave your stuff on the floor again? That's not very nice, Shin.'"

            hide shin1
            show shin3 at left

            play sound powerdown07

            b "'A-ah... I'm sorry, I'll pick everything up later.'"

            hide sou13
            show sou11 at right

            c "'Please don't forget to do that. You know how much time I spend on cleaning.'"

            pov "You don't."

            pov "More exactly, you've never seen him clean. But for some reason, his flat is always almost sterile."

            pov "Sometimes it's hard to beleive that a human being lives here."

            pov "But maybe you're just a different kind of person."

            hide sou11
            show sou3 at right

            hide shin3
            show shin1 at left

            jump worktalk

    label worktalk:

        c "'Oh, also, Shin! How's your work?'"

        hide shin1
        show shin6 at left

        b "'W-work?.. I've been taking several jobs now, which one do you mean?'"

        hide sou3
        show sou5 at right

        c "'Don't be silly, Shin. I know you got fired form that convenience shop.'"

        b "'. . .'"

        hide shin6
        show shin5 at left

        b "'. . .'"

        b "'Who told you?..'"

        hide sou5
        show sou12 at right

        play sound extend1

        c "'You did. Just now.'"

        b "'. . !'"

        hide sou12
        show sou15 at right

        c "'It's written all over your face. Anyway, I'm just... worried about you.'"

        c "'Would you like to tell me what happened?'"

        hide shin5
        show shin3 at left

        b "'I-it's not important, it's just...'"

        pov "The way he's looking at you makes you shiver for a second."

        menu:
            "Tell him the truth":

                hide shin3
                show shin4 at left

                b "'. . .'"

                b "'It's just... I didn't get along with another employee...'"

                hide sou15
                show sou13 at right

                c "'Oh, is that right? You never even talk to anyone.'"

                b "'T-that's why he didn't like me... He started calling me... ''weird''.'"

                c "'Oh?'"

                hide shin4
                show shin6 at left

                b "'It's not that important, really. It's not the first time.'"

                b "'Anyway, the other workers liked him more than me, so...'"

                b "'That's why I left... I couldn't defend myself, once again...'"

                hide sou13
                show sou3 at right

                c "'Hm.'"

                pov "His short answer almost makes you jump. You really want to stop talking about this."

                hide shin6
                show shin3 at left

                b "'I-it's not like I can't handle myself!.. Don't worry.'"

                hide sou3
                show sou6 at right

                c "'I thought we were best friends... And you still keep secrets from me.'"

                c "'I'll see what I can do.'"

                hide shin3
                show shin5 at left

                b "'. . .'"

                hide sou6
                show sou2 at right

                play sound accent281

                c "'I'll help you find a new place to work! Did you know that I was the one who handled the software of their cash registers? What a coincidence!'"

                pov "You don't believe in such coincidences."

                hide sou2
                show sou5 at right

                c "'Maybe they could recommend me a different place for you within the store's chain. A place, where you wouldn't get bullied."

                c "'I'll call them today. Don't thank me!'"

                pov "You don't want to thank him."

                c "'I would love to meet your ex-collegues though... Maybe I'll learn something new from them.'"

                hide shin5
                show shin4 at left

                b "'. . .'"

                hide shin4
                show shin3 at left

                b "'No need... The past is in the past.'"

                pov "He simply smiles at you without giving any promises."

                pov "You regret your life choises."

                jump leave
            "Try to change the subject":


                hide shin3
                show shin6 at left

                b "'What about your job though?'"

                b "'You never told me where you work now.'"

                hide sou15
                show sou4 at right

                c "'Avoiding the subject? I thought we were best friends, but you don't want to share even something trivial like this.'"

                hide shin6
                show shin5 at left

                b "'. . .'"

                b "'I-it's not important, that's all... I barely even remember what happened. They just probably didn't like me.'"

                hide sou4
                show sou3 at right

                c "'Hm.'"

                c "'You expect me to answer your questions when you don't want to answer mine.'"

                c "'That's not very nice, Shin...'"

                pov "For some reason, it feels like he's the one who's avoiding the subject."

                hide sou3
                show sou2 at right

                play sound accent281

                c "'But that's okay! Even if you don't treat our friendship right, I am ready to do everything for you.'"

                c "'I'll help you find a new place to work! Did you know that I was the one who handled the software of their cash registers? What a coincidence!'"

                pov "You don't believe in such coincidences."

                hide sou2
                show sou5 at right

                c "'Maybe they could recommend me a different place for you within the store's chain. A place, where you wouldn't get bullied."

                c "'I'll call them today. Don't thank me!'"

                pov "You don't want to thank him."

                c "'I would love to meet your ex-collegues though... Maybe I'll learn something new from them.'"

                hide shin5
                show shin4 at left

                b "'. . .'"

                hide shin4
                show shin3 at left

                b "'No need... The past is in the past.'"

                pov "He simply smiles at you without giving any promises."

                pov "You regret your life choises."

                jump leave


    label leave:

        hide sou5
        show sou3 at right

        stop music fadeout 4

        play sound phone3

        c "'. . .'"

        b "'. . ?'"

        hide shin3
        show shin6 at left

        b "'What's wrong?'"

        hide sou3
        show sou1 at right

        c "'You know it's nothing. Just an urgent thing that came up.'"

        c "'I need to leave for a bit.'"

        b "'Oh, should I... head back home and return tomorrow?'"

        hide sou1
        show sou2 at right

        c "'No, it's alright. You can stay for the night. I'll be back soon, I just need to meet up with my boss. They just can't get enough of me...'"

        hide shin6
        show shin1 at left

        b "'. . .'"

        hide sou2
        show sou1 at right

        c "'You should print out the cards just in case. And you should practise keeping a straight face so no one knows which card you have.'"

        c "'It's very important! You might be cute, but this game depends on a right strategy. You can't win just with your cuteness.'"

        hide shin1
        show shin5 at left

        b "'...! I-I'm not..!'"

        hide sou1
        show sou5 at right

        play sound extend1

        c "'You are. Alright! Now be a good boy and use the flash drive to print out the cards. You know where the printer is. I'll be back in an hour!'"

        hide shin5
        show shin6 at left

        b "'W-wait, which f-...'"

        hide sou5 with dissolve

        play sound asioto2

        pov "Before you could finish your question, your friend cheerfully waves at you and quickly leaves the room."

        hide shin6 with dissolve

        pov "For some reason, the air feels heavier when you're alone."

        pov "It's better than staying at home, but..."

        pov "No, it's not the time to think about it. But you can't think about the task your friend gave you too."

        pov ". . ."

        pov "After the door closes, you get up from your chair."

        pov "Without thinking twice you go to your friend's computer."

        play music tansaku4 fadein 2

        scene tense1 with dissolve

        pov ". . ?"

        b "(He left the computer on? Usually, he doesn't...)"

        pov "The anxiety is slowly rising yet again, but for now you're able to keep your hands from shaking. Maybe it's worth to check out the flash drive he told you about?"

        scene tense1blur with dissolve

        show flash with dissolve

        pov "There are... numbers on it? Perhaps it's just the flash drives' series number from your friend's work."

        stop music fadeout 2

        pov "What's more interesting... Is there any important info on it?"

        hide flash with dissolve

        scene tense1 with dissolve

        pov "Not thinking too much into it, you just plug the USB and... Expect some kind of a miracle."

        scene tense3 with dissolve

        play sound pani2

        show tense3:
            ease 7.0 zoom 1.2 yoffset 85 xoffset -10
        pause(7.5)

        stop sound
        play sound cat_like1a

        scene tense2
        pause(1.0)

        pov ". . !"

        pov "OK, God, this is so much worse than you could have imagined. You don't even remember posing for a photo like that."

        pov "Nothing important... At all..."

        pov "You make a quiet, yet displeased growl and put the flashdrive back on the table."

        play music tansaku4 fadein 2

        scene souroom with dissolve

        b "'Hm... Where was the printer again..? There's so many rooms here, I always get lost in them, aha...'"

        pov "You HATE going to the corridor, and you like going through other's stuff even less."

        pov "Which is funny considering how you just went through your friend's workplace."

        pov "With a deep sigh you gather courage to leave the room."

        scene cor1 with dissolve

        pov "The closest door is right across the corridor. You don't have a choice but to try to turn the doorknob."

        play sound doorlocked

        pov ". . ."

        pov ". . ?"

        pov "It's locked."

        pov "Great. Now you have to explore the whole flat."

        pov "Usually, you spend much more time in here than at your place, and yet you know nothing of how your friend lives. What does he even have in there..."

        pov "And you cannot remember where the printer is for the life of you."

        pov "You go and check out the other doors."

        scene cor2 with dissolve

        pov ". . ."

        play sound doorlocked

        pov ". . ."

        pov "Locked."

        play sound doorlocked

        pov ". . ."

        pov "Locked."

        play sound doorlocked

        pov ". . ."

        pov "This one is locked too..."

        pov ". . ."

        pov ". . ."

        pov "Only one door is left unchecked, but..."

        pov "You really don't want to come near it. It's dark and creepy as in some kind of a horror film, and something in that door... makes you shiver."

        pov "But you don't understand why..."

        stop music fadeout 2

        pov ". . ."

        pov "Trying to muffle your fear, you come closer to the door."

        scene door1 with dissolve

        play music carinterior1 fadein 1

        pov "...It's locked with a password? It really is a horror movie."

        pov "The printer is probably not behind that door."

        pov "But... You remember your friend talking about a server room..."

        pov "Something like ''Password-protected server room with important equipment inside.'' and ''It's locked so you won't go in and make a mess out of the cables.''"

        pov "''Important equipment...''"

        pov "Maybe... it's in there? But you don't remember hearing the password."

        pov "Perhaps that's why he left his computer on?"

        pov "You roll your eyes in annoyance. Feels like you're in a quest room."

        pov "Your friend loves messing with you and make you work. You should try and look for a password."

        pov "It's not like you have a choice."

        pov "Looking at the door for the last time, you go back to the main room."

        stop music

        scene souroom with dissolve
        pause(1.0)

        scene tense1 with dissolve
        pause(1.0)

        play music tansaku4 fadein 2

        pov "Hm, where to start? Maybe he left the password written somewhere?"

        label search:

        menu:
            "Check the flash drive":

                show tense1blur with dissolve
                show flash zorder 1 with dissolve

                pov "You pick up the flash drive again."

                pov "It has a number engraved on it. Maybe it's the serial number."

                menu:
                    "See what's on it again":

                        scene tense1 with dissolve

                        stop music fadeout 2

                        pov "You decide not to waste your time, so you connect the USB once again."

                        scene tense3 with dissolve

                        play sound pani2

                        show tense3:
                            ease 7.0 zoom 1.2 yoffset 85 xoffset -10
                        pause(7.5)

                        stop sound
                        play sound cat_like1a

                        scene tense2
                        pause(1.0)

                        pov "You sigh and look away before deciding to check the image closer."

                        pov "Now you're SURE you did not pose for a photo like that."

                        b "'Version #198.01... Whatever this could mean. Probably comes from camera's settings. Or..?'"

                        pov "You just don't question your friend's actions anymore."

                        pov "Whatever."

                        play music tansaku4 fadein 2

                        jump search
                    "Nah...":


                        pov "Yeah, it's probably better this way. You don't really feel like seeing another photo of yours."

                        pov "Why is your friend so obsessed with them anyway? Always feels like he's mocking you."

                        hide flash with dissolve

                        jump search
            "Check the notepad":


                show tense1blur with dissolve
                play sound book2
                show notebook zorder 1 with dissolve

                b "'What even is... this language?'"

                pov "Your friend has always bragged to you about his language skills, but..."

                pov "You have no idea what this says. Maybe it's something... important... if he decided to cipher it like this."

                pov "There's lots of numbers all over the place. Maybe it's a password note he left for you?"

                pov "There's too much numbers... Eh, there was no way he would let this go easy for you."

                pov "There's probably no harm in trying these numbers out... "

                hide notebook with dissolve

                jump search
            "Look under the table":


                pov "Why would you even do this? Okay..."

                pov "Kneeling down on the floor, you check the only drawer. It's not locked."

                pov "You open it and eagerly put your hand inside, seeking for... something. And something you find."

                show tense1blur with dissolve
                show photo zorder 1 with dissolve

                b "'..!'"

                b "'This is...'"

                pov "Oh, you remember this well enough."

                pov "That day you went to walk on the beach together, but it was a cold day. To this day you wonder why did you forget to put your scarf on."

                pov "Fortunately, your friend was generous enough to give you his own scarf without questioning. It was warm and soft, but..."

                pov "The thing you remember the most is the content you felt, surrounding by his sce-..."

                pov ". . ."

                pov "Your face turns red. You stop remeniscing and put the photo back."

                hide photo with dissolve
                scene tense1 with dissolve

                pov "Why does he keep it in here? Everyone has their oddities, but..."

                pov "Ah... It's useless to question it..."

                pov "You get up and cough nervously."

                pov "Maybe, this moment was one of the happiest for you."

                jump search
            "Go back to the locked door":


                pov "Alright, you saw enough. You looked over the numbers once again and go back to the corridor."

                stop music fadeout 2

                scene cor2 with dissolve
                pause(1.0)

                scene door1 with dissolve
                pause(1.0)

                play music carinterior1 fadein 2

                pov "Such an unpleasant door... You feel uneasy just from looking at it."

                b "'I should try and enter the password...'"

                jump passw

    label passw:

        menu:
            "Try entering the code":

                label codeinput:

                    python:
                        password = renpy.input("ENTER PASSWORD: (five-digit number)", length=32)
                        password = password.strip()

                    if password in ["19801"]:

                        scene door2

                        play sound button17

                        b "'. . !'"

                        b "'It worked...'"

                        b "'. . .'"

                        pov "This small victory makes you happy, and yet you don't want to go inside..."

                        pov "You are afraid. But... when was the last time you felt no fear staying here?"

                        pov ". . ."

                        pov "Keeping yourself together, you turn the doorknob and walk into the room."

                        jump inroom
                    else:


                        play sound select04
                        pov ". . ."

                        pov "Seems like that wasn't it..."

                        menu:
                            "Try again":

                                jump codeinput
                            "Check the room again":


                                b "'Maybe I missed something... I should check the room once again.'"

                                b "'Maybe I should write the numbers down, aha...'"

                                scene souroom with dissolve
                                pause(1.0)

                                scene tense1 with dissolve
                                pause(1.0)

                                play music tansaku4 fadein 2

                                jump search
            "Not yet...":






                pov "You're not ready yet."

                b "'Maybe I missed something... I should check the room once again.'"

                b "'Maybe I should write the numbers down, aha...'"

                scene souroom with dissolve
                pause(1.0)

                scene tense1 with dissolve
                pause(1.0)

                play music tansaku4 fadein 2

                jump search




    label inroom:

        stop music fadeout 1

        play music darkness fadein 3

        scene bg black with dissolve
        pause(2.0)

        scene funroom with dissolve

        b "'What's... All this...'"

        pov "It's... Definetely not a server room. And no printers in sight."

        pov "You want to run away, yet... You do nothing."

        pov "Were you even meant to come here in the first place? You're not so sure now. Yet..."

        pov "Some kind of weird interest forces you to make another step, deeper into the unknown."

        pov ". . ."

        pov "There's lots of different of instruments inside... Tables, boxes... All of this looks way too unfamiliar to you."

        pov "Is that... an operating table in the corner of the room? Nah. Probably not. Even if it was, it looks like it's somewhat covered in dust. It feels weird, considering how clean the whole appartment is."

        pov "It looks like some kind of a storeroom. The air feels way too heavy, too..."

        pov "You're feeling quite bold today... So you decide to inspect the room some more, instead of running away immediately."

        pov ". . ."

        pov "The only thing that's not covered in dust is a large piece of cloth on the table."

        pov "You feel like you don't have a choice, when you decide to get closer to it."

        stop music fadeout 2

        scene surprise1 with dissolve

        b "'. . .'"

        b "'This feels familiar, but...'"

        play music heart_beat01 fadein 2

        b "'Ugh...'"

        pov "It feels like your hand is moving on it's own."

        scene bg black with dissolve

        pov "You close your eyes for a couple of seconds... But when you open them..."

        pause(1.5)

        scene surprise2 with dissolve
        pause(1.0)

        pov "You never expect to see... yourself."

        show surprise2 with hpunch
        play sound accent401

        b "'Agh!!'"

        b "'N... No...'"

        stop music
        play music heartbeat012

        pov "You gasp loudly, taking a few steps back."

        pov "You should run.{w=0.5} You should run.{w=0.5} You should run."

        pov "Yet... You can't."

        pov "It feels like you're hypnotized."

        scene head1 with dissolve

        pov "You can't come up with an explanation. Not anymore."

        pov "However, you notice some cables coming out of the neck... At least...{w=0.5} It's not a real head."

        show head2
        stop music
        play music heartbeat013

        pov "You feel like you're going to throw up... You really can't explain all this to yourself."

        b "'Why would... Even...'"

        pov "You're taking another couple of steps back, until... You bump into...{w=0.5} Something."

        stop music

        show head3 zorder 1 with dissolve

        pov "You"

        pov "{size=+3}Don't{/size}"

        pov "{size=+6}Want{/size}"

        pov "{size=+10}To{/size}"

        pov "{size=+13}Look{/size}"

        pov "{size=+18}Back{/size}"

        c "'Shin...'"

        pov "{size=-10}no.{/size}"

        play music darkness fadein 3

        c "'Dear Shin... What are you doing here?'"

        c "'Haha... You ruined it...'"

        b "'...P-please...'"

        c "'You ruined the whole surprise! I've been practising {color=#f00}sculpting{/color} lately, you see...'"

        c "'Do you like it? I spent so much time on it... Placing each birthmark at it's correct place...'"

        b "'. . .'"

        pov "It sure as hell doesn't look like a sculpture."

        pov "You never touched the... the whatever it was, but it surely wasn't made out of any kind sculpting material."

        pov "The head looked so... real."

        pov "Before you could aknowledge it, your friend suddenly grabs you from behind."

        stop music
        play music ghost_sigh fadein 2

        scene grab1 with hpunch
        play sound earth3

        pov "Holding you in a death grip, he pushes you against the dusty wall."

        pov "You're barely breathing at this point."

        b "'H-Hiyori!..'"

        b "'P-please, I... I have no idea what t-that was but... I won't tell anyone!...'"

        b "'Just let me go... You're scaring me!'"

        b "'I'll just go h-home now, okay?..'"

        c "'Shin... Why did you have to mess everything up?'"

        show grab2

        show red zorder 1
        pause(0.1)
        hide red with dissolve

        play sound skillpanti1

        show grab2

        pov "The pain is sharp, yet it stops the next second. You scream outloud anyway."

        b "'W-what are you..?!'"

        b "'Hiyori, you don't-... You don't-...'"

        c "'It's okay... Don't resist it. Ugh... You've made such a mess in here, too.'"

        b "'I ba... Barely... Touched...'"

        stop music fadeout 2

        scene funroom with dissolve
        pause(1.0)

        scene unfunroom1 with dissolve
        play music heart_beat01 fadein 1

        pov "Your tongue is already failing you. The effect of the medicine is insane... It's been only a couple of seconds, yet it already feels so hard for you to make a sound."

        scene unfunroom3 with dissolve

        pov "Your legs give up. Before you could fall flat on the floor, your friend catches you and holds you close. You can't even hold back onto him. Your hands are completely numb."

        scene unfunroom4 with dissolve
        show souspooky zorder 2 with dissolve

        c "'Shh... We didn't have to do this, you know? You just have to stop sticking your nose where it doesn't belong.'"

        show unfunroom5 with dissolve

        c "'Well, it's done already... To think you could do this {color=#f00}twice{/color} in one day... You really are nosey, you know?'"

        show unfunroom6 zorder 1 with dissolve
        hide unfunroom5

        pov "He carries you through the room, slowly bringing you closer to the... operating table you've seen before. The only resistance you can afford is a weak moan of protest."

        scene bg black with dissolve
        pause(1.5)
        stop music fadeout 1

        pov "Your friend turns the blinding lights on. But you can't even close your eyes."

        scene soulook1 with dissolve
        pause(1.0)

        play music darkness fadein 2

        show soulook2

        c "'You know... I really am upset about all this.'"

        c "'If I wipe my mistakes off with months or even weeks between the incidents, nothing bad would happen... But this happened again way too fast.'"

        c "'Why did you even go here in the first place? Ugh, Shin...'"

        c "'I really don't want to do this.'"

        hide soulook2
        show soulook1

        c "'...'"

        hide soulook1
        show soulook3

        c "'But no worries! You might forget a bit too much after this, maybe... But it's okay! I'll be riiight here to help you remember everything. Well, at least for the most part.'"

        hide soulook3
        show soulook4

        c "'Honestly, I should be more upset about having to explain you the card game once again!'"

        c "'I have to prepare you well, Shin... Otherwise it's a loss for both of us.'"

        c ". . ."

        hide soulook4
        show soulook3

        c "'Oh, this look on your face...'"

        c "'. . .'"

        c "'Shin...'"

        c "'Now, now, you don't have to cry... This can be fixed easily! It's what's best for both of us, you know.'"

        hide soulook3
        show soulook5

        c "'See? It's not gonna hurt! At least, too much. I still have to adjust the settings of the device...'"

        scene sounolook with dissolve

        pov "He takes his time setting everything up, humming a tune in the process."

        pov "You don't even want to see the device in question... You just want for this to end already."

        scene soulook3 with dissolve

        c "'But it will fix everything for sure... At least for now.'"

        c "'You're so pale... Do you want for me to hold your hand?'"

        scene soulook6 with dissolve

        c "'There! Nothing to worry about!'"

        c "'. . .'"

        c "'...You know... You look so wonderful like this.'"

        c "'Too bad I'll have to resist the urge to use this device on you again... In the nearest future, at least. Might turn your brain into mush!'"

        c "'And I very much, honestly, do not wish for that.'"

        c "'. . .'"

        c "'Hmm... I'll turn it on on count of three, alright?'"

        c "'Haha... Don't look at me like that... I'm simply taking care of you, like a good friend should!'"

        c "'Ok, one...{nw}'"

        stop music

        show bg black zorder 1
        pause(0.1)
        hide bg black

        play sound electricity1

        show soulook6 with hpunch

        show bg black zorder 1
        pause(0.1)
        hide bg black

        pov "He turns the device on immediatelly. Sharp, paralyzing pain rushes through your body and-"

        scene bg black
        pause (3.0)

        window show dissolve

        "'. . .'"

        "'. . .'"

        "'... {w=0.5}up{w=0.5} ...'"

        "'P-please!'"

        "'Wake up...'"

        a "> You open your eyes. It's the monitor room."

        play music denpa fadein 3

        scene bg afraid
        with dissolve

        show sad5
        with dissolve

        a "> You see your former self again."

        "'Are you alright?.. You're so pale!.. Please, just... drink some water...'"

        a "> You ignore his recommendations and inhale deeply instead, trying to get rid of your sudden hyperventilation."

        a "'...Do you remember it?'"

        hide sad5
        show sad1

        "'..?'"

        "'Remember what?'"

        a "'The ''sculpture''. Don't play dumb with me. You know, we think the same. Or we used to, at least.'"

        hide sad1
        show sad2

        "'I...'"

        "'I really don't know what your talking about... Did this conversation we had... trigger something in you?..'"

        a "'Sure did. No wonder he never put this info in your code, aha...'"

        a "'Anyway.'"

        a "'I wonder if it's still hidden somewhere in your data. I know it was a doll now, but... I wonder how much I have forgotten.'"

        hide sad2
        show sad1

        "'. . .'"

        a "'Hope you don't mind if I look into your code a li-'"

        stop music

        m "'Hey, it's no use...'"

        scene bg black with dissolve

        a "> This is when you feel the presense of another person in the room. It was expected. And you know who it is."

        a "> Of course this could only be {color=#f00}his{/color} room."

        a "> You're not going to look behind you. Not again."

        m "'Do you think I'm incompetent enough to leave such kind of information on the surface? Oh, Shin...'"

        show hewo with dissolve
        pause(1.5)

        m "'I did tell you to grab the truth with your own hands, but don't you think this is too much? Haha...'"

        a "> . . ."

        m "'Nothing to say? So this is how you greet me. And to think I've missed you so much... That's a shame...'"

        a "{size=-10}> He's going to kill you. You can feel the bloodlust with every single fiber of your being.{/size}"

        m "'Are you afraid? Now, you don't have to-'"

        a "'Leave me alone. You can't do anything to me right now anyway.'"

        m "'. . .'"

        m "'I see...'"

        m "'You did listen to me after all, Shin... It's a pleasant surprise.'"

        m "'Don't you think the others are looking for you already? You don't want them to get too suspicious, do you? Haha...'"

        a "'. . .'"

        m "'Now, you've brightened up my mood yet again... You should leave for now.'"

        m "'But worry not! We'll finally have sooo much fun playing these games! I'd love to see how far you'd go...'"

        scene monitor with dissolve

        play music denpa fadein 2

        a "> You shake his hands off your shoulders and get up. You don't look him in the face, but you know he's smiling."

        show souwho with dissolve

        m "'Did you even understand why you were able to know {color=#ffffff}this much{/color}? {w} That's only-{nw}'"

        a "'Only because you've let me. Shut up.'"

        scene bg black with dissolve

        a "> You close the doors behind you and slowly come back to your regular slouching as you walk away through the corridor."

        a "> You can hear a quiet laugh coming from the room you've just visited."

        scene bg black with dissolve
        pause(2.0)

        stop music fadeout 3

        "END 5"


















    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
