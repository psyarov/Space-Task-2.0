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


class Trial:
    
    # variables
    endExpNow = False
    frameTolerance = 0.001
    task_rew = 0
    rew = 'hello'
    block_str = 'hello'
    number_list = [1,2,3,4]
    random.shuffle(number_list)
    task_str = "hello"
    lists = [0, 1, 2, 3] #, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]   # manipulate blocks
    block_lists = lists
    number_of_blocks = len(block_lists)
    random.shuffle(block_lists);
    print(block_lists);
    x = [0] #,1,2]#,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]                      # manipulate trials
    random.shuffle(x);
    trial_lists = x;
    ques_word = 'hello'
    total_blocks = number_of_blocks
    block_num = 0;
    cond1_rew = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0];
    cond2_rew = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0];
    random.shuffle(cond1_rew);
    random.shuffle(cond2_rew);
    task_str = 'hello'
    mu = 0
    
    # experiment information (variables)
    _thisDir = None
    _thisDir = None 
    psychopyVersion = None
    expName = None
    expInfo = None
    
    # participant window
    dlg = None
    filename = None
    
    # experiment handler
    thisExp = None
    logFile = None
    logging = None
    
    # setup window
    win = None
    frameDur = None
    
    # setup devices
    ioConfig = None
    ioSession = None
    ioServer = None
    io = None
    eyetracker = False
    defaultKeyboard = None
    
    # initialize routines
    # language preference
    language_preferenceClock = None
    text_101 = None
    lang_keys = None
    language_preference_components = None
    continueRoutine = None
    routineForceEnded = None
    _lang_keys_allKeys = None
    t = None
    frameN = None
    _timeToFirstFrame = None
    tThisFlip = None
    tThisFlipGlobal = None
    waitOnFlip = None
    theseKeys = None
    # prac_block
    space_image_7 = None
    proceed_17 = None
    _proceed_17_allKeys = None
    text_20 = None
    prac_block_components = None
    # primer_mu                 -> create xlsx table with all values for space background -> import -> replace e.g. ori=0.o with table.whatever
    space_bg_12 = None
    shuttle_5 = None
    planet_right_6 = None
    planet_left_6 = None
    arrow_left_3 = None
    mu_5 = None
    text_21 = None
    key_resp_3 = None
    left_planet = None
    right_planet = None
    # signal
    space_image_8 = None
    radar_3 = None
    left_patch_7 = None
    fix_circle_7 = None
    right_patch_7 = None
    # slider_3
    space_bg_13 = None
    text_22 = None
    reported_mu = None
    mu_ghost = None
    shuttle_3 = None
    planet_right_7 = None
    planet_left_7 = None
    arrow_left_4 = None
    # prechoice_text
    space_bg_14 = None
    text_23 = None
    key_resp_4 = None
    # last_mu
    space_bg_15 = None
    shuttle_6 = None
    planet_right_8 = None
    planet_left_8 = None
    arrow_left_5 = None
    mu_7 = None
    text_24 = None
    key_resp_5 = None
    text_31 = None
    mu = None
    # block_choice
    space_bg_16 = None
    shuttle_7 = None
    planet_right_9 = None
    planet_left_9 = None
    text_25 = None
    question = None
    mouse_resp = None
    x, y = [None, None]
    # block_rew
    space_bg_17 = None
    proceed_18 = None
    text_26 = None
    planet = None
    shuttle_8 = None
    crystal = None
    # block_completed
    space_bg_18 = None
    proceed_19 = None
    text_27 = None
    # task_score
    space_bg_19 = None
    text_28 = None
    proceed_20 = None
    
    # create timers
    globalClock = None
    routineTimer = None
    
    # prac_main handler
    prac_main_task = None
    thisPrac_main_task = None
    currentLoop = None
    
    #block_handler
    block = None
    thisBlock = None
    task_file = None
    
    #primer handler
    primer = None
    thisPrimer = None
    condition_file = None
    
    #trials handler
    trials = None
    thisTrial = None
    
    # last handler
    last = None
    thisLast = None
    
    
    def __init__(self, type):
        self.type = type
    
    def experiment_info(self):
        # this may be redundant, since the variables get initialized in the class attributes section
        self._thisDir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(self._thisDir) # check function, may also be problematic in participant_window
        self.psychopyVersion = '2022.2.5'
        self.expName = 'space_task_offline'
        self.expInfo = {
            'participant': f"{randint(0, 999999):06.0f}",
            'session': '001',
        }
    
    def participant_window(self):
        self.dlg = gui.DlgFromDict(dictionary=self.expInfo, sortKeys=False, title=self.expName)
        if self.dlg.OK == False: core.quit()
        self.expInfo['date'] = data.getDateStr()
        self.expInfo['expName'] = self.expName
        self.expInfo['psychopyVersion'] = self.psychopyVersion
        self.filename = self._thisDir + os.sep + u'data/%s_%s' % (self.expInfo['participant'], self.expName)

    def experiment_handler(self):
        self.thisExp = data.ExperimentHandler(name=self.expName, version='',
            extraInfo=self.expInfo, runtimeInfo=None,
            originPath='C:\\Users\\prash\\Nextcloud\\Thesis_laptop\\Semester 6\\pavlovia_offline\\space_task_offline.py',
            savePickle=True, saveWideText=True,
            dataFileName=self.filename)
        self.logFile = logging.LogFile(self.filename+'.log', level=logging.EXP) # check
        logging.console.setLevel(logging.WARNING) # check

    def setup_window(self):
        self.win = visual.Window(size=[1536, 864], fullscr=True, screen=0, winType='pyglet', allowStencil=False, monitor='testMonitor', color=[0,0,0], colorSpace='rgb', blendMode='avg', useFBO=True, units='height')
        self.win.mouseVisible = False
        self.expInfo['frameRate'] = self.win.getActualFrameRate()
        if self.expInfo['frameRate'] != None:
            self.frameDur = 1.0 / round(self.expInfo['frameRate'])
        else:
            self.frameDur = 1.0 / 60.0

    def setup_devices(self):
        self.ioConfig = {}
        self.ioConfig['Keyboard'] = dict(use_keymap='psychopy') 
        self.ioSession = '1'
        if 'session' in self.expInfo: self.ioSession = str(self.expInfo['session'])
        self.ioServer = io.launchHubServer(window=self.win, **self.ioConfig) # check
        self.eyetracker = None
        self.defaultKeyboard = keyboard.Keyboard(backend='iohub')

    def setup(self):
        self.experiment_info()
        self.participant_window()
        self.experiment_handler()
        self.setup_window()
        self.setup_devices()

    def initialize_routines(self):
        # language preference
        self.language_preferenceClock = core.Clock()
        self.text_101 = visual.TextStim(win=self.win, name='text_101', text='Bitte gib an, welche Sprache du für die Instruktionen bevorzugst.\n\nDrücke G für Deutsch. \nDrücke E für Englisch.\n\nIndicate the language that you prefer for the task instructions.\n\nPress G for German. \nPress E for English.', font='Times New Roman', pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0,  color='black', colorSpace='rgb', opacity=None,  languageStyle='LTR', depth=0.0);
        self.lang_keys = keyboard.Keyboard() 
        # prac_block
        self.space_image_7 = visual.ImageStim(win=self.win, name='space_image_7', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-1.0)
        self.proceed_17 = keyboard.Keyboard()
        self.text_20 = visual.TextStim(win=self.win, name='text_20', text='', font='Times New Roman', pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-3.0);
        # primer_mu
        self.space_bg_12 = visual.ImageStim(win=self.win, name='space_bg_12', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
        self.shuttle_5 = visual.ImageStim(win=self.win, name='shuttle_5', image='resources/space-shuttle.png', mask=None, anchor='center', ori=0.0, pos=(0, -0.15), size=(0.2, 0.2), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-2.0)
        self.planet_right_6 = visual.ImageStim(win=self.win, name='planet_right_6', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-3.0)
        self.planet_left_6 = visual.ImageStim(win=self.win, name='planet_left_6', image='sin', mask=None, anchor='center', ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-4.0)
        self.arrow_left_3 = visual.ImageStim(win=self.win, name='arrow_left_3', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.2,0.35), color=[1,1,1], colorSpace='rgb', opacity=0.5, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-5.0)
        self.mu_5 = visual.Slider(win=self.win, name='mu_5', startValue=None, size=(0.8, 0.03), pos=(0, -0.38), units=None, labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0, style='rating', styleTweaks=(), opacity=None, labelColor=[0.8824, 0.9451, 1.0000], markerColor=[1.0000, 1.0000, 1.0000], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb', font='Times New Roman', labelHeight=0.03, flip=False, ori=0.0, depth=-6, readOnly=True)
        self.text_21 = visual.TextStim(win=self.win, name='text_21', text='', font='Times New Roman', pos=(0, -0.3), height=0.03, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-7.0);
        self.key_resp_3 = keyboard.Keyboard()
        self.mu_ghost = visual.Slider(win=self.win, name='mu_ghost', startValue=None, size=(0.8, 0.03), pos=(0, -0.38), units=None, labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0, style='rating', styleTweaks=(), opacity=0, labelColor=[0.8824, 0.9451, 1.0000], markerColor=[-0.4980, 0.7569, 0.6314], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb', font='Times New Roman', labelHeight=0.03, flip=False, ori=0.0, depth=-6.0, readOnly=True)
        # signal
        self.space_image_8 = visual.ImageStim(win=self.win, name='space_image_8', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
        self.radar_3 = visual.ImageStim(win=self.win, name='radar_3', image='resources/radar_grayl.png', mask=None, anchor='center', ori=0.0, pos=(0,0), size=(0.6, 0.6), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-1.0)
        self.left_patch_7 = visual.GratingStim(win=self.win, name='left_patch_7', tex='sin', mask='gauss', anchor='center', ori=0.0, pos=(-0.12, 0), size=(0.12, 0.12), sf=8.0, phase=0.0, color=[1,1,1], colorSpace='rgb', opacity=None, contrast=1.0, blendmode='avg', texRes=512.0, interpolate=True, depth=-2.0)
        self.fix_circle_7 = visual.ShapeStim(win=self.win, name='fix_circle_7', size=(0.007, 0.007), vertices='circle', ori=0.0, pos=(0, 0), anchor='center', lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black', opacity=None, depth=-3.0, interpolate=True)
        self.right_patch_7 = visual.GratingStim(win=self.win, name='right_patch_7', tex='sin', mask='gauss', anchor='center', ori=0.0, pos=(0.12, 0), size=(0.12, 0.12), sf=8.0, phase=0.0, color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, contrast=1.0, blendmode='avg', texRes=512.0, interpolate=True, depth=-4.0)
        # slider_3
        self.space_bg_13 = visual.ImageStim(win=self.win, name='space_bg_13', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
        self.text_22 = visual.TextStim(win=self.win, name='text_22', text='', font='Times New Roman', pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0.0, color=[0.8824, 0.9451, 1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0);
        self.reported_mu = visual.Slider(win=self.win, name='reported_mu', startValue=50, size=(0.8, 0.03), pos=(0, -0.38), units=None, labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0, style='rating', styleTweaks=(), opacity=None, labelColor=[0.8824, 0.9451, 1.0000], markerColor=[1.0000, 1.0000, 1.0000], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb', font='Times New Roman', labelHeight=0.03, flip=False, ori=0.0, depth=-3, readOnly=False)
        self.mu_ghost = visual.Slider(win=self.win, name='mu_ghost', startValue=None, size=(0.8, 0.03), pos=(0, -0.38), units=None, labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0, style='rating', styleTweaks=(), opacity=0, labelColor=[0.8824, 0.9451, 1.0000], markerColor=[-0.4980, 0.7569, 0.6314], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb', font='Times New Roman', labelHeight=0.03, flip=False, ori=0.0, depth=-6.0, readOnly=True)
        self.shuttle_3 = visual.ImageStim(win=self.win, name='shuttle_3', image='resources/space-shuttle.png', mask=None, anchor='center', ori=0.0, pos=(0, -0.15), size=(0.2, 0.2), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-4.0)
        self.planet_right_7 = visual.ImageStim(win=self.win, name='planet_right_7', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-5.0)
        self.planet_left_7 = visual.ImageStim(win=self.win, name='planet_left_7', image='sin', mask=None, anchor='center', ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-6.0)
        self.arrow_left_4 = visual.ImageStim(win=self.win, name='arrow_left_4', image='sin', mask=None, anchor='center', ori=1.0, pos=[0,0], size=(0.2,0.35), color=[1,1,1], colorSpace='rgb', opacity=0.5, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-7.0)
        # prechoice_text
        self.space_bg_14 = visual.ImageStim(win=self.win, name='space_bg_14', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
        self.text_23 = visual.TextStim(win=self.win, name='text_23', text='', font='Times New Roman', pos=(0, 0), height=0.03, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-1.0);
        self.key_resp_4 = keyboard.Keyboard()
        # last_mu
        self.space_bg_15 = visual.ImageStim(win=self.win, name='space_bg_15', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
        self.shuttle_6 = visual.ImageStim(win=self.win, name='shuttle_6', image='resources/space-shuttle.png', mask=None, anchor='center', ori=0.0, pos=(0, -0.15), size=(0.2, 0.2), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-2.0)
        self.planet_right_8 = visual.ImageStim(win=self.win, name='planet_right_8', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-3.0)
        self.planet_left_8 = visual.ImageStim(win=self.win, name='planet_left_8', image='sin', mask=None, anchor='center', ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-4.0)
        self.arrow_left_5 = visual.ImageStim(win=self.win, name='arrow_left_5', image='sin', mask=None, anchor='center', ori=1.0, pos=[0,0], size=(0.2,0.35), color=[1,1,1], colorSpace='rgb', opacity=0.5, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-5.0)
        self.mu_7 = visual.Slider(win=self.win, name='mu_7', startValue=0, size=(0.8, 0.03), pos=(0, -0.38), units=None, labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0, style='rating', styleTweaks=(), opacity=None, labelColor=[0.8824, 0.9451, 1.0000], markerColor=[-0.4980, 0.7569, 0.6314], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb', font='Times New Roman', labelHeight=0.03, flip=False, ori=0.0, depth=-6, readOnly=True)
        self.text_24 = visual.TextStim(win=self.win, name='text_24', text='', font='Times New Roman', pos=(0, -0.3), height=0.03, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-7.0);
        self.key_resp_5 = keyboard.Keyboard()
        self.text_31 = visual.TextStim(win=self.win, name='text_31', text='Press SPACEBAR to proceed.', font='Times New Roman', pos=(0, -0.45), height=0.02, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-9.0);
        # block_choice
        self.space_bg_16 = visual.ImageStim(win=self.win, name='space_bg_16', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
        self.shuttle_7 = visual.ImageStim(win=self.win, name='shuttle_7', image='resources/space-shuttle.png', mask=None, anchor='center', ori=0.0, pos=(0, -0.135), size=(0.2, 0.2), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-1.0)
        self.planet_right_9 = visual.ImageStim(win=self.win, name='planet_right_9', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-2.0)
        self.planet_left_9 = visual.ImageStim(win=self.win, name='planet_left_9', image='sin', mask=None, anchor='center', ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-3.0)
        self.text_25 = visual.TextStim(win=self.win, name='text_25', text='', font='Times New Roman', pos=(0, -0.35), height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-4.0);
        self.question = visual.ImageStim(win=self.win, name='question', image='resources/question-mark.png', mask=None, anchor='center', ori=0.0, pos=(0, 0.05), size=(0.1, 0.1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-6.0)
        self.mouse_resp = event.Mouse(win=self.win)
        self.x, self.y = [None, None]
        self.mouse_resp.mouseClock = core.Clock()
        # block_rew
        self.space_bg_17 = visual.ImageStim(win=self.win, name='space_bg_17', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
        self.proceed_18 = keyboard.Keyboard()
        self.text_26 = visual.TextStim(win=self.win, name='text_26',text='', font='Open Sans', pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0);
        self.planet = visual.ImageStim(win=self.win, name='planet', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.5, 0.5), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-3.0)
        self.shuttle_8 = visual.ImageStim(win=self.win, name='shuttle_8', image='resources/shuttle_fire.png', mask=None, anchor='center', ori=1.0, pos=[0,0], size=(0.2, 0.3), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-4.0)
        self.crystal = visual.ImageStim(win=self.win, name='crystal', image='resources/crystal.png', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.1, 0.1), color=[1,1,1], colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-6.0)
        # block_completed
        self.space_bg_18 = visual.ImageStim(win=self.win, name='space_bg_18', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
        self.proceed_19 = keyboard.Keyboard()
        self.text_27 = visual.TextStim(win=self.win, name='text_27', text='', font='Times New Roman', pos=[0,0], height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0);
        # task_score
        self.space_bg_19 = visual.ImageStim(win=self.win, name='space_bg_19', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-1.0)
        self.text_28 = visual.TextStim(win=self.win, name='text_28', text='', font='Times New Roman', pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0);
        self.proceed_20 = keyboard.Keyboard()


    def create_timers(self):
        self.globalClock = core.Clock()
        self.routineTimer = core.Clock()

    def keep_track(self, components):
        for thisComponent in components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        return components
        

    def reset_timers(self):
        self.t = 0
        self.frameN = -1
        self._timeToFirstFrame = self.win.getFutureFlipTime(clock="now")

    def get_current_time(self, some_clock):
        self.t = some_clock.getTime()
        self.tThisFlip = self.win.getFutureFlipTime(clock=some_clock)
        self.tThisFlipGlobal = self.win.getFutureFlipTime(clock=None)
    
    def text_or_image_update(self, component):
        if component.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance: 
            # keep track of time function?
            component.frameNStart = self.frameN
            component.tStart = self.t
            component.tStartRefresh = self.tThisFlipGlobal
            self.win.timeOnFlip(component, 'tStartRefresh')
            component.setAutoDraw(True)
        return component
    
    def keys_update_1(self, keys):
        keys.frameNStart = self.frameN
        keys.tStart = self.t
        keys.tStartRefresh = self.tThisFlipGlobal
        self.win.timeOnFlip(keys, 'tStartRefresh')
        keys.status = STARTED 
        self.waitOnFlip = True
        self.win.callOnFlip(keys.clock.reset)
        self.win.callOnFlip(keys.clearEvents, eventType='keyboard')
        return keys
    
    def keys_update_2(self, keys, all_keys, key):
        self.theseKeys = keys.getKeys(keyList=key, waitRelease=False)
        all_keys.extend(self.theseKeys)
        self.continueRoutine = True # check
        if len(all_keys):
            keys.keys = all_keys[-1].name
            keys.rt = all_keys[-1].rt
            self.continueRoutine = False
        return all_keys, keys

    def check_if_components_finished(self, components):
        for thisComponent in components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                self.continueRoutine = True
                break
        return components

    def hide_components(self, components):
        for thisComponent in components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        return components

    def routine_reset(self):
        self.continueRoutine = True
        self.routineForceEnded = False

    def prepare_routine(self, components):
        self.routine_reset()
        components = self.keep_track(components)
        self.reset_timers() # check
        return components

    def run_routine(self, components): # currently only functional for language_preference
        while self.continueRoutine:
            self.get_current_time(self.language_preferenceClock)
            self.frameN = self.frameN + 1
            self.text_101 = self.text_or_image_update(self.text_101)
            # add a keys update function keys_update() with keys_list = ['e','g'] or keys_list = ["space"] or something -> so that we can use functions from the language preference keys
            self.waitOnFlip = False
            if self.lang_keys.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.lang_keys = self.keys_update_1(self.lang_keys)
            if self.lang_keys.status == STARTED and not self.waitOnFlip:
                self._lang_keys_allKeys, self.lang_keys = self.keys_update_2(self.lang_keys, self._lang_keys_allKeys, ['e','g'])
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: break
            self.continueRoutine = False
            components = self.check_if_components_finished(components)
            if self.continueRoutine: self.win.flip()
        return components

    def end_routine(self, components):
        components = self.hide_components(components)
        self.thisExp.addData('text_101.started', self.text_101.tStartRefresh)
        self.thisExp.addData('text_101.stopped', self.text_101.tStopRefresh)
        if self.lang_keys.keys in ['', [], None]:
            self.lang_keys.keys = None
        self.thisExp.addData('lang_keys.keys',self.lang_keys.keys)
        if self.lang_keys.keys != None:
            self.thisExp.addData('lang_keys.rt', self.lang_keys.rt)
        self.thisExp.addData('lang_keys.started', self.lang_keys.tStartRefresh)
        self.thisExp.addData('lang_keys.stopped', self.lang_keys.tStopRefresh)
        self.thisExp.nextEntry()
        self.routineTimer.reset()
        return components

    def language_preference(self):
        self.lang_keys.keys = []
        self.lang_keys.rt = []
        self._lang_keys_allKeys = []
        self.language_preference_components = [self.text_101, self.lang_keys]
        self.language_preference_components = self.prepare_routine(self.language_preference_components)
        self.language_preferenceClock.reset(-self._timeToFirstFrame)
        
        self.language_preference_components = self.run_routine(self.language_preference_components)
        self.language_preference_components = self.end_routine(self.language_preference_components)

    def create_variables(self, handler):
        if handler != None:
            for paramName in handler:
                exec('{} = handler[paramName]'.format(paramName))
        return handler

    def prac_main_handler(self):
        self.prac_main_task = data.TrialHandler(nReps=1.0, method='sequential', extraInfo=self.expInfo, originPath=-1, trialList=data.importConditions('resources/task_files.xlsx', selection='0,1'), seed=None, name='prac_main_task')
        self.thisExp.addLoop(self.prac_main_task)
        self.thisPrac_main_task = self.prac_main_task.trialList[0]
        self.thisPrac_main_task = self.create_variables(self.thisPrac_main_task)

    def block_handler(self):
        self.block = data.TrialHandler(nReps=1.0, method='sequential', extraInfo=self.expInfo, originPath=-1, trialList=data.importConditions('resources/condition_files.xlsx', selection=self.block_lists), seed=None, name='block') # task_file is HIGHLY!!!!!! questionable
        self.thisExp.addLoop(self.block)
        self.thisBlock = self.block.trialList[0]
        self.thisBlock = self.create_variables(self.thisBlock)

    def prac_block(self):
        
        if self.lang_keys.keys == 'e':
            self.text_20.setText('New block of the main task is coming up. \n Press SPACEBAR to proceed.')
        else:
            self.text_20.setText('Ein neuer Block der Hauptaufgabe wird angezeigt. Drücke die LEERTASTE, um fortzufahren.')
        self.proceed_17.keys = []
        self.proceed_17.rt = []
        self._proceed_17_allKeys = []
        
        self.prac_block_components = [self.space_image_7, self.proceed_17, self.text_20]
        self.prac_block_components = self.prepare_routine(self.prac_block_components)
       
        # self.prac_block_components = self.run_routine(self.prac_block_components)  -> needs to be implemented
        while self.continueRoutine:
            self.get_current_time(self.routineTimer)
            self.frameN = self.frameN + 1
            self.space_image_7 = self.text_or_image_update(self.space_image_7)
            self.thisExp.timestampOnFlip(self.win, 'space_image_7.started')
            self.waitOnFlip = False
            if self.proceed_17.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.proceed_17 = self.keys_update_1(self.proceed_17)
                self.thisExp.timestampOnFlip(self.win, 'proceed_17.started')
            if self.proceed_17.status == STARTED and not self.waitOnFlip:
                self._proceed_17_allKeys, self.proceed_17 = self.keys_update_2(self.proceed_17, self._proceed_17_allKeys, ['space'])
            self.text_20 = self.text_or_image_update(self.text_20)
            self.thisExp.timestampOnFlip(self.win, 'text_20.started')
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.prac_block_components = self.check_if_components_finished(self.prac_block_components)
            if self.continueRoutine: self.win.flip()
        
        # self.prac_block_components = self.end_routine(self.prac_block_components) --> implement this
        self.prac_block_components = self.hide_components(self.prac_block_components)
        if self.proceed_17.keys in ['', [], None]:
            self.proceed_17.keys = None
        self.block.addData('proceed_17.keys',self.proceed_17.keys)
        if self.proceed_17.keys != None:
            self.block.addData('proceed_17.rt', self.proceed_17.rt)
        self.routineTimer.reset()

    def primer_handler(self):
        self.primer = data.TrialHandler(nReps=1.0, method='random', extraInfo=self.expInfo, originPath=-1, trialList=data.importConditions(self.thisBlock['condition_file'], selection='1'), seed=None, name='primer') 
        self.thisExp.addLoop(self.primer)
        self.thisPrimer = self.primer.trialList[0]
        self.thisPrimer = self.create_variables(self.thisPrimer)
        print(self.thisPrimer)

    def primer_mu(self):
        #self.prepare_routine(primer_mu_components)
        print("WHAT IS GOING ON") 
        self.routine_reset()
        if self.thisPrimer['left'] == 0:                                                       # PROBLEMATIC
            print("left0 ?????????\n")
            pos = 0.07
            if self.lang_keys.keys == 'e':
                self.text_21.setText('Please note that in this block of trials, you will be asked to indicate the probability of finding space crystals on the RIGHT planet. Press SPACEBAR to proceed.')
            else:
                self.text_21.setText('Bitte beachte, dass du in diesem Block die Wahrscheinlichkeit angeben sollst, dass die Weltraumkristalle auf dem RECHTEN Planeten gefunden werden. Drücke die LEERTASTE, um fortzufahren.')
            arrow = 'resources/curved_arrow_right.png'
            arrow_ori = 40;
            left_op = 1;
            right_op = 1;
        else:
            print("not left0 ?????????\n")
            pos = -0.07;
            if self.lang_keys.keys == 'e':
                self.text_21.setText('Please note that in this block of trials, you will be asked to indicate the probability of finding space crystals on the LEFT planet. Press SPACEBAR to proceed.')
            else:
                self.text_21.setText('Bitte beachte, dass du in diesem Block die Wahrscheinlichkeit angeben sollst, dass die Weltraumkristalle auf dem LINKEN Planeten gefunden werden. Drücke die LEERTASTE, um fortzufahren.')
            arrow = 'resources/curved_arrow.png'
            arrow_ori = 320;
            left_op = 1;
            right_op = 1;
        if self.thisPrimer['planet_pos'] == 0:           # ...
            print("planet_pos0 ?????????\n")
            self.left_planet = 'resources/green_blur.png'
            self.right_planet = 'resources/blue_blur.png'
        else:
            print("not planet_pos0 ?????????\n")
            self.left_planet = 'resources/blue_blur.png'
            self.right_planet = 'resources/green_blur.png'
        self.planet_right_6.setOpacity(right_op)
        self.planet_right_6.setPos((0.4, 0.4))
        self.planet_right_6.setImage(self.right_planet)
        self.planet_left_6.setOpacity(left_op)
        self.planet_left_6.setImage(self.left_planet)
        self.arrow_left_3.setPos((pos,0.17))
        self.arrow_left_3.setImage(arrow)
        self.mu_5.reset()
        self.key_resp_3.keys = []
        self.key_resp_3.rt = []
        self._key_resp_3_allKeys = []
        self.mu_ghost.markerPos = None
        self.primer_mu_components = [self.space_bg_12, self.shuttle_5, self.planet_right_6, self.planet_left_6, self.arrow_left_3, self.mu_5, self.text_21, self.key_resp_3]
        self.primer_mu_components = self.keep_track(self.primer_mu_components)
        self.reset_timers()
        
        #self.run_routine(primer_mu_components) --> implement
        while self.continueRoutine:
            self.get_current_time(self.routineTimer)
            self.frameN = self.frameN + 1
            self.space_bg_12 = self.text_or_image_update(self.space_bg_12)
            self.thisExp.timestampOnFlip(self.win, 'space_bg_12.started') # -> huge problem, should only be done once, and now gets done many many times -> ANSWER: add text (eg.: 'space_bg_12.started') argument to the function
            self.shuttle_5 = self.text_or_image_update(self.shuttle_5)
            self.thisExp.timestampOnFlip(self.win, 'shuttle_5.started')
            self.planet_right_6 = self.text_or_image_update(self.planet_right_6)
            self.thisExp.timestampOnFlip(self.win, 'planet_right_6.started')
            self.planet_left_6 = self.text_or_image_update(self.planet_left_6)
            self.thisExp.timestampOnFlip(self.win, 'planet_left_6.started')
            self.arrow_left_3 = self.text_or_image_update(self.arrow_left_3)
            self.thisExp.timestampOnFlip(self.win, 'arrow_left_3.started')
            self.mu_5 = self.text_or_image_update(self.mu_5)
            self.thisExp.timestampOnFlip(self.win, 'mu_5.started')
            self.text_21 = self.text_or_image_update(self.text_21)
            self.thisExp.timestampOnFlip(self.win, 'text_21.started')
            self.waitOnFlip = False
            if self.key_resp_3.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.key_resp_3 = self.keys_update_1(self.key_resp_3)
                self.thisExp.timestampOnFlip(self.win, 'key_resp_3.started')
            if self.key_resp_3.status == STARTED and not self.waitOnFlip:
                self._key_resp_3_allKeys, self.key_resp_3 = self.keys_update_2(self.key_resp_3, self._key_resp_3_allKeys, ['space'])
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.primer_mu_components = self.check_if_components_finished(self.primer_mu_components)
            if self.continueRoutine: self.win.flip()
        
        #self.end_routine(primer_mu_components)
        self.primer_mu_components = self.hide_components(self.primer_mu_components)
        self.primer.addData('mu_5.response', self.mu_5.getRating())
        self.primer.addData('mu_5.rt', self.mu_5.getRT())
        if self.key_resp_3.keys in ['', [], None]:
            self.key_resp_3.keys = None
        self.primer.addData('key_resp_3.keys',self.key_resp_3.keys)
        if self.key_resp_3.keys != None:
            self.primer.addData('key_resp_3.rt', self.key_resp_3.rt)
        self.routineTimer.reset()

    def trials_handler(self):
        self.trials = data.TrialHandler(nReps=1.0, method='random', extraInfo=self.expInfo, originPath=-1, trialList=data.importConditions(self.thisBlock['condition_file'], selection=self.trial_lists), seed=None, name='trials')
        self.thisExp.addLoop(self.trials) 
        self.thisTrial = self.trials.trialList[0]
        self.thisTrial = self.create_variables(self.thisTrial)

    def signal(self): # SPECIFICS!!!
        #self.prepare_routine(signal_components)
        self.routine_reset()
        self.left_patch_7.setContrast(self.thisTrial['con_left'])
        self.right_patch_7.setContrast(self.thisTrial['con_right'])
        self.signal_components = [self.space_image_8, self.radar_3, self.left_patch_7, self.fix_circle_7, self.right_patch_7]
        self.signal_components = self.keep_track(self.signal_components)
        self.reset_timers()
        
        #self.run_routine(signal_components)
        while self.continueRoutine and self.routineTimer.getTime() < 1.0:
            self.get_current_time(self.routineTimer)
            self.frameN = self.frameN + 1 
            if self.space_image_8.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.space_image_8 = self.text_or_image_update(self.space_image_8)
                self.thisExp.timestampOnFlip(self.win, 'space_image_8.started')
            if self.space_image_8.status == STARTED:                 # check out how to delete this or make it a function ***
                if self.tThisFlipGlobal > self.space_image_8.tStartRefresh + 1-self.frameTolerance:
                    self.space_image_8.tStop = self.t
                    self.space_image_8.frameNStop = self.frameN
                    self.thisExp.timestampOnFlip(self.win, 'space_image_8.stopped')
                    self.space_image_8.setAutoDraw(False)
            if self.radar_3.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.radar_3 = self.text_or_image_update(self.radar_3)
                self.thisExp.timestampOnFlip(self.win, 'radar_3.started')
            if self.radar_3.status == STARTED: # ***
                if self.tThisFlipGlobal > self.radar_3.tStartRefresh + 1-self.frameTolerance:
                    self.radar_3.tStop = self.t
                    self.radar_3.frameNStop = self.frameN
                    self.thisExp.timestampOnFlip(self.win, 'radar_3.stopped')
                    self.radar_3.setAutoDraw(False)
            if self.left_patch_7.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.left_patch_7 = self.text_or_image_update(self.left_patch_7)
                self.thisExp.timestampOnFlip(self.win, 'left_patch_7.started')
            if self.left_patch_7.status == STARTED: # ***
                if self.tThisFlipGlobal > self.left_patch_7.tStartRefresh + 1-self.frameTolerance:
                    self.left_patch_7.tStop = self.t
                    self.left_patch_7.frameNStop = self.frameN
                    self.thisExp.timestampOnFlip(self.win, 'left_patch_7.stopped')
                    self.left_patch_7.setAutoDraw(False)
            if self.fix_circle_7.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.fix_circle_7 = self.text_or_image_update(self.fix_circle_7)
                self.thisExp.timestampOnFlip(self.win, 'fix_circle_7.started')
            if self.fix_circle_7.status == STARTED:
                if self.tThisFlipGlobal > self.fix_circle_7.tStartRefresh + 1-self.frameTolerance:
                    self.fix_circle_7.tStop = self.t
                    self.fix_circle_7.frameNStop = self.frameN
                    self.thisExp.timestampOnFlip(self.win, 'fix_circle_7.stopped')
                    self.fix_circle_7.setAutoDraw(False)
            if self.right_patch_7.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.right_patch_7 = self.text_or_image_update(self.right_patch_7)
                self.thisExp.timestampOnFlip(self.win, 'right_patch_7.started')
            if self.right_patch_7.status == STARTED:
                if self.tThisFlipGlobal > self.right_patch_7.tStartRefresh + 1-self.frameTolerance:
                    self.right_patch_7.tStop = self.t
                    self.right_patch_7.frameNStop = self.frameN
                    self.thisExp.timestampOnFlip(self.win, 'right_patch_7.stopped')
                    self.right_patch_7.setAutoDraw(False)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.signal_components = self.check_if_components_finished(self.signal_components)
            if self.continueRoutine: self.win.flip()
        
        #self.end_routine(signal_components)
        self.signal_components = self.hide_components(self.signal_components)
        if self.routineForceEnded: self.routineTimer.reset()
        else: self.routineTimer.addTime(-1.000000)

    def slider(self): # SPECIFICS!!!
        #self.prepare_routine(slider_components)
        self.routine_reset()
        if self.thisPrimer['left'] == 0:
            pos = 0.075
            if self.lang_keys.keys == 'e':
                ques_word = 'Please indicate the probability of finding space crystals on the RIGHT planet.'
            else:
                ques_word = 'Bitte gib die Wahrscheinlichkeit an, auf dem RECHTEN Planeten Weltraumkristalle zu finden.'
            arrow = 'resources/curved_arrow_right.png'
        else:
            pos = -0.075;
            if self.lang_keys.keys == 'e':
                ques_word = 'Please indicate the probability of finding space crystals on the LEFT planet.'
            else:
                ques_word = 'Bitte gib die Wahrscheinlichkeit an, auf dem LINKEN Planeten Weltraumkristalle zu finden.'
            arrow = 'resources/curved_arrow.png'
        if self.thisPrimer['planet_pos'] == 0:
            self.left_planet = 'resources/green_blur.png'
            self.right_planet = 'resources/blue_blur.png'
        else:
            self.left_planet = 'resources/blue_blur.png'
            self.right_planet = 'resources/green_blur.png'
        self.text_22.setText(ques_word)
        self.reported_mu.reset()
        self.planet_right_7.setPos((0.4, 0.4))
        self.planet_right_7.setImage(self.right_planet)
        self.planet_left_7.setImage(self.left_planet)
        self.arrow_left_4.setPos((pos,0.17))
        self.arrow_left_4.setOri(0.0)
        self.arrow_left_4.setImage(arrow)
        self.mu_ghost.marker.opacity = 0.7
        self.mu_ghost.depth = -1.0
        self.slider_3_components = [self.space_bg_13, self.text_22, self.mu_ghost, self.reported_mu, self.shuttle_3, self.planet_right_7, self.planet_left_7, self.arrow_left_4]
        self.slider_3_components = self.keep_track(self.slider_3_components)
        self.reset_timers()
        
        #self.run_routine(slider_components)
        while self.continueRoutine and self.routineTimer.getTime() < 7.5:
            self.get_current_time(self.routineTimer)
            self.frameN = self.frameN + 1
            if self.space_bg_13.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.space_bg_13 = self.text_or_image_update(self.space_bg_13)
                self.thisExp.timestampOnFlip(self.win, 'space_bg_13.started')
            if self.space_bg_13.status == STARTED: # ***
                if self.tThisFlipGlobal > self.space_bg_13.tStartRefresh + 7.5-self.frameTolerance:
                    self.space_bg_13.tStop = self.t
                    self.space_bg_13.frameNStop = self.frameN
                    self.thisExp.timestampOnFlip(self.win, 'space_bg_13.stopped')
                    self.space_bg_13.setAutoDraw(False)
            if self.text_22.status == NOT_STARTED and self.tThisFlip >= 0-self.frameTolerance:
                self.text_22 = self.text_or_image_update(self.text_22)
                self.thisExp.timestampOnFlip(self.win, 'text_22.started')
            if self.text_22.status == STARTED: # ***
                if self.tThisFlip > 7.5-self.frameTolerance:
                    self.text_22.tStop = self.t
                    self.text_22.frameNStop = self.frameN
                    self.thisExp.timestampOnFlip(self.win, 'text_22.stopped')
                    self.text_22.setAutoDraw(False)
            if self.reported_mu.status == NOT_STARTED and self.tThisFlip >= 1.5-self.frameTolerance:
                self.reported_mu = self.text_or_image_update(self.reported_mu)
                self.thisExp.timestampOnFlip(self.win, 'reported_mu.started')
                self.mu_ghost.setAutoDraw(True)                                  # check
            if self.reported_mu.status == STARTED: # ***
                if self.tThisFlipGlobal > self.reported_mu.tStartRefresh + 6-self.frameTolerance:
                    self.reported_mu.tStop = self.t
                    self.reported_mu.frameNStop = self.frameN
                    self.thisExp.timestampOnFlip(self.win, 'reported_mu.stopped')
                    self.mu_ghost.setAutoDraw(False)                             # this too
                    self.reported_mu.setAutoDraw(False)
            if self.reported_mu.getRating() is not None and self.reported_mu.status == STARTED: self.continueRoutine = False
            if self.shuttle_3.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.shuttle_3 = self.text_or_image_update(self.shuttle_3)
                self.thisExp.timestampOnFlip(self.win, 'shuttle_3.started')
            if self.shuttle_3.status == STARTED: # ***
                if self.tThisFlipGlobal > self.shuttle_3.tStartRefresh + 7.5-self.frameTolerance:
                    self.shuttle_3.tStop = self.t
                    self.shuttle_3.frameNStop = self.frameN
                    self.thisExp.timestampOnFlip(self.win, 'shuttle_3.stopped')
                    self.shuttle_3.setAutoDraw(False)                
            if self.planet_right_7.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.planet_right_7 = self.text_or_image_update(self.planet_right_7)
                self.thisExp.timestampOnFlip(self.win, 'planet_right_7.started')
            if self.planet_right_7.status == STARTED:
                if self.tThisFlipGlobal > self.planet_right_7.tStartRefresh + 7.5-self.frameTolerance:
                    self.planet_right_7.tStop = self.t
                    self.planet_right_7.frameNStop = self.frameN
                    self.thisExp.timestampOnFlip(self.win, 'planet_right_7.stopped')
                    self.planet_right_7.setAutoDraw(False)
            if self.planet_left_7.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.planet_left_7 = self.text_or_image_update(self.planet_left_7)
                self.thisExp.timestampOnFlip(self.win, 'planet_left_7.started')
            if self.planet_left_7.status == STARTED:
                if self.tThisFlipGlobal > self.planet_left_7.tStartRefresh + 7.5-self.frameTolerance:
                    self.planet_left_7.tStop = self.t
                    self.planet_left_7.frameNStop = self.frameN 
                    self.thisExp.timestampOnFlip(self.win, 'planet_left_7.stopped')
                    self.planet_left_7.setAutoDraw(False)
            if self.arrow_left_4.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.arrow_left_4 = self.text_or_image_update(self.arrow_left_4)
                self.thisExp.timestampOnFlip(self.win, 'arrow_left_4.started')
            if self.arrow_left_4.status == STARTED:
                if self.tThisFlipGlobal > self.arrow_left_4.tStartRefresh + 7.5-self.frameTolerance:
                    self.arrow_left_4.tStop = self.t
                    self.arrow_left_4.frameNStop = self.frameN
                    self.thisExp.timestampOnFlip(self.win, 'arrow_left_4.stopped')
                    self.arrow_left_4.setAutoDraw(False)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.slider_3_components = self.check_if_components_finished(self.slider_3_components)
            if self.continueRoutine: self.win.flip()
        
        #self.end_routine(slider_components)
        self.slider_3_components = self.hide_components(self.slider_3_components)
        if self.reported_mu.getRating() is not None: mu = self.reported_mu.getRating();
        self.trials.addData('reported_mu.response', self.reported_mu.getRating())
        self.trials.addData('reported_mu.rt', self.reported_mu.getRT())
        if self.reported_mu.getRating() is not None: self.mu_ghost.markerPos = mu # check
        self.mu = mu
        if self.routineForceEnded:
            self.routineTimer.reset()
        else:
            self.routineTimer.addTime(-7.500000)
        self.thisExp.nextEntry()

    def prechoice_text(self):
        #self.prepare_routine(prechoice_text_components)
        self.routine_reset()
        if self.lang_keys.keys == 'e':
            instr='Before you provide advise to the spaceship, you will be shown your reported probability on the latest trial.\n\nPlease use the analysis of the radar signals that you conducted throughout the block, to inform the spaceship.\n\nPress SPACEBAR to proceed.'
        else:
            self.instr='Bevor du den Astronaut:innen deinen Ratschlag erteilst, wird dir deine gemeldete Wahrscheinlichkeit für den letzten Versuch angezeigt.\n\nBitte verwende die Analyse der Radarsignale, die du während des gesamten Blocks durchgeführt hast, um das Raumschiff zu informieren.\n\nDrücke die LEERTASTE, um fortzufahren.'
        self.text_23.setText(instr)
        self.key_resp_4.keys = []
        self.key_resp_4.rt = []
        self._key_resp_4_allKeys = []
        self.prechoice_text_components = [self.space_bg_14, self.text_23, self.key_resp_4]
        self.prechoice_text_components = self.keep_track(self.prechoice_text_components)
        self.reset_timers()
        
        #self.run_routine(prechoice_text_components)
        while self.continueRoutine:
            self.get_current_time(self.routineTimer)
            self.frameN = self.frameN + 1                        
            if self.space_bg_14.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.space_bg_14 = self.text_or_image_update(self.space_bg_14)
                self.thisExp.timestampOnFlip(self.win, 'space_bg_14.started')
            if self.text_23.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.text_23 = self.text_or_image_update(self.text_23)
                self.thisExp.timestampOnFlip(self.win, 'text_23.started')
            self.waitOnFlip = False
            if self.key_resp_4.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.key_resp_4 = self.keys_update_1(self.key_resp_4)
                self.thisExp.timestampOnFlip(self.win, 'key_resp_4.started')
            if self.key_resp_4.status == STARTED and not self.waitOnFlip:
                self._key_resp_4_allKeys, self.key_resp_4 = self.keys_update_2(self.key_resp_4, self._key_resp_4_allKeys, ['space'])
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.prechoice_text_components = self.check_if_components_finished(self.prechoice_text_components)
            if self.continueRoutine: self.win.flip()
        
        #self.end_routine(prechoice_text_components)
        self.prechoice_text_components = self.hide_components(self.prechoice_text_components)
        if self.key_resp_4.keys in ['', [], None]: self.key_resp_4.keys = None
        self.block.addData('key_resp_4.keys',self.key_resp_4.keys)
        if self.key_resp_4.keys != None: self.block.addData('key_resp_4.rt', self.key_resp_4.rt)
        self.routineTimer.reset()

    def last_handler(self):
        self.last = data.TrialHandler(nReps=1.0, method='random', extraInfo=self.expInfo, originPath=-1, trialList=data.importConditions(self.thisBlock['condition_file'], selection='1'), seed=None, name='last')
        self.thisExp.addLoop(self.last)
        self.thisLast = self.last.trialList[0]
        self.thisLast = self.create_variables(self.thisLast)
        

    def last_mu(self): # SPECIFICS!
        #self.prepare_routine(last_mu_components)
        self.routine_reset()
        self.mu_7.markerPos = self.mu; # check
        if self.thisPrimer['left'] == 0:
            pos = 0.07
            if self.lang_keys.keys == 'e':
                ques_word = 'On the last trial, you reported that the probability of finding space crystals on the RIGHT planet is '
            else:
                ques_word='Beim letzten Versuch hast du angegeben, dass die Wahrscheinlichkeit, auf dem RECHTEN Planeten Weltraumkristalle zu finden, wie folgt ist '
            arrow = 'resources/curved_arrow_right.png'
            arrow_ori = 40;
            left_op = 1;
            right_op = 1;
        else:
            pos = -0.07;
            if self.lang_keys.keys == 'e':
                ques_word = 'On the last trial, you reported that the probability of finding space crystals on the LEFT planet is '
            else:
                ques_word='Beim letzten Versuch hast du angegeben, dass die Wahrscheinlichkeit, Weltraumkristalle auf dem LINKEN Planeten zu finden, wie folgt ist '
            arrow = 'resources/curved_arrow.png'
            arrow_ori = 320;
            left_op = 1;
            right_op = 1;
        if self.thisPrimer['planet_pos'] == 0:
            self.left_planet = 'resources/green_blur.png'
            self.right_planet = 'resources/blue_blur.png'
        else:
            self.left_planet = 'resources/blue_blur.png'
            self.right_planet = 'resources/green_blur.png'
        self.planet_right_8.setOpacity(right_op)
        self.planet_right_8.setPos((0.4, 0.4))
        self.planet_right_8.setImage(self.right_planet)
        self.planet_left_8.setOpacity(left_op)
        self.planet_left_8.setImage(self.left_planet)
        self.arrow_left_5.setPos((pos, 0.17))
        self.arrow_left_5.setOri(0.0)
        self.arrow_left_5.setImage(arrow)
        self.mu_7.reset()
        self.text_24.setText(ques_word)
        self.key_resp_5.keys = []
        self.key_resp_5.rt = []
        self._key_resp_5_allKeys = []
        self.last_mu_components = [self.space_bg_15, self.shuttle_6, self.planet_right_8, self.planet_left_8, self.arrow_left_5, self.mu_7, self.text_24, self.key_resp_5, self.text_31]
        self.last_mu_components = self.keep_track(self.last_mu_components)
        self.reset_timers()
        
        #self.run_routine(last_mu_components)
        while self.continueRoutine:
            self.get_current_time(self.routineTimer)
            self.frameN = self.frameN + 1
            if self.space_bg_15.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.space_bg_15 = self.text_or_image_update(self.space_bg_15)
                self.thisExp.timestampOnFlip(self.win, 'space_bg_15.started')
            self.mu_7.markerPos = self.mu;
            if self.shuttle_6.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.shuttle_6 = self.text_or_image_update(self.shuttle_6)
                self.thisExp.timestampOnFlip(self.win, 'shuttle_6.started')
            if self.planet_right_8.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.planet_right_8 = self.text_or_image_update(self.planet_right_8)
                self.thisExp.timestampOnFlip(self.win, 'planet_right_8.started')
            if self.planet_left_8.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.planet_left_8 = self.text_or_image_update(self.planet_left_8)
                self.thisExp.timestampOnFlip(self.win, 'planet_left_8.started')
            if self.arrow_left_5.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.arrow_left_5 = self.text_or_image_update(self.arrow_left_5)
                self.thisExp.timestampOnFlip(self.win, 'arrow_left_5.started')
            if self.mu_7.status == NOT_STARTED and self.tThisFlip >= 0-self.frameTolerance:
                self.mu_7 = self.text_or_image_update(self.mu_7)
            if self.text_24.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.text_24 = self.text_or_image_update(self.text_24)
                self.thisExp.timestampOnFlip(self.win, 'text_24.started')
            self.waitOnFlip = False
            if self.key_resp_5.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.key_resp_5 = self.keys_update_1(self.key_resp_5)
                self.thisExp.timestampOnFlip(self.win, 'key_resp_5.started')
            if self.key_resp_5.status == STARTED and not self.waitOnFlip:
                self._key_resp_5_allKeys, self.key_resp_5 = self.keys_update_2(self.key_resp_5, self._key_resp_5_allKeys, ['space'])
            if self.text_31.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.text_31 = self.text_or_image_update(self.text_31)
                self.thisExp.timestampOnFlip(self.win, 'text_31.started')
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.last_mu_components = self.check_if_components_finished(self.last_mu_components)
            if self.continueRoutine: self.win.flip()
        
        #self.end_routine(last_mu_components)
        self.last_mu_components = self.hide_components(self.last_mu_components)
        self.last.addData('mu_7.response', self.mu_7.getRating())
        self.last.addData('mu_7.rt', self.mu_7.getRT())
        if self.reported_mu.getRating() is not None: self.mu_ghost.markerPos = self.mu
        if self.key_resp_5.keys in ['', [], None]: self.key_resp_5.keys = None
        self.last.addData('key_resp_5.keys',self.key_resp_5.keys)
        if self.key_resp_5.keys != None: self.last.addData('key_resp_5.rt', self.key_resp_5.rt)
        self.routineTimer.reset()

    def block_choice(self): # SPECIFICS
        #self.prepare_routine(block_choice_components)
        self.routine_reset()
        if self.lang_keys.keys == 'e':
            self.text_25.setText('Please make a choice about which planet you want the spaceship to go to.\n\nTo make a choice, you need to click on the planet which you want to send the spaceship to. ')
        else:
            self.text_25.setText('Bitte entscheide dich für einen Planeten, zu dem das Raumschiff fliegen soll.\n\nUm eine Wahl zu treffen, musst du auf den Planeten klicken, zu dem du das Raumschiff schicken willst.')
        self.planet_right_9.setPos((0.4, 0.4))
        self.planet_right_9.setImage(self.right_planet)
        self.planet_left_9.setImage(self.left_planet)
        if self.thisPrimer['planet_pos'] == 0: # ???? watch out -> is it always from the Primer or maybe also depending on the block (is there even a difference)
            self.left_planet = 'resources/green_blur.png'
            self.right_planet = 'resources/blue_blur.png'
        else:
            self.left_planet = 'resources/blue_blur.png'
            self.right_planet = 'resources/green_blur.png'
        self.mouse_resp.x = []
        self.mouse_resp.y = []
        self.mouse_resp.leftButton = []
        self.mouse_resp.midButton = []
        self.mouse_resp.rightButton = []
        self.mouse_resp.time = []
        self.mouse_resp.clicked_name = []
        self.gotValidClick = False
        self.block_choice_components = [self.space_bg_16, self.shuttle_7, self.planet_right_9, self.planet_left_9, self.text_25, self.question, self.mouse_resp]
        self.block_choice_components = self.keep_track(self.block_choice_components)
        self.reset_timers()
        
        #self.run_routine(block_choice_components)
        while self.continueRoutine:
            self.get_current_time(self.routineTimer)
            self.frameN = self.frameN + 1
            if self.space_bg_16.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.space_bg_16 = self.text_or_image_update(self.space_bg_16)
                self.thisExp.timestampOnFlip(self.win, 'space_bg_16.started')
            if self.shuttle_7.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.shuttle_7 = self.text_or_image_update(self.shuttle_7)
                self.thisExp.timestampOnFlip(self.win, 'shuttle_7.started')
            if self.planet_right_9.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.planet_right_9 = self.text_or_image_update(self.planet_right_9)
                self.thisExp.timestampOnFlip(self.win, 'planet_right_9.started')
            if self.planet_left_9.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.planet_left_9 = self.text_or_image_update(self.planet_left_9)
                self.thisExp.timestampOnFlip(self.win, 'planet_left_9.started')
            if self.text_25.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.text_25 = self.text_or_image_update(self.text_25)
                self.thisExp.timestampOnFlip(self.win, 'text_25.started')
            if self.question.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.question = self.text_or_image_update(self.question)
                self.thisExp.timestampOnFlip(self.win, 'question.started')
            if self.mouse_resp.status == NOT_STARTED and self.t >= 0.0-self.frameTolerance: # I SHOULD ADD A NEW FUNCTION FOR THIS
                # keep track of start time/frame for later
                self.mouse_resp.frameNStart = self.frameN  # exact frame index
                self.mouse_resp.tStart = self.t  # local t and not account for scr refresh
                self.mouse_resp.tStartRefresh = self.tThisFlipGlobal  # on global time
                self.win.timeOnFlip(self.mouse_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                self.thisExp.addData('mouse_resp.started', self.t)
                self.mouse_resp.status = STARTED
                self.mouse_resp.mouseClock.reset()
                self.prevButtonState = self.mouse_resp.getPressed()  # if button is down already this ISN'T a new click
            if self.mouse_resp.status == STARTED:  # only update if started and not finished!
                self.buttons = self.mouse_resp.getPressed()
                if self.buttons != self.prevButtonState:  # button state changed?
                    self.prevButtonState = self.buttons
                    if sum(self.buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        self.gotValidClick = False
                        try:
                            iter([self.planet_right_9,self.planet_left_9])
                            self.clickableList = [self.planet_right_9,self.planet_left_9]
                        except:
                            self.clickableList = [[self.planet_right_9,self.planet_left_9]]
                        for obj in self.clickableList:
                            if obj.contains(self.mouse_resp):
                                self.gotValidClick = True
                                self.mouse_resp.clicked_name.append(obj.name)
                        if self.gotValidClick:
                            self.x, self.y = self.mouse_resp.getPos()
                            self.mouse_resp.x.append(self.x)
                            self.mouse_resp.y.append(self.y)
                            self.buttons = self.mouse_resp.getPressed()
                            self.mouse_resp.leftButton.append(self.buttons[0])
                            self.mouse_resp.midButton.append(self.buttons[1])
                            self.mouse_resp.rightButton.append(self.buttons[2])
                            self.mouse_resp.time.append(self.mouse_resp.mouseClock.getTime())
                        if self.gotValidClick:
                            self.continueRoutine = False  # abort routine on response
            
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.block_choice_components = self.check_if_components_finished(self.block_choice_components)
            if self.continueRoutine: self.win.flip()
        
        #self.end_routine(block_choice_components)
        self.block_choice_components = self.hide_components(self.block_choice_components)
        if self.mouse_resp.clicked_name[0] == 'planet_left_9':
            self.text_pos = 0.2;
            self.pos_planet = -0.4;
            self.ship_pos = -0.19;
            self.ship_ori = 305;
            self.crystal_pos = 0.5;
            if self.thisPrimer['planet_pos'] == 0: # check (planet_pos before)
                self.image = 'resources/green_blur.png'
            else:
                self.image = 'resources/blue_blur.png'
        else:
            self.text_pos = -0.4;
            self.pos_planet = 0.4;
            self.ship_pos = -0.19;
            self.ship_ori = 45;
            self.crystal_pos = -0.1;
            if self.thisPrimer['planet_pos'] == 0: # check
                self.image = 'resources/blue_blur.png'
            else:
                self.image = 'resources/green_blur.png'
                
        if self.mouse_resp.clicked_name[0] == self.thisBlock['corr']: # not sure about thisBlock['corr'] (it was only == corr before)
            if self.thisPrimer['condition'] == 1: # check (maybe thisBlock instead)
                self.prob = 0.7 
                self.block_rew = self.cond1_rew[self.block_num]#generate_zero_or_one(prob)
            else:
                self.prob = 0.9
                self.block_rew = self.cond2_rew[self.block_num] #generate_zero_or_one(prob)
        else:
            if self.thisPrimer['condition'] == 1: # check (maybe thisBlock instead)
                self.prob = 0.3
                self.block_rew = 1-self.cond1_rew[self.block_num] #generate_zero_or_one(prob)
            else:
                self.prob = 0.1
                self.block_rew = 1-self.cond2_rew[self.block_num] #generate_zero_or_one(prob)
        
        if self.block_rew == 1:
            if self.lang_keys.keys == 'e':
                self.str4 = "Space crystal found!\n"
            else:
                self.str4='Weltraumkristall gefunden!\n'
            self.op = 0.7;
        else:
            if self.lang_keys.keys == 'e':
                self.str4 = "No crystals found!\n"
            else:
                self.str4='Keine Weltraumkristalle gefunden.\n'
            self.op = 0;
        
        if self.lang_keys.keys == 'e':
            self.str1 = "You win"
            self.str2 = str(self.block_rew)
            self.str3 = " "+"points!" 
        else:
            self.str1 = "Du gewinnst "
            self.str2 = str(self.block_rew)
            if self.block_rew == 1:
                self.str3 = " "+"Punkt!" 
            else:
                self.str3 = " "+"Punkte!" 
        
        self.block_num = self.block_num + 1;
        
        self.rew = self.str4 + " " +self.str1 + " " + self.str2 + " " + self.str3
        self.task_rew = self.task_rew + self.block_rew;
        self.thisExp.addData('block_points', self.block_rew)
        self.block.addData('mouse_resp.x', self.mouse_resp.x)
        self.block.addData('mouse_resp.y', self.mouse_resp.y)
        self.block.addData('mouse_resp.leftButton', self.mouse_resp.leftButton)
        self.block.addData('mouse_resp.midButton', self.mouse_resp.midButton)
        self.block.addData('mouse_resp.rightButton', self.mouse_resp.rightButton)
        self.block.addData('mouse_resp.time', self.mouse_resp.time)
        self.block.addData('mouse_resp.clicked_name', self.mouse_resp.clicked_name)
        self.routineTimer.reset()

    def block_reward(self):
        #self.prepare_routine(block_reward_components)
        self.routine_reset()
        self.proceed_18.keys = []
        self.proceed_18.rt = []
        self._proceed_18_allKeys = []
        self.text_26.setPos((self.text_pos + 0.2, 0))
        self.text_26.setText(self.rew)
        self.planet.setPos((self.pos_planet + 0.05, 0))
        self.planet.setImage(self.image)
        self.shuttle_8.setPos((0, self.ship_pos))
        self.shuttle_8.setOri(self.ship_ori)
        self.ori = 0;
        self.crystal.setOpacity(self.op)
        self.crystal.setPos((self.crystal_pos, 0 + 0.1))
        self.block_rew_components = [self.space_bg_17, self.proceed_18, self.text_26, self.planet, self.shuttle_8, self.crystal]
        self.block_rew_components = self.keep_track(self.block_rew_components)
        self.reset_timers()
        
        #self.run_routine(block_reward_components)
        while self.continueRoutine:
            self.get_current_time(self.routineTimer)
            self.frameN = self.frameN + 1
            if self.space_bg_17.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.space_bg_17 = self.text_or_image_update(self.space_bg_17)
                self.thisExp.timestampOnFlip(self.win, 'space_bg_17.started')
            self.waitOnFlip = False
            if self.proceed_18.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.proceed_18 = self.keys_update_1(self.proceed_18)
                self.thisExp.timestampOnFlip(self.win, 'proceed_18.started')
            if self.proceed_18.status == STARTED and not self.waitOnFlip:
                self._proceed_18_allKeys, self.proceed_18 = self.keys_update_2(self.proceed_18, self._proceed_18_allKeys, ['space'])
            if self.text_26.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.text_26 = self.text_or_image_update(self.text_26)
                self.thisExp.timestampOnFlip(self.win, 'text_26.started')
            if self.planet.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.planet = self.text_or_image_update(self.planet)
                self.thisExp.timestampOnFlip(self.win, 'planet.started')
            if self.shuttle_8.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.shuttle_8 = self.text_or_image_update(self.shuttle_8)
                self.thisExp.timestampOnFlip(self.win, 'shuttle_8.started')
            if self.crystal.status == STARTED:
                self.crystal.setOri(1,'+')
                self.crystal.draw()
            if self.crystal.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.crystal = self.text_or_image_update(self.crystal)
                self.thisExp.timestampOnFlip(self.win, 'crystal.started')
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.block_rew_components = self.check_if_components_finished(self.block_rew_components)
            if self.continueRoutine: self.win.flip()
        
        
        #self.end_routine(block_reward_components)
        self.block_rew_components = self.hide_components(self.block_rew_components)
        if self.proceed_18.keys in ['', [], None]: self.proceed_18.keys = None
        self.block.addData('proceed_18.keys',self.proceed_18.keys)
        if self.proceed_18.keys != None: self.block.addData('proceed_18.rt', self.proceed_18.rt)
        if self.lang_keys.keys == 'e':
            self.str1 = "You completed"
            self.str2 = " " + str(self.block_num)
            self.str3 = " " + "out of"
            self.str4 = " " + str(self.total_blocks)
            self.str5 = " " + "blocks."
            self.str6 = "\n Press SPACEBAR to proceed."
        else:
            self.str1 = "Du hast"
            self.str2 = " " + str(self.block_num)
            self.str3 = " " + "von"
            self.str4 = " " + str(self.total_blocks)
            self.str5 = " " + "Blöcken abgeschlossen."
            self.str6 = "\n Drücke die LEERTASTE, um fortzufahren."
        self.block_str = self.str1 + self.str2 + self.str3 + self.str4 + self.str5 + self.str6
        self.routineTimer.reset()

    def block_completed(self):
        #self.prepare_routine(block_completed_components)
        self.routine_reset()
        self.proceed_19.keys = []
        self.proceed_19.rt = []
        self._proceed_19_allKeys = []
        self.text_27.setPos((0, 0))
        self.text_27.setText(self.block_str)
        self.block_completed_components = [self.space_bg_18, self.proceed_19, self.text_27]
        self.block_completed_components = self.keep_track(self.block_completed_components)
        self.reset_timers()
        
        #self.run_routine(block_completed_components)
        while self.continueRoutine:
            self.t = self.routineTimer.getTime()
            self.tThisFlip = self.win.getFutureFlipTime(clock=self.routineTimer)
            self.tThisFlipGlobal = self.win.getFutureFlipTime(clock=None)
            self.frameN = self.frameN + 1 
            if self.space_bg_18.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.space_bg_18 = self.text_or_image_update(self.space_bg_18)
                self.thisExp.timestampOnFlip(self.win, 'space_bg_18.started')
            self.waitOnFlip = False
            if self.proceed_19.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.proceed_19 = self.keys_update_1(self.proceed_19)
                self.thisExp.timestampOnFlip(self.win, 'proceed_19.started')
            if self.proceed_19.status == STARTED and not self.waitOnFlip:
                self._proceed_19_allKeys, self.proceed_19 = self.keys_update_2(self.proceed_19, self._proceed_19_allKeys, ['space'])
            if self.text_27.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.text_27 = self.text_or_image_update(self.text_27)
                self.thisExp.timestampOnFlip(self.win, 'text_27.started')
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.block_completed_components = self.check_if_components_finished(self.block_completed_components)
            if self.continueRoutine: self.win.flip()
        
        #self.end_routine(block_completed_components)
        self.block_completed_components = self.hide_components(self.block_completed_components)
        if self.proceed_19.keys in ['', [], None]: self.proceed_19.keys = None
        self.block.addData('proceed_19.keys',self.proceed_19.keys)
        if self.proceed_19.keys != None: self.block.addData('proceed_19.rt', self.proceed_19.rt)
        self.routineTimer.reset()
        self.thisExp.nextEntry()
        
        

    def task_score(self):
        #self.prepare_routine(task_score_components)
        self.routine_reset()
        if self.lang_keys.keys == 'e':
            self.text_28.setText("You win " + str(self.task_rew) + " "+ "points in these set of blocks!")
        else:
            self.text_28.setText("Du gewinnst " + str(self.task_rew) + " "+ "Punkte in diesem Satz von Blöcken!")
        self.proceed_20.keys = []
        self.proceed_20.rt = []
        self._proceed_20_allKeys = []
        self.task_score_components = [self.space_bg_19, self.text_28, self.proceed_20]
        self.task_score_components = self.keep_track(self.task_score_components)
        self.reset_timers()
        
        #self.run_routine(task_score_components)
        while self.continueRoutine:
            self.get_current_time(self.language_preferenceClock)
            self.frameN = self.frameN + 1
            if self.space_bg_19.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.space_bg_19 = self.text_or_image_update(self.space_bg_19)
                self.thisExp.timestampOnFlip(self.win, 'space_bg_19.started')
            if self.text_28.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.text_28 = self.text_or_image_update(self.text_28)
                self.thisExp.timestampOnFlip(self.win, 'text_28.started')
            self.waitOnFlip = False
            if self.proceed_20.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.proceed_20 = self.keys_update_1(self.proceed_20)
                self.thisExp.timestampOnFlip(self.win, 'proceed_20.started')
            if self.proceed_20.status == STARTED and not self.waitOnFlip:
                self._proceed_20_allKeys, self.proceed_20 = self.keys_update_2(self.proceed_20, self._proceed_20_allKeys, ['space'])
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.task_score_components = self.check_if_components_finished(self.task_score_components)
            if self.continueRoutine: self.win.flip()
        
        #self.end_routine(task_score_components)
        self.task_score_components = self.hide_components(self.task_score_components)
        if self.proceed_20.keys in ['', [], None]: self.proceed_20.keys = None
        self.prac_main_task.addData('proceed_20.keys',self.proceed_20.keys)
        if self.proceed_20.keys != None: self.prac_main_task.addData('proceed_20.rt', self.proceed_20.rt)
        self.routineTimer.reset()
        

    def end_experiment(self):
        if self.block_num == self.total_blocks:
            self.win.flip()
            self.thisExp.saveAsWideText(self.filename+'.csv', delim='auto')
            self.thisExp.saveAsPickle(self.filename)
            logging.flush()
            if self.eyetracker: self.eyetracker.setConnectionState(False)
            self.thisExp.abort()
            self.win.close()
            core.quit()