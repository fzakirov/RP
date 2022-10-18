#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Октябрь 15, 2022, at 18:42
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'PD'  # from the Builder filename that created this script
expInfo = {
    'ID': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['ID'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath="C:\\Users\\nilsk\\RP\\Prisoner's Dilemma\\PD_lastrun.py",
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1, -1, -1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "start" ---
start_text = visual.TextStim(win=win, name='start_text',
    text='In this task you will be asked to win points by either cooperating with or defecting against another player\n\nTry to gain as many point as possible and win the game\n\nWe will begin by asking you to enter some details about yourself!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start_cont = visual.TextStim(win=win, name='start_cont',
    text='click HERE to continue',
    font='Arial',
    pos=(0, -0.8), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
start_mouse = event.Mouse(win=win)
x, y = [None, None]
start_mouse.mouseClock = core.Clock()
# Run 'Begin Experiment' code from random_order_code
import random
order_list = ['A', 'B', 'C', 'D']
random.shuffle(order_list)
order = order_list[0]

thisExp.addData('order', order)

# --- Initialize components for Routine "name" ---
name_text = visual.TextStim(win=win, name='name_text',
    text='Type your name:',
    font='Open Sans',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
type_name = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0.2),     letterHeight=0.1,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='type_name',
     autoLog=True,
)
name_cont = visual.TextStim(win=win, name='name_cont',
    text='click HERE to continue',
    font='Arial',
    pos=(0, -0.8), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
name_mouse = event.Mouse(win=win)
x, y = [None, None]
name_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "avatar" ---
avatar_text = visual.TextStim(win=win, name='avatar_text',
    text='Choose an avatar!',
    font='Arial',
    pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
avatar1 = visual.ImageStim(
    win=win,
    name='avatar1', 
    image='avatar1.png', mask=None, anchor='center',
    ori=0, pos=(-0.4, 0.4), size=(0.35, 0.6125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
avatar2 = visual.ImageStim(
    win=win,
    name='avatar2', 
    image='avatar2.png', mask=None, anchor='center',
    ori=0, pos=(0, 0.4), size=(0.35, 0.6125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
avatar3 = visual.ImageStim(
    win=win,
    name='avatar3', 
    image='avatar3.png', mask=None, anchor='center',
    ori=0, pos=(0.4, 0.4), size=(0.35, 0.6125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
avatar4 = visual.ImageStim(
    win=win,
    name='avatar4', 
    image='avatar4.png', mask=None, anchor='center',
    ori=0, pos=(-0.4, -0.4), size=(0.35, 0.6125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
avatar5 = visual.ImageStim(
    win=win,
    name='avatar5', 
    image='avatar5.png', mask=None, anchor='center',
    ori=0, pos=(0, -0.4), size=(0.35, 0.6125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
avatar6 = visual.ImageStim(
    win=win,
    name='avatar6', 
    image='avatar6.png', mask=None, anchor='center',
    ori=0, pos=(0.4, -0.4), size=(0.35, 0.6125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
avatar_mouse = event.Mouse(win=win)
x, y = [None, None]
avatar_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "intro" ---
intro_text = visual.TextStim(win=win, name='intro_text',
    text='You will win points by either choosing to cooperate with or defect against another player\n\nBoth you and the other player will make your choice and then your decisions will be revealed\n\nYou will receive points based on both of your choices\n\nYou will play against two different players in separate rounds',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
intro_cont = visual.TextStim(win=win, name='intro_cont',
    text='click HERE to continue',
    font='Arial',
    pos=(0, -0.9), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
intro_mouse = event.Mouse(win=win)
x, y = [None, None]
intro_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "practice_trial_1" ---
practice_avatar_1 = visual.ImageStim(
    win=win,
    name='practice_avatar_1', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-0.2, 0.7), size=(0.0875, 0.153125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
practice_top_left_1 = visual.Rect(
    win=win, name='practice_top_left_1',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(-0.14,0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-1.0, interpolate=True)
practice_top_right_1 = visual.Rect(
    win=win, name='practice_top_right_1',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(0.14,0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-2.0, interpolate=True)
practice_bottom_left_1 = visual.Rect(
    win=win, name='practice_bottom_left_1',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(-0.14,-0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-3.0, interpolate=True)
practice_bottom_right_1 = visual.Rect(
    win=win, name='practice_bottom_right_1',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(0.14,-0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-4.0, interpolate=True)
practice_points_tl_p_1 = visual.TextStim(win=win, name='practice_points_tl_p_1',
    text='',
    font='Arial',
    pos=(-0.2,0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
practice_points_tl_o_1 = visual.TextStim(win=win, name='practice_points_tl_o_1',
    text='',
    font='Arial',
    pos=(-0.1,0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
practice_points_bl_p_1 = visual.TextStim(win=win, name='practice_points_bl_p_1',
    text='',
    font='Arial',
    pos=(-0.2,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
practice_points_bl_o_1 = visual.TextStim(win=win, name='practice_points_bl_o_1',
    text='',
    font='Arial',
    pos=(-0.1,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
practice_points_tr_p_1 = visual.TextStim(win=win, name='practice_points_tr_p_1',
    text='',
    font='Arial',
    pos=(0.1,0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
practice_points_tr_o_1 = visual.TextStim(win=win, name='practice_points_tr_o_1',
    text='',
    font='Arial',
    pos=(0.2,0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
practice_points_br_p_1 = visual.TextStim(win=win, name='practice_points_br_p_1',
    text='',
    font='Arial',
    pos=(0.1,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
practice_points_br_o_1 = visual.TextStim(win=win, name='practice_points_br_o_1',
    text='',
    font='Arial',
    pos=(0.2,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
practice_tr_header_1 = visual.TextStim(win=win, name='practice_tr_header_1',
    text='Defect',
    font='Arial',
    pos=(0.13,0.57), height=0.08, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
practice_bt_header_1 = visual.TextStim(win=win, name='practice_bt_header_1',
    text='Cooperate',
    font='Arial',
    pos=(-0.4,0.25), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
practice_p_header_1 = visual.TextStim(win=win, name='practice_p_header_1',
    text='',
    font='Arial',
    pos=(0, 0.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
practice_o_header_1 = visual.TextStim(win=win, name='practice_o_header_1',
    text='Other player',
    font='Arial',
    pos=(-0.6, 0), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
practice_bb_header_1 = visual.TextStim(win=win, name='practice_bb_header_1',
    text='Defect',
    font='Arial',
    pos=(-0.4,-0.25), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
practice_tl_header_1 = visual.TextStim(win=win, name='practice_tl_header_1',
    text='Cooperate',
    font='Arial',
    pos=(-0.13,0.57), height=0.08, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
practice_text_1 = visual.TextStim(win=win, name='practice_text_1',
    text="This is what you will see for each trail of the game\n\nAt the top of you can see your choices\n\nOn the left you can see the other player's choices",
    font='Arial',
    pos=(0.6, 0), height=0.1, wrapWidth=0.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);
practice_cont_1 = visual.TextStim(win=win, name='practice_cont_1',
    text='click HERE to continue',
    font='Arial',
    pos=(0, -0.8), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-20.0);
practice_mouse_1 = event.Mouse(win=win)
x, y = [None, None]
practice_mouse_1.mouseClock = core.Clock()

# --- Initialize components for Routine "practice_trial_2" ---
practice_avatar_2 = visual.ImageStim(
    win=win,
    name='practice_avatar_2', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-0.2, 0.7), size=(0.0875, 0.153125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
practice_top_left_2 = visual.Rect(
    win=win, name='practice_top_left_2',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(-0.14,0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-1.0, interpolate=True)
practice_top_right_2 = visual.Rect(
    win=win, name='practice_top_right_2',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(0.14,0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-2.0, interpolate=True)
practice_bottom_left_2 = visual.Rect(
    win=win, name='practice_bottom_left_2',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(-0.14,-0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-3.0, interpolate=True)
practice_bottom_right_2 = visual.Rect(
    win=win, name='practice_bottom_right_2',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(0.14,-0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-4.0, interpolate=True)
practice_points_tl_p_2 = visual.TextStim(win=win, name='practice_points_tl_p_2',
    text='',
    font='Arial',
    pos=(-0.2,0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
practice_points_tl_o_2 = visual.TextStim(win=win, name='practice_points_tl_o_2',
    text='',
    font='Arial',
    pos=(-0.1,0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
practice_points_bl_p_2 = visual.TextStim(win=win, name='practice_points_bl_p_2',
    text='',
    font='Arial',
    pos=(-0.2,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
practice_points_bl_o_2 = visual.TextStim(win=win, name='practice_points_bl_o_2',
    text='',
    font='Arial',
    pos=(-0.1,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
practice_points_tr_p_2 = visual.TextStim(win=win, name='practice_points_tr_p_2',
    text='',
    font='Arial',
    pos=(0.1,0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
practice_points_tr_o_2 = visual.TextStim(win=win, name='practice_points_tr_o_2',
    text='',
    font='Arial',
    pos=(0.2,0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
practice_points_br_p_2 = visual.TextStim(win=win, name='practice_points_br_p_2',
    text='',
    font='Arial',
    pos=(0.1,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
practice_points_br_o_2 = visual.TextStim(win=win, name='practice_points_br_o_2',
    text='',
    font='Arial',
    pos=(0.2,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
practice_tr_header_2 = visual.TextStim(win=win, name='practice_tr_header_2',
    text='Defect',
    font='Arial',
    pos=(0.13,0.57), height=0.08, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
practice_bt_header_2 = visual.TextStim(win=win, name='practice_bt_header_2',
    text='Cooperate',
    font='Arial',
    pos=(-0.4,0.25), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
practice_p_header_2 = visual.TextStim(win=win, name='practice_p_header_2',
    text='',
    font='Arial',
    pos=(0, 0.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
practice_o_header_2 = visual.TextStim(win=win, name='practice_o_header_2',
    text='Other player',
    font='Arial',
    pos=(-0.6, 0), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
practice_bb_header_2 = visual.TextStim(win=win, name='practice_bb_header_2',
    text='Defect',
    font='Arial',
    pos=(-0.4,-0.25), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
practice_tl_header_2 = visual.TextStim(win=win, name='practice_tl_header_2',
    text='Cooperate',
    font='Arial',
    pos=(-0.13,0.57), height=0.08, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
practice_text_2 = visual.TextStim(win=win, name='practice_text_2',
    text="In the boxes you can see the amount of points you will win from your choice\n\nYour points are in WHITE\n\nThe other player's points are in YELLOW",
    font='Arial',
    pos=(0.6, 0), height=0.1, wrapWidth=0.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);
practice_cont_2 = visual.TextStim(win=win, name='practice_cont_2',
    text='click HERE to continue',
    font='Arial',
    pos=(0, -0.8), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-20.0);
practice_mouse_2 = event.Mouse(win=win)
x, y = [None, None]
practice_mouse_2.mouseClock = core.Clock()

# --- Initialize components for Routine "practice_trial_3" ---
practice_avatar_3 = visual.ImageStim(
    win=win,
    name='practice_avatar_3', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-0.2, 0.7), size=(0.0875, 0.153125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
practice_top_left_3 = visual.Rect(
    win=win, name='practice_top_left_3',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(-0.14,0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=[1.000,1.000,0.004],
    opacity=0.2, depth=-1.0, interpolate=True)
practice_top_right_3 = visual.Rect(
    win=win, name='practice_top_right_3',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(0.14,0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-2.0, interpolate=True)
practice_bottom_left_3 = visual.Rect(
    win=win, name='practice_bottom_left_3',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(-0.14,-0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-3.0, interpolate=True)
practice_bottom_right_3 = visual.Rect(
    win=win, name='practice_bottom_right_3',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(0.14,-0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-4.0, interpolate=True)
practice_points_tl_p_3 = visual.TextStim(win=win, name='practice_points_tl_p_3',
    text='',
    font='Arial',
    pos=(-0.2,0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
practice_points_tl_o_3 = visual.TextStim(win=win, name='practice_points_tl_o_3',
    text='',
    font='Arial',
    pos=(-0.1,0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
practice_points_bl_p_3 = visual.TextStim(win=win, name='practice_points_bl_p_3',
    text='',
    font='Arial',
    pos=(-0.2,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
practice_points_bl_o_3 = visual.TextStim(win=win, name='practice_points_bl_o_3',
    text='',
    font='Arial',
    pos=(-0.1,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
practice_points_tr_p_3 = visual.TextStim(win=win, name='practice_points_tr_p_3',
    text='',
    font='Arial',
    pos=(0.1,0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
practice_points_tr_o_3 = visual.TextStim(win=win, name='practice_points_tr_o_3',
    text='',
    font='Arial',
    pos=(0.2,0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
practice_points_br_p_3 = visual.TextStim(win=win, name='practice_points_br_p_3',
    text='',
    font='Arial',
    pos=(0.1,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
practice_points_br_o_3 = visual.TextStim(win=win, name='practice_points_br_o_3',
    text='',
    font='Arial',
    pos=(0.2,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
practice_tr_header_3 = visual.TextStim(win=win, name='practice_tr_header_3',
    text='Defect',
    font='Arial',
    pos=(0.13,0.57), height=0.08, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
practice_bt_header_3 = visual.TextStim(win=win, name='practice_bt_header_3',
    text='Cooperate',
    font='Arial',
    pos=(-0.4,0.25), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
practice_p_header_3 = visual.TextStim(win=win, name='practice_p_header_3',
    text='',
    font='Arial',
    pos=(0, 0.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
practice_o_header_3 = visual.TextStim(win=win, name='practice_o_header_3',
    text='Other player',
    font='Arial',
    pos=(-0.6, 0), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
practice_bb_header_3 = visual.TextStim(win=win, name='practice_bb_header_3',
    text='Defect',
    font='Arial',
    pos=(-0.4,-0.25), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
practice_tl_header_3 = visual.TextStim(win=win, name='practice_tl_header_3',
    text='Cooperate',
    font='Arial',
    pos=(-0.13,0.57), height=0.08, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
practice_text_3 = visual.TextStim(win=win, name='practice_text_3',
    text='For example, if both you and the other player choose to cooperate you will both get 1 point each',
    font='Arial',
    pos=(0.6, 0), height=0.1, wrapWidth=0.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);
practice_cont_3 = visual.TextStim(win=win, name='practice_cont_3',
    text='click HERE to continue',
    font='Arial',
    pos=(0, -0.8), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-20.0);
practice_mouse_3 = event.Mouse(win=win)
x, y = [None, None]
practice_mouse_3.mouseClock = core.Clock()

# --- Initialize components for Routine "practice_trial_4" ---
practice_avatar_4 = visual.ImageStim(
    win=win,
    name='practice_avatar_4', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-0.2, 0.7), size=(0.0875, 0.153125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
practice_top_left_4 = visual.Rect(
    win=win, name='practice_top_left_4',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(-0.14,0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-1.0, interpolate=True)
practice_top_right_4 = visual.Rect(
    win=win, name='practice_top_right_4',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(0.14,0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-2.0, interpolate=True)
practice_bottom_left_4 = visual.Rect(
    win=win, name='practice_bottom_left_4',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(-0.14,-0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-3.0, interpolate=True)
practice_bottom_right_4 = visual.Rect(
    win=win, name='practice_bottom_right_4',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(0.14,-0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=[1.000,1.000,0.004],
    opacity=0.2, depth=-4.0, interpolate=True)
practice_points_tl_p_4 = visual.TextStim(win=win, name='practice_points_tl_p_4',
    text='',
    font='Arial',
    pos=(-0.2,0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
practice_points_tl_o_4 = visual.TextStim(win=win, name='practice_points_tl_o_4',
    text='',
    font='Arial',
    pos=(-0.1,0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
practice_points_bl_p_4 = visual.TextStim(win=win, name='practice_points_bl_p_4',
    text='',
    font='Arial',
    pos=(-0.2,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
practice_points_bl_o_4 = visual.TextStim(win=win, name='practice_points_bl_o_4',
    text='',
    font='Arial',
    pos=(-0.1,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
practice_points_tr_p_4 = visual.TextStim(win=win, name='practice_points_tr_p_4',
    text='',
    font='Arial',
    pos=(0.1,0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
practice_points_tr_o_4 = visual.TextStim(win=win, name='practice_points_tr_o_4',
    text='',
    font='Arial',
    pos=(0.2,0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
practice_points_br_p_4 = visual.TextStim(win=win, name='practice_points_br_p_4',
    text='',
    font='Arial',
    pos=(0.1,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
practice_points_br_o_4 = visual.TextStim(win=win, name='practice_points_br_o_4',
    text='',
    font='Arial',
    pos=(0.2,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
practice_tr_header_4 = visual.TextStim(win=win, name='practice_tr_header_4',
    text='Defect',
    font='Arial',
    pos=(0.13,0.57), height=0.08, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
practice_bt_header_4 = visual.TextStim(win=win, name='practice_bt_header_4',
    text='Cooperate',
    font='Arial',
    pos=(-0.4,0.25), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
practice_p_header_4 = visual.TextStim(win=win, name='practice_p_header_4',
    text='',
    font='Arial',
    pos=(0, 0.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
practice_o_header_4 = visual.TextStim(win=win, name='practice_o_header_4',
    text='Other player',
    font='Arial',
    pos=(-0.6, 0), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
practice_bb_header_4 = visual.TextStim(win=win, name='practice_bb_header_4',
    text='Defect',
    font='Arial',
    pos=(-0.4,-0.25), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
practice_tl_header_4 = visual.TextStim(win=win, name='practice_tl_header_4',
    text='Cooperate',
    font='Arial',
    pos=(-0.13,0.57), height=0.08, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
practice_text_4 = visual.TextStim(win=win, name='practice_text_4',
    text='If both you and the other player choose to defect you will both get 0.5 points each',
    font='Arial',
    pos=(0.6, 0), height=0.1, wrapWidth=0.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);
practice_cont_4 = visual.TextStim(win=win, name='practice_cont_4',
    text='click HERE to continue',
    font='Arial',
    pos=(0, -0.8), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-20.0);
practice_mouse_4 = event.Mouse(win=win)
x, y = [None, None]
practice_mouse_4.mouseClock = core.Clock()

# --- Initialize components for Routine "practice_trial_5" ---
practice_avatar_trial_5 = visual.ImageStim(
    win=win,
    name='practice_avatar_trial_5', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-0.2, 0.7), size=(0.0875, 0.153125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
practice_top_left_5 = visual.Rect(
    win=win, name='practice_top_left_5',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(-0.14,0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-1.0, interpolate=True)
practice_top_right_5 = visual.Rect(
    win=win, name='practice_top_right_5',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(0.14,0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-2.0, interpolate=True)
practice_bottom_left_5 = visual.Rect(
    win=win, name='practice_bottom_left_5',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(-0.14,-0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=[1.000,1.000,0.004],
    opacity=0.2, depth=-3.0, interpolate=True)
practice_bottom_right_5 = visual.Rect(
    win=win, name='practice_bottom_right_5',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(0.14,-0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-4.0, interpolate=True)
practice_points_tl_p_5 = visual.TextStim(win=win, name='practice_points_tl_p_5',
    text='',
    font='Arial',
    pos=(-0.2,0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
practice_points_tl_o_5 = visual.TextStim(win=win, name='practice_points_tl_o_5',
    text='',
    font='Arial',
    pos=(-0.1,0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
practice_points_bl_p_5 = visual.TextStim(win=win, name='practice_points_bl_p_5',
    text='',
    font='Arial',
    pos=(-0.2,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
practice_points_bl_o_5 = visual.TextStim(win=win, name='practice_points_bl_o_5',
    text='',
    font='Arial',
    pos=(-0.1,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
practice_points_tr_p_5 = visual.TextStim(win=win, name='practice_points_tr_p_5',
    text='',
    font='Arial',
    pos=(0.1,0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
practice_points_tr_o_5 = visual.TextStim(win=win, name='practice_points_tr_o_5',
    text='',
    font='Arial',
    pos=(0.2,0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
practice_points_br_p_5 = visual.TextStim(win=win, name='practice_points_br_p_5',
    text='',
    font='Arial',
    pos=(0.1,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
practice_points_br_o_5 = visual.TextStim(win=win, name='practice_points_br_o_5',
    text='',
    font='Arial',
    pos=(0.2,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
practice_tr_header_5 = visual.TextStim(win=win, name='practice_tr_header_5',
    text='Defect',
    font='Arial',
    pos=(0.13,0.57), height=0.08, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
practice_bt_header_5 = visual.TextStim(win=win, name='practice_bt_header_5',
    text='Cooperate',
    font='Arial',
    pos=(-0.4,0.25), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
practice_p_header_5 = visual.TextStim(win=win, name='practice_p_header_5',
    text='',
    font='Arial',
    pos=(0, 0.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
practice_o_header_5 = visual.TextStim(win=win, name='practice_o_header_5',
    text='Other player',
    font='Arial',
    pos=(-0.6, 0), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
practice_bb_header_5 = visual.TextStim(win=win, name='practice_bb_header_5',
    text='Defect',
    font='Arial',
    pos=(-0.4,-0.25), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
practice_tl_header_5 = visual.TextStim(win=win, name='practice_tl_header_5',
    text='Cooperate',
    font='Arial',
    pos=(-0.13,0.57), height=0.08, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
practice_text_5 = visual.TextStim(win=win, name='practice_text_5',
    text='If you choose to cooperate but the other player chooses to defect, you will get 0 points and the other player will get 1.5 points',
    font='Arial',
    pos=(0.6, 0), height=0.1, wrapWidth=0.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);
practice_cont_5 = visual.TextStim(win=win, name='practice_cont_5',
    text='click HERE to continue',
    font='Arial',
    pos=(0, -0.8), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-20.0);
practice_mouse_5 = event.Mouse(win=win)
x, y = [None, None]
practice_mouse_5.mouseClock = core.Clock()

# --- Initialize components for Routine "practice_trial_6" ---
practice_avatar_6 = visual.ImageStim(
    win=win,
    name='practice_avatar_6', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-0.2, 0.7), size=(0.0875, 0.153125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
practice_top_left_6 = visual.Rect(
    win=win, name='practice_top_left_6',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(-0.14,0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-1.0, interpolate=True)
practice_top_right_6 = visual.Rect(
    win=win, name='practice_top_right_6',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(0.14,0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=[1.000,1.000,0.004],
    opacity=0.2, depth=-2.0, interpolate=True)
practice_bottom_left_6 = visual.Rect(
    win=win, name='practice_bottom_left_6',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(-0.14,-0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-3.0, interpolate=True)
practice_bottom_right_6 = visual.Rect(
    win=win, name='practice_bottom_right_6',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(0.14,-0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-4.0, interpolate=True)
practice_points_tl_p_6 = visual.TextStim(win=win, name='practice_points_tl_p_6',
    text='',
    font='Arial',
    pos=(-0.2,0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
practice_points_tl_o_6 = visual.TextStim(win=win, name='practice_points_tl_o_6',
    text='',
    font='Arial',
    pos=(-0.1,0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
practice_points_bl_p_6 = visual.TextStim(win=win, name='practice_points_bl_p_6',
    text='',
    font='Arial',
    pos=(-0.2,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
practice_points_bl_o_6 = visual.TextStim(win=win, name='practice_points_bl_o_6',
    text='',
    font='Arial',
    pos=(-0.1,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
practice_points_tr_p_6 = visual.TextStim(win=win, name='practice_points_tr_p_6',
    text='',
    font='Arial',
    pos=(0.1,0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
practice_points_tr_o_6 = visual.TextStim(win=win, name='practice_points_tr_o_6',
    text='',
    font='Arial',
    pos=(0.2,0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
practice_points_br_p_6 = visual.TextStim(win=win, name='practice_points_br_p_6',
    text='',
    font='Arial',
    pos=(0.1,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
practice_points_br_o_6 = visual.TextStim(win=win, name='practice_points_br_o_6',
    text='',
    font='Arial',
    pos=(0.2,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
practice_tr_header_6 = visual.TextStim(win=win, name='practice_tr_header_6',
    text='Defect',
    font='Arial',
    pos=(0.13,0.57), height=0.08, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
practice_bt_header_6 = visual.TextStim(win=win, name='practice_bt_header_6',
    text='Cooperate',
    font='Arial',
    pos=(-0.4,0.25), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
practice_p_header_6 = visual.TextStim(win=win, name='practice_p_header_6',
    text='',
    font='Arial',
    pos=(0, 0.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
practice_o_header_6 = visual.TextStim(win=win, name='practice_o_header_6',
    text='Other player',
    font='Arial',
    pos=(-0.6, 0), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
practice_bb_header_6 = visual.TextStim(win=win, name='practice_bb_header_6',
    text='Defect',
    font='Arial',
    pos=(-0.4,-0.25), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
practice_tl_header_6 = visual.TextStim(win=win, name='practice_tl_header_6',
    text='Cooperate',
    font='Arial',
    pos=(-0.13,0.57), height=0.08, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
practice_text_6 = visual.TextStim(win=win, name='practice_text_6',
    text='Finally, if you choose to defect and the other player chooses to cooperate you will get 1.5 points and the other player will get 0 points',
    font='Arial',
    pos=(0.6, 0), height=0.1, wrapWidth=0.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);
practice_cont_6 = visual.TextStim(win=win, name='practice_cont_6',
    text='click HERE to continue',
    font='Arial',
    pos=(0, -0.8), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-20.0);
practice_mouse_6 = event.Mouse(win=win)
x, y = [None, None]
practice_mouse_6.mouseClock = core.Clock()

# --- Initialize components for Routine "practice_trial_7" ---
practice_avatar_7 = visual.ImageStim(
    win=win,
    name='practice_avatar_7', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-0.2, 0.7), size=(0.0875, 0.153125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
practice_top_left_7 = visual.Rect(
    win=win, name='practice_top_left_7',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(-0.14,0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-1.0, interpolate=True)
practice_top_right_7 = visual.Rect(
    win=win, name='practice_top_right_7',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(0.14,0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-2.0, interpolate=True)
practice_bottom_left_7 = visual.Rect(
    win=win, name='practice_bottom_left_7',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(-0.14,-0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-3.0, interpolate=True)
practice_bottom_right_7 = visual.Rect(
    win=win, name='practice_bottom_right_7',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(0.14,-0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-4.0, interpolate=True)
practice_points_tl_p_7 = visual.TextStim(win=win, name='practice_points_tl_p_7',
    text='',
    font='Arial',
    pos=(-0.2,0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
practice_points_tl_o_7 = visual.TextStim(win=win, name='practice_points_tl_o_7',
    text='',
    font='Arial',
    pos=(-0.1,0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
practice_points_bl_p_7 = visual.TextStim(win=win, name='practice_points_bl_p_7',
    text='',
    font='Arial',
    pos=(-0.2,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
practice_points_bl_o_7 = visual.TextStim(win=win, name='practice_points_bl_o_7',
    text='',
    font='Arial',
    pos=(-0.1,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
practice_points_tr_p_7 = visual.TextStim(win=win, name='practice_points_tr_p_7',
    text='',
    font='Arial',
    pos=(0.1,0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
practice_points_tr_o_7 = visual.TextStim(win=win, name='practice_points_tr_o_7',
    text='',
    font='Arial',
    pos=(0.2,0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
practice_points_br_p_7 = visual.TextStim(win=win, name='practice_points_br_p_7',
    text='',
    font='Arial',
    pos=(0.1,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
practice_points_br_o_7 = visual.TextStim(win=win, name='practice_points_br_o_7',
    text='',
    font='Arial',
    pos=(0.2,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
practice_tr_header_7 = visual.TextStim(win=win, name='practice_tr_header_7',
    text='Defect',
    font='Arial',
    pos=(0.13,0.57), height=0.08, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
practice_bt_header_7 = visual.TextStim(win=win, name='practice_bt_header_7',
    text='Cooperate',
    font='Arial',
    pos=(-0.4,0.25), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
practice_p_header_7 = visual.TextStim(win=win, name='practice_p_header_7',
    text='',
    font='Arial',
    pos=(0, 0.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
practice_other_header_7 = visual.TextStim(win=win, name='practice_other_header_7',
    text='Other player',
    font='Arial',
    pos=(-0.6, 0), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
practice_bb_header_7 = visual.TextStim(win=win, name='practice_bb_header_7',
    text='Defect',
    font='Arial',
    pos=(-0.4,-0.25), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
practice_tl_header_7 = visual.TextStim(win=win, name='practice_tl_header_7',
    text='Cooperate',
    font='Arial',
    pos=(-0.13,0.57), height=0.08, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
practice_text_7 = visual.TextStim(win=win, name='practice_text_7',
    text="You will not know the other player's choice before you have made yours!\n\nAfter you have made your choice, you will find out the other player's decision and the amount of points you have won",
    font='Arial',
    pos=(0.6, 0), height=0.1, wrapWidth=0.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);
practice_cont_7 = visual.TextStim(win=win, name='practice_cont_7',
    text='click HERE to continue',
    font='Arial',
    pos=(0, -0.8), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-20.0);
practice_mouse_7 = event.Mouse(win=win)
x, y = [None, None]
practice_mouse_7.mouseClock = core.Clock()

# --- Initialize components for Routine "practice_trial_8" ---
practice_choice_p_8 = visual.TextStim(win=win, name='practice_choice_p_8',
    text='',
    font='Arial',
    pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
practice_choice_o_8 = visual.TextStim(win=win, name='practice_choice_o_8',
    text='',
    font='Arial',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
practice_points_p_8 = visual.TextStim(win=win, name='practice_points_p_8',
    text='',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
practice_points_o_8 = visual.TextStim(win=win, name='practice_points_o_8',
    text='',
    font='Arial',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
practice_bottom_left_8 = visual.Rect(
    win=win, name='practice_bottom_left_8',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(-0.14,-0.4), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-4.0, interpolate=True)
practice_bottom_right_8 = visual.Rect(
    win=win, name='practice_bottom_right_8',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(0.14,-0.4), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-5.0, interpolate=True)
practice_bl_text_8 = visual.TextStim(win=win, name='practice_bl_text_8',
    text='',
    font='Arial',
    pos=(-0.14, -0.4), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
practice_br_text_8 = visual.TextStim(win=win, name='practice_br_text_8',
    text='',
    font='Arial',
    pos=(0.14, -0.4), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
practice_mult_8 = visual.TextStim(win=win, name='practice_mult_8',
    text='Multiply your points?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
practice_text_8 = visual.TextStim(win=win, name='practice_text_8',
    text='Each time you win points, you will be able to multiply them, however after waiting some delay',
    font='Arial',
    pos=(0.6, -0.4), height=0.1, wrapWidth=0.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
practice_cont_8 = visual.TextStim(win=win, name='practice_cont_8',
    text='click HERE to start your first game',
    font='Arial',
    pos=(0, -0.8), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
practice_mouse_8 = event.Mouse(win=win)
x, y = [None, None]
practice_mouse_8.mouseClock = core.Clock()

# --- Initialize components for Routine "OP_introduction" ---
o_intro_text = visual.TextStim(win=win, name='o_intro_text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
o_intro_avatar_p = visual.ImageStim(
    win=win,
    name='o_intro_avatar_p', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0.55, 0.3), size=(0.0875, 0.153125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
o_intro_avatar_o = visual.ImageStim(
    win=win,
    name='o_intro_avatar_o', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0.55, -0.2), size=(0.0875, 0.153125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
o_intro_cont = visual.TextStim(win=win, name='o_intro_cont',
    text='click HERE to continue',
    font='Arial',
    pos=(0, -0.8), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
o_intro_mouse = event.Mouse(win=win)
x, y = [None, None]
o_intro_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "trial" ---
# Run 'Begin Experiment' code from trial_code
import random
button_list = ['Cooperate', 'Defect']
button_list_dd=['Yes', 'No']
choice_list = []
choice_list_dd=[]

increment=0.2
mult=2
participant_points_total = 0
other_points_total = 0
trial_avatar_o = visual.ImageStim(
    win=win,
    name='trial_avatar_o', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-0.8, 0), size=(0.0875, 0.153125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
trial_avatar_p = visual.ImageStim(
    win=win,
    name='trial_avatar_p', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-0.2, 0.7), size=(0.0875, 0.153125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
top_left = visual.Rect(
    win=win, name='top_left',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(-0.14,0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-3.0, interpolate=True)
top_right = visual.Rect(
    win=win, name='top_right',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(0.14,0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-4.0, interpolate=True)
bottom_left = visual.Rect(
    win=win, name='bottom_left',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(-0.14,-0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-5.0, interpolate=True)
bottom_right = visual.Rect(
    win=win, name='bottom_right',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(0.14,-0.25), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-6.0, interpolate=True)
trial_tl_p = visual.TextStim(win=win, name='trial_tl_p',
    text='',
    font='Arial',
    pos=(-0.2,0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
trial_tl_o = visual.TextStim(win=win, name='trial_tl_o',
    text='',
    font='Arial',
    pos=(-0.1,0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
trial_bl_p = visual.TextStim(win=win, name='trial_bl_p',
    text='',
    font='Arial',
    pos=(-0.2,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
trial_bl_o = visual.TextStim(win=win, name='trial_bl_o',
    text='',
    font='Arial',
    pos=(-0.1,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
trial_tr_p = visual.TextStim(win=win, name='trial_tr_p',
    text='',
    font='Arial',
    pos=(0.1,0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
trial_tr_o = visual.TextStim(win=win, name='trial_tr_o',
    text='',
    font='Arial',
    pos=(0.2,0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
trial_br_p = visual.TextStim(win=win, name='trial_br_p',
    text='',
    font='Arial',
    pos=(0.1,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
trial_br_o = visual.TextStim(win=win, name='trial_br_o',
    text='',
    font='Arial',
    pos=(0.2,-0.25), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
topleft_header = visual.TextStim(win=win, name='topleft_header',
    text='Cooperate',
    font='Arial',
    pos=(-0.13,0.57), height=0.08, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
topright_header = visual.TextStim(win=win, name='topright_header',
    text='Defect',
    font='Arial',
    pos=(0.13,0.57), height=0.08, wrapWidth=None, ori=0, 
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
bottomtop_header = visual.TextStim(win=win, name='bottomtop_header',
    text='Cooperate',
    font='Arial',
    pos=(-0.4,0.25), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
bottombottom_header = visual.TextStim(win=win, name='bottombottom_header',
    text='Defect',
    font='Arial',
    pos=(-0.4,-0.25), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
trial_header_p = visual.TextStim(win=win, name='trial_header_p',
    text='',
    font='Arial',
    pos=(0, 0.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);
trial_header_o = visual.TextStim(win=win, name='trial_header_o',
    text='',
    font='Arial',
    pos=(-0.6, 0), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-20.0);
left_choice = visual.Rect(
    win=win, name='left_choice',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0, pos=(-0.2, -0.7), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=0.2, depth=-21.0, interpolate=True)
leftchoice_text = visual.TextStim(win=win, name='leftchoice_text',
    text='',
    font='Arial',
    pos=(-0.2, -0.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-22.0);
right_choice = visual.Rect(
    win=win, name='right_choice',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0, pos=(0.2, -0.7), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=0.2, depth=-23.0, interpolate=True)
rightchoice_text = visual.TextStim(win=win, name='rightchoice_text',
    text='',
    font='Arial',
    pos=(0.2, -0.7), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-24.0);
trial_mouse = event.Mouse(win=win)
x, y = [None, None]
trial_mouse.mouseClock = core.Clock()
make_your_choice_text = visual.TextStim(win=win, name='make_your_choice_text',
    text='',
    font='Arial',
    pos=(0, -0.9), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-26.0);

# --- Initialize components for Routine "multiply" ---
mult_avatar_o = visual.ImageStim(
    win=win,
    name='mult_avatar_o', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-0.5, 0.3), size=(0.13125, 0.2296875),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
mult_avatar_p = visual.ImageStim(
    win=win,
    name='mult_avatar_p', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-0.5, 0.7), size=(0.13125, 0.2296875),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
mult_choice_p = visual.TextStim(win=win, name='mult_choice_p',
    text='',
    font='Arial',
    pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
mult_choice_o = visual.TextStim(win=win, name='mult_choice_o',
    text='',
    font='Arial',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
mult_points_p = visual.TextStim(win=win, name='mult_points_p',
    text='',
    font='Arial',
    pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
mult_points_o = visual.TextStim(win=win, name='mult_points_o',
    text='',
    font='Arial',
    pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
mult_left = visual.Rect(
    win=win, name='mult_left',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(-0.14,-0.4), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-7.0, interpolate=True)
mult_left_text = visual.TextStim(win=win, name='mult_left_text',
    text='',
    font='Arial',
    pos=(-0.14, -0.4), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
mult_right = visual.Rect(
    win=win, name='mult_right',
    width=(0.28, 0.5)[0], height=(0.28, 0.5)[1],
    ori=0, pos=(0.14,-0.4), anchor='center',
    lineWidth=2,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=1, depth=-9.0, interpolate=True)
mult_right_text = visual.TextStim(win=win, name='mult_right_text',
    text='',
    font='Arial',
    pos=(0.14, -0.4), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
mult_mult = visual.TextStim(win=win, name='mult_mult',
    text='Multiply your points?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
make_your_choice_text_2 = visual.TextStim(win=win, name='make_your_choice_text_2',
    text='',
    font='Arial',
    pos=(0, -0.9), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
mult_mouse = event.Mouse(win=win)
x, y = [None, None]
mult_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "feedback" ---
feedback_scoreboard_o = visual.ImageStim(
    win=win,
    name='feedback_scoreboard_o', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.07, 0.1225),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
feedback_scoreboard_p = visual.ImageStim(
    win=win,
    name='feedback_scoreboard_p', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.07, 0.1225),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
feedback_avatar_o = visual.ImageStim(
    win=win,
    name='feedback_avatar_o', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-0.5, 0.2), size=(0.13125, 0.2296875),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
feedback_avatar_p = visual.ImageStim(
    win=win,
    name='feedback_avatar_p', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(-0.5, 0.6), size=(0.13125, 0.2296875),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
feedback_choice_p = visual.TextStim(win=win, name='feedback_choice_p',
    text='',
    font='Arial',
    pos=(0, 0.7), height=0.12, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
feedback_choice_o = visual.TextStim(win=win, name='feedback_choice_o',
    text='',
    font='Arial',
    pos=(0, 0.3), height=0.12, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
feedback_points_p = visual.TextStim(win=win, name='feedback_points_p',
    text='',
    font='Arial',
    pos=(0, 0.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
feedback_points_o = visual.TextStim(win=win, name='feedback_points_o',
    text='',
    font='Arial',
    pos=(0, 0.1), height=0.1, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
feedback_total_p = visual.TextStim(win=win, name='feedback_total_p',
    text='',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
feedback_total_o = visual.TextStim(win=win, name='feedback_total_o',
    text='',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
feedback_name_p = visual.TextStim(win=win, name='feedback_name_p',
    text='',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
feedback_name_o = visual.TextStim(win=win, name='feedback_name_o',
    text='',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
feedback_scoreboard = visual.TextStim(win=win, name='feedback_scoreboard',
    text='Total Points',
    font='Arial',
    pos=(0, -0.3), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
feedback_cont = visual.TextStim(win=win, name='feedback_cont',
    text='click HERE for next trial',
    font='Arial',
    pos=(0, -0.9), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
feedback_mouse = event.Mouse(win=win)
x, y = [None, None]
feedback_mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "score" ---
p_total_text = visual.TextStim(win=win, name='p_total_text',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
o_total_text = visual.TextStim(win=win, name='o_total_text',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
participant_avatar_scoreboard = visual.ImageStim(
    win=win,
    name='participant_avatar_scoreboard', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.175, 0.30625),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
p_name_text = visual.TextStim(win=win, name='p_name_text',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
o_name_text = visual.TextStim(win=win, name='o_name_text',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
other_avatar_scoreboard = visual.ImageStim(
    win=win,
    name='other_avatar_scoreboard', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=[0,0], size=(0.175, 0.30625),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
name_header = visual.TextStim(win=win, name='name_header',
    text='Player',
    font='Arial',
    pos=(-0.15, 0.5), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
total_point_header = visual.TextStim(win=win, name='total_point_header',
    text='Total Points',
    font='Arial',
    pos=(0.3, 0.5), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
scoreboard_cont_text = visual.TextStim(win=win, name='scoreboard_cont_text',
    text='',
    font='Arial',
    pos=(0, -0.8), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
scoreabord_mouse = event.Mouse(win=win)
x, y = [None, None]
scoreabord_mouse.mouseClock = core.Clock()
scoreboard_intro_text = visual.TextStim(win=win, name='scoreboard_intro_text',
    text='',
    font='Arial',
    pos=(0, 0.8), height=0.09, wrapWidth=1.2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);

# --- Initialize components for Routine "finish" ---
end_routine_text = visual.TextStim(win=win, name='end_routine_text',
    text='Well done you have finished the task!\n\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_routine_continue_text = visual.TextStim(win=win, name='end_routine_continue_text',
    text='click HERE to close the task',
    font='Arial',
    pos=(0, -0.5), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
end_routine_mouse = event.Mouse(win=win)
x, y = [None, None]
end_routine_mouse.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "start" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the start_mouse
start_mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
startComponents = [start_text, start_cont, start_mouse]
for thisComponent in startComponents:
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

# --- Run Routine "start" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_text* updates
    if start_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_text.frameNStart = frameN  # exact frame index
        start_text.tStart = t  # local t and not account for scr refresh
        start_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_text, 'tStartRefresh')  # time at next scr refresh
        start_text.setAutoDraw(True)
    
    # *start_cont* updates
    if start_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_cont.frameNStart = frameN  # exact frame index
        start_cont.tStart = t  # local t and not account for scr refresh
        start_cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_cont, 'tStartRefresh')  # time at next scr refresh
        start_cont.setAutoDraw(True)
    # *start_mouse* updates
    if start_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_mouse.frameNStart = frameN  # exact frame index
        start_mouse.tStart = t  # local t and not account for scr refresh
        start_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_mouse, 'tStartRefresh')  # time at next scr refresh
        start_mouse.status = STARTED
        start_mouse.mouseClock.reset()
        prevButtonState = start_mouse.getPressed()  # if button is down already this ISN'T a new click
    if start_mouse.status == STARTED:  # only update if started and not finished!
        buttons = start_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(start_cont)
                    clickableList = start_cont
                except:
                    clickableList = [start_cont]
                for obj in clickableList:
                    if obj.contains(start_mouse):
                        gotValidClick = True
                        start_mouse.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "start" ---
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = start_mouse.getPos()
buttons = start_mouse.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(start_cont)
        clickableList = start_cont
    except:
        clickableList = [start_cont]
    for obj in clickableList:
        if obj.contains(start_mouse):
            gotValidClick = True
            start_mouse.clicked_name.append(obj.name)
thisExp.addData('start_mouse.x', x)
thisExp.addData('start_mouse.y', y)
thisExp.addData('start_mouse.leftButton', buttons[0])
thisExp.addData('start_mouse.midButton', buttons[1])
thisExp.addData('start_mouse.rightButton', buttons[2])
if len(start_mouse.clicked_name):
    thisExp.addData('start_mouse.clicked_name', start_mouse.clicked_name[0])
thisExp.nextEntry()
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "name" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
type_name.reset()
# setup some python lists for storing info about the name_mouse
name_mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
nameComponents = [name_text, type_name, name_cont, name_mouse]
for thisComponent in nameComponents:
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

# --- Run Routine "name" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *name_text* updates
    if name_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        name_text.frameNStart = frameN  # exact frame index
        name_text.tStart = t  # local t and not account for scr refresh
        name_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(name_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'name_text.started')
        name_text.setAutoDraw(True)
    
    # *type_name* updates
    if type_name.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        type_name.frameNStart = frameN  # exact frame index
        type_name.tStart = t  # local t and not account for scr refresh
        type_name.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(type_name, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'type_name.started')
        type_name.setAutoDraw(True)
    
    # *name_cont* updates
    if name_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        name_cont.frameNStart = frameN  # exact frame index
        name_cont.tStart = t  # local t and not account for scr refresh
        name_cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(name_cont, 'tStartRefresh')  # time at next scr refresh
        name_cont.setAutoDraw(True)
    # *name_mouse* updates
    if name_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        name_mouse.frameNStart = frameN  # exact frame index
        name_mouse.tStart = t  # local t and not account for scr refresh
        name_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(name_mouse, 'tStartRefresh')  # time at next scr refresh
        name_mouse.status = STARTED
        name_mouse.mouseClock.reset()
        prevButtonState = name_mouse.getPressed()  # if button is down already this ISN'T a new click
    if name_mouse.status == STARTED:  # only update if started and not finished!
        buttons = name_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(name_cont)
                    clickableList = name_cont
                except:
                    clickableList = [name_cont]
                for obj in clickableList:
                    if obj.contains(name_mouse):
                        gotValidClick = True
                        name_mouse.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in nameComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "name" ---
for thisComponent in nameComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from username_code
username = type_name.text
thisExp.addData('type_name.text',type_name.text)
# store data for thisExp (ExperimentHandler)
x, y = name_mouse.getPos()
buttons = name_mouse.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(name_cont)
        clickableList = name_cont
    except:
        clickableList = [name_cont]
    for obj in clickableList:
        if obj.contains(name_mouse):
            gotValidClick = True
            name_mouse.clicked_name.append(obj.name)
thisExp.addData('name_mouse.x', x)
thisExp.addData('name_mouse.y', y)
thisExp.addData('name_mouse.leftButton', buttons[0])
thisExp.addData('name_mouse.midButton', buttons[1])
thisExp.addData('name_mouse.rightButton', buttons[2])
if len(name_mouse.clicked_name):
    thisExp.addData('name_mouse.clicked_name', name_mouse.clicked_name[0])
thisExp.nextEntry()
# the Routine "name" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "avatar" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the avatar_mouse
gotValidClick = False  # until a click is received
# keep track of which components have finished
avatarComponents = [avatar_text, avatar1, avatar2, avatar3, avatar4, avatar5, avatar6, avatar_mouse]
for thisComponent in avatarComponents:
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

# --- Run Routine "avatar" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # Run 'Each Frame' code from avatar_code
    #Saying what avatar has been selected
    if avatar_mouse.isPressedIn(avatar1):
        continueRoutine = False
        thisExp.addData('selected_avatar', 'avatar1')
        chosen_avatar = "avatar1.png"
        unselected_avatar = ['avatar2.png', 'avatar3.png', 'avatar4.png', 'avatar5.png', 'avatar6.png']
    elif avatar_mouse.isPressedIn(avatar2):
        continueRoutine = False
        thisExp.addData('selected_avatar', 'avatar2')
        chosen_avatar = "avatar2.png"
        unselected_avatar = ['avatar1.png', 'avatar3.png', 'avatar4.png', 'avatar5.png', 'avatar6.png']
    elif avatar_mouse.isPressedIn(avatar3):
        continueRoutine = False
        thisExp.addData('selected_avatar', 'avatar3')
        chosen_avatar = "avatar3.png"
        unselected_avatar = ['avatar1.png', 'avatar2.png', 'avatar4.png', 'avatar5.png', 'avatar6.png']
    elif avatar_mouse.isPressedIn(avatar4):
        continueRoutine = False
        thisExp.addData('selected_avatar', 'avatar4')
        chosen_avatar = "avatar4.png"
        unselected_avatar = ['avatar1.png', 'avatar2.png', 'avatar3.png', 'avatar5.png', 'avatar6.png']
    elif avatar_mouse.isPressedIn(avatar5):
        continueRoutine = False
        thisExp.addData('selected_avatar', 'avatar5')
        chosen_avatar = "avatar5.png"
        unselected_avatar = ['avatar1.png', 'avatar2.png', 'avatar3.png', 'avatar4.png', 'avatar6.png']
    elif avatar_mouse.isPressedIn(avatar6):
        continueRoutine = False
        thisExp.addData('selected_avatar', 'avatar6')
        chosen_avatar = "avatar6.png"
        unselected_avatar = ['avatar1.png', 'avatar2.png', 'avatar3.png', 'avatar4.png', 'avatar5.png']
    
    # *avatar_text* updates
    if avatar_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        avatar_text.frameNStart = frameN  # exact frame index
        avatar_text.tStart = t  # local t and not account for scr refresh
        avatar_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(avatar_text, 'tStartRefresh')  # time at next scr refresh
        avatar_text.setAutoDraw(True)
    
    # *avatar1* updates
    if avatar1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        avatar1.frameNStart = frameN  # exact frame index
        avatar1.tStart = t  # local t and not account for scr refresh
        avatar1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(avatar1, 'tStartRefresh')  # time at next scr refresh
        avatar1.setAutoDraw(True)
    
    # *avatar2* updates
    if avatar2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        avatar2.frameNStart = frameN  # exact frame index
        avatar2.tStart = t  # local t and not account for scr refresh
        avatar2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(avatar2, 'tStartRefresh')  # time at next scr refresh
        avatar2.setAutoDraw(True)
    
    # *avatar3* updates
    if avatar3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        avatar3.frameNStart = frameN  # exact frame index
        avatar3.tStart = t  # local t and not account for scr refresh
        avatar3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(avatar3, 'tStartRefresh')  # time at next scr refresh
        avatar3.setAutoDraw(True)
    
    # *avatar4* updates
    if avatar4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        avatar4.frameNStart = frameN  # exact frame index
        avatar4.tStart = t  # local t and not account for scr refresh
        avatar4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(avatar4, 'tStartRefresh')  # time at next scr refresh
        avatar4.setAutoDraw(True)
    
    # *avatar5* updates
    if avatar5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        avatar5.frameNStart = frameN  # exact frame index
        avatar5.tStart = t  # local t and not account for scr refresh
        avatar5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(avatar5, 'tStartRefresh')  # time at next scr refresh
        avatar5.setAutoDraw(True)
    
    # *avatar6* updates
    if avatar6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        avatar6.frameNStart = frameN  # exact frame index
        avatar6.tStart = t  # local t and not account for scr refresh
        avatar6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(avatar6, 'tStartRefresh')  # time at next scr refresh
        avatar6.setAutoDraw(True)
    # *avatar_mouse* updates
    if avatar_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        avatar_mouse.frameNStart = frameN  # exact frame index
        avatar_mouse.tStart = t  # local t and not account for scr refresh
        avatar_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(avatar_mouse, 'tStartRefresh')  # time at next scr refresh
        avatar_mouse.status = STARTED
        avatar_mouse.mouseClock.reset()
        prevButtonState = avatar_mouse.getPressed()  # if button is down already this ISN'T a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in avatarComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "avatar" ---
for thisComponent in avatarComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = avatar_mouse.getPos()
buttons = avatar_mouse.getPressed()
thisExp.addData('avatar_mouse.x', x)
thisExp.addData('avatar_mouse.y', y)
thisExp.addData('avatar_mouse.leftButton', buttons[0])
thisExp.addData('avatar_mouse.midButton', buttons[1])
thisExp.addData('avatar_mouse.rightButton', buttons[2])
thisExp.nextEntry()
# the Routine "avatar" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "intro" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the intro_mouse
intro_mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
introComponents = [intro_text, intro_cont, intro_mouse]
for thisComponent in introComponents:
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

# --- Run Routine "intro" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_text* updates
    if intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_text.frameNStart = frameN  # exact frame index
        intro_text.tStart = t  # local t and not account for scr refresh
        intro_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_text, 'tStartRefresh')  # time at next scr refresh
        intro_text.setAutoDraw(True)
    
    # *intro_cont* updates
    if intro_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_cont.frameNStart = frameN  # exact frame index
        intro_cont.tStart = t  # local t and not account for scr refresh
        intro_cont.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_cont, 'tStartRefresh')  # time at next scr refresh
        intro_cont.setAutoDraw(True)
    # *intro_mouse* updates
    if intro_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_mouse.frameNStart = frameN  # exact frame index
        intro_mouse.tStart = t  # local t and not account for scr refresh
        intro_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_mouse, 'tStartRefresh')  # time at next scr refresh
        intro_mouse.status = STARTED
        intro_mouse.mouseClock.reset()
        prevButtonState = intro_mouse.getPressed()  # if button is down already this ISN'T a new click
    if intro_mouse.status == STARTED:  # only update if started and not finished!
        buttons = intro_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(intro_cont)
                    clickableList = intro_cont
                except:
                    clickableList = [intro_cont]
                for obj in clickableList:
                    if obj.contains(intro_mouse):
                        gotValidClick = True
                        intro_mouse.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "intro" ---
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('payoff_matrices_intro.xlsx'),
    seed=None, name='practice_loop')
thisExp.addLoop(practice_loop)  # add the loop to the experiment
thisPractice_loop = practice_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
if thisPractice_loop != None:
    for paramName in thisPractice_loop:
        exec('{} = thisPractice_loop[paramName]'.format(paramName))

for thisPractice_loop in practice_loop:
    currentLoop = practice_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
    if thisPractice_loop != None:
        for paramName in thisPractice_loop:
            exec('{} = thisPractice_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "practice_trial_1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    practice_avatar_1.setImage(chosen_avatar)
    practice_points_tl_p_1.setText(tl_p_intro)
    practice_points_tl_o_1.setText(tl_o_intro)
    practice_points_bl_p_1.setText(bl_p_intro

)
    practice_points_bl_o_1.setText(bl_o_intro)
    practice_points_tr_p_1.setText(tr_p_intro)
    practice_points_tr_o_1.setText(tr_o_intro)
    practice_points_br_p_1.setText(br_p_intro)
    practice_points_br_o_1.setText(br_o_intro)
    practice_p_header_1.setText(username)
    # setup some python lists for storing info about the practice_mouse_1
    practice_mouse_1.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    practice_trial_1Components = [practice_avatar_1, practice_top_left_1, practice_top_right_1, practice_bottom_left_1, practice_bottom_right_1, practice_points_tl_p_1, practice_points_tl_o_1, practice_points_bl_p_1, practice_points_bl_o_1, practice_points_tr_p_1, practice_points_tr_o_1, practice_points_br_p_1, practice_points_br_o_1, practice_tr_header_1, practice_bt_header_1, practice_p_header_1, practice_o_header_1, practice_bb_header_1, practice_tl_header_1, practice_text_1, practice_cont_1, practice_mouse_1]
    for thisComponent in practice_trial_1Components:
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
    
    # --- Run Routine "practice_trial_1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_avatar_1* updates
        if practice_avatar_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_avatar_1.frameNStart = frameN  # exact frame index
            practice_avatar_1.tStart = t  # local t and not account for scr refresh
            practice_avatar_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_avatar_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_avatar_1.started')
            practice_avatar_1.setAutoDraw(True)
        
        # *practice_top_left_1* updates
        if practice_top_left_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_top_left_1.frameNStart = frameN  # exact frame index
            practice_top_left_1.tStart = t  # local t and not account for scr refresh
            practice_top_left_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_top_left_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_top_left_1.started')
            practice_top_left_1.setAutoDraw(True)
        
        # *practice_top_right_1* updates
        if practice_top_right_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_top_right_1.frameNStart = frameN  # exact frame index
            practice_top_right_1.tStart = t  # local t and not account for scr refresh
            practice_top_right_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_top_right_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_top_right_1.started')
            practice_top_right_1.setAutoDraw(True)
        
        # *practice_bottom_left_1* updates
        if practice_bottom_left_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bottom_left_1.frameNStart = frameN  # exact frame index
            practice_bottom_left_1.tStart = t  # local t and not account for scr refresh
            practice_bottom_left_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bottom_left_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bottom_left_1.started')
            practice_bottom_left_1.setAutoDraw(True)
        
        # *practice_bottom_right_1* updates
        if practice_bottom_right_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bottom_right_1.frameNStart = frameN  # exact frame index
            practice_bottom_right_1.tStart = t  # local t and not account for scr refresh
            practice_bottom_right_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bottom_right_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bottom_right_1.started')
            practice_bottom_right_1.setAutoDraw(True)
        
        # *practice_points_tl_p_1* updates
        if practice_points_tl_p_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tl_p_1.frameNStart = frameN  # exact frame index
            practice_points_tl_p_1.tStart = t  # local t and not account for scr refresh
            practice_points_tl_p_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tl_p_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tl_p_1.started')
            practice_points_tl_p_1.setAutoDraw(True)
        
        # *practice_points_tl_o_1* updates
        if practice_points_tl_o_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tl_o_1.frameNStart = frameN  # exact frame index
            practice_points_tl_o_1.tStart = t  # local t and not account for scr refresh
            practice_points_tl_o_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tl_o_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tl_o_1.started')
            practice_points_tl_o_1.setAutoDraw(True)
        
        # *practice_points_bl_p_1* updates
        if practice_points_bl_p_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_bl_p_1.frameNStart = frameN  # exact frame index
            practice_points_bl_p_1.tStart = t  # local t and not account for scr refresh
            practice_points_bl_p_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_bl_p_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_bl_p_1.started')
            practice_points_bl_p_1.setAutoDraw(True)
        
        # *practice_points_bl_o_1* updates
        if practice_points_bl_o_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_bl_o_1.frameNStart = frameN  # exact frame index
            practice_points_bl_o_1.tStart = t  # local t and not account for scr refresh
            practice_points_bl_o_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_bl_o_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_bl_o_1.started')
            practice_points_bl_o_1.setAutoDraw(True)
        
        # *practice_points_tr_p_1* updates
        if practice_points_tr_p_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tr_p_1.frameNStart = frameN  # exact frame index
            practice_points_tr_p_1.tStart = t  # local t and not account for scr refresh
            practice_points_tr_p_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tr_p_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tr_p_1.started')
            practice_points_tr_p_1.setAutoDraw(True)
        
        # *practice_points_tr_o_1* updates
        if practice_points_tr_o_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tr_o_1.frameNStart = frameN  # exact frame index
            practice_points_tr_o_1.tStart = t  # local t and not account for scr refresh
            practice_points_tr_o_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tr_o_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tr_o_1.started')
            practice_points_tr_o_1.setAutoDraw(True)
        
        # *practice_points_br_p_1* updates
        if practice_points_br_p_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_br_p_1.frameNStart = frameN  # exact frame index
            practice_points_br_p_1.tStart = t  # local t and not account for scr refresh
            practice_points_br_p_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_br_p_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_br_p_1.started')
            practice_points_br_p_1.setAutoDraw(True)
        
        # *practice_points_br_o_1* updates
        if practice_points_br_o_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_br_o_1.frameNStart = frameN  # exact frame index
            practice_points_br_o_1.tStart = t  # local t and not account for scr refresh
            practice_points_br_o_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_br_o_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_br_o_1.started')
            practice_points_br_o_1.setAutoDraw(True)
        
        # *practice_tr_header_1* updates
        if practice_tr_header_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_tr_header_1.frameNStart = frameN  # exact frame index
            practice_tr_header_1.tStart = t  # local t and not account for scr refresh
            practice_tr_header_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_tr_header_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_tr_header_1.started')
            practice_tr_header_1.setAutoDraw(True)
        
        # *practice_bt_header_1* updates
        if practice_bt_header_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bt_header_1.frameNStart = frameN  # exact frame index
            practice_bt_header_1.tStart = t  # local t and not account for scr refresh
            practice_bt_header_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bt_header_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bt_header_1.started')
            practice_bt_header_1.setAutoDraw(True)
        
        # *practice_p_header_1* updates
        if practice_p_header_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_p_header_1.frameNStart = frameN  # exact frame index
            practice_p_header_1.tStart = t  # local t and not account for scr refresh
            practice_p_header_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_p_header_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_p_header_1.started')
            practice_p_header_1.setAutoDraw(True)
        
        # *practice_o_header_1* updates
        if practice_o_header_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_o_header_1.frameNStart = frameN  # exact frame index
            practice_o_header_1.tStart = t  # local t and not account for scr refresh
            practice_o_header_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_o_header_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_o_header_1.started')
            practice_o_header_1.setAutoDraw(True)
        
        # *practice_bb_header_1* updates
        if practice_bb_header_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bb_header_1.frameNStart = frameN  # exact frame index
            practice_bb_header_1.tStart = t  # local t and not account for scr refresh
            practice_bb_header_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bb_header_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bb_header_1.started')
            practice_bb_header_1.setAutoDraw(True)
        
        # *practice_tl_header_1* updates
        if practice_tl_header_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_tl_header_1.frameNStart = frameN  # exact frame index
            practice_tl_header_1.tStart = t  # local t and not account for scr refresh
            practice_tl_header_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_tl_header_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_tl_header_1.started')
            practice_tl_header_1.setAutoDraw(True)
        
        # *practice_text_1* updates
        if practice_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_text_1.frameNStart = frameN  # exact frame index
            practice_text_1.tStart = t  # local t and not account for scr refresh
            practice_text_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_text_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_text_1.started')
            practice_text_1.setAutoDraw(True)
        
        # *practice_cont_1* updates
        if practice_cont_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_cont_1.frameNStart = frameN  # exact frame index
            practice_cont_1.tStart = t  # local t and not account for scr refresh
            practice_cont_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_cont_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_cont_1.started')
            practice_cont_1.setAutoDraw(True)
        # *practice_mouse_1* updates
        if practice_mouse_1.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_mouse_1.frameNStart = frameN  # exact frame index
            practice_mouse_1.tStart = t  # local t and not account for scr refresh
            practice_mouse_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_mouse_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('practice_mouse_1.started', t)
            practice_mouse_1.status = STARTED
            practice_mouse_1.mouseClock.reset()
            prevButtonState = practice_mouse_1.getPressed()  # if button is down already this ISN'T a new click
        if practice_mouse_1.status == STARTED:  # only update if started and not finished!
            buttons = practice_mouse_1.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(practice_cont_1)
                        clickableList = practice_cont_1
                    except:
                        clickableList = [practice_cont_1]
                    for obj in clickableList:
                        if obj.contains(practice_mouse_1):
                            gotValidClick = True
                            practice_mouse_1.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_trial_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_trial_1" ---
    for thisComponent in practice_trial_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practice_loop (TrialHandler)
    # the Routine "practice_trial_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice_trial_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    practice_avatar_2.setImage(chosen_avatar)
    practice_points_tl_p_2.setText(tl_p_intro)
    practice_points_tl_o_2.setText(tl_o_intro)
    practice_points_bl_p_2.setText(bl_p_intro

)
    practice_points_bl_o_2.setText(bl_o_intro)
    practice_points_tr_p_2.setText(tr_p_intro)
    practice_points_tr_o_2.setText(tr_o_intro)
    practice_points_br_p_2.setText(br_p_intro)
    practice_points_br_o_2.setText(br_o_intro)
    practice_p_header_2.setText(username)
    # setup some python lists for storing info about the practice_mouse_2
    practice_mouse_2.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    practice_trial_2Components = [practice_avatar_2, practice_top_left_2, practice_top_right_2, practice_bottom_left_2, practice_bottom_right_2, practice_points_tl_p_2, practice_points_tl_o_2, practice_points_bl_p_2, practice_points_bl_o_2, practice_points_tr_p_2, practice_points_tr_o_2, practice_points_br_p_2, practice_points_br_o_2, practice_tr_header_2, practice_bt_header_2, practice_p_header_2, practice_o_header_2, practice_bb_header_2, practice_tl_header_2, practice_text_2, practice_cont_2, practice_mouse_2]
    for thisComponent in practice_trial_2Components:
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
    
    # --- Run Routine "practice_trial_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_avatar_2* updates
        if practice_avatar_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_avatar_2.frameNStart = frameN  # exact frame index
            practice_avatar_2.tStart = t  # local t and not account for scr refresh
            practice_avatar_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_avatar_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_avatar_2.started')
            practice_avatar_2.setAutoDraw(True)
        
        # *practice_top_left_2* updates
        if practice_top_left_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_top_left_2.frameNStart = frameN  # exact frame index
            practice_top_left_2.tStart = t  # local t and not account for scr refresh
            practice_top_left_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_top_left_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_top_left_2.started')
            practice_top_left_2.setAutoDraw(True)
        
        # *practice_top_right_2* updates
        if practice_top_right_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_top_right_2.frameNStart = frameN  # exact frame index
            practice_top_right_2.tStart = t  # local t and not account for scr refresh
            practice_top_right_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_top_right_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_top_right_2.started')
            practice_top_right_2.setAutoDraw(True)
        
        # *practice_bottom_left_2* updates
        if practice_bottom_left_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bottom_left_2.frameNStart = frameN  # exact frame index
            practice_bottom_left_2.tStart = t  # local t and not account for scr refresh
            practice_bottom_left_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bottom_left_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bottom_left_2.started')
            practice_bottom_left_2.setAutoDraw(True)
        
        # *practice_bottom_right_2* updates
        if practice_bottom_right_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bottom_right_2.frameNStart = frameN  # exact frame index
            practice_bottom_right_2.tStart = t  # local t and not account for scr refresh
            practice_bottom_right_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bottom_right_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bottom_right_2.started')
            practice_bottom_right_2.setAutoDraw(True)
        
        # *practice_points_tl_p_2* updates
        if practice_points_tl_p_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tl_p_2.frameNStart = frameN  # exact frame index
            practice_points_tl_p_2.tStart = t  # local t and not account for scr refresh
            practice_points_tl_p_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tl_p_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tl_p_2.started')
            practice_points_tl_p_2.setAutoDraw(True)
        
        # *practice_points_tl_o_2* updates
        if practice_points_tl_o_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tl_o_2.frameNStart = frameN  # exact frame index
            practice_points_tl_o_2.tStart = t  # local t and not account for scr refresh
            practice_points_tl_o_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tl_o_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tl_o_2.started')
            practice_points_tl_o_2.setAutoDraw(True)
        
        # *practice_points_bl_p_2* updates
        if practice_points_bl_p_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_bl_p_2.frameNStart = frameN  # exact frame index
            practice_points_bl_p_2.tStart = t  # local t and not account for scr refresh
            practice_points_bl_p_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_bl_p_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_bl_p_2.started')
            practice_points_bl_p_2.setAutoDraw(True)
        
        # *practice_points_bl_o_2* updates
        if practice_points_bl_o_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_bl_o_2.frameNStart = frameN  # exact frame index
            practice_points_bl_o_2.tStart = t  # local t and not account for scr refresh
            practice_points_bl_o_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_bl_o_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_bl_o_2.started')
            practice_points_bl_o_2.setAutoDraw(True)
        
        # *practice_points_tr_p_2* updates
        if practice_points_tr_p_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tr_p_2.frameNStart = frameN  # exact frame index
            practice_points_tr_p_2.tStart = t  # local t and not account for scr refresh
            practice_points_tr_p_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tr_p_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tr_p_2.started')
            practice_points_tr_p_2.setAutoDraw(True)
        
        # *practice_points_tr_o_2* updates
        if practice_points_tr_o_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tr_o_2.frameNStart = frameN  # exact frame index
            practice_points_tr_o_2.tStart = t  # local t and not account for scr refresh
            practice_points_tr_o_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tr_o_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tr_o_2.started')
            practice_points_tr_o_2.setAutoDraw(True)
        
        # *practice_points_br_p_2* updates
        if practice_points_br_p_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_br_p_2.frameNStart = frameN  # exact frame index
            practice_points_br_p_2.tStart = t  # local t and not account for scr refresh
            practice_points_br_p_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_br_p_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_br_p_2.started')
            practice_points_br_p_2.setAutoDraw(True)
        
        # *practice_points_br_o_2* updates
        if practice_points_br_o_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_br_o_2.frameNStart = frameN  # exact frame index
            practice_points_br_o_2.tStart = t  # local t and not account for scr refresh
            practice_points_br_o_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_br_o_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_br_o_2.started')
            practice_points_br_o_2.setAutoDraw(True)
        
        # *practice_tr_header_2* updates
        if practice_tr_header_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_tr_header_2.frameNStart = frameN  # exact frame index
            practice_tr_header_2.tStart = t  # local t and not account for scr refresh
            practice_tr_header_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_tr_header_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_tr_header_2.started')
            practice_tr_header_2.setAutoDraw(True)
        
        # *practice_bt_header_2* updates
        if practice_bt_header_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bt_header_2.frameNStart = frameN  # exact frame index
            practice_bt_header_2.tStart = t  # local t and not account for scr refresh
            practice_bt_header_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bt_header_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bt_header_2.started')
            practice_bt_header_2.setAutoDraw(True)
        
        # *practice_p_header_2* updates
        if practice_p_header_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_p_header_2.frameNStart = frameN  # exact frame index
            practice_p_header_2.tStart = t  # local t and not account for scr refresh
            practice_p_header_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_p_header_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_p_header_2.started')
            practice_p_header_2.setAutoDraw(True)
        
        # *practice_o_header_2* updates
        if practice_o_header_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_o_header_2.frameNStart = frameN  # exact frame index
            practice_o_header_2.tStart = t  # local t and not account for scr refresh
            practice_o_header_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_o_header_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_o_header_2.started')
            practice_o_header_2.setAutoDraw(True)
        
        # *practice_bb_header_2* updates
        if practice_bb_header_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bb_header_2.frameNStart = frameN  # exact frame index
            practice_bb_header_2.tStart = t  # local t and not account for scr refresh
            practice_bb_header_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bb_header_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bb_header_2.started')
            practice_bb_header_2.setAutoDraw(True)
        
        # *practice_tl_header_2* updates
        if practice_tl_header_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_tl_header_2.frameNStart = frameN  # exact frame index
            practice_tl_header_2.tStart = t  # local t and not account for scr refresh
            practice_tl_header_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_tl_header_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_tl_header_2.started')
            practice_tl_header_2.setAutoDraw(True)
        
        # *practice_text_2* updates
        if practice_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_text_2.frameNStart = frameN  # exact frame index
            practice_text_2.tStart = t  # local t and not account for scr refresh
            practice_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_text_2.started')
            practice_text_2.setAutoDraw(True)
        
        # *practice_cont_2* updates
        if practice_cont_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_cont_2.frameNStart = frameN  # exact frame index
            practice_cont_2.tStart = t  # local t and not account for scr refresh
            practice_cont_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_cont_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_cont_2.started')
            practice_cont_2.setAutoDraw(True)
        # *practice_mouse_2* updates
        if practice_mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_mouse_2.frameNStart = frameN  # exact frame index
            practice_mouse_2.tStart = t  # local t and not account for scr refresh
            practice_mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_mouse_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('practice_mouse_2.started', t)
            practice_mouse_2.status = STARTED
            practice_mouse_2.mouseClock.reset()
            prevButtonState = practice_mouse_2.getPressed()  # if button is down already this ISN'T a new click
        if practice_mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = practice_mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(practice_cont_2)
                        clickableList = practice_cont_2
                    except:
                        clickableList = [practice_cont_2]
                    for obj in clickableList:
                        if obj.contains(practice_mouse_2):
                            gotValidClick = True
                            practice_mouse_2.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_trial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_trial_2" ---
    for thisComponent in practice_trial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practice_loop (TrialHandler)
    # the Routine "practice_trial_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice_trial_3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    practice_avatar_3.setImage(chosen_avatar)
    practice_points_tl_p_3.setText(tl_p_intro)
    practice_points_tl_o_3.setText(tl_o_intro)
    practice_points_bl_p_3.setText(bl_p_intro

)
    practice_points_bl_o_3.setText(bl_o_intro)
    practice_points_tr_p_3.setText(tr_p_intro)
    practice_points_tr_o_3.setText(tr_o_intro)
    practice_points_br_p_3.setText(br_p_intro)
    practice_points_br_o_3.setText(br_o_intro)
    practice_p_header_3.setText(username)
    # setup some python lists for storing info about the practice_mouse_3
    practice_mouse_3.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    practice_trial_3Components = [practice_avatar_3, practice_top_left_3, practice_top_right_3, practice_bottom_left_3, practice_bottom_right_3, practice_points_tl_p_3, practice_points_tl_o_3, practice_points_bl_p_3, practice_points_bl_o_3, practice_points_tr_p_3, practice_points_tr_o_3, practice_points_br_p_3, practice_points_br_o_3, practice_tr_header_3, practice_bt_header_3, practice_p_header_3, practice_o_header_3, practice_bb_header_3, practice_tl_header_3, practice_text_3, practice_cont_3, practice_mouse_3]
    for thisComponent in practice_trial_3Components:
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
    
    # --- Run Routine "practice_trial_3" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_avatar_3* updates
        if practice_avatar_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_avatar_3.frameNStart = frameN  # exact frame index
            practice_avatar_3.tStart = t  # local t and not account for scr refresh
            practice_avatar_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_avatar_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_avatar_3.started')
            practice_avatar_3.setAutoDraw(True)
        
        # *practice_top_left_3* updates
        if practice_top_left_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_top_left_3.frameNStart = frameN  # exact frame index
            practice_top_left_3.tStart = t  # local t and not account for scr refresh
            practice_top_left_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_top_left_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_top_left_3.started')
            practice_top_left_3.setAutoDraw(True)
        
        # *practice_top_right_3* updates
        if practice_top_right_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_top_right_3.frameNStart = frameN  # exact frame index
            practice_top_right_3.tStart = t  # local t and not account for scr refresh
            practice_top_right_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_top_right_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_top_right_3.started')
            practice_top_right_3.setAutoDraw(True)
        
        # *practice_bottom_left_3* updates
        if practice_bottom_left_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bottom_left_3.frameNStart = frameN  # exact frame index
            practice_bottom_left_3.tStart = t  # local t and not account for scr refresh
            practice_bottom_left_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bottom_left_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bottom_left_3.started')
            practice_bottom_left_3.setAutoDraw(True)
        
        # *practice_bottom_right_3* updates
        if practice_bottom_right_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bottom_right_3.frameNStart = frameN  # exact frame index
            practice_bottom_right_3.tStart = t  # local t and not account for scr refresh
            practice_bottom_right_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bottom_right_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bottom_right_3.started')
            practice_bottom_right_3.setAutoDraw(True)
        
        # *practice_points_tl_p_3* updates
        if practice_points_tl_p_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tl_p_3.frameNStart = frameN  # exact frame index
            practice_points_tl_p_3.tStart = t  # local t and not account for scr refresh
            practice_points_tl_p_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tl_p_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tl_p_3.started')
            practice_points_tl_p_3.setAutoDraw(True)
        
        # *practice_points_tl_o_3* updates
        if practice_points_tl_o_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tl_o_3.frameNStart = frameN  # exact frame index
            practice_points_tl_o_3.tStart = t  # local t and not account for scr refresh
            practice_points_tl_o_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tl_o_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tl_o_3.started')
            practice_points_tl_o_3.setAutoDraw(True)
        
        # *practice_points_bl_p_3* updates
        if practice_points_bl_p_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_bl_p_3.frameNStart = frameN  # exact frame index
            practice_points_bl_p_3.tStart = t  # local t and not account for scr refresh
            practice_points_bl_p_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_bl_p_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_bl_p_3.started')
            practice_points_bl_p_3.setAutoDraw(True)
        
        # *practice_points_bl_o_3* updates
        if practice_points_bl_o_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_bl_o_3.frameNStart = frameN  # exact frame index
            practice_points_bl_o_3.tStart = t  # local t and not account for scr refresh
            practice_points_bl_o_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_bl_o_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_bl_o_3.started')
            practice_points_bl_o_3.setAutoDraw(True)
        
        # *practice_points_tr_p_3* updates
        if practice_points_tr_p_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tr_p_3.frameNStart = frameN  # exact frame index
            practice_points_tr_p_3.tStart = t  # local t and not account for scr refresh
            practice_points_tr_p_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tr_p_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tr_p_3.started')
            practice_points_tr_p_3.setAutoDraw(True)
        
        # *practice_points_tr_o_3* updates
        if practice_points_tr_o_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tr_o_3.frameNStart = frameN  # exact frame index
            practice_points_tr_o_3.tStart = t  # local t and not account for scr refresh
            practice_points_tr_o_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tr_o_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tr_o_3.started')
            practice_points_tr_o_3.setAutoDraw(True)
        
        # *practice_points_br_p_3* updates
        if practice_points_br_p_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_br_p_3.frameNStart = frameN  # exact frame index
            practice_points_br_p_3.tStart = t  # local t and not account for scr refresh
            practice_points_br_p_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_br_p_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_br_p_3.started')
            practice_points_br_p_3.setAutoDraw(True)
        
        # *practice_points_br_o_3* updates
        if practice_points_br_o_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_br_o_3.frameNStart = frameN  # exact frame index
            practice_points_br_o_3.tStart = t  # local t and not account for scr refresh
            practice_points_br_o_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_br_o_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_br_o_3.started')
            practice_points_br_o_3.setAutoDraw(True)
        
        # *practice_tr_header_3* updates
        if practice_tr_header_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_tr_header_3.frameNStart = frameN  # exact frame index
            practice_tr_header_3.tStart = t  # local t and not account for scr refresh
            practice_tr_header_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_tr_header_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_tr_header_3.started')
            practice_tr_header_3.setAutoDraw(True)
        
        # *practice_bt_header_3* updates
        if practice_bt_header_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bt_header_3.frameNStart = frameN  # exact frame index
            practice_bt_header_3.tStart = t  # local t and not account for scr refresh
            practice_bt_header_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bt_header_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bt_header_3.started')
            practice_bt_header_3.setAutoDraw(True)
        
        # *practice_p_header_3* updates
        if practice_p_header_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_p_header_3.frameNStart = frameN  # exact frame index
            practice_p_header_3.tStart = t  # local t and not account for scr refresh
            practice_p_header_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_p_header_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_p_header_3.started')
            practice_p_header_3.setAutoDraw(True)
        
        # *practice_o_header_3* updates
        if practice_o_header_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_o_header_3.frameNStart = frameN  # exact frame index
            practice_o_header_3.tStart = t  # local t and not account for scr refresh
            practice_o_header_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_o_header_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_o_header_3.started')
            practice_o_header_3.setAutoDraw(True)
        
        # *practice_bb_header_3* updates
        if practice_bb_header_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bb_header_3.frameNStart = frameN  # exact frame index
            practice_bb_header_3.tStart = t  # local t and not account for scr refresh
            practice_bb_header_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bb_header_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bb_header_3.started')
            practice_bb_header_3.setAutoDraw(True)
        
        # *practice_tl_header_3* updates
        if practice_tl_header_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_tl_header_3.frameNStart = frameN  # exact frame index
            practice_tl_header_3.tStart = t  # local t and not account for scr refresh
            practice_tl_header_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_tl_header_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_tl_header_3.started')
            practice_tl_header_3.setAutoDraw(True)
        
        # *practice_text_3* updates
        if practice_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_text_3.frameNStart = frameN  # exact frame index
            practice_text_3.tStart = t  # local t and not account for scr refresh
            practice_text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_text_3.started')
            practice_text_3.setAutoDraw(True)
        
        # *practice_cont_3* updates
        if practice_cont_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_cont_3.frameNStart = frameN  # exact frame index
            practice_cont_3.tStart = t  # local t and not account for scr refresh
            practice_cont_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_cont_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_cont_3.started')
            practice_cont_3.setAutoDraw(True)
        # *practice_mouse_3* updates
        if practice_mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_mouse_3.frameNStart = frameN  # exact frame index
            practice_mouse_3.tStart = t  # local t and not account for scr refresh
            practice_mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_mouse_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('practice_mouse_3.started', t)
            practice_mouse_3.status = STARTED
            practice_mouse_3.mouseClock.reset()
            prevButtonState = practice_mouse_3.getPressed()  # if button is down already this ISN'T a new click
        if practice_mouse_3.status == STARTED:  # only update if started and not finished!
            buttons = practice_mouse_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(practice_cont_2)
                        clickableList = practice_cont_2
                    except:
                        clickableList = [practice_cont_2]
                    for obj in clickableList:
                        if obj.contains(practice_mouse_3):
                            gotValidClick = True
                            practice_mouse_3.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_trial_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_trial_3" ---
    for thisComponent in practice_trial_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practice_loop (TrialHandler)
    # the Routine "practice_trial_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice_trial_4" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    practice_avatar_4.setImage(chosen_avatar)
    practice_points_tl_p_4.setText(tl_p_intro)
    practice_points_tl_o_4.setText(tl_o_intro)
    practice_points_bl_p_4.setText(bl_p_intro

)
    practice_points_bl_o_4.setText(bl_o_intro)
    practice_points_tr_p_4.setText(tr_p_intro)
    practice_points_tr_o_4.setText(tr_o_intro)
    practice_points_br_p_4.setText(br_p_intro)
    practice_points_br_o_4.setText(br_o_intro)
    practice_p_header_4.setText(username)
    # setup some python lists for storing info about the practice_mouse_4
    practice_mouse_4.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    practice_trial_4Components = [practice_avatar_4, practice_top_left_4, practice_top_right_4, practice_bottom_left_4, practice_bottom_right_4, practice_points_tl_p_4, practice_points_tl_o_4, practice_points_bl_p_4, practice_points_bl_o_4, practice_points_tr_p_4, practice_points_tr_o_4, practice_points_br_p_4, practice_points_br_o_4, practice_tr_header_4, practice_bt_header_4, practice_p_header_4, practice_o_header_4, practice_bb_header_4, practice_tl_header_4, practice_text_4, practice_cont_4, practice_mouse_4]
    for thisComponent in practice_trial_4Components:
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
    
    # --- Run Routine "practice_trial_4" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_avatar_4* updates
        if practice_avatar_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_avatar_4.frameNStart = frameN  # exact frame index
            practice_avatar_4.tStart = t  # local t and not account for scr refresh
            practice_avatar_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_avatar_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_avatar_4.started')
            practice_avatar_4.setAutoDraw(True)
        
        # *practice_top_left_4* updates
        if practice_top_left_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_top_left_4.frameNStart = frameN  # exact frame index
            practice_top_left_4.tStart = t  # local t and not account for scr refresh
            practice_top_left_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_top_left_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_top_left_4.started')
            practice_top_left_4.setAutoDraw(True)
        
        # *practice_top_right_4* updates
        if practice_top_right_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_top_right_4.frameNStart = frameN  # exact frame index
            practice_top_right_4.tStart = t  # local t and not account for scr refresh
            practice_top_right_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_top_right_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_top_right_4.started')
            practice_top_right_4.setAutoDraw(True)
        
        # *practice_bottom_left_4* updates
        if practice_bottom_left_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bottom_left_4.frameNStart = frameN  # exact frame index
            practice_bottom_left_4.tStart = t  # local t and not account for scr refresh
            practice_bottom_left_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bottom_left_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bottom_left_4.started')
            practice_bottom_left_4.setAutoDraw(True)
        
        # *practice_bottom_right_4* updates
        if practice_bottom_right_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bottom_right_4.frameNStart = frameN  # exact frame index
            practice_bottom_right_4.tStart = t  # local t and not account for scr refresh
            practice_bottom_right_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bottom_right_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bottom_right_4.started')
            practice_bottom_right_4.setAutoDraw(True)
        
        # *practice_points_tl_p_4* updates
        if practice_points_tl_p_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tl_p_4.frameNStart = frameN  # exact frame index
            practice_points_tl_p_4.tStart = t  # local t and not account for scr refresh
            practice_points_tl_p_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tl_p_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tl_p_4.started')
            practice_points_tl_p_4.setAutoDraw(True)
        
        # *practice_points_tl_o_4* updates
        if practice_points_tl_o_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tl_o_4.frameNStart = frameN  # exact frame index
            practice_points_tl_o_4.tStart = t  # local t and not account for scr refresh
            practice_points_tl_o_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tl_o_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tl_o_4.started')
            practice_points_tl_o_4.setAutoDraw(True)
        
        # *practice_points_bl_p_4* updates
        if practice_points_bl_p_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_bl_p_4.frameNStart = frameN  # exact frame index
            practice_points_bl_p_4.tStart = t  # local t and not account for scr refresh
            practice_points_bl_p_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_bl_p_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_bl_p_4.started')
            practice_points_bl_p_4.setAutoDraw(True)
        
        # *practice_points_bl_o_4* updates
        if practice_points_bl_o_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_bl_o_4.frameNStart = frameN  # exact frame index
            practice_points_bl_o_4.tStart = t  # local t and not account for scr refresh
            practice_points_bl_o_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_bl_o_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_bl_o_4.started')
            practice_points_bl_o_4.setAutoDraw(True)
        
        # *practice_points_tr_p_4* updates
        if practice_points_tr_p_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tr_p_4.frameNStart = frameN  # exact frame index
            practice_points_tr_p_4.tStart = t  # local t and not account for scr refresh
            practice_points_tr_p_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tr_p_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tr_p_4.started')
            practice_points_tr_p_4.setAutoDraw(True)
        
        # *practice_points_tr_o_4* updates
        if practice_points_tr_o_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tr_o_4.frameNStart = frameN  # exact frame index
            practice_points_tr_o_4.tStart = t  # local t and not account for scr refresh
            practice_points_tr_o_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tr_o_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tr_o_4.started')
            practice_points_tr_o_4.setAutoDraw(True)
        
        # *practice_points_br_p_4* updates
        if practice_points_br_p_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_br_p_4.frameNStart = frameN  # exact frame index
            practice_points_br_p_4.tStart = t  # local t and not account for scr refresh
            practice_points_br_p_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_br_p_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_br_p_4.started')
            practice_points_br_p_4.setAutoDraw(True)
        
        # *practice_points_br_o_4* updates
        if practice_points_br_o_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_br_o_4.frameNStart = frameN  # exact frame index
            practice_points_br_o_4.tStart = t  # local t and not account for scr refresh
            practice_points_br_o_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_br_o_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_br_o_4.started')
            practice_points_br_o_4.setAutoDraw(True)
        
        # *practice_tr_header_4* updates
        if practice_tr_header_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_tr_header_4.frameNStart = frameN  # exact frame index
            practice_tr_header_4.tStart = t  # local t and not account for scr refresh
            practice_tr_header_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_tr_header_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_tr_header_4.started')
            practice_tr_header_4.setAutoDraw(True)
        
        # *practice_bt_header_4* updates
        if practice_bt_header_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bt_header_4.frameNStart = frameN  # exact frame index
            practice_bt_header_4.tStart = t  # local t and not account for scr refresh
            practice_bt_header_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bt_header_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bt_header_4.started')
            practice_bt_header_4.setAutoDraw(True)
        
        # *practice_p_header_4* updates
        if practice_p_header_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_p_header_4.frameNStart = frameN  # exact frame index
            practice_p_header_4.tStart = t  # local t and not account for scr refresh
            practice_p_header_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_p_header_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_p_header_4.started')
            practice_p_header_4.setAutoDraw(True)
        
        # *practice_o_header_4* updates
        if practice_o_header_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_o_header_4.frameNStart = frameN  # exact frame index
            practice_o_header_4.tStart = t  # local t and not account for scr refresh
            practice_o_header_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_o_header_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_o_header_4.started')
            practice_o_header_4.setAutoDraw(True)
        
        # *practice_bb_header_4* updates
        if practice_bb_header_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bb_header_4.frameNStart = frameN  # exact frame index
            practice_bb_header_4.tStart = t  # local t and not account for scr refresh
            practice_bb_header_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bb_header_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bb_header_4.started')
            practice_bb_header_4.setAutoDraw(True)
        
        # *practice_tl_header_4* updates
        if practice_tl_header_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_tl_header_4.frameNStart = frameN  # exact frame index
            practice_tl_header_4.tStart = t  # local t and not account for scr refresh
            practice_tl_header_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_tl_header_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_tl_header_4.started')
            practice_tl_header_4.setAutoDraw(True)
        
        # *practice_text_4* updates
        if practice_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_text_4.frameNStart = frameN  # exact frame index
            practice_text_4.tStart = t  # local t and not account for scr refresh
            practice_text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_text_4.started')
            practice_text_4.setAutoDraw(True)
        
        # *practice_cont_4* updates
        if practice_cont_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_cont_4.frameNStart = frameN  # exact frame index
            practice_cont_4.tStart = t  # local t and not account for scr refresh
            practice_cont_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_cont_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_cont_4.started')
            practice_cont_4.setAutoDraw(True)
        # *practice_mouse_4* updates
        if practice_mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_mouse_4.frameNStart = frameN  # exact frame index
            practice_mouse_4.tStart = t  # local t and not account for scr refresh
            practice_mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_mouse_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('practice_mouse_4.started', t)
            practice_mouse_4.status = STARTED
            practice_mouse_4.mouseClock.reset()
            prevButtonState = practice_mouse_4.getPressed()  # if button is down already this ISN'T a new click
        if practice_mouse_4.status == STARTED:  # only update if started and not finished!
            buttons = practice_mouse_4.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(practice_cont_4)
                        clickableList = practice_cont_4
                    except:
                        clickableList = [practice_cont_4]
                    for obj in clickableList:
                        if obj.contains(practice_mouse_4):
                            gotValidClick = True
                            practice_mouse_4.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_trial_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_trial_4" ---
    for thisComponent in practice_trial_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practice_loop (TrialHandler)
    # the Routine "practice_trial_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice_trial_5" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    practice_avatar_trial_5.setImage(chosen_avatar)
    practice_points_tl_p_5.setText(tl_p_intro)
    practice_points_tl_o_5.setText(tl_o_intro)
    practice_points_bl_p_5.setText(bl_p_intro

)
    practice_points_bl_o_5.setText(bl_o_intro)
    practice_points_tr_p_5.setText(tr_p_intro)
    practice_points_tr_o_5.setText(tr_o_intro)
    practice_points_br_p_5.setText(br_p_intro)
    practice_points_br_o_5.setText(br_o_intro)
    practice_p_header_5.setText(username)
    # setup some python lists for storing info about the practice_mouse_5
    practice_mouse_5.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    practice_trial_5Components = [practice_avatar_trial_5, practice_top_left_5, practice_top_right_5, practice_bottom_left_5, practice_bottom_right_5, practice_points_tl_p_5, practice_points_tl_o_5, practice_points_bl_p_5, practice_points_bl_o_5, practice_points_tr_p_5, practice_points_tr_o_5, practice_points_br_p_5, practice_points_br_o_5, practice_tr_header_5, practice_bt_header_5, practice_p_header_5, practice_o_header_5, practice_bb_header_5, practice_tl_header_5, practice_text_5, practice_cont_5, practice_mouse_5]
    for thisComponent in practice_trial_5Components:
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
    
    # --- Run Routine "practice_trial_5" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_avatar_trial_5* updates
        if practice_avatar_trial_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_avatar_trial_5.frameNStart = frameN  # exact frame index
            practice_avatar_trial_5.tStart = t  # local t and not account for scr refresh
            practice_avatar_trial_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_avatar_trial_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_avatar_trial_5.started')
            practice_avatar_trial_5.setAutoDraw(True)
        
        # *practice_top_left_5* updates
        if practice_top_left_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_top_left_5.frameNStart = frameN  # exact frame index
            practice_top_left_5.tStart = t  # local t and not account for scr refresh
            practice_top_left_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_top_left_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_top_left_5.started')
            practice_top_left_5.setAutoDraw(True)
        
        # *practice_top_right_5* updates
        if practice_top_right_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_top_right_5.frameNStart = frameN  # exact frame index
            practice_top_right_5.tStart = t  # local t and not account for scr refresh
            practice_top_right_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_top_right_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_top_right_5.started')
            practice_top_right_5.setAutoDraw(True)
        
        # *practice_bottom_left_5* updates
        if practice_bottom_left_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bottom_left_5.frameNStart = frameN  # exact frame index
            practice_bottom_left_5.tStart = t  # local t and not account for scr refresh
            practice_bottom_left_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bottom_left_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bottom_left_5.started')
            practice_bottom_left_5.setAutoDraw(True)
        
        # *practice_bottom_right_5* updates
        if practice_bottom_right_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bottom_right_5.frameNStart = frameN  # exact frame index
            practice_bottom_right_5.tStart = t  # local t and not account for scr refresh
            practice_bottom_right_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bottom_right_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bottom_right_5.started')
            practice_bottom_right_5.setAutoDraw(True)
        
        # *practice_points_tl_p_5* updates
        if practice_points_tl_p_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tl_p_5.frameNStart = frameN  # exact frame index
            practice_points_tl_p_5.tStart = t  # local t and not account for scr refresh
            practice_points_tl_p_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tl_p_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tl_p_5.started')
            practice_points_tl_p_5.setAutoDraw(True)
        
        # *practice_points_tl_o_5* updates
        if practice_points_tl_o_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tl_o_5.frameNStart = frameN  # exact frame index
            practice_points_tl_o_5.tStart = t  # local t and not account for scr refresh
            practice_points_tl_o_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tl_o_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tl_o_5.started')
            practice_points_tl_o_5.setAutoDraw(True)
        
        # *practice_points_bl_p_5* updates
        if practice_points_bl_p_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_bl_p_5.frameNStart = frameN  # exact frame index
            practice_points_bl_p_5.tStart = t  # local t and not account for scr refresh
            practice_points_bl_p_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_bl_p_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_bl_p_5.started')
            practice_points_bl_p_5.setAutoDraw(True)
        
        # *practice_points_bl_o_5* updates
        if practice_points_bl_o_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_bl_o_5.frameNStart = frameN  # exact frame index
            practice_points_bl_o_5.tStart = t  # local t and not account for scr refresh
            practice_points_bl_o_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_bl_o_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_bl_o_5.started')
            practice_points_bl_o_5.setAutoDraw(True)
        
        # *practice_points_tr_p_5* updates
        if practice_points_tr_p_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tr_p_5.frameNStart = frameN  # exact frame index
            practice_points_tr_p_5.tStart = t  # local t and not account for scr refresh
            practice_points_tr_p_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tr_p_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tr_p_5.started')
            practice_points_tr_p_5.setAutoDraw(True)
        
        # *practice_points_tr_o_5* updates
        if practice_points_tr_o_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tr_o_5.frameNStart = frameN  # exact frame index
            practice_points_tr_o_5.tStart = t  # local t and not account for scr refresh
            practice_points_tr_o_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tr_o_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tr_o_5.started')
            practice_points_tr_o_5.setAutoDraw(True)
        
        # *practice_points_br_p_5* updates
        if practice_points_br_p_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_br_p_5.frameNStart = frameN  # exact frame index
            practice_points_br_p_5.tStart = t  # local t and not account for scr refresh
            practice_points_br_p_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_br_p_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_br_p_5.started')
            practice_points_br_p_5.setAutoDraw(True)
        
        # *practice_points_br_o_5* updates
        if practice_points_br_o_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_br_o_5.frameNStart = frameN  # exact frame index
            practice_points_br_o_5.tStart = t  # local t and not account for scr refresh
            practice_points_br_o_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_br_o_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_br_o_5.started')
            practice_points_br_o_5.setAutoDraw(True)
        
        # *practice_tr_header_5* updates
        if practice_tr_header_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_tr_header_5.frameNStart = frameN  # exact frame index
            practice_tr_header_5.tStart = t  # local t and not account for scr refresh
            practice_tr_header_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_tr_header_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_tr_header_5.started')
            practice_tr_header_5.setAutoDraw(True)
        
        # *practice_bt_header_5* updates
        if practice_bt_header_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bt_header_5.frameNStart = frameN  # exact frame index
            practice_bt_header_5.tStart = t  # local t and not account for scr refresh
            practice_bt_header_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bt_header_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bt_header_5.started')
            practice_bt_header_5.setAutoDraw(True)
        
        # *practice_p_header_5* updates
        if practice_p_header_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_p_header_5.frameNStart = frameN  # exact frame index
            practice_p_header_5.tStart = t  # local t and not account for scr refresh
            practice_p_header_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_p_header_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_p_header_5.started')
            practice_p_header_5.setAutoDraw(True)
        
        # *practice_o_header_5* updates
        if practice_o_header_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_o_header_5.frameNStart = frameN  # exact frame index
            practice_o_header_5.tStart = t  # local t and not account for scr refresh
            practice_o_header_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_o_header_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_o_header_5.started')
            practice_o_header_5.setAutoDraw(True)
        
        # *practice_bb_header_5* updates
        if practice_bb_header_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bb_header_5.frameNStart = frameN  # exact frame index
            practice_bb_header_5.tStart = t  # local t and not account for scr refresh
            practice_bb_header_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bb_header_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bb_header_5.started')
            practice_bb_header_5.setAutoDraw(True)
        
        # *practice_tl_header_5* updates
        if practice_tl_header_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_tl_header_5.frameNStart = frameN  # exact frame index
            practice_tl_header_5.tStart = t  # local t and not account for scr refresh
            practice_tl_header_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_tl_header_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_tl_header_5.started')
            practice_tl_header_5.setAutoDraw(True)
        
        # *practice_text_5* updates
        if practice_text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_text_5.frameNStart = frameN  # exact frame index
            practice_text_5.tStart = t  # local t and not account for scr refresh
            practice_text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_text_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_text_5.started')
            practice_text_5.setAutoDraw(True)
        
        # *practice_cont_5* updates
        if practice_cont_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_cont_5.frameNStart = frameN  # exact frame index
            practice_cont_5.tStart = t  # local t and not account for scr refresh
            practice_cont_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_cont_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_cont_5.started')
            practice_cont_5.setAutoDraw(True)
        # *practice_mouse_5* updates
        if practice_mouse_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_mouse_5.frameNStart = frameN  # exact frame index
            practice_mouse_5.tStart = t  # local t and not account for scr refresh
            practice_mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_mouse_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('practice_mouse_5.started', t)
            practice_mouse_5.status = STARTED
            practice_mouse_5.mouseClock.reset()
            prevButtonState = practice_mouse_5.getPressed()  # if button is down already this ISN'T a new click
        if practice_mouse_5.status == STARTED:  # only update if started and not finished!
            buttons = practice_mouse_5.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(practice_cont_5)
                        clickableList = practice_cont_5
                    except:
                        clickableList = [practice_cont_5]
                    for obj in clickableList:
                        if obj.contains(practice_mouse_5):
                            gotValidClick = True
                            practice_mouse_5.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_trial_5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_trial_5" ---
    for thisComponent in practice_trial_5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practice_loop (TrialHandler)
    # the Routine "practice_trial_5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice_trial_6" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    practice_avatar_6.setImage(chosen_avatar)
    practice_points_tl_p_6.setText(tl_p_intro)
    practice_points_tl_o_6.setText(tl_o_intro)
    practice_points_bl_p_6.setText(bl_p_intro

)
    practice_points_bl_o_6.setText(bl_o_intro)
    practice_points_tr_p_6.setText(tr_p_intro)
    practice_points_tr_o_6.setText(tr_o_intro)
    practice_points_br_p_6.setText(br_p_intro)
    practice_points_br_o_6.setText(br_o_intro)
    practice_p_header_6.setText(username)
    # setup some python lists for storing info about the practice_mouse_6
    practice_mouse_6.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    practice_trial_6Components = [practice_avatar_6, practice_top_left_6, practice_top_right_6, practice_bottom_left_6, practice_bottom_right_6, practice_points_tl_p_6, practice_points_tl_o_6, practice_points_bl_p_6, practice_points_bl_o_6, practice_points_tr_p_6, practice_points_tr_o_6, practice_points_br_p_6, practice_points_br_o_6, practice_tr_header_6, practice_bt_header_6, practice_p_header_6, practice_o_header_6, practice_bb_header_6, practice_tl_header_6, practice_text_6, practice_cont_6, practice_mouse_6]
    for thisComponent in practice_trial_6Components:
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
    
    # --- Run Routine "practice_trial_6" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_avatar_6* updates
        if practice_avatar_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_avatar_6.frameNStart = frameN  # exact frame index
            practice_avatar_6.tStart = t  # local t and not account for scr refresh
            practice_avatar_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_avatar_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_avatar_6.started')
            practice_avatar_6.setAutoDraw(True)
        
        # *practice_top_left_6* updates
        if practice_top_left_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_top_left_6.frameNStart = frameN  # exact frame index
            practice_top_left_6.tStart = t  # local t and not account for scr refresh
            practice_top_left_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_top_left_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_top_left_6.started')
            practice_top_left_6.setAutoDraw(True)
        
        # *practice_top_right_6* updates
        if practice_top_right_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_top_right_6.frameNStart = frameN  # exact frame index
            practice_top_right_6.tStart = t  # local t and not account for scr refresh
            practice_top_right_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_top_right_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_top_right_6.started')
            practice_top_right_6.setAutoDraw(True)
        
        # *practice_bottom_left_6* updates
        if practice_bottom_left_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bottom_left_6.frameNStart = frameN  # exact frame index
            practice_bottom_left_6.tStart = t  # local t and not account for scr refresh
            practice_bottom_left_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bottom_left_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bottom_left_6.started')
            practice_bottom_left_6.setAutoDraw(True)
        
        # *practice_bottom_right_6* updates
        if practice_bottom_right_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bottom_right_6.frameNStart = frameN  # exact frame index
            practice_bottom_right_6.tStart = t  # local t and not account for scr refresh
            practice_bottom_right_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bottom_right_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bottom_right_6.started')
            practice_bottom_right_6.setAutoDraw(True)
        
        # *practice_points_tl_p_6* updates
        if practice_points_tl_p_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tl_p_6.frameNStart = frameN  # exact frame index
            practice_points_tl_p_6.tStart = t  # local t and not account for scr refresh
            practice_points_tl_p_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tl_p_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tl_p_6.started')
            practice_points_tl_p_6.setAutoDraw(True)
        
        # *practice_points_tl_o_6* updates
        if practice_points_tl_o_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tl_o_6.frameNStart = frameN  # exact frame index
            practice_points_tl_o_6.tStart = t  # local t and not account for scr refresh
            practice_points_tl_o_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tl_o_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tl_o_6.started')
            practice_points_tl_o_6.setAutoDraw(True)
        
        # *practice_points_bl_p_6* updates
        if practice_points_bl_p_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_bl_p_6.frameNStart = frameN  # exact frame index
            practice_points_bl_p_6.tStart = t  # local t and not account for scr refresh
            practice_points_bl_p_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_bl_p_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_bl_p_6.started')
            practice_points_bl_p_6.setAutoDraw(True)
        
        # *practice_points_bl_o_6* updates
        if practice_points_bl_o_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_bl_o_6.frameNStart = frameN  # exact frame index
            practice_points_bl_o_6.tStart = t  # local t and not account for scr refresh
            practice_points_bl_o_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_bl_o_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_bl_o_6.started')
            practice_points_bl_o_6.setAutoDraw(True)
        
        # *practice_points_tr_p_6* updates
        if practice_points_tr_p_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tr_p_6.frameNStart = frameN  # exact frame index
            practice_points_tr_p_6.tStart = t  # local t and not account for scr refresh
            practice_points_tr_p_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tr_p_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tr_p_6.started')
            practice_points_tr_p_6.setAutoDraw(True)
        
        # *practice_points_tr_o_6* updates
        if practice_points_tr_o_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tr_o_6.frameNStart = frameN  # exact frame index
            practice_points_tr_o_6.tStart = t  # local t and not account for scr refresh
            practice_points_tr_o_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tr_o_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tr_o_6.started')
            practice_points_tr_o_6.setAutoDraw(True)
        
        # *practice_points_br_p_6* updates
        if practice_points_br_p_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_br_p_6.frameNStart = frameN  # exact frame index
            practice_points_br_p_6.tStart = t  # local t and not account for scr refresh
            practice_points_br_p_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_br_p_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_br_p_6.started')
            practice_points_br_p_6.setAutoDraw(True)
        
        # *practice_points_br_o_6* updates
        if practice_points_br_o_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_br_o_6.frameNStart = frameN  # exact frame index
            practice_points_br_o_6.tStart = t  # local t and not account for scr refresh
            practice_points_br_o_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_br_o_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_br_o_6.started')
            practice_points_br_o_6.setAutoDraw(True)
        
        # *practice_tr_header_6* updates
        if practice_tr_header_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_tr_header_6.frameNStart = frameN  # exact frame index
            practice_tr_header_6.tStart = t  # local t and not account for scr refresh
            practice_tr_header_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_tr_header_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_tr_header_6.started')
            practice_tr_header_6.setAutoDraw(True)
        
        # *practice_bt_header_6* updates
        if practice_bt_header_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bt_header_6.frameNStart = frameN  # exact frame index
            practice_bt_header_6.tStart = t  # local t and not account for scr refresh
            practice_bt_header_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bt_header_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bt_header_6.started')
            practice_bt_header_6.setAutoDraw(True)
        
        # *practice_p_header_6* updates
        if practice_p_header_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_p_header_6.frameNStart = frameN  # exact frame index
            practice_p_header_6.tStart = t  # local t and not account for scr refresh
            practice_p_header_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_p_header_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_p_header_6.started')
            practice_p_header_6.setAutoDraw(True)
        
        # *practice_o_header_6* updates
        if practice_o_header_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_o_header_6.frameNStart = frameN  # exact frame index
            practice_o_header_6.tStart = t  # local t and not account for scr refresh
            practice_o_header_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_o_header_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_o_header_6.started')
            practice_o_header_6.setAutoDraw(True)
        
        # *practice_bb_header_6* updates
        if practice_bb_header_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bb_header_6.frameNStart = frameN  # exact frame index
            practice_bb_header_6.tStart = t  # local t and not account for scr refresh
            practice_bb_header_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bb_header_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bb_header_6.started')
            practice_bb_header_6.setAutoDraw(True)
        
        # *practice_tl_header_6* updates
        if practice_tl_header_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_tl_header_6.frameNStart = frameN  # exact frame index
            practice_tl_header_6.tStart = t  # local t and not account for scr refresh
            practice_tl_header_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_tl_header_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_tl_header_6.started')
            practice_tl_header_6.setAutoDraw(True)
        
        # *practice_text_6* updates
        if practice_text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_text_6.frameNStart = frameN  # exact frame index
            practice_text_6.tStart = t  # local t and not account for scr refresh
            practice_text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_text_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_text_6.started')
            practice_text_6.setAutoDraw(True)
        
        # *practice_cont_6* updates
        if practice_cont_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_cont_6.frameNStart = frameN  # exact frame index
            practice_cont_6.tStart = t  # local t and not account for scr refresh
            practice_cont_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_cont_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_cont_6.started')
            practice_cont_6.setAutoDraw(True)
        # *practice_mouse_6* updates
        if practice_mouse_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_mouse_6.frameNStart = frameN  # exact frame index
            practice_mouse_6.tStart = t  # local t and not account for scr refresh
            practice_mouse_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_mouse_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('practice_mouse_6.started', t)
            practice_mouse_6.status = STARTED
            practice_mouse_6.mouseClock.reset()
            prevButtonState = practice_mouse_6.getPressed()  # if button is down already this ISN'T a new click
        if practice_mouse_6.status == STARTED:  # only update if started and not finished!
            buttons = practice_mouse_6.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(practice_cont_6)
                        clickableList = practice_cont_6
                    except:
                        clickableList = [practice_cont_6]
                    for obj in clickableList:
                        if obj.contains(practice_mouse_6):
                            gotValidClick = True
                            practice_mouse_6.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_trial_6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_trial_6" ---
    for thisComponent in practice_trial_6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practice_loop (TrialHandler)
    # the Routine "practice_trial_6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice_trial_7" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    practice_avatar_7.setImage(chosen_avatar)
    practice_points_tl_p_7.setText(tl_p_intro)
    practice_points_tl_o_7.setText(tl_o_intro)
    practice_points_bl_p_7.setText(bl_p_intro

)
    practice_points_bl_o_7.setText(bl_o_intro)
    practice_points_tr_p_7.setText(tr_p_intro)
    practice_points_tr_o_7.setText(tr_o_intro)
    practice_points_br_p_7.setText(br_p_intro)
    practice_points_br_o_7.setText(br_o_intro)
    practice_p_header_7.setText(username)
    # setup some python lists for storing info about the practice_mouse_7
    practice_mouse_7.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    practice_trial_7Components = [practice_avatar_7, practice_top_left_7, practice_top_right_7, practice_bottom_left_7, practice_bottom_right_7, practice_points_tl_p_7, practice_points_tl_o_7, practice_points_bl_p_7, practice_points_bl_o_7, practice_points_tr_p_7, practice_points_tr_o_7, practice_points_br_p_7, practice_points_br_o_7, practice_tr_header_7, practice_bt_header_7, practice_p_header_7, practice_other_header_7, practice_bb_header_7, practice_tl_header_7, practice_text_7, practice_cont_7, practice_mouse_7]
    for thisComponent in practice_trial_7Components:
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
    
    # --- Run Routine "practice_trial_7" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_avatar_7* updates
        if practice_avatar_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_avatar_7.frameNStart = frameN  # exact frame index
            practice_avatar_7.tStart = t  # local t and not account for scr refresh
            practice_avatar_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_avatar_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_avatar_7.started')
            practice_avatar_7.setAutoDraw(True)
        
        # *practice_top_left_7* updates
        if practice_top_left_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_top_left_7.frameNStart = frameN  # exact frame index
            practice_top_left_7.tStart = t  # local t and not account for scr refresh
            practice_top_left_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_top_left_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_top_left_7.started')
            practice_top_left_7.setAutoDraw(True)
        
        # *practice_top_right_7* updates
        if practice_top_right_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_top_right_7.frameNStart = frameN  # exact frame index
            practice_top_right_7.tStart = t  # local t and not account for scr refresh
            practice_top_right_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_top_right_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_top_right_7.started')
            practice_top_right_7.setAutoDraw(True)
        
        # *practice_bottom_left_7* updates
        if practice_bottom_left_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bottom_left_7.frameNStart = frameN  # exact frame index
            practice_bottom_left_7.tStart = t  # local t and not account for scr refresh
            practice_bottom_left_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bottom_left_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bottom_left_7.started')
            practice_bottom_left_7.setAutoDraw(True)
        
        # *practice_bottom_right_7* updates
        if practice_bottom_right_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bottom_right_7.frameNStart = frameN  # exact frame index
            practice_bottom_right_7.tStart = t  # local t and not account for scr refresh
            practice_bottom_right_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bottom_right_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bottom_right_7.started')
            practice_bottom_right_7.setAutoDraw(True)
        
        # *practice_points_tl_p_7* updates
        if practice_points_tl_p_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tl_p_7.frameNStart = frameN  # exact frame index
            practice_points_tl_p_7.tStart = t  # local t and not account for scr refresh
            practice_points_tl_p_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tl_p_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tl_p_7.started')
            practice_points_tl_p_7.setAutoDraw(True)
        
        # *practice_points_tl_o_7* updates
        if practice_points_tl_o_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tl_o_7.frameNStart = frameN  # exact frame index
            practice_points_tl_o_7.tStart = t  # local t and not account for scr refresh
            practice_points_tl_o_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tl_o_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tl_o_7.started')
            practice_points_tl_o_7.setAutoDraw(True)
        
        # *practice_points_bl_p_7* updates
        if practice_points_bl_p_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_bl_p_7.frameNStart = frameN  # exact frame index
            practice_points_bl_p_7.tStart = t  # local t and not account for scr refresh
            practice_points_bl_p_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_bl_p_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_bl_p_7.started')
            practice_points_bl_p_7.setAutoDraw(True)
        
        # *practice_points_bl_o_7* updates
        if practice_points_bl_o_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_bl_o_7.frameNStart = frameN  # exact frame index
            practice_points_bl_o_7.tStart = t  # local t and not account for scr refresh
            practice_points_bl_o_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_bl_o_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_bl_o_7.started')
            practice_points_bl_o_7.setAutoDraw(True)
        
        # *practice_points_tr_p_7* updates
        if practice_points_tr_p_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tr_p_7.frameNStart = frameN  # exact frame index
            practice_points_tr_p_7.tStart = t  # local t and not account for scr refresh
            practice_points_tr_p_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tr_p_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tr_p_7.started')
            practice_points_tr_p_7.setAutoDraw(True)
        
        # *practice_points_tr_o_7* updates
        if practice_points_tr_o_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_tr_o_7.frameNStart = frameN  # exact frame index
            practice_points_tr_o_7.tStart = t  # local t and not account for scr refresh
            practice_points_tr_o_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_tr_o_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_tr_o_7.started')
            practice_points_tr_o_7.setAutoDraw(True)
        
        # *practice_points_br_p_7* updates
        if practice_points_br_p_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_br_p_7.frameNStart = frameN  # exact frame index
            practice_points_br_p_7.tStart = t  # local t and not account for scr refresh
            practice_points_br_p_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_br_p_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_br_p_7.started')
            practice_points_br_p_7.setAutoDraw(True)
        
        # *practice_points_br_o_7* updates
        if practice_points_br_o_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_br_o_7.frameNStart = frameN  # exact frame index
            practice_points_br_o_7.tStart = t  # local t and not account for scr refresh
            practice_points_br_o_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_br_o_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_br_o_7.started')
            practice_points_br_o_7.setAutoDraw(True)
        
        # *practice_tr_header_7* updates
        if practice_tr_header_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_tr_header_7.frameNStart = frameN  # exact frame index
            practice_tr_header_7.tStart = t  # local t and not account for scr refresh
            practice_tr_header_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_tr_header_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_tr_header_7.started')
            practice_tr_header_7.setAutoDraw(True)
        
        # *practice_bt_header_7* updates
        if practice_bt_header_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bt_header_7.frameNStart = frameN  # exact frame index
            practice_bt_header_7.tStart = t  # local t and not account for scr refresh
            practice_bt_header_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bt_header_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bt_header_7.started')
            practice_bt_header_7.setAutoDraw(True)
        
        # *practice_p_header_7* updates
        if practice_p_header_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_p_header_7.frameNStart = frameN  # exact frame index
            practice_p_header_7.tStart = t  # local t and not account for scr refresh
            practice_p_header_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_p_header_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_p_header_7.started')
            practice_p_header_7.setAutoDraw(True)
        
        # *practice_other_header_7* updates
        if practice_other_header_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_other_header_7.frameNStart = frameN  # exact frame index
            practice_other_header_7.tStart = t  # local t and not account for scr refresh
            practice_other_header_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_other_header_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_other_header_7.started')
            practice_other_header_7.setAutoDraw(True)
        
        # *practice_bb_header_7* updates
        if practice_bb_header_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bb_header_7.frameNStart = frameN  # exact frame index
            practice_bb_header_7.tStart = t  # local t and not account for scr refresh
            practice_bb_header_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bb_header_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bb_header_7.started')
            practice_bb_header_7.setAutoDraw(True)
        
        # *practice_tl_header_7* updates
        if practice_tl_header_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_tl_header_7.frameNStart = frameN  # exact frame index
            practice_tl_header_7.tStart = t  # local t and not account for scr refresh
            practice_tl_header_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_tl_header_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_tl_header_7.started')
            practice_tl_header_7.setAutoDraw(True)
        
        # *practice_text_7* updates
        if practice_text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_text_7.frameNStart = frameN  # exact frame index
            practice_text_7.tStart = t  # local t and not account for scr refresh
            practice_text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_text_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_text_7.started')
            practice_text_7.setAutoDraw(True)
        
        # *practice_cont_7* updates
        if practice_cont_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_cont_7.frameNStart = frameN  # exact frame index
            practice_cont_7.tStart = t  # local t and not account for scr refresh
            practice_cont_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_cont_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_cont_7.started')
            practice_cont_7.setAutoDraw(True)
        # *practice_mouse_7* updates
        if practice_mouse_7.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_mouse_7.frameNStart = frameN  # exact frame index
            practice_mouse_7.tStart = t  # local t and not account for scr refresh
            practice_mouse_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_mouse_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('practice_mouse_7.started', t)
            practice_mouse_7.status = STARTED
            practice_mouse_7.mouseClock.reset()
            prevButtonState = practice_mouse_7.getPressed()  # if button is down already this ISN'T a new click
        if practice_mouse_7.status == STARTED:  # only update if started and not finished!
            buttons = practice_mouse_7.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(practice_cont_7)
                        clickableList = practice_cont_7
                    except:
                        clickableList = [practice_cont_7]
                    for obj in clickableList:
                        if obj.contains(practice_mouse_7):
                            gotValidClick = True
                            practice_mouse_7.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_trial_7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_trial_7" ---
    for thisComponent in practice_trial_7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practice_loop (TrialHandler)
    # the Routine "practice_trial_7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "practice_trial_8" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    practice_choice_p_8.setText('You chose to defect'

)
    practice_choice_o_8.setText("Other player chose to cooperate")
    practice_points_p_8.setText("You gain {} points".format(tr_p_intro))
    practice_points_o_8.setText("Other player gains {} points".format(tr_o_intro))
    practice_bl_text_8.setText('No\n{}'.format(bl_o_intro))
    practice_br_text_8.setText('Yes\n{}x{}'.format(bl_o_intro, mult_intro))
    # setup some python lists for storing info about the practice_mouse_8
    practice_mouse_8.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    practice_trial_8Components = [practice_choice_p_8, practice_choice_o_8, practice_points_p_8, practice_points_o_8, practice_bottom_left_8, practice_bottom_right_8, practice_bl_text_8, practice_br_text_8, practice_mult_8, practice_text_8, practice_cont_8, practice_mouse_8]
    for thisComponent in practice_trial_8Components:
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
    
    # --- Run Routine "practice_trial_8" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_choice_p_8* updates
        if practice_choice_p_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_choice_p_8.frameNStart = frameN  # exact frame index
            practice_choice_p_8.tStart = t  # local t and not account for scr refresh
            practice_choice_p_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_choice_p_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_choice_p_8.started')
            practice_choice_p_8.setAutoDraw(True)
        
        # *practice_choice_o_8* updates
        if practice_choice_o_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_choice_o_8.frameNStart = frameN  # exact frame index
            practice_choice_o_8.tStart = t  # local t and not account for scr refresh
            practice_choice_o_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_choice_o_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_choice_o_8.started')
            practice_choice_o_8.setAutoDraw(True)
        
        # *practice_points_p_8* updates
        if practice_points_p_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_p_8.frameNStart = frameN  # exact frame index
            practice_points_p_8.tStart = t  # local t and not account for scr refresh
            practice_points_p_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_p_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_p_8.started')
            practice_points_p_8.setAutoDraw(True)
        
        # *practice_points_o_8* updates
        if practice_points_o_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_points_o_8.frameNStart = frameN  # exact frame index
            practice_points_o_8.tStart = t  # local t and not account for scr refresh
            practice_points_o_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_points_o_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_points_o_8.started')
            practice_points_o_8.setAutoDraw(True)
        
        # *practice_bottom_left_8* updates
        if practice_bottom_left_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bottom_left_8.frameNStart = frameN  # exact frame index
            practice_bottom_left_8.tStart = t  # local t and not account for scr refresh
            practice_bottom_left_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bottom_left_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bottom_left_8.started')
            practice_bottom_left_8.setAutoDraw(True)
        
        # *practice_bottom_right_8* updates
        if practice_bottom_right_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bottom_right_8.frameNStart = frameN  # exact frame index
            practice_bottom_right_8.tStart = t  # local t and not account for scr refresh
            practice_bottom_right_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bottom_right_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bottom_right_8.started')
            practice_bottom_right_8.setAutoDraw(True)
        
        # *practice_bl_text_8* updates
        if practice_bl_text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_bl_text_8.frameNStart = frameN  # exact frame index
            practice_bl_text_8.tStart = t  # local t and not account for scr refresh
            practice_bl_text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_bl_text_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_bl_text_8.started')
            practice_bl_text_8.setAutoDraw(True)
        
        # *practice_br_text_8* updates
        if practice_br_text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_br_text_8.frameNStart = frameN  # exact frame index
            practice_br_text_8.tStart = t  # local t and not account for scr refresh
            practice_br_text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_br_text_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_br_text_8.started')
            practice_br_text_8.setAutoDraw(True)
        
        # *practice_mult_8* updates
        if practice_mult_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_mult_8.frameNStart = frameN  # exact frame index
            practice_mult_8.tStart = t  # local t and not account for scr refresh
            practice_mult_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_mult_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_mult_8.started')
            practice_mult_8.setAutoDraw(True)
        
        # *practice_text_8* updates
        if practice_text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_text_8.frameNStart = frameN  # exact frame index
            practice_text_8.tStart = t  # local t and not account for scr refresh
            practice_text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_text_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_text_8.started')
            practice_text_8.setAutoDraw(True)
        
        # *practice_cont_8* updates
        if practice_cont_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_cont_8.frameNStart = frameN  # exact frame index
            practice_cont_8.tStart = t  # local t and not account for scr refresh
            practice_cont_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_cont_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_cont_8.started')
            practice_cont_8.setAutoDraw(True)
        # *practice_mouse_8* updates
        if practice_mouse_8.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_mouse_8.frameNStart = frameN  # exact frame index
            practice_mouse_8.tStart = t  # local t and not account for scr refresh
            practice_mouse_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_mouse_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('practice_mouse_8.started', t)
            practice_mouse_8.status = STARTED
            practice_mouse_8.mouseClock.reset()
            prevButtonState = practice_mouse_8.getPressed()  # if button is down already this ISN'T a new click
        if practice_mouse_8.status == STARTED:  # only update if started and not finished!
            buttons = practice_mouse_8.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(practice_cont_8)
                        clickableList = practice_cont_8
                    except:
                        clickableList = [practice_cont_8]
                    for obj in clickableList:
                        if obj.contains(practice_mouse_8):
                            gotValidClick = True
                            practice_mouse_8.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_trial_8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "practice_trial_8" ---
    for thisComponent in practice_trial_8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for practice_loop (TrialHandler)
    # the Routine "practice_trial_8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice_loop'


# set up handler to look after randomisation of conditions etc
initial_choice_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('other_player_initial_choice'+order+'.xlsx'),
    seed=None, name='initial_choice_loop')
thisExp.addLoop(initial_choice_loop)  # add the loop to the experiment
thisInitial_choice_loop = initial_choice_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInitial_choice_loop.rgb)
if thisInitial_choice_loop != None:
    for paramName in thisInitial_choice_loop:
        exec('{} = thisInitial_choice_loop[paramName]'.format(paramName))

for thisInitial_choice_loop in initial_choice_loop:
    currentLoop = initial_choice_loop
    # abbreviate parameter names if possible (e.g. rgb = thisInitial_choice_loop.rgb)
    if thisInitial_choice_loop != None:
        for paramName in thisInitial_choice_loop:
            exec('{} = thisInitial_choice_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "OP_introduction" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from o_intro_code
    #Setting points to 0 for first trial with each other
    participant_points_total = 0
    other_points_total = 0
    
    #Choosing other avatar (random)
    if initial_choice_loop.thisTrialN == 0:
        random.shuffle(unselected_avatar)
        other_avatar = unselected_avatar[0]
    elif initial_choice_loop.thisTrialN > 0 :
        del unselected_avatar[0]
        random.shuffle(unselected_avatar)
        other_avatar = unselected_avatar[0]
    
    initial_choice_loop.addData('other_avatar', other_avatar)
    o_intro_text.setText("Hello {} !\n\n\n\nIn this game you will be playing with {}!".format(username, other_name))
    o_intro_avatar_p.setImage(chosen_avatar)
    o_intro_avatar_o.setImage(other_avatar)
    # setup some python lists for storing info about the o_intro_mouse
    o_intro_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    OP_introductionComponents = [o_intro_text, o_intro_avatar_p, o_intro_avatar_o, o_intro_cont, o_intro_mouse]
    for thisComponent in OP_introductionComponents:
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
    
    # --- Run Routine "OP_introduction" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *o_intro_text* updates
        if o_intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            o_intro_text.frameNStart = frameN  # exact frame index
            o_intro_text.tStart = t  # local t and not account for scr refresh
            o_intro_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(o_intro_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'o_intro_text.started')
            o_intro_text.setAutoDraw(True)
        
        # *o_intro_avatar_p* updates
        if o_intro_avatar_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            o_intro_avatar_p.frameNStart = frameN  # exact frame index
            o_intro_avatar_p.tStart = t  # local t and not account for scr refresh
            o_intro_avatar_p.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(o_intro_avatar_p, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'o_intro_avatar_p.started')
            o_intro_avatar_p.setAutoDraw(True)
        
        # *o_intro_avatar_o* updates
        if o_intro_avatar_o.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            o_intro_avatar_o.frameNStart = frameN  # exact frame index
            o_intro_avatar_o.tStart = t  # local t and not account for scr refresh
            o_intro_avatar_o.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(o_intro_avatar_o, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'o_intro_avatar_o.started')
            o_intro_avatar_o.setAutoDraw(True)
        
        # *o_intro_cont* updates
        if o_intro_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            o_intro_cont.frameNStart = frameN  # exact frame index
            o_intro_cont.tStart = t  # local t and not account for scr refresh
            o_intro_cont.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(o_intro_cont, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'o_intro_cont.started')
            o_intro_cont.setAutoDraw(True)
        # *o_intro_mouse* updates
        if o_intro_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            o_intro_mouse.frameNStart = frameN  # exact frame index
            o_intro_mouse.tStart = t  # local t and not account for scr refresh
            o_intro_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(o_intro_mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('o_intro_mouse.started', t)
            o_intro_mouse.status = STARTED
            o_intro_mouse.mouseClock.reset()
            prevButtonState = o_intro_mouse.getPressed()  # if button is down already this ISN'T a new click
        if o_intro_mouse.status == STARTED:  # only update if started and not finished!
            buttons = o_intro_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(o_intro_cont)
                        clickableList = o_intro_cont
                    except:
                        clickableList = [o_intro_cont]
                    for obj in clickableList:
                        if obj.contains(o_intro_mouse):
                            gotValidClick = True
                            o_intro_mouse.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in OP_introductionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "OP_introduction" ---
    for thisComponent in OP_introductionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for initial_choice_loop (TrialHandler)
    # the Routine "OP_introduction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trial_loop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('payoff_matrices_coop_defect.xlsx'),
        seed=None, name='trial_loop')
    thisExp.addLoop(trial_loop)  # add the loop to the experiment
    thisTrial_loop = trial_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_loop.rgb)
    if thisTrial_loop != None:
        for paramName in thisTrial_loop:
            exec('{} = thisTrial_loop[paramName]'.format(paramName))
    
    for thisTrial_loop in trial_loop:
        currentLoop = trial_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_loop.rgb)
        if thisTrial_loop != None:
            for paramName in thisTrial_loop:
                exec('{} = thisTrial_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from trial_code
        #Randomising button order
        random.shuffle(button_list)
        left_text = button_list[0]
        right_text = button_list[1]
        
        #Changing bottom text to only show on first trial
        if trial_loop.thisTrialN == 0:
            trial_bottom_text = "Make your choice by clicking one of the boxes"
        else:
            trial_bottom_text = "                                             "
        
        
        
        
        trial_avatar_o.setImage(other_avatar)
        trial_avatar_p.setImage(chosen_avatar)
        trial_tl_p.setText(tl_p)
        trial_tl_o.setText(tl_o)
        trial_bl_p.setText(bl_p

)
        trial_bl_o.setText(bl_o)
        trial_tr_p.setText(tr_p)
        trial_tr_o.setText(tr_o)
        trial_br_p.setText(br_p)
        trial_br_o.setText(br_o)
        trial_header_p.setText(username)
        trial_header_o.setText(other_name)
        leftchoice_text.setText(left_text)
        rightchoice_text.setText(right_text
)
        # setup some python lists for storing info about the trial_mouse
        trial_mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        make_your_choice_text.setText(trial_bottom_text)
        # keep track of which components have finished
        trialComponents = [trial_avatar_o, trial_avatar_p, top_left, top_right, bottom_left, bottom_right, trial_tl_p, trial_tl_o, trial_bl_p, trial_bl_o, trial_tr_p, trial_tr_o, trial_br_p, trial_br_o, topleft_header, topright_header, bottomtop_header, bottombottom_header, trial_header_p, trial_header_o, left_choice, leftchoice_text, right_choice, rightchoice_text, trial_mouse, make_your_choice_text]
        for thisComponent in trialComponents:
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
        
        # --- Run Routine "trial" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *trial_avatar_o* updates
            if trial_avatar_o.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_avatar_o.frameNStart = frameN  # exact frame index
                trial_avatar_o.tStart = t  # local t and not account for scr refresh
                trial_avatar_o.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_avatar_o, 'tStartRefresh')  # time at next scr refresh
                trial_avatar_o.setAutoDraw(True)
            
            # *trial_avatar_p* updates
            if trial_avatar_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_avatar_p.frameNStart = frameN  # exact frame index
                trial_avatar_p.tStart = t  # local t and not account for scr refresh
                trial_avatar_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_avatar_p, 'tStartRefresh')  # time at next scr refresh
                trial_avatar_p.setAutoDraw(True)
            
            # *top_left* updates
            if top_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                top_left.frameNStart = frameN  # exact frame index
                top_left.tStart = t  # local t and not account for scr refresh
                top_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(top_left, 'tStartRefresh')  # time at next scr refresh
                top_left.setAutoDraw(True)
            
            # *top_right* updates
            if top_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                top_right.frameNStart = frameN  # exact frame index
                top_right.tStart = t  # local t and not account for scr refresh
                top_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(top_right, 'tStartRefresh')  # time at next scr refresh
                top_right.setAutoDraw(True)
            
            # *bottom_left* updates
            if bottom_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bottom_left.frameNStart = frameN  # exact frame index
                bottom_left.tStart = t  # local t and not account for scr refresh
                bottom_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bottom_left, 'tStartRefresh')  # time at next scr refresh
                bottom_left.setAutoDraw(True)
            
            # *bottom_right* updates
            if bottom_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bottom_right.frameNStart = frameN  # exact frame index
                bottom_right.tStart = t  # local t and not account for scr refresh
                bottom_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bottom_right, 'tStartRefresh')  # time at next scr refresh
                bottom_right.setAutoDraw(True)
            
            # *trial_tl_p* updates
            if trial_tl_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_tl_p.frameNStart = frameN  # exact frame index
                trial_tl_p.tStart = t  # local t and not account for scr refresh
                trial_tl_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_tl_p, 'tStartRefresh')  # time at next scr refresh
                trial_tl_p.setAutoDraw(True)
            
            # *trial_tl_o* updates
            if trial_tl_o.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_tl_o.frameNStart = frameN  # exact frame index
                trial_tl_o.tStart = t  # local t and not account for scr refresh
                trial_tl_o.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_tl_o, 'tStartRefresh')  # time at next scr refresh
                trial_tl_o.setAutoDraw(True)
            
            # *trial_bl_p* updates
            if trial_bl_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_bl_p.frameNStart = frameN  # exact frame index
                trial_bl_p.tStart = t  # local t and not account for scr refresh
                trial_bl_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_bl_p, 'tStartRefresh')  # time at next scr refresh
                trial_bl_p.setAutoDraw(True)
            
            # *trial_bl_o* updates
            if trial_bl_o.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_bl_o.frameNStart = frameN  # exact frame index
                trial_bl_o.tStart = t  # local t and not account for scr refresh
                trial_bl_o.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_bl_o, 'tStartRefresh')  # time at next scr refresh
                trial_bl_o.setAutoDraw(True)
            
            # *trial_tr_p* updates
            if trial_tr_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_tr_p.frameNStart = frameN  # exact frame index
                trial_tr_p.tStart = t  # local t and not account for scr refresh
                trial_tr_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_tr_p, 'tStartRefresh')  # time at next scr refresh
                trial_tr_p.setAutoDraw(True)
            
            # *trial_tr_o* updates
            if trial_tr_o.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_tr_o.frameNStart = frameN  # exact frame index
                trial_tr_o.tStart = t  # local t and not account for scr refresh
                trial_tr_o.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_tr_o, 'tStartRefresh')  # time at next scr refresh
                trial_tr_o.setAutoDraw(True)
            
            # *trial_br_p* updates
            if trial_br_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_br_p.frameNStart = frameN  # exact frame index
                trial_br_p.tStart = t  # local t and not account for scr refresh
                trial_br_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_br_p, 'tStartRefresh')  # time at next scr refresh
                trial_br_p.setAutoDraw(True)
            
            # *trial_br_o* updates
            if trial_br_o.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_br_o.frameNStart = frameN  # exact frame index
                trial_br_o.tStart = t  # local t and not account for scr refresh
                trial_br_o.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_br_o, 'tStartRefresh')  # time at next scr refresh
                trial_br_o.setAutoDraw(True)
            
            # *topleft_header* updates
            if topleft_header.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                topleft_header.frameNStart = frameN  # exact frame index
                topleft_header.tStart = t  # local t and not account for scr refresh
                topleft_header.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(topleft_header, 'tStartRefresh')  # time at next scr refresh
                topleft_header.setAutoDraw(True)
            
            # *topright_header* updates
            if topright_header.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                topright_header.frameNStart = frameN  # exact frame index
                topright_header.tStart = t  # local t and not account for scr refresh
                topright_header.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(topright_header, 'tStartRefresh')  # time at next scr refresh
                topright_header.setAutoDraw(True)
            
            # *bottomtop_header* updates
            if bottomtop_header.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bottomtop_header.frameNStart = frameN  # exact frame index
                bottomtop_header.tStart = t  # local t and not account for scr refresh
                bottomtop_header.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bottomtop_header, 'tStartRefresh')  # time at next scr refresh
                bottomtop_header.setAutoDraw(True)
            
            # *bottombottom_header* updates
            if bottombottom_header.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                bottombottom_header.frameNStart = frameN  # exact frame index
                bottombottom_header.tStart = t  # local t and not account for scr refresh
                bottombottom_header.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bottombottom_header, 'tStartRefresh')  # time at next scr refresh
                bottombottom_header.setAutoDraw(True)
            
            # *trial_header_p* updates
            if trial_header_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_header_p.frameNStart = frameN  # exact frame index
                trial_header_p.tStart = t  # local t and not account for scr refresh
                trial_header_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_header_p, 'tStartRefresh')  # time at next scr refresh
                trial_header_p.setAutoDraw(True)
            
            # *trial_header_o* updates
            if trial_header_o.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_header_o.frameNStart = frameN  # exact frame index
                trial_header_o.tStart = t  # local t and not account for scr refresh
                trial_header_o.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_header_o, 'tStartRefresh')  # time at next scr refresh
                trial_header_o.setAutoDraw(True)
            
            # *left_choice* updates
            if left_choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                left_choice.frameNStart = frameN  # exact frame index
                left_choice.tStart = t  # local t and not account for scr refresh
                left_choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_choice, 'tStartRefresh')  # time at next scr refresh
                left_choice.setAutoDraw(True)
            
            # *leftchoice_text* updates
            if leftchoice_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                leftchoice_text.frameNStart = frameN  # exact frame index
                leftchoice_text.tStart = t  # local t and not account for scr refresh
                leftchoice_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftchoice_text, 'tStartRefresh')  # time at next scr refresh
                leftchoice_text.setAutoDraw(True)
            
            # *right_choice* updates
            if right_choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                right_choice.frameNStart = frameN  # exact frame index
                right_choice.tStart = t  # local t and not account for scr refresh
                right_choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_choice, 'tStartRefresh')  # time at next scr refresh
                right_choice.setAutoDraw(True)
            
            # *rightchoice_text* updates
            if rightchoice_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rightchoice_text.frameNStart = frameN  # exact frame index
                rightchoice_text.tStart = t  # local t and not account for scr refresh
                rightchoice_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightchoice_text, 'tStartRefresh')  # time at next scr refresh
                rightchoice_text.setAutoDraw(True)
            # *trial_mouse* updates
            if trial_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_mouse.frameNStart = frameN  # exact frame index
                trial_mouse.tStart = t  # local t and not account for scr refresh
                trial_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_mouse, 'tStartRefresh')  # time at next scr refresh
                trial_mouse.status = STARTED
                trial_mouse.mouseClock.reset()
                prevButtonState = trial_mouse.getPressed()  # if button is down already this ISN'T a new click
            if trial_mouse.status == STARTED:  # only update if started and not finished!
                buttons = trial_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([left_choice, right_choice])
                            clickableList = [left_choice, right_choice]
                        except:
                            clickableList = [[left_choice, right_choice]]
                        for obj in clickableList:
                            if obj.contains(trial_mouse):
                                gotValidClick = True
                                trial_mouse.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # *make_your_choice_text* updates
            if make_your_choice_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                make_your_choice_text.frameNStart = frameN  # exact frame index
                make_your_choice_text.tStart = t  # local t and not account for scr refresh
                make_your_choice_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(make_your_choice_text, 'tStartRefresh')  # time at next scr refresh
                make_your_choice_text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from trial_code
        #Adding button text to data file
        trial_loop.addData('left_text', left_text)
        trial_loop.addData('right_text', right_text)
        
        #Saving choice
        if trial_mouse.isPressedIn(left_choice):
            choice = left_text
        elif trial_mouse.isPressedIn(right_choice):
            choice = right_text
        trial_loop.addData('choice_pd', choice)
        
        choice_list.append(choice)
        
        #Creating tit for tat strategy (i.e. the other player mimics the participant)
        if trial_loop.thisTrialN == 0:
            other_choice = initial_other_choice
        elif trial_loop.thisTrialN > 0:
            other_choice = choice_list[-2]
        
        trial_loop.addData('other_choice', other_choice)
        
        #Saving points gained
        if choice == 'Cooperate' and other_choice == 'Cooperate':
            participant_points = tl_p
            other_points = tl_o
        elif choice == 'Defect' and other_choice == 'Defect':
            participant_points = br_p
            other_points = br_o
        elif choice == 'Cooperate' and other_choice == 'Defect':
            participant_points = bl_p
            other_points = bl_o
        elif choice == 'Defect' and other_choice == 'Cooperate':
            participant_points = tr_p
            other_points = tr_o
        
        other_points_total += other_points
        
        trial_loop.addData('participant_points', participant_points)
        trial_loop.addData('other_points', other_points)
        trial_loop.addData('other_points_total', other_points_total)
        
        
        # store data for trial_loop (TrialHandler)
        x, y = trial_mouse.getPos()
        buttons = trial_mouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter([left_choice, right_choice])
                clickableList = [left_choice, right_choice]
            except:
                clickableList = [[left_choice, right_choice]]
            for obj in clickableList:
                if obj.contains(trial_mouse):
                    gotValidClick = True
                    trial_mouse.clicked_name.append(obj.name)
        trial_loop.addData('trial_mouse.x', x)
        trial_loop.addData('trial_mouse.y', y)
        trial_loop.addData('trial_mouse.leftButton', buttons[0])
        trial_loop.addData('trial_mouse.midButton', buttons[1])
        trial_loop.addData('trial_mouse.rightButton', buttons[2])
        if len(trial_mouse.clicked_name):
            trial_loop.addData('trial_mouse.clicked_name', trial_mouse.clicked_name[0])
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "multiply" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from mult_code
        #Changing position of stimuli based on player's position
        if participant_points==0:
            continueRoutine=False
            choice_dd='Z'
        
        if participant_points_total > other_points_total or participant_points_total == other_points_total:
            p_av = (-0.3,-0.45)
            o_av = (-0.3, - 0.6)
            p_name = (0, -0.45)
            o_name = (0, - 0.6)
            p_points = (0.3, -0.45)
            o_points = (0.3, - 0.6)
        elif participant_points_total < other_points_total:
            p_av = (-0.3, - 0.6)
            o_av = (-0.3, -0.45)
            p_name = (0, - 0.6)
            o_name = (0, -0.45)
            p_points = (0.3, - 0.6)
            o_points = (0.3, -0.45)
            
        #Randomising button order
        random.shuffle(button_list_dd)
        left_text_dd = button_list_dd[0]
        right_text_dd = button_list_dd[1]
        
        if trial_loop.thisTrialN == 0:
            mult=mult
        elif trial_loop.thisTrialN > 0:
            if choice_list_dd[-1]=='Y' and mult>=1.2:
                mult=mult-increment
            elif choice_list_dd[-1]=='Y' and mult<1.2:
                mult=mult
            elif choice_list_dd[-1]=='N' and mult<=2.8:
                mult=mult+increment
            elif choice_list_dd[-1]=='N' and mult>2.8:
                mult=mult
        
        if left_text_dd=='Yes':
            left_text_dd='Yes\n{}x{}'.format(round(participant_points,1),mult)
        elif left_text_dd=='No':
            left_text_dd='No\n{}'.format(round(participant_points,1))
            
        if right_text_dd=='Yes':
            right_text_dd='Yes\n{}x{}'.format(round(participant_points,1),mult)
        elif right_text_dd=='No':
            right_text_dd='No\n{}'.format(round(participant_points,1))
        
        #Changing bottom text to only show on first trial
        if trial_loop.thisTrialN == 0:
            trial_bottom_text = "Make your choice by clicking one of the boxes"
        else:
            trial_bottom_text = "                                             "
        
        
        
        
        mult_avatar_o.setImage(other_avatar)
        mult_avatar_p.setImage(chosen_avatar)
        mult_choice_p.setText("You chose to {}".format(choice))
        mult_choice_o.setText("{} chose to {}".format(other_name, other_choice))
        mult_points_p.setText("You gain {} points".format(participant_points))
        mult_points_o.setText("{} gains {} points".format(other_name, other_points))
        mult_left_text.setText(left_text_dd)
        mult_right_text.setText(right_text_dd)
        make_your_choice_text_2.setText(trial_bottom_text)
        # setup some python lists for storing info about the mult_mouse
        mult_mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        multiplyComponents = [mult_avatar_o, mult_avatar_p, mult_choice_p, mult_choice_o, mult_points_p, mult_points_o, mult_left, mult_left_text, mult_right, mult_right_text, mult_mult, make_your_choice_text_2, mult_mouse]
        for thisComponent in multiplyComponents:
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
        
        # --- Run Routine "multiply" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *mult_avatar_o* updates
            if mult_avatar_o.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mult_avatar_o.frameNStart = frameN  # exact frame index
                mult_avatar_o.tStart = t  # local t and not account for scr refresh
                mult_avatar_o.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mult_avatar_o, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mult_avatar_o.started')
                mult_avatar_o.setAutoDraw(True)
            
            # *mult_avatar_p* updates
            if mult_avatar_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mult_avatar_p.frameNStart = frameN  # exact frame index
                mult_avatar_p.tStart = t  # local t and not account for scr refresh
                mult_avatar_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mult_avatar_p, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mult_avatar_p.started')
                mult_avatar_p.setAutoDraw(True)
            
            # *mult_choice_p* updates
            if mult_choice_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mult_choice_p.frameNStart = frameN  # exact frame index
                mult_choice_p.tStart = t  # local t and not account for scr refresh
                mult_choice_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mult_choice_p, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mult_choice_p.started')
                mult_choice_p.setAutoDraw(True)
            
            # *mult_choice_o* updates
            if mult_choice_o.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mult_choice_o.frameNStart = frameN  # exact frame index
                mult_choice_o.tStart = t  # local t and not account for scr refresh
                mult_choice_o.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mult_choice_o, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mult_choice_o.started')
                mult_choice_o.setAutoDraw(True)
            
            # *mult_points_p* updates
            if mult_points_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mult_points_p.frameNStart = frameN  # exact frame index
                mult_points_p.tStart = t  # local t and not account for scr refresh
                mult_points_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mult_points_p, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mult_points_p.started')
                mult_points_p.setAutoDraw(True)
            
            # *mult_points_o* updates
            if mult_points_o.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mult_points_o.frameNStart = frameN  # exact frame index
                mult_points_o.tStart = t  # local t and not account for scr refresh
                mult_points_o.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mult_points_o, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mult_points_o.started')
                mult_points_o.setAutoDraw(True)
            
            # *mult_left* updates
            if mult_left.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                mult_left.frameNStart = frameN  # exact frame index
                mult_left.tStart = t  # local t and not account for scr refresh
                mult_left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mult_left, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mult_left.started')
                mult_left.setAutoDraw(True)
            
            # *mult_left_text* updates
            if mult_left_text.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                mult_left_text.frameNStart = frameN  # exact frame index
                mult_left_text.tStart = t  # local t and not account for scr refresh
                mult_left_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mult_left_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mult_left_text.started')
                mult_left_text.setAutoDraw(True)
            
            # *mult_right* updates
            if mult_right.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                mult_right.frameNStart = frameN  # exact frame index
                mult_right.tStart = t  # local t and not account for scr refresh
                mult_right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mult_right, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mult_right.started')
                mult_right.setAutoDraw(True)
            
            # *mult_right_text* updates
            if mult_right_text.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                mult_right_text.frameNStart = frameN  # exact frame index
                mult_right_text.tStart = t  # local t and not account for scr refresh
                mult_right_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mult_right_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mult_right_text.started')
                mult_right_text.setAutoDraw(True)
            
            # *mult_mult* updates
            if mult_mult.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                mult_mult.frameNStart = frameN  # exact frame index
                mult_mult.tStart = t  # local t and not account for scr refresh
                mult_mult.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mult_mult, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mult_mult.started')
                mult_mult.setAutoDraw(True)
            
            # *make_your_choice_text_2* updates
            if make_your_choice_text_2.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                make_your_choice_text_2.frameNStart = frameN  # exact frame index
                make_your_choice_text_2.tStart = t  # local t and not account for scr refresh
                make_your_choice_text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(make_your_choice_text_2, 'tStartRefresh')  # time at next scr refresh
                make_your_choice_text_2.setAutoDraw(True)
            # *mult_mouse* updates
            if mult_mouse.status == NOT_STARTED and t >= 4-frameTolerance:
                # keep track of start time/frame for later
                mult_mouse.frameNStart = frameN  # exact frame index
                mult_mouse.tStart = t  # local t and not account for scr refresh
                mult_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mult_mouse, 'tStartRefresh')  # time at next scr refresh
                mult_mouse.status = STARTED
                mult_mouse.mouseClock.reset()
                prevButtonState = mult_mouse.getPressed()  # if button is down already this ISN'T a new click
            if mult_mouse.status == STARTED:  # only update if started and not finished!
                buttons = mult_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([mult_left, mult_right])
                            clickableList = [mult_left, mult_right]
                        except:
                            clickableList = [[mult_left, mult_right]]
                        for obj in clickableList:
                            if obj.contains(mult_mouse):
                                gotValidClick = True
                                mult_mouse.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in multiplyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "multiply" ---
        for thisComponent in multiplyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from mult_code
        #Adding button text to data file
        trial_loop.addData('left_text_dd', left_text_dd)
        trial_loop.addData('right_text_dd', right_text_dd)
        
        #Saving choice
        if trial_mouse.isPressedIn(mult_left):
            choice_dd = left_text_dd[0]
        elif trial_mouse.isPressedIn(mult_right):
            choice_dd = right_text_dd[0]
        trial_loop.addData('choice_dd', choice_dd)
        
        choice_list_dd.append(choice_dd)
                
        if choice_dd=='Y':
            participant_points=round(participant_points*mult,1)
            
        participant_points_total+=round(participant_points,1)
        
        trial_loop.addData('participant_points_multiplied', participant_points)
        trial_loop.addData('participant_points_total', participant_points_total)
        # store data for trial_loop (TrialHandler)
        x, y = mult_mouse.getPos()
        buttons = mult_mouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter([mult_left, mult_right])
                clickableList = [mult_left, mult_right]
            except:
                clickableList = [[mult_left, mult_right]]
            for obj in clickableList:
                if obj.contains(mult_mouse):
                    gotValidClick = True
                    mult_mouse.clicked_name.append(obj.name)
        trial_loop.addData('mult_mouse.x', x)
        trial_loop.addData('mult_mouse.y', y)
        trial_loop.addData('mult_mouse.leftButton', buttons[0])
        trial_loop.addData('mult_mouse.midButton', buttons[1])
        trial_loop.addData('mult_mouse.rightButton', buttons[2])
        if len(mult_mouse.clicked_name):
            trial_loop.addData('mult_mouse.clicked_name', mult_mouse.clicked_name[0])
        # the Routine "multiply" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from feedback_code
        #Changing position of stimuli based on player's position
        if choice_dd[0]=='Y':
            core.wait(5)
        
        if participant_points_total > other_points_total or participant_points_total == other_points_total:
            p_av = (-0.3,-0.45)
            o_av = (-0.3, - 0.6)
            p_name = (0, -0.45)
            o_name = (0, - 0.6)
            p_points = (0.3, -0.45)
            o_points = (0.3, - 0.6)
        elif participant_points_total < other_points_total:
            p_av = (-0.3, - 0.6)
            o_av = (-0.3, -0.45)
            p_name = (0, - 0.6)
            o_name = (0, -0.45)
            p_points = (0.3, - 0.6)
            o_points = (0.3, -0.45)
        feedback_scoreboard_o.setPos(o_av)
        feedback_scoreboard_o.setImage(other_avatar)
        feedback_scoreboard_p.setPos(p_av)
        feedback_scoreboard_p.setImage(chosen_avatar)
        feedback_avatar_o.setImage(other_avatar)
        feedback_avatar_p.setImage(chosen_avatar)
        feedback_choice_p.setText("You chose to {}".format(choice))
        feedback_choice_o.setText("{} chose to {}".format(other_name, other_choice))
        feedback_points_p.setText("You gain {} points".format(participant_points))
        feedback_points_o.setText("{} gains {} points".format(other_name, other_points))
        feedback_total_p.setPos(p_points)
        feedback_total_p.setText(participant_points_total)
        feedback_total_o.setPos(o_points)
        feedback_total_o.setText(other_points_total)
        feedback_name_p.setPos(p_name)
        feedback_name_p.setText(username)
        feedback_name_o.setPos(o_name)
        feedback_name_o.setText(other_name)
        # setup some python lists for storing info about the feedback_mouse
        feedback_mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        feedbackComponents = [feedback_scoreboard_o, feedback_scoreboard_p, feedback_avatar_o, feedback_avatar_p, feedback_choice_p, feedback_choice_o, feedback_points_p, feedback_points_o, feedback_total_p, feedback_total_o, feedback_name_p, feedback_name_o, feedback_scoreboard, feedback_cont, feedback_mouse]
        for thisComponent in feedbackComponents:
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
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_scoreboard_o* updates
            if feedback_scoreboard_o.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_scoreboard_o.frameNStart = frameN  # exact frame index
                feedback_scoreboard_o.tStart = t  # local t and not account for scr refresh
                feedback_scoreboard_o.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_scoreboard_o, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_scoreboard_o.started')
                feedback_scoreboard_o.setAutoDraw(True)
            
            # *feedback_scoreboard_p* updates
            if feedback_scoreboard_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_scoreboard_p.frameNStart = frameN  # exact frame index
                feedback_scoreboard_p.tStart = t  # local t and not account for scr refresh
                feedback_scoreboard_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_scoreboard_p, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_scoreboard_p.started')
                feedback_scoreboard_p.setAutoDraw(True)
            
            # *feedback_avatar_o* updates
            if feedback_avatar_o.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_avatar_o.frameNStart = frameN  # exact frame index
                feedback_avatar_o.tStart = t  # local t and not account for scr refresh
                feedback_avatar_o.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_avatar_o, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_avatar_o.started')
                feedback_avatar_o.setAutoDraw(True)
            
            # *feedback_avatar_p* updates
            if feedback_avatar_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_avatar_p.frameNStart = frameN  # exact frame index
                feedback_avatar_p.tStart = t  # local t and not account for scr refresh
                feedback_avatar_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_avatar_p, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_avatar_p.started')
                feedback_avatar_p.setAutoDraw(True)
            
            # *feedback_choice_p* updates
            if feedback_choice_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_choice_p.frameNStart = frameN  # exact frame index
                feedback_choice_p.tStart = t  # local t and not account for scr refresh
                feedback_choice_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_choice_p, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_choice_p.started')
                feedback_choice_p.setAutoDraw(True)
            
            # *feedback_choice_o* updates
            if feedback_choice_o.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_choice_o.frameNStart = frameN  # exact frame index
                feedback_choice_o.tStart = t  # local t and not account for scr refresh
                feedback_choice_o.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_choice_o, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_choice_o.started')
                feedback_choice_o.setAutoDraw(True)
            
            # *feedback_points_p* updates
            if feedback_points_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_points_p.frameNStart = frameN  # exact frame index
                feedback_points_p.tStart = t  # local t and not account for scr refresh
                feedback_points_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_points_p, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_points_p.started')
                feedback_points_p.setAutoDraw(True)
            
            # *feedback_points_o* updates
            if feedback_points_o.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_points_o.frameNStart = frameN  # exact frame index
                feedback_points_o.tStart = t  # local t and not account for scr refresh
                feedback_points_o.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_points_o, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_points_o.started')
                feedback_points_o.setAutoDraw(True)
            
            # *feedback_total_p* updates
            if feedback_total_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_total_p.frameNStart = frameN  # exact frame index
                feedback_total_p.tStart = t  # local t and not account for scr refresh
                feedback_total_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_total_p, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_total_p.started')
                feedback_total_p.setAutoDraw(True)
            
            # *feedback_total_o* updates
            if feedback_total_o.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_total_o.frameNStart = frameN  # exact frame index
                feedback_total_o.tStart = t  # local t and not account for scr refresh
                feedback_total_o.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_total_o, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_total_o.started')
                feedback_total_o.setAutoDraw(True)
            
            # *feedback_name_p* updates
            if feedback_name_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_name_p.frameNStart = frameN  # exact frame index
                feedback_name_p.tStart = t  # local t and not account for scr refresh
                feedback_name_p.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_name_p, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_name_p.started')
                feedback_name_p.setAutoDraw(True)
            
            # *feedback_name_o* updates
            if feedback_name_o.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_name_o.frameNStart = frameN  # exact frame index
                feedback_name_o.tStart = t  # local t and not account for scr refresh
                feedback_name_o.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_name_o, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_name_o.started')
                feedback_name_o.setAutoDraw(True)
            
            # *feedback_scoreboard* updates
            if feedback_scoreboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_scoreboard.frameNStart = frameN  # exact frame index
                feedback_scoreboard.tStart = t  # local t and not account for scr refresh
                feedback_scoreboard.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_scoreboard, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_scoreboard.started')
                feedback_scoreboard.setAutoDraw(True)
            
            # *feedback_cont* updates
            if feedback_cont.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_cont.frameNStart = frameN  # exact frame index
                feedback_cont.tStart = t  # local t and not account for scr refresh
                feedback_cont.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_cont, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_cont.started')
                feedback_cont.setAutoDraw(True)
            # *feedback_mouse* updates
            if feedback_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_mouse.frameNStart = frameN  # exact frame index
                feedback_mouse.tStart = t  # local t and not account for scr refresh
                feedback_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('feedback_mouse.started', t)
                feedback_mouse.status = STARTED
                feedback_mouse.mouseClock.reset()
                prevButtonState = feedback_mouse.getPressed()  # if button is down already this ISN'T a new click
            if feedback_mouse.status == STARTED:  # only update if started and not finished!
                buttons = feedback_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter(feedback_cont)
                            clickableList = feedback_cont
                        except:
                            clickableList = [feedback_cont]
                        for obj in clickableList:
                            if obj.contains(feedback_mouse):
                                gotValidClick = True
                                feedback_mouse.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # abort routine on response
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trial_loop (TrialHandler)
        # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trial_loop'
    
    
    # --- Prepare to start Routine "score" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from scoreboard_code
    #Changing position of stimuli based on player's position
    if participant_points_total > other_points_total or participant_points_total == other_points_total:
        p_av = (-0.3, 0.2)
        o_av = (-0.3, - 0.2)
        p_name = (0, 0.2)
        o_name = (0, - 0.2)
        p_points = (0.3, 0.2)
        o_points = (0.3, -0.2)
    elif participant_points_total < other_points_total:
        p_av = (-0.3, -0.2)
        o_av = (-0.3, 0.2)
        p_name = (0, -0.2)
        o_name = (0, 0.2)
        p_points = (0.3, - 0.2)
        o_points = (0.3, 0.2)
        
    
    #Changing text at bottom
    if initial_choice_loop.thisTrialN == 0:
        scoreboard_continue_text_message = "click HERE to play against a new person!"
    else:
        scoreboard_continue_text_message = "click HERE to continue"
    p_total_text.setPos(p_points)
    p_total_text.setText(participant_points_total)
    o_total_text.setPos(o_points)
    o_total_text.setText(other_points_total)
    participant_avatar_scoreboard.setPos(p_av)
    participant_avatar_scoreboard.setImage(chosen_avatar)
    p_name_text.setPos(p_name)
    p_name_text.setText(username)
    o_name_text.setPos(o_name)
    o_name_text.setText(other_name)
    other_avatar_scoreboard.setPos(o_av)
    other_avatar_scoreboard.setImage(other_avatar)
    scoreboard_cont_text.setText(scoreboard_continue_text_message)
    # setup some python lists for storing info about the scoreabord_mouse
    scoreabord_mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    scoreboard_intro_text.setText("Well done you have finished playing with {}!".format(other_name))
    # keep track of which components have finished
    scoreComponents = [p_total_text, o_total_text, participant_avatar_scoreboard, p_name_text, o_name_text, other_avatar_scoreboard, name_header, total_point_header, scoreboard_cont_text, scoreabord_mouse, scoreboard_intro_text]
    for thisComponent in scoreComponents:
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
    
    # --- Run Routine "score" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *p_total_text* updates
        if p_total_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_total_text.frameNStart = frameN  # exact frame index
            p_total_text.tStart = t  # local t and not account for scr refresh
            p_total_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_total_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'p_total_text.started')
            p_total_text.setAutoDraw(True)
        
        # *o_total_text* updates
        if o_total_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            o_total_text.frameNStart = frameN  # exact frame index
            o_total_text.tStart = t  # local t and not account for scr refresh
            o_total_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(o_total_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'o_total_text.started')
            o_total_text.setAutoDraw(True)
        
        # *participant_avatar_scoreboard* updates
        if participant_avatar_scoreboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            participant_avatar_scoreboard.frameNStart = frameN  # exact frame index
            participant_avatar_scoreboard.tStart = t  # local t and not account for scr refresh
            participant_avatar_scoreboard.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(participant_avatar_scoreboard, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'participant_avatar_scoreboard.started')
            participant_avatar_scoreboard.setAutoDraw(True)
        
        # *p_name_text* updates
        if p_name_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            p_name_text.frameNStart = frameN  # exact frame index
            p_name_text.tStart = t  # local t and not account for scr refresh
            p_name_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(p_name_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'p_name_text.started')
            p_name_text.setAutoDraw(True)
        
        # *o_name_text* updates
        if o_name_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            o_name_text.frameNStart = frameN  # exact frame index
            o_name_text.tStart = t  # local t and not account for scr refresh
            o_name_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(o_name_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'o_name_text.started')
            o_name_text.setAutoDraw(True)
        
        # *other_avatar_scoreboard* updates
        if other_avatar_scoreboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            other_avatar_scoreboard.frameNStart = frameN  # exact frame index
            other_avatar_scoreboard.tStart = t  # local t and not account for scr refresh
            other_avatar_scoreboard.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(other_avatar_scoreboard, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'other_avatar_scoreboard.started')
            other_avatar_scoreboard.setAutoDraw(True)
        
        # *name_header* updates
        if name_header.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            name_header.frameNStart = frameN  # exact frame index
            name_header.tStart = t  # local t and not account for scr refresh
            name_header.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(name_header, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'name_header.started')
            name_header.setAutoDraw(True)
        
        # *total_point_header* updates
        if total_point_header.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            total_point_header.frameNStart = frameN  # exact frame index
            total_point_header.tStart = t  # local t and not account for scr refresh
            total_point_header.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(total_point_header, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'total_point_header.started')
            total_point_header.setAutoDraw(True)
        
        # *scoreboard_cont_text* updates
        if scoreboard_cont_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            scoreboard_cont_text.frameNStart = frameN  # exact frame index
            scoreboard_cont_text.tStart = t  # local t and not account for scr refresh
            scoreboard_cont_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scoreboard_cont_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'scoreboard_cont_text.started')
            scoreboard_cont_text.setAutoDraw(True)
        # *scoreabord_mouse* updates
        if scoreabord_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            scoreabord_mouse.frameNStart = frameN  # exact frame index
            scoreabord_mouse.tStart = t  # local t and not account for scr refresh
            scoreabord_mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scoreabord_mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('scoreabord_mouse.started', t)
            scoreabord_mouse.status = STARTED
            scoreabord_mouse.mouseClock.reset()
            prevButtonState = scoreabord_mouse.getPressed()  # if button is down already this ISN'T a new click
        if scoreabord_mouse.status == STARTED:  # only update if started and not finished!
            buttons = scoreabord_mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(scoreboard_cont_text)
                        clickableList = scoreboard_cont_text
                    except:
                        clickableList = [scoreboard_cont_text]
                    for obj in clickableList:
                        if obj.contains(scoreabord_mouse):
                            gotValidClick = True
                            scoreabord_mouse.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *scoreboard_intro_text* updates
        if scoreboard_intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            scoreboard_intro_text.frameNStart = frameN  # exact frame index
            scoreboard_intro_text.tStart = t  # local t and not account for scr refresh
            scoreboard_intro_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scoreboard_intro_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'scoreboard_intro_text.started')
            scoreboard_intro_text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scoreComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "score" ---
    for thisComponent in scoreComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for initial_choice_loop (TrialHandler)
    # the Routine "score" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'initial_choice_loop'


# --- Prepare to start Routine "finish" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# setup some python lists for storing info about the end_routine_mouse
end_routine_mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
finishComponents = [end_routine_text, end_routine_continue_text, end_routine_mouse]
for thisComponent in finishComponents:
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

# --- Run Routine "finish" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_routine_text* updates
    if end_routine_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_routine_text.frameNStart = frameN  # exact frame index
        end_routine_text.tStart = t  # local t and not account for scr refresh
        end_routine_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_routine_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_routine_text.started')
        end_routine_text.setAutoDraw(True)
    
    # *end_routine_continue_text* updates
    if end_routine_continue_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_routine_continue_text.frameNStart = frameN  # exact frame index
        end_routine_continue_text.tStart = t  # local t and not account for scr refresh
        end_routine_continue_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_routine_continue_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_routine_continue_text.started')
        end_routine_continue_text.setAutoDraw(True)
    # *end_routine_mouse* updates
    if end_routine_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_routine_mouse.frameNStart = frameN  # exact frame index
        end_routine_mouse.tStart = t  # local t and not account for scr refresh
        end_routine_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_routine_mouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('end_routine_mouse.started', t)
        end_routine_mouse.status = STARTED
        end_routine_mouse.mouseClock.reset()
        prevButtonState = end_routine_mouse.getPressed()  # if button is down already this ISN'T a new click
    if end_routine_mouse.status == STARTED:  # only update if started and not finished!
        buttons = end_routine_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(end_routine_continue_text)
                    clickableList = end_routine_continue_text
                except:
                    clickableList = [end_routine_continue_text]
                for obj in clickableList:
                    if obj.contains(end_routine_mouse):
                        gotValidClick = True
                        end_routine_mouse.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "finish" ---
for thisComponent in finishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "finish" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
