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
from functions import keep_track, reset_timers, get_current_time, text_or_image_update, keys_update_1, keys_update_2, check_if_components_finished, hide_components

# DIRECTORY CHECKS & EXPERIMENT INFO
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
psychopyVersion = '2022.2.5'
expName = 'space_task_offline'
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}

# PARTICIPANT INFO DIALOG
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName) # create a function for that
if dlg.OK == False: core.quit()
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# FILENAME ASSIGNMENT
filename = _thisDir + os.sep + u'data/%s_%s' % (expInfo['participant'], expName)

# EXPERIMENT HANDLER FOR DATA SAVING & LOG FILE
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\prash\\Nextcloud\\Thesis_laptop\\Semester 6\\pavlovia_offline\\space_task_offline.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)

# VARIABLE INITIALIZATION
import random
from random import shuffle
endExpNow = False
frameTolerance = 0.001
task_rew = 0
rew = 'hello'
block_str = 'hello'
number_list = [1,2,3,4]
random.shuffle(number_list)
task_str = "hello"
lists = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
block_lists = lists
random.shuffle(block_lists);
print(block_lists);
x = [0]#,1,2]#,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]                      # manipulate trials
random.shuffle(x);
trial_lists = x;
ques_word = 'hello'
total_blocks = 16;
block_num = 0;
cond1_rew = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0];
cond2_rew = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0];
random.shuffle(cond1_rew);
random.shuffle(cond2_rew);
task_str = 'hello'
mu = 0

# WINDOW SETUP
win = visual.Window(size=[1536, 864], fullscr=True, screen=0, winType='pyglet', allowStencil=False, monitor='testMonitor', color=[0,0,0], colorSpace='rgb', blendMode='avg', useFBO=True, units='height')
win.mouseVisible = False
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0

# SETUP DEVICES & KEYBOARD
ioConfig = {}
ioConfig['Keyboard'] = dict(use_keymap='psychopy') 
ioSession = '1'
if 'session' in expInfo: ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# INITIALIZE 'LANGUAGE PREFERENCE'
language_preferenceClock = core.Clock()
text_101 = visual.TextStim(win=win, name='text_101', text='Bitte gib an, welche Sprache du für die Instruktionen bevorzugst.\n\nDrücke G für Deutsch. \nDrücke E für Englisch.\n\nIndicate the language that you prefer for the task instructions.\n\nPress G for German. \nPress E for English.', font='Times New Roman', pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0,  color='black', colorSpace='rgb', opacity=None,  languageStyle='LTR', depth=0.0);
lang_keys = keyboard.Keyboard() 

# INITIALIZE 'PRAC_BLOCK'
space_image_7 = visual.ImageStim(win=win, name='space_image_7', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-1.0)
proceed_17 = keyboard.Keyboard()
text_20 = visual.TextStim(win=win, name='text_20', text='', font='Times New Roman', pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-3.0);

# INITIALIZE 'PRIMER_MU'                    # -> create xlsx table with all values for space background -> import -> replace e.g. ori=0.o with table.whatever
space_bg_12 = visual.ImageStim(win=win, name='space_bg_12', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
shuttle_5 = visual.ImageStim(win=win, name='shuttle_5', image='resources/space-shuttle.png', mask=None, anchor='center', ori=0.0, pos=(0, -0.15), size=(0.2, 0.2), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-2.0)
planet_right_6 = visual.ImageStim(win=win, name='planet_right_6', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-3.0)
planet_left_6 = visual.ImageStim(win=win, name='planet_left_6', image='sin', mask=None, anchor='center', ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-4.0)
arrow_left_3 = visual.ImageStim(win=win, name='arrow_left_3', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.2,0.35), color=[1,1,1], colorSpace='rgb', opacity=0.5, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-5.0)
mu_5 = visual.Slider(win=win, name='mu_5', startValue=None, size=(0.8, 0.03), pos=(0, -0.38), units=None, labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0, style='rating', styleTweaks=(), opacity=None, labelColor=[0.8824, 0.9451, 1.0000], markerColor=[1.0000, 1.0000, 1.0000], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb', font='Times New Roman', labelHeight=0.03, flip=False, ori=0.0, depth=-6, readOnly=True)
text_21 = visual.TextStim(win=win, name='text_21', text='', font='Times New Roman', pos=(0, -0.3), height=0.03, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-7.0);
key_resp_3 = keyboard.Keyboard()

# INITIALIZE 'SIGNAL'
space_image_8 = visual.ImageStim(win=win, name='space_image_8', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
radar_3 = visual.ImageStim(win=win, name='radar_3', image='resources/radar_grayl.png', mask=None, anchor='center', ori=0.0, pos=(0,0), size=(0.6, 0.6), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-1.0)
left_patch_7 = visual.GratingStim(win=win, name='left_patch_7', tex='sin', mask='gauss', anchor='center', ori=0.0, pos=(-0.12, 0), size=(0.12, 0.12), sf=8.0, phase=0.0, color=[1,1,1], colorSpace='rgb', opacity=None, contrast=1.0, blendmode='avg', texRes=512.0, interpolate=True, depth=-2.0)
fix_circle_7 = visual.ShapeStim(win=win, name='fix_circle_7', size=(0.007, 0.007), vertices='circle', ori=0.0, pos=(0, 0), anchor='center', lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black', opacity=None, depth=-3.0, interpolate=True)
right_patch_7 = visual.GratingStim(win=win, name='right_patch_7', tex='sin', mask='gauss', anchor='center', ori=0.0, pos=(0.12, 0), size=(0.12, 0.12), sf=8.0, phase=0.0, color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, contrast=1.0, blendmode='avg', texRes=512.0, interpolate=True, depth=-4.0)

# INITIALIZE 'SLIDER_3'
space_bg_13 = visual.ImageStim(win=win, name='space_bg_13', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
text_22 = visual.TextStim(win=win, name='text_22', text='', font='Times New Roman', pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0.0, color=[0.8824, 0.9451, 1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0);
reported_mu = visual.Slider(win=win, name='reported_mu', startValue=50, size=(0.8, 0.03), pos=(0, -0.38), units=None, labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0, style='rating', styleTweaks=(), opacity=None, labelColor=[0.8824, 0.9451, 1.0000], markerColor=[1.0000, 1.0000, 1.0000], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb', font='Times New Roman', labelHeight=0.03, flip=False, ori=0.0, depth=-3, readOnly=False)
mu_ghost = visual.Slider(win=win, name='mu_ghost', startValue=None, size=(0.8, 0.03), pos=(0, -0.38), units=None, labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0, style='rating', styleTweaks=(), opacity=0, labelColor=[0.8824, 0.9451, 1.0000], markerColor=[-0.4980, 0.7569, 0.6314], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb', font='Times New Roman', labelHeight=0.03, flip=False, ori=0.0, depth=-6.0, readOnly=True)
shuttle_3 = visual.ImageStim(win=win, name='shuttle_3', image='resources/space-shuttle.png', mask=None, anchor='center', ori=0.0, pos=(0, -0.15), size=(0.2, 0.2), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-4.0)
planet_right_7 = visual.ImageStim(win=win, name='planet_right_7', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-5.0)
planet_left_7 = visual.ImageStim(win=win, name='planet_left_7', image='sin', mask=None, anchor='center', ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-6.0)
arrow_left_4 = visual.ImageStim(win=win, name='arrow_left_4', image='sin', mask=None, anchor='center', ori=1.0, pos=[0,0], size=(0.2,0.35), color=[1,1,1], colorSpace='rgb', opacity=0.5, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-7.0)

# INITIALIZE 'PRECHOICE_TEXT'
space_bg_14 = visual.ImageStim(win=win, name='space_bg_14', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
text_23 = visual.TextStim(win=win, name='text_23', text='', font='Times New Roman', pos=(0, 0), height=0.03, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-1.0);
key_resp_4 = keyboard.Keyboard()

# INITIALIZE 'LAST_MU'
space_bg_15 = visual.ImageStim(win=win, name='space_bg_15', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
shuttle_6 = visual.ImageStim(win=win, name='shuttle_6', image='resources/space-shuttle.png', mask=None, anchor='center', ori=0.0, pos=(0, -0.15), size=(0.2, 0.2), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-2.0)
planet_right_8 = visual.ImageStim(win=win, name='planet_right_8', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-3.0)
planet_left_8 = visual.ImageStim(win=win, name='planet_left_8', image='sin', mask=None, anchor='center', ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-4.0)
arrow_left_5 = visual.ImageStim(win=win, name='arrow_left_5', image='sin', mask=None, anchor='center', ori=1.0, pos=[0,0], size=(0.2,0.35), color=[1,1,1], colorSpace='rgb', opacity=0.5, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-5.0)
mu_7 = visual.Slider(win=win, name='mu_7', startValue=mu, size=(0.8, 0.03), pos=(0, -0.38), units=None, labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0, style='rating', styleTweaks=(), opacity=None, labelColor=[0.8824, 0.9451, 1.0000], markerColor=[-0.4980, 0.7569, 0.6314], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb', font='Times New Roman', labelHeight=0.03, flip=False, ori=0.0, depth=-6, readOnly=True)
text_24 = visual.TextStim(win=win, name='text_24', text='', font='Times New Roman', pos=(0, -0.3), height=0.03, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-7.0);
key_resp_5 = keyboard.Keyboard()
text_31 = visual.TextStim(win=win, name='text_31', text='Press SPACEBAR to proceed.', font='Times New Roman', pos=(0, -0.45), height=0.02, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-9.0);

# INITIALIZE 'BLOCK_CHOICE'
space_bg_16 = visual.ImageStim(win=win, name='space_bg_16', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
shuttle_7 = visual.ImageStim(win=win, name='shuttle_7', image='resources/space-shuttle.png', mask=None, anchor='center', ori=0.0, pos=(0, -0.135), size=(0.2, 0.2), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-1.0)
planet_right_9 = visual.ImageStim(win=win, name='planet_right_9', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-2.0)
planet_left_9 = visual.ImageStim(win=win, name='planet_left_9', image='sin', mask=None, anchor='center', ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-3.0)
text_25 = visual.TextStim(win=win, name='text_25', text='', font='Times New Roman', pos=(0, -0.35), height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-4.0);
question = visual.ImageStim(win=win, name='question', image='resources/question-mark.png', mask=None, anchor='center', ori=0.0, pos=(0, 0.05), size=(0.1, 0.1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-6.0)
mouse_resp = event.Mouse(win=win)
x, y = [None, None]
mouse_resp.mouseClock = core.Clock()

# INITIALIZE 'BLOCK_REW'
space_bg_17 = visual.ImageStim(win=win, name='space_bg_17', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
proceed_18 = keyboard.Keyboard()
text_26 = visual.TextStim(win=win, name='text_26',text='', font='Open Sans', pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0);
planet = visual.ImageStim(win=win, name='planet', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.5, 0.5), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-3.0)
shuttle_8 = visual.ImageStim(win=win, name='shuttle_8', image='resources/shuttle_fire.png', mask=None, anchor='center', ori=1.0, pos=[0,0], size=(0.2, 0.3), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-4.0)
crystal = visual.ImageStim(win=win, name='crystal', image='resources/crystal.png', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.1, 0.1), color=[1,1,1], colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-6.0)

# INITIALIZE 'BLOCK_COMPLETED'
space_bg_18 = visual.ImageStim(win=win, name='space_bg_18', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
proceed_19 = keyboard.Keyboard()
text_27 = visual.TextStim(win=win, name='text_27', text='', font='Times New Roman', pos=[0,0], height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0);

# INITIALIZE 'TASK_SCORE'
space_bg_19 = visual.ImageStim(win=win, name='space_bg_19', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-1.0)
text_28 = visual.TextStim(win=win, name='text_28', text='', font='Times New Roman', pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0);
proceed_20 = keyboard.Keyboard()

# CREATE HANDY TIMERS
globalClock = core.Clock()
routineTimer = core.Clock()

# PREPARE 'LANGUAGE PREFERENCE'
continueRoutine = True
lang_keys.keys = []
lang_keys.rt = []
_lang_keys_allKeys = []
language_preferenceComponents = [text_101, lang_keys]
language_preferenceComponents = keep_track(language_preferenceComponents)
t, frameN, _timeToFirstFrame = reset_timers(win)
language_preferenceClock.reset(-_timeToFirstFrame)

# RUN 'LANGUAGE PREFERENCE'
while continueRoutine:
    t, tThisFlip, tThisFlipGlobal = get_current_time(language_preferenceClock, win)
    frameN = frameN + 1
    text_101, win = text_or_image_update(text_101, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
    # add a keys update function keys_update() with keys_list = ['e','g'] or keys_list = ["space"] or something -> so that we can use functions from the language preference keys
    waitOnFlip = False
    if lang_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        lang_keys, win, waitOnFlip = keys_update_1(lang_keys, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
    if lang_keys.status == STARTED and not waitOnFlip:
        theseKeys, _lang_keys_allKeys, lang_keys, continueRoutine = keys_update_2(lang_keys, _lang_keys_allKeys, ['e','g'])    
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
    if not continueRoutine: break
    continueRoutine = False
    language_preferenceComponents, continueRoutine = check_if_components_finished(language_preferenceComponents, continueRoutine)
    if continueRoutine: win.flip()

# END 'LANGUAGE PREFERENCE'
language_preferenceComponents = hide_components(language_preferenceComponents)
thisExp.addData('text_101.started', text_101.tStartRefresh)
thisExp.addData('text_101.stopped', text_101.tStopRefresh)
# add check_and_save_responses() function
if lang_keys.keys in ['', [], None]:
    lang_keys.keys = None
thisExp.addData('lang_keys.keys',lang_keys.keys)
if lang_keys.keys != None:
    thisExp.addData('lang_keys.rt', lang_keys.rt)
thisExp.addData('lang_keys.started', lang_keys.tStartRefresh)
thisExp.addData('lang_keys.stopped', lang_keys.tStopRefresh)
thisExp.nextEntry()
routineTimer.reset()

# SETUP 'PRAC_MAIN' HANDLER
prac_main_task = data.TrialHandler(nReps=1.0, method='sequential', extraInfo=expInfo, originPath=-1, trialList=data.importConditions('resources/task_files.xlsx', selection='0,1'), seed=None, name='prac_main_task')
thisExp.addLoop(prac_main_task)
thisPrac_main_task = prac_main_task.trialList[0]
if thisPrac_main_task != None:
    for paramName in thisPrac_main_task:
        exec('{} = thisPrac_main_task[paramName]'.format(paramName))

# 'PRAC_BLOCK' LOOP (MAIN CODE)
for thisPrac_main_task in prac_main_task:
    currentLoop = prac_main_task
    if thisPrac_main_task != None:
        for paramName in thisPrac_main_task:
            exec('{} = thisPrac_main_task[paramName]'.format(paramName))
    
    # SETUP BLOCK HANDLER
    block = data.TrialHandler(nReps=1.0, method='sequential', extraInfo=expInfo, originPath=-1, trialList=data.importConditions(task_file, selection=block_lists), seed=None, name='block')
    thisExp.addLoop(block)
    thisBlock = block.trialList[0]
    
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # BLOCKS LOOP
    for thisBlock in block:
        currentLoop = block
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock:
                exec('{} = thisBlock[paramName]'.format(paramName))
        
        # PREPARE 'PRAC_BLOCK'
        continueRoutine = True
        routineForceEnded = False
        if lang_keys.keys == 'e':
            block_intro = 'New block of the main task is coming up. \n Press SPACEBAR to proceed.'
        else:
            block_intro = 'Ein neuer Block der Hauptaufgabe wird angezeigt. Drücke die LEERTASTE, um fortzufahren.'
        proceed_17.keys = []
        proceed_17.rt = []
        _proceed_17_allKeys = []
        text_20.setText(block_intro)
        prac_blockComponents = [space_image_7, proceed_17, text_20]
        prac_blockComponents = keep_track(prac_blockComponents)
        t, _timeToFirstFrame, frameN = reset_timers(win)
        
        
        # RUN 'PRAC_BLOCK'
        while continueRoutine:
            t, tThisFlip, tThisFlipGlobal = get_current_time(routineTimer, win)
            frameN = frameN + 1
            space_image_7, win = text_or_image_update(space_image_7, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
            thisExp.timestampOnFlip(win, 'space_image_7.started')
            waitOnFlip = False
            if proceed_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                proceed_17, win, waitOnFlip = keys_update_1(proceed_17, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'proceed_17.started')
            if proceed_17.status == STARTED and not waitOnFlip:
                theseKeys, _proceed_17_allKeys, proceed_17, continueRoutine = keys_update_2(proceed_17, _proceed_17_allKeys, ['space'])
            text_20, win = text_or_image_update(text_20, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
            thisExp.timestampOnFlip(win, 'text_20.started')
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not continueRoutine: routineForceEnded = True; break
            continueRoutine = False
            prac_blockComponents, continueRoutine = check_if_components_finished(prac_blockComponents, continueRoutine)
            if continueRoutine: win.flip()
        
        # END 'PRAC_BLOCK'
        prac_blockComponents = hide_components(prac_blockComponents)
        if proceed_17.keys in ['', [], None]:
            proceed_17.keys = None
        block.addData('proceed_17.keys',proceed_17.keys)
        if proceed_17.keys != None:
            block.addData('proceed_17.rt', proceed_17.rt)
        routineTimer.reset()
        
        # SETUP PRIMER HANDLER
        primer = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(condition_file, selection='1'),
            seed=None, name='primer')
        thisExp.addLoop(primer)
        thisPrimer = primer.trialList[0]
        if thisPrimer != None:
            for paramName in thisPrimer:
                exec('{} = thisPrimer[paramName]'.format(paramName))
        for thisPrimer in primer:
            currentLoop = primer
            if thisPrimer != None:
                for paramName in thisPrimer:
                    exec('{} = thisPrimer[paramName]'.format(paramName))
            
            # PREPARE 'PRIMER_MU'
            continueRoutine = True
            routineForceEnded = False
            if left == 0:                                                       # Did you add this, Prashanti?
                pos = 0.07
                if lang_keys.keys == 'e':
                    ques_word = 'Please note that in this block of trials, you will be asked to indicate the probability of finding space crystals on the RIGHT planet. Press SPACEBAR to proceed.'
                else:
                    ques_word = 'Bitte beachte, dass du in diesem Block die Wahrscheinlichkeit angeben sollst, dass die Weltraumkristalle auf dem RECHTEN Planeten gefunden werden. Drücke die LEERTASTE, um fortzufahren.'
                arrow = 'resources/curved_arrow_right.png'
                arrow_ori = 40;
                left_op = 1;
                right_op = 1;
            else:
                pos = -0.07;
                if lang_keys.keys == 'e':
                    ques_word = 'Please note that in this block of trials, you will be asked to indicate the probability of finding space crystals on the LEFT planet. Press SPACEBAR to proceed.'
                else:
                    ques_word = 'Bitte beachte, dass du in diesem Block die Wahrscheinlichkeit angeben sollst, dass die Weltraumkristalle auf dem LINKEN Planeten gefunden werden. Drücke die LEERTASTE, um fortzufahren.'
                arrow = 'resources/curved_arrow.png'
                arrow_ori = 320;
                left_op = 1;
                right_op = 1;
            if planet_pos == 0:
                left_planet = 'resources/green_blur.png'
                right_planet = 'resources/blue_blur.png'
            else:
                left_planet = 'resources/blue_blur.png'
                right_planet = 'resources/green_blur.png'
            planet_right_6.setOpacity(right_op)
            planet_right_6.setPos((0.4, 0.4))
            planet_right_6.setImage(right_planet)
            planet_left_6.setOpacity(left_op)
            planet_left_6.setImage(left_planet)
            arrow_left_3.setPos((pos,0.17))
            arrow_left_3.setImage(arrow)
            mu_5.reset()
            text_21.setText(ques_word)
            key_resp_3.keys = []
            key_resp_3.rt = []
            _key_resp_3_allKeys = []
            mu_ghost.markerPos = None
            primer_muComponents = [space_bg_12, shuttle_5, planet_right_6, planet_left_6, arrow_left_3, mu_5, text_21, key_resp_3]
            primer_muComponents = keep_track(primer_muComponents)
            t, frameN, _timeToFirstFrame = reset_timers(win)
            
            # RUN 'PRIMER_MU'
            while continueRoutine:
                t, tThisFlip, tThisFlipGlobal = get_current_time(routineTimer, win)
                frameN = frameN + 1
                space_bg_12, win = text_or_image_update(space_bg_12, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'space_bg_12.started') # -> huge problem, should only be done once, and now gets done many many times -> ANSWER: add text (eg.: 'space_bg_12.started') argument to the function
                shuttle_5, win = text_or_image_update(shuttle_5, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'shuttle_5.started')
                planet_right_6, win = text_or_image_update(planet_right_6, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'planet_right_6.started')
                planet_left_6, win = text_or_image_update(planet_left_6, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'planet_left_6.started')
                arrow_left_3, win = text_or_image_update(arrow_left_3, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'arrow_left_3.started')
                mu_5, win = text_or_image_update(mu_5, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'mu_5.started')
                text_21, win = text_or_image_update(text_21, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'text_21.started')
                waitOnFlip = False
                if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    key_resp_3, win, waitOnFlip = keys_update_1(key_resp_3, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'key_resp_3.started')
                if key_resp_3.status == STARTED and not waitOnFlip:
                    theseKeys, _key_resp_3_allKeys, key_resp_3, continueRoutine = keys_update_2(key_resp_3, _key_resp_3_allKeys, ['space'])
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
                if not continueRoutine: routineForceEnded = True; break
                continueRoutine = False
                primer_muComponents, continueRoutine = check_if_components_finished(primer_muComponents, continueRoutine)
                if continueRoutine: win.flip()
            
            # END 'PRIMER_MU'
            primer_muComponents = hide_components(primer_muComponents)
            primer.addData('mu_5.response', mu_5.getRating())
            primer.addData('mu_5.rt', mu_5.getRT())
            if key_resp_3.keys in ['', [], None]:
                key_resp_3.keys = None
            primer.addData('key_resp_3.keys',key_resp_3.keys)
            if key_resp_3.keys != None:
                primer.addData('key_resp_3.rt', key_resp_3.rt)
            routineTimer.reset()
        # completed 1.0 repeats of 'primer'
        
        
        # SETUP 'TRIALS' HANDLER
        trials = data.TrialHandler(nReps=1.0, method='random', extraInfo=expInfo, originPath=-1, trialList=data.importConditions(condition_file, selection=trial_lists), seed=None, name='trials')
        thisExp.addLoop(trials) 
        thisTrial = trials.trialList[0]
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        for thisTrial in trials:
            currentLoop = trials
            if thisTrial != None:
                for paramName in thisTrial:
                    exec('{} = thisTrial[paramName]'.format(paramName))
            
            # PREPARE 'SIGNAL'
            continueRoutine = True
            routineForceEnded = False
            left_patch_7.setContrast(con_left)
            right_patch_7.setContrast(con_right)
            signalComponents = [space_image_8, radar_3, left_patch_7, fix_circle_7, right_patch_7]
            signalComponents = keep_track(signalComponents)
            t, frameN, _timeToFirstFrame = reset_timers(win)
           
            
            # RUN 'SIGNAL'
            while continueRoutine and routineTimer.getTime() < 1.0:
                t, tThisFlip, tThisFlipGlobal = get_current_time(routineTimer, win)
                frameN = frameN + 1 
                if space_image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    space_image_8, win = text_or_image_update(space_image_8, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'space_image_8.started')
                if space_image_8.status == STARTED:                 # check out how to delete this or make it a function ***
                    if tThisFlipGlobal > space_image_8.tStartRefresh + 1-frameTolerance:
                        space_image_8.tStop = t
                        space_image_8.frameNStop = frameN
                        thisExp.timestampOnFlip(win, 'space_image_8.stopped')
                        space_image_8.setAutoDraw(False)
                if radar_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    radar_3, win = text_or_image_update(radar_3, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'radar_3.started')
                if radar_3.status == STARTED: # ***
                    if tThisFlipGlobal > radar_3.tStartRefresh + 1-frameTolerance:
                        radar_3.tStop = t
                        radar_3.frameNStop = frameN
                        thisExp.timestampOnFlip(win, 'radar_3.stopped')
                        radar_3.setAutoDraw(False)
                if left_patch_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    left_patch_7, win = text_or_image_update(left_patch_7, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'left_patch_7.started')
                if left_patch_7.status == STARTED: # ***
                    if tThisFlipGlobal > left_patch_7.tStartRefresh + 1-frameTolerance:
                        left_patch_7.tStop = t
                        left_patch_7.frameNStop = frameN
                        thisExp.timestampOnFlip(win, 'left_patch_7.stopped')
                        left_patch_7.setAutoDraw(False)
                if fix_circle_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    fix_circle_7, win = text_or_image_update(fix_circle_7, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'fix_circle_7.started')
                if fix_circle_7.status == STARTED:
                    if tThisFlipGlobal > fix_circle_7.tStartRefresh + 1-frameTolerance:
                        fix_circle_7.tStop = t
                        fix_circle_7.frameNStop = frameN
                        thisExp.timestampOnFlip(win, 'fix_circle_7.stopped')
                        fix_circle_7.setAutoDraw(False)
                if right_patch_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    right_patch_7, win = text_or_image_update(right_patch_7, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'right_patch_7.started')
                if right_patch_7.status == STARTED:
                    if tThisFlipGlobal > right_patch_7.tStartRefresh + 1-frameTolerance:
                        right_patch_7.tStop = t
                        right_patch_7.frameNStop = frameN
                        thisExp.timestampOnFlip(win, 'right_patch_7.stopped')
                        right_patch_7.setAutoDraw(False)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
                if not continueRoutine: routineForceEnded = True; break
                continueRoutine = False
                signalComponents, continueRoutine = check_if_components_finished(signalComponents, continueRoutine)
                if continueRoutine: win.flip()
            
            # END 'SIGNAL'
            signalComponents = hide_components(signalComponents)
            if routineForceEnded: routineTimer.reset()
            else: routineTimer.addTime(-1.000000)
            
            # PREPARE 'SLIDER_3'
            continueRoutine = True
            routineForceEnded = False
            if left == 0:
                pos = 0.075
                if lang_keys.keys == 'e':
                    ques_word = 'Please indicate the probability of finding space crystals on the RIGHT planet.'
                else:
                    ques_word = 'Bitte gib die Wahrscheinlichkeit an, auf dem RECHTEN Planeten Weltraumkristalle zu finden.'
                arrow = 'resources/curved_arrow_right.png'
            else:
                pos = -0.075;
                if lang_keys.keys == 'e':
                    ques_word = 'Please indicate the probability of finding space crystals on the LEFT planet.'
                else:
                    ques_word = 'Bitte gib die Wahrscheinlichkeit an, auf dem LINKEN Planeten Weltraumkristalle zu finden.'
                arrow = 'resources/curved_arrow.png'
            if planet_pos == 0:
                left_planet = 'resources/green_blur.png'
                right_planet = 'resources/blue_blur.png'
            else:
                left_planet = 'resources/blue_blur.png'
                right_planet = 'resources/green_blur.png'
            text_22.setText(ques_word)
            reported_mu.reset()
            planet_right_7.setPos((0.4, 0.4))
            planet_right_7.setImage(right_planet)
            planet_left_7.setImage(left_planet)
            arrow_left_4.setPos((pos,0.17))
            arrow_left_4.setOri(0.0)
            arrow_left_4.setImage(arrow)
            mu_ghost.marker.opacity = 0.7
            mu_ghost.depth = -1.0
            slider_3Components = [space_bg_13, text_22, mu_ghost, reported_mu, shuttle_3, planet_right_7, planet_left_7, arrow_left_4]
            slider_3Components = keep_track(slider_3Components)
            t, frameN, _timeToFirstFrame = reset_timers(win)
            
            # RUN 'SLIDER_3'
            while continueRoutine and routineTimer.getTime() < 7.5:
                t, tThisFlip, tThisFlipGlobal = get_current_time(routineTimer, win)
                frameN = frameN + 1
                if space_bg_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    space_bg_13, win = text_or_image_update(space_bg_13, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'space_bg_13.started')
                if space_bg_13.status == STARTED: # ***
                    if tThisFlipGlobal > space_bg_13.tStartRefresh + 7.5-frameTolerance:
                        space_bg_13.tStop = t
                        space_bg_13.frameNStop = frameN
                        thisExp.timestampOnFlip(win, 'space_bg_13.stopped')
                        space_bg_13.setAutoDraw(False)
                if text_22.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    text_22, win = text_or_image_update(text_22, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'text_22.started')
                if text_22.status == STARTED: # ***
                    if tThisFlip > 7.5-frameTolerance:
                        text_22.tStop = t
                        text_22.frameNStop = frameN
                        thisExp.timestampOnFlip(win, 'text_22.stopped')
                        text_22.setAutoDraw(False)
                if reported_mu.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    reported_mu, win = text_or_image_update(reported_mu, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'reported_mu.started')
                    mu_ghost.setAutoDraw(True)                                  # I need to take care of this maybe
                if reported_mu.status == STARTED: # ***
                    if tThisFlipGlobal > reported_mu.tStartRefresh + 6-frameTolerance:
                        reported_mu.tStop = t
                        reported_mu.frameNStop = frameN
                        thisExp.timestampOnFlip(win, 'reported_mu.stopped')
                        mu_ghost.setAutoDraw(False)                             # this too
                        reported_mu.setAutoDraw(False)
                if reported_mu.getRating() is not None and reported_mu.status == STARTED: continueRoutine = False
                if shuttle_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    shuttle_3, win = text_or_image_update(shuttle_3, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'shuttle_3.started')
                if shuttle_3.status == STARTED: # ***
                    if tThisFlipGlobal > shuttle_3.tStartRefresh + 7.5-frameTolerance:
                        shuttle_3.tStop = t
                        shuttle_3.frameNStop = frameN
                        thisExp.timestampOnFlip(win, 'shuttle_3.stopped')
                        shuttle_3.setAutoDraw(False)                
                if planet_right_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    planet_right_7, win = text_or_image_update(planet_right_7, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'planet_right_7.started')
                if planet_right_7.status == STARTED:
                    if tThisFlipGlobal > planet_right_7.tStartRefresh + 7.5-frameTolerance:
                        planet_right_7.tStop = t
                        planet_right_7.frameNStop = frameN
                        thisExp.timestampOnFlip(win, 'planet_right_7.stopped')
                        planet_right_7.setAutoDraw(False)
                if planet_left_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    planet_left_7, win = text_or_image_update(planet_left_7, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'planet_left_7.started')
                if planet_left_7.status == STARTED:
                    if tThisFlipGlobal > planet_left_7.tStartRefresh + 7.5-frameTolerance:
                        planet_left_7.tStop = t
                        planet_left_7.frameNStop = frameN 
                        thisExp.timestampOnFlip(win, 'planet_left_7.stopped')
                        planet_left_7.setAutoDraw(False)
                if arrow_left_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    arrow_left_4, win = text_or_image_update(arrow_left_4, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'arrow_left_4.started')
                if arrow_left_4.status == STARTED:
                    if tThisFlipGlobal > arrow_left_4.tStartRefresh + 7.5-frameTolerance:
                        arrow_left_4.tStop = t
                        arrow_left_4.frameNStop = frameN
                        thisExp.timestampOnFlip(win, 'arrow_left_4.stopped')
                        arrow_left_4.setAutoDraw(False)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
                if not continueRoutine: routineForceEnded = True; break
                continueRoutine = False
                slider_3Components, continueRoutine = check_if_components_finished(slider_3Components, continueRoutine)
                if continueRoutine: win.flip()
            
            # END 'SLIDER_3
            slider_3Components = hide_components(slider_3Components)
            if reported_mu.getRating() is not None: mu = reported_mu.getRating();
            trials.addData('reported_mu.response', reported_mu.getRating())
            trials.addData('reported_mu.rt', reported_mu.getRT())
            if reported_mu.getRating() is not None: mu_ghost.markerPos = mu
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-7.500000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials'
        
        
        # PREPARE 'PRECHOICE_TEXT'
        continueRoutine = True
        routineForceEnded = False
        if lang_keys.keys == 'e':
            instr='Before you provide advise to the spaceship, you will be shown your reported probability on the latest trial.\n\nPlease use the analysis of the radar signals that you conducted throughout the block, to inform the spaceship.\n\nPress SPACEBAR to proceed.'
        else:
            instr='Bevor du den Astronaut:innen deinen Ratschlag erteilst, wird dir deine gemeldete Wahrscheinlichkeit für den letzten Versuch angezeigt.\n\nBitte verwende die Analyse der Radarsignale, die du während des gesamten Blocks durchgeführt hast, um das Raumschiff zu informieren.\n\nDrücke die LEERTASTE, um fortzufahren.'
        text_23.setText(instr)
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        prechoice_textComponents = [space_bg_14, text_23, key_resp_4]
        prechoice_textComponents = keep_track(prechoice_textComponents)
        t, frameN, _timeToFirstFrame = reset_timers(win)
        
        # RUN 'PRECHOICE_TEXT'
        while continueRoutine:
            t, tThisFlip, tThisFlipGlobal = get_current_time(routineTimer, win)
            frameN = frameN + 1                        
            if space_bg_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                space_bg_14, win = text_or_image_update(space_bg_14, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'space_bg_14.started')
            if text_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                text_23, win = text_or_image_update(text_23, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'text_23.started')
            waitOnFlip = False
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                key_resp_4, win, waitOnFlip = keys_update_1(key_resp_4, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'key_resp_4.started')
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys, _key_resp_4_allKeys, key_resp_4, continueRoutine = keys_update_2(key_resp_4, _key_resp_4_allKeys, ['space'])
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not continueRoutine: routineForceEnded = True; break
            continueRoutine = False
            prechoice_textComponents, continueRoutine = check_if_components_finished(prechoice_textComponents, continueRoutine)
            if continueRoutine: win.flip()
        
        # END 'PRECHOICE_TEXT'
        prechoice_textComponents = hide_components(prechoice_textComponents)
        if key_resp_4.keys in ['', [], None]: key_resp_4.keys = None
        block.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None: block.addData('key_resp_4.rt', key_resp_4.rt)
        routineTimer.reset()
        
        # SETUP 'LAST' HANDLER
        last = data.TrialHandler(nReps=1.0, method='random', extraInfo=expInfo, originPath=-1, trialList=data.importConditions(condition_file, selection='1'), seed=None, name='last')
        thisExp.addLoop(last)
        thisLast = last.trialList[0]
        if thisLast != None:
            for paramName in thisLast:
                exec('{} = thisLast[paramName]'.format(paramName))
        
        for thisLast in last:
            currentLoop = last
            if thisLast != None:
                for paramName in thisLast:
                    exec('{} = thisLast[paramName]'.format(paramName))
            
            # PREPARE 'LAST_MU'
            continueRoutine = True
            routineForceEnded = False
            mu_7.markerPos = mu;
            if left == 0:
                pos = 0.07
                if lang_keys.keys == 'e':
                    ques_word = 'On the last trial, you reported that the probability of finding space crystals on the RIGHT planet is '
                else:
                    ques_word='Beim letzten Versuch hast du angegeben, dass die Wahrscheinlichkeit, auf dem RECHTEN Planeten Weltraumkristalle zu finden, wie folgt ist '
                arrow = 'resources/curved_arrow_right.png'
                arrow_ori = 40;
                left_op = 1;
                right_op = 1;
            else:
                pos = -0.07;
                if lang_keys.keys == 'e':
                    ques_word = 'On the last trial, you reported that the probability of finding space crystals on the LEFT planet is '
                else:
                    ques_word='Beim letzten Versuch hast du angegeben, dass die Wahrscheinlichkeit, Weltraumkristalle auf dem LINKEN Planeten zu finden, wie folgt ist '
                arrow = 'resources/curved_arrow.png'
                arrow_ori = 320;
                left_op = 1;
                right_op = 1;
            if planet_pos == 0:
                left_planet = 'resources/green_blur.png'
                right_planet = 'resources/blue_blur.png'
            else:
                left_planet = 'resources/blue_blur.png'
                right_planet = 'resources/green_blur.png'
            planet_right_8.setOpacity(right_op)
            planet_right_8.setPos((0.4, 0.4))
            planet_right_8.setImage(right_planet)
            planet_left_8.setOpacity(left_op)
            planet_left_8.setImage(left_planet)
            arrow_left_5.setPos((pos, 0.17))
            arrow_left_5.setOri(0.0)
            arrow_left_5.setImage(arrow)
            mu_7.reset()
            text_24.setText(ques_word)
            key_resp_5.keys = []
            key_resp_5.rt = []
            _key_resp_5_allKeys = []
            last_muComponents = [space_bg_15, shuttle_6, planet_right_8, planet_left_8, arrow_left_5, mu_7, text_24, key_resp_5, text_31]
            last_muComponents = keep_track(last_muComponents)
            t, frameN, _timeToFirstFrame = reset_timers(win)
            
            # RUN 'LAST_MU'
            while continueRoutine:
                t, tThisFlip, tThisFlipGlobal = get_current_time(routineTimer, win)
                frameN = frameN + 1
                if space_bg_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    space_bg_15, win = text_or_image_update(space_bg_15, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'space_bg_15.started')
                mu_7.markerPos = mu;
                if shuttle_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    shuttle_6, win = text_or_image_update(shuttle_6, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'shuttle_6.started')
                if planet_right_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    planet_right_8, win = text_or_image_update(planet_right_8, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'planet_right_8.started')
                if planet_left_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    planet_left_8, win = text_or_image_update(planet_left_8, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'planet_left_8.started')
                if arrow_left_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    arrow_left_5, win = text_or_image_update(arrow_left_5, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'arrow_left_5.started')
                if mu_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    mu_7, win = text_or_image_update(mu_7, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                if text_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    text_24, win = text_or_image_update(text_24, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'text_24.started')
                waitOnFlip = False
                if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    key_resp_5, win, waitOnFlip = keys_update_1(key_resp_5, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'key_resp_5.started')
                if key_resp_5.status == STARTED and not waitOnFlip:
                    theseKeys, _key_resp_5_allKeys, key_resp_5, continueRoutine = keys_update_2(key_resp_5, _key_resp_5_allKeys, ['space'])
                if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    text_31, win = text_or_image_update(text_31, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                    thisExp.timestampOnFlip(win, 'text_31.started')
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
                if not continueRoutine: routineForceEnded = True; break
                continueRoutine = False
                last_muComponents, continueRoutine = check_if_components_finished(last_muComponents, continueRoutine)
                if continueRoutine: win.flip()
            
            # END 'LAST_MU'
            last_muComponents = hide_components(last_muComponents)
            last.addData('mu_7.response', mu_7.getRating())
            last.addData('mu_7.rt', mu_7.getRT())
            if reported_mu.getRating() is not None: mu_ghost.markerPos = mu
            if key_resp_5.keys in ['', [], None]: key_resp_5.keys = None
            last.addData('key_resp_5.keys',key_resp_5.keys)
            if key_resp_5.keys != None: last.addData('key_resp_5.rt', key_resp_5.rt)
            routineTimer.reset()
        # completed 1.0 repeats of 'last'
        
        
        # PREPARE 'BLOCK_CHOICE'
        continueRoutine = True
        routineForceEnded = False
        if lang_keys.keys == 'e':
            instr='Please make a choice about which planet you want the spaceship to go to.\n\nTo make a choice, you need to click on the planet which you want to send the spaceship to. '
        else:
            instr='Bitte entscheide dich für einen Planeten, zu dem das Raumschiff fliegen soll.\n\nUm eine Wahl zu treffen, musst du auf den Planeten klicken, zu dem du das Raumschiff schicken willst.'
        text_25.setText(instr)
        planet_right_9.setPos((0.4, 0.4))
        planet_right_9.setImage(right_planet)
        planet_left_9.setImage(left_planet)
        if planet_pos == 0:
            left_planet = 'resources/green_blur.png'
            right_planet = 'resources/blue_blur.png'
        else:
            left_planet = 'resources/blue_blur.png'
            right_planet = 'resources/green_blur.png'
        mouse_resp.x = []
        mouse_resp.y = []
        mouse_resp.leftButton = []
        mouse_resp.midButton = []
        mouse_resp.rightButton = []
        mouse_resp.time = []
        mouse_resp.clicked_name = []
        gotValidClick = False
        block_choiceComponents = [space_bg_16, shuttle_7, planet_right_9, planet_left_9, text_25, question, mouse_resp]
        block_choiceComponents = keep_track(block_choiceComponents)
        t, frameN, _timeToFirstFrame = reset_timers(win)
        
        # RUN 'BLOCK_CHOICE'
        while continueRoutine:
            t, tThisFlip, tThisFlipGlobal = get_current_time(routineTimer, win)
            frameN = frameN + 1
            if space_bg_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                space_bg_16, win = text_or_image_update(space_bg_16, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'space_bg_16.started')
            if shuttle_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                shuttle_7, win = text_or_image_update(shuttle_7, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'shuttle_7.started')
            if planet_right_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                planet_right_9, win = text_or_image_update(planet_right_9, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'planet_right_9.started')
            if planet_left_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                planet_left_9, win = text_or_image_update(planet_left_9, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'planet_left_9.started')
            if text_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                text_25, win = text_or_image_update(text_25, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'text_25.started')
            if question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                question, win = text_or_image_update(question, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'question.started')
            if mouse_resp.status == NOT_STARTED and t >= 0.0-frameTolerance: # I SHOULD ADD A NEW FUNCTION FOR THIS
                # keep track of start time/frame for later
                mouse_resp.frameNStart = frameN  # exact frame index
                mouse_resp.tStart = t  # local t and not account for scr refresh
                mouse_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_resp.started', t)
                mouse_resp.status = STARTED
                mouse_resp.mouseClock.reset()
                prevButtonState = mouse_resp.getPressed()  # if button is down already this ISN'T a new click
            if mouse_resp.status == STARTED:  # only update if started and not finished!
                buttons = mouse_resp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([planet_right_9,planet_left_9])
                            clickableList = [planet_right_9,planet_left_9]
                        except:
                            clickableList = [[planet_right_9,planet_left_9]]
                        for obj in clickableList:
                            if obj.contains(mouse_resp):
                                gotValidClick = True
                                mouse_resp.clicked_name.append(obj.name)
                        if gotValidClick:
                            x, y = mouse_resp.getPos()
                            mouse_resp.x.append(x)
                            mouse_resp.y.append(y)
                            buttons = mouse_resp.getPressed()
                            mouse_resp.leftButton.append(buttons[0])
                            mouse_resp.midButton.append(buttons[1])
                            mouse_resp.rightButton.append(buttons[2])
                            mouse_resp.time.append(mouse_resp.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # abort routine on response
            
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not continueRoutine: routineForceEnded = True; break
            continueRoutine = False
            block_choiceComponents, continueRoutine = check_if_components_finished(block_choiceComponents, continueRoutine)
            if continueRoutine: win.flip()
        
        # END 'BLOCK_CHOICE'
        block_choiceComponents = hide_components(block_choiceComponents)
        if mouse_resp.clicked_name[0] == 'planet_left_9':
            text_pos = 0.2;
            pos_planet = -0.4;
            ship_pos = -0.19;
            ship_ori = 305;
            crystal_pos = 0.5;
            if planet_pos == 0:
                image = 'resources/green_blur.png'
            else:
                image = 'resources/blue_blur.png'
        else:
            text_pos = -0.4;
            pos_planet = 0.4;
            ship_pos = -0.19;
            ship_ori = 45;
            crystal_pos = -0.1;
            if planet_pos == 0:
                image = 'resources/blue_blur.png'
            else:
                image = 'resources/green_blur.png'
                
        if mouse_resp.clicked_name[0] == corr:
            if condition == 1:
                prob = 0.7 
                block_rew = cond1_rew[block_num]#generate_zero_or_one(prob)
            else:
                prob = 0.9
                block_rew = cond2_rew[block_num] #generate_zero_or_one(prob)
        else:
            if condition == 1:
                prob = 0.3
                block_rew = 1-cond1_rew[block_num] #generate_zero_or_one(prob)
            else:
                prob = 0.1
                block_rew = 1-cond2_rew[block_num] #generate_zero_or_one(prob)
        
        if block_rew == 1:
            if lang_keys.keys == 'e':
                str4 = "Space crystal found!\n"
            else:
                str4='Weltraumkristall gefunden!\n'
            op = 0.7;
        else:
            if lang_keys.keys == 'e':
                str4 = "No crystals found!\n"
            else:
                str4='Keine Weltraumkristalle gefunden.\n'
            op = 0;
        
        if lang_keys.keys == 'e':
            str1 = "You win"
            str2 = str(block_rew)
            str3 = " "+"points!" 
        else:
            str1 = "Du gewinnst "
            str2 = str(block_rew)
            if block_rew == 1:
                str3 = " "+"Punkt!" 
            else:
                str3 = " "+"Punkte!" 
        
        block_num = block_num + 1;
        
        rew = str4 + " " +str1 + " " + str2 + " " + str3
        task_rew = task_rew + block_rew;
        thisExp.addData('block_points', block_rew)
        block.addData('mouse_resp.x', mouse_resp.x)
        block.addData('mouse_resp.y', mouse_resp.y)
        block.addData('mouse_resp.leftButton', mouse_resp.leftButton)
        block.addData('mouse_resp.midButton', mouse_resp.midButton)
        block.addData('mouse_resp.rightButton', mouse_resp.rightButton)
        block.addData('mouse_resp.time', mouse_resp.time)
        block.addData('mouse_resp.clicked_name', mouse_resp.clicked_name)
        routineTimer.reset()
        
        # PREPARE 'BLOCK_REW'
        continueRoutine = True
        routineForceEnded = False
        proceed_18.keys = []
        proceed_18.rt = []
        _proceed_18_allKeys = []
        text_26.setPos((text_pos + 0.2, 0))
        text_26.setText(rew)
        planet.setPos((pos_planet + 0.05, 0))
        planet.setImage(image)
        shuttle_8.setPos((0, ship_pos))
        shuttle_8.setOri(ship_ori)
        ori = 0;
        crystal.setOpacity(op)
        crystal.setPos((crystal_pos, 0 + 0.1))
        block_rewComponents = [space_bg_17, proceed_18, text_26, planet, shuttle_8, crystal]
        block_rewComponents = keep_track(block_rewComponents)
        t, frameN, _timeToFirstFrame = reset_timers(win)
        
        # RUN 'BLOCK_REW'
        while continueRoutine:
            t, tThisFlip, tThisFlipGlobal = get_current_time(routineTimer, win)
            frameN = frameN + 1
            if space_bg_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                space_bg_17, win = text_or_image_update(space_bg_17, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'space_bg_17.started')
            waitOnFlip = False
            if proceed_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                proceed_18, win, waitOnFlip = keys_update_1(proceed_18, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'proceed_18.started')
            if proceed_18.status == STARTED and not waitOnFlip:
                theseKeys, _proceed_18_allKeys, proceed_18, continueRoutine = keys_update_2(proceed_18, _proceed_18_allKeys, ['space'])
            if text_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                text_26, win = text_or_image_update(text_26, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'text_26.started')
            if planet.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                planet, win = text_or_image_update(planet, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'planet.started')
            if shuttle_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                shuttle_8, win = text_or_image_update(shuttle_8, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'shuttle_8.started')
            if crystal.status == STARTED:
                crystal.setOri(1,'+')
                crystal.draw()
            if crystal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                crystal, win = text_or_image_update(crystal, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'crystal.started')
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not continueRoutine: routineForceEnded = True; break
            continueRoutine = False
            block_rewComponents, continueRoutine = check_if_components_finished(block_rewComponents, continueRoutine)
            if continueRoutine: win.flip()
        
        # END 'BLOCK_REW'
        block_rewComponents = hide_components(block_rewComponents)
        if proceed_18.keys in ['', [], None]: proceed_18.keys = None
        block.addData('proceed_18.keys',proceed_18.keys)
        if proceed_18.keys != None: block.addData('proceed_18.rt', proceed_18.rt)
        if lang_keys.keys == 'e':
            str1 = "You completed"
            str2 = " " + str(block_num)
            str3 = " " + "out of"
            str4 = " " + str(total_blocks)
            str5 = " " + "blocks."
            str6 = "\n Press SPACEBAR to proceed."
        else:
            str1 = "Du hast"
            str2 = " " + str(block_num)
            str3 = " " + "von"
            str4 = " " + str(total_blocks)
            str5 = " " + "Blöcken abgeschlossen."
            str6 = "\n Drücke die LEERTASTE, um fortzufahren."
        block_str = str1 + str2 + str3 + str4 + str5 + str6
        routineTimer.reset()
        
        # PREPARE 'BLOCK_COMPLETED'
        continueRoutine = True
        routineForceEnded = False
        proceed_19.keys = []
        proceed_19.rt = []
        _proceed_19_allKeys = []
        text_27.setPos((0, 0))
        text_27.setText(block_str)
        block_completedComponents = [space_bg_18, proceed_19, text_27]
        block_completedComponents = keep_track(block_completedComponents)
        t, frameN, _timeToFirstFrame = reset_timers(win)
        
        # RUN 'BLOCK_COMPLETED'
        while continueRoutine:
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1 
            if space_bg_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                space_bg_18, win = text_or_image_update(space_bg_18, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'space_bg_18.started')
            waitOnFlip = False
            if proceed_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                proceed_19, win, waitOnFlip = keys_update_1(proceed_19, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'proceed_19.started')
            if proceed_19.status == STARTED and not waitOnFlip:
                theseKeys, _proceed_19_allKeys, proceed_19, continueRoutine = keys_update_2(proceed_19, _proceed_19_allKeys, ['space'])
            if text_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                text_27, win = text_or_image_update(text_27, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
                thisExp.timestampOnFlip(win, 'text_27.started')
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not continueRoutine: routineForceEnded = True; break
            continueRoutine = False
            block_completedComponents, continueRoutine = check_if_components_finished(block_completedComponents, continueRoutine)
            if continueRoutine: win.flip()
        
        # END 'BLOCK_COMPLETED'
        block_completedComponents = hide_components(block_completedComponents)
        if proceed_19.keys in ['', [], None]: proceed_19.keys = None
        block.addData('proceed_19.keys',proceed_19.keys)
        if proceed_19.keys != None: block.addData('proceed_19.rt', proceed_19.rt)
        routineTimer.reset()
        thisExp.nextEntry()
    # completed 1.0 repeats of 'block'
    
    
    # PREPARE 'TASK_SCORE'
    continueRoutine = True
    routineForceEnded = False
    if lang_keys.keys == 'e': task_str = "You win " + str(task_rew) + " "+ "points in these set of blocks!"
    else: task_str = "Du gewinnst " + str(task_rew) + " "+ "Punkte in diesem Satz von Blöcken!"
    text_28.setText(task_str)
    proceed_20.keys = []
    proceed_20.rt = []
    _proceed_20_allKeys = []
    task_scoreComponents = [space_bg_19, text_28, proceed_20]
    task_scoreComponents = keep_track(task_scoreComponents)
    t, frameN, _timeToFirstFrame = reset_timers(win)
    
    # RUN 'TASK_SCORE'
    while continueRoutine:
        t, tThisFlip, tThisFlipGlobal = get_current_time(language_preferenceClock, win)
        frameN = frameN + 1
        if space_bg_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            space_bg_19, win = text_or_image_update(space_bg_19, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
            thisExp.timestampOnFlip(win, 'space_bg_19.started')
        if text_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            text_28, win = text_or_image_update(text_28, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
            thisExp.timestampOnFlip(win, 'text_28.started')
        waitOnFlip = False
        if proceed_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            proceed_20, win, waitOnFlip = keys_update_1(proceed_20, tThisFlip, frameTolerance, frameN, t, tThisFlipGlobal, win)
            thisExp.timestampOnFlip(win, 'proceed_20.started')
        if proceed_20.status == STARTED and not waitOnFlip:
            theseKeys, _proceed_20_allKeys, proceed_20, continueRoutine = keys_update_2(proceed_20, _proceed_20_allKeys, ['space'])
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
        if not continueRoutine: routineForceEnded = True; break
        continueRoutine = False
        task_scoreComponents, continueRoutine = check_if_components_finished(task_scoreComponents, continueRoutine)
        if continueRoutine: win.flip()
    
    # END 'TASK_SCORE'
    task_scoreComponents = hide_components(task_scoreComponents)
    if proceed_20.keys in ['', [], None]: proceed_20.keys = None
    prac_main_task.addData('proceed_20.keys',proceed_20.keys)
    if proceed_20.keys != None: prac_main_task.addData('proceed_20.rt', proceed_20.rt)
    routineTimer.reset()
    
    if block_num == 16:
        win.flip()
        thisExp.saveAsWideText(filename+'.csv', delim='auto')
        thisExp.saveAsPickle(filename)
        logging.flush()
        if eyetracker: eyetracker.setConnectionState(False)
        thisExp.abort()
        win.close()
        core.quit()


# END EXPERIMENT
win.flip()
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()
win.close()
core.quit()











