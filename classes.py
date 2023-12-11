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


class Trial:
    
    # experiment information
    _thisDir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(_thisDir)
    psychopyVersion = '2022.2.5'
    expName = 'space_task_offline'
    expInfo = {
        'participant': f"{randint(0, 999999):06.0f}",
        'session': '001',
    }
    # yes yes yes
    
    def __init__(self, type):
        self.type = type
    
    def experiment_info(self):
        # this may be redundant, since the variables get initialized in the class attributes section
    
    def participant_window(self):
        #

    def experiment_handler(self):
        #

    def setup_window(self):
        #

    def setup_devices(self):
        #

    def setup(self):
        self.experiment_info()
        self.participant_window()
        self.experiment_handler()
        self.setup_window()
        self.setup_devices()

    def initialize_routines(self):
        #create lists containing all components of the given routines, assign the values from the global class attributes (e.g.: class attribute space_background → space_bg_17 = space_background → routine_x_components = […, space_bg_17, …])

    def create_timers(self):
        #

    def keep_track(self, components):
        #

    def reset_timers(self):
        #

    def get_current_time(self):
        #

    def text_or_image_update(self):
        #

    def keys_update(self):
        #

    def check_if_components_finished(self):
        #

    def hide_components(self):
        #

    def check_and_save_responses(self):
        # implement this

    def prepare_routine(self, components):
        self.keep_track(components)
        self.reset_timers()

    def run_routine(self, components):
        while continueRoutine:
            self.get_current_time()
            self.text_or_image_update()
            self.keys_update()
            self.check_if_components_finished()

    def end_routine(self, components):
        self.hide_components()
        self.check_and_save_responses()

    def language_preference(self):
        language_preference_components = []
        self.prepare_routine(language_preference_components)
        self.run_routine(language_preference_components)
        self.end_routine(language_preference_components)

    def prac_main_handler(self):
        #

    def block_handler(self):
        #

    def prac_block(self):
        prac_block_components = []
        self.prepare_routine(prac_block_components)
        self.run_routine(prac_block_components)
        self.end_routine(prac_block_components)

    def primer_handler(self):
        #

    def primer_mu(self):
        primer_mu_components = []
        self.prepare_routine(primer_mu_components)
        self.run_routine(primer_mu_components)
        self.end_routine(primer_mu_components)

    def trials_handler(self):
        #

    def signal(self): # SPECIFICS!!!
        signal_components = []
        self.prepare_routine(signal_components)
        self.run_routine(signal_components)
        self.end_routine(signal_components)

    def slider(self): # SPECIFICS!!!
        slider_components = []
        self.prepare_routine(slider_components)
        self.run_routine(slider_components)
        self.end_routine(slider_components)

    def prechoice_text(self):
        prechoice_text_components = […]
        self.prepare_routine(prechoice_text_components)
        self.run_routine(prechoice_text_components)
        self.end_routine(prechoice_text_components)

    def last_handler(self):
        #

    def last_mu(self): # SPECIFICS!
        last_mu_components = […]
        self.prepare_routine(last_mu_components)
        self.run_routine(last_mu_components)
        self.end_routine(last_mu_components)

    def block_choice(self): # SPECIFICS
        block_choice_components = […]
        self.prepare_routine(block_choice_components)
        self.run_routine(block_choice_components)
        self.end_routine(block_choice_components)

    def block_reward(self):
        block_reward_components = […]
        self.prepare_routine(block_reward_components)
        self.run_routine(block_reward_components)
        self.end_routine(block_reward_components)

    def block_completed(self):
        block_completed_components = […]
        self.prepare_routine(block_completed_components)
        self.run_routine(block_completed_components)
        self.end_routine(block_completed_components)

    def task_score(self):
        task_score_components = […]
        self.prepare_routine(task_score_components)
        self.run_routine(task_score_components)
        self.end_routine(task_score_components)

    def end_experiment(self):
        #