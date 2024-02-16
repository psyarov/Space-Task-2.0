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


def components_init(main):
    
    # language_preference
    main.language_preferenceClock = core.Clock()
    main.text_101 = visual.TextStim(win=main.win, name='text_101',**common_params['text'])
    main.lang_keys = keyboard.Keyboard()
    # welcome
    main.instru = 'doh'
    main.space_bg_4 = visual.ImageStim(win=main.win, name='space_bg_4', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.text_8 = visual.TextStim(win=main.win, name='text_8',text = '',font='Times New Roman',pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-1.0);
    main.proceed_4 = keyboard.Keyboard()
    # intro_planet
    main.space_image_2 = visual.ImageStim(win=main.win,name='space_image_2',image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
    main.shuttle_4 = visual.ImageStim(win=main.win,name='shuttle_4',image='resources/space-shuttle.png', mask=None, anchor='center',ori=0.0, pos=(0, -0.08), size=(0.2, 0.2),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-1.0)
    main.planet_right_3 = visual.ImageStim(win=main.win,name='planet_right_3',image='resources/green_blur.png', mask=None, anchor='center',ori=0.0, pos=[0,0], size=(0.15, 0.15),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-2.0)
    main.planet_left_3 = visual.ImageStim(win=main.win,name='planet_left_3',image='resources/blue_blur.png', mask=None, anchor='center',ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-3.0)
    main.text_11 = visual.TextStim(win=main.win, name='text_11',text='',font='Times New Roman',pos=(0, -0.33), height=0.027, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-4.0);
    main.proceed_7 = keyboard.Keyboard()
    main.radar_2 = visual.ImageStim(win=main.win,name='radar_2', image='resources/radar_grayl.png', mask=None, anchor='center',ori=0.0, pos=(0,0.18), size=(0.3, 0.3),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-6.0)
    main.text_3 = visual.TextStim(win=main.win, name='text_3',text='Radar',font='Times New Roman',pos=(0.25, 0.18), height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-7.0);
    main.arrow = visual.ImageStim(win=main.win,name='arrow', image='resources/arrow.png', mask=None, anchor='center',ori=0.0, pos=(0.185, 0.175), size=(0.06, 0.03),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-8.0)
    main.left_patch = visual.GratingStim(win=main.win, name='left_patch',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(-0.065, 0.18), size=(0.08, 0.08), sf=8.0, phase=0.0,color=[1,1,1], colorSpace='rgb',opacity=None, contrast=0.9, blendmode='avg',texRes=512.0, interpolate=True, depth=-9.0)
    main.right_patch = visual.GratingStim(win=main.win, name='right_patch',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(0.065, 0.18), size=(0.08, 0.08), sf=8.0, phase=0.0,color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',opacity=None, contrast=0.1, blendmode='avg',texRes=512.0, interpolate=True, depth=-10.0)
    main.fix_circle = visual.ShapeStim(win=main.win, name='fix_circle',size=(0.007, 0.007), vertices='circle',ori=0.0, pos=(0, 0.18), anchor='center',lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',opacity=None, depth=-11.0, interpolate=True)
    # intro_radar
    main.space_bg_5 = visual.ImageStim(win=main.win,name='space_bg_5', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
    main.radar_4 = visual.ImageStim(win=main.win,name='radar_4', image='resources/radar_grayl.png', mask=None, anchor='center',ori=0.0, pos=(0,0.1), size=(0.6, 0.6),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-1.0)
    main.text_9 = visual.TextStim(win=main.win, name='text_9',text='',font='Times New Roman',pos=(0, -0.3), height=0.03, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-2.0);
    main.proceed_5 = keyboard.Keyboard()
    # intro_signal
    main.space_bg_6 = visual.ImageStim(win=main.win,name='space_bg_6', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
    main.radar_5 = visual.ImageStim(win=main.win,name='radar_5', image='resources/radar_grayl.png', mask=None, anchor='center',ori=0.0, pos=(0,0.1), size=(0.6, 0.6),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-1.0)
    main.left_patch_4 = visual.GratingStim(win=main.win, name='left_patch_4',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(-0.12, 0.1), size=(0.12, 0.12), sf=8.0, phase=0.0,color=[1,1,1], colorSpace='rgb',opacity=None, contrast=0.9, blendmode='avg',texRes=512.0, interpolate=True, depth=-2.0)
    main.right_patch_4 = visual.GratingStim(win=main.win, name='right_patch_4',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(0.12, 0.1), size=(0.12, 0.12), sf=8.0, phase=0.0,color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',opacity=None, contrast=0.1, blendmode='avg',texRes=512.0, interpolate=True, depth=-3.0)
    main.text_10 = visual.TextStim(win=main.win, name='text_10',text='',font='Times New Roman',pos=(0, -0.3), height=0.03, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-4.0);
    main.proceed_6 = keyboard.Keyboard()
    main.fix_circle_4 = visual.ShapeStim(win=main.win, name='fix_circle_4',size=(0.007, 0.007), vertices='circle',ori=0.0, pos=(0, 0.1), anchor='center',lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',opacity=None, depth=-6.0, interpolate=True)
    # intro_crystal
    main.space_bg_7 = visual.ImageStim(win=main.win,name='space_bg_7', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
    main.radar_6 = visual.ImageStim(win=main.win,name='radar_6', image='resources/radar_grayl.png', mask=None, anchor='center',ori=0.0, pos=(0,0.1), size=(0.6, 0.6),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-1.0)
    main.left_patch_5 = visual.GratingStim(win=main.win, name='left_patch_5',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(-0.12, 0.1), size=(0.12, 0.12), sf=8.0, phase=0.0,color=[1,1,1], colorSpace='rgb',opacity=None, contrast=0.9, blendmode='avg',texRes=512.0, interpolate=True, depth=-2.0)
    main.right_patch_5 = visual.GratingStim(win=main.win, name='right_patch_5',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(0.12, 0.1), size=(0.12, 0.12), sf=8.0, phase=0.0,color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',opacity=None, contrast=0.1, blendmode='avg',texRes=512.0, interpolate=True, depth=-3.0)
    main.text_12 = visual.TextStim(win=main.win, name='text_12',text='',font='Times New Roman',pos=(0, -0.32), height=0.025, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-4.0);
    main.proceed_8 = keyboard.Keyboard()
    main.fix_circle_5 = visual.ShapeStim(win=main.win, name='fix_circle_5',size=(0.007, 0.007), vertices='circle',ori=0.0, pos=(0, 0.1), anchor='center',lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',opacity=None, depth=-6.0, interpolate=True)
    main.planet_right_4 = visual.ImageStim(win=main.win,name='planet_right_4', image='resources/green_blur.png', mask=None, anchor='center',ori=0.0, pos=[0,0], size=(0.15, 0.15),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-7.0)
    main.planet_left_4 = visual.ImageStim(win=main.win,name='planet_left_4', image='resources/blue_blur.png', mask=None, anchor='center',ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-8.0)
    main.arrow_2 = visual.ImageStim(win=main.win,name='arrow_2', image='resources/arrow.png', mask=None, anchor='center',ori=90.0, pos=(-0.4, 0.23), size=(0.2, 0.05),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-9.0)
    # intro_crystal2
    main.space_bg_8 = visual.ImageStim(win=main.win,name='space_bg_8', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
    main.radar_7 = visual.ImageStim(win=main.win,name='radar_7', image='resources/radar_grayl.png', mask=None, anchor='center',ori=0.0, pos=(0,0.1), size=(0.6, 0.6),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-1.0)
    main.left_patch_6 = visual.GratingStim(win=main.win, name='left_patch_6',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(-0.12, 0.1), size=(0.12, 0.12), sf=8.0, phase=0.0,color=[1,1,1], colorSpace='rgb',opacity=None, contrast=0.1, blendmode='avg',texRes=512.0, interpolate=True, depth=-2.0)
    main.right_patch_6 = visual.GratingStim(win=main.win, name='right_patch_6',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(0.12, 0.1), size=(0.12, 0.12), sf=8.0, phase=0.0,color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',opacity=None, contrast=0.9, blendmode='avg',texRes=512.0, interpolate=True, depth=-3.0)
    main.text_13 = visual.TextStim(win=main.win, name='text_13',text='',font='Times New Roman',pos=(0, -0.33), height=0.025, wrapWidth=1.2, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-4.0);
    main.proceed_9 = keyboard.Keyboard()
    main.fix_circle_6 = visual.ShapeStim(win=main.win, name='fix_circle_6',size=(0.007, 0.007),vertices='circle',ori=0.0,pos=(0, 0.1),anchor='center',lineWidth=1.0,colorSpace='rgb',lineColor='black',fillColor='black',opacity=None,depth=-6.0,interpolate=True) # wrapWidth: 1.0->1.2
    main.arrow_3 = visual.ImageStim(win=main.win,name='arrow_3', image='resources/arrow.png', mask=None, anchor='center',ori=90.0, pos=(0.4, 0.23), size=(0.2, 0.05),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-7.0)
    main.planet_right_5 = visual.ImageStim(win=main.win,name='planet_right_5', image='resources/green_blur.png', mask=None, anchor='center',ori=0.0, pos=[0,0], size=(0.15, 0.15),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-8.0)
    main.planet_left_5 = visual.ImageStim(win=main.win,name='planet_left_5', image='resources/blue_blur.png', mask=None, anchor='center',ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-9.0)
    # training_block
    main.space_bg = visual.ImageStim(win=main.win,name='space_bg', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
    main.proceed_2 = keyboard.Keyboard()
    main.text_5 = visual.TextStim(win=main.win, name='text_5',text='',font='Times New Roman',pos=(0, 0), height=0.03, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-2.0);
    # space
    main.space_image = visual.ImageStim(win=main.win,name='space_image', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
    main.radar = visual.ImageStim(win=main.win,name='radar', image='resources/radar_grayl.png', mask=None, anchor='center',ori=0.0, pos=(0,0), size=(0.6, 0.6),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-1.0)
    main.left_patch_3 = visual.GratingStim(win=main.win, name='left_patch_3',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(-0.12, 0), size=(0.12, 0.12), sf=8.0, phase=0.0,color=[1,1,1], colorSpace='rgb',opacity=None, contrast=1.0, blendmode='avg',texRes=512.0, interpolate=True, depth=-2.0)
    main.fix_circle_3 = visual.ShapeStim(win=main.win, name='fix_circle_3',size=(0.007, 0.007), vertices='circle',ori=0.0, pos=(0, 0), anchor='center',lineWidth=1.0, colorSpace='rgb',  lineColor='black', fillColor='black',opacity=None, depth=-3.0, interpolate=True)
    main.right_patch_3 = visual.GratingStim(win=main.win, name='right_patch_3',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(0.12, 0), size=(0.12, 0.12), sf=8.0, phase=0.0,color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',opacity=None, contrast=1.0, blendmode='avg',texRes=512.0, interpolate=True, depth=-4.0)
    main.choice_training = keyboard.Keyboard()
    # space_main
    main.choice_main = keyboard.Keyboard()
    # feedback
    main.space_image_3 = visual.ImageStim(win=main.win,name='space_image_3', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
    main.msg = 'hello'
    main.fb_msg = visual.TextStim(win=main.win, name='fb_msg',text='',font='Times New Roman',pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-2.0);
    # feedback_main
    main.space_image_3_main = visual.ImageStim(win=main.win,name='space_image_3', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
    main.msg_main = 'hello'
    main.fb_msg_main = visual.TextStim(win=main.win, name='fb_msg',text='',font='Times New Roman',pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-2.0);
    
    # PRACTICE BLOCK ROUTINES
    
    #incong_vid
    #instr = 'doh' # --> initializing instr variable
    main.space_incong_vid = visual.ImageStim(win=main.win,name='space_incong_vid', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
    main.text_incong_vid = visual.TextStim(win=main.win, name='text_incong_vid',text = '',font='Times New Roman',pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-1.0);
    main.proceed_incong = keyboard.Keyboard()
    
    # prob
    main.arrow_less = 'doh'
    main.arrow_more = 'doh'
    main.space_bg_23 = visual.ImageStim(win=main.win,name='space_bg_23', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
    main.text_33 = visual.TextStim(win=main.win, name='text_33',text='',font='Times New Roman',pos=(0, -0.35), height=0.025, wrapWidth=1.3, ori=0.0, color=[0.8824, 0.9451, 1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-1.0); # wrapWidth None to 1.3
    main.text_crit = visual.TextStim(win=main.win, name='text_crit',text='',font='Times New Roman',pos=(0, 0), height=0.025, wrapWidth=1.3, ori=0.0, color=[0.8824, 0.9451, 1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-1.0);  # delete?
    main.proceed_23 = keyboard.Keyboard()
    main.more_text = visual.TextStim(win=main.win, name='more_text',text='',font='Times New Roman',pos=(0.15, 0.22), height=0.025, wrapWidth=1.3, ori=315, color=[0.8824, 0.9451, 1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-1.0);
    main.less_text = visual.TextStim(win=main.win, name='more_text',text='',font='Times New Roman',pos=(-0.15, 0.22), height=0.025, wrapWidth=1.3, ori=45, color=[0.8824, 0.9451, 1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-1.0);
    main.mu_4 = visual.Slider(win=main.win, name='mu_4',startValue=None, size=(0.8, 0.03), pos=(0, -0.1), units=None,labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0,style='rating', styleTweaks=(), opacity=None,labelColor=[0.8824, 0.9451, 1.0000], markerColor=[1.0000, 1.0000, 1.0000], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb',font='Times New Roman', labelHeight=0.03,flip=False, ori=0.0, depth=-3, readOnly=False)
    main.shuttle_9 = visual.ImageStim(win=main.win,name='shuttle_9', image='resources/space-shuttle.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(0.2, 0.2),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-4.0)
    main.planet_left_10 = visual.ImageStim(win=main.win,name='planet_left_10', image='sin', mask=None, anchor='center',ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-5.0)
    main.planet_right_10 = visual.ImageStim(win=main.win,name='planet_right_10', image='sin', mask=None, anchor='center',ori=0.0, pos=[0,0], size=(0.15, 0.15),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-6.0)
    main.arrow_left_6 = visual.ImageStim(win=main.win,name='arrow_left_6', image='sin', mask=None, anchor='center',ori=45, pos=[0.18,0.23], size=(0.03,0.38),color=[1,1,1], colorSpace='rgb', opacity=0.85,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-7.0)
    main.arrow_right_6 = visual.ImageStim(win=main.win,name='arrow_right_6', image='sin', mask=None, anchor='center',ori=315, pos=[-0.18,0.23], size=(0.03,0.39),color=[1,1,1], colorSpace='rgb', opacity=0.3,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-7.0)
    
    # prob1
    main.less_text1 = visual.TextStim(win=main.win, name='less_text1', text='', font='Times New Roman', pos=(0.15, 0.22), height=0.025, wrapWidth=1.3, ori=315, color=[0.8824, 0.9451, 1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-1.0)
    main.more_text1 = visual.TextStim(win=main.win, name='more_text1', text='', font='Times New Roman', pos=(-0.15, 0.22), height=0.025, wrapWidth=1.3, ori=45, color=[0.8824, 0.9451, 1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-1.0)
    main.space_bg_24 = visual.ImageStim(win=main.win, name='space_bg_24', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.text_35 = visual.TextStim(win=main.win, name='text_35', text='', font='Times New Roman', pos=(0, -0.35), height=0.025, wrapWidth=None, ori=0.0, color=[0.8824, 0.9451, 1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-1.0)
    main.proceed_25 = keyboard.Keyboard()
    main.mu_9 = visual.Slider(win=main.win, name='mu_9', startValue=None, size=(0.8, 0.03), pos=(0, -0.1), units=None, labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0, style='rating', styleTweaks=(), opacity=None, labelColor=[0.8824, 0.9451, 1.0000], markerColor=[1.0000, 1.0000, 1.0000], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb', font='Times New Roman', labelHeight=0.03, flip=False, ori=0.0, depth=-3, readOnly=False)
    main.shuttle_10 = visual.ImageStim(win=main.win, name='shuttle_10', image='resources/space-shuttle.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(0.2, 0.2), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-4.0)
    main.planet_left_11 = visual.ImageStim(win=main.win, name='planet_left_11', image='sin', mask=None, anchor='center', ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-5.0)
    main.planet_right_11 = visual.ImageStim(win=main.win, name='planet_right_11', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-6.0)
    main.arrow_left_7 = visual.ImageStim(win=main.win, name='arrow_left_7', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.2,0.25), color=[1,1,1], colorSpace='rgb', opacity=0.5, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-7.0)
    main.arrow_left_7 = visual.ImageStim(win=main.win, name='arrow_left_6', image='sin', mask=None, anchor='center', ori=45, pos=[0.18,0.23], size=(0.03,0.38), color=[1,1,1], colorSpace='rgb', opacity=0.3, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-7.0)
    main.arrow_right_7 = visual.ImageStim(win=main.win, name='arrow_right_6', image='sin', mask=None, anchor='center', ori=315, pos=[-0.18,0.23], size=(0.03,0.39), color=[1,1,1], colorSpace='rgb', opacity=0.7, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-7.0)
    
    # demo -> win -> win=main.win
    main.movie = visual.MovieStim(win=main.win, name='movie', filename='resources/demo_vid.mp4', movieLib='ffpyplayer', loop=True, volume=1.0, pos=(0, 0), size=[1.5,0.75], units=None, ori=0.0, anchor='center',opacity=None, contrast=1.0)
    main.movie_ger = visual.MovieStim(win=main.win, name='movie', filename='resources/demo_vid.mp4', movieLib='ffpyplayer', loop=True, volume=1.0, pos=(0, 0), size=[1.5,0.75], units=None, ori=0.0, anchor='center',opacity=None, contrast=1.0)
    main.text_34 = visual.TextStim(win=main.win, name='text_34', text='', font='Times New Roman', pos=(0, -0.43), height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-1.0)
    main.proceed_24 = keyboard.Keyboard()
    
    # demo_incong
    main.movie_2 = visual.MovieStim(win=main.win, name='movie_2', filename='resources/demo_incong.mp4', movieLib='ffpyplayer', loop=True, volume=1.0, pos=(0, 0), size=[1.5,0.75], units=None, ori=0.0, anchor='center',opacity=None, contrast=1.0)
    main.movie_2_ger = visual.MovieStim(win=main.win, name='movie_2', filename='resources/demo_incong.mp4', movieLib='ffpyplayer', loop=True, volume=1.0, pos=(0, 0), size=[1.5,0.75], units=None, ori=0.0, anchor='center',opacity=None, contrast=1.0)
    main.demo_msg = visual.TextStim(win=main.win, name='demo_msg', text='', font='Times New Roman', pos=(0, -0.43), height=0.03, wrapWidth=3.1, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-1.0)
    main.proceed_26 = keyboard.Keyboard()
    
    # space_slider
    main.space_bg_2 = visual.ImageStim(win=main.win, name='space_bg_2', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.text_4 = visual.TextStim(win=main.win, name='text_4', text='', font='Times New Roman', pos=(0, -0.3), height=0.03, wrapWidth=1.3, ori=0.0, color=[0.8824, 0.9451, 1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0)
    main.mu_3 = visual.Slider(win=main.win, name='mu_3', startValue=None, size=(0.8, 0.03), pos=(0, -0.1), units=None, labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0, style='rating', styleTweaks=(), opacity=None, labelColor=[0.8824, 0.9451, 1.0000], markerColor=[1.0000, 1.0000, 1.0000], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb', font='Times New Roman', labelHeight=0.03, flip=False, ori=0.0, depth=-3, readOnly=False)
    main.shuttle = visual.ImageStim(win=main.win, name='shuttle', image='resources/space-shuttle.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(0.2, 0.2), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-4.0)
    main.planet_right = visual.ImageStim(win=main.win, name='planet_right', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-5.0)
    main.planet_left = visual.ImageStim(win=main.win, name='planet_left', image='sin', mask=None, anchor='center', ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-6.0)
    main.arrow_left = visual.ImageStim(win=main.win, name='arrow_left', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.2,0.25), color=[1,1,1], colorSpace='rgb', opacity=0.5, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-7.0)
    main.proceed = keyboard.Keyboard()
    
    # space_slider2
    main.space_bg_9 = visual.ImageStim(win=main.win, name='space_bg_9', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.text_6 = visual.TextStim(win=main.win, name='text_6', text='', font='Times New Roman', pos=(0, -0.3), height=0.027, wrapWidth=None, ori=0.0, color=[0.8824, 0.9451, 1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-1.0)
    main.shuttle_2 = visual.ImageStim(win=main.win, name='shuttle_2', image='resources/space-shuttle.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(0.2, 0.2), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-2.0)
    main.planet_right_2 = visual.ImageStim(win=main.win, name='planet_right_2', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-3.0)
    main.planet_left_2 = visual.ImageStim(win=main.win, name='planet_left_2', image='sin', mask=None, anchor='center', ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-4.0)
    main.arrow_left_2 = visual.ImageStim(win=main.win, name='arrow_left_2', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.2,0.25), color=[1,1,1], colorSpace='rgb', opacity=0.5, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-5.0)
    main.proceed_10 = keyboard.Keyboard()
    main.mu_8 = visual.Slider(win=main.win, name='mu_8', startValue=None, size=(0.8, 0.03), pos=(0, -0.1), units=None, labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0, style='rating', styleTweaks=(), opacity=None, labelColor=[0.8824, 0.9451, 1.0000], markerColor=[1.0000, 1.0000, 1.0000], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb', font='Times New Roman', labelHeight=0.03, flip=False, ori=0.0, depth=-7, readOnly=False)
    
    # slider_example
    main.slider_1 = visual.ImageStim(win=main.win, name='slider_1', image='resources/slider_ex.png', mask=None, anchor='center', ori=0.0, pos=(0, 0.18), size=(1.05, 0.6), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.slider_ger = visual.ImageStim(win=main.win, name='slider', image='resources/slider_ex_ger.png', mask=None, anchor='center', ori=0.0, pos=(0, 0.18), size=(1.05, 0.6), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.proceed_11 = keyboard.Keyboard()
    main.text_14 = visual.TextStim(win=main.win, name='text_14', text='', font='Times New Roman', pos=(0, -0.3), height=0.027, wrapWidth=1.0, ori=0.0, color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0)
    main.arrow_4 = visual.ImageStim(win=main.win, name='arrow_4', image='resources/arrow.png', mask=None, anchor='center', ori=90.0, pos=(-0.12, -0.12), size=(0.06, 0.03), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-3.0)
    
    # slider_example1
    main.slider_2 = visual.ImageStim(win=main.win, name='slider_2', image='resources/slider_ex_right.png', mask=None, anchor='center', ori=0.0, pos=(0, 0.18), size=(1.05, 0.6), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.slider_2_ger = visual.ImageStim(win=main.win, name='slider_2', image='resources/slider_ex_right_ger.png', mask=None, anchor='center', ori=0.0, pos=(0, 0.18), size=(1.05, 0.6), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.proceed_12 = keyboard.Keyboard()
    main.text_15 = visual.TextStim(win=main.win, name='text_15', text='', font='Times New Roman', pos=(0, -0.3), height=0.027, wrapWidth=1.0, ori=0.0, color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0)
    main.arrow_5 = visual.ImageStim(win=main.win, name='arrow_5', image='resources/arrow.png', mask=None, anchor='center', ori=90.0, pos=(0.12, -0.12), size=(0.06, 0.03), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-3.0)
    
    # ghost_marker
    main.slider_ghost = visual.ImageStim(win=main.win, name='slider_2', image='resources/slider_ghost_eng.png', mask=None, anchor='center', ori=0.0, pos=(0, 0.18), size=(1.05, 0.6), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.slider_ghost_ger = visual.ImageStim(win=main.win, name='slider_2', image='resources/slider_ghost_ger.png', mask=None, anchor='center', ori=0.0, pos=(0, 0.18), size=(1.05, 0.6), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.proceed_ghost = keyboard.Keyboard()
    main.text_ghost = visual.TextStim(win=main.win, name='text_15', text='', font='Times New Roman', pos=(0, -0.3), height=0.027, wrapWidth=1.0, ori=0.0, color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0)
    main.arrow_ghost = visual.ImageStim(win=main.win, name='arrow_5', image='resources/arrow.png', mask=None, anchor='center', ori=90.0, pos=(0.04, -0.12), size=(0.06, 0.03), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-3.0)
    
    # choice
    main.space_image_4 = visual.ImageStim(win=main.win, name='space_image_4', image='resources/choice_mouse.png', mask=None, anchor='center', ori=0.0, pos=(0, 0.18), size=(1.05, 0.6), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.space_image_4_ger = visual.ImageStim(win=main.win, name='space_image_4', image='resources/choice_ger.png', mask=None, anchor='center', ori=0.0, pos=(0, 0.18), size=(1.05, 0.6), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.text_16 = visual.TextStim(win=main.win, name='text_16', text='', font='Times New Roman', pos=(0, -0.3), height=0.027, wrapWidth=1.4, ori=0.0, color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-1.0) #wrapWidth 1.0 to 1.4
    main.proceed_13 = keyboard.Keyboard()
    
    # reward
    main.proceed_14 = keyboard.Keyboard()
    main.space_image_5 = visual.ImageStim(win=main.win, name='space_image_5', image='resources/reward.png', mask=None, anchor='center', ori=0.0, pos=(0, 0.18), size=(1.05, 0.6), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-1.0)
    main.space_image_5_ger = visual.ImageStim(win=main.win, name='space_image_5', image='resources/reward_ger.png', mask=None, anchor='center', ori=0.0, pos=(0, 0.18), size=(1.05, 0.6), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-1.0)
    main.text_17 = visual.TextStim(win=main.win, name='text_17', text='', font='Times New Roman', pos=(0, -0.3), height=0.027, wrapWidth=1.0, ori=0.0, color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0)
    
    # no_reward
    main.proceed_15 = keyboard.Keyboard()
    main.space_image_6 = visual.ImageStim(win=main.win, name='space_image_6', image='resources/no_reward.png', mask=None, anchor='center', ori=0.0, pos=(0, 0.18), size=(1.05, 0.6), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-1.0)
    main.space_image_6_ger = visual.ImageStim(win=main.win, name='space_image_6', image='resources/no_reward_ger.png', mask=None, anchor='center', ori=0.0, pos=(0, 0.18), size=(1.05, 0.6), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-1.0)
    main.text_18 = visual.TextStim(win=main.win, name='text_18', text='', font='Times New Roman', pos=(0, -0.3), height=0.027, wrapWidth=1.0, ori=0.0, color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0)
    
    # points
    main.space_bg_11 = visual.ImageStim(win=main.win, name='space_bg_11', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.proceed_16 = keyboard.Keyboard()
    main.text_19 = visual.TextStim(win=main.win, name='text_19', text='', font='Times New Roman', pos=(0, 0), height=0.027, wrapWidth=1.0, ori=0.0, color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0)
    
    # congruence_caution
    main.space_bg_congruence_caution = visual.ImageStim(win=main.win, name='space_bg_11', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.proceed_congruence_caution = keyboard.Keyboard()
    main.text_congruence_caution = visual.TextStim(win=main.win, name='text_19', text='', font='Times New Roman', pos=(0, 0), height=0.027, wrapWidth=1.0, ori=0.0, color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0)
    
    # slider_accuracy
    main.space_bg_slider_accuracy = visual.ImageStim(win=main.win, name='space_bg_11', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.proceed_slider_accuracy = keyboard.Keyboard()
    main.text_slider_accuracy = visual.TextStim(win=main.win, name='text_19', text='', font='Times New Roman', pos=(0, 0), height=0.027, wrapWidth=1.0, ori=0.0, color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0)
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # MAIN BLOCK ROUTINES
    
    # intro_pu
    main.text = 'hello' # watch out
    main.space_bg_10 = visual.ImageStim(win=main.win,name='space_bg_10', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-1.0)
    main.proceed_3 = keyboard.Keyboard()
    main.text_7 = visual.TextStim(win=main.win, name='text_7',text='',font='Times New Roman',pos=(0, 0), height=0.03, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-3.0);
    # prac_block
    main.space_image_7 = visual.ImageStim(win=main.win, name='space_image_7', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-1.0)
    main.proceed_17 = keyboard.Keyboard()
    main.text_20 = visual.TextStim(win=main.win, name='text_20', text='', font='Times New Roman', pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-3.0);
    # primer_mu
    main.space_bg_12 = main.space_image_7; main.space_bg_12.name = 'space_bg_12'; main.space_bg_12.depth = 0.0
    main.shuttle_5 = visual.ImageStim(win=main.win, name='shuttle_5', image='resources/space-shuttle.png', mask=None, anchor='center', ori=0.0, pos=(0, -0.15), size=(0.2, 0.2), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-2.0)
    main.planet_right_6 = visual.ImageStim(win=main.win, name='planet_right_6', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-3.0)
    main.planet_left_6 = visual.ImageStim(win=main.win, name='planet_left_6', image='sin', mask=None, anchor='center', ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-4.0)
    main.arrow_left_3 = visual.ImageStim(win=main.win, name='arrow_left_3', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.2,0.35), color=[1,1,1], colorSpace='rgb', opacity=0.5, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-5.0)
    main.mu_5 = visual.Slider(win=main.win, name='mu_5', startValue=None, size=(0.8, 0.03), pos=(0, -0.38), units=None, labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0, style='rating', styleTweaks=(), opacity=None, labelColor=[0.8824, 0.9451, 1.0000], markerColor=[1.0000, 1.0000, 1.0000], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb', font='Times New Roman', labelHeight=0.03, flip=False, ori=0.0, depth=-6, readOnly=True)
    main.text_21 = visual.TextStim(win=main.win, name='text_21', text='', font='Times New Roman', pos=(0, -0.3), height=0.03, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-7.0);
    main.key_resp_3 = keyboard.Keyboard()
    main.mu_ghost = visual.Slider(win=main.win, name='mu_ghost', startValue=None, size=(0.8, 0.03), pos=(0, -0.38), units=None, labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0, style='rating', styleTweaks=(), opacity=0, labelColor=[0.8824, 0.9451, 1.0000], markerColor=[-0.4980, 0.7569, 0.6314], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb', font='Times New Roman', labelHeight=0.03, flip=False, ori=0.0, depth=-6.0, readOnly=True)
    # fixation
    main.space_image_fixation = visual.ImageStim(win=main.win,name='space_image_3', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
#    main.fixation_dot = visual.Circle(win = main.win, radius=10, fillColor='white', lineColor='white', pos=(0, 0))
    main.fixation_dot = visual.ShapeStim(win=main.win, name='fixation_dot',size=(0.025, 0.025), vertices='circle',ori=0.0, pos=(0, 0), anchor='center',lineWidth=1.0, colorSpace='rgb',  lineColor='white', fillColor='white',opacity=None, depth=-3.0, interpolate=True)
    # signal
    main.space_image_8 = main.space_bg_12; main.space_image_8.name = 'space_image_8'
    main.radar_3 = visual.ImageStim(win=main.win, name='radar_3', image='resources/radar_grayl.png', mask=None, anchor='center', ori=0.0, pos=(0,0), size=(0.6, 0.6), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-1.0)
    main.left_patch_7 = visual.GratingStim(win=main.win, name='left_patch_7', tex='sin', mask='gauss', anchor='center', ori=0.0, pos=(-0.12, 0), size=(0.12, 0.12), sf=8.0, phase=0.0, color=[1,1,1], colorSpace='rgb', opacity=None, contrast=1.0, blendmode='avg', texRes=512.0, interpolate=True, depth=-2.0)
    main.fix_circle_7 = visual.ShapeStim(win=main.win, name='fix_circle_7', size=(0.007, 0.007), vertices='circle', ori=0.0, pos=(0, 0), anchor='center', lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black', opacity=None, depth=-3.0, interpolate=True)
    main.right_patch_7 = visual.GratingStim(win=main.win, name='right_patch_7', tex='sin', mask='gauss', anchor='center', ori=0.0, pos=(0.12, 0), size=(0.12, 0.12), sf=8.0, phase=0.0, color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, contrast=1.0, blendmode='avg', texRes=512.0, interpolate=True, depth=-4.0)
    # slider_3
    main.space_bg_13 = main.space_bg_12; main.space_bg_13.name = 'space_bg_13'
    #self.space_bg_13 = visual.ImageStim(win=self.win, name='space_bg_13', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.text_22 = visual.TextStim(win=main.win, name='text_22', text='', font='Times New Roman', pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0.0, color=[0.8824, 0.9451, 1.0000], colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0);
    main.reported_mu = visual.Slider(win=main.win, name='reported_mu', startValue=50, size=(0.8, 0.03), pos=(0, -0.38), units=None, labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0, style='rating', styleTweaks=(), opacity=None, labelColor=[0.8824, 0.9451, 1.0000], markerColor=[1.0000, 1.0000, 1.0000], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb', font='Times New Roman', labelHeight=0.03, flip=False, ori=0.0, depth=-3, readOnly=False)
    main.mu_ghost = visual.Slider(win=main.win, name='mu_ghost', startValue=None, size=(0.8, 0.03), pos=(0, -0.38), units=None, labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0, style='rating', styleTweaks=(), opacity=0, labelColor=[0.8824, 0.9451, 1.0000], markerColor=[-0.4980, 0.7569, 0.6314], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb', font='Times New Roman', labelHeight=0.03, flip=False, ori=0.0, depth=-6.0, readOnly=True)
    main.shuttle_3 = visual.ImageStim(win=main.win, name='shuttle_3', image='resources/space-shuttle.png', mask=None, anchor='center', ori=0.0, pos=(0, -0.15), size=(0.2, 0.2), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-4.0)
    main.planet_right_7 = visual.ImageStim(win=main.win, name='planet_right_7', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-5.0)
    main.planet_left_7 = visual.ImageStim(win=main.win, name='planet_left_7', image='sin', mask=None, anchor='center', ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-6.0)
    main.arrow_left_4 = visual.ImageStim(win=main.win, name='arrow_left_4', image='sin', mask=None, anchor='center', ori=1.0, pos=[0,0], size=(0.2,0.35), color=[1,1,1], colorSpace='rgb', opacity=0.5, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-7.0)
    # prechoice_text
    main.space_bg_14 = visual.ImageStim(win=main.win, name='space_bg_14', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.text_23 = visual.TextStim(win=main.win, name='text_23', text='', font='Times New Roman', pos=(0, 0), height=0.03, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-1.0);
    main.key_resp_4 = keyboard.Keyboard()
    # last_mu
    main.space_bg_15 = visual.ImageStim(win=main.win, name='space_bg_15', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.shuttle_6 = visual.ImageStim(win=main.win, name='shuttle_6', image='resources/space-shuttle.png', mask=None, anchor='center', ori=0.0, pos=(0, -0.15), size=(0.2, 0.2), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-2.0)
    main.planet_right_8 = visual.ImageStim(win=main.win, name='planet_right_8', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-3.0)
    main.planet_left_8 = visual.ImageStim(win=main.win, name='planet_left_8', image='sin', mask=None, anchor='center', ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-4.0)
    main.arrow_left_5 = visual.ImageStim(win=main.win, name='arrow_left_5', image='sin', mask=None, anchor='center', ori=1.0, pos=[0,0], size=(0.2,0.35), color=[1,1,1], colorSpace='rgb', opacity=0.5, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-5.0)
    main.mu_7 = visual.Slider(win=main.win, name='mu_7', startValue=0, size=(0.8, 0.03), pos=(0, -0.38), units=None, labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0, style='rating', styleTweaks=(), opacity=None, labelColor=[0.8824, 0.9451, 1.0000], markerColor=[-0.4980, 0.7569, 0.6314], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb', font='Times New Roman', labelHeight=0.03, flip=False, ori=0.0, depth=-6, readOnly=True)
    main.text_24 = visual.TextStim(win=main.win, name='text_24', text='', font='Times New Roman', pos=(0, -0.3), height=0.03, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-7.0);
    main.key_resp_5 = keyboard.Keyboard()
    main.text_31 = visual.TextStim(win=main.win, name='text_31', text='Press SPACEBAR to proceed.', font='Times New Roman', pos=(0, -0.45), height=0.02, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-9.0);
    # block_choice
    main.space_bg_16 = visual.ImageStim(win=main.win, name='space_bg_16', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.shuttle_7 = visual.ImageStim(win=main.win, name='shuttle_7', image='resources/space-shuttle.png', mask=None, anchor='center', ori=0.0, pos=(0, -0.135), size=(0.2, 0.2), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-1.0)
    main.planet_right_9 = visual.ImageStim(win=main.win, name='planet_right_9', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-2.0)
    main.planet_left_9 = visual.ImageStim(win=main.win, name='planet_left_9', image='sin', mask=None, anchor='center', ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-3.0)
    main.text_25 = visual.TextStim(win=main.win, name='text_25', text='', font='Times New Roman', pos=(0, -0.35), height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-4.0);
    main.question = visual.ImageStim(win=main.win, name='question', image='resources/question-mark.png', mask=None, anchor='center', ori=0.0, pos=(0, 0.05), size=(0.1, 0.1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-6.0)
    main.mouse_resp = event.Mouse(win=main.win)
    main.x, main.y = [None, None]
    main.mouse_resp.mouseClock = core.Clock()
    # block_rew
    main.space_bg_17 = visual.ImageStim(win=main.win, name='space_bg_17', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.proceed_18 = keyboard.Keyboard()
    main.text_26 = visual.TextStim(win=main.win, name='text_26',text='', font='Open Sans', pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0);
    main.planet = visual.ImageStim(win=main.win, name='planet', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.5, 0.5), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-3.0)
    main.shuttle_8 = visual.ImageStim(win=main.win, name='shuttle_8', image='resources/shuttle_fire.png', mask=None, anchor='center', ori=1.0, pos=[0,0], size=(0.2, 0.3), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-4.0)
    main.crystal = visual.ImageStim(win=main.win, name='crystal', image='resources/crystal.png', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.1, 0.1), color=[1,1,1], colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-6.0)
    # block_completed
    main.space_bg_18 = visual.ImageStim(win=main.win, name='space_bg_18', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
    main.proceed_19 = keyboard.Keyboard()
    main.text_27 = visual.TextStim(win=main.win, name='text_27', text='', font='Times New Roman', pos=[0,0], height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0);
    # task_score
    main.space_bg_19 = visual.ImageStim(win=main.win, name='space_bg_19', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-1.0)
    main.text_28 = visual.TextStim(win=main.win, name='text_28', text='', font='Times New Roman', pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-2.0);
    main.proceed_20 = keyboard.Keyboard()