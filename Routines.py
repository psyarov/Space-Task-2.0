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
from Practice import prob, prob1, space_slider, space_slider2, slider_example, slider_example1, ghost_marker, slider_accuracy, demo, incong_vid, demo_incong, choice, reward, no_reward, congruence_caution, points


# HANDLES ALL ROUTINES
# BACKBONE OF THE EXPERIMENT

class Routines:

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # VARIABLE INITIALIZATION
    endExpNow = False                                                        # checks whether experiment should be ended ('True' when ending condition is met)
    frameTolerance = 0.001                                                   # used to time the routines
    task_rew = 0                                                             # stores how many points participant wins throughout the task
    rew = 'hello'                                                            # stores text about whether crystals are found
    block_str = 'hello'                                                      # stores text about how many blocks have been completed
    lists = [0, 1, 2, 3] #, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]         # manipulate number of blocks
    block_lists = lists                                                      # stores number values and order of the blocks
    number_of_blocks = len(block_lists)                                      # stores the number of blocks
    random.shuffle(block_lists);                                             # shuffles the order of the blocks
    x = [0] #,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]               # manipulate number of trials
    random.shuffle(x);                                                       # shuffle the order of trials
    trial_lists = x;                                                         # list for the order of trials
    ques_word = 'hello'                                                      # random variable to locally store text value which is later anyway added to another variable (can be used multiple times)
    total_blocks = number_of_blocks                                          # variable to store the total number of blocks
    block_num = 0;                                                           # variable to follow the block number
    cond1_rew = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0];                     # stores possibility of finding crystals for mixed uncertainty condition
    cond2_rew = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0];                     # stores possibility of finding crystals for perceptual uncertainty condition
    random.shuffle(cond1_rew);                                               # shuffles possibility variables for mixed condition
    random.shuffle(cond2_rew);                                               # shuffles possibility variables for perceptual condition
    mu = 0                                                                   # stores slider value
    training_blocks = None                                                   # stores data from training_blocks handler
    thisTraining_block = None                                                # stores conditions for current training block
    training = None                                                          # stores data from training handler
    thisTraining = None                                                      # stores conditions for current trial of a certain training block
    
    
    # experiment information (variables)
    _thisDir = None                                                          # stores the path name for the experiment directory
    psychopyVersion = None                                                   # stores psychopy version name
    expName = None                                                           # stores the name of the experiment
    expInfo = None                                                           # dictionary to save experiment info (participant, session, etc.)
    
    # participant window
    dlg = None                                                               # participant window module (psychopy library)
    filename = None                                                          # saves the file name for the current participant
    
    # experiment handler
    thisExp = None                                                           # experiment handler (stores information about the experiment throughout the whole task)
    logFile = None                                                           # creates a log file
    logging = None                                                           # variable for setting of logging level 
    
    # setup window
    win = None                                                               # window module (pp library)
    frameDur = None                                                          # variable for frame duration
    
    # setup devices
    ioConfig = None                                                          # input/output configuration handling
    ioSession = None                                                         # current session
    ioServer = None                                                          # connection to server
    io = None                                                                # generic interface
    eyetracker = False                                                       # checks whether eyetracker is also used
    defaultKeyboard = None                                                   # used with keyboard module (pp library)
    
    # VARIABLE COUNTERBALANCING FOR PRACTICE TASK
    pr_number_list = [1,2,3,4]
    random.shuffle(pr_number_list)
    cbal = pr_number_list[1]
    if cbal == 1:
        third_blocks = [17,18,19,21,22,23];
        random.shuffle(third_blocks);
        third_block = third_blocks[1];
        print(third_block)
        pr_lists = [16,20,third_block];#4,13,9,0];
    elif cbal == 2:
        third_blocks = [16,18,19,20,22,23];
        random.shuffle(third_blocks);
        third_block = third_blocks[1];
        print(third_block)
        pr_lists = [17,21,third_block];#,12,5,11,3];
    elif cbal == 3:
        third_blocks = [16,17,19,20,21,23];
        random.shuffle(third_blocks);
        third_block = third_blocks[1];
        print(third_block)
        pr_lists = [18,22,third_block];#,15,6,2,1];
    else:
        third_blocks = [16,17,18,20,21,22];
        random.shuffle(third_blocks);
        third_block = third_blocks[1];
        print(third_block)
        pr_lists = [19,23,third_block];#,7,14,10,8];
    pr_blok_num = 1
    criterion_met = 0
    pr_block_lists = pr_lists
    pr_total_blocks = 7
    
    # create timers
    globalClock = None                                                       # sets up a global clock
    routineTimer = None                                                      # sets up a routine timer component
    
    # prac_main handler
    prac_main_task = None                                                    # stores data and conditions for main/prac tasks
    thisPrac_main_task = None                                                # stores data and conditions for current iteration of prac_main_task (either main or prac)
    currentLoop = None                                                       # stores data and conditions of current main/prac loop
    block = None                                                             # stores data and conditions for all blocks
    thisBlock = None                                                         # stors data and condition for current block
    task_file = None                                                         # stores task file path name
    primer = None                                                            # stores data and conditions for all primers (primer=1 trial of each block)
    thisPrimer = None                                                        # stores data and conditions for current primer
    condition_file = None                                                    # stores condition file path name
    trials = None                                                            # stores data and conditions for all trials
    thisTrial = None                                                         # stores data and codnitions for current trial
    last = None                                                              # stores data and conditions for all last slider uses of a block
    thisLast = None                                                          # stores data and conditions for last slider use

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __init__(self, type, handler, timing, components):
        '''
         Constructor for the class.
         
         Parameters:
         - type: Type of the instance.
         - handler: Handler instance for managing experimental data.
         - timing: Timing instance for managing timing-related functionalities.
         - components: Components instance for managing stimuli and responses.
        '''

        self.type = type
        self.handler = handler
        self.timing = timing
        self.components = components

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def initialize_routines(self):
        components_init(self)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def generate_zero_or_one(probability):
        '''
        Generates 0 or 1 with the given probability.
    
        Parameters:
        - probability (float): The probability of generating 1.
    
        Returns:
        - int: 0 or 1 based on the generated result.
        '''

        if random.random() < probability:
            return 1
        else:
            return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def setup(self):
        '''
        Prepares the start of the experiment. Assigns path names, extracts information from resources folder,
        asks for participant info input.
        '''
        self.handler.experiment_info(self)
        self.handler.participant_window(self)
        self.handler.experiment_handler(self)
        self.handler.setup_window(self)
        self.handler.setup_devices(self)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def prepare_routine(self, components):
        '''
        Prepares the routine by resetting timers, keeping track of component start/stop times,
        and resetting timers again.
    
        Parameters:
        - components (list): All components of a given routine.
    
        Returns:
        - components (list): The same components but with recorded start/stop times.
        '''
        
        self.timing.routine_reset(self)
        components = self.timing.keep_track(components)
        self.timing.reset_timers(self) # check
        return components

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def run_routine(self, components):
        '''
        Runs the routine, currently only functional for language_preference (also redundant at this point).
    
        Parameters:
        - components (list): All components of a given routine.

        Returns:
        - components (list): The same components but with recorded start/stop times.
        '''
        
        while self.continueRoutine:
            self.timing.get_current_time(self.language_preferenceClock, self)
            self.frameN = self.frameN + 1
            self.text_101 = self.components.text_or_image_update(self.text_101, 'text_101.started', self) # VERY CAREFUL HERE, CAUSE I'VE ADDED A TIMESTAMP IN THE FUNCTION which wasn't originally there for text_101
            self.waitOnFlip = False
            #self.lang_keys, self._lang_keys_allKeys = self.keys_update(self.lang_keys, self._lang_keys_allKeys, 'redundant') -> fix this
            if self.lang_keys.status == NOT_STARTED and self.tThisFlip >= 0.0-self.frameTolerance:
                self.lang_keys = self.components.keys_update_1(self.lang_keys, self)
            if self.lang_keys.status == STARTED and not self.waitOnFlip:
                self._lang_keys_allKeys, self.lang_keys = self.components.keys_update_2(self.lang_keys, self._lang_keys_allKeys, ['e','g'], self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: break
            self.continueRoutine = False
            components = self.components.check_if_components_finished(components, self)
            if self.continueRoutine: self.win.flip()
        return components

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def end_routine(self, components):
        '''
        Ends the routine by hiding components, saving key responses, and resetting timers.
    
        Parameters:
        - components (list): All components of a given routine.
    
        Returns:
        - components (list): The same components but with recorded start/stop times.
        '''
        
        components = self.components.hide_components(components)
        self.thisExp.addData('text_101.started', self.text_101.tStartRefresh)
        self.thisExp.addData('text_101.stopped', self.text_101.tStopRefresh)
        self.lang_keys = self.components.save_key_response(self.lang_keys, 'lang_keys.keys', 'lang_keys.rt', self)
        self.thisExp.addData('lang_keys.started', self.lang_keys.tStartRefresh)
        self.thisExp.addData('lang_keys.stopped', self.lang_keys.tStopRefresh)
        self.thisExp.nextEntry()
        self.routineTimer.reset()
        return components

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def language_preference(self):
        '''
        Prepares, runs and ends language preference routine, where participant chooses between english and german instructions.
        '''
        
        # prepare routine & components
        self.text_101.setText('Bitte gib an, welche Sprache du für die Instruktionen bevorzugst.\n\nDrücke G für Deutsch. \nDrücke E für Englisch.\n\nIndicate the language that you prefer for the task instructions.\n\nPress G for German. \nPress E for English.')
        self.text_101.color = 'black'
        self.lang_keys.keys = []
        self.lang_keys.rt = []
        self._lang_keys_allKeys = []
        self.language_preference_components = [self.text_101, self.lang_keys]
        self.language_preference_components = self.prepare_routine(self.language_preference_components)
        self.language_preferenceClock.reset(-self._timeToFirstFrame)
        
        # run routine
        self.language_preference_components = self.run_routine(self.language_preference_components)
        
        # end routine
        self.language_preference_components = self.end_routine(self.language_preference_components)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def welcome(self):
        '''
        Prepares, runs and ends routine for welcoming of the participants into the experiment.
        '''
        
        # prepare
        if self.lang_keys.keys == 'g':
            instr= 'Willkommen zur Weltraum-Aufgabe.\nHerzlichen Glückwunsch, du wirst jetzt zu unserem/unserer neuen Expert:in für Radarsignale aus dem Weltraum ausgebildet!\n\nDrücke die LEERTASTE, um fortzufahren.\n'    
        else:
            instr= 'Welcome to the Space Task.\nCongratulations, you are now going to get trained to be our new expert for radar signals from space!\n\nPress SPACEBAR to proceed.\n'
        self.text_8.setText(instr)
        self.proceed_4.keys = []
        self.proceed_4.rt = []
        self._proceed_4_allKeys = []
        self.welcome_components = [self.space_bg_4, self.text_8, self.proceed_4]
        self.welcome_components = self.prepare_routine(self.welcome_components)
        
        # run
        while self.continueRoutine:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1
            self.space_bg_4 = self.components.text_or_image_update(self.space_bg_4, 'space_bg_4.started', self)
            self.text_8 = self.components.text_or_image_update(self.text_8, 'text_8.started', self)
            self.waitOnFlip = False
            self.proceed_4, self._proceed_4_allKeys = self.components.keys_update(self.proceed_4, self._proceed_4_allKeys, 'proceed_4.started', self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.welcome_components = self.components.check_if_components_finished(self.welcome_components, self)
            if self.continueRoutine: self.win.flip()
        
        # end
        self.welcome_components = self.components.hide_components(self.welcome_components)
        self.proceed_4 = self.components.save_key_response(self.proceed_4, 'proceed_4.keys', 'proceed_4.rt', self)
        self.thisExp.nextEntry() # watch out
        self.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def intro_planet(self):
        '''
        Prepares, runs and ends planet introduction routine.
        '''
        
        #prepare
        if self.lang_keys.keys == 'e':
            instr='The space ship on the screen can travel to the left or the right planet. The purpose of the journey is to find as many space crystals as possible. However, the astronauts on the space ship do not know on which planet they can find space crystals.\n\nThus, as our space station expert, you will be advising them about which planet to fly to based on the signals on the radar. The signals on the radar will indicate on which planet is it more likely to find space crystals.\n\nPress SPACEBAR if you have understood this and proceed.'
        else:
            instr='Das Raumschiff kann zum linken oder rechten Planeten fliegen. Das Ziel der Reise ist es, so viele Weltraumkristalle wie möglich zu finden. Die Astronaut:innen auf dem Raumschiff wissen jedoch nicht, auf welchem Planeten sie die Kristalle finden können.\n\nAls unser Radarexpert:in wirst du anhand von Radarsignalen entscheiden, zu welchem Planeten die Astronaut:innen fliegen werden. Die Signale auf dem Radar geben einen Hinweis, auf welchem Planeten es wahrscheinlicher ist, Weltraumkristalle zu finden.\n\n Drücke die LEERTASTE, um fortzufahren.'
        self.text_11.setText(instr)
        self.planet_right_3.setPos((0.4, 0.4))
        self.proceed_7.keys = []
        self.proceed_7.rt = []
        self._proceed_7_allKeys = []
        self.intro_planet_components = [self.space_image_2, self.shuttle_4, self.planet_right_3, self.planet_left_3, self.text_11, self.proceed_7, self.radar_2, self.text_3, self.arrow, self.left_patch, self.right_patch, self.fix_circle]
        self.intro_planet_components = self.prepare_routine(self.intro_planet_components)
        
        #run
        while self.continueRoutine:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1
            self.space_image_2 = self.components.text_or_image_update(self.space_image_2, 'space_image_2.started', self)
            self.shuttle_4 = self.components.text_or_image_update(self.shuttle_4, 'shuttle_4.started', self)
            self.planet_right_3 = self.components.text_or_image_update(self.planet_right_3, 'planet_right_3.started', self)
            self.planet_left_3 = self.components.text_or_image_update(self.planet_left_3, 'planet_left_3.started', self)
            self.text_11 = self.components.text_or_image_update(self.text_11, 'text_11.started', self)
            self.waitOnFlip = False
            self.proceed_7, self._proceed_7_allKeys = self.components.keys_update(self.proceed_7, self._proceed_7_allKeys, 'proceed_7.started', self)
            self.radar_2 = self.components.text_or_image_update(self.radar_2, 'radar_2.started', self)
            self.text_3 = self.components.text_or_image_update(self.text_3, 'text_3.started', self)
            self.arrow = self.components.text_or_image_update(self.arrow, 'arrow.started', self)
            self.left_patch = self.components.text_or_image_update(self.left_patch, 'left_patch.started', self)
            self.right_patch = self.components.text_or_image_update(self.right_patch, 'right_patch.started', self)
            self.fix_circle = self.components.text_or_image_update(self.fix_circle, 'fix_circle.started', self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.intro_planet_components = self.components.check_if_components_finished(self.intro_planet_components, self)
            if self.continueRoutine: self.win.flip()
        
        #end
        self.intro_planet_components = self.components.hide_components(self.intro_planet_components)
        self.proceed_7 = self.components.save_key_response(self.proceed_7, 'proceed_7.keys', 'proceed_7.rt', self)
        self.thisExp.nextEntry()
        self.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def intro_radar(self):
        '''
        Prepares, runs and ends radar introduction routine.
        '''
        
        #prepare
        if self.lang_keys.keys == 'e':
            instr='Here is a picture of the radar.\n\nPress SPACEBAR to proceed.'
        else:
            instr='Hier ist ein Bild des Radars.\n\nDrücke die LEERTASTE, um fortzufahren.'
        self.text_9.setText(instr)
        self.proceed_5.keys = []
        self.proceed_5.rt = []
        self._proceed_5_allKeys = []
        self.intro_radar_components = [self.space_bg_5, self.radar_4, self.text_9, self.proceed_5]
        self.intro_radar_components = self.prepare_routine(self.intro_radar_components)

        #run
        while self.continueRoutine:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1
            self.space_bg_5 = self.components.text_or_image_update(self.space_bg_5, 'space_bg_5.started', self)
            self.radar_4 = self.components.text_or_image_update(self.radar_4, 'radar_4.started', self)
            self.text_9 = self.components.text_or_image_update(self.text_9, 'text_9.started', self)
            self.waitOnFlip = False
            self.proceed_5, self._proceed_5_allKeys = self.components.keys_update(self.proceed_5, self._proceed_5_allKeys, 'proceed_5.started', self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.intro_radar_components = self.components.check_if_components_finished(self.intro_radar_components, self)
            if self.continueRoutine: self.win.flip()
        
        #end
        self.intro_radar_components = self.components.hide_components(self.intro_radar_components)
        self.proceed_5 = self.components.save_key_response(self.proceed_5, 'proceed_5.keys', 'proceed_5.rt', self)
        self.thisExp.nextEntry()
        self.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def intro_signal(self):
        '''
        Prepares, runs and ends signal introduction routine.
        '''
        
        #prepare
        if self.lang_keys.keys == 'e':
            instr='On the radar, you will be seeing a signal from space. The signal strength will be higher on either the left or the right side.\n\nBased on this, you will advise the astronauts in the space shuttle which planet to fly to. Press SPACEBAR to if you have understood this and proceed.\n'
        else:
            instr='Auf dem Radar siehst du ein Signal aus dem Weltraum. Die Signalstärke wird entweder auf der linken oder auf der rechten Seite höher sein.\n\nAuf dieser Grundlage wirst du die Astronaut:innen im Raumschiff beraten, zu welchem Planeten sie fliegen sollen.\nDrücke die LEERTASTE, wenn du dies verstanden hast und fahre fort.\n'
        self.text_10.setText(instr)
        self.proceed_6.keys = []
        self.proceed_6.rt = []
        self._proceed_6_allKeys = []
        self.intro_signal_components = [self.space_bg_6, self.radar_5, self.left_patch_4, self.right_patch_4, self.text_10, self.proceed_6, self.fix_circle_4]
        self.intro_signal_components = self.prepare_routine(self.intro_signal_components)

        #run
        while self.continueRoutine:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1
            self.space_bg_6 = self.components.text_or_image_update(self.space_bg_6, 'space_bg_6.started', self)
            self.radar_5 = self.components.text_or_image_update(self.radar_5, 'radar_5.started', self)
            self.left_patch_4 = self.components.text_or_image_update(self.left_patch_4, 'left_patch_4.started', self)
            self.right_patch_4 = self.components.text_or_image_update(self.right_patch_4, 'right_patch_4.started', self)
            self.text_10 = self.components.text_or_image_update(self.text_10, 'text_10.started', self)
            self.waitOnFlip = False
            self.proceed_6, self._proceed_6_allKeys = self.components.keys_update(self.proceed_6, self._proceed_6_allKeys, 'proceed_6.started', self)
            self.fix_circle_4 = self.components.text_or_image_update(self.fix_circle_4, 'fix_circle_4.started', self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.intro_signal_components = self.components.check_if_components_finished(self.intro_signal_components, self)
            if self.continueRoutine: self.win.flip()
        
        #end
        self.intro_signal_components = self.components.hide_components(self.intro_signal_components)
        self.proceed_6 = self.components.save_key_response(self.proceed_6, 'proceed_6.keys', 'proceed_6.rt', self)
        self.thisExp.nextEntry()
        self.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def intro_crystal(self):
        '''
        Prepares, runs and ends crystal introduction routines.
        '''
        
        #prepare
        if self.lang_keys.keys == 'e':
            instr='On the radar, if the signal has higher contrast on your left, it indicates that space crystals can be found on the left planet. For instance, in the image above, the signal strength is higher on the left and hence, it signals the presence of space crystals on the left planet (indicated by the white arrow).\n\nPress SPACEBAR to if you have understood this and want to proceed.\n\n'
        else:
            instr='Wenn das Signal auf dem Radar auf der linken Seite einen höheren Kontrast aufweist, ist dies ein Hinweis, dass Weltraumkristalle auf dem linken Planeten zu finden sind. In der obigen Abbildung ist die Signalstärke auf der linken Seite höher und signalisiert somit, dass die Weltraumkristalle auf dem linken Planeten sind (angezeigt durch den weißen Pfeil).\n\nDrücke die LEERTASTE, wenn du dies verstanden hast und fortfahren möchtest.'
        self.text_12.setText(instr)
        self.proceed_8.keys = []
        self.proceed_8.rt = []
        self._proceed_8_allKeys = []
        self.planet_right_4.setPos((0.4, 0.4))
        self.intro_crystal_components = [self.space_bg_7, self.radar_6, self.left_patch_5, self.right_patch_5, self.text_12, self.proceed_8, self.fix_circle_5, self.planet_right_4, self.planet_left_4, self.arrow_2]
        self.intro_crystal_components = self.prepare_routine(self.intro_crystal_components)
        
        #run
        while self.continueRoutine:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1
            self.space_bg_7 = self.components.text_or_image_update(self.space_bg_7, 'space_bg_7.started', self)
            self.radar_6 = self.components.text_or_image_update(self.radar_6, 'radar_6.started', self)
            self.left_patch_5 = self.components.text_or_image_update(self.left_patch_5, 'left_patch_5.started', self)
            self.right_patch_5 = self.components.text_or_image_update(self.right_patch_5, 'right_patch_5.started', self)
            self.text_12 = self.components.text_or_image_update(self.text_12, 'text_12.started', self)
            self.waitOnFlip = False
            self.proceed_8, self._proceed_8_allKeys = self.components.keys_update(self.proceed_8, self._proceed_8_allKeys, 'proceed_8.started', self)
            self.fix_circle_5 = self.components.text_or_image_update(self.fix_circle_5, 'fix_circle_5.started', self)
            self.planet_right_4 = self.components.text_or_image_update(self.planet_right_4, 'planet_right_4.started', self)
            self.planet_left_4 = self.components.text_or_image_update(self.planet_left_4, 'planet_left_4.started', self)
            self.arrow_2 = self.components.text_or_image_update(self.arrow_2, 'arrow_2.started', self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.intro_crystal_components = self.components.check_if_components_finished(self.intro_crystal_components, self)
            if self.continueRoutine: self.win.flip()
        
        #end
        self.intro_crystal_components = self.components.hide_components(self.intro_crystal_components)
        self.proceed_8 = self.components.save_key_response(self.proceed_8, 'proceed_8.keys', 'proceed_8.rt', self)
        self.thisExp.nextEntry()
        self.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def intro_crystal2(self):
        '''
        Prepares, runs and ends second crystal introduction routine (inverted planets).
        '''
        
        #prepare
        if self.lang_keys.keys == 'e':
            instr='On the radar, if the signal has higher contrast on your right, it indicates that space crystals can be found on the right planet. For instance, in the image above, the signal strength is higher on the right and hence, it signals the presence of space crystals on the right planet (indicated by the white arrow).\n\nPress SPACEBAR to if you have understood this and proceed.'
        else:
            instr='Wenn das Signal auf dem Radar auf der rechten Seite einen höheren Kontrast aufweist, ist dies ein Hinweis, dass Weltraumkristalle auf dem rechten Planeten zu finden sind. In der obigen Abbildung zum Beispiel ist die Signalstärke auf der rechten Seite höher und signalisiert damit, dass Weltraumkristalle auf dem rechten Planeten sind (gekennzeichnet durch den weißen Pfeil).\n\nDrücke die LEERTASTE, wenn du dies verstanden hast und fahre fort.'
        self.text_13.setText(instr)
        self.proceed_9.keys = []
        self.proceed_9.rt = []
        self._proceed_9_allKeys = []
        self.planet_right_5.setPos((0.4, 0.4))
        self.intro_crystal2_components = [self.space_bg_8, self.radar_7, self.left_patch_6, self.right_patch_6, self.text_13, self.proceed_9, self.fix_circle_6, self.arrow_3, self.planet_right_5, self.planet_left_5]
        self.intro_crystal2_components = self.prepare_routine(self.intro_crystal2_components)
        
        #run
        while self.continueRoutine:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1
            self.space_bg_8 = self.components.text_or_image_update(self.space_bg_8, 'space_bg_8.started', self)
            self.radar_7 = self.components.text_or_image_update(self.radar_7, 'radar_7.started', self)
            self.left_patch_6 = self.components.text_or_image_update(self.left_patch_6, 'left_patch_6.started', self)
            self.right_patch_6 = self.components.text_or_image_update(self.right_patch_6, 'right_patch_6.started', self)
            self.text_13 = self.components.text_or_image_update(self.text_13, 'text_13.started', self)
            self.waitOnFlip = False
            self.proceed_9, self._proceed_9_allKeys = self.components.keys_update(self.proceed_9, self._proceed_9_allKeys, 'proceed_9.started', self)
            self.fix_circle_6 = self.components.text_or_image_update(self.fix_circle_6, 'fix_circle_6.started', self)
            self.arrow_3 = self.components.text_or_image_update(self.arrow_3, 'arrow_3.started', self)
            self.planet_right_5 = self.components.text_or_image_update(self.planet_right_5, 'planet_right_5.started', self)
            self.planet_left_5 = self.components.text_or_image_update(self.planet_left_5, 'planet_left_5.started', self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.intro_crystal2_components = self.components.check_if_components_finished(self.intro_crystal2_components, self)
            if self.continueRoutine: self.win.flip()
        
        #end
        self.intro_crystal2_components = self.components.hide_components(self.intro_crystal2_components)
        self.proceed_9 = self.components.save_key_response(self.proceed_9, 'proceed_9.keys', 'proceed_9.rt', self)
        self.thisExp.nextEntry()
        self.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def training_block(self):
        '''
        Prepares, runs and ends routine informing the participant of the upcoming training task.
        '''
        
        #prepare
        if self.lang_keys.keys == 'e':
            instr='You will now complete a signal training task. You will be presented with a signal on the radar and you have to determine if the space crystals are on the right or the left planet. \n\nPress the LEFT arrow if the signal indicates the presence of space crystals on the left planet.\nPress the RIGHT arrow if the signal indicates the presence of space crystals on the right planet.\n\nPlease note that there is a limited time duration within which you need to respond using the left/right arrow. Thus, we recommend that you respond as fast as possible.\n\nPress SPACEBAR to proceed.'
        else:
            instr='Jetzt kommt eine Übungsaufgabe. Du wirst Radarsignale sehen und sollst angeben, ob die Kristalle auf dem linken oder rechten Planeten vorkommen.\n\nDrücke den LINKEN Pfeil, wenn das Signal ein Hinweis auf Weltraumkristalle auf dem linken Planeten ist.\n\nDrücke den RECHTEN Pfeil, wenn das Signal ein Hinweis auf Weltraumkristalle auf dem rechten Planeten ist.\n\nBitte beachte, dass die Zeitspanne, in der du mit dem Pfeil nach links/rechts antworten musst, begrenzt ist. Wir empfehlen daher, dass du so schnell wie möglich antwortest.\n Drücke die LEERTASTE, um fortzufahren.'
        self.text_5.setText(instr)
        self.proceed_2.keys = []
        self.proceed_2.rt = []
        self._proceed_2_allKeys = []
        self.training_block_components = [self.space_bg, self.proceed_2, self.text_5]
        self.training_block_components = self.prepare_routine(self.training_block_components)
        
        #run
        while self.continueRoutine:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1
            self.space_bg = self.components.text_or_image_update(self.space_bg, 'space_bg.started', self)
            self.waitOnFlip = False
            self.proceed_2, self._proceed_2_allKeys = self.components.keys_update(self.proceed_2, self._proceed_2_allKeys, 'proceed_2.started', self)
            self.text_5 = self.components.text_or_image_update(self.text_5, 'text_5.started', self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]):core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.training_block_components = self.components.check_if_components_finished(self.training_block_components, self)
            if self.continueRoutine: self.win.flip()
        
        #end
        self.training_block_components = self.components.hide_components(self.training_block_components)
        self.proceed_2 = self.components.save_key_response(self.proceed_2, 'proceed_2.keys', 'proceed_2.rt', self)
        self.thisExp.nextEntry()
        self.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def space(self):
        '''
        Prepares, runs and ends signal training task where stimulus is shown.
        '''
        
        #prepare
        self.left_patch_3.setContrast(self.thisTraining['con_left']) # self.thisTrial['con_left'] # self.thisTraining['con_left'] # old: con_left
        self.right_patch_3.setContrast(self.thisTraining['con_right']) # same as above
        self.choice_training.keys = []
        self.choice_training.rt = []
        self._choice_training_allKeys = []
        self.space_components = [self.space_image, self.radar, self.left_patch_3, self.fix_circle_3, self.right_patch_3, self.choice_training]
        self.space_components = self.prepare_routine(self.space_components)

        #run
        while self.continueRoutine and self.routineTimer.getTime() < 1.0:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1
            self.space_image = self.components.text_or_image_update(self.space_image, 'space_image.started', self)
            self.space_image = self.components.text_or_image_update_2(self.space_image, 'space_image.stopped', 1, self)
            self.radar = self.components.text_or_image_update(self.radar, 'radar.started', self)
            self.radar = self.components.text_or_image_update_2(self.radar, 'radar.stopped', 1, self)
            self.left_patch_3 = self.components.text_or_image_update(self.left_patch_3, 'left_patch_3.started', self)
            self.left_patch_3 = self.components.text_or_image_update_2(self.left_patch_3, 'left_patch_3.stopped', 1, self)
            self.fix_circle_3 = self.components.text_or_image_update(self.fix_circle_3, 'fix_circle_3.started', self)
            self.fix_circle_3 = self.components.text_or_image_update_2(self.fix_circle_3, 'fix_circle_3.stopped', 1, self)
            self.right_patch_3 = self.components.text_or_image_update(self.right_patch_3, 'right_patch_3.started', self)
            self.right_patch_3 = self.components.text_or_image_update_2(self.right_patch_3, 'right_patch_3.stopped', 1, self)
            # automate this later
            if self.choice_training.status == NOT_STARTED and self.t >= 0.0-self.frameTolerance:
                self.choice_training.frameNStart = self.frameN
                self.choice_training.tStart = self.t
                self.choice_training.tStartRefresh = self.tThisFlipGlobal
                self.win.timeOnFlip(self.choice_training, 'tStartRefresh')
                self.thisExp.addData('choice_training.started', self.t)
                self.choice_training.status = STARTED
                self.choice_training.clock.reset()
                self.choice_training.clearEvents(eventType='keyboard')
            if self.choice_training.status == STARTED:
                if self.tThisFlipGlobal > self.choice_training.tStartRefresh + 1-self.frameTolerance:
                    self.choice_training.tStop = self.t
                    self.choice_training.frameNStop = self.frameN
                    self.thisExp.addData('choice_training.stopped', self.t)
                    self.choice_training.status = FINISHED
            if self.choice_training.status == STARTED: # careful
                self.theseKeys = self.choice_training.getKeys(keyList=['left','right'], waitRelease=False)
                self._choice_training_allKeys.extend(self.theseKeys)
                if len(self._choice_training_allKeys):
                    self.choice_training.keys = self._choice_training_allKeys[-1].name
                    self.choice_training.rt = self._choice_training_allKeys[-1].rt
                    if (self.choice_training.keys == str(self.thisTraining['corr_resp'])) or (self.choice_training.keys == self.thisTraining['corr_resp']): # old: corr_resp
                        self.choice_training.corr = 1
                    else:
                        self.choice_training.corr = 0
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            for thisComponent in self.space_components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    self.continueRoutine = True
                    break
            if self.continueRoutine: self.win.flip()
        
        #end
        self.space_components = self.components.hide_components(self.space_components)        
        if self.choice_training.keys in ['', [], None]:
            self.choice_training.keys = None
            if str(self.thisTraining['corr_resp']).lower() == 'none': # old: corr_resp
               self.choice_training.corr = 1;
            else:
               self.choice_training.corr = 0;
        self.training.addData('choice_training.keys',self.choice_training.keys)
        self.training.addData('choice_training.corr', self.choice_training.corr)
        if self.choice_training.keys != None:
            self.training.addData('choice_training.rt', self.choice_training.rt)
        if self.routineForceEnded:
            self.routineTimer.reset()
        else:
            self.routineTimer.addTime(-1.000000)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def feedback(self):
        '''
        Prepares, runs and ends signal training feedback routine (correct/incorrect/time out)
        '''
        
        #prepare
        if self.choice_training.keys == self.thisTraining['corr_resp']: # old: corr_resp
            if self.lang_keys.keys == 'e':
                msg='Correct'
            else:
                msg='Richtig'
        elif self.choice_training.keys != self.thisTraining['corr_resp']: # old: corr_resp
            if not self.choice_training.keys:
                if self.lang_keys.keys == 'e':
                    msg='You missed the trial.'
                else:
                    msg='Du hast den Versuch verpasst.'
            else:
                if self.lang_keys.keys == 'e':
                    msg='Incorrect'
                else:
                    msg='Falsch'
        self.fb_msg.setText(msg)
        self.feedback_components = [self.space_image_3, self.fb_msg]
        self.feedback_components = self.prepare_routine(self.feedback_components)
        
        #run
        while self.continueRoutine and self.routineTimer.getTime() < 1.0:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1
            self.space_image_3 = self.components.text_or_image_update(self.space_image_3, 'space_image_3.started', self)
            self.space_image_3 = self.components.text_or_image_update_2(self.space_image_3, 'space_image_3.stopped', 1, self)
            self.fb_msg = self.components.text_or_image_update(self.fb_msg, 'fb_msg.started', self)
            self.fb_msg = self.components.text_or_image_update_2(self.fb_msg, 'fb_msg.stopped', 1, self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: routineForceEnded = True; break
            self.continueRoutine = False
            for thisComponent in self.feedback_components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    self.continueRoutine = True
                    break 
            if self.continueRoutine: self.win.flip()
        
        #end
        self.feedback_components = self.components.hide_components(self.feedback_components)
        if self.routineForceEnded:
            self.routineTimer.reset()
        else:
            self.routineTimer.addTime(-1.000000)
        self.thisExp.nextEntry()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def intro_pu(self):
        '''
        Prepares, runs and ends warning routine ("signal strength is sometimes lower")
        '''
        
        #prepare
        if self.thisTraining['condition'] == 3: # old: condition
            if self.lang_keys.keys == 'e':
                instr = 'Please note that sometimes it might be difficult to tell on which side the signal strength is higher. This makes the interpretation of the signal more difficult. Thus, now we do another set of training trials where it is more difficult to tell if the signal strength is higher on the left or right. Press SPACEBAR to proceed.'
            else:
                instr='Bitte beachte, dass es manchmal schwierig sein kann, zu erkennen, auf welcher Seite die Signalstärke höher ist. Dies erschwert die Interpretation des Signals. Daher kommt jetzt eine weitere Übung, bei der es schwieriger zu erkennen ist, ob die Signalstärke links oder rechts höher ist. Drücke die LEERTASTE, um fortzufahren.'
        else:
            if self.lang_keys.keys == 'e':
                instr = 'Press SPACEBAR to proceed.'
            else:
                instr='Drücke die LEERTASTE, um fortzufahren.'
        self.proceed_3.keys = []
        self.proceed_3.rt = []
        self._proceed_3_allKeys = []
        self.text_7.setText(instr)
        self.intro_pu_components = [self.space_bg_10, self.proceed_3, self.text_7]
        self.intro_pu_components = self.prepare_routine(self.intro_pu_components)

        #run
        while self.continueRoutine:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1
            self.space_bg_10 = self.components.text_or_image_update(self.space_bg_10, 'space_bg_10.started', self)
            self.waitOnFlip = False
            self.proceed_3, self._proceed_3_allKeys = self.components.keys_update(self.proceed_3, self._proceed_3_allKeys, 'proceed_3.started', self)
            self.text_7 = self.components.text_or_image_update(self.text_7, 'text_7.started', self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: routineForceEnded = True; break
            self.continueRoutine = False
            self.intro_pu_components = self.components.check_if_components_finished(self.intro_pu_components, self)
            if self.continueRoutine: self.win.flip()
        
        #end
        self.intro_pu_components = self.components.hide_components(self.intro_pu_components)
        #self.proceed_3 = self.save_key_response(self.proceed_3, 'proceed_3.keys', 'proceed_3.rt') # implement later 
        if self.proceed_3.keys in ['', [], None]:
            self.proceed_3.keys = None
        self.training_blocks.addData('proceed_3.keys',self.proceed_3.keys)
        if self.proceed_3.keys != None:
            self.training_blocks.addData('proceed_3.rt', self.proceed_3.rt)
        self.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def training_task(self):
        self.welcome()
        self.intro_planet()
        self.intro_radar()
        self.intro_signal()
        self.intro_crystal()
        self.intro_crystal2()
        self.training_block()
        self.handler.training_blocks_handler(self)
        for self.thisTraining_block in self.training_blocks:
            self.currentLoop = self.training_blocks
            self.thisTraining_block = self.handler.create_variables(self.thisTraining_block)
            self.handler.training_handler(self)
            for self.thisTraining in self.training:
                self.currentLoop = self.training
                self.thisTraining = self.handler.create_variables(self.thisTraining)
                self.space()
                self.feedback()
            self.intro_pu()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def practice_task(self):
        prob(self)
        prob1(self)
        space_slider(self)
        space_slider2(self)
        slider_example(self)
        slider_example1(self)
        ghost_marker(self)
        slider_accuracy(self)
        demo(self)
        incong_vid(self)
        demo_incong(self)
        choice(self)
        reward(self)
        no_reward(self)
        congruence_caution(self)
        points(self)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def prac_block(self):                                                    # executes practice_block routine
        
        # prepare routine
        if self.lang_keys.keys == 'e':
            self.text_20.setText('New block of the main task is coming up. \n Press SPACEBAR to proceed.')
        else:
            self.text_20.setText('Ein neuer Block der Hauptaufgabe wird angezeigt. Drücke die LEERTASTE, um fortzufahren.')
        self.proceed_17.keys = []
        self.proceed_17.rt = []
        self._proceed_17_allKeys = []
        self.prac_block_components = [self.space_image_7, self.proceed_17, self.text_20]
        self.prac_block_components = self.prepare_routine(self.prac_block_components)
       
        # run routine
        while self.continueRoutine:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1
            self.space_image_7 = self.components.text_or_image_update(self.space_image_7, 'space_image_7.started', self)
            self.waitOnFlip = False
            self.proceed_17, self._proceed_17_allKeys = self.components.keys_update(self.proceed_17, self._proceed_17_allKeys, 'proceed_17.started', self)
            self.text_20 = self.components.text_or_image_update(self.text_20, 'text_20.started', self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.prac_block_components = self.components.check_if_components_finished(self.prac_block_components, self)
            if self.continueRoutine: self.win.flip()
        
        # end routine
        self.prac_block_components = self.components.hide_components(self.prac_block_components)
        self.proceed_17 = self.components.save_key_response(self.proceed_17, 'proceed_17.keys', 'proceed_17.rt', self)
        self.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def primer_mu(self):                                                     # executes primer_mu routine
        
        # prepare routine
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
        self.primer_mu_components = self.prepare_routine(self.primer_mu_components)
        
        # run routine
        while self.continueRoutine:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1
            self.space_bg_12 = self.components.text_or_image_update(self.space_bg_12, 'space_bg_12.started', self)
            self.shuttle_5 = self.components.text_or_image_update(self.shuttle_5, 'shuttle_5.started', self)
            self.planet_right_6 = self.components.text_or_image_update(self.planet_right_6, 'planet_right_6.started', self)
            self.planet_left_6 = self.components.text_or_image_update(self.planet_left_6, 'planet_left_6.started', self)
            self.arrow_left_3 = self.components.text_or_image_update(self.arrow_left_3, 'arrow_left_3.started', self)
            self.mu_5 = self.components.text_or_image_update(self.mu_5, 'mu_5.started', self)
            self.text_21 = self.components.text_or_image_update(self.text_21, 'text_21.started', self)
            self.waitOnFlip = False
            self.key_resp_3, self._key_resp_3_allKeys = self.components.keys_update(self.key_resp_3, self._key_resp_3_allKeys, 'key_resp_3.started', self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.primer_mu_components = self.components.check_if_components_finished(self.primer_mu_components, self)
            if self.continueRoutine: self.win.flip()
        
        # end routine
        self.primer_mu_components = self.components.hide_components(self.primer_mu_components)
        self.primer.addData('mu_5.response', self.mu_5.getRating())
        self.primer.addData('mu_5.rt', self.mu_5.getRT())
        self.key_resp_3 = self.components.save_key_response(self.key_resp_3, 'key_resp_3.keys', 'key_resp_3.rt', self) # LATER DELETE self.key_resp_3 in the beginning -> no need to re-assign as it doesn't get used again
        self.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def fixation(self):
        #prepare
        self.fixation_components = [self.space_image_fixation, self.fixation_dot]
        self.fixation_components = self.prepare_routine(self.fixation_components)
        
        #run
        while self.continueRoutine and self.routineTimer.getTime() < 4.0:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1
            self.space_image_fixation = self.components.text_or_image_update(self.space_image_fixation, 'space_image_fixation.started', self)
            self.space_image_fixation = self.components.text_or_image_update_2(self.space_image_fixation, 'space_image_fixation.stopped', 1, self)
            self.fixation_dot = self.components.text_or_image_update(self.fixation_dot, 'fixation_dot.started', self)
            self.fixation_dot = self.components.text_or_image_update_2(self.fixation_dot, 'fixation_dot.stopped', 1, self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: routineForceEnded = True; break
            self.continueRoutine = False
            for thisComponent in self.fixation_components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    self.continueRoutine = True
                    break 
            if self.continueRoutine: self.win.flip()
        
        #end
        self.fixation_components = self.components.hide_components(self.fixation_components)
        if self.routineForceEnded:
            self.routineTimer.reset()
        else:
            self.routineTimer.addTime(-1.000000)
        self.thisExp.nextEntry()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def signal(self): # SPECIFICS!!!                                         # executes signal routine
        
        # prepare routine
        self.left_patch_7.setContrast(self.thisTrial['con_left'])
        self.right_patch_7.setContrast(self.thisTrial['con_right'])
        
        self.choice_main.keys = []
        self.choice_main.rt = []
        self._choice_main_allKeys = []
        
        self.signal_components = [self.space_image_8, self.radar_3, self.left_patch_7, self.fix_circle_7, self.right_patch_7, self.choice_main]
        self.signal_components = self.prepare_routine(self.signal_components)
        
        # run routine
        while self.continueRoutine and self.routineTimer.getTime() < 1.0:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1 
            self.space_image_8 = self.components.text_or_image_update(self.space_image_8, 'space_image_8.started', self)
            self.space_image_8 = self.components.text_or_image_update_2(self.space_image_8, 'space_image_8.stopped', 1, self)
            self.radar_3 = self.components.text_or_image_update(self.radar_3, 'radar_3.started', self)
            self.radar_3 = self.components.text_or_image_update_2(self.radar_3, 'radar_3.stopped', 1, self)
            self.left_patch_7 = self.components.text_or_image_update(self.left_patch_7, 'left_patch_7.started', self)
            self.left_patch_7 = self.components.text_or_image_update_2(self.left_patch_7, 'left_patch_7.stopped', 1, self)
            self.fix_circle_7 = self.components.text_or_image_update(self.fix_circle_7, 'fix_circle_7.started', self)
            self.fix_circle_7 = self.components.text_or_image_update_2(self.fix_circle_7, 'fix_circle_7.stopped', 1, self)
            self.right_patch_7 = self.components.text_or_image_update(self.right_patch_7, 'right_patch_7.started', self)
            self.right_patch_7 = self.components.text_or_image_update_2(self.right_patch_7, 'right_patch_7.stopped', 1, self)
            if self.block_num == 0 or self.block_num == 1:
                if self.choice_main.status == NOT_STARTED and self.t >= 0.0-self.frameTolerance:
                    self.choice_main.frameNStart = self.frameN
                    self.choice_main.tStart = self.t
                    self.choice_main.tStartRefresh = self.tThisFlipGlobal
                    self.win.timeOnFlip(self.choice_main, 'tStartRefresh')
                    self.thisExp.addData('choice_main.started', self.t)
                    self.choice_main.status = STARTED
                    self.choice_main.clock.reset()
                    self.choice_main.clearEvents(eventType='keyboard')
                if self.choice_main.status == STARTED:
                    if self.tThisFlipGlobal > self.choice_main.tStartRefresh + 1-self.frameTolerance:
                        self.choice_main.tStop = self.t
                        self.choice_main.frameNStop = self.frameN
                        self.thisExp.addData('choice_main.stopped', self.t)
                        self.choice_main.status = FINISHED
                if self.choice_main.status == STARTED: # careful
                    self.theseKeys = self.choice_main.getKeys(keyList=['left','right'], waitRelease=False)
                    self._choice_main_allKeys.extend(self.theseKeys)
                    if len(self._choice_main_allKeys):
                        self.choice_main.keys = self._choice_main_allKeys[-1].name
                        self.choice_main.rt = self._choice_main_allKeys[-1].rt
#                        if (self.choice_main.keys == str(self.thisTraining['corr_resp'])) or (self.choice_main.keys == self.thisTraining['corr_resp']): # old: corr_resp
                        if (self.choice_main.keys == 'left' and int(self.thisTrial['state']) == 1) or (self.choice_main.keys == 'right' and int(self.thisTrial['state']) == 0): # old: corr_resp
                            self.choice_main.corr = 1
                        else:
                            self.choice_main.corr = 0
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.signal_components = self.components.check_if_components_finished(self.signal_components, self)
            if self.continueRoutine: self.win.flip()
        
        #self.end_routine(signal_components)
        self.signal_components = self.components.hide_components(self.signal_components)
        if self.block_num == 0 or self.block_num == 1:
            if self.routineForceEnded: self.routineTimer.reset()
            else: self.routineTimer.addTime(-1.000000)
        else:
            if self.choice_main.keys in ['', [], None]:
                self.choice_main.keys = None
                if str(self.thisTrial['state']).lower() == 'none': # old: corr_resp
                    self.choice_main.corr = 1;
                else:
                    self.choice_main.corr = 0;
            self.trials.addData('choice_main.keys',self.choice_main.keys)
            self.trials.addData('choice_main.corr', self.choice_main.corr)
            if self.choice_main.keys != None:
                self.trials.addData('choice_main.rt', self.choice_main.rt)
            if self.routineForceEnded:
                self.routineTimer.reset()
            else:
                self.routineTimer.addTime(-1.000000)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def feedback_main(self):
        #prepare
        if self.choice_main.keys == 'left' and int(self.thisTrial['state']) == 1: # old: corr_resp
            if self.lang_keys.keys == 'e':
                msg='Correct'
            else:
                msg='Richtig'
#        elif self.choice_main.keys != self.thisTraining['corr_resp']: # old: corr_resp
        else: # old: corr_resp
            if not self.choice_main.keys:
                if self.lang_keys.keys == 'e':
                    msg='You missed the trial.'
                else:
                    msg='Du hast den Versuch verpasst.'
            else:
                if self.lang_keys.keys == 'e':
                    msg='Incorrect'
                else:
                    msg='Falsch'
        self.fb_msg_main.setText(msg)
        self.feedback_main_components = [self.space_image_3_main, self.fb_msg_main]
        self.feedback_main_components = self.prepare_routine(self.feedback_main_components)
        
        #run
        while self.continueRoutine and self.routineTimer.getTime() < 1.0:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1
            self.space_image_3_main = self.components.text_or_image_update(self.space_image_3_main, 'space_image_3_main.started', self)
            self.space_image_3_main = self.components.text_or_image_update_2(self.space_image_3_main, 'space_image_3_main.stopped', 1, self)
            self.fb_msg_main = self.components.text_or_image_update(self.fb_msg_main, 'fb_msg_main.started', self)
            self.fb_msg_main = self.components.text_or_image_update_2(self.fb_msg_main, 'fb_msg_main.stopped', 1, self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: routineForceEnded = True; break
            self.continueRoutine = False
            for thisComponent in self.feedback_main_components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    self.continueRoutine = True
                    break 
            if self.continueRoutine: self.win.flip()
        
        #end
        self.feedback_main_components = self.components.hide_components(self.feedback_main_components)
        if self.routineForceEnded:
            self.routineTimer.reset()
        else:
            self.routineTimer.addTime(-1.000000)
        self.thisExp.nextEntry()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def slider(self): # SPECIFICS!!!
        print("Here?")
        # prepare routine
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
        print("1")
        self.text_22.setText(ques_word)
        self.reported_mu.reset()
        print("2")
        self.planet_right_7.setPos((0.4, 0.4))
        self.planet_right_7.setImage(self.right_planet)
        self.planet_left_7.setImage(self.left_planet)
        self.arrow_left_4.setPos((pos,0.17))
        self.arrow_left_4.setOri(0.0)
        self.arrow_left_4.setImage(arrow)
        self.mu_ghost.marker.opacity = 0.7
        self.mu_ghost.depth = -1.0
        self.slider_3_components = [self.space_bg_13, self.text_22, self.mu_ghost, self.reported_mu, self.shuttle_3, self.planet_right_7, self.planet_left_7, self.arrow_left_4]
        print("3")
        self.slider_3_components = self.prepare_routine(self.slider_3_components)
        print("4")
        
        # run routine
        while self.continueRoutine and self.routineTimer.getTime() < 7.5:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1
            print("5")
            self.space_bg_13 = self.components.text_or_image_update(self.space_bg_13, 'space_bg_13.started', self)
            self.space_bg_13 = self.components.text_or_image_update_2(self.space_bg_13, 'space_bg_13.stopped', 7.5, self)
            self.text_22 = self.components.text_or_image_update(self.text_22, 'text_22.started', self)
            self.text_22 = self.components.text_or_image_update_2(self.text_22, 'text_22.stopped', 7.5, self)
            print("6")
            #self.reported_mu = self.text_or_image_update(self.reported_mu, 'reported_mu.started') # FIX THIS TO MAKE IT WORK
            if self.reported_mu.status == NOT_STARTED and self.tThisFlip >= 1.5-self.frameTolerance: # DELETE THIS PART WHEN LINE ABOVE IS FIXED
                self.reported_mu.frameNStart = self.frameN
                self.reported_mu.tStart = self.t
                self.reported_mu.tStartRefresh = self.tThisFlipGlobal
                self.win.timeOnFlip(self.reported_mu, 'tStartRefresh')
                self.thisExp.timestampOnFlip(self.win, 'reported_mu.started')
                self.reported_mu.setAutoDraw(True)
                self.mu_ghost.setAutoDraw(True)
                
            if self.reported_mu.status == STARTED: # ***
                if self.tThisFlipGlobal > self.reported_mu.tStartRefresh + 6-self.frameTolerance:
                    self.reported_mu.tStop = self.t
                    self.reported_mu.frameNStop = self.frameN
                    self.thisExp.timestampOnFlip(self.win, 'reported_mu.stopped')
                    self.mu_ghost.setAutoDraw(False)                             # this too
                    self.reported_mu.setAutoDraw(False)
            if self.reported_mu.getRating() is not None and self.reported_mu.status == STARTED: self.continueRoutine = False
            self.shuttle_3 = self.components.text_or_image_update(self.shuttle_3, 'shuttle_3.started', self)
            self.shuttle_3 = self.components.text_or_image_update_2(self.shuttle_3, 'shuttle_3.stopped', 7.5, self)
            self.planet_right_7 = self.components.text_or_image_update(self.planet_right_7, 'planet_right_7.started', self)
            self.planet_right_7 = self.components.text_or_image_update_2(self.planet_right_7, 'planet_right_7.stopped', 7.5, self)
            self.planet_left_7 = self.components.text_or_image_update(self.planet_left_7, 'planet_left_7.started', self)
            self.planet_left_7 = self.components.text_or_image_update_2(self.planet_left_7, 'planet_left_7.stopped', 7.5, self)
            self.arrow_left_4 = self.components.text_or_image_update(self.arrow_left_4, 'arrow_left_4.started', self)
            self.arrow_left_4 = self.components.text_or_image_update_2(self.arrow_left_4, 'arrow_left_4.stopped', 7.5, self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.slider_3_components = self.components.check_if_components_finished(self.slider_3_components, self)
            if self.continueRoutine: self.win.flip()
        
        #self.end_routine(slider_components)
        self.slider_3_components = self.components.hide_components(self.slider_3_components)
        if self.reported_mu.getRating() is not None: mu = self.reported_mu.getRating();
        self.trials.addData('reported_mu.response', self.reported_mu.getRating())
        self.trials.addData('reported_mu.rt', self.reported_mu.getRT())
        if self.reported_mu.getRating() is not None: self.mu_ghost.markerPos = mu # check
        if self.reported_mu.getRating() is not None: # this is exeprimental, may cause problems
            self.mu = mu
        #self.mu = mu
        if self.routineForceEnded:
            self.routineTimer.reset()
        else:
            self.routineTimer.addTime(-7.500000)
        self.thisExp.nextEntry()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def prechoice_text(self):
        
        # prepare routine
        if self.lang_keys.keys == 'e':
            instr='Before you provide advise to the spaceship, you will be shown your reported probability on the latest trial.\n\nPlease use the analysis of the radar signals that you conducted throughout the block, to inform the spaceship.\n\nPress SPACEBAR to proceed.'
        else:
            instr='Bevor du den Astronaut:innen deinen Ratschlag erteilst, wird dir deine gemeldete Wahrscheinlichkeit für den letzten Versuch angezeigt.\n\nBitte verwende die Analyse der Radarsignale, die du während des gesamten Blocks durchgeführt hast, um das Raumschiff zu informieren.\n\nDrücke die LEERTASTE, um fortzufahren.'
        self.text_23.setText(instr)
        self.key_resp_4.keys = []
        self.key_resp_4.rt = []
        self._key_resp_4_allKeys = []
        self.prechoice_text_components = [self.space_bg_14, self.text_23, self.key_resp_4]
        self.prechoice_text_components = self.prepare_routine(self.prechoice_text_components)
        
        #self.run_routine(prechoice_text_components)
        while self.continueRoutine:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1                        
            self.space_bg_14 = self.components.text_or_image_update(self.space_bg_14, 'space_bg_14.started', self)
            self.text_23 = self.components.text_or_image_update(self.text_23, 'text_23.started', self)
            self.waitOnFlip = False
            self.key_resp_4, self._key_resp_4_allKeys = self.components.keys_update(self.key_resp_4, self._key_resp_4_allKeys, 'key_resp_4.started', self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.prechoice_text_components = self.components.check_if_components_finished(self.prechoice_text_components, self)
            if self.continueRoutine: self.win.flip()
        
        #self.end_routine(prechoice_text_components)
        self.prechoice_text_components = self.components.hide_components(self.prechoice_text_components)
        self.key_resp_4 = self.components.save_key_response(self.key_resp_4, 'key_resp_4.keys', 'key_resp_4.rt', self)
        self.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def last_mu(self): # SPECIFICS!
        
        # prepare routine
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
        self.last_mu_components = self.prepare_routine(self.last_mu_components)
        
        #self.run_routine(last_mu_components)
        while self.continueRoutine:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1
            self.space_bg_15 = self.components.text_or_image_update(self.space_bg_15, 'space_bg_15.started', self)
            self.mu_7.markerPos = self.mu;
            self.shuttle_6 = self.components.text_or_image_update(self.shuttle_6, 'shuttle_6.started', self)
            self.planet_right_8 = self.components.text_or_image_update(self.planet_right_8, 'planet_right_8.started', self)
            self.planet_left_8 = self.components.text_or_image_update(self.planet_left_8, 'planet_left_8.started', self)
            self.arrow_left_5 = self.components.text_or_image_update(self.arrow_left_5, 'arrow_left_5.started', self)
            self.mu_7 = self.components.text_or_image_update(self.mu_7, 'mu_7.started', self) # --> TEXT PART WASN'T THERE BEFORE
            self.text_24 = self.components.text_or_image_update(self.text_24, 'text_24.started', self)
            self.waitOnFlip = False
            self.key_resp_5, self._key_resp_5_allKeys = self.components.keys_update(self.key_resp_5, self._key_resp_5_allKeys, 'key_resp_5.started', self)
            self.text_31 = self.components.text_or_image_update(self.text_31, 'text_31.started', self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.last_mu_components = self.components.check_if_components_finished(self.last_mu_components, self)
            if self.continueRoutine: self.win.flip()
        
        #self.end_routine(last_mu_components)
        self.last_mu_components = self.components.hide_components(self.last_mu_components)
        self.last.addData('mu_7.response', self.mu_7.getRating())
        self.last.addData('mu_7.rt', self.mu_7.getRT())
        if self.reported_mu.getRating() is not None: self.mu_ghost.markerPos = self.mu
        self.key_resp_5 = self.components.save_key_response(self.key_resp_5, 'key_resp_5.keys', 'key_resp_5.rt', self)
        self.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def block_choice(self): # SPECIFICS
        
        # prepare routine
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
        self.block_choice_components = self.prepare_routine(self.block_choice_components)
        
        #self.run_routine(block_choice_components)
        while self.continueRoutine:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1
            self.space_bg_16 = self.components.text_or_image_update(self.space_bg_16, 'space_bg_16.started', self)
            self.shuttle_7 = self.components.text_or_image_update(self.shuttle_7, 'shuttle_7.started', self)
            self.planet_right_9 = self.components.text_or_image_update(self.planet_right_9, 'planet_right_9.started', self)
            self.planet_left_9 = self.components.text_or_image_update(self.planet_left_9, 'planet_left_9.started', self)
            self.text_25 = self.components.text_or_image_update(self.text_25, 'text_25.started', self)
            self.question = self.components.text_or_image_update(self.question, 'question.started', self)
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
            self.block_choice_components = self.components.check_if_components_finished(self.block_choice_components, self)
            if self.continueRoutine: self.win.flip()
        
        # end routine
        self.block_choice_components = self.components.hide_components(self.block_choice_components)
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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def block_reward(self):
        
        # prepare routine
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
        self.block_rew_components = self.prepare_routine(self.block_rew_components)
        
        #self.run_routine(block_reward_components)
        while self.continueRoutine:
            self.timing.get_current_time(self.routineTimer, self)
            self.frameN = self.frameN + 1
            self.space_bg_17 = self.components.text_or_image_update(self.space_bg_17, 'space_bg_17.started', self)
            self.waitOnFlip = False
            self.proceed_18, self._proceed_18_allKeys = self.components.keys_update(self.proceed_18, self._proceed_18_allKeys, 'proceed_18.started', self)
            self.text_26 = self.components.text_or_image_update(self.text_26, 'text_26.started', self)
            self.planet = self.components.text_or_image_update(self.planet, 'planet.started', self)
            self.shuttle_8 = self.components.text_or_image_update(self.shuttle_8, 'shuttle_8.started', self)
            if self.crystal.status == STARTED:
                self.crystal.setOri(1,'+')
                self.crystal.draw()
            self.crystal = self.components.text_or_image_update(self.crystal, 'crystal.started', self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.block_rew_components = self.components.check_if_components_finished(self.block_rew_components, self)
            if self.continueRoutine: self.win.flip()
        
        
        #self.end_routine(block_reward_components)
        self.block_rew_components = self.components.hide_components(self.block_rew_components)
        self.proceed_18 = self.components.save_key_response(self.proceed_18, 'proceed_18.keys', 'proceed_18.rt', self)
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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def block_completed(self):
        
        # prepare routine
        self.proceed_19.keys = []
        self.proceed_19.rt = []
        self._proceed_19_allKeys = []
        self.text_27.setPos((0, 0))
        self.text_27.setText(self.block_str)
        self.block_completed_components = [self.space_bg_18, self.proceed_19, self.text_27]
        self.block_completed_components = self.prepare_routine(self.block_completed_components)
        
        #self.run_routine(block_completed_components)
        while self.continueRoutine:
            self.t = self.routineTimer.getTime()
            self.tThisFlip = self.win.getFutureFlipTime(clock=self.routineTimer)
            self.tThisFlipGlobal = self.win.getFutureFlipTime(clock=None)
            self.frameN = self.frameN + 1
            self.space_bg_18 = self.components.text_or_image_update(self.space_bg_18, 'space_bg_18.started', self)
            self.waitOnFlip = False
            self.proceed_19, self._proceed_19_allKeys = self.components.keys_update(self.proceed_19, self._proceed_19_allKeys, 'proceed_19.started', self)
            self.text_27 = self.components.text_or_image_update(self.text_27, 'text_27.started', self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.block_completed_components = self.components.check_if_components_finished(self.block_completed_components, self)
            if self.continueRoutine: self.win.flip()
        
        # end routine
        self.block_completed_components = self.components.hide_components(self.block_completed_components)
        self.proceed_19 = self.components.save_key_response(self.proceed_19, 'proceed_19.keys', 'proceed_19.rt', self)
        self.routineTimer.reset()
        self.thisExp.nextEntry()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def task_score(self):
        
        # prepare routine
        if self.lang_keys.keys == 'e':
            self.text_28.setText("You win " + str(self.task_rew) + " "+ "points in these set of blocks!")
        else:
            self.text_28.setText("Du gewinnst " + str(self.task_rew) + " "+ "Punkte in diesem Satz von Blöcken!")
        self.proceed_20.keys = []
        self.proceed_20.rt = []
        self._proceed_20_allKeys = []
        self.task_score_components = [self.space_bg_19, self.text_28, self.proceed_20]
        self.task_score_components = self.prepare_routine(self.task_score_components)
        
        # run routine
        while self.continueRoutine:
            self.timing.get_current_time(self.language_preferenceClock, self)
            self.frameN = self.frameN + 1
            self.space_bg_19 = self.components.text_or_image_update(self.space_bg_19, 'space_bg_19.started', self)
            self.text_28 = self.components.text_or_image_update(self.text_28, 'text_28.started', self)
            self.waitOnFlip = False
            self.proceed_20, self._proceed_20_allKeys = self.components.keys_update(self.proceed_20, self._proceed_20_allKeys, 'proceed_20.started', self)
            if self.endExpNow or self.defaultKeyboard.getKeys(keyList=["escape"]): core.quit()
            if not self.continueRoutine: self.routineForceEnded = True; break
            self.continueRoutine = False
            self.task_score_components = self.components.check_if_components_finished(self.task_score_components, self)
            if self.continueRoutine: self.win.flip()
        
        # end routine
        self.task_score_components = self.components.hide_components(self.task_score_components)
        self.proceed_20 = self.components.save_key_response(self.proceed_20, 'proceed_20.keys', 'proceed_20.rt', self)
        self.routineTimer.reset()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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