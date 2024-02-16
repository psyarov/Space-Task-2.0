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

# CREATES TIMERS
# KEEPS TRACK OF STIMULI AND START/STOP TIMES


class Timing:

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __init__(self, type):
        self.type = type

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def create_timers(self, main):
        '''
        Creates handy timers to track stimuli and responses.
        
        Parameters:
        - main (object): object of the class Routines which stores all variables and components
        '''
        main.globalClock = core.Clock()
        main.routineTimer = core.Clock()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def keep_track(self, components):
        '''
        Keeps track of start/stop time of a given list of components.
        
        Parameters:
        - components (list): all components of a given routine
        
        Returns:
        - components (list): same components but with recorded start/stop times
        '''
        for thisComponent in components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        return components

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def reset_timers(self, main):
        '''
        Sets timer values to zero in order to start a new routine.
        '''
        main.t = 0
        main.frameN = -1
        main._timeToFirstFrame = main.win.getFutureFlipTime(clock="now")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def get_current_time(self, some_clock, main):
        '''
        Extracts current time information from global timers.
        
        Parameters:
        - some_clock(time component): global timer
        '''
        main.t = some_clock.getTime()
        main.tThisFlip = main.win.getFutureFlipTime(clock=some_clock)
        main.tThisFlipGlobal = main.win.getFutureFlipTime(clock=None)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def routine_reset(self, main):
        '''
        Resets global routine variables to start a new routine.
        '''
        main.continueRoutine = True
        main.routineForceEnded = False