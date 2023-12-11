# IMPORT PACKAGES
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

# FUNCTION CREATION
def keep_track(list_of_components):
    for thisComponent in list_of_components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    return list_of_components

def reset_timers(win):
    t = 0
    frameN = -1
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    return t, frameN, _timeToFirstFrame
    
def get_current_time(some_clock, win):
    t = some_clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=some_clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    return t, tThisFlip, tThisFlipGlobal

def text_or_image_update(text, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win):
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance: 
        # keep track of time function?
        text.frameNStart = frameN
        text.tStart = t
        text.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(text, 'tStartRefresh')
        text.setAutoDraw(True)
    return text, win

def keys_update_1(keys, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win):
    keys.frameNStart = frameN
    keys.tStart = t
    keys.tStartRefresh = tThisFlipGlobal
    win.timeOnFlip(keys, 'tStartRefresh')
    keys.status = STARTED 
    waitOnFlip = True
    win.callOnFlip(keys.clock.reset)
    win.callOnFlip(keys.clearEvents, eventType='keyboard')
    return keys, win, waitOnFlip
    
def keys_update_2(keys, all_keys, key):
    theseKeys = keys.getKeys(keyList=key, waitRelease=False)
    all_keys.extend(theseKeys)
    continueRoutine = True # careful with this, it was not initially here
    if len(all_keys):
        keys.keys = all_keys[-1].name
        keys.rt = all_keys[-1].rt
        continueRoutine = False
    return theseKeys, all_keys, keys, continueRoutine

def check_if_components_finished(components, continueRoutine):
    for thisComponent in components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    return components, continueRoutine

def hide_components(components):
    for thisComponent in components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    return components