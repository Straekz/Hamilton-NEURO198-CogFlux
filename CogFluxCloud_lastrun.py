#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on November 09, 2024, at 22:16
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from imports_3
import random
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'CogFluxCloud'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1920, 1080]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\skitt\\Desktop\\Courses\\F24 N198 Prof List\\CogFluxCloud\\CogFluxCloud_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('Start') is None:
        # initialise Start
        Start = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Start',
        )
    if deviceManager.getDevice('Response_2') is None:
        # initialise Response_2
        Response_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Response_2',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "consentForm_1" ---
    Consent_Form = visual.TextStim(win=win, name='Consent_Form',
        text='',
        font='Arial',
        pos=(0, 0.05), draggable=False, height=0.023, wrapWidth=None, ori=0.0, 
        color=[1,1,1], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    forward = visual.TextStim(win=win, name='forward',
        text='',
        font='Arial',
        pos=(0, -0.4), draggable=False, height=0.023, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    click = event.Mouse(win=win)
    x, y = [None, None]
    click.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "consentForm_2" ---
    Consent_Form_2 = visual.TextStim(win=win, name='Consent_Form_2',
        text='',
        font='Arial',
        pos=(0, 0.15), draggable=False, height=0.023, wrapWidth=None, ori=0.0, 
        color=[1,1,1], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    SaC = visual.TextStim(win=win, name='SaC',
        text='Statement of Consent:\nI have read the above information. Select one of the two following options:',
        font='Arial',
        pos=(0, -0.15), draggable=False, height=0.023, wrapWidth=1.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    consent = visual.Slider(win=win, name='consent',
        startValue=None, size=(30, 60), pos=(-250, -280), units='pix',
        labels=("I consent to participation and am 18 years or older.", "I do not consent to participation or I am younger than 18 years old."), ticks=(1, 2), granularity=0.0,
        style='choice', styleTweaks=(), opacity=None,
        labelColor='Black', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Arial', labelHeight=20.0,
        flip=True, ori=0.0, depth=-3, readOnly=False)
    forward_2 = visual.TextStim(win=win, name='forward_2',
        text='',
        font='Arial',
        pos=(0, -0.4), draggable=False, height=0.023, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    click_2 = event.Mouse(win=win)
    x, y = [None, None]
    click_2.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "exclusion" ---
    ThanksText_2 = visual.TextStim(win=win, name='ThanksText_2',
        text='Sorry, you are not qualified for this experiment.\n\nThank you.\n\nYou can press the [ESC] button to leave.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "instructColor" ---
    confirmSign_click_14 = event.Mouse(win=win)
    x, y = [None, None]
    confirmSign_click_14.mouseClock = core.Clock()
    confirmSign_button_14 = visual.TextStim(win=win, name='confirmSign_button_14',
        text='Click here to continue.',
        font='Arial',
        pos=(0, -0.25), draggable=False, height=0.023, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_4 = visual.TextStim(win=win, name='text_4',
        text='After you click the continue button, \na green vertical rectangle and a red vertical rectangle will appear.\n\nClick on the red vertical rectangle.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.023, wrapWidth=None, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "RG_colorblind" ---
    # Run 'Begin Experiment' code from code
    opposite = [-1,1]
    green = visual.ImageStim(
        win=win,
        name='green', units='pix', 
        image='resources/GV.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=[25, 100],
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    red = visual.ImageStim(
        win=win,
        name='red', units='pix', 
        image='resources/RV.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=[25, 100],
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "instructTrial" ---
    text = visual.TextStim(win=win, name='text',
        text='In the following task you will be presented with arrays of various colored rectangles (green and red). \n\nYour task is to search for a red vertical rectangle.\n \nPress the [P] key if the red vertical rectangle is PRESENT \nand the [A] key if the red vertical rectangle is ABSENT. \n\nPlease respond as quickly as possible, while minimizing errors.\n\nPress the [spacebar] when you are ready to begin.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.023, wrapWidth=1.1, ori=0.0, 
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Start = keyboard.Keyboard(deviceName='Start')
    
    # --- Initialize components for Routine "both_trials" ---
    fixation_3 = visual.TextStim(win=win, name='fixation_3',
        text='+',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    targetRV_2 = visual.ImageStim(
        win=win,
        name='targetRV_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=[25, 100],
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    dist1img_2 = visual.ImageStim(
        win=win,
        name='dist1img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    dist2img_2 = visual.ImageStim(
        win=win,
        name='dist2img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    dist3img_2 = visual.ImageStim(
        win=win,
        name='dist3img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-8.0)
    dist4img_2 = visual.ImageStim(
        win=win,
        name='dist4img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-9.0)
    dist5img_2 = visual.ImageStim(
        win=win,
        name='dist5img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-10.0)
    dist6img_2 = visual.ImageStim(
        win=win,
        name='dist6img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-11.0)
    dist7img_2 = visual.ImageStim(
        win=win,
        name='dist7img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-12.0)
    dist8img_2 = visual.ImageStim(
        win=win,
        name='dist8img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-13.0)
    dist9img_2 = visual.ImageStim(
        win=win,
        name='dist9img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-14.0)
    dist10img_2 = visual.ImageStim(
        win=win,
        name='dist10img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-15.0)
    dist11img_2 = visual.ImageStim(
        win=win,
        name='dist11img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-16.0)
    dist12img_2 = visual.ImageStim(
        win=win,
        name='dist12img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-17.0)
    Response_2 = keyboard.Keyboard(deviceName='Response_2')
    
    # --- Initialize components for Routine "feedback" ---
    fd = visual.TextStim(win=win, name='fd',
        text='Incorrect',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "both_trials" ---
    fixation_3 = visual.TextStim(win=win, name='fixation_3',
        text='+',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    targetRV_2 = visual.ImageStim(
        win=win,
        name='targetRV_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=[25, 100],
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    dist1img_2 = visual.ImageStim(
        win=win,
        name='dist1img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    dist2img_2 = visual.ImageStim(
        win=win,
        name='dist2img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    dist3img_2 = visual.ImageStim(
        win=win,
        name='dist3img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-8.0)
    dist4img_2 = visual.ImageStim(
        win=win,
        name='dist4img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-9.0)
    dist5img_2 = visual.ImageStim(
        win=win,
        name='dist5img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-10.0)
    dist6img_2 = visual.ImageStim(
        win=win,
        name='dist6img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-11.0)
    dist7img_2 = visual.ImageStim(
        win=win,
        name='dist7img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-12.0)
    dist8img_2 = visual.ImageStim(
        win=win,
        name='dist8img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-13.0)
    dist9img_2 = visual.ImageStim(
        win=win,
        name='dist9img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-14.0)
    dist10img_2 = visual.ImageStim(
        win=win,
        name='dist10img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-15.0)
    dist11img_2 = visual.ImageStim(
        win=win,
        name='dist11img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-16.0)
    dist12img_2 = visual.ImageStim(
        win=win,
        name='dist12img_2', units='pix', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=1.0,
        color=[.8, .8, .8], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-17.0)
    Response_2 = keyboard.Keyboard(deviceName='Response_2')
    
    # --- Initialize components for Routine "feedback" ---
    fd = visual.TextStim(win=win, name='fd',
        text='Incorrect',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "Rest" ---
    RestText = visual.TextStim(win=win, name='RestText',
        text='30 Second Rest\n\nRemember to find the red vertical rectangle.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "PreMEQ" ---
    form = visual.TextStim(win=win, name='form',
        text='Thank you for completing our tasks.\n\nPlease answer the following questions about yourself.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.023, wrapWidth=None, ori=0.0, 
        color=[1,1,1], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    confirmSign_button_3 = visual.TextStim(win=win, name='confirmSign_button_3',
        text='Click here to continue.',
        font='Arial',
        pos=(0, -0.4), draggable=False, height=0.023, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    confirmSign_click_3 = event.Mouse(win=win)
    x, y = [None, None]
    confirmSign_click_3.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "bestfeel_meq" ---
    confirmSign_click_4 = event.Mouse(win=win)
    x, y = [None, None]
    confirmSign_click_4.mouseClock = core.Clock()
    confirmSign_button_4 = visual.TextStim(win=win, name='confirmSign_button_4',
        text='Click here to confirm\n[You will not be able to go back]',
        font='Arial',
        pos=(0, -0.25), draggable=False, height=0.023, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    best_feel_Q = visual.TextStim(win=win, name='best_feel_Q',
        text='Considering only your own “best feeling” rhythm, at what time would you get up if you were entirely free to plan your day?',
        font='Arial',
        pos=(0, 0.22), draggable=False, height=0.023, wrapWidth=1.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    best_feel = visual.Slider(win=win, name='best_feel',
        startValue=None, size=(30, 250), pos=(-175, 0), units='pix',
        labels=('10:45 AM - 12:00 PM', '9:30 AM - 10:45 AM', '7:45 AM - 9:30 AM', '6:30 AM - 7:45 AM', '5:00 AM - 6:30 AM'), ticks=(1, 2, 3, 4, 5), granularity=0.0,
        style='choice', styleTweaks=(), opacity=None,
        labelColor='White', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Arial', labelHeight=18.0,
        flip=True, ori=0.0, depth=-4, readOnly=False)
    
    # --- Initialize components for Routine "wokentired_meq" ---
    confirmSign_click_6 = event.Mouse(win=win)
    x, y = [None, None]
    confirmSign_click_6.mouseClock = core.Clock()
    confirmSign_button_6 = visual.TextStim(win=win, name='confirmSign_button_6',
        text='Click here to confirm\n[You will not be able to go back]',
        font='Arial',
        pos=(0, -0.25), draggable=False, height=0.023, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    woken_tired_Q = visual.TextStim(win=win, name='woken_tired_Q',
        text='After the first half hour after having woken in the morning, how tired do you feel?',
        font='Arial',
        pos=(0, 0.22), draggable=False, height=0.023, wrapWidth=1.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    woken_tired = visual.Slider(win=win, name='woken_tired',
        startValue=None, size=(30, 250), pos=(-175, 0), units='pix',
        labels=('Very Refreshed', 'Fairly Refreshed', 'Fairly Tired', 'Very Tired'), ticks=(1, 2, 3, 4), granularity=0.0,
        style='choice', styleTweaks=(), opacity=None,
        labelColor='White', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Arial', labelHeight=18.0,
        flip=True, ori=0.0, depth=-4, readOnly=False)
    
    # --- Initialize components for Routine "sleepytime_meq" ---
    confirmSign_click_7 = event.Mouse(win=win)
    x, y = [None, None]
    confirmSign_click_7.mouseClock = core.Clock()
    confirmSign_button_7 = visual.TextStim(win=win, name='confirmSign_button_7',
        text='Click here to confirm\n[You will not be able to go back]',
        font='Arial',
        pos=(0, -0.25), draggable=False, height=0.023, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    sleepy_time_Q = visual.TextStim(win=win, name='sleepy_time_Q',
        text='At what time in the evening would you feel tired and as a result in need of sleep?',
        font='Arial',
        pos=(0, 0.22), draggable=False, height=0.023, wrapWidth=1.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    sleepy_time = visual.Slider(win=win, name='sleepy_time',
        startValue=None, size=(30, 250), pos=(-175, 0), units='pix',
        labels=('1:45 AM - 3:00 AM', '12:30 AM - 1:45 AM', '10:15 PM - 12:30 AM', '9:00 PM - 10:15 PM', '8:00 PM - 9:00 PM'), ticks=(1, 2, 3, 4, 5), granularity=0.0,
        style='choice', styleTweaks=(), opacity=None,
        labelColor='White', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Arial', labelHeight=18.0,
        flip=True, ori=0.0, depth=-4, readOnly=False)
    
    # --- Initialize components for Routine "bestpeak_meq" ---
    confirmSign_click_8 = event.Mouse(win=win)
    x, y = [None, None]
    confirmSign_click_8.mouseClock = core.Clock()
    confirmSign_button_8 = visual.TextStim(win=win, name='confirmSign_button_8',
        text='Click here to confirm\n[You will not be able to go back]',
        font='Arial',
        pos=(0, -0.25), draggable=False, height=0.023, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    best_peak_Q = visual.TextStim(win=win, name='best_peak_Q',
        text='At what time of the day do you think that you reach your “feeling best” peak?',
        font='Arial',
        pos=(0, 0.22), draggable=False, height=0.023, wrapWidth=1.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    best_peak = visual.Slider(win=win, name='best_peak',
        startValue=None, size=(30, 250), pos=(-175, 0), units='pix',
        labels=('9:30 PM - 4:30 AM', '4:30 PM - 9:30 PM', '9:30 AM - 4:30 PM', '7:30 AM - 9:30 AM', '4:30 AM - 7:30 AM'), ticks=(1, 2, 3, 4, 5), granularity=0.0,
        style='choice', styleTweaks=(), opacity=None,
        labelColor='White', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Arial', labelHeight=18.0,
        flip=True, ori=0.0, depth=-4, readOnly=False)
    
    # --- Initialize components for Routine "persontype_meq" ---
    confirmSign_click_9 = event.Mouse(win=win)
    x, y = [None, None]
    confirmSign_click_9.mouseClock = core.Clock()
    confirmSign_button_9 = visual.TextStim(win=win, name='confirmSign_button_9',
        text='Click here to confirm\n[You will not be able to go back]',
        font='Arial',
        pos=(0, -0.25), draggable=False, height=0.023, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    person_type_Q = visual.TextStim(win=win, name='person_type_Q',
        text='One hears about morning and evening types of people. Which one of these types do you consider yourself to be? ',
        font='Arial',
        pos=(0, 0.22), draggable=False, height=0.023, wrapWidth=1.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    person_type = visual.Slider(win=win, name='person_type',
        startValue=None, size=(30, 250), pos=(-175, 0), units='pix',
        labels=('Definitely an "evening" type', 'Rather more a "evening" than a "morning" type', 'Rather more a "morning" than an "evening" type', 'Definitely a "morning" type'), ticks=(1, 2, 3, 4), granularity=0.0,
        style='choice', styleTweaks=(), opacity=None,
        labelColor='White', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Arial', labelHeight=18.0,
        flip=True, ori=0.0, depth=-4, readOnly=False)
    
    # --- Initialize components for Routine "what_age" ---
    confirmSign_click_10 = event.Mouse(win=win)
    x, y = [None, None]
    confirmSign_click_10.mouseClock = core.Clock()
    confirmSign_button_10 = visual.TextStim(win=win, name='confirmSign_button_10',
        text='Click here after you have typed your age.\n[You will not be able to go back]',
        font='Arial',
        pos=(0, -0.25), draggable=False, height=0.023, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    age_fill_Q = visual.TextStim(win=win, name='age_fill_Q',
        text='Enter your age in the textbox below.',
        font='Arial',
        pos=(0, 0.06), draggable=False, height=0.023, wrapWidth=1.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    age_Q = visual.TextBox2(
         win, text=None, placeholder='Type your age here...', font='Arial',
         ori=0.0, pos=(0, -0.05), draggable=False,      letterHeight=0.023,
         size=(0.8, 0.1), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='age_Q',
         depth=-4, autoLog=True,
    )
    
    # --- Initialize components for Routine "gender" ---
    confirmSign_click_11 = event.Mouse(win=win)
    x, y = [None, None]
    confirmSign_click_11.mouseClock = core.Clock()
    confirmSign_button_11 = visual.TextStim(win=win, name='confirmSign_button_11',
        text='Click here to confirm\n[You will not be able to go back]',
        font='Arial',
        pos=(0, -0.35), draggable=False, height=0.023, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    gender_Q = visual.TextStim(win=win, name='gender_Q',
        text='With which gender do you identify?',
        font='Arial',
        pos=(0, 0.36), draggable=False, height=0.023, wrapWidth=1.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    gender_c = visual.Slider(win=win, name='gender_c',
        startValue=None, size=(30, 300), pos=(-175, 125), units='pix',
        labels=('Other gender (please describe below)', 'Transgender male', 'Transgender female', 'Gender non-binary/genderfluid/genderqueer', 'Cisgender male', 'Cisgender female'), ticks=(1, 2, 3, 4, 5, 6), granularity=0.0,
        style='choice', styleTweaks=(), opacity=None,
        labelColor='White', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Arial', labelHeight=18.0,
        flip=True, ori=0.0, depth=-4, readOnly=False)
    other_gender_text = visual.TextBox2(
         win, text=None, placeholder="(Please describe gender here if you chose 'another')", font='Arial',
         ori=0.0, pos=(0, -0.2), draggable=False,      letterHeight=0.023,
         size=(0.95, 0.2), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='other_gender_text',
         depth=-5, autoLog=True,
    )
    
    # --- Initialize components for Routine "race_ethn" ---
    confirmSign_click_13 = event.Mouse(win=win)
    x, y = [None, None]
    confirmSign_click_13.mouseClock = core.Clock()
    confirmSign_button_13 = visual.TextStim(win=win, name='confirmSign_button_13',
        text='Click here to confirm\n[You will not be able to go back]',
        font='Arial',
        pos=(0, -0.35), draggable=False, height=0.023, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    race_Q = visual.TextStim(win=win, name='race_Q',
        text='Which best describes your race/ethnicity?',
        font='Arial',
        pos=(0, 0.37), draggable=False, height=0.023, wrapWidth=1.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    race_c = visual.Slider(win=win, name='race_c',
        startValue=None, size=(30, 300), pos=(-175, 125), units='pix',
        labels=('Multiple or Other race/ethnicity (please describe below)', 'White', 'Middle Eastern or North African', 'American Indian or Alaskan Native', 'Native Hawaiian or other Pacific Islander', 'Asian or Asian-American', 'Hispanic, Latinx, or Spanish Origin', 'Black or African-American'), ticks=(1, 2, 3, 4, 5, 6, 7, 8), granularity=0.0,
        style='choice', styleTweaks=(), opacity=None,
        labelColor='White', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Arial', labelHeight=18.0,
        flip=True, ori=0.0, depth=-4, readOnly=False)
    other_race_text = visual.TextBox2(
         win, text=None, placeholder="(Please describe race/ethnicity here if you chose 'other')", font='Arial',
         ori=0.0, pos=(0, -0.2), draggable=False,      letterHeight=0.023,
         size=(0.95, 0.2), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor='white',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='other_race_text',
         depth=-5, autoLog=True,
    )
    
    # --- Initialize components for Routine "Thanks" ---
    ThanksText = visual.TextStim(win=win, name='ThanksText',
        text='Thank you for your participation.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "consentForm_1" ---
    # create an object to store info about Routine consentForm_1
    consentForm_1 = data.Routine(
        name='consentForm_1',
        components=[Consent_Form, forward, click],
    )
    consentForm_1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from showMouse
    win.mouseVisible = True
    Consent_Form.setText('Hamilton College\nPsychology Department\n198 College Hill Rd.\nClinton, NY 13323\n\nParticipant Consent Form: Cognitive Fluctuations\n\nPurpose:\nThe purpose of this study is to examine how cognitive performance fluctuates for different people, at different times, while doing different tasks. This study is part of Prof. Alexandra List’s research.\n\nProcedure:\nIf you agree to be in this study, you will be asked to view simple images on a computer screen and respond with specific button presses. You will be asked to respond quickly and accurately. You will also be asked to answer a series of questions about when you prefer to be awake and performing various tasks, in addition to providing basic demographic information (i.e., age, gender, race/ethnicity).\n\nThe total time required to complete the study should be under 15 minutes. If you complete the study, you will receive $2.50 for participating in the study.\n\nBenefits/Risks to Participant:\nParticipants will learn about the empirical methodologies of and will help contribute to the body of knowledge in Psychology. Risks include any boredom you may feel while answering the questions. Breaks can be taken as needed.')
    forward.setText('Click here to continue')
    # setup some python lists for storing info about the click
    click.x = []
    click.y = []
    click.leftButton = []
    click.midButton = []
    click.rightButton = []
    click.time = []
    click.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for consentForm_1
    consentForm_1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    consentForm_1.tStart = globalClock.getTime(format='float')
    consentForm_1.status = STARTED
    thisExp.addData('consentForm_1.started', consentForm_1.tStart)
    consentForm_1.maxDuration = None
    # keep track of which components have finished
    consentForm_1Components = consentForm_1.components
    for thisComponent in consentForm_1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "consentForm_1" ---
    consentForm_1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Consent_Form* updates
        
        # if Consent_Form is starting this frame...
        if Consent_Form.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Consent_Form.frameNStart = frameN  # exact frame index
            Consent_Form.tStart = t  # local t and not account for scr refresh
            Consent_Form.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Consent_Form, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Consent_Form.started')
            # update status
            Consent_Form.status = STARTED
            Consent_Form.setAutoDraw(True)
        
        # if Consent_Form is active this frame...
        if Consent_Form.status == STARTED:
            # update params
            pass
        
        # *forward* updates
        
        # if forward is starting this frame...
        if forward.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            forward.frameNStart = frameN  # exact frame index
            forward.tStart = t  # local t and not account for scr refresh
            forward.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(forward, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'forward.started')
            # update status
            forward.status = STARTED
            forward.setAutoDraw(True)
        
        # if forward is active this frame...
        if forward.status == STARTED:
            # update params
            pass
        # *click* updates
        
        # if click is starting this frame...
        if click.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            click.frameNStart = frameN  # exact frame index
            click.tStart = t  # local t and not account for scr refresh
            click.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(click, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('click.started', t)
            # update status
            click.status = STARTED
            click.mouseClock.reset()
            prevButtonState = click.getPressed()  # if button is down already this ISN'T a new click
        if click.status == STARTED:  # only update if started and not finished!
            buttons = click.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(forward, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(click):
                            gotValidClick = True
                            click.clicked_name.append(obj.name)
                    if not gotValidClick:
                        click.clicked_name.append(None)
                    x, y = click.getPos()
                    click.x.append(x)
                    click.y.append(y)
                    buttons = click.getPressed()
                    click.leftButton.append(buttons[0])
                    click.midButton.append(buttons[1])
                    click.rightButton.append(buttons[2])
                    click.time.append(click.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            consentForm_1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in consentForm_1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "consentForm_1" ---
    for thisComponent in consentForm_1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for consentForm_1
    consentForm_1.tStop = globalClock.getTime(format='float')
    consentForm_1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('consentForm_1.stopped', consentForm_1.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('click.x', click.x)
    thisExp.addData('click.y', click.y)
    thisExp.addData('click.leftButton', click.leftButton)
    thisExp.addData('click.midButton', click.midButton)
    thisExp.addData('click.rightButton', click.rightButton)
    thisExp.addData('click.time', click.time)
    thisExp.addData('click.clicked_name', click.clicked_name)
    thisExp.nextEntry()
    # the Routine "consentForm_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "consentForm_2" ---
    # create an object to store info about Routine consentForm_2
    consentForm_2 = data.Routine(
        name='consentForm_2',
        components=[Consent_Form_2, SaC, consent, forward_2, click_2],
    )
    consentForm_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from showMouse_8
    win.mouseVisible = True
    Consent_Form_2.setText('Voluntary Nature of the Study/Confidentiality:\nYour participation in this study is entirely voluntary and you may refuse to complete the study at any point during the experiment, or refuse to answer or skip any questions with which you are uncomfortable. You may also stop at any time. Your name will never be connected to your results or to your responses; instead, a number will be used for data identification purposes. Information that would make it possible to identify you or any other participant will never be included in any sort of report. The data will be accessible only to those working on the project.\n\nContacts and Questions:\nIf you have questions, you may contact Dr. Alexandra List at 315-859-4308 or scct3045@hamilton.edu. Questions or concerns about institutional approval should be directed to Dr. Rachel White, Chair of the Institutional Review Board for Human Subjects, 315-859-4518 or iboard@hamilton.edu.\n\nI have been provided a link to\xa0Hamilton’s Privacy Notice\xa0(https://www.hamilton.edu/privacy) and have read and understood it. I consent to the processing of my personal data and special categories of personal data in accordance with the Privacy Notice and for the purposes of applying to and participating in Hamilton College research studies.')
    consent.reset()
    forward_2.setText('Click here to continue')
    # setup some python lists for storing info about the click_2
    click_2.x = []
    click_2.y = []
    click_2.leftButton = []
    click_2.midButton = []
    click_2.rightButton = []
    click_2.time = []
    click_2.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for consentForm_2
    consentForm_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    consentForm_2.tStart = globalClock.getTime(format='float')
    consentForm_2.status = STARTED
    thisExp.addData('consentForm_2.started', consentForm_2.tStart)
    consentForm_2.maxDuration = None
    # keep track of which components have finished
    consentForm_2Components = consentForm_2.components
    for thisComponent in consentForm_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "consentForm_2" ---
    consentForm_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Consent_Form_2* updates
        
        # if Consent_Form_2 is starting this frame...
        if Consent_Form_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Consent_Form_2.frameNStart = frameN  # exact frame index
            Consent_Form_2.tStart = t  # local t and not account for scr refresh
            Consent_Form_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Consent_Form_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Consent_Form_2.started')
            # update status
            Consent_Form_2.status = STARTED
            Consent_Form_2.setAutoDraw(True)
        
        # if Consent_Form_2 is active this frame...
        if Consent_Form_2.status == STARTED:
            # update params
            pass
        
        # *SaC* updates
        
        # if SaC is starting this frame...
        if SaC.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SaC.frameNStart = frameN  # exact frame index
            SaC.tStart = t  # local t and not account for scr refresh
            SaC.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SaC, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'SaC.started')
            # update status
            SaC.status = STARTED
            SaC.setAutoDraw(True)
        
        # if SaC is active this frame...
        if SaC.status == STARTED:
            # update params
            pass
        
        # *consent* updates
        
        # if consent is starting this frame...
        if consent.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            consent.frameNStart = frameN  # exact frame index
            consent.tStart = t  # local t and not account for scr refresh
            consent.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consent, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'consent.started')
            # update status
            consent.status = STARTED
            consent.setAutoDraw(True)
        
        # if consent is active this frame...
        if consent.status == STARTED:
            # update params
            pass
        
        # *forward_2* updates
        
        # if forward_2 is starting this frame...
        if forward_2.status == NOT_STARTED and consent.rating:
            # keep track of start time/frame for later
            forward_2.frameNStart = frameN  # exact frame index
            forward_2.tStart = t  # local t and not account for scr refresh
            forward_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(forward_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'forward_2.started')
            # update status
            forward_2.status = STARTED
            forward_2.setAutoDraw(True)
        
        # if forward_2 is active this frame...
        if forward_2.status == STARTED:
            # update params
            pass
        # *click_2* updates
        
        # if click_2 is starting this frame...
        if click_2.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            click_2.frameNStart = frameN  # exact frame index
            click_2.tStart = t  # local t and not account for scr refresh
            click_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(click_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('click_2.started', t)
            # update status
            click_2.status = STARTED
            click_2.mouseClock.reset()
            prevButtonState = click_2.getPressed()  # if button is down already this ISN'T a new click
        if click_2.status == STARTED:  # only update if started and not finished!
            buttons = click_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(forward_2, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(click_2):
                            gotValidClick = True
                            click_2.clicked_name.append(obj.name)
                    if not gotValidClick:
                        click_2.clicked_name.append(None)
                    x, y = click_2.getPos()
                    click_2.x.append(x)
                    click_2.y.append(y)
                    buttons = click_2.getPressed()
                    click_2.leftButton.append(buttons[0])
                    click_2.midButton.append(buttons[1])
                    click_2.rightButton.append(buttons[2])
                    click_2.time.append(click_2.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            consentForm_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in consentForm_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "consentForm_2" ---
    for thisComponent in consentForm_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for consentForm_2
    consentForm_2.tStop = globalClock.getTime(format='float')
    consentForm_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('consentForm_2.stopped', consentForm_2.tStop)
    thisExp.addData('consent.response', consent.getRating())
    thisExp.addData('consent.rt', consent.getRT())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('click_2.x', click_2.x)
    thisExp.addData('click_2.y', click_2.y)
    thisExp.addData('click_2.leftButton', click_2.leftButton)
    thisExp.addData('click_2.midButton', click_2.midButton)
    thisExp.addData('click_2.rightButton', click_2.rightButton)
    thisExp.addData('click_2.time', click_2.time)
    thisExp.addData('click_2.clicked_name', click_2.clicked_name)
    thisExp.nextEntry()
    # the Routine "consentForm_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "exclusion" ---
    # create an object to store info about Routine exclusion
    exclusion = data.Routine(
        name='exclusion',
        components=[ThanksText_2],
    )
    exclusion.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from exclude_show
    if consent.rating != 2:
        continueRoutine = False
    # Run 'Begin Routine' code from showMouse_9
    win.mouseVisible = True
    # store start times for exclusion
    exclusion.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    exclusion.tStart = globalClock.getTime(format='float')
    exclusion.status = STARTED
    thisExp.addData('exclusion.started', exclusion.tStart)
    exclusion.maxDuration = None
    # keep track of which components have finished
    exclusionComponents = exclusion.components
    for thisComponent in exclusion.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "exclusion" ---
    exclusion.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ThanksText_2* updates
        
        # if ThanksText_2 is starting this frame...
        if ThanksText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ThanksText_2.frameNStart = frameN  # exact frame index
            ThanksText_2.tStart = t  # local t and not account for scr refresh
            ThanksText_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ThanksText_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ThanksText_2.started')
            # update status
            ThanksText_2.status = STARTED
            ThanksText_2.setAutoDraw(True)
        
        # if ThanksText_2 is active this frame...
        if ThanksText_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            exclusion.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exclusion.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "exclusion" ---
    for thisComponent in exclusion.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for exclusion
    exclusion.tStop = globalClock.getTime(format='float')
    exclusion.tStopRefresh = tThisFlipGlobal
    thisExp.addData('exclusion.stopped', exclusion.tStop)
    thisExp.nextEntry()
    # the Routine "exclusion" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructColor" ---
    # create an object to store info about Routine instructColor
    instructColor = data.Routine(
        name='instructColor',
        components=[confirmSign_click_14, confirmSign_button_14, text_4],
    )
    instructColor.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from exclude
    if consent.rating == 2:
        continueRoutine = False
    # setup some python lists for storing info about the confirmSign_click_14
    confirmSign_click_14.x = []
    confirmSign_click_14.y = []
    confirmSign_click_14.leftButton = []
    confirmSign_click_14.midButton = []
    confirmSign_click_14.rightButton = []
    confirmSign_click_14.time = []
    confirmSign_click_14.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for instructColor
    instructColor.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructColor.tStart = globalClock.getTime(format='float')
    instructColor.status = STARTED
    thisExp.addData('instructColor.started', instructColor.tStart)
    instructColor.maxDuration = None
    # keep track of which components have finished
    instructColorComponents = instructColor.components
    for thisComponent in instructColor.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructColor" ---
    instructColor.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *confirmSign_click_14* updates
        
        # if confirmSign_click_14 is starting this frame...
        if confirmSign_click_14.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            confirmSign_click_14.frameNStart = frameN  # exact frame index
            confirmSign_click_14.tStart = t  # local t and not account for scr refresh
            confirmSign_click_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_click_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('confirmSign_click_14.started', t)
            # update status
            confirmSign_click_14.status = STARTED
            confirmSign_click_14.mouseClock.reset()
            prevButtonState = confirmSign_click_14.getPressed()  # if button is down already this ISN'T a new click
        if confirmSign_click_14.status == STARTED:  # only update if started and not finished!
            buttons = confirmSign_click_14.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(confirmSign_button_10, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(confirmSign_click_14):
                            gotValidClick = True
                            confirmSign_click_14.clicked_name.append(obj.name)
                    if not gotValidClick:
                        confirmSign_click_14.clicked_name.append(None)
                    x, y = confirmSign_click_14.getPos()
                    confirmSign_click_14.x.append(x)
                    confirmSign_click_14.y.append(y)
                    buttons = confirmSign_click_14.getPressed()
                    confirmSign_click_14.leftButton.append(buttons[0])
                    confirmSign_click_14.midButton.append(buttons[1])
                    confirmSign_click_14.rightButton.append(buttons[2])
                    confirmSign_click_14.time.append(confirmSign_click_14.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *confirmSign_button_14* updates
        
        # if confirmSign_button_14 is starting this frame...
        if confirmSign_button_14.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            confirmSign_button_14.frameNStart = frameN  # exact frame index
            confirmSign_button_14.tStart = t  # local t and not account for scr refresh
            confirmSign_button_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_button_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confirmSign_button_14.started')
            # update status
            confirmSign_button_14.status = STARTED
            confirmSign_button_14.setAutoDraw(True)
        
        # if confirmSign_button_14 is active this frame...
        if confirmSign_button_14.status == STARTED:
            # update params
            pass
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructColor.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructColor.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructColor" ---
    for thisComponent in instructColor.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructColor
    instructColor.tStop = globalClock.getTime(format='float')
    instructColor.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructColor.stopped', instructColor.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('confirmSign_click_14.x', confirmSign_click_14.x)
    thisExp.addData('confirmSign_click_14.y', confirmSign_click_14.y)
    thisExp.addData('confirmSign_click_14.leftButton', confirmSign_click_14.leftButton)
    thisExp.addData('confirmSign_click_14.midButton', confirmSign_click_14.midButton)
    thisExp.addData('confirmSign_click_14.rightButton', confirmSign_click_14.rightButton)
    thisExp.addData('confirmSign_click_14.time', confirmSign_click_14.time)
    thisExp.addData('confirmSign_click_14.clicked_name', confirmSign_click_14.clicked_name)
    thisExp.nextEntry()
    # the Routine "instructColor" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    loop10_colorblind = data.TrialHandler2(
        name='loop10_colorblind',
        nReps=10.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(loop10_colorblind)  # add the loop to the experiment
    thisLoop10_colorblind = loop10_colorblind.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop10_colorblind.rgb)
    if thisLoop10_colorblind != None:
        for paramName in thisLoop10_colorblind:
            globals()[paramName] = thisLoop10_colorblind[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisLoop10_colorblind in loop10_colorblind:
        currentLoop = loop10_colorblind
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisLoop10_colorblind.rgb)
        if thisLoop10_colorblind != None:
            for paramName in thisLoop10_colorblind:
                globals()[paramName] = thisLoop10_colorblind[paramName]
        
        # --- Prepare to start Routine "RG_colorblind" ---
        # create an object to store info about Routine RG_colorblind
        RG_colorblind = data.Routine(
            name='RG_colorblind',
            components=[green, red, mouse],
        )
        RG_colorblind.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from exclude_2
        if consent.rating == 2:
            continueRoutine = False
        # Run 'Begin Routine' code from code
        import random
        shuffle (opposite)
        GV_xPos = opposite[0]*100
        RV_xPos = opposite[1]*100
        
        jitter_1 = random.randint(-45, 45)
        jitter_2 = random.randint(-45, 45)
        jitter_3 = random.randint(-45, 45)
        jitter_4 = random.randint(-45, 45)
        green.setOpacity(1.0)
        green.setPos([GV_xPos + jitter_1, jitter_2])
        red.setOpacity(1.0)
        red.setPos([RV_xPos + jitter_3, jitter_4])
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from showMouse_2
        win.mouseVisible = True
        # store start times for RG_colorblind
        RG_colorblind.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        RG_colorblind.tStart = globalClock.getTime(format='float')
        RG_colorblind.status = STARTED
        thisExp.addData('RG_colorblind.started', RG_colorblind.tStart)
        RG_colorblind.maxDuration = None
        # keep track of which components have finished
        RG_colorblindComponents = RG_colorblind.components
        for thisComponent in RG_colorblind.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "RG_colorblind" ---
        # if trial has changed, end Routine now
        if isinstance(loop10_colorblind, data.TrialHandler2) and thisLoop10_colorblind.thisN != loop10_colorblind.thisTrial.thisN:
            continueRoutine = False
        RG_colorblind.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *green* updates
            
            # if green is starting this frame...
            if green.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                green.frameNStart = frameN  # exact frame index
                green.tStart = t  # local t and not account for scr refresh
                green.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(green, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'green.started')
                # update status
                green.status = STARTED
                green.setAutoDraw(True)
            
            # if green is active this frame...
            if green.status == STARTED:
                # update params
                pass
            
            # *red* updates
            
            # if red is starting this frame...
            if red.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                red.frameNStart = frameN  # exact frame index
                red.tStart = t  # local t and not account for scr refresh
                red.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'red.started')
                # update status
                red.status = STARTED
                red.setAutoDraw(True)
            
            # if red is active this frame...
            if red.status == STARTED:
                # update params
                pass
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 1-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([green, red], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        if not gotValidClick:
                            mouse.clicked_name.append(None)
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                RG_colorblind.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RG_colorblind.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "RG_colorblind" ---
        for thisComponent in RG_colorblind.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for RG_colorblind
        RG_colorblind.tStop = globalClock.getTime(format='float')
        RG_colorblind.tStopRefresh = tThisFlipGlobal
        thisExp.addData('RG_colorblind.stopped', RG_colorblind.tStop)
        # store data for loop10_colorblind (TrialHandler)
        loop10_colorblind.addData('mouse.x', mouse.x)
        loop10_colorblind.addData('mouse.y', mouse.y)
        loop10_colorblind.addData('mouse.leftButton', mouse.leftButton)
        loop10_colorblind.addData('mouse.midButton', mouse.midButton)
        loop10_colorblind.addData('mouse.rightButton', mouse.rightButton)
        loop10_colorblind.addData('mouse.time', mouse.time)
        loop10_colorblind.addData('mouse.clicked_name', mouse.clicked_name)
        # the Routine "RG_colorblind" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 10.0 repeats of 'loop10_colorblind'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "instructTrial" ---
    # create an object to store info about Routine instructTrial
    instructTrial = data.Routine(
        name='instructTrial',
        components=[text, Start],
    )
    instructTrial.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from exclude_3
    if consent.rating == 2:
        continueRoutine = False
    # create starting attributes for Start
    Start.keys = []
    Start.rt = []
    _Start_allKeys = []
    # Run 'Begin Routine' code from hide_mouse_2
    win.mouseVisible = True
    # store start times for instructTrial
    instructTrial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructTrial.tStart = globalClock.getTime(format='float')
    instructTrial.status = STARTED
    thisExp.addData('instructTrial.started', instructTrial.tStart)
    instructTrial.maxDuration = None
    # keep track of which components have finished
    instructTrialComponents = instructTrial.components
    for thisComponent in instructTrial.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructTrial" ---
    instructTrial.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *Start* updates
        waitOnFlip = False
        
        # if Start is starting this frame...
        if Start.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            Start.frameNStart = frameN  # exact frame index
            Start.tStart = t  # local t and not account for scr refresh
            Start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Start, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Start.started')
            # update status
            Start.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Start.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Start.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Start.status == STARTED and not waitOnFlip:
            theseKeys = Start.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _Start_allKeys.extend(theseKeys)
            if len(_Start_allKeys):
                Start.keys = _Start_allKeys[-1].name  # just the last key pressed
                Start.rt = _Start_allKeys[-1].rt
                Start.duration = _Start_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructTrial.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructTrial.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructTrial" ---
    for thisComponent in instructTrial.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructTrial
    instructTrial.tStop = globalClock.getTime(format='float')
    instructTrial.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructTrial.stopped', instructTrial.tStop)
    # check responses
    if Start.keys in ['', [], None]:  # No response was made
        Start.keys = None
    thisExp.addData('Start.keys',Start.keys)
    if Start.keys != None:  # we had a response
        thisExp.addData('Start.rt', Start.rt)
        thisExp.addData('Start.duration', Start.duration)
    thisExp.nextEntry()
    # the Routine "instructTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    exp_loop = data.TrialHandler2(
        name='exp_loop',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('resources/experimentType.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(exp_loop)  # add the loop to the experiment
    thisExp_loop = exp_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExp_loop.rgb)
    if thisExp_loop != None:
        for paramName in thisExp_loop:
            globals()[paramName] = thisExp_loop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisExp_loop in exp_loop:
        currentLoop = exp_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisExp_loop.rgb)
        if thisExp_loop != None:
            for paramName in thisExp_loop:
                globals()[paramName] = thisExp_loop[paramName]
        
        # set up handler to look after randomisation of conditions etc
        prac = data.TrialHandler2(
            name='prac',
            nReps=1.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('resources/pracConditions_4.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(prac)  # add the loop to the experiment
        thisPrac = prac.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPrac.rgb)
        if thisPrac != None:
            for paramName in thisPrac:
                globals()[paramName] = thisPrac[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisPrac in prac:
            currentLoop = prac
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisPrac.rgb)
            if thisPrac != None:
                for paramName in thisPrac:
                    globals()[paramName] = thisPrac[paramName]
            
            # --- Prepare to start Routine "both_trials" ---
            # create an object to store info about Routine both_trials
            both_trials = data.Routine(
                name='both_trials',
                components=[fixation_3, targetRV_2, dist1img_2, dist2img_2, dist3img_2, dist4img_2, dist5img_2, dist6img_2, dist7img_2, dist8img_2, dist9img_2, dist10img_2, dist11img_2, dist12img_2, Response_2],
            )
            both_trials.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from exclude_4
            if consent.rating == 2:
                continueRoutine = False
            # Run 'Begin Routine' code from randomize_position_2
            #define array for stimuli:
            x_pos_Top = [-450, -150, 150, 450]
            x_pos_Mid = [-450, -150, 150, 450]
            x_pos_Bot = [-450, -150, 150, 450]
            y_pos_fix = [-300, 0, 300]
            
            #randomize stimulus position
            if setSize == 6:
                x_pos_Top = [-150, 150]
                x_pos_Mid = [-150, 150]
                x_pos_Bot = [-150, 150]
                shuffle (x_pos_Top)
                shuffle (x_pos_Mid)
                shuffle (x_pos_Bot)
                for x in range(2):
                    x_pos_Top.append(0)
                    x_pos_Mid.append(0)
                    x_pos_Bot.append(0)
            else:
                x_pos_Top = [-450, -150, 150, 450]
                x_pos_Mid = [-450, -150, 150, 450]
                x_pos_Bot = [-450, -150, 150, 450]
                shuffle (x_pos_Top)
                shuffle (x_pos_Mid)
                shuffle (x_pos_Bot)
            
            jitter_1 = random.randint(-45, 45)
            jitter_2 = random.randint(-45, 45)
            jitter_3 = random.randint(-45, 45)
            jitter_4 = random.randint(-45, 45)
            jitter_5 = random.randint(-45, 45)
            jitter_6 = random.randint(-45, 45)
            jitter_7 = random.randint(-45, 45)
            jitter_8 = random.randint(-45, 45)
            jitter_9 = random.randint(-45, 45)
            jitter_10 = random.randint(-45, 45)
            jitter_11 = random.randint(-45, 45)
            jitter_12 = random.randint(-45, 45)
            jitter_13 = random.randint(-45, 45)
            jitter_14 = random.randint(-45, 45)
            jitter_15 = random.randint(-45, 45)
            jitter_16 = random.randint(-45, 45)
            jitter_17 = random.randint(-45, 45)
            jitter_18 = random.randint(-45, 45)
            jitter_19 = random.randint(-45, 45)
            jitter_20 = random.randint(-45, 45)
            jitter_21 = random.randint(-45, 45)
            jitter_22 = random.randint(-45, 45)
            jitter_23 = random.randint(-45, 45)
            jitter_24 = random.randint(-45, 45)
            # Run 'Begin Routine' code from position_vars_2
            dist1_pos = [x_pos_Top[0] + jitter_1, y_pos_fix[2] + jitter_2]
            dist2_pos = [x_pos_Mid[0] + jitter_3, y_pos_fix[1] + jitter_4]
            dist3_pos = [x_pos_Bot[0] + jitter_5, y_pos_fix[0] + jitter_6]
            dist4_pos = [x_pos_Top[1] + jitter_7, y_pos_fix[2] + jitter_8]
            dist5_pos = [x_pos_Mid[1] + jitter_9, y_pos_fix[1] + jitter_10]
            dist6_pos = [x_pos_Bot[1] + jitter_11, y_pos_fix[0] + jitter_12]
            dist7_pos = [x_pos_Top[2] + jitter_13, y_pos_fix[2] + jitter_14]
            dist8_pos = [x_pos_Mid[2] + jitter_15, y_pos_fix[1] + jitter_16]
            dist9_pos = [x_pos_Bot[2] + jitter_17, y_pos_fix[0] + jitter_18]
            dist10_pos = [x_pos_Top[3] + jitter_19, y_pos_fix[2] + jitter_20]
            dist11_pos = [x_pos_Mid[3] + jitter_21, y_pos_fix[1] + jitter_22]
            dist12_pos = [x_pos_Bot[3] + jitter_23, y_pos_fix[0] + jitter_24]
            
            #position, no jitter
            O_dist1_pos = [x_pos_Top[0], y_pos_fix[2]]
            O_dist2_pos = [x_pos_Mid[0], y_pos_fix[1]]
            O_dist3_pos = [x_pos_Bot[0], y_pos_fix[0]]
            O_dist4_pos = [x_pos_Top[1], y_pos_fix[2]]
            O_dist5_pos = [x_pos_Mid[1], y_pos_fix[1]]
            O_dist6_pos = [x_pos_Bot[1], y_pos_fix[0]]
            O_dist7_pos = [x_pos_Top[2], y_pos_fix[2]]
            O_dist8_pos = [x_pos_Mid[2], y_pos_fix[1]]
            O_dist9_pos = [x_pos_Bot[2], y_pos_fix[0]]
            O_dist10_pos = [x_pos_Top[3], y_pos_fix[2]]
            O_dist11_pos = [x_pos_Mid[3], y_pos_fix[1]]
            O_dist12_pos = [x_pos_Bot[3], y_pos_fix[0]]
            O_target_pos = [targetPos_X,targetPos_Y]
            # Run 'Begin Routine' code from img_set
            targetFile = 'resources/RV.png'
            
            FileSet_1 = 'resources/GV.png'
            FileSet_2 = 'resources/GV.png'
            
            size_conj = [25, 100]
            
            if trialver == 'conjuction':
                FileSet_1 = 'resources/RH.png'
                size_conj = [100, 25]
            
            targetRV_2.setOpacity(targetopacity)
            targetRV_2.setPos([0, 0])
            targetRV_2.setImage(targetFile)
            dist1img_2.setOpacity(opacity_1)
            dist1img_2.setPos(dist1_pos)
            dist1img_2.setSize(size_conj)
            dist1img_2.setImage(FileSet_1)
            dist2img_2.setOpacity(opacity_2)
            dist2img_2.setPos(dist2_pos)
            dist2img_2.setSize(size_conj)
            dist2img_2.setImage(FileSet_1)
            dist3img_2.setOpacity(opacity_3)
            dist3img_2.setPos(dist3_pos)
            dist3img_2.setSize(size_conj)
            dist3img_2.setImage(FileSet_1)
            dist4img_2.setOpacity(opacity_4)
            dist4img_2.setPos(dist4_pos)
            dist4img_2.setSize([25, 100])
            dist4img_2.setImage(FileSet_2)
            dist5img_2.setOpacity(opacity_5)
            dist5img_2.setPos(dist5_pos)
            dist5img_2.setSize([25, 100])
            dist5img_2.setImage(FileSet_2)
            dist6img_2.setOpacity(opacity_6)
            dist6img_2.setPos(dist6_pos)
            dist6img_2.setSize([25, 100])
            dist6img_2.setImage(FileSet_2)
            dist7img_2.setOpacity(opacity_7)
            dist7img_2.setPos(dist7_pos)
            dist7img_2.setSize(size_conj)
            dist7img_2.setImage(FileSet_1)
            dist8img_2.setOpacity(opacity_8)
            dist8img_2.setPos(dist8_pos)
            dist8img_2.setSize(size_conj)
            dist8img_2.setImage(FileSet_1)
            dist9img_2.setOpacity(opacity_9)
            dist9img_2.setPos(dist9_pos)
            dist9img_2.setSize(size_conj)
            dist9img_2.setImage(FileSet_1)
            dist10img_2.setOpacity(opacity_10)
            dist10img_2.setPos(dist10_pos)
            dist10img_2.setSize([25, 100])
            dist10img_2.setImage(FileSet_2)
            dist11img_2.setOpacity(opacity_11)
            dist11img_2.setPos(dist11_pos)
            dist11img_2.setSize([25, 100])
            dist11img_2.setImage(FileSet_2)
            dist12img_2.setOpacity(opacity_12)
            dist12img_2.setPos(dist12_pos)
            dist12img_2.setSize([25, 100])
            dist12img_2.setImage(FileSet_2)
            # Run 'Begin Routine' code from replace_2
            # Remove the distractor for trials where target is present
            distractors = [dist1img_2, dist2img_2, dist3img_2, dist4img_2, dist5img_2, dist6img_2, dist7img_2, dist8img_2, dist9img_2, dist10img_2, dist11img_2, dist12img_2]
            dists_pos = [O_dist1_pos, O_dist2_pos, O_dist3_pos, O_dist4_pos, O_dist5_pos, O_dist6_pos, O_dist7_pos, O_dist8_pos, O_dist9_pos, O_dist10_pos, O_dist11_pos, O_dist12_pos]
            
            if setSize == 6:
                distractors = [dist1img_2, dist2img_2, dist3img_2, dist4img_2, dist5img_2, dist6img_2]
                dists_pos = [O_dist1_pos, O_dist2_pos, O_dist3_pos, O_dist4_pos, O_dist5_pos, O_dist6_pos]
            
            target_opacity = targetopacity
            target_present = (target_opacity == 1)
            
            # Only for trials where the target is present is one distractor removed.
            if target_present:
                for idx in range(len(dists_pos)):
                    if dists_pos[idx] == O_target_pos:
                        distractors[idx].opacity = 0
                        targetRV_2.pos = distractors[idx].pos
                        break
            # create starting attributes for Response_2
            Response_2.keys = []
            Response_2.rt = []
            _Response_2_allKeys = []
            # store start times for both_trials
            both_trials.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            both_trials.tStart = globalClock.getTime(format='float')
            both_trials.status = STARTED
            thisExp.addData('both_trials.started', both_trials.tStart)
            both_trials.maxDuration = None
            # keep track of which components have finished
            both_trialsComponents = both_trials.components
            for thisComponent in both_trials.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "both_trials" ---
            # if trial has changed, end Routine now
            if isinstance(prac, data.TrialHandler2) and thisPrac.thisN != prac.thisTrial.thisN:
                continueRoutine = False
            both_trials.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 4.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_3* updates
                
                # if fixation_3 is starting this frame...
                if fixation_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_3.frameNStart = frameN  # exact frame index
                    fixation_3.tStart = t  # local t and not account for scr refresh
                    fixation_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_3.started')
                    # update status
                    fixation_3.status = STARTED
                    fixation_3.setAutoDraw(True)
                
                # if fixation_3 is active this frame...
                if fixation_3.status == STARTED:
                    # update params
                    pass
                
                # if fixation_3 is stopping this frame...
                if fixation_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_3.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_3.tStop = t  # not accounting for scr refresh
                        fixation_3.tStopRefresh = tThisFlipGlobal  # on global time
                        fixation_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_3.stopped')
                        # update status
                        fixation_3.status = FINISHED
                        fixation_3.setAutoDraw(False)
                
                # *targetRV_2* updates
                
                # if targetRV_2 is starting this frame...
                if targetRV_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    targetRV_2.frameNStart = frameN  # exact frame index
                    targetRV_2.tStart = t  # local t and not account for scr refresh
                    targetRV_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(targetRV_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'targetRV_2.started')
                    # update status
                    targetRV_2.status = STARTED
                    targetRV_2.setAutoDraw(True)
                
                # if targetRV_2 is active this frame...
                if targetRV_2.status == STARTED:
                    # update params
                    pass
                
                # if targetRV_2 is stopping this frame...
                if targetRV_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > targetRV_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        targetRV_2.tStop = t  # not accounting for scr refresh
                        targetRV_2.tStopRefresh = tThisFlipGlobal  # on global time
                        targetRV_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'targetRV_2.stopped')
                        # update status
                        targetRV_2.status = FINISHED
                        targetRV_2.setAutoDraw(False)
                
                # *dist1img_2* updates
                
                # if dist1img_2 is starting this frame...
                if dist1img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist1img_2.frameNStart = frameN  # exact frame index
                    dist1img_2.tStart = t  # local t and not account for scr refresh
                    dist1img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist1img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist1img_2.started')
                    # update status
                    dist1img_2.status = STARTED
                    dist1img_2.setAutoDraw(True)
                
                # if dist1img_2 is active this frame...
                if dist1img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist1img_2 is stopping this frame...
                if dist1img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist1img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist1img_2.tStop = t  # not accounting for scr refresh
                        dist1img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist1img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist1img_2.stopped')
                        # update status
                        dist1img_2.status = FINISHED
                        dist1img_2.setAutoDraw(False)
                
                # *dist2img_2* updates
                
                # if dist2img_2 is starting this frame...
                if dist2img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist2img_2.frameNStart = frameN  # exact frame index
                    dist2img_2.tStart = t  # local t and not account for scr refresh
                    dist2img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist2img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist2img_2.started')
                    # update status
                    dist2img_2.status = STARTED
                    dist2img_2.setAutoDraw(True)
                
                # if dist2img_2 is active this frame...
                if dist2img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist2img_2 is stopping this frame...
                if dist2img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist2img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist2img_2.tStop = t  # not accounting for scr refresh
                        dist2img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist2img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist2img_2.stopped')
                        # update status
                        dist2img_2.status = FINISHED
                        dist2img_2.setAutoDraw(False)
                
                # *dist3img_2* updates
                
                # if dist3img_2 is starting this frame...
                if dist3img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist3img_2.frameNStart = frameN  # exact frame index
                    dist3img_2.tStart = t  # local t and not account for scr refresh
                    dist3img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist3img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist3img_2.started')
                    # update status
                    dist3img_2.status = STARTED
                    dist3img_2.setAutoDraw(True)
                
                # if dist3img_2 is active this frame...
                if dist3img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist3img_2 is stopping this frame...
                if dist3img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist3img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist3img_2.tStop = t  # not accounting for scr refresh
                        dist3img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist3img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist3img_2.stopped')
                        # update status
                        dist3img_2.status = FINISHED
                        dist3img_2.setAutoDraw(False)
                
                # *dist4img_2* updates
                
                # if dist4img_2 is starting this frame...
                if dist4img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist4img_2.frameNStart = frameN  # exact frame index
                    dist4img_2.tStart = t  # local t and not account for scr refresh
                    dist4img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist4img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist4img_2.started')
                    # update status
                    dist4img_2.status = STARTED
                    dist4img_2.setAutoDraw(True)
                
                # if dist4img_2 is active this frame...
                if dist4img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist4img_2 is stopping this frame...
                if dist4img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist4img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist4img_2.tStop = t  # not accounting for scr refresh
                        dist4img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist4img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist4img_2.stopped')
                        # update status
                        dist4img_2.status = FINISHED
                        dist4img_2.setAutoDraw(False)
                
                # *dist5img_2* updates
                
                # if dist5img_2 is starting this frame...
                if dist5img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist5img_2.frameNStart = frameN  # exact frame index
                    dist5img_2.tStart = t  # local t and not account for scr refresh
                    dist5img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist5img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist5img_2.started')
                    # update status
                    dist5img_2.status = STARTED
                    dist5img_2.setAutoDraw(True)
                
                # if dist5img_2 is active this frame...
                if dist5img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist5img_2 is stopping this frame...
                if dist5img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist5img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist5img_2.tStop = t  # not accounting for scr refresh
                        dist5img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist5img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist5img_2.stopped')
                        # update status
                        dist5img_2.status = FINISHED
                        dist5img_2.setAutoDraw(False)
                
                # *dist6img_2* updates
                
                # if dist6img_2 is starting this frame...
                if dist6img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist6img_2.frameNStart = frameN  # exact frame index
                    dist6img_2.tStart = t  # local t and not account for scr refresh
                    dist6img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist6img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist6img_2.started')
                    # update status
                    dist6img_2.status = STARTED
                    dist6img_2.setAutoDraw(True)
                
                # if dist6img_2 is active this frame...
                if dist6img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist6img_2 is stopping this frame...
                if dist6img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist6img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist6img_2.tStop = t  # not accounting for scr refresh
                        dist6img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist6img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist6img_2.stopped')
                        # update status
                        dist6img_2.status = FINISHED
                        dist6img_2.setAutoDraw(False)
                
                # *dist7img_2* updates
                
                # if dist7img_2 is starting this frame...
                if dist7img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist7img_2.frameNStart = frameN  # exact frame index
                    dist7img_2.tStart = t  # local t and not account for scr refresh
                    dist7img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist7img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist7img_2.started')
                    # update status
                    dist7img_2.status = STARTED
                    dist7img_2.setAutoDraw(True)
                
                # if dist7img_2 is active this frame...
                if dist7img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist7img_2 is stopping this frame...
                if dist7img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist7img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist7img_2.tStop = t  # not accounting for scr refresh
                        dist7img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist7img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist7img_2.stopped')
                        # update status
                        dist7img_2.status = FINISHED
                        dist7img_2.setAutoDraw(False)
                
                # *dist8img_2* updates
                
                # if dist8img_2 is starting this frame...
                if dist8img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist8img_2.frameNStart = frameN  # exact frame index
                    dist8img_2.tStart = t  # local t and not account for scr refresh
                    dist8img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist8img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist8img_2.started')
                    # update status
                    dist8img_2.status = STARTED
                    dist8img_2.setAutoDraw(True)
                
                # if dist8img_2 is active this frame...
                if dist8img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist8img_2 is stopping this frame...
                if dist8img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist8img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist8img_2.tStop = t  # not accounting for scr refresh
                        dist8img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist8img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist8img_2.stopped')
                        # update status
                        dist8img_2.status = FINISHED
                        dist8img_2.setAutoDraw(False)
                
                # *dist9img_2* updates
                
                # if dist9img_2 is starting this frame...
                if dist9img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist9img_2.frameNStart = frameN  # exact frame index
                    dist9img_2.tStart = t  # local t and not account for scr refresh
                    dist9img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist9img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist9img_2.started')
                    # update status
                    dist9img_2.status = STARTED
                    dist9img_2.setAutoDraw(True)
                
                # if dist9img_2 is active this frame...
                if dist9img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist9img_2 is stopping this frame...
                if dist9img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist9img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist9img_2.tStop = t  # not accounting for scr refresh
                        dist9img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist9img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist9img_2.stopped')
                        # update status
                        dist9img_2.status = FINISHED
                        dist9img_2.setAutoDraw(False)
                
                # *dist10img_2* updates
                
                # if dist10img_2 is starting this frame...
                if dist10img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist10img_2.frameNStart = frameN  # exact frame index
                    dist10img_2.tStart = t  # local t and not account for scr refresh
                    dist10img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist10img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist10img_2.started')
                    # update status
                    dist10img_2.status = STARTED
                    dist10img_2.setAutoDraw(True)
                
                # if dist10img_2 is active this frame...
                if dist10img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist10img_2 is stopping this frame...
                if dist10img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist10img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist10img_2.tStop = t  # not accounting for scr refresh
                        dist10img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist10img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist10img_2.stopped')
                        # update status
                        dist10img_2.status = FINISHED
                        dist10img_2.setAutoDraw(False)
                
                # *dist11img_2* updates
                
                # if dist11img_2 is starting this frame...
                if dist11img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist11img_2.frameNStart = frameN  # exact frame index
                    dist11img_2.tStart = t  # local t and not account for scr refresh
                    dist11img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist11img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist11img_2.started')
                    # update status
                    dist11img_2.status = STARTED
                    dist11img_2.setAutoDraw(True)
                
                # if dist11img_2 is active this frame...
                if dist11img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist11img_2 is stopping this frame...
                if dist11img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist11img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist11img_2.tStop = t  # not accounting for scr refresh
                        dist11img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist11img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist11img_2.stopped')
                        # update status
                        dist11img_2.status = FINISHED
                        dist11img_2.setAutoDraw(False)
                
                # *dist12img_2* updates
                
                # if dist12img_2 is starting this frame...
                if dist12img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist12img_2.frameNStart = frameN  # exact frame index
                    dist12img_2.tStart = t  # local t and not account for scr refresh
                    dist12img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist12img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist12img_2.started')
                    # update status
                    dist12img_2.status = STARTED
                    dist12img_2.setAutoDraw(True)
                
                # if dist12img_2 is active this frame...
                if dist12img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist12img_2 is stopping this frame...
                if dist12img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist12img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist12img_2.tStop = t  # not accounting for scr refresh
                        dist12img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist12img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist12img_2.stopped')
                        # update status
                        dist12img_2.status = FINISHED
                        dist12img_2.setAutoDraw(False)
                
                # *Response_2* updates
                waitOnFlip = False
                
                # if Response_2 is starting this frame...
                if Response_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    Response_2.frameNStart = frameN  # exact frame index
                    Response_2.tStart = t  # local t and not account for scr refresh
                    Response_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Response_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Response_2.started')
                    # update status
                    Response_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Response_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Response_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if Response_2 is stopping this frame...
                if Response_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Response_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        Response_2.tStop = t  # not accounting for scr refresh
                        Response_2.tStopRefresh = tThisFlipGlobal  # on global time
                        Response_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Response_2.stopped')
                        # update status
                        Response_2.status = FINISHED
                        Response_2.status = FINISHED
                if Response_2.status == STARTED and not waitOnFlip:
                    theseKeys = Response_2.getKeys(keyList=['p','a'], ignoreKeys=["escape"], waitRelease=False)
                    _Response_2_allKeys.extend(theseKeys)
                    if len(_Response_2_allKeys):
                        Response_2.keys = _Response_2_allKeys[0].name  # just the first key pressed
                        Response_2.rt = _Response_2_allKeys[0].rt
                        Response_2.duration = _Response_2_allKeys[0].duration
                        # was this correct?
                        if (Response_2.keys == str(correctAnswer)) or (Response_2.keys == correctAnswer):
                            Response_2.corr = 1
                        else:
                            Response_2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    both_trials.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in both_trials.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "both_trials" ---
            for thisComponent in both_trials.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for both_trials
            both_trials.tStop = globalClock.getTime(format='float')
            both_trials.tStopRefresh = tThisFlipGlobal
            thisExp.addData('both_trials.stopped', both_trials.tStop)
            # check responses
            if Response_2.keys in ['', [], None]:  # No response was made
                Response_2.keys = None
                # was no response the correct answer?!
                if str(correctAnswer).lower() == 'none':
                   Response_2.corr = 1;  # correct non-response
                else:
                   Response_2.corr = 0;  # failed to respond (incorrectly)
            # store data for prac (TrialHandler)
            prac.addData('Response_2.keys',Response_2.keys)
            prac.addData('Response_2.corr', Response_2.corr)
            if Response_2.keys != None:  # we had a response
                prac.addData('Response_2.rt', Response_2.rt)
                prac.addData('Response_2.duration', Response_2.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if both_trials.maxDurationReached:
                routineTimer.addTime(-both_trials.maxDuration)
            elif both_trials.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-4.500000)
            
            # --- Prepare to start Routine "feedback" ---
            # create an object to store info about Routine feedback
            feedback = data.Routine(
                name='feedback',
                components=[fd],
            )
            feedback.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from exclude_5
            if consent.rating == 2:
                continueRoutine = False
            # Run 'Begin Routine' code from feedback_display
            correctness = response_time = None
            
            #if trialver == 0:
            #    correctness = Response_E.corr
            #    response_time = Response_E.rt
            #else:
            #    correctness = Response.corr
            #    response_time = Response.rt
            
            correctness = Response_2.corr
            response_time = Response_2.rt
            
            # Check if the response is correct (1 in the data file)
            if correctness == 1:
                # End the routine if response is correct, so feedback is not displayed
                continueRoutine = False
            
            if isinstance(response_time, list): # response time returns an empty list if user is too slow
                fd.text = "Too Slow"
            else:
                fd.text = "Incorrect"
            # store start times for feedback
            feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            feedback.tStart = globalClock.getTime(format='float')
            feedback.status = STARTED
            thisExp.addData('feedback.started', feedback.tStart)
            feedback.maxDuration = None
            # keep track of which components have finished
            feedbackComponents = feedback.components
            for thisComponent in feedback.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "feedback" ---
            # if trial has changed, end Routine now
            if isinstance(prac, data.TrialHandler2) and thisPrac.thisN != prac.thisTrial.thisN:
                continueRoutine = False
            feedback.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fd* updates
                
                # if fd is starting this frame...
                if fd.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    fd.frameNStart = frameN  # exact frame index
                    fd.tStart = t  # local t and not account for scr refresh
                    fd.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fd, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fd.started')
                    # update status
                    fd.status = STARTED
                    fd.setAutoDraw(True)
                
                # if fd is active this frame...
                if fd.status == STARTED:
                    # update params
                    pass
                
                # if fd is stopping this frame...
                if fd.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fd.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fd.tStop = t  # not accounting for scr refresh
                        fd.tStopRefresh = tThisFlipGlobal  # on global time
                        fd.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fd.stopped')
                        # update status
                        fd.status = FINISHED
                        fd.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    feedback.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedback.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback" ---
            for thisComponent in feedback.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for feedback
            feedback.tStop = globalClock.getTime(format='float')
            feedback.tStopRefresh = tThisFlipGlobal
            thisExp.addData('feedback.stopped', feedback.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if feedback.maxDurationReached:
                routineTimer.addTime(-feedback.maxDuration)
            elif feedback.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'prac'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        trial_48 = data.TrialHandler2(
            name='trial_48',
            nReps=1.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('resources/trialConditions_48.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(trial_48)  # add the loop to the experiment
        thisTrial_48 = trial_48.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_48.rgb)
        if thisTrial_48 != None:
            for paramName in thisTrial_48:
                globals()[paramName] = thisTrial_48[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial_48 in trial_48:
            currentLoop = trial_48
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_48.rgb)
            if thisTrial_48 != None:
                for paramName in thisTrial_48:
                    globals()[paramName] = thisTrial_48[paramName]
            
            # --- Prepare to start Routine "both_trials" ---
            # create an object to store info about Routine both_trials
            both_trials = data.Routine(
                name='both_trials',
                components=[fixation_3, targetRV_2, dist1img_2, dist2img_2, dist3img_2, dist4img_2, dist5img_2, dist6img_2, dist7img_2, dist8img_2, dist9img_2, dist10img_2, dist11img_2, dist12img_2, Response_2],
            )
            both_trials.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from exclude_4
            if consent.rating == 2:
                continueRoutine = False
            # Run 'Begin Routine' code from randomize_position_2
            #define array for stimuli:
            x_pos_Top = [-450, -150, 150, 450]
            x_pos_Mid = [-450, -150, 150, 450]
            x_pos_Bot = [-450, -150, 150, 450]
            y_pos_fix = [-300, 0, 300]
            
            #randomize stimulus position
            if setSize == 6:
                x_pos_Top = [-150, 150]
                x_pos_Mid = [-150, 150]
                x_pos_Bot = [-150, 150]
                shuffle (x_pos_Top)
                shuffle (x_pos_Mid)
                shuffle (x_pos_Bot)
                for x in range(2):
                    x_pos_Top.append(0)
                    x_pos_Mid.append(0)
                    x_pos_Bot.append(0)
            else:
                x_pos_Top = [-450, -150, 150, 450]
                x_pos_Mid = [-450, -150, 150, 450]
                x_pos_Bot = [-450, -150, 150, 450]
                shuffle (x_pos_Top)
                shuffle (x_pos_Mid)
                shuffle (x_pos_Bot)
            
            jitter_1 = random.randint(-45, 45)
            jitter_2 = random.randint(-45, 45)
            jitter_3 = random.randint(-45, 45)
            jitter_4 = random.randint(-45, 45)
            jitter_5 = random.randint(-45, 45)
            jitter_6 = random.randint(-45, 45)
            jitter_7 = random.randint(-45, 45)
            jitter_8 = random.randint(-45, 45)
            jitter_9 = random.randint(-45, 45)
            jitter_10 = random.randint(-45, 45)
            jitter_11 = random.randint(-45, 45)
            jitter_12 = random.randint(-45, 45)
            jitter_13 = random.randint(-45, 45)
            jitter_14 = random.randint(-45, 45)
            jitter_15 = random.randint(-45, 45)
            jitter_16 = random.randint(-45, 45)
            jitter_17 = random.randint(-45, 45)
            jitter_18 = random.randint(-45, 45)
            jitter_19 = random.randint(-45, 45)
            jitter_20 = random.randint(-45, 45)
            jitter_21 = random.randint(-45, 45)
            jitter_22 = random.randint(-45, 45)
            jitter_23 = random.randint(-45, 45)
            jitter_24 = random.randint(-45, 45)
            # Run 'Begin Routine' code from position_vars_2
            dist1_pos = [x_pos_Top[0] + jitter_1, y_pos_fix[2] + jitter_2]
            dist2_pos = [x_pos_Mid[0] + jitter_3, y_pos_fix[1] + jitter_4]
            dist3_pos = [x_pos_Bot[0] + jitter_5, y_pos_fix[0] + jitter_6]
            dist4_pos = [x_pos_Top[1] + jitter_7, y_pos_fix[2] + jitter_8]
            dist5_pos = [x_pos_Mid[1] + jitter_9, y_pos_fix[1] + jitter_10]
            dist6_pos = [x_pos_Bot[1] + jitter_11, y_pos_fix[0] + jitter_12]
            dist7_pos = [x_pos_Top[2] + jitter_13, y_pos_fix[2] + jitter_14]
            dist8_pos = [x_pos_Mid[2] + jitter_15, y_pos_fix[1] + jitter_16]
            dist9_pos = [x_pos_Bot[2] + jitter_17, y_pos_fix[0] + jitter_18]
            dist10_pos = [x_pos_Top[3] + jitter_19, y_pos_fix[2] + jitter_20]
            dist11_pos = [x_pos_Mid[3] + jitter_21, y_pos_fix[1] + jitter_22]
            dist12_pos = [x_pos_Bot[3] + jitter_23, y_pos_fix[0] + jitter_24]
            
            #position, no jitter
            O_dist1_pos = [x_pos_Top[0], y_pos_fix[2]]
            O_dist2_pos = [x_pos_Mid[0], y_pos_fix[1]]
            O_dist3_pos = [x_pos_Bot[0], y_pos_fix[0]]
            O_dist4_pos = [x_pos_Top[1], y_pos_fix[2]]
            O_dist5_pos = [x_pos_Mid[1], y_pos_fix[1]]
            O_dist6_pos = [x_pos_Bot[1], y_pos_fix[0]]
            O_dist7_pos = [x_pos_Top[2], y_pos_fix[2]]
            O_dist8_pos = [x_pos_Mid[2], y_pos_fix[1]]
            O_dist9_pos = [x_pos_Bot[2], y_pos_fix[0]]
            O_dist10_pos = [x_pos_Top[3], y_pos_fix[2]]
            O_dist11_pos = [x_pos_Mid[3], y_pos_fix[1]]
            O_dist12_pos = [x_pos_Bot[3], y_pos_fix[0]]
            O_target_pos = [targetPos_X,targetPos_Y]
            # Run 'Begin Routine' code from img_set
            targetFile = 'resources/RV.png'
            
            FileSet_1 = 'resources/GV.png'
            FileSet_2 = 'resources/GV.png'
            
            size_conj = [25, 100]
            
            if trialver == 'conjuction':
                FileSet_1 = 'resources/RH.png'
                size_conj = [100, 25]
            
            targetRV_2.setOpacity(targetopacity)
            targetRV_2.setPos([0, 0])
            targetRV_2.setImage(targetFile)
            dist1img_2.setOpacity(opacity_1)
            dist1img_2.setPos(dist1_pos)
            dist1img_2.setSize(size_conj)
            dist1img_2.setImage(FileSet_1)
            dist2img_2.setOpacity(opacity_2)
            dist2img_2.setPos(dist2_pos)
            dist2img_2.setSize(size_conj)
            dist2img_2.setImage(FileSet_1)
            dist3img_2.setOpacity(opacity_3)
            dist3img_2.setPos(dist3_pos)
            dist3img_2.setSize(size_conj)
            dist3img_2.setImage(FileSet_1)
            dist4img_2.setOpacity(opacity_4)
            dist4img_2.setPos(dist4_pos)
            dist4img_2.setSize([25, 100])
            dist4img_2.setImage(FileSet_2)
            dist5img_2.setOpacity(opacity_5)
            dist5img_2.setPos(dist5_pos)
            dist5img_2.setSize([25, 100])
            dist5img_2.setImage(FileSet_2)
            dist6img_2.setOpacity(opacity_6)
            dist6img_2.setPos(dist6_pos)
            dist6img_2.setSize([25, 100])
            dist6img_2.setImage(FileSet_2)
            dist7img_2.setOpacity(opacity_7)
            dist7img_2.setPos(dist7_pos)
            dist7img_2.setSize(size_conj)
            dist7img_2.setImage(FileSet_1)
            dist8img_2.setOpacity(opacity_8)
            dist8img_2.setPos(dist8_pos)
            dist8img_2.setSize(size_conj)
            dist8img_2.setImage(FileSet_1)
            dist9img_2.setOpacity(opacity_9)
            dist9img_2.setPos(dist9_pos)
            dist9img_2.setSize(size_conj)
            dist9img_2.setImage(FileSet_1)
            dist10img_2.setOpacity(opacity_10)
            dist10img_2.setPos(dist10_pos)
            dist10img_2.setSize([25, 100])
            dist10img_2.setImage(FileSet_2)
            dist11img_2.setOpacity(opacity_11)
            dist11img_2.setPos(dist11_pos)
            dist11img_2.setSize([25, 100])
            dist11img_2.setImage(FileSet_2)
            dist12img_2.setOpacity(opacity_12)
            dist12img_2.setPos(dist12_pos)
            dist12img_2.setSize([25, 100])
            dist12img_2.setImage(FileSet_2)
            # Run 'Begin Routine' code from replace_2
            # Remove the distractor for trials where target is present
            distractors = [dist1img_2, dist2img_2, dist3img_2, dist4img_2, dist5img_2, dist6img_2, dist7img_2, dist8img_2, dist9img_2, dist10img_2, dist11img_2, dist12img_2]
            dists_pos = [O_dist1_pos, O_dist2_pos, O_dist3_pos, O_dist4_pos, O_dist5_pos, O_dist6_pos, O_dist7_pos, O_dist8_pos, O_dist9_pos, O_dist10_pos, O_dist11_pos, O_dist12_pos]
            
            if setSize == 6:
                distractors = [dist1img_2, dist2img_2, dist3img_2, dist4img_2, dist5img_2, dist6img_2]
                dists_pos = [O_dist1_pos, O_dist2_pos, O_dist3_pos, O_dist4_pos, O_dist5_pos, O_dist6_pos]
            
            target_opacity = targetopacity
            target_present = (target_opacity == 1)
            
            # Only for trials where the target is present is one distractor removed.
            if target_present:
                for idx in range(len(dists_pos)):
                    if dists_pos[idx] == O_target_pos:
                        distractors[idx].opacity = 0
                        targetRV_2.pos = distractors[idx].pos
                        break
            # create starting attributes for Response_2
            Response_2.keys = []
            Response_2.rt = []
            _Response_2_allKeys = []
            # store start times for both_trials
            both_trials.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            both_trials.tStart = globalClock.getTime(format='float')
            both_trials.status = STARTED
            thisExp.addData('both_trials.started', both_trials.tStart)
            both_trials.maxDuration = None
            # keep track of which components have finished
            both_trialsComponents = both_trials.components
            for thisComponent in both_trials.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "both_trials" ---
            # if trial has changed, end Routine now
            if isinstance(trial_48, data.TrialHandler2) and thisTrial_48.thisN != trial_48.thisTrial.thisN:
                continueRoutine = False
            both_trials.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 4.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_3* updates
                
                # if fixation_3 is starting this frame...
                if fixation_3.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_3.frameNStart = frameN  # exact frame index
                    fixation_3.tStart = t  # local t and not account for scr refresh
                    fixation_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_3.started')
                    # update status
                    fixation_3.status = STARTED
                    fixation_3.setAutoDraw(True)
                
                # if fixation_3 is active this frame...
                if fixation_3.status == STARTED:
                    # update params
                    pass
                
                # if fixation_3 is stopping this frame...
                if fixation_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_3.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_3.tStop = t  # not accounting for scr refresh
                        fixation_3.tStopRefresh = tThisFlipGlobal  # on global time
                        fixation_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_3.stopped')
                        # update status
                        fixation_3.status = FINISHED
                        fixation_3.setAutoDraw(False)
                
                # *targetRV_2* updates
                
                # if targetRV_2 is starting this frame...
                if targetRV_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    targetRV_2.frameNStart = frameN  # exact frame index
                    targetRV_2.tStart = t  # local t and not account for scr refresh
                    targetRV_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(targetRV_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'targetRV_2.started')
                    # update status
                    targetRV_2.status = STARTED
                    targetRV_2.setAutoDraw(True)
                
                # if targetRV_2 is active this frame...
                if targetRV_2.status == STARTED:
                    # update params
                    pass
                
                # if targetRV_2 is stopping this frame...
                if targetRV_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > targetRV_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        targetRV_2.tStop = t  # not accounting for scr refresh
                        targetRV_2.tStopRefresh = tThisFlipGlobal  # on global time
                        targetRV_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'targetRV_2.stopped')
                        # update status
                        targetRV_2.status = FINISHED
                        targetRV_2.setAutoDraw(False)
                
                # *dist1img_2* updates
                
                # if dist1img_2 is starting this frame...
                if dist1img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist1img_2.frameNStart = frameN  # exact frame index
                    dist1img_2.tStart = t  # local t and not account for scr refresh
                    dist1img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist1img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist1img_2.started')
                    # update status
                    dist1img_2.status = STARTED
                    dist1img_2.setAutoDraw(True)
                
                # if dist1img_2 is active this frame...
                if dist1img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist1img_2 is stopping this frame...
                if dist1img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist1img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist1img_2.tStop = t  # not accounting for scr refresh
                        dist1img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist1img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist1img_2.stopped')
                        # update status
                        dist1img_2.status = FINISHED
                        dist1img_2.setAutoDraw(False)
                
                # *dist2img_2* updates
                
                # if dist2img_2 is starting this frame...
                if dist2img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist2img_2.frameNStart = frameN  # exact frame index
                    dist2img_2.tStart = t  # local t and not account for scr refresh
                    dist2img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist2img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist2img_2.started')
                    # update status
                    dist2img_2.status = STARTED
                    dist2img_2.setAutoDraw(True)
                
                # if dist2img_2 is active this frame...
                if dist2img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist2img_2 is stopping this frame...
                if dist2img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist2img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist2img_2.tStop = t  # not accounting for scr refresh
                        dist2img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist2img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist2img_2.stopped')
                        # update status
                        dist2img_2.status = FINISHED
                        dist2img_2.setAutoDraw(False)
                
                # *dist3img_2* updates
                
                # if dist3img_2 is starting this frame...
                if dist3img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist3img_2.frameNStart = frameN  # exact frame index
                    dist3img_2.tStart = t  # local t and not account for scr refresh
                    dist3img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist3img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist3img_2.started')
                    # update status
                    dist3img_2.status = STARTED
                    dist3img_2.setAutoDraw(True)
                
                # if dist3img_2 is active this frame...
                if dist3img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist3img_2 is stopping this frame...
                if dist3img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist3img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist3img_2.tStop = t  # not accounting for scr refresh
                        dist3img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist3img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist3img_2.stopped')
                        # update status
                        dist3img_2.status = FINISHED
                        dist3img_2.setAutoDraw(False)
                
                # *dist4img_2* updates
                
                # if dist4img_2 is starting this frame...
                if dist4img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist4img_2.frameNStart = frameN  # exact frame index
                    dist4img_2.tStart = t  # local t and not account for scr refresh
                    dist4img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist4img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist4img_2.started')
                    # update status
                    dist4img_2.status = STARTED
                    dist4img_2.setAutoDraw(True)
                
                # if dist4img_2 is active this frame...
                if dist4img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist4img_2 is stopping this frame...
                if dist4img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist4img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist4img_2.tStop = t  # not accounting for scr refresh
                        dist4img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist4img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist4img_2.stopped')
                        # update status
                        dist4img_2.status = FINISHED
                        dist4img_2.setAutoDraw(False)
                
                # *dist5img_2* updates
                
                # if dist5img_2 is starting this frame...
                if dist5img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist5img_2.frameNStart = frameN  # exact frame index
                    dist5img_2.tStart = t  # local t and not account for scr refresh
                    dist5img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist5img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist5img_2.started')
                    # update status
                    dist5img_2.status = STARTED
                    dist5img_2.setAutoDraw(True)
                
                # if dist5img_2 is active this frame...
                if dist5img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist5img_2 is stopping this frame...
                if dist5img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist5img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist5img_2.tStop = t  # not accounting for scr refresh
                        dist5img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist5img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist5img_2.stopped')
                        # update status
                        dist5img_2.status = FINISHED
                        dist5img_2.setAutoDraw(False)
                
                # *dist6img_2* updates
                
                # if dist6img_2 is starting this frame...
                if dist6img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist6img_2.frameNStart = frameN  # exact frame index
                    dist6img_2.tStart = t  # local t and not account for scr refresh
                    dist6img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist6img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist6img_2.started')
                    # update status
                    dist6img_2.status = STARTED
                    dist6img_2.setAutoDraw(True)
                
                # if dist6img_2 is active this frame...
                if dist6img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist6img_2 is stopping this frame...
                if dist6img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist6img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist6img_2.tStop = t  # not accounting for scr refresh
                        dist6img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist6img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist6img_2.stopped')
                        # update status
                        dist6img_2.status = FINISHED
                        dist6img_2.setAutoDraw(False)
                
                # *dist7img_2* updates
                
                # if dist7img_2 is starting this frame...
                if dist7img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist7img_2.frameNStart = frameN  # exact frame index
                    dist7img_2.tStart = t  # local t and not account for scr refresh
                    dist7img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist7img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist7img_2.started')
                    # update status
                    dist7img_2.status = STARTED
                    dist7img_2.setAutoDraw(True)
                
                # if dist7img_2 is active this frame...
                if dist7img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist7img_2 is stopping this frame...
                if dist7img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist7img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist7img_2.tStop = t  # not accounting for scr refresh
                        dist7img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist7img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist7img_2.stopped')
                        # update status
                        dist7img_2.status = FINISHED
                        dist7img_2.setAutoDraw(False)
                
                # *dist8img_2* updates
                
                # if dist8img_2 is starting this frame...
                if dist8img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist8img_2.frameNStart = frameN  # exact frame index
                    dist8img_2.tStart = t  # local t and not account for scr refresh
                    dist8img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist8img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist8img_2.started')
                    # update status
                    dist8img_2.status = STARTED
                    dist8img_2.setAutoDraw(True)
                
                # if dist8img_2 is active this frame...
                if dist8img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist8img_2 is stopping this frame...
                if dist8img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist8img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist8img_2.tStop = t  # not accounting for scr refresh
                        dist8img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist8img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist8img_2.stopped')
                        # update status
                        dist8img_2.status = FINISHED
                        dist8img_2.setAutoDraw(False)
                
                # *dist9img_2* updates
                
                # if dist9img_2 is starting this frame...
                if dist9img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist9img_2.frameNStart = frameN  # exact frame index
                    dist9img_2.tStart = t  # local t and not account for scr refresh
                    dist9img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist9img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist9img_2.started')
                    # update status
                    dist9img_2.status = STARTED
                    dist9img_2.setAutoDraw(True)
                
                # if dist9img_2 is active this frame...
                if dist9img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist9img_2 is stopping this frame...
                if dist9img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist9img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist9img_2.tStop = t  # not accounting for scr refresh
                        dist9img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist9img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist9img_2.stopped')
                        # update status
                        dist9img_2.status = FINISHED
                        dist9img_2.setAutoDraw(False)
                
                # *dist10img_2* updates
                
                # if dist10img_2 is starting this frame...
                if dist10img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist10img_2.frameNStart = frameN  # exact frame index
                    dist10img_2.tStart = t  # local t and not account for scr refresh
                    dist10img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist10img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist10img_2.started')
                    # update status
                    dist10img_2.status = STARTED
                    dist10img_2.setAutoDraw(True)
                
                # if dist10img_2 is active this frame...
                if dist10img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist10img_2 is stopping this frame...
                if dist10img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist10img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist10img_2.tStop = t  # not accounting for scr refresh
                        dist10img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist10img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist10img_2.stopped')
                        # update status
                        dist10img_2.status = FINISHED
                        dist10img_2.setAutoDraw(False)
                
                # *dist11img_2* updates
                
                # if dist11img_2 is starting this frame...
                if dist11img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist11img_2.frameNStart = frameN  # exact frame index
                    dist11img_2.tStart = t  # local t and not account for scr refresh
                    dist11img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist11img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist11img_2.started')
                    # update status
                    dist11img_2.status = STARTED
                    dist11img_2.setAutoDraw(True)
                
                # if dist11img_2 is active this frame...
                if dist11img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist11img_2 is stopping this frame...
                if dist11img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist11img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist11img_2.tStop = t  # not accounting for scr refresh
                        dist11img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist11img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist11img_2.stopped')
                        # update status
                        dist11img_2.status = FINISHED
                        dist11img_2.setAutoDraw(False)
                
                # *dist12img_2* updates
                
                # if dist12img_2 is starting this frame...
                if dist12img_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    dist12img_2.frameNStart = frameN  # exact frame index
                    dist12img_2.tStart = t  # local t and not account for scr refresh
                    dist12img_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(dist12img_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist12img_2.started')
                    # update status
                    dist12img_2.status = STARTED
                    dist12img_2.setAutoDraw(True)
                
                # if dist12img_2 is active this frame...
                if dist12img_2.status == STARTED:
                    # update params
                    pass
                
                # if dist12img_2 is stopping this frame...
                if dist12img_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > dist12img_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        dist12img_2.tStop = t  # not accounting for scr refresh
                        dist12img_2.tStopRefresh = tThisFlipGlobal  # on global time
                        dist12img_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist12img_2.stopped')
                        # update status
                        dist12img_2.status = FINISHED
                        dist12img_2.setAutoDraw(False)
                
                # *Response_2* updates
                waitOnFlip = False
                
                # if Response_2 is starting this frame...
                if Response_2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                    # keep track of start time/frame for later
                    Response_2.frameNStart = frameN  # exact frame index
                    Response_2.tStart = t  # local t and not account for scr refresh
                    Response_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Response_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Response_2.started')
                    # update status
                    Response_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Response_2.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Response_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if Response_2 is stopping this frame...
                if Response_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Response_2.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        Response_2.tStop = t  # not accounting for scr refresh
                        Response_2.tStopRefresh = tThisFlipGlobal  # on global time
                        Response_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Response_2.stopped')
                        # update status
                        Response_2.status = FINISHED
                        Response_2.status = FINISHED
                if Response_2.status == STARTED and not waitOnFlip:
                    theseKeys = Response_2.getKeys(keyList=['p','a'], ignoreKeys=["escape"], waitRelease=False)
                    _Response_2_allKeys.extend(theseKeys)
                    if len(_Response_2_allKeys):
                        Response_2.keys = _Response_2_allKeys[0].name  # just the first key pressed
                        Response_2.rt = _Response_2_allKeys[0].rt
                        Response_2.duration = _Response_2_allKeys[0].duration
                        # was this correct?
                        if (Response_2.keys == str(correctAnswer)) or (Response_2.keys == correctAnswer):
                            Response_2.corr = 1
                        else:
                            Response_2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    both_trials.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in both_trials.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "both_trials" ---
            for thisComponent in both_trials.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for both_trials
            both_trials.tStop = globalClock.getTime(format='float')
            both_trials.tStopRefresh = tThisFlipGlobal
            thisExp.addData('both_trials.stopped', both_trials.tStop)
            # check responses
            if Response_2.keys in ['', [], None]:  # No response was made
                Response_2.keys = None
                # was no response the correct answer?!
                if str(correctAnswer).lower() == 'none':
                   Response_2.corr = 1;  # correct non-response
                else:
                   Response_2.corr = 0;  # failed to respond (incorrectly)
            # store data for trial_48 (TrialHandler)
            trial_48.addData('Response_2.keys',Response_2.keys)
            trial_48.addData('Response_2.corr', Response_2.corr)
            if Response_2.keys != None:  # we had a response
                trial_48.addData('Response_2.rt', Response_2.rt)
                trial_48.addData('Response_2.duration', Response_2.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if both_trials.maxDurationReached:
                routineTimer.addTime(-both_trials.maxDuration)
            elif both_trials.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-4.500000)
            
            # --- Prepare to start Routine "feedback" ---
            # create an object to store info about Routine feedback
            feedback = data.Routine(
                name='feedback',
                components=[fd],
            )
            feedback.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from exclude_5
            if consent.rating == 2:
                continueRoutine = False
            # Run 'Begin Routine' code from feedback_display
            correctness = response_time = None
            
            #if trialver == 0:
            #    correctness = Response_E.corr
            #    response_time = Response_E.rt
            #else:
            #    correctness = Response.corr
            #    response_time = Response.rt
            
            correctness = Response_2.corr
            response_time = Response_2.rt
            
            # Check if the response is correct (1 in the data file)
            if correctness == 1:
                # End the routine if response is correct, so feedback is not displayed
                continueRoutine = False
            
            if isinstance(response_time, list): # response time returns an empty list if user is too slow
                fd.text = "Too Slow"
            else:
                fd.text = "Incorrect"
            # store start times for feedback
            feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            feedback.tStart = globalClock.getTime(format='float')
            feedback.status = STARTED
            thisExp.addData('feedback.started', feedback.tStart)
            feedback.maxDuration = None
            # keep track of which components have finished
            feedbackComponents = feedback.components
            for thisComponent in feedback.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "feedback" ---
            # if trial has changed, end Routine now
            if isinstance(trial_48, data.TrialHandler2) and thisTrial_48.thisN != trial_48.thisTrial.thisN:
                continueRoutine = False
            feedback.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fd* updates
                
                # if fd is starting this frame...
                if fd.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    fd.frameNStart = frameN  # exact frame index
                    fd.tStart = t  # local t and not account for scr refresh
                    fd.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fd, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fd.started')
                    # update status
                    fd.status = STARTED
                    fd.setAutoDraw(True)
                
                # if fd is active this frame...
                if fd.status == STARTED:
                    # update params
                    pass
                
                # if fd is stopping this frame...
                if fd.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fd.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        fd.tStop = t  # not accounting for scr refresh
                        fd.tStopRefresh = tThisFlipGlobal  # on global time
                        fd.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fd.stopped')
                        # update status
                        fd.status = FINISHED
                        fd.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    feedback.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedback.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback" ---
            for thisComponent in feedback.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for feedback
            feedback.tStop = globalClock.getTime(format='float')
            feedback.tStopRefresh = tThisFlipGlobal
            thisExp.addData('feedback.stopped', feedback.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if feedback.maxDurationReached:
                routineTimer.addTime(-feedback.maxDuration)
            elif feedback.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trial_48'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "Rest" ---
        # create an object to store info about Routine Rest
        Rest = data.Routine(
            name='Rest',
            components=[RestText],
        )
        Rest.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from exclude_6
        if consent.rating == 2:
            continueRoutine = False
        # Run 'Begin Routine' code from code_4
        if exp_loop.thisN == 1:
            continueRoutine = False
        # store start times for Rest
        Rest.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Rest.tStart = globalClock.getTime(format='float')
        Rest.status = STARTED
        thisExp.addData('Rest.started', Rest.tStart)
        Rest.maxDuration = None
        # keep track of which components have finished
        RestComponents = Rest.components
        for thisComponent in Rest.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Rest" ---
        # if trial has changed, end Routine now
        if isinstance(exp_loop, data.TrialHandler2) and thisExp_loop.thisN != exp_loop.thisTrial.thisN:
            continueRoutine = False
        Rest.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 30.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *RestText* updates
            
            # if RestText is starting this frame...
            if RestText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                RestText.frameNStart = frameN  # exact frame index
                RestText.tStart = t  # local t and not account for scr refresh
                RestText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RestText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'RestText.started')
                # update status
                RestText.status = STARTED
                RestText.setAutoDraw(True)
            
            # if RestText is active this frame...
            if RestText.status == STARTED:
                # update params
                pass
            
            # if RestText is stopping this frame...
            if RestText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RestText.tStartRefresh + 30-frameTolerance:
                    # keep track of stop time/frame for later
                    RestText.tStop = t  # not accounting for scr refresh
                    RestText.tStopRefresh = tThisFlipGlobal  # on global time
                    RestText.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'RestText.stopped')
                    # update status
                    RestText.status = FINISHED
                    RestText.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Rest.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Rest.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Rest" ---
        for thisComponent in Rest.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Rest
        Rest.tStop = globalClock.getTime(format='float')
        Rest.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Rest.stopped', Rest.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Rest.maxDurationReached:
            routineTimer.addTime(-Rest.maxDuration)
        elif Rest.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-30.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'exp_loop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "PreMEQ" ---
    # create an object to store info about Routine PreMEQ
    PreMEQ = data.Routine(
        name='PreMEQ',
        components=[form, confirmSign_button_3, confirmSign_click_3],
    )
    PreMEQ.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from exclude_7
    if consent.rating == 2:
        continueRoutine = False
    # setup some python lists for storing info about the confirmSign_click_3
    confirmSign_click_3.x = []
    confirmSign_click_3.y = []
    confirmSign_click_3.leftButton = []
    confirmSign_click_3.midButton = []
    confirmSign_click_3.rightButton = []
    confirmSign_click_3.time = []
    confirmSign_click_3.clicked_name = []
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from showMouse_3
    win.mouseVisible = True
    # store start times for PreMEQ
    PreMEQ.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    PreMEQ.tStart = globalClock.getTime(format='float')
    PreMEQ.status = STARTED
    thisExp.addData('PreMEQ.started', PreMEQ.tStart)
    PreMEQ.maxDuration = None
    # keep track of which components have finished
    PreMEQComponents = PreMEQ.components
    for thisComponent in PreMEQ.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "PreMEQ" ---
    PreMEQ.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *form* updates
        
        # if form is starting this frame...
        if form.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            form.frameNStart = frameN  # exact frame index
            form.tStart = t  # local t and not account for scr refresh
            form.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(form, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'form.started')
            # update status
            form.status = STARTED
            form.setAutoDraw(True)
        
        # if form is active this frame...
        if form.status == STARTED:
            # update params
            pass
        
        # *confirmSign_button_3* updates
        
        # if confirmSign_button_3 is starting this frame...
        if confirmSign_button_3.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            confirmSign_button_3.frameNStart = frameN  # exact frame index
            confirmSign_button_3.tStart = t  # local t and not account for scr refresh
            confirmSign_button_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_button_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confirmSign_button_3.started')
            # update status
            confirmSign_button_3.status = STARTED
            confirmSign_button_3.setAutoDraw(True)
        
        # if confirmSign_button_3 is active this frame...
        if confirmSign_button_3.status == STARTED:
            # update params
            pass
        # *confirmSign_click_3* updates
        
        # if confirmSign_click_3 is starting this frame...
        if confirmSign_click_3.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            confirmSign_click_3.frameNStart = frameN  # exact frame index
            confirmSign_click_3.tStart = t  # local t and not account for scr refresh
            confirmSign_click_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_click_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('confirmSign_click_3.started', t)
            # update status
            confirmSign_click_3.status = STARTED
            confirmSign_click_3.mouseClock.reset()
            prevButtonState = confirmSign_click_3.getPressed()  # if button is down already this ISN'T a new click
        if confirmSign_click_3.status == STARTED:  # only update if started and not finished!
            buttons = confirmSign_click_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(confirmSign_button_3, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(confirmSign_click_3):
                            gotValidClick = True
                            confirmSign_click_3.clicked_name.append(obj.name)
                    if not gotValidClick:
                        confirmSign_click_3.clicked_name.append(None)
                    x, y = confirmSign_click_3.getPos()
                    confirmSign_click_3.x.append(x)
                    confirmSign_click_3.y.append(y)
                    buttons = confirmSign_click_3.getPressed()
                    confirmSign_click_3.leftButton.append(buttons[0])
                    confirmSign_click_3.midButton.append(buttons[1])
                    confirmSign_click_3.rightButton.append(buttons[2])
                    confirmSign_click_3.time.append(confirmSign_click_3.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            PreMEQ.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PreMEQ.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "PreMEQ" ---
    for thisComponent in PreMEQ.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for PreMEQ
    PreMEQ.tStop = globalClock.getTime(format='float')
    PreMEQ.tStopRefresh = tThisFlipGlobal
    thisExp.addData('PreMEQ.stopped', PreMEQ.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('confirmSign_click_3.x', confirmSign_click_3.x)
    thisExp.addData('confirmSign_click_3.y', confirmSign_click_3.y)
    thisExp.addData('confirmSign_click_3.leftButton', confirmSign_click_3.leftButton)
    thisExp.addData('confirmSign_click_3.midButton', confirmSign_click_3.midButton)
    thisExp.addData('confirmSign_click_3.rightButton', confirmSign_click_3.rightButton)
    thisExp.addData('confirmSign_click_3.time', confirmSign_click_3.time)
    thisExp.addData('confirmSign_click_3.clicked_name', confirmSign_click_3.clicked_name)
    thisExp.nextEntry()
    # the Routine "PreMEQ" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "bestfeel_meq" ---
    # create an object to store info about Routine bestfeel_meq
    bestfeel_meq = data.Routine(
        name='bestfeel_meq',
        components=[confirmSign_click_4, confirmSign_button_4, best_feel_Q, best_feel],
    )
    bestfeel_meq.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from exclude_8
    if consent.rating == 2:
        continueRoutine = False
    # setup some python lists for storing info about the confirmSign_click_4
    confirmSign_click_4.x = []
    confirmSign_click_4.y = []
    confirmSign_click_4.leftButton = []
    confirmSign_click_4.midButton = []
    confirmSign_click_4.rightButton = []
    confirmSign_click_4.time = []
    confirmSign_click_4.clicked_name = []
    gotValidClick = False  # until a click is received
    best_feel.reset()
    # Run 'Begin Routine' code from showMouse_4
    win.mouseVisible = True
    # store start times for bestfeel_meq
    bestfeel_meq.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    bestfeel_meq.tStart = globalClock.getTime(format='float')
    bestfeel_meq.status = STARTED
    thisExp.addData('bestfeel_meq.started', bestfeel_meq.tStart)
    bestfeel_meq.maxDuration = None
    # keep track of which components have finished
    bestfeel_meqComponents = bestfeel_meq.components
    for thisComponent in bestfeel_meq.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "bestfeel_meq" ---
    bestfeel_meq.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *confirmSign_click_4* updates
        
        # if confirmSign_click_4 is starting this frame...
        if confirmSign_click_4.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            confirmSign_click_4.frameNStart = frameN  # exact frame index
            confirmSign_click_4.tStart = t  # local t and not account for scr refresh
            confirmSign_click_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_click_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('confirmSign_click_4.started', t)
            # update status
            confirmSign_click_4.status = STARTED
            confirmSign_click_4.mouseClock.reset()
            prevButtonState = confirmSign_click_4.getPressed()  # if button is down already this ISN'T a new click
        if confirmSign_click_4.status == STARTED:  # only update if started and not finished!
            buttons = confirmSign_click_4.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(confirmSign_button_4, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(confirmSign_click_4):
                            gotValidClick = True
                            confirmSign_click_4.clicked_name.append(obj.name)
                    if not gotValidClick:
                        confirmSign_click_4.clicked_name.append(None)
                    x, y = confirmSign_click_4.getPos()
                    confirmSign_click_4.x.append(x)
                    confirmSign_click_4.y.append(y)
                    buttons = confirmSign_click_4.getPressed()
                    confirmSign_click_4.leftButton.append(buttons[0])
                    confirmSign_click_4.midButton.append(buttons[1])
                    confirmSign_click_4.rightButton.append(buttons[2])
                    confirmSign_click_4.time.append(confirmSign_click_4.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *confirmSign_button_4* updates
        
        # if confirmSign_button_4 is starting this frame...
        if confirmSign_button_4.status == NOT_STARTED and (best_feel.rating):
            # keep track of start time/frame for later
            confirmSign_button_4.frameNStart = frameN  # exact frame index
            confirmSign_button_4.tStart = t  # local t and not account for scr refresh
            confirmSign_button_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_button_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confirmSign_button_4.started')
            # update status
            confirmSign_button_4.status = STARTED
            confirmSign_button_4.setAutoDraw(True)
        
        # if confirmSign_button_4 is active this frame...
        if confirmSign_button_4.status == STARTED:
            # update params
            pass
        
        # *best_feel_Q* updates
        
        # if best_feel_Q is starting this frame...
        if best_feel_Q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            best_feel_Q.frameNStart = frameN  # exact frame index
            best_feel_Q.tStart = t  # local t and not account for scr refresh
            best_feel_Q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(best_feel_Q, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'best_feel_Q.started')
            # update status
            best_feel_Q.status = STARTED
            best_feel_Q.setAutoDraw(True)
        
        # if best_feel_Q is active this frame...
        if best_feel_Q.status == STARTED:
            # update params
            pass
        
        # *best_feel* updates
        
        # if best_feel is starting this frame...
        if best_feel.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            best_feel.frameNStart = frameN  # exact frame index
            best_feel.tStart = t  # local t and not account for scr refresh
            best_feel.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(best_feel, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'best_feel.started')
            # update status
            best_feel.status = STARTED
            best_feel.setAutoDraw(True)
        
        # if best_feel is active this frame...
        if best_feel.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            bestfeel_meq.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in bestfeel_meq.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "bestfeel_meq" ---
    for thisComponent in bestfeel_meq.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for bestfeel_meq
    bestfeel_meq.tStop = globalClock.getTime(format='float')
    bestfeel_meq.tStopRefresh = tThisFlipGlobal
    thisExp.addData('bestfeel_meq.stopped', bestfeel_meq.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('confirmSign_click_4.x', confirmSign_click_4.x)
    thisExp.addData('confirmSign_click_4.y', confirmSign_click_4.y)
    thisExp.addData('confirmSign_click_4.leftButton', confirmSign_click_4.leftButton)
    thisExp.addData('confirmSign_click_4.midButton', confirmSign_click_4.midButton)
    thisExp.addData('confirmSign_click_4.rightButton', confirmSign_click_4.rightButton)
    thisExp.addData('confirmSign_click_4.time', confirmSign_click_4.time)
    thisExp.addData('confirmSign_click_4.clicked_name', confirmSign_click_4.clicked_name)
    thisExp.addData('best_feel.response', best_feel.getRating())
    thisExp.addData('best_feel.rt', best_feel.getRT())
    thisExp.nextEntry()
    # the Routine "bestfeel_meq" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "wokentired_meq" ---
    # create an object to store info about Routine wokentired_meq
    wokentired_meq = data.Routine(
        name='wokentired_meq',
        components=[confirmSign_click_6, confirmSign_button_6, woken_tired_Q, woken_tired],
    )
    wokentired_meq.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from exclude_9
    if consent.rating == 2:
        continueRoutine = False
    # setup some python lists for storing info about the confirmSign_click_6
    confirmSign_click_6.x = []
    confirmSign_click_6.y = []
    confirmSign_click_6.leftButton = []
    confirmSign_click_6.midButton = []
    confirmSign_click_6.rightButton = []
    confirmSign_click_6.time = []
    confirmSign_click_6.clicked_name = []
    gotValidClick = False  # until a click is received
    woken_tired.reset()
    # store start times for wokentired_meq
    wokentired_meq.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    wokentired_meq.tStart = globalClock.getTime(format='float')
    wokentired_meq.status = STARTED
    thisExp.addData('wokentired_meq.started', wokentired_meq.tStart)
    wokentired_meq.maxDuration = None
    # keep track of which components have finished
    wokentired_meqComponents = wokentired_meq.components
    for thisComponent in wokentired_meq.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "wokentired_meq" ---
    wokentired_meq.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *confirmSign_click_6* updates
        
        # if confirmSign_click_6 is starting this frame...
        if confirmSign_click_6.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            confirmSign_click_6.frameNStart = frameN  # exact frame index
            confirmSign_click_6.tStart = t  # local t and not account for scr refresh
            confirmSign_click_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_click_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('confirmSign_click_6.started', t)
            # update status
            confirmSign_click_6.status = STARTED
            confirmSign_click_6.mouseClock.reset()
            prevButtonState = confirmSign_click_6.getPressed()  # if button is down already this ISN'T a new click
        if confirmSign_click_6.status == STARTED:  # only update if started and not finished!
            buttons = confirmSign_click_6.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(confirmSign_button_6, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(confirmSign_click_6):
                            gotValidClick = True
                            confirmSign_click_6.clicked_name.append(obj.name)
                    if not gotValidClick:
                        confirmSign_click_6.clicked_name.append(None)
                    x, y = confirmSign_click_6.getPos()
                    confirmSign_click_6.x.append(x)
                    confirmSign_click_6.y.append(y)
                    buttons = confirmSign_click_6.getPressed()
                    confirmSign_click_6.leftButton.append(buttons[0])
                    confirmSign_click_6.midButton.append(buttons[1])
                    confirmSign_click_6.rightButton.append(buttons[2])
                    confirmSign_click_6.time.append(confirmSign_click_6.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *confirmSign_button_6* updates
        
        # if confirmSign_button_6 is starting this frame...
        if confirmSign_button_6.status == NOT_STARTED and woken_tired.rating:
            # keep track of start time/frame for later
            confirmSign_button_6.frameNStart = frameN  # exact frame index
            confirmSign_button_6.tStart = t  # local t and not account for scr refresh
            confirmSign_button_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_button_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confirmSign_button_6.started')
            # update status
            confirmSign_button_6.status = STARTED
            confirmSign_button_6.setAutoDraw(True)
        
        # if confirmSign_button_6 is active this frame...
        if confirmSign_button_6.status == STARTED:
            # update params
            pass
        
        # *woken_tired_Q* updates
        
        # if woken_tired_Q is starting this frame...
        if woken_tired_Q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            woken_tired_Q.frameNStart = frameN  # exact frame index
            woken_tired_Q.tStart = t  # local t and not account for scr refresh
            woken_tired_Q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(woken_tired_Q, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'woken_tired_Q.started')
            # update status
            woken_tired_Q.status = STARTED
            woken_tired_Q.setAutoDraw(True)
        
        # if woken_tired_Q is active this frame...
        if woken_tired_Q.status == STARTED:
            # update params
            pass
        
        # *woken_tired* updates
        
        # if woken_tired is starting this frame...
        if woken_tired.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            woken_tired.frameNStart = frameN  # exact frame index
            woken_tired.tStart = t  # local t and not account for scr refresh
            woken_tired.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(woken_tired, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'woken_tired.started')
            # update status
            woken_tired.status = STARTED
            woken_tired.setAutoDraw(True)
        
        # if woken_tired is active this frame...
        if woken_tired.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            wokentired_meq.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in wokentired_meq.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "wokentired_meq" ---
    for thisComponent in wokentired_meq.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for wokentired_meq
    wokentired_meq.tStop = globalClock.getTime(format='float')
    wokentired_meq.tStopRefresh = tThisFlipGlobal
    thisExp.addData('wokentired_meq.stopped', wokentired_meq.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('confirmSign_click_6.x', confirmSign_click_6.x)
    thisExp.addData('confirmSign_click_6.y', confirmSign_click_6.y)
    thisExp.addData('confirmSign_click_6.leftButton', confirmSign_click_6.leftButton)
    thisExp.addData('confirmSign_click_6.midButton', confirmSign_click_6.midButton)
    thisExp.addData('confirmSign_click_6.rightButton', confirmSign_click_6.rightButton)
    thisExp.addData('confirmSign_click_6.time', confirmSign_click_6.time)
    thisExp.addData('confirmSign_click_6.clicked_name', confirmSign_click_6.clicked_name)
    thisExp.addData('woken_tired.response', woken_tired.getRating())
    thisExp.addData('woken_tired.rt', woken_tired.getRT())
    thisExp.nextEntry()
    # the Routine "wokentired_meq" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "sleepytime_meq" ---
    # create an object to store info about Routine sleepytime_meq
    sleepytime_meq = data.Routine(
        name='sleepytime_meq',
        components=[confirmSign_click_7, confirmSign_button_7, sleepy_time_Q, sleepy_time],
    )
    sleepytime_meq.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from exclude_10
    if consent.rating == 2:
        continueRoutine = False
    # setup some python lists for storing info about the confirmSign_click_7
    confirmSign_click_7.x = []
    confirmSign_click_7.y = []
    confirmSign_click_7.leftButton = []
    confirmSign_click_7.midButton = []
    confirmSign_click_7.rightButton = []
    confirmSign_click_7.time = []
    confirmSign_click_7.clicked_name = []
    gotValidClick = False  # until a click is received
    sleepy_time.reset()
    # store start times for sleepytime_meq
    sleepytime_meq.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    sleepytime_meq.tStart = globalClock.getTime(format='float')
    sleepytime_meq.status = STARTED
    thisExp.addData('sleepytime_meq.started', sleepytime_meq.tStart)
    sleepytime_meq.maxDuration = None
    # keep track of which components have finished
    sleepytime_meqComponents = sleepytime_meq.components
    for thisComponent in sleepytime_meq.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "sleepytime_meq" ---
    sleepytime_meq.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *confirmSign_click_7* updates
        
        # if confirmSign_click_7 is starting this frame...
        if confirmSign_click_7.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            confirmSign_click_7.frameNStart = frameN  # exact frame index
            confirmSign_click_7.tStart = t  # local t and not account for scr refresh
            confirmSign_click_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_click_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('confirmSign_click_7.started', t)
            # update status
            confirmSign_click_7.status = STARTED
            confirmSign_click_7.mouseClock.reset()
            prevButtonState = confirmSign_click_7.getPressed()  # if button is down already this ISN'T a new click
        if confirmSign_click_7.status == STARTED:  # only update if started and not finished!
            buttons = confirmSign_click_7.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(confirmSign_button_7, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(confirmSign_click_7):
                            gotValidClick = True
                            confirmSign_click_7.clicked_name.append(obj.name)
                    if not gotValidClick:
                        confirmSign_click_7.clicked_name.append(None)
                    x, y = confirmSign_click_7.getPos()
                    confirmSign_click_7.x.append(x)
                    confirmSign_click_7.y.append(y)
                    buttons = confirmSign_click_7.getPressed()
                    confirmSign_click_7.leftButton.append(buttons[0])
                    confirmSign_click_7.midButton.append(buttons[1])
                    confirmSign_click_7.rightButton.append(buttons[2])
                    confirmSign_click_7.time.append(confirmSign_click_7.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *confirmSign_button_7* updates
        
        # if confirmSign_button_7 is starting this frame...
        if confirmSign_button_7.status == NOT_STARTED and sleepy_time.rating:
            # keep track of start time/frame for later
            confirmSign_button_7.frameNStart = frameN  # exact frame index
            confirmSign_button_7.tStart = t  # local t and not account for scr refresh
            confirmSign_button_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_button_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confirmSign_button_7.started')
            # update status
            confirmSign_button_7.status = STARTED
            confirmSign_button_7.setAutoDraw(True)
        
        # if confirmSign_button_7 is active this frame...
        if confirmSign_button_7.status == STARTED:
            # update params
            pass
        
        # *sleepy_time_Q* updates
        
        # if sleepy_time_Q is starting this frame...
        if sleepy_time_Q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sleepy_time_Q.frameNStart = frameN  # exact frame index
            sleepy_time_Q.tStart = t  # local t and not account for scr refresh
            sleepy_time_Q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sleepy_time_Q, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sleepy_time_Q.started')
            # update status
            sleepy_time_Q.status = STARTED
            sleepy_time_Q.setAutoDraw(True)
        
        # if sleepy_time_Q is active this frame...
        if sleepy_time_Q.status == STARTED:
            # update params
            pass
        
        # *sleepy_time* updates
        
        # if sleepy_time is starting this frame...
        if sleepy_time.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sleepy_time.frameNStart = frameN  # exact frame index
            sleepy_time.tStart = t  # local t and not account for scr refresh
            sleepy_time.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sleepy_time, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sleepy_time.started')
            # update status
            sleepy_time.status = STARTED
            sleepy_time.setAutoDraw(True)
        
        # if sleepy_time is active this frame...
        if sleepy_time.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            sleepytime_meq.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sleepytime_meq.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "sleepytime_meq" ---
    for thisComponent in sleepytime_meq.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for sleepytime_meq
    sleepytime_meq.tStop = globalClock.getTime(format='float')
    sleepytime_meq.tStopRefresh = tThisFlipGlobal
    thisExp.addData('sleepytime_meq.stopped', sleepytime_meq.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('confirmSign_click_7.x', confirmSign_click_7.x)
    thisExp.addData('confirmSign_click_7.y', confirmSign_click_7.y)
    thisExp.addData('confirmSign_click_7.leftButton', confirmSign_click_7.leftButton)
    thisExp.addData('confirmSign_click_7.midButton', confirmSign_click_7.midButton)
    thisExp.addData('confirmSign_click_7.rightButton', confirmSign_click_7.rightButton)
    thisExp.addData('confirmSign_click_7.time', confirmSign_click_7.time)
    thisExp.addData('confirmSign_click_7.clicked_name', confirmSign_click_7.clicked_name)
    thisExp.addData('sleepy_time.response', sleepy_time.getRating())
    thisExp.addData('sleepy_time.rt', sleepy_time.getRT())
    thisExp.nextEntry()
    # the Routine "sleepytime_meq" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "bestpeak_meq" ---
    # create an object to store info about Routine bestpeak_meq
    bestpeak_meq = data.Routine(
        name='bestpeak_meq',
        components=[confirmSign_click_8, confirmSign_button_8, best_peak_Q, best_peak],
    )
    bestpeak_meq.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from exclude_11
    if consent.rating == 2:
        continueRoutine = False
    # setup some python lists for storing info about the confirmSign_click_8
    confirmSign_click_8.x = []
    confirmSign_click_8.y = []
    confirmSign_click_8.leftButton = []
    confirmSign_click_8.midButton = []
    confirmSign_click_8.rightButton = []
    confirmSign_click_8.time = []
    confirmSign_click_8.clicked_name = []
    gotValidClick = False  # until a click is received
    best_peak.reset()
    # store start times for bestpeak_meq
    bestpeak_meq.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    bestpeak_meq.tStart = globalClock.getTime(format='float')
    bestpeak_meq.status = STARTED
    thisExp.addData('bestpeak_meq.started', bestpeak_meq.tStart)
    bestpeak_meq.maxDuration = None
    # keep track of which components have finished
    bestpeak_meqComponents = bestpeak_meq.components
    for thisComponent in bestpeak_meq.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "bestpeak_meq" ---
    bestpeak_meq.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *confirmSign_click_8* updates
        
        # if confirmSign_click_8 is starting this frame...
        if confirmSign_click_8.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            confirmSign_click_8.frameNStart = frameN  # exact frame index
            confirmSign_click_8.tStart = t  # local t and not account for scr refresh
            confirmSign_click_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_click_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('confirmSign_click_8.started', t)
            # update status
            confirmSign_click_8.status = STARTED
            confirmSign_click_8.mouseClock.reset()
            prevButtonState = confirmSign_click_8.getPressed()  # if button is down already this ISN'T a new click
        if confirmSign_click_8.status == STARTED:  # only update if started and not finished!
            buttons = confirmSign_click_8.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(confirmSign_button_8, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(confirmSign_click_8):
                            gotValidClick = True
                            confirmSign_click_8.clicked_name.append(obj.name)
                    if not gotValidClick:
                        confirmSign_click_8.clicked_name.append(None)
                    x, y = confirmSign_click_8.getPos()
                    confirmSign_click_8.x.append(x)
                    confirmSign_click_8.y.append(y)
                    buttons = confirmSign_click_8.getPressed()
                    confirmSign_click_8.leftButton.append(buttons[0])
                    confirmSign_click_8.midButton.append(buttons[1])
                    confirmSign_click_8.rightButton.append(buttons[2])
                    confirmSign_click_8.time.append(confirmSign_click_8.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *confirmSign_button_8* updates
        
        # if confirmSign_button_8 is starting this frame...
        if confirmSign_button_8.status == NOT_STARTED and best_peak.rating:
            # keep track of start time/frame for later
            confirmSign_button_8.frameNStart = frameN  # exact frame index
            confirmSign_button_8.tStart = t  # local t and not account for scr refresh
            confirmSign_button_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_button_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confirmSign_button_8.started')
            # update status
            confirmSign_button_8.status = STARTED
            confirmSign_button_8.setAutoDraw(True)
        
        # if confirmSign_button_8 is active this frame...
        if confirmSign_button_8.status == STARTED:
            # update params
            pass
        
        # *best_peak_Q* updates
        
        # if best_peak_Q is starting this frame...
        if best_peak_Q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            best_peak_Q.frameNStart = frameN  # exact frame index
            best_peak_Q.tStart = t  # local t and not account for scr refresh
            best_peak_Q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(best_peak_Q, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'best_peak_Q.started')
            # update status
            best_peak_Q.status = STARTED
            best_peak_Q.setAutoDraw(True)
        
        # if best_peak_Q is active this frame...
        if best_peak_Q.status == STARTED:
            # update params
            pass
        
        # *best_peak* updates
        
        # if best_peak is starting this frame...
        if best_peak.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            best_peak.frameNStart = frameN  # exact frame index
            best_peak.tStart = t  # local t and not account for scr refresh
            best_peak.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(best_peak, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'best_peak.started')
            # update status
            best_peak.status = STARTED
            best_peak.setAutoDraw(True)
        
        # if best_peak is active this frame...
        if best_peak.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            bestpeak_meq.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in bestpeak_meq.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "bestpeak_meq" ---
    for thisComponent in bestpeak_meq.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for bestpeak_meq
    bestpeak_meq.tStop = globalClock.getTime(format='float')
    bestpeak_meq.tStopRefresh = tThisFlipGlobal
    thisExp.addData('bestpeak_meq.stopped', bestpeak_meq.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('confirmSign_click_8.x', confirmSign_click_8.x)
    thisExp.addData('confirmSign_click_8.y', confirmSign_click_8.y)
    thisExp.addData('confirmSign_click_8.leftButton', confirmSign_click_8.leftButton)
    thisExp.addData('confirmSign_click_8.midButton', confirmSign_click_8.midButton)
    thisExp.addData('confirmSign_click_8.rightButton', confirmSign_click_8.rightButton)
    thisExp.addData('confirmSign_click_8.time', confirmSign_click_8.time)
    thisExp.addData('confirmSign_click_8.clicked_name', confirmSign_click_8.clicked_name)
    thisExp.addData('best_peak.response', best_peak.getRating())
    thisExp.addData('best_peak.rt', best_peak.getRT())
    thisExp.nextEntry()
    # the Routine "bestpeak_meq" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "persontype_meq" ---
    # create an object to store info about Routine persontype_meq
    persontype_meq = data.Routine(
        name='persontype_meq',
        components=[confirmSign_click_9, confirmSign_button_9, person_type_Q, person_type],
    )
    persontype_meq.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from exclude_12
    if consent.rating == 2:
        continueRoutine = False
    # setup some python lists for storing info about the confirmSign_click_9
    confirmSign_click_9.x = []
    confirmSign_click_9.y = []
    confirmSign_click_9.leftButton = []
    confirmSign_click_9.midButton = []
    confirmSign_click_9.rightButton = []
    confirmSign_click_9.time = []
    confirmSign_click_9.clicked_name = []
    gotValidClick = False  # until a click is received
    person_type.reset()
    # store start times for persontype_meq
    persontype_meq.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    persontype_meq.tStart = globalClock.getTime(format='float')
    persontype_meq.status = STARTED
    thisExp.addData('persontype_meq.started', persontype_meq.tStart)
    persontype_meq.maxDuration = None
    # keep track of which components have finished
    persontype_meqComponents = persontype_meq.components
    for thisComponent in persontype_meq.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "persontype_meq" ---
    persontype_meq.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *confirmSign_click_9* updates
        
        # if confirmSign_click_9 is starting this frame...
        if confirmSign_click_9.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            confirmSign_click_9.frameNStart = frameN  # exact frame index
            confirmSign_click_9.tStart = t  # local t and not account for scr refresh
            confirmSign_click_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_click_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('confirmSign_click_9.started', t)
            # update status
            confirmSign_click_9.status = STARTED
            confirmSign_click_9.mouseClock.reset()
            prevButtonState = confirmSign_click_9.getPressed()  # if button is down already this ISN'T a new click
        if confirmSign_click_9.status == STARTED:  # only update if started and not finished!
            buttons = confirmSign_click_9.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(confirmSign_button_9, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(confirmSign_click_9):
                            gotValidClick = True
                            confirmSign_click_9.clicked_name.append(obj.name)
                    if not gotValidClick:
                        confirmSign_click_9.clicked_name.append(None)
                    x, y = confirmSign_click_9.getPos()
                    confirmSign_click_9.x.append(x)
                    confirmSign_click_9.y.append(y)
                    buttons = confirmSign_click_9.getPressed()
                    confirmSign_click_9.leftButton.append(buttons[0])
                    confirmSign_click_9.midButton.append(buttons[1])
                    confirmSign_click_9.rightButton.append(buttons[2])
                    confirmSign_click_9.time.append(confirmSign_click_9.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *confirmSign_button_9* updates
        
        # if confirmSign_button_9 is starting this frame...
        if confirmSign_button_9.status == NOT_STARTED and person_type.rating:
            # keep track of start time/frame for later
            confirmSign_button_9.frameNStart = frameN  # exact frame index
            confirmSign_button_9.tStart = t  # local t and not account for scr refresh
            confirmSign_button_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_button_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confirmSign_button_9.started')
            # update status
            confirmSign_button_9.status = STARTED
            confirmSign_button_9.setAutoDraw(True)
        
        # if confirmSign_button_9 is active this frame...
        if confirmSign_button_9.status == STARTED:
            # update params
            pass
        
        # *person_type_Q* updates
        
        # if person_type_Q is starting this frame...
        if person_type_Q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            person_type_Q.frameNStart = frameN  # exact frame index
            person_type_Q.tStart = t  # local t and not account for scr refresh
            person_type_Q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(person_type_Q, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'person_type_Q.started')
            # update status
            person_type_Q.status = STARTED
            person_type_Q.setAutoDraw(True)
        
        # if person_type_Q is active this frame...
        if person_type_Q.status == STARTED:
            # update params
            pass
        
        # *person_type* updates
        
        # if person_type is starting this frame...
        if person_type.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            person_type.frameNStart = frameN  # exact frame index
            person_type.tStart = t  # local t and not account for scr refresh
            person_type.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(person_type, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'person_type.started')
            # update status
            person_type.status = STARTED
            person_type.setAutoDraw(True)
        
        # if person_type is active this frame...
        if person_type.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            persontype_meq.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in persontype_meq.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "persontype_meq" ---
    for thisComponent in persontype_meq.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for persontype_meq
    persontype_meq.tStop = globalClock.getTime(format='float')
    persontype_meq.tStopRefresh = tThisFlipGlobal
    thisExp.addData('persontype_meq.stopped', persontype_meq.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('confirmSign_click_9.x', confirmSign_click_9.x)
    thisExp.addData('confirmSign_click_9.y', confirmSign_click_9.y)
    thisExp.addData('confirmSign_click_9.leftButton', confirmSign_click_9.leftButton)
    thisExp.addData('confirmSign_click_9.midButton', confirmSign_click_9.midButton)
    thisExp.addData('confirmSign_click_9.rightButton', confirmSign_click_9.rightButton)
    thisExp.addData('confirmSign_click_9.time', confirmSign_click_9.time)
    thisExp.addData('confirmSign_click_9.clicked_name', confirmSign_click_9.clicked_name)
    thisExp.addData('person_type.response', person_type.getRating())
    thisExp.addData('person_type.rt', person_type.getRT())
    thisExp.nextEntry()
    # the Routine "persontype_meq" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "what_age" ---
    # create an object to store info about Routine what_age
    what_age = data.Routine(
        name='what_age',
        components=[confirmSign_click_10, confirmSign_button_10, age_fill_Q, age_Q],
    )
    what_age.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from exclude_13
    if consent.rating == 2:
        continueRoutine = False
    # setup some python lists for storing info about the confirmSign_click_10
    confirmSign_click_10.x = []
    confirmSign_click_10.y = []
    confirmSign_click_10.leftButton = []
    confirmSign_click_10.midButton = []
    confirmSign_click_10.rightButton = []
    confirmSign_click_10.time = []
    confirmSign_click_10.clicked_name = []
    gotValidClick = False  # until a click is received
    age_Q.reset()
    # store start times for what_age
    what_age.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    what_age.tStart = globalClock.getTime(format='float')
    what_age.status = STARTED
    thisExp.addData('what_age.started', what_age.tStart)
    what_age.maxDuration = None
    # keep track of which components have finished
    what_ageComponents = what_age.components
    for thisComponent in what_age.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "what_age" ---
    what_age.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *confirmSign_click_10* updates
        
        # if confirmSign_click_10 is starting this frame...
        if confirmSign_click_10.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            confirmSign_click_10.frameNStart = frameN  # exact frame index
            confirmSign_click_10.tStart = t  # local t and not account for scr refresh
            confirmSign_click_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_click_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('confirmSign_click_10.started', t)
            # update status
            confirmSign_click_10.status = STARTED
            confirmSign_click_10.mouseClock.reset()
            prevButtonState = confirmSign_click_10.getPressed()  # if button is down already this ISN'T a new click
        if confirmSign_click_10.status == STARTED:  # only update if started and not finished!
            buttons = confirmSign_click_10.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(confirmSign_button_10, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(confirmSign_click_10):
                            gotValidClick = True
                            confirmSign_click_10.clicked_name.append(obj.name)
                    if not gotValidClick:
                        confirmSign_click_10.clicked_name.append(None)
                    x, y = confirmSign_click_10.getPos()
                    confirmSign_click_10.x.append(x)
                    confirmSign_click_10.y.append(y)
                    buttons = confirmSign_click_10.getPressed()
                    confirmSign_click_10.leftButton.append(buttons[0])
                    confirmSign_click_10.midButton.append(buttons[1])
                    confirmSign_click_10.rightButton.append(buttons[2])
                    confirmSign_click_10.time.append(confirmSign_click_10.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *confirmSign_button_10* updates
        
        # if confirmSign_button_10 is starting this frame...
        if confirmSign_button_10.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            confirmSign_button_10.frameNStart = frameN  # exact frame index
            confirmSign_button_10.tStart = t  # local t and not account for scr refresh
            confirmSign_button_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_button_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confirmSign_button_10.started')
            # update status
            confirmSign_button_10.status = STARTED
            confirmSign_button_10.setAutoDraw(True)
        
        # if confirmSign_button_10 is active this frame...
        if confirmSign_button_10.status == STARTED:
            # update params
            pass
        
        # *age_fill_Q* updates
        
        # if age_fill_Q is starting this frame...
        if age_fill_Q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            age_fill_Q.frameNStart = frameN  # exact frame index
            age_fill_Q.tStart = t  # local t and not account for scr refresh
            age_fill_Q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(age_fill_Q, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'age_fill_Q.started')
            # update status
            age_fill_Q.status = STARTED
            age_fill_Q.setAutoDraw(True)
        
        # if age_fill_Q is active this frame...
        if age_fill_Q.status == STARTED:
            # update params
            pass
        
        # *age_Q* updates
        
        # if age_Q is starting this frame...
        if age_Q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            age_Q.frameNStart = frameN  # exact frame index
            age_Q.tStart = t  # local t and not account for scr refresh
            age_Q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(age_Q, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'age_Q.started')
            # update status
            age_Q.status = STARTED
            age_Q.setAutoDraw(True)
        
        # if age_Q is active this frame...
        if age_Q.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            what_age.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in what_age.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "what_age" ---
    for thisComponent in what_age.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for what_age
    what_age.tStop = globalClock.getTime(format='float')
    what_age.tStopRefresh = tThisFlipGlobal
    thisExp.addData('what_age.stopped', what_age.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('confirmSign_click_10.x', confirmSign_click_10.x)
    thisExp.addData('confirmSign_click_10.y', confirmSign_click_10.y)
    thisExp.addData('confirmSign_click_10.leftButton', confirmSign_click_10.leftButton)
    thisExp.addData('confirmSign_click_10.midButton', confirmSign_click_10.midButton)
    thisExp.addData('confirmSign_click_10.rightButton', confirmSign_click_10.rightButton)
    thisExp.addData('confirmSign_click_10.time', confirmSign_click_10.time)
    thisExp.addData('confirmSign_click_10.clicked_name', confirmSign_click_10.clicked_name)
    thisExp.addData('age_Q.text',age_Q.text)
    thisExp.nextEntry()
    # the Routine "what_age" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "gender" ---
    # create an object to store info about Routine gender
    gender = data.Routine(
        name='gender',
        components=[confirmSign_click_11, confirmSign_button_11, gender_Q, gender_c, other_gender_text],
    )
    gender.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from exclude_14
    if consent.rating == 2:
        continueRoutine = False
    # setup some python lists for storing info about the confirmSign_click_11
    confirmSign_click_11.x = []
    confirmSign_click_11.y = []
    confirmSign_click_11.leftButton = []
    confirmSign_click_11.midButton = []
    confirmSign_click_11.rightButton = []
    confirmSign_click_11.time = []
    confirmSign_click_11.clicked_name = []
    gotValidClick = False  # until a click is received
    gender_c.reset()
    other_gender_text.reset()
    # Run 'Begin Routine' code from showMouse_6
    win.mouseVisible = True
    # store start times for gender
    gender.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    gender.tStart = globalClock.getTime(format='float')
    gender.status = STARTED
    thisExp.addData('gender.started', gender.tStart)
    gender.maxDuration = None
    # keep track of which components have finished
    genderComponents = gender.components
    for thisComponent in gender.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "gender" ---
    gender.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *confirmSign_click_11* updates
        
        # if confirmSign_click_11 is starting this frame...
        if confirmSign_click_11.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            confirmSign_click_11.frameNStart = frameN  # exact frame index
            confirmSign_click_11.tStart = t  # local t and not account for scr refresh
            confirmSign_click_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_click_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('confirmSign_click_11.started', t)
            # update status
            confirmSign_click_11.status = STARTED
            confirmSign_click_11.mouseClock.reset()
            prevButtonState = confirmSign_click_11.getPressed()  # if button is down already this ISN'T a new click
        if confirmSign_click_11.status == STARTED:  # only update if started and not finished!
            buttons = confirmSign_click_11.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(confirmSign_button_11, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(confirmSign_click_11):
                            gotValidClick = True
                            confirmSign_click_11.clicked_name.append(obj.name)
                    if not gotValidClick:
                        confirmSign_click_11.clicked_name.append(None)
                    x, y = confirmSign_click_11.getPos()
                    confirmSign_click_11.x.append(x)
                    confirmSign_click_11.y.append(y)
                    buttons = confirmSign_click_11.getPressed()
                    confirmSign_click_11.leftButton.append(buttons[0])
                    confirmSign_click_11.midButton.append(buttons[1])
                    confirmSign_click_11.rightButton.append(buttons[2])
                    confirmSign_click_11.time.append(confirmSign_click_11.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *confirmSign_button_11* updates
        
        # if confirmSign_button_11 is starting this frame...
        if confirmSign_button_11.status == NOT_STARTED and gender_c.rating:
            # keep track of start time/frame for later
            confirmSign_button_11.frameNStart = frameN  # exact frame index
            confirmSign_button_11.tStart = t  # local t and not account for scr refresh
            confirmSign_button_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_button_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confirmSign_button_11.started')
            # update status
            confirmSign_button_11.status = STARTED
            confirmSign_button_11.setAutoDraw(True)
        
        # if confirmSign_button_11 is active this frame...
        if confirmSign_button_11.status == STARTED:
            # update params
            pass
        
        # *gender_Q* updates
        
        # if gender_Q is starting this frame...
        if gender_Q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gender_Q.frameNStart = frameN  # exact frame index
            gender_Q.tStart = t  # local t and not account for scr refresh
            gender_Q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gender_Q, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'gender_Q.started')
            # update status
            gender_Q.status = STARTED
            gender_Q.setAutoDraw(True)
        
        # if gender_Q is active this frame...
        if gender_Q.status == STARTED:
            # update params
            pass
        
        # *gender_c* updates
        
        # if gender_c is starting this frame...
        if gender_c.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            gender_c.frameNStart = frameN  # exact frame index
            gender_c.tStart = t  # local t and not account for scr refresh
            gender_c.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gender_c, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'gender_c.started')
            # update status
            gender_c.status = STARTED
            gender_c.setAutoDraw(True)
        
        # if gender_c is active this frame...
        if gender_c.status == STARTED:
            # update params
            pass
        
        # *other_gender_text* updates
        
        # if other_gender_text is starting this frame...
        if other_gender_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            other_gender_text.frameNStart = frameN  # exact frame index
            other_gender_text.tStart = t  # local t and not account for scr refresh
            other_gender_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(other_gender_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'other_gender_text.started')
            # update status
            other_gender_text.status = STARTED
            other_gender_text.setAutoDraw(True)
        
        # if other_gender_text is active this frame...
        if other_gender_text.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from max_char_limit
        if len(other_gender_text.text) > 500:
             other_gender_text.text = other_gender_text.text[0:500]
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            gender.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in gender.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "gender" ---
    for thisComponent in gender.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for gender
    gender.tStop = globalClock.getTime(format='float')
    gender.tStopRefresh = tThisFlipGlobal
    thisExp.addData('gender.stopped', gender.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('confirmSign_click_11.x', confirmSign_click_11.x)
    thisExp.addData('confirmSign_click_11.y', confirmSign_click_11.y)
    thisExp.addData('confirmSign_click_11.leftButton', confirmSign_click_11.leftButton)
    thisExp.addData('confirmSign_click_11.midButton', confirmSign_click_11.midButton)
    thisExp.addData('confirmSign_click_11.rightButton', confirmSign_click_11.rightButton)
    thisExp.addData('confirmSign_click_11.time', confirmSign_click_11.time)
    thisExp.addData('confirmSign_click_11.clicked_name', confirmSign_click_11.clicked_name)
    thisExp.addData('gender_c.response', gender_c.getRating())
    thisExp.addData('gender_c.rt', gender_c.getRT())
    thisExp.addData('other_gender_text.text',other_gender_text.text)
    thisExp.nextEntry()
    # the Routine "gender" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "race_ethn" ---
    # create an object to store info about Routine race_ethn
    race_ethn = data.Routine(
        name='race_ethn',
        components=[confirmSign_click_13, confirmSign_button_13, race_Q, race_c, other_race_text],
    )
    race_ethn.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from exclude_15
    if consent.rating == 2:
        continueRoutine = False
    # setup some python lists for storing info about the confirmSign_click_13
    confirmSign_click_13.x = []
    confirmSign_click_13.y = []
    confirmSign_click_13.leftButton = []
    confirmSign_click_13.midButton = []
    confirmSign_click_13.rightButton = []
    confirmSign_click_13.time = []
    confirmSign_click_13.clicked_name = []
    gotValidClick = False  # until a click is received
    race_c.reset()
    other_race_text.reset()
    # Run 'Begin Routine' code from showMouse_7
    win.mouseVisible = True
    # store start times for race_ethn
    race_ethn.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    race_ethn.tStart = globalClock.getTime(format='float')
    race_ethn.status = STARTED
    thisExp.addData('race_ethn.started', race_ethn.tStart)
    race_ethn.maxDuration = None
    # keep track of which components have finished
    race_ethnComponents = race_ethn.components
    for thisComponent in race_ethn.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "race_ethn" ---
    race_ethn.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *confirmSign_click_13* updates
        
        # if confirmSign_click_13 is starting this frame...
        if confirmSign_click_13.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            confirmSign_click_13.frameNStart = frameN  # exact frame index
            confirmSign_click_13.tStart = t  # local t and not account for scr refresh
            confirmSign_click_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_click_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('confirmSign_click_13.started', t)
            # update status
            confirmSign_click_13.status = STARTED
            confirmSign_click_13.mouseClock.reset()
            prevButtonState = confirmSign_click_13.getPressed()  # if button is down already this ISN'T a new click
        if confirmSign_click_13.status == STARTED:  # only update if started and not finished!
            buttons = confirmSign_click_13.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(confirmSign_button_13, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(confirmSign_click_13):
                            gotValidClick = True
                            confirmSign_click_13.clicked_name.append(obj.name)
                    if not gotValidClick:
                        confirmSign_click_13.clicked_name.append(None)
                    x, y = confirmSign_click_13.getPos()
                    confirmSign_click_13.x.append(x)
                    confirmSign_click_13.y.append(y)
                    buttons = confirmSign_click_13.getPressed()
                    confirmSign_click_13.leftButton.append(buttons[0])
                    confirmSign_click_13.midButton.append(buttons[1])
                    confirmSign_click_13.rightButton.append(buttons[2])
                    confirmSign_click_13.time.append(confirmSign_click_13.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *confirmSign_button_13* updates
        
        # if confirmSign_button_13 is starting this frame...
        if confirmSign_button_13.status == NOT_STARTED and gender_c.rating:
            # keep track of start time/frame for later
            confirmSign_button_13.frameNStart = frameN  # exact frame index
            confirmSign_button_13.tStart = t  # local t and not account for scr refresh
            confirmSign_button_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirmSign_button_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confirmSign_button_13.started')
            # update status
            confirmSign_button_13.status = STARTED
            confirmSign_button_13.setAutoDraw(True)
        
        # if confirmSign_button_13 is active this frame...
        if confirmSign_button_13.status == STARTED:
            # update params
            pass
        
        # *race_Q* updates
        
        # if race_Q is starting this frame...
        if race_Q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            race_Q.frameNStart = frameN  # exact frame index
            race_Q.tStart = t  # local t and not account for scr refresh
            race_Q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(race_Q, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'race_Q.started')
            # update status
            race_Q.status = STARTED
            race_Q.setAutoDraw(True)
        
        # if race_Q is active this frame...
        if race_Q.status == STARTED:
            # update params
            pass
        
        # *race_c* updates
        
        # if race_c is starting this frame...
        if race_c.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            race_c.frameNStart = frameN  # exact frame index
            race_c.tStart = t  # local t and not account for scr refresh
            race_c.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(race_c, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'race_c.started')
            # update status
            race_c.status = STARTED
            race_c.setAutoDraw(True)
        
        # if race_c is active this frame...
        if race_c.status == STARTED:
            # update params
            pass
        
        # *other_race_text* updates
        
        # if other_race_text is starting this frame...
        if other_race_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            other_race_text.frameNStart = frameN  # exact frame index
            other_race_text.tStart = t  # local t and not account for scr refresh
            other_race_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(other_race_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'other_race_text.started')
            # update status
            other_race_text.status = STARTED
            other_race_text.setAutoDraw(True)
        
        # if other_race_text is active this frame...
        if other_race_text.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from max_char_limit_2
        if len(other_race_text.text) > 500:
             other_gender_text.text = other_gender_text.text[0:500]
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            race_ethn.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in race_ethn.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "race_ethn" ---
    for thisComponent in race_ethn.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for race_ethn
    race_ethn.tStop = globalClock.getTime(format='float')
    race_ethn.tStopRefresh = tThisFlipGlobal
    thisExp.addData('race_ethn.stopped', race_ethn.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('confirmSign_click_13.x', confirmSign_click_13.x)
    thisExp.addData('confirmSign_click_13.y', confirmSign_click_13.y)
    thisExp.addData('confirmSign_click_13.leftButton', confirmSign_click_13.leftButton)
    thisExp.addData('confirmSign_click_13.midButton', confirmSign_click_13.midButton)
    thisExp.addData('confirmSign_click_13.rightButton', confirmSign_click_13.rightButton)
    thisExp.addData('confirmSign_click_13.time', confirmSign_click_13.time)
    thisExp.addData('confirmSign_click_13.clicked_name', confirmSign_click_13.clicked_name)
    thisExp.addData('race_c.response', race_c.getRating())
    thisExp.addData('race_c.rt', race_c.getRT())
    thisExp.addData('other_race_text.text',other_race_text.text)
    thisExp.nextEntry()
    # the Routine "race_ethn" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Thanks" ---
    # create an object to store info about Routine Thanks
    Thanks = data.Routine(
        name='Thanks',
        components=[ThanksText],
    )
    Thanks.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from exclude_16
    if consent.rating == 2:
        continueRoutine = False
    # Run 'Begin Routine' code from showMouse_5
    win.mouseVisible = True
    # store start times for Thanks
    Thanks.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Thanks.tStart = globalClock.getTime(format='float')
    Thanks.status = STARTED
    thisExp.addData('Thanks.started', Thanks.tStart)
    Thanks.maxDuration = None
    # keep track of which components have finished
    ThanksComponents = Thanks.components
    for thisComponent in Thanks.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Thanks" ---
    Thanks.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ThanksText* updates
        
        # if ThanksText is starting this frame...
        if ThanksText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ThanksText.frameNStart = frameN  # exact frame index
            ThanksText.tStart = t  # local t and not account for scr refresh
            ThanksText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ThanksText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ThanksText.started')
            # update status
            ThanksText.status = STARTED
            ThanksText.setAutoDraw(True)
        
        # if ThanksText is active this frame...
        if ThanksText.status == STARTED:
            # update params
            pass
        
        # if ThanksText is stopping this frame...
        if ThanksText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ThanksText.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                ThanksText.tStop = t  # not accounting for scr refresh
                ThanksText.tStopRefresh = tThisFlipGlobal  # on global time
                ThanksText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ThanksText.stopped')
                # update status
                ThanksText.status = FINISHED
                ThanksText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Thanks.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Thanks.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Thanks" ---
    for thisComponent in Thanks.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Thanks
    Thanks.tStop = globalClock.getTime(format='float')
    Thanks.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Thanks.stopped', Thanks.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Thanks.maxDurationReached:
        routineTimer.addTime(-Thanks.maxDuration)
    elif Thanks.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
