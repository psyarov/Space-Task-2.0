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

# HANDLES ALL COMPONENTS
# SHOWS COMPONENTS ON SCREEN
# HIDES COMPONENT FROM SCREEN


class Components:

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __init__(self, type):
        self.type = type

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def text_or_image_update(self, component, text, main):
        '''
        Shows component (text, image, etc.) on screen if not already shown.
        
        Parameters:
        - component(text/image component): text or image component from a certain routine
        - text(string): name under which to store time status in log file
        
        Returns:
        - components(text/image component): but with status  set to STARTED (=shown on screen)
        '''
        if component.status == NOT_STARTED and main.tThisFlip >= 0.0-main.frameTolerance: 
            # keep track of time function?
            component.frameNStart = main.frameN
            component.tStart = main.t
            component.tStartRefresh = main.tThisFlipGlobal
            main.win.timeOnFlip(component, 'tStartRefresh')
            main.thisExp.timestampOnFlip(main.win, text)
            component.setAutoDraw(True)
            if text == 'movie.started':
                main.movie.play()
            elif text == 'movie_2.started':
                main.movie_2.play()
        return component

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def text_or_image_update_2(self, component, text, num, main):
        '''
        Hides component from the screen if the routine ends.
        '''
        if component.status == STARTED:
            if main.tThisFlipGlobal > component.tStartRefresh + num-main.frameTolerance:
                component.tStop = main.t
                component.frameNStop = main.frameN
                main.thisExp.timestampOnFlip(main.win, text)
                component.setAutoDraw(False)
        return component

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def keys_update(self, keys, all_keys, text, main):
        '''
        Records key press.
        '''
        if keys.status == NOT_STARTED and main.tThisFlip >= 0.0-main.frameTolerance:
            keys = self.keys_update_1(keys, main)
            main.thisExp.timestampOnFlip(main.win, text)
        if keys.status == STARTED and not main.waitOnFlip:
            all_keys, keys = self.keys_update_2(keys, all_keys, ['space'], main)
        return keys, all_keys

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def keys_update_1(self, keys, main):
        '''
        Records time conditions of key press.
        '''
        keys.frameNStart = main.frameN
        keys.tStart = main.t
        keys.tStartRefresh = main.tThisFlipGlobal
        main.win.timeOnFlip(keys, 'tStartRefresh')
        keys.status = STARTED 
        main.waitOnFlip = True
        main.win.callOnFlip(keys.clock.reset)
        main.win.callOnFlip(keys.clearEvents, eventType='keyboard')
        return keys

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def keys_update_2(self, keys, all_keys, key, main):
        '''
        If keys are pressed, the routine ends.
        '''
        main.theseKeys = keys.getKeys(keyList=key, waitRelease=False)
        all_keys.extend(main.theseKeys)
        main.continueRoutine = True # check
        if len(all_keys):
            keys.keys = all_keys[-1].name
            keys.rt = all_keys[-1].rt
            main.continueRoutine = False
        return all_keys, keys

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def check_if_components_finished(self, components, main):
        '''
        Checks if any components are not finished and continues the routine accordingly.
        '''
        for thisComponent in components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                main.continueRoutine = True
                break
        return components

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def hide_components(self, components):
        '''
        Hides all components from the screen.
        '''
        for thisComponent in components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        return components

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def save_key_response(self, key_type, text1, text2, main):
        '''
        Logs key responses.
        '''
        if key_type.keys in ['', [], None]:
            key_type.keys = None
        if text1 == 'lang_keys.keys' or text1 == 'proceed_4.keys' or text1 == 'proceed_7.keys' or text1 == 'proceed_5.keys' or text1 == 'proceed_6.keys' or text1 == 'proceed_8.keys' or text1 == 'proceed_9.keys' or text1 == 'proceed_2.keys' or text1 == 'proceed_23.keys' or text1 in ('proceed_25.keys', 'proceed.keys', 'proceed_10.keys', 'proceed_11.keys', 'proceed_12.keys', 'proceed_ghost.keys', 'proceed_slider_accuracy.keys', 'proceed_24.keys', 'proceed_incong.keys', 'proceed_26.keys', 'proceed_13.keys', 'proceed_14.keys', 'proceed_15.keys', 'proceed_congruence_caution.keys', 'proceed_16.keys'):
            main.thisExp.addData(text1, key_type.keys)
        elif text1 == 'key_resp_3.keys':
            main.primer.addData(text1, key_type.keys)
        elif text1 == 'key_resp_5.keys':
            main.last.addData(text1, key_type.keys)
        elif text1 == 'proceed_20.keys':
            main.prac_main_task.addData(text1, key_type.keys)
        else:
            main.block.addData(text1, key_type.keys)
        if key_type.keys != None:
            if text1 == 'lang_keys.keys' or text1 == 'proceed_4.keys' or text1 == 'proceed_7.keys' or text1 == 'proceed_5.keys' or text1 == 'proceed_6.keys' or text1 == 'proceed_8.keys' or text1 == 'proceed_9.keys' or text1 == 'proceed_2.keys' or text1 == 'proceed_23.keys' or text1 in ('proceed_25.keys', 'proceed.keys', 'proceed_10.keys', 'proceed_11.keys', 'proceed_12.keys', 'proceed_ghost.keys', 'proceed_slider_accuracy.keys', 'proceed_24.keys', 'proceed_incong.keys', 'proceed_26.keys', 'proceed_13.keys', 'proceed_14.keys', 'proceed_15.keys', 'proceed_congruence_caution.keys', 'proceed_16.keys'):
                main.thisExp.addData(text2, key_type.rt)
            elif text1 == 'key_resp_3.keys':
                main.primer.addData(text2, key_type.rt)
            elif text1 == 'key_resp_5.keys':
                main.last.addData(text2, key_type.rt)
            elif text1 == 'proceed_20.keys':
                main.prac_main_task.addData(text2, key_type.rt)
            else:
                main.block.addData(text2, key_type.rt)
        return key_type