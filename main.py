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
from Routines import Routines
from Handler import Handler
from Timing import Timing
from Components import Components
#from del_me import rand_init

# MAIN SCRIPT TO RUN

# TRAINING / PRACTICE / MAIN TASK
handler = Handler('handler')
timing = Timing('timing')
components = Components('components')
main = Routines('main', handler, timing, components)

# SETUP EXPERIMENT
main.setup()                                                                 # sets up experiment and participant info, an experiment handler, the window, and devices
timing.create_timers(main)                                                   # creates a global clock and a routine timer
main.initialize_routines()
main.language_preference()                                                   # asks participant to choose between english and german
main.training_task()                                                         # gives instructions to participants + trains them on radar usage
main.practice_task()                                                         # gives instructions for whole task

# START TASK
handler.prac_main_handler(main)                                                     # sets up a practice/main task handler (conditions import)
for main.thisPrac_main_task in main.prac_main_task:                          # loops first the practice and then the main task blocks (redundant code, delete in future)
    
    main.currentLoop = main.prac_main_task                                   # store info for current loop (either practice task loop or main task loop)
    main.thisPrac_main_task = handler.create_variables(main.thisPrac_main_task) # assign variables (contrast levels, planets, etc.) for current loop
    handler.block_handler(main)                                                     # sets up a blocks handler (conditions import for all blocks)
    
    for main.thisBlock in main.block:                                        # loops all the blocks
        main.currentLoop = main.block                                        # stores info for current loop
        main.thisBlock = handler.create_variables(main.thisBlock)               # assign variables (contrast levels, planets, etc.) for current block
        
        main.prac_block()                                                    # indicates what is coming up (e.g.: a new block of the main task)
        main.fixation()
        handler.primer_handler(main)                                                # sets up a primer handler (conditions import for first trial of a loop (=primer)) to extract planet info
        
        for main.thisPrimer in main.primer:                                  # handles all primer conditions (primer = first trial of each block)
            main.currentLoop = main.primer
            main.thisPrimer = handler.create_variables(main.thisPrimer)
            
            main.primer_mu()                                                 # indicates which planet the participant needs to follow the possibility for (e.g.: in this set of trials, indicate the possibility of finding space crystals on the right planet)
        
        handler.trials_handler(main)                                                # setup a trials handler (import conditions for next (20) trials)
        
        for main.thisTrial in main.trials:                                   # loops (20) trials
            main.currentLoop = main.trials                                   # log specific info about each trial
            main.thisTrial = handler.create_variables(main.thisTrial)           # assign variables (contrast levels, planets, etc.) for current trial
            
            main.fixation()
            main.signal()                                                    # signal is shown
            if main.block_num == 0 or main.block_num == 1:
                main.feedback_main()
            main.slider()                                                    # participant uses slider
            
        main.prechoice_text()                                                # paricipant is shown an info window ('before you provide..., you'll be shown...')
        handler.last_handler(main)                                                  # setup last handler (last mu)
        
        for main.thisLast in main.last:                                      # handles last slider usage
            main.currentLoop = main.last
            main.thisLast = handler.create_variables(main.thisLast)
            
            main.last_mu()                                                   # show last slider response 
        
        main.block_choice()                                                  # participants makes planet choice
        main.block_reward()                                                  # crystals are either found or not found
        main.block_completed()                                               # how many blocks has the participant completed
    main.task_score()                                                        # how many points did the participant win in the whole task
    main.end_experiment()                                                    # if we've done 16 blocks, the script saves and quits
    
    