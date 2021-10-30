













define config.name = _("Shin AI\n Talk Sim")





define gui.show_name = True




define config.version = "1.0"





define gui.about = _p("""CONTENT WARNING:

loud sound (may occur)

sound of a heartbeat

description of being watched/stalked


This game doesn't contain any jumpscares, gore, nor any other dark topics.


This game was made by @letsdrawkittens/@DepressionHole, who did the programming; and @wetmango69, who did the visuals.


For more detailed info, please, read README(CW,+guide-ish).txt
""")






define build.name = "ShinAITalkSim"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True















python:
    preferences.set_volume('music', 0.5)
    preferences.set_volume('sound', 0.5)
    renpy.restart_interaction()










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 50





default preferences.afm_time = 15
















define config.save_directory = "shingame-1631912977"






define config.window_icon = "gui/window_icon.png"

define config.hard_rollback_limit = 1






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)









    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
