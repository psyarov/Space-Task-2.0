from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np 
from numpy import (sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os
import sys
import psychopy.iohub as io
from psychopy.hardware import keyboard
import random
from random import shuffle
from Parameters import common_params
from component_init import components_init

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def prob(main):
    # prepare
    if main.lang_keys.keys == 'e':
        instr='It is not guaranteed that space crystals can be found every time on a given planet.\n\nThroughout the block, if the signal strength for the right planet is higher more often, the space crystals are more likely to be found on the right planet (and less likely to be found on the left planet).\n\n'
    else:
        instr='Im Folgenden ist es leider nicht garantiert, dass es auf einem Planeten jedes mal Kristalle zu finden sind.\n\n Wenn die Signalstärke für den rechten Planeten während eines Blocks häufiger höher ist, ist es wahrscheinlicher, dass die Weltraumkristalle auf dem rechten Planeten sind (und weniger wahrscheinlich auf dem linken Planeten).\n\n'
    main.text_33.setText(instr)

    if main.lang_keys.keys == 'e':
        arrow_more = 'more likely'
    else:
        arrow_more = 'wahrscheinlicher'
    main.more_text.setText(arrow_more)

    if main.lang_keys.keys == 'e':
        arrow_less = 'less likely'
    else:
        arrow_less = 'weniger wahrscheinlich'
    main.less_text.setText(arrow_less)
    main.proceed_23.keys = []
    main.proceed_23.rt = []
    main._proceed_23_allKeys = []
    main.mu_4.reset()
    main.planet_left_10.setImage('resources/blue_blur.png')
    main.planet_right_10.setPos((0.4, 0.4))
    main.planet_right_10.setImage('resources/green_blur.png')
    main.arrow_left_6.setImage('resources/arrow_diag.png')
    main.arrow_right_6.setImage('resources/arrow_diag.png')
    main.prob_components = [main.space_bg_23, main.text_33, main.proceed_23, main.mu_4, main.shuttle_9, main.planet_left_10, main.planet_right_10, main.arrow_left_6, main.arrow_right_6, main.less_text, main.more_text]
    main.prob_components = main.prepare_routine(main.prob_components)
    
    # run
    while main.continueRoutine:
        main.timing.get_current_time(main.routineTimer, main)
        main.frameN = main.frameN + 1
        main.space_bg_23 = main.components.text_or_image_update(main.space_bg_23, 'space_bg_23.started', main)
        main.text_33 = main.components.text_or_image_update(main.text_33, 'text_33.started', main)
        main.more_text = main.components.text_or_image_update(main.more_text, 'more_text.started', main)
        main.less_text = main.components.text_or_image_update(main.less_text, 'less_text.started', main)
        main.waitOnFlip = False
        main.proceed_23, main._proceed_23_allKeys = main.components.keys_update(main.proceed_23, main._proceed_23_allKeys, 'proceed_23.started', main)
        main.shuttle_9 = main.components.text_or_image_update(main.shuttle_9, 'shuttle_9.started', main)
        main.planet_left_10 = main.components.text_or_image_update(main.planet_left_10, 'planet_left_10.started', main)
        main.planet_right_10 = main.components.text_or_image_update(main.planet_right_10, 'planet_right_10.started', main)
        main.arrow_left_6 = main.components.text_or_image_update(main.arrow_left_6, 'arrow_left_6.started', main)
        main.arrow_right_6 = main.components.text_or_image_update(main.arrow_right_6, 'arrow_right_6.started', main)
    
        if main.endExpNow or main.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
        if not main.continueRoutine: main.routineForceEnded = True; break
        main.continueRoutine = False
        main.prob_components = main.components.check_if_components_finished(main.prob_components, main)
        if main.continueRoutine: main.win.flip()
    
    # end
    main.prob_components = main.components.hide_components(main.prob_components)
    main.proceed_23 = main.components.save_key_response(main.proceed_23, 'proceed_23.keys', 'proceed_23.rt', main)
    main.thisExp.nextEntry() # watch out
    main.thisExp.addData('mu_4.response', main.mu_4.getRating())
    main.thisExp.addData('mu_4.rt', main.mu_4.getRT())
    main.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def prob1(main):
    # prepare
    if main.lang_keys.keys == 'e':
        instr= 'Throughout the block, if the signal strength for the left planet is higher more often, the space crystals are more likely to be found on the left planet (and less likely to be found on the right planet).\n\n'
        arrow_more = 'more likely'
        arrow_less = 'less likely'
    else:
        instr= 'Wenn die Signalstärke für den linken Planeten während eines Blocks häufiger höher ist, ist es wahrscheinlicher, dass die Weltraumkristalle auf dem linken Planeten sind (und weniger wahrscheinlich auf dem rechten Planeten).\n\n'
        arrow_more = 'wahrscheinlicher'
        arrow_less = 'weniger wahrscheinlich'
    main.text_35.setText(instr)
    main.more_text1.setText(arrow_more)
    main.less_text1.setText(arrow_less)
    main.proceed_25.keys = []
    main.proceed_25.rt = []
    main._proceed_25_allKeys = []
    main.mu_9.reset()
    main.planet_left_11.setImage('resources/blue_blur.png')
    main.planet_right_11.setPos((0.4, 0.4))
    main.planet_right_11.setImage('resources/green_blur.png')
    main.arrow_left_7.setImage('resources/arrow_diag.png')
    main.arrow_right_7.setImage('resources/arrow_diag.png')
    main.prob1_components = [main.space_bg_24, main.text_35, main.proceed_25, main.mu_9, main.shuttle_10, main.planet_left_11, main.planet_right_11, main.arrow_left_7, main.more_text1, main.less_text1, main.arrow_right_7]
    main.prob1_components = main.prepare_routine(main.prob1_components)
    
    # run
    while main.continueRoutine:
        main.timing.get_current_time(main.routineTimer, main)
        main.frameN = main.frameN + 1
        main.space_bg_24 = main.components.text_or_image_update(main.space_bg_24, 'space_bg_24.started', main)
        main.text_35 = main.components.text_or_image_update(main.text_35, 'text_35.started', main)
        main.more_text1 = main.components.text_or_image_update(main.more_text1, 'more_text1.started', main)
        main.less_text1 = main.components.text_or_image_update(main.less_text1, 'less_text1.started', main)
        main.waitOnFlip = False
        main.proceed_25, main._proceed_25_allKeys = main.components.keys_update(main.proceed_25, main._proceed_25_allKeys, 'proceed_25.started', main)
        main.shuttle_10 = main.components.text_or_image_update(main.shuttle_10, 'shuttle_10.started', main)
        main.planet_left_11 = main.components.text_or_image_update(main.planet_left_11, 'planet_left_11.started', main)
        main.planet_right_11 = main.components.text_or_image_update(main.planet_right_11, 'planet_right_11.started', main)
        main.arrow_left_7 = main.components.text_or_image_update(main.arrow_left_7, 'arrow_left_7.started', main)
        main.arrow_right_7 = main.components.text_or_image_update(main.arrow_right_7, 'arrow_right_7.started', main)
        if main.endExpNow or main.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
        if not main.continueRoutine: main.routineForceEnded = True; break
        main.continueRoutine = False
        main.prob_components = main.components.check_if_components_finished(main.prob_components, main)
        if main.continueRoutine: main.win.flip()
    
    # end
    main.prob1_components = main.components.hide_components(main.prob1_components)
    main.proceed_25 = main.components.save_key_response(main.proceed_25, 'proceed_25.keys', 'proceed_25.rt', main)
    main.thisExp.nextEntry() # watch out
    main.thisExp.addData('mu_9.response', main.mu_9.getRating())
    main.thisExp.addData('mu_9.rt', main.mu_9.getRT())
    main.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def space_slider(main):
    # prepare
    if main.lang_keys.keys == 'e':
        instr='To keep track of the probability, you can use a slider.\n\nFor e.g., in the image above, you have to report what the probability of finding space crystals on the planet on the left is.'
    else:
        instr='Um über die Trials hinweg zu verfolgen, wie hoch die Wahrscheinlichkeit für Kristalle auf einem der Planeten sind, kannst du einen Schieberegler benutzen.\n\nIn der obigen Abbildung musst du z. B. angeben, wie hoch die Wahrscheinlichkeit ist, dass die Astronaut:innen auf dem linken Planeten Weltraumkristalle finden.'
    main.text_4.setText(instr)
    main.mu_3.reset()
    main.planet_right.setPos((0.4, 0.4))
    main.planet_right.setImage('resources/green_blur.png')
    main.planet_left.setImage('resources/blue_blur.png')
    main.arrow_left.setPos((-0.075, 0.25))
    main.arrow_left.setImage('resources/curved_arrow.png')
    main.proceed.keys = []
    main.proceed.rt = []
    main._proceed_allKeys = []
    main.space_slider_components = [main.space_bg_2, main.text_4, main.mu_3, main.shuttle, main.planet_right, main.planet_left, main.arrow_left, main.proceed]
    main.space_slider_components = main.prepare_routine(main.space_slider_components)
    
    # run
    while main.continueRoutine:
        main.timing.get_current_time(main.routineTimer, main)
        main.frameN = main.frameN + 1
        main.space_bg_2 = main.components.text_or_image_update(main.space_bg_2, 'space_bg_2.started', main)
        main.text_4 = main.components.text_or_image_update(main.text_4, 'text_4.started', main)
        main.mu_3 = main.components.text_or_image_update(main.mu_3, 'mu_3.started', main)
        main.shuttle = main.components.text_or_image_update(main.shuttle, 'shuttle.started', main)
        main.planet_right = main.components.text_or_image_update(main.planet_right, 'planet_right.started', main)
        main.planet_left = main.components.text_or_image_update(main.planet_left, 'planet_left.started', main)
        main.arrow_left = main.components.text_or_image_update(main.arrow_left, 'arrow_left.started', main)
        main.waitOnFlip = False
        main.proceed, main._proceed_allKeys = main.components.keys_update(main.proceed, main._proceed_allKeys, 'proceed.started', main)
        if main.endExpNow or main.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
        if not main.continueRoutine: main.routineForceEnded = True; break
        main.continueRoutine = False
        main.space_slider_components = main.components.check_if_components_finished(main.space_slider_components, main)
        if main.continueRoutine: main.win.flip()
    
    # end
    main.space_slider_components = main.components.hide_components(main.space_slider_components)
    main.proceed = main.components.save_key_response(main.proceed, 'proceed.keys', 'proceed.rt', main)
    main.thisExp.nextEntry() # watch out
    main.thisExp.addData('mu_3.response', main.mu_3.getRating())
    main.thisExp.addData('mu_3.rt', main.mu_3.getRT())
    main.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def space_slider2(main):
    # prepare
    if main.lang_keys.keys == 'e':
        instr='Similarly, in the image above, you have to report what you think the probability of finding space crystals on the planet on the right is. \n\n\n'
    else:
        instr='In der obigen Abbildung musst du angeben, wie hoch du die Wahrscheinlichkeit einschätzt, auf dem rechten Planeten Weltraumkristalle zu finden.\n\n\n'
    main.text_6.setText(instr)
    main.planet_right_2.setPos((0.4, 0.4))
    main.planet_right_2.setImage('resources/green_blur.png')
    main.planet_left_2.setImage('resources/blue_blur.png')
    main.arrow_left_2.setPos((0.075, 0.25))
    main.arrow_left_2.setImage('resources/curved_arrow_right.png')
    main.proceed_10.keys = []
    main.proceed_10.rt = []
    main._proceed_10_allKeys = []
    main.mu_8.reset()
    main.space_slider2_components = [main.space_bg_9, main.text_6, main.shuttle_2, main.planet_right_2, main.planet_left_2, main.arrow_left_2, main.proceed_10, main.mu_8]
    main.space_slider2_components = main.prepare_routine(main.space_slider2_components)
    
    # run
    while main.continueRoutine:
        main.timing.get_current_time(main.routineTimer, main)
        main.frameN = main.frameN + 1
        main.space_bg_9 = main.components.text_or_image_update(main.space_bg_9, 'space_bg_9.started', main)
        main.text_6 = main.components.text_or_image_update(main.text_6, 'text_6.started', main)
        main.shuttle_2 = main.components.text_or_image_update(main.shuttle_2, 'shuttle_2.started', main)
        main.planet_right_2 = main.components.text_or_image_update(main.planet_right_2, 'planet_right_2.started', main)
        main.planet_left_2 = main.components.text_or_image_update(main.planet_left_2, 'planet_left_2.started', main)
        main.arrow_left_2 = main.components.text_or_image_update(main.arrow_left_2, 'arrow_left_2.started', main)
        main.mu_8 = main.components.text_or_image_update(main.mu_8, 'mu_8.started', main)
        main.waitOnFlip = False
        main.proceed_10, main._proceed_10_allKeys = main.components.keys_update(main.proceed_10, main._proceed_10_allKeys, 'proceed_10.started', main)
        if main.endExpNow or main.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
        if not main.continueRoutine: main.routineForceEnded = True; break
        main.continueRoutine = False
        main.space_slider2_components = main.components.check_if_components_finished(main.space_slider2_components, main)
        if main.continueRoutine: main.win.flip()
    
    # end
    main.space_slider2_components = main.components.hide_components(main.space_slider2_components)
    main.proceed_10 = main.components.save_key_response(main.proceed_10, 'proceed_10.keys', 'proceed_10.rt', main)
    main.thisExp.nextEntry() # watch out
    main.thisExp.addData('mu_8.response', main.mu_8.getRating())
    main.thisExp.addData('mu_8.rt', main.mu_8.getRT())
    main.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def slider_example(main):
    # prepare
    if main.lang_keys.keys == 'e':
        instr='The image above is an example of using the slider. \n\nFor instance, if you think that the probability of finding space crystals on the left planet is 25 percent, then please use the slider like shown in the image (indicated by the white arrow). \n\nPress SPACEBAR to proceed.\n'
    else:
        instr='Das obige Bild ist ein Beispiel für die Verwendung des Schiebereglers.\n\nWenn du zum Beispiel glaubst, dass die Wahrscheinlichkeit, auf dem linken Planeten Weltraumkristalle zu finden, 25 Prozent beträgt, dann verwende bitte den Schieberegler wie in der Abbildung gezeigt (gekennzeichnet durch den weißen Pfeil).\n\nDrücke die LEERTASTE, um fortzufahren.'
        main.slider_1 = main.slider_ger # maybe problem
    main.text_14.setText(instr)
    main.proceed_11.keys = []
    main.proceed_11.rt = []
    main._proceed_11_allKeys = []
    main.slider_example_components = [main.slider_1, main.proceed_11, main.text_14, main.arrow_4]
    main.slider_example_components = main.prepare_routine(main.slider_example_components)

    # run
    while main.continueRoutine:
        main.timing.get_current_time(main.routineTimer, main)
        main.frameN = main.frameN + 1
        main.slider_1 = main.components.text_or_image_update(main.slider_1, 'slider_1.started', main)
        main.text_14 = main.components.text_or_image_update(main.text_14, 'text_14.started', main)
        main.arrow_4 = main.components.text_or_image_update(main.arrow_4, 'arrow_4.started', main)
        main.waitOnFlip = False
        main.proceed_11, main._proceed_11_allKeys = main.components.keys_update(main.proceed_11, main._proceed_11_allKeys, 'proceed_11.started', main)
        if main.endExpNow or main.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
        if not main.continueRoutine: main.routineForceEnded = True; break
        main.continueRoutine = False
        main.slider_example_components = main.components.check_if_components_finished(main.slider_example_components, main)
        if main.continueRoutine: main.win.flip()

    # end
    main.slider_example_components = main.components.hide_components(main.slider_example_components)
    main.proceed_11 = main.components.save_key_response(main.proceed_11, 'proceed_11.keys', 'proceed_11.rt', main)
    main.thisExp.nextEntry() # watch out
    main.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def slider_example1(main):
    # prepare
    if main.lang_keys.keys == 'e':
        instr='Here is another example.\n\nFor instance, if you think that the probability of finding space crystals on the left planet is 75 percent, then please use the slider like shown in the image (indicated by the white arrow). \n\nPress SPACEBAR to proceed.\n\n'
    else:
        main.instr='Hier ist ein weiteres Beispiel.\n\nWenn du zum Beispiel glaubst, dass die Wahrscheinlichkeit, auf dem linken Planeten Weltraumkristalle zu finden, 75 Prozent beträgt, dann verwende bitte den Schieberegler wie im Bild gezeigt (gekennzeichnet durch den weißen Pfeil).\n\nDrücke die LEERTASTE, um fortzufahren.'
        main.slider_2 = main.slider_2_ger
    main.text_15.setText(instr)
    main.proceed_12.keys = []
    main.proceed_12.rt = []
    main._proceed_12_allKeys = []
    main.slider_example1_components = [main.slider_2, main.proceed_12, main.text_15, main.arrow_5]
    main.slider_example1_components = main.prepare_routine(main.slider_example1_components)
    
    # run
    while main.continueRoutine:
        main.timing.get_current_time(main.routineTimer, main)
        main.frameN = main.frameN + 1
        main.slider_2 = main.components.text_or_image_update(main.slider_2, 'slider_2.started', main)
        main.text_15 = main.components.text_or_image_update(main.text_15, 'text_15.started', main)
        main.arrow_5 = main.components.text_or_image_update(main.arrow_5, 'arrow_5.started', main)
        main.waitOnFlip = False
        main.proceed_12, main._proceed_12_allKeys = main.components.keys_update(main.proceed_12, main._proceed_12_allKeys, 'proceed_12.started', main)
        if main.endExpNow or main.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
        if not main.continueRoutine: main.routineForceEnded = True; break
        main.continueRoutine = False
        main.slider_example1_components = main.components.check_if_components_finished(main.slider_example1_components, main)
        if main.continueRoutine: main.win.flip()
    
    # end
    main.slider_example1_components = main.components.hide_components(main.slider_example1_components)
    main.proceed_12 = main.components.save_key_response(main.proceed_12, 'proceed_12.keys', 'proceed_12.rt', main)
    main.thisExp.nextEntry() # watch out
    main.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def ghost_marker(main):
    # prepare
    if main.lang_keys.keys == 'e':
        instr='After each trial you are going to see a blue marker which indicates your slider update from the last trial. \n\nPress SPACEBAR to proceed.\n'
    else:
        instr='Nach jedem Versuch siehst du eine blaue Markierung, die deine letzte Aktualisierung des Schiebereglers anzeigt. \n\nDrücke die LEERTASTE, um fortzufahren.'
        main.slider_ghost = main.slider_ghost_ger
    main.text_ghost.setText(instr)
    main.proceed_ghost.keys = []
    main.proceed_ghost.rt = []
    main._proceed_ghost_allKeys = []
    main.ghost_marker_components = [main.slider_ghost, main.proceed_ghost, main.text_ghost, main.arrow_ghost]
    main.ghost_marker_components = main.prepare_routine(main.ghost_marker_components)
    
    # run
    while main.continueRoutine:
        main.timing.get_current_time(main.routineTimer, main)
        main.frameN = main.frameN + 1
        main.slider_ghost = main.components.text_or_image_update(main.slider_ghost, 'slider_ghost.started', main)
        main.text_ghost = main.components.text_or_image_update(main.text_ghost, 'text_ghost.started', main)
        main.arrow_ghost = main.components.text_or_image_update(main.arrow_ghost, 'arrow_ghost.started', main)
        main.waitOnFlip = False
        main.proceed_ghost, main._proceed_ghost_allKeys = main.components.keys_update(main.proceed_ghost, main._proceed_ghost_allKeys, 'proceed_ghost.started', main)
        if main.endExpNow or main.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
        if not main.continueRoutine: main.routineForceEnded = True; break
        main.continueRoutine = False
        main.ghost_marker_components = main.components.check_if_components_finished(main.ghost_marker_components, main)
        if main.continueRoutine: main.win.flip()
    
    # end
    main.ghost_marker_components = main.components.hide_components(main.ghost_marker_components)
    main.proceed_ghost = main.components.save_key_response(main.proceed_ghost, 'proceed_ghost.keys', 'proceed_ghost.rt', main)
    main.thisExp.nextEntry() # watch out
    main.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def slider_accuracy(main):
    # prepare
    if main.lang_keys.keys == 'e':
        instr='Please note: It is important to use the slider on trials when you think there is a change in the probability as it is important for your reported probability to come as close to the actual probability of finding space crystals on a given planet.'
    else:
        instr='Es ist wichtig, den Schieberegler bei den Trials zu verwenden, wenn du glaubst, dass sich die Wahrscheinlichkeit verändert hat. Es ist wichtig, dass die von dir gemeldete Wahrscheinlichkeit der tatsächlichen Wahrscheinlichkeit, auf einem bestimmten Planeten Weltraumkristalle zu finden, möglichst nahekommt.'
    main.text_slider_accuracy.setText(instr)
    main.proceed_slider_accuracy.keys = []
    main.proceed_slider_accuracy.rt = []
    main._proceed_slider_accuracy_allKeys = []
    main.slider_accuracy_components = [main.space_bg_slider_accuracy, main.proceed_slider_accuracy, main.text_slider_accuracy]
    main.slider_accuracy_components = main.prepare_routine(main.slider_accuracy_components)
    
    # run
    while main.continueRoutine:
        main.timing.get_current_time(main.routineTimer, main)
        main.frameN = main.frameN + 1
        main.space_bg_slider_accuracy = main.components.text_or_image_update(main.space_bg_slider_accuracy, 'space_bg_slider_accuracy.started', main)
        main.text_slider_accuracy = main.components.text_or_image_update(main.text_slider_accuracy, 'text_slider_accuracy.started', main)
        main.waitOnFlip = False
        main.proceed_slider_accuracy, main._proceed_slider_accuracy_allKeys = main.components.keys_update(main.proceed_slider_accuracy, main._proceed_slider_accuracy_allKeys, 'proceed_slider_accuracy.started', main)
        if main.endExpNow or main.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
        if not main.continueRoutine: main.routineForceEnded = True; break
        main.continueRoutine = False
        main.slider_accuracy_components = main.components.check_if_components_finished(main.slider_accuracy_components, main)
        if main.continueRoutine: main.win.flip()
    
    # end
    main.slider_accuracy_components = main.components.hide_components(main.slider_accuracy_components)
    main.proceed_slider_accuracy = main.components.save_key_response(main.proceed_slider_accuracy, 'proceed_slider_accuracy.keys', 'proceed_slider_accuracy.rt', main)
    main.thisExp.nextEntry() # watch out
    main.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def demo(main):
    # prepare
    if main.lang_keys.keys == 'e':
        instr='To better understand the task, you are now going to see a short video. Please wait for the video to start automatically.\nOnce you have seen and understood the video, press SPACEBAR to proceed.'
    else:
        main.instr='Um dir einen besseren Eindruck der Aufgabe zu geben, siehst du jetzt ein kurzes Video. Bitte warte, bis das Video automatisch startet.\nDrücke die LEERTASTE, um fortzufahren, wenn du fertig bist.'
        main.movie = main.movie_ger
    main.text_34.setText(instr)
    main.proceed_24.keys = []
    main.proceed_24.rt = []
    main._proceed_24_allKeys = []
    main.demo_components = [main.movie, main.text_34, main.proceed_24]
    main.demo_components = main.prepare_routine(main.demo_components)
    
    # run
    while main.continueRoutine:
        main.timing.get_current_time(main.routineTimer, main)
        main.frameN = main.frameN + 1
        main.movie = main.components.text_or_image_update(main.movie, 'movie.started', main)
        main.text_34 = main.components.text_or_image_update(main.text_34, 'text_34.started', main)
        main.waitOnFlip = False
        main.proceed_24, main._proceed_24_allKeys = main.components.keys_update(main.proceed_24, main._proceed_24_allKeys, 'proceed_24.started', main)
        if main.endExpNow or main.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
        if not main.continueRoutine: main.routineForceEnded = True; break
        main.continueRoutine = False
        main.demo_components = main.components.check_if_components_finished(main.demo_components, main)
        if main.continueRoutine: main.win.flip()
    
    # end
    main.demo_components = main.components.hide_components(main.demo_components)
    main.movie.stop()
    main.proceed_24 = main.components.save_key_response(main.proceed_24, 'proceed_24.keys', 'proceed_24.rt', main)
    main.thisExp.nextEntry() # watch out
    main.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def incong_vid(main):
    # prepare
    if main.lang_keys.keys == 'e':
        instr = 'Please note that there will be blocks in the task where you are required to report the probability of finding space crystals on the planet on which the signal indicates that it is less likely to find space crystals. Here is an example video of this scenario. Press SPACEBAR to proceed.'
    else:
        instr = 'Bitte beachte, dass es in der Aufgabe Blöcke geben wird, in denen du die Wahrscheinlichkeit angeben musst, Weltraumkristalle auf dem Planeten zu finden, auf dem das Signal anzeigt, dass es weniger wahrscheinlich ist, Weltraumkristalle zu finden. Hier ist ein Beispielvideo dazu. Drücke die LEERTASTE, um fortzufahren'
    main.text_incong_vid.setText(instr)
    main.proceed_incong.keys = []
    main.proceed_incong.rt = []
    main._proceed_incong_allKeys = []
    main.incong_components = [main.space_incong_vid, main.text_incong_vid, main.proceed_incong]
    main.incong_components = main.prepare_routine(main.incong_components)
    
    # run
    while main.continueRoutine:
        main.timing.get_current_time(main.routineTimer, main)
        main.frameN = main.frameN + 1
        main.space_incong_vid = main.components.text_or_image_update(main.space_incong_vid, 'space_incong_vid.started', main)
        main.text_incong_vid = main.components.text_or_image_update(main.text_incong_vid, 'text_incong_vid.started', main)
        main.waitOnFlip = False
        main.proceed_incong, main._proceed_incong_allKeys = main.components.keys_update(main.proceed_incong, main._proceed_incong_allKeys, 'proceed_incong.started', main)
        if main.endExpNow or main.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
        if not main.continueRoutine: main.routineForceEnded = True; break
        main.continueRoutine = False
        main.incong_components = main.components.check_if_components_finished(main.incong_components, main)
        if main.continueRoutine: main.win.flip()
    
    # end
    main.incong_components = main.components.hide_components(main.incong_components)
    main.proceed_incong = main.components.save_key_response(main.proceed_incong, 'proceed_incong.keys', 'proceed_incong.rt', main)
    main.thisExp.nextEntry() # watch out
    main.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def demo_incong(main):
    # prepare
    if main.lang_keys.keys == 'e':
        instr='Here is another demo of the task. Please wait for the video to start automatically.\nOnce you have seen the video, press SPACEBAR to proceed.'
    else:
        instr='Hier ist noch eine Demo der Aufgabe. Bitte warte, bis das Video automatisch startet. Das Video wird kontinuierlich abgespielt.\nSobald du das Video gesehen und verstanden hast, drücke die LEERTASTE, um fortzufahren.'
        main.movie_2 = main.movie_2_ger
    main.demo_msg.setText(instr)
    main.proceed_26.keys = []
    main.proceed_26.rt = []
    main._proceed_26_allKeys = []
    main.demo_incong_components = [main.movie_2, main.demo_msg, main.proceed_26]
    main.demo_incong_components = main.prepare_routine(main.demo_incong_components)
    
    # run
    while main.continueRoutine:
        main.timing.get_current_time(main.routineTimer, main)
        main.frameN = main.frameN + 1
        main.movie_2 = main.components.text_or_image_update(main.movie_2, 'movie_2.started', main)
        main.demo_msg = main.components.text_or_image_update(main.demo_msg, 'demo_msg.started', main)
        main.waitOnFlip = False
        main.proceed_26, main._proceed_26_allKeys = main.components.keys_update(main.proceed_26, main._proceed_26_allKeys, 'proceed_26.started', main)
        if main.endExpNow or main.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
        if not main.continueRoutine: main.routineForceEnded = True; break
        main.continueRoutine = False
        main.demo_incong_components = main.components.check_if_components_finished(main.demo_incong_components, main)
        if main.continueRoutine: main.win.flip()
    
    # end
    main.demo_incong_components = main.components.hide_components(main.demo_incong_components)
    main.movie_2.stop()
    main.proceed_26 = main.components.save_key_response(main.proceed_26, 'proceed_26.keys', 'proceed_26.rt', main)
    main.thisExp.nextEntry() # watch out
    main.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def choice(main):
    # prepare
    if main.lang_keys.keys == 'e':
        instr='In the next phase, you will advise the astronauts about whether they should fly to the left or the right planet. You need to make this decision based on the analysis of the signals from the radar which you have done throughout the block. Hence, for this purpose, please use the probability of finding space crystals for a given planet that you reported throughout the block.\n\nIf you want to advise the astronauts to go to the left planet, press the LEFT planet. \nIf you want to advise the astronauts to go to the right planet, press the RIGHT planet. '
    else:
        instr='In der nächsten Phase wirst du den Astronaut:innen sagen, ob sie zum linken oder zum rechten Planeten fliegen sollen. Diese Entscheidung musst du auf der Grundlage der Analyse der Radarsignale treffen, die du während des gesamten Blocks durchgeführt hast. Verwende zu diesem Zweck die Wahrscheinlichkeit für Weltraumkristalle auf dem Planeten, die du während des gesamten Blocks angegeben hast.\n\nWenn du den Astronaut:innen sagen willst, zum linken Planeten zu fliegen, klicke auf den LINKEN Planeten.\n\nWenn du den Astronaut:innen sagen willst, zum rechten Planeten zu fliegen, klicke auf den RECHTEN Planeten.'
        main.space_image_4 = main.space_image_4_ger
    main.text_16.setText(instr)
    main.proceed_13.keys = []
    main.proceed_13.rt = []
    main._proceed_13_allKeys = []
    main.choice_components = [main.space_image_4, main.text_16, main.proceed_13]
    main.choice_components = main.prepare_routine(main.choice_components)
    
    # prepare
    while main.continueRoutine:
        main.timing.get_current_time(main.routineTimer, main)
        main.frameN = main.frameN + 1
        main.space_image_4 = main.components.text_or_image_update(main.space_image_4, 'space_image_4.started', main)
        main.text_16 = main.components.text_or_image_update(main.text_16, 'text_16.started', main)
        main.waitOnFlip = False
        main.proceed_13, main._proceed_13_allKeys = main.components.keys_update(main.proceed_13, main._proceed_13_allKeys, 'proceed_13.started', main)
        if main.endExpNow or main.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
        if not main.continueRoutine: main.routineForceEnded = True; break
        main.continueRoutine = False
        main.choice_components = main.components.check_if_components_finished(main.choice_components, main)
        if main.continueRoutine: main.win.flip()
    
    # end
    main.choice_components = main.components.hide_components(main.choice_components)
    main.proceed_13 = main.components.save_key_response(main.proceed_13, 'proceed_13.keys', 'proceed_13.rt', main)
    main.thisExp.nextEntry() # watch out
    main.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def reward(main):
    # prepare
    if main.lang_keys.keys == 'e':
        instr='Next, the spaceship travels to the left/right planet depending on the advice you gave. \n\nIf the spaceship finds the space crystals on that planet, you get a point.\nFor instance, in the image above, the spaceship found the crystals on the given planet and hence, you win 1 point.'
    else:
        instr='Danach reist das Raumschiff zum linken/rechten Planeten, je nachdem, welchen Rat du gegeben hast.\n\nWenn das Raumschiff die Raumkristalle auf diesem Planeten findet, erhältst du 1 Punkt.\nIm obigen Bild zum Beispiel hat das Raumschiff die Kristalle auf dem angegebenen Planeten gefunden und du bekommst 1 Punkt.'
        main.space_image_5 = main.space_image_5_ger
    main.text_17.setText(instr)
    main.proceed_14.keys = []
    main.proceed_14.rt = []
    main._proceed_14_allKeys = []
    main.reward_components = [main.proceed_14, main.space_image_5, main.text_17]
    main.reward_components = main.prepare_routine(main.reward_components)
    
    # run
    while main.continueRoutine:
        main.timing.get_current_time(main.routineTimer, main)
        main.frameN = main.frameN + 1
        main.space_image_5 = main.components.text_or_image_update(main.space_image_5, 'space_image_5.started', main)
        main.text_17 = main.components.text_or_image_update(main.text_17, 'text_17.started', main)
        main.waitOnFlip = False
        main.proceed_14, main._proceed_14_allKeys = main.components.keys_update(main.proceed_14, main._proceed_14_allKeys, 'proceed_14.started', main)
        if main.endExpNow or main.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
        if not main.continueRoutine: main.routineForceEnded = True; break
        main.continueRoutine = False
        main.reward_components = main.components.check_if_components_finished(main.reward_components, main)
        if main.continueRoutine: main.win.flip()
    
    # end
    main.reward_components = main.components.hide_components(main.reward_components)
    main.proceed_14 = main.components.save_key_response(main.proceed_14, 'proceed_14.keys', 'proceed_14.rt', main)
    main.thisExp.nextEntry() # watch out
    main.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def no_reward(main):
    # prepare
    if main.lang_keys.keys == 'e':
        instr='Similarly, if the spaceship does not find the space crystals on that planet, you get 0 points. For instance, in the image above, the spaceship did not find the crystals on the given planet and hence, you win 0 points. \n\n'
    else:
        instr='Wenn das Raumschiff auf dem Planeten keine Kristalle findet, erhält man 0 Punkte. Im obigen Bild zum Beispiel hat das Raumschiff die Kristalle auf dem angegebenen Planeten nicht gefunden, und du erhältst 0 Punkte.\n\n'
        main.space_image_6 = main.space_image_6_ger
    main.text_18.setText(instr)
    main.proceed_15.keys = []
    main.proceed_15.rt = []
    main._proceed_15_allKeys = []
    main.no_reward_components = [main.proceed_15, main.space_image_6, main.text_18]
    main.no_reward_components = main.prepare_routine(main.no_reward_components)
    
    # run
    while main.continueRoutine:
        main.timing.get_current_time(main.routineTimer, main)
        main.frameN = main.frameN + 1
        main.space_image_6 = main.components.text_or_image_update(main.space_image_6, 'space_image_6.started', main)
        main.text_18 = main.components.text_or_image_update(main.text_18, 'text_18.started', main)
        main.waitOnFlip = False
        main.proceed_15, main._proceed_15_allKeys = main.components.keys_update(main.proceed_15, main._proceed_15_allKeys, 'proceed_15.started', main)
        if main.endExpNow or main.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
        if not main.continueRoutine: main.routineForceEnded = True; break
        main.continueRoutine = False
        main.no_reward_components = main.components.check_if_components_finished(main.no_reward_components, main)
        if main.continueRoutine: main.win.flip()
    
    # end
    main.no_reward_components = main.components.hide_components(main.no_reward_components)
    main.proceed_15 = main.components.save_key_response(main.proceed_15, 'proceed_15.keys', 'proceed_15.rt', main)
    main.thisExp.nextEntry() # watch out
    main.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def congruence_caution(main):
    # prepare
    if main.lang_keys.keys == 'e':
        instr='Please note: You might have noticed that in some blocks you are asked to indicate the probability of finding space crystals for a planet where the chance is actually lower. This is done on purpose.'
    else:
        instr='Du hast vielleicht bemerkt, dass du in einigen Blöcken aufgefordert wirst, die Wahrscheinlichkeit anzugeben, Weltraumkristalle für einen Planeten zu finden, auf dem die Chance tatsächlich geringer ist. Dies geschieht absichtlich.'
    main.text_congruence_caution.setText(instr)
    main.proceed_congruence_caution.keys = []
    main.proceed_congruence_caution.rt = []
    main._proceed_congruence_caution_allKeys = []
    main.congruence_caution_components = [main.space_bg_congruence_caution, main.proceed_congruence_caution, main.text_congruence_caution]
    main.congruence_caution_components = main.prepare_routine(main.congruence_caution_components)

    
    # run
    while main.continueRoutine:
        main.timing.get_current_time(main.routineTimer, main)
        main.frameN = main.frameN + 1
        main.space_bg_congruence_caution = main.components.text_or_image_update(main.space_bg_congruence_caution, 'space_bg_congruence_caution.started', main)
        main.text_congruence_caution = main.components.text_or_image_update(main.text_congruence_caution, 'text_congruence_caution.started', main)
        main.waitOnFlip = False
        main.proceed_congruence_caution, main._proceed_congruence_caution_allKeys = main.components.keys_update(main.proceed_congruence_caution, main._proceed_congruence_caution_allKeys, 'proceed_congruence_caution.started', main)
        if main.endExpNow or main.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
        if not main.continueRoutine: main.routineForceEnded = True; break
        main.continueRoutine = False
        main.congruence_caution_components = main.components.check_if_components_finished(main.congruence_caution_components, main)
        if main.continueRoutine: main.win.flip()
    
    # end
    main.congruence_caution_components = main.components.hide_components(main.congruence_caution_components)
    main.proceed_congruence_caution = main.components.save_key_response(main.proceed_congruence_caution, 'proceed_congruence_caution.keys', 'proceed_congruence_caution.rt', main)
    main.thisExp.nextEntry() # watch out
    main.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def points(main):
    # prepare
    if main.lang_keys.keys == 'e':
        instr='Short summary: The aim of the task is to win as many points as possible. To do this, you need to:\n\n1. Analyze the radar signals \n2. Report the probability of finding space crystals on a given planet\n3. Advise the astronauts which planet they should fly to\n\nNow, we will do a few practice blocks of the task.\n\nPress SPACEBAR to proceed.'
    else:
        instr='Kurz zusammengefasst: Das Ziel der Aufgabe ist es, so viele Punkte wie möglich zu gewinnen. Um dies zu erreichen, musst du:\n\n1. Die Radarsignale analysieren\n\n2. Die Wahrscheinlichkeit angeben, dass man auf einem bestimmten Planeten Weltraumkristalle findet\n\n3. Den Astronaut:innen sagen, zu welchem Planeten sie fliegen sollten\n\nJetzt werden wir ein paar Übungsblöcke der Aufgabe machen.\n\nDrücke die die LEERTASTE, um fortzufahren.'
    main.text_19.setText(instr)
    main.proceed_16.keys = []
    main.proceed_16.rt = []
    main._proceed_16_allKeys = []
    main.points_components = [main.space_bg_11, main.proceed_16, main.text_19]
    main.points_components = main.prepare_routine(main.points_components)
    
    # run
    while main.continueRoutine:
        main.timing.get_current_time(main.routineTimer, main)
        main.frameN = main.frameN + 1
        main.space_bg_11 = main.components.text_or_image_update(main.space_bg_11, 'space_bg_11.started', main)
        main.text_19 = main.components.text_or_image_update(main.text_19, 'text_19.started', main)
        main.waitOnFlip = False
        main.proceed_16, main._proceed_16_allKeys = main.components.keys_update(main.proceed_16, main._proceed_16_allKeys, 'proceed_16.started', main)
        if main.endExpNow or main.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
        if not main.continueRoutine: main.routineForceEnded = True; break
        main.continueRoutine = False
        main.points_components = main.components.check_if_components_finished(main.points_components, main)
        if main.continueRoutine: main.win.flip()
    
    # end
    main.points_components = main.components.hide_components(main.points_components)
    main.proceed_16 = main.components.save_key_response(main.proceed_16, 'proceed_16.keys', 'proceed_16.rt', main)
    main.thisExp.nextEntry() # watch out
    main.routineTimer.reset()

    