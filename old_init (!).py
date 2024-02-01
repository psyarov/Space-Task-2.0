# OLD INITIALIZATION, WHICH MADE THE CODE MUCH FASTER THOUGH!

main.initialize_routines()                                                   # creates distinct component lists for all routines


    def initialize_routines(self):
        '''
        Function to initialize the components of all routine with specific values.
        '''
        

        # welcome
        self.instru = 'doh'
        self.space_bg_4 = visual.ImageStim(win=self.win, name='space_bg_4', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
        self.text_8 = visual.TextStim(win=self.win, name='text_8',text = '',font='Times New Roman',pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-1.0);
        self.proceed_4 = keyboard.Keyboard()
        # intro_planet
        self.space_image_2 = visual.ImageStim(win=self.win,name='space_image_2',image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
        self.shuttle_4 = visual.ImageStim(win=self.win,name='shuttle_4',image='resources/space-shuttle.png', mask=None, anchor='center',ori=0.0, pos=(0, -0.08), size=(0.2, 0.2),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-1.0)
        self.planet_right_3 = visual.ImageStim(win=self.win,name='planet_right_3',image='resources/green_blur.png', mask=None, anchor='center',ori=0.0, pos=[0,0], size=(0.15, 0.15),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-2.0)
        self.planet_left_3 = visual.ImageStim(win=self.win,name='planet_left_3',image='resources/blue_blur.png', mask=None, anchor='center',ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-3.0)
        self.text_11 = visual.TextStim(win=self.win, name='text_11',text='',font='Times New Roman',pos=(0, -0.33), height=0.027, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-4.0);
        self.proceed_7 = keyboard.Keyboard()
        self.radar_2 = visual.ImageStim(win=self.win,name='radar_2', image='resources/radar_grayl.png', mask=None, anchor='center',ori=0.0, pos=(0,0.18), size=(0.3, 0.3),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-6.0)
        self.text_3 = visual.TextStim(win=self.win, name='text_3',text='Radar',font='Times New Roman',pos=(0.25, 0.18), height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-7.0);
        self.arrow = visual.ImageStim(win=self.win,name='arrow', image='resources/arrow.png', mask=None, anchor='center',ori=0.0, pos=(0.185, 0.175), size=(0.06, 0.03),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-8.0)
        self.left_patch = visual.GratingStim(win=self.win, name='left_patch',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(-0.065, 0.18), size=(0.08, 0.08), sf=8.0, phase=0.0,color=[1,1,1], colorSpace='rgb',opacity=None, contrast=0.9, blendmode='avg',texRes=512.0, interpolate=True, depth=-9.0)
        self.right_patch = visual.GratingStim(win=self.win, name='right_patch',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(0.065, 0.18), size=(0.08, 0.08), sf=8.0, phase=0.0,color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',opacity=None, contrast=0.1, blendmode='avg',texRes=512.0, interpolate=True, depth=-10.0)
        self.fix_circle = visual.ShapeStim(win=self.win, name='fix_circle',size=(0.007, 0.007), vertices='circle',ori=0.0, pos=(0, 0.18), anchor='center',lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',opacity=None, depth=-11.0, interpolate=True)
        # intro_radar
        self.space_bg_5 = visual.ImageStim(win=self.win,name='space_bg_5', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
        self.radar_4 = visual.ImageStim(win=self.win,name='radar_4', image='resources/radar_grayl.png', mask=None, anchor='center',ori=0.0, pos=(0,0.1), size=(0.6, 0.6),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-1.0)
        self.text_9 = visual.TextStim(win=self.win, name='text_9',text='',font='Times New Roman',pos=(0, -0.3), height=0.03, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-2.0);
        self.proceed_5 = keyboard.Keyboard()
        # intro_signal
        self.space_bg_6 = visual.ImageStim(win=self.win,name='space_bg_6', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
        self.radar_5 = visual.ImageStim(win=self.win,name='radar_5', image='resources/radar_grayl.png', mask=None, anchor='center',ori=0.0, pos=(0,0.1), size=(0.6, 0.6),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-1.0)
        self.left_patch_4 = visual.GratingStim(win=self.win, name='left_patch_4',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(-0.12, 0.1), size=(0.12, 0.12), sf=8.0, phase=0.0,color=[1,1,1], colorSpace='rgb',opacity=None, contrast=0.9, blendmode='avg',texRes=512.0, interpolate=True, depth=-2.0)
        self.right_patch_4 = visual.GratingStim(win=self.win, name='right_patch_4',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(0.12, 0.1), size=(0.12, 0.12), sf=8.0, phase=0.0,color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',opacity=None, contrast=0.1, blendmode='avg',texRes=512.0, interpolate=True, depth=-3.0)
        self.text_10 = visual.TextStim(win=self.win, name='text_10',text='',font='Times New Roman',pos=(0, -0.3), height=0.03, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-4.0);
        self.proceed_6 = keyboard.Keyboard()
        self.fix_circle_4 = visual.ShapeStim(win=self.win, name='fix_circle_4',size=(0.007, 0.007), vertices='circle',ori=0.0, pos=(0, 0.1), anchor='center',lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',opacity=None, depth=-6.0, interpolate=True)
        # intro_crystal
        self.space_bg_7 = visual.ImageStim(win=self.win,name='space_bg_7', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
        self.radar_6 = visual.ImageStim(win=self.win,name='radar_6', image='resources/radar_grayl.png', mask=None, anchor='center',ori=0.0, pos=(0,0.1), size=(0.6, 0.6),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-1.0)
        self.left_patch_5 = visual.GratingStim(win=self.win, name='left_patch_5',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(-0.12, 0.1), size=(0.12, 0.12), sf=8.0, phase=0.0,color=[1,1,1], colorSpace='rgb',opacity=None, contrast=0.9, blendmode='avg',texRes=512.0, interpolate=True, depth=-2.0)
        self.right_patch_5 = visual.GratingStim(win=self.win, name='right_patch_5',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(0.12, 0.1), size=(0.12, 0.12), sf=8.0, phase=0.0,color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',opacity=None, contrast=0.1, blendmode='avg',texRes=512.0, interpolate=True, depth=-3.0)
        self.text_12 = visual.TextStim(win=self.win, name='text_12',text='',font='Times New Roman',pos=(0, -0.32), height=0.025, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-4.0);
        self.proceed_8 = keyboard.Keyboard()
        self.fix_circle_5 = visual.ShapeStim(win=self.win, name='fix_circle_5',size=(0.007, 0.007), vertices='circle',ori=0.0, pos=(0, 0.1), anchor='center',lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',opacity=None, depth=-6.0, interpolate=True)
        self.planet_right_4 = visual.ImageStim(win=self.win,name='planet_right_4', image='resources/green_blur.png', mask=None, anchor='center',ori=0.0, pos=[0,0], size=(0.15, 0.15),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-7.0)
        self.planet_left_4 = visual.ImageStim(win=self.win,name='planet_left_4', image='resources/blue_blur.png', mask=None, anchor='center',ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-8.0)
        self.arrow_2 = visual.ImageStim(win=self.win,name='arrow_2', image='resources/arrow.png', mask=None, anchor='center',ori=90.0, pos=(-0.4, 0.23), size=(0.2, 0.05),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-9.0)
        # intro_crystal2
        self.space_bg_8 = visual.ImageStim(win=self.win,name='space_bg_8', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
        self.radar_7 = visual.ImageStim(win=self.win,name='radar_7', image='resources/radar_grayl.png', mask=None, anchor='center',ori=0.0, pos=(0,0.1), size=(0.6, 0.6),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-1.0)
        self.left_patch_6 = visual.GratingStim(win=self.win, name='left_patch_6',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(-0.12, 0.1), size=(0.12, 0.12), sf=8.0, phase=0.0,color=[1,1,1], colorSpace='rgb',opacity=None, contrast=0.1, blendmode='avg',texRes=512.0, interpolate=True, depth=-2.0)
        self.right_patch_6 = visual.GratingStim(win=self.win, name='right_patch_6',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(0.12, 0.1), size=(0.12, 0.12), sf=8.0, phase=0.0,color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',opacity=None, contrast=0.9, blendmode='avg',texRes=512.0, interpolate=True, depth=-3.0)
        self.text_13 = visual.TextStim(win=self.win, name='text_13',text='',font='Times New Roman',pos=(0, -0.33), height=0.025, wrapWidth=1.2, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-4.0);
        self.proceed_9 = keyboard.Keyboard()
        self.fix_circle_6 = visual.ShapeStim(win=self.win, name='fix_circle_6',size=(0.007, 0.007),vertices='circle',ori=0.0,pos=(0, 0.1),anchor='center',lineWidth=1.0,colorSpace='rgb',lineColor='black',fillColor='black',opacity=None,depth=-6.0,interpolate=True) # wrapWidth: 1.0->1.2
        self.arrow_3 = visual.ImageStim(win=self.win,name='arrow_3', image='resources/arrow.png', mask=None, anchor='center',ori=90.0, pos=(0.4, 0.23), size=(0.2, 0.05),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-7.0)
        self.planet_right_5 = visual.ImageStim(win=self.win,name='planet_right_5', image='resources/green_blur.png', mask=None, anchor='center',ori=0.0, pos=[0,0], size=(0.15, 0.15),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-8.0)
        self.planet_left_5 = visual.ImageStim(win=self.win,name='planet_left_5', image='resources/blue_blur.png', mask=None, anchor='center',ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-9.0)
        # training_block
        self.space_bg = visual.ImageStim(win=self.win,name='space_bg', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
        self.proceed_2 = keyboard.Keyboard()
        self.text_5 = visual.TextStim(win=self.win, name='text_5',text='',font='Times New Roman',pos=(0, 0), height=0.03, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-2.0);
        # space
        self.space_image = visual.ImageStim(win=self.win,name='space_image', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
        self.radar = visual.ImageStim(win=self.win,name='radar', image='resources/radar_grayl.png', mask=None, anchor='center',ori=0.0, pos=(0,0), size=(0.6, 0.6),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-1.0)
        self.left_patch_3 = visual.GratingStim(win=self.win, name='left_patch_3',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(-0.12, 0), size=(0.12, 0.12), sf=8.0, phase=0.0,color=[1,1,1], colorSpace='rgb',opacity=None, contrast=1.0, blendmode='avg',texRes=512.0, interpolate=True, depth=-2.0)
        self.fix_circle_3 = visual.ShapeStim(win=self.win, name='fix_circle_3',size=(0.007, 0.007), vertices='circle',ori=0.0, pos=(0, 0), anchor='center',lineWidth=1.0, colorSpace='rgb',  lineColor='black', fillColor='black',opacity=None, depth=-3.0, interpolate=True)
        self.right_patch_3 = visual.GratingStim(win=self.win, name='right_patch_3',tex='sin', mask='gauss', anchor='center',ori=0.0, pos=(0.12, 0), size=(0.12, 0.12), sf=8.0, phase=0.0,color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',opacity=None, contrast=1.0, blendmode='avg',texRes=512.0, interpolate=True, depth=-4.0)
        self.choice_training = keyboard.Keyboard()
        # feedback
        self.space_image_3 = visual.ImageStim(win=self.win,name='space_image_3', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=0.0)
        self.msg = 'hello'
        self.fb_msg = visual.TextStim(win=self.win, name='fb_msg',text='',font='Times New Roman',pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-2.0);
        # intro_pu
        self.text = 'hello' # watch out
        self.space_bg_10 = visual.ImageStim(win=self.win,name='space_bg_10', image='resources/space3.png', mask=None, anchor='center',ori=0.0, pos=(0, 0), size=(2, 1),color=[1,1,1], colorSpace='rgb', opacity=None,flipHoriz=False, flipVert=False,texRes=128.0, interpolate=True, depth=-1.0)
        self.proceed_3 = keyboard.Keyboard()
        self.text_7 = visual.TextStim(win=self.win, name='text_7',text='',font='Times New Roman',pos=(0, 0), height=0.03, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=-3.0);
        # prac_block
        self.space_image_7 = visual.ImageStim(win=self.win, name='space_image_7', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-1.0)
        self.proceed_17 = keyboard.Keyboard()
        self.text_20 = visual.TextStim(win=self.win, name='text_20', text='', font='Times New Roman', pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-3.0);
        # primer_mu
        self.space_bg_12 = self.space_image_7; self.space_bg_12.name = 'space_bg_12'; self.space_bg_12.depth = 0.0
        self.shuttle_5 = visual.ImageStim(win=self.win, name='shuttle_5', image='resources/space-shuttle.png', mask=None, anchor='center', ori=0.0, pos=(0, -0.15), size=(0.2, 0.2), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-2.0)
        self.planet_right_6 = visual.ImageStim(win=self.win, name='planet_right_6', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-3.0)
        self.planet_left_6 = visual.ImageStim(win=self.win, name='planet_left_6', image='sin', mask=None, anchor='center', ori=0.0, pos=(-0.4, 0.4), size=(0.15, 0.15), color=[1,1,1], colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-4.0)
        self.arrow_left_3 = visual.ImageStim(win=self.win, name='arrow_left_3', image='sin', mask=None, anchor='center', ori=0.0, pos=[0,0], size=(0.2,0.35), color=[1,1,1], colorSpace='rgb', opacity=0.5, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-5.0)
        self.mu_5 = visual.Slider(win=self.win, name='mu_5', startValue=None, size=(0.8, 0.03), pos=(0, -0.38), units=None, labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0, style='rating', styleTweaks=(), opacity=None, labelColor=[0.8824, 0.9451, 1.0000], markerColor=[1.0000, 1.0000, 1.0000], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb', font='Times New Roman', labelHeight=0.03, flip=False, ori=0.0, depth=-6, readOnly=True)
        self.text_21 = visual.TextStim(win=self.win, name='text_21', text='', font='Times New Roman', pos=(0, -0.3), height=0.03, wrapWidth=1.0, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR', depth=-7.0);
        self.key_resp_3 = keyboard.Keyboard()
        self.mu_ghost = visual.Slider(win=self.win, name='mu_ghost', startValue=None, size=(0.8, 0.03), pos=(0, -0.38), units=None, labels=(0, 25, 50, 75, 100), ticks=(0, 25, 50, 75, 100), granularity=0.0, style='rating', styleTweaks=(), opacity=0, labelColor=[0.8824, 0.9451, 1.0000], markerColor=[-0.4980, 0.7569, 0.6314], lineColor=[0.8824, 0.9451, 1.0000], colorSpace='rgb', font='Times New Roman', labelHeight=0.03, flip=False, ori=0.0, depth=-6.0, readOnly=True)
        # signal
        self.space_image_8 = self.space_bg_12; self.space_image_8.name = 'space_image_8'
        self.radar_3 = visual.ImageStim(win=self.win, name='radar_3', image='resources/radar_grayl.png', mask=None, anchor='center', ori=0.0, pos=(0,0), size=(0.6, 0.6), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=-1.0)
        self.left_patch_7 = visual.GratingStim(win=self.win, name='left_patch_7', tex='sin', mask='gauss', anchor='center', ori=0.0, pos=(-0.12, 0), size=(0.12, 0.12), sf=8.0, phase=0.0, color=[1,1,1], colorSpace='rgb', opacity=None, contrast=1.0, blendmode='avg', texRes=512.0, interpolate=True, depth=-2.0)
        self.fix_circle_7 = visual.ShapeStim(win=self.win, name='fix_circle_7', size=(0.007, 0.007), vertices='circle', ori=0.0, pos=(0, 0), anchor='center', lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black', opacity=None, depth=-3.0, interpolate=True)
        self.right_patch_7 = visual.GratingStim(win=self.win, name='right_patch_7', tex='sin', mask='gauss', anchor='center', ori=0.0, pos=(0.12, 0), size=(0.12, 0.12), sf=8.0, phase=0.0, color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, contrast=1.0, blendmode='avg', texRes=512.0, interpolate=True, depth=-4.0)
        # slider_3
        self.space_bg_13 = self.space_bg_12; self.space_bg_13.name = 'space_bg_13'
        #self.space_bg_13 = visual.ImageStim(win=self.win, name='space_bg_13', image='resources/space3.png', mask=None, anchor='center', ori=0.0, pos=(0, 0), size=(2, 1), color=[1,1,1], colorSpace='rgb', opacity=None, flipHoriz=False, flipVert=False, texRes=128.0, interpolate=True, depth=0.0)
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
