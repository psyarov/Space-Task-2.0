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

# SETUP (DEVICES)
# EXPERIMENT DATA HANDLING
# INFO LOGGING
# CONDITIONS IMPORT

class Handler:

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __init__(self, type):
        self.type = type

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def experiment_info(self, main):
        '''
        Stores experiment information.
        '''
        main._thisDir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(main._thisDir)
        main.psychopyVersion = '2022.2.5'
        main.expName = 'space_task_offline'
        main.expInfo = {
            'participant': f"{randint(0, 999999):06.0f}",
            'session': '001',
        }

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def participant_window(self, main):
        '''
        Shows a window for participant and session number input.
        '''
        main.dlg = gui.DlgFromDict(dictionary=main.expInfo, sortKeys=False, title=main.expName)
        if main.dlg.OK == False: core.quit()
        main.expInfo['date'] = data.getDateStr()
        main.expInfo['expName'] = main.expName
        main.expInfo['psychopyVersion'] = main.psychopyVersion
        main.filename = main._thisDir + os.sep + u'data/%s_%s' % (main.expInfo['participant'], main.expName)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def setup_window(self, main):
        '''
        Sets up a window for the task.
        '''
        main.win = visual.Window(size=[1536, 864], fullscr=True, screen=0, winType='pyglet', allowStencil=False, monitor='testMonitor', color=[0,0,0], colorSpace='rgb', blendMode='avg', useFBO=True, units='height')
        main.win.mouseVisible = False
        main.expInfo['frameRate'] = main.win.getActualFrameRate()
        if main.expInfo['frameRate'] != None:
            main.frameDur = 1.0 / round(main.expInfo['frameRate'])
        else:
            main.frameDur = 1.0 / 60.0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def setup_devices(self, main):
        '''
        Prepare devices to be used during the experiment (keyboard, mouse, eyetracker, etc.).
        '''
        main.ioConfig = {}
        main.ioConfig['Keyboard'] = dict(use_keymap='psychopy') 
        main.ioSession = '1'
        if 'session' in main.expInfo: main.ioSession = str(main.expInfo['session'])
        main.ioServer = io.launchHubServer(window=main.win, **main.ioConfig) # check
        main.eyetracker = None
        main.defaultKeyboard = keyboard.Keyboard(backend='iohub')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def create_variables(self, handler):
        if handler != None:
            for paramName in handler:
                exec('{} = handler[paramName]'.format(paramName))
        return handler

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def experiment_handler(self, main):
        '''
        Handles the data for the whole experiment.
        '''
        main.thisExp = data.ExperimentHandler(name=main.expName, version='',
            extraInfo=main.expInfo, runtimeInfo=None,
            originPath='C:\\Users\\prash\\Nextcloud\\Thesis_laptop\\Semester 6\\pavlovia_offline\\space_task_offline.py',
            savePickle=True, saveWideText=True,
            dataFileName=main.filename)
        main.logFile = logging.LogFile(main.filename+'.log', level=logging.EXP)
        logging.console.setLevel(logging.WARNING)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def training_blocks_handler(self, main):
        '''
        Imports conditions for training blocks.
        '''
        main.training_blocks = data.TrialHandler(nReps=1.0, method='sequential', extraInfo=main.expInfo, originPath=-1, trialList=data.importConditions('resources/training_files.xlsx', selection='0,1'), seed=None, name='training_blocks')
        main.thisExp.addLoop(main.training_blocks)
        main.thisTraining_block = main.training_blocks.trialList[0]
        main.thisTraining_block = self.create_variables(main.thisTraining_block)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def training_handler(self, main):
        '''
        Imports conditions for current training block.
        '''
        main.training = data.TrialHandler(nReps=1.0, method='random', extraInfo=main.expInfo, originPath=-1, trialList=data.importConditions(main.thisTraining_block['condition_file'], selection=main.trial_lists), seed=None, name='training')
        main.thisExp.addLoop(main.training)
        main.thisTraining = main.training.trialList[0]
        main.thisTraining = self.create_variables(main.thisTraining)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def prac_main_handler(self, main):
        '''
        Imports conditions for all blocks of practice/main task.
        '''
        main.prac_main_task = data.TrialHandler(nReps=1.0, method='sequential', extraInfo=main.expInfo, originPath=-1, trialList=data.importConditions('resources/task_files.xlsx', selection='0,1'), seed=None, name='prac_main_task')
        main.thisExp.addLoop(main.prac_main_task)
        main.thisPrac_main_task = main.prac_main_task.trialList[0]
        main.thisPrac_main_task = self.create_variables(main.thisPrac_main_task)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def block_handler(self, main):
        '''
        Imports conditions for current block of practice/main task.
        '''
        main.block = data.TrialHandler(nReps=1.0, method='sequential', extraInfo=main.expInfo, originPath=-1, trialList=data.importConditions('resources/condition_files.xlsx', selection=main.block_lists), seed=None, name='block')
        main.thisExp.addLoop(main.block)
        main.thisBlock = main.block.trialList[0]
        main.thisBlock = self.create_variables(main.thisBlock)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def primer_handler(self, main):
        '''
        Imports conditions for first trial of a given block.
        '''
        main.primer = data.TrialHandler(nReps=1.0, method='random', extraInfo=main.expInfo, originPath=-1, trialList=data.importConditions(main.thisBlock['condition_file'], selection='1'), seed=None, name='primer') 
        main.thisExp.addLoop(main.primer)
        main.thisPrimer = main.primer.trialList[0]
        main.thisPrimer = self.create_variables(main.thisPrimer)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def trials_handler(self, main):
        '''
        Imports conditions for all trial of a given block in practice/main task.
        '''
        main.trials = data.TrialHandler(nReps=1.0, method='random', extraInfo=main.expInfo, originPath=-1, trialList=data.importConditions(main.thisBlock['condition_file'], selection=main.trial_lists), seed=None, name='trials')
        main.thisExp.addLoop(main.trials) 
        main.thisTrial = main.trials.trialList[0]
        main.thisTrial = self.create_variables(main.thisTrial)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def last_handler(self, main):
        '''
        Imports conditions for last slider usage of a given block.
        '''
        main.last = data.TrialHandler(nReps=1.0, method='random', extraInfo=main.expInfo, originPath=-1, trialList=data.importConditions(main.thisBlock['condition_file'], selection='1'), seed=None, name='last')
        main.thisExp.addLoop(main.last)
        main.thisLast = main.last.trialList[0]
        main.thisLast = self.create_variables(main.thisLast)

