/********************* 
 * Cogfluxcloud *
 *********************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'CogFluxCloud';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'assignment': '001',
    'project': '001',
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(consentForm_1RoutineBegin());
flowScheduler.add(consentForm_1RoutineEachFrame());
flowScheduler.add(consentForm_1RoutineEnd());
flowScheduler.add(consentForm_2RoutineBegin());
flowScheduler.add(consentForm_2RoutineEachFrame());
flowScheduler.add(consentForm_2RoutineEnd());
flowScheduler.add(exclusionRoutineBegin());
flowScheduler.add(exclusionRoutineEachFrame());
flowScheduler.add(exclusionRoutineEnd());
flowScheduler.add(instructColorRoutineBegin());
flowScheduler.add(instructColorRoutineEachFrame());
flowScheduler.add(instructColorRoutineEnd());
const loop10_colorblindLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(loop10_colorblindLoopBegin(loop10_colorblindLoopScheduler));
flowScheduler.add(loop10_colorblindLoopScheduler);
flowScheduler.add(loop10_colorblindLoopEnd);


flowScheduler.add(instructTrialRoutineBegin());
flowScheduler.add(instructTrialRoutineEachFrame());
flowScheduler.add(instructTrialRoutineEnd());
const exp_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(exp_loopLoopBegin(exp_loopLoopScheduler));
flowScheduler.add(exp_loopLoopScheduler);
flowScheduler.add(exp_loopLoopEnd);










flowScheduler.add(PreMEQRoutineBegin());
flowScheduler.add(PreMEQRoutineEachFrame());
flowScheduler.add(PreMEQRoutineEnd());
flowScheduler.add(bestfeel_meqRoutineBegin());
flowScheduler.add(bestfeel_meqRoutineEachFrame());
flowScheduler.add(bestfeel_meqRoutineEnd());
flowScheduler.add(wokentired_meqRoutineBegin());
flowScheduler.add(wokentired_meqRoutineEachFrame());
flowScheduler.add(wokentired_meqRoutineEnd());
flowScheduler.add(sleepytime_meqRoutineBegin());
flowScheduler.add(sleepytime_meqRoutineEachFrame());
flowScheduler.add(sleepytime_meqRoutineEnd());
flowScheduler.add(bestpeak_meqRoutineBegin());
flowScheduler.add(bestpeak_meqRoutineEachFrame());
flowScheduler.add(bestpeak_meqRoutineEnd());
flowScheduler.add(persontype_meqRoutineBegin());
flowScheduler.add(persontype_meqRoutineEachFrame());
flowScheduler.add(persontype_meqRoutineEnd());
flowScheduler.add(what_ageRoutineBegin());
flowScheduler.add(what_ageRoutineEachFrame());
flowScheduler.add(what_ageRoutineEnd());
flowScheduler.add(genderRoutineBegin());
flowScheduler.add(genderRoutineEachFrame());
flowScheduler.add(genderRoutineEnd());
flowScheduler.add(race_ethnRoutineBegin());
flowScheduler.add(race_ethnRoutineEachFrame());
flowScheduler.add(race_ethnRoutineEnd());
flowScheduler.add(ThanksRoutineBegin());
flowScheduler.add(ThanksRoutineEachFrame());
flowScheduler.add(ThanksRoutineEnd());
flowScheduler.add(quitPsychoJS, "Please click 'Ok' to verify completion on CloudResearch.", true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, "Please click 'Ok' to verify completion on CloudResearch.", false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'resources/experimentType.xlsx', 'path': 'resources/experimentType.xlsx'},
    {'name': 'resources/pracConditions_4.xlsx', 'path': 'resources/pracConditions_4.xlsx'},
    {'name': 'resources/trialConditions_48.xlsx', 'path': 'resources/trialConditions_48.xlsx'},
    {'name': 'resources/GV.png', 'path': 'resources/GV.png'},
    {'name': 'resources/RV.png', 'path': 'resources/RV.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'resources/experimentType.xlsx', 'path': 'resources/experimentType.xlsx'},
    {'name': 'resources/GV.png', 'path': 'resources/GV.png'},
    {'name': 'resources/pracConditions_4.xlsx', 'path': 'resources/pracConditions_4.xlsx'},
    {'name': 'resources/RH.png', 'path': 'resources/RH.png'},
    {'name': 'resources/RV.png', 'path': 'resources/RV.png'},
    {'name': 'resources/trialConditions_48.xlsx', 'path': 'resources/trialConditions_48.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('https://connect.cloudresearch.com/participant/project/EB85DB0832/complete', '');


  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var consentForm_1Clock;
var Consent_Form;
var forward;
var click;
var consentForm_2Clock;
var Consent_Form_2;
var SaC;
var consent;
var forward_2;
var click_2;
var exclusionClock;
var ThanksText_2;
var instructColorClock;
var confirmSign_click_14;
var confirmSign_button_14;
var text_4;
var RG_colorblindClock;
var opposite;
var green;
var red;
var mouse;
var instructTrialClock;
var text;
var Start;
var both_trialsClock;
var fixation_3;
var targetRV_2;
var dist1img_2;
var dist2img_2;
var dist3img_2;
var dist4img_2;
var dist5img_2;
var dist6img_2;
var dist7img_2;
var dist8img_2;
var dist9img_2;
var dist10img_2;
var dist11img_2;
var dist12img_2;
var Response_2;
var feedbackClock;
var fd;
var RestClock;
var RestText;
var PreMEQClock;
var form;
var confirmSign_button_3;
var confirmSign_click_3;
var bestfeel_meqClock;
var confirmSign_click_4;
var confirmSign_button_4;
var best_feel_Q;
var best_feel;
var wokentired_meqClock;
var confirmSign_click_6;
var confirmSign_button_6;
var woken_tired_Q;
var woken_tired;
var sleepytime_meqClock;
var confirmSign_click_7;
var confirmSign_button_7;
var sleepy_time_Q;
var sleepy_time;
var bestpeak_meqClock;
var confirmSign_click_8;
var confirmSign_button_8;
var best_peak_Q;
var best_peak;
var persontype_meqClock;
var confirmSign_click_9;
var confirmSign_button_9;
var person_type_Q;
var person_type;
var what_ageClock;
var confirmSign_click_10;
var confirmSign_button_10;
var age_fill_Q;
var age_Q;
var genderClock;
var confirmSign_click_11;
var confirmSign_button_11;
var gender_Q;
var gender_c;
var other_gender_text;
var race_ethnClock;
var confirmSign_click_13;
var confirmSign_button_13;
var race_Q;
var race_c;
var other_race_text;
var ThanksClock;
var ThanksText;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "consentForm_1"
  consentForm_1Clock = new util.Clock();
  Consent_Form = new visual.TextStim({
    win: psychoJS.window,
    name: 'Consent_Form',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.05], draggable: false, height: 0.023,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1, 1, 1]),  opacity: undefined,
    depth: -2.0 
  });
  
  forward = new visual.TextStim({
    win: psychoJS.window,
    name: 'forward',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.023,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  click = new core.Mouse({
    win: psychoJS.window,
  });
  click.mouseClock = new util.Clock();
  // Initialize components for Routine "consentForm_2"
  consentForm_2Clock = new util.Clock();
  Consent_Form_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Consent_Form_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.15], draggable: false, height: 0.023,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1, 1, 1]),  opacity: undefined,
    depth: -1.0 
  });
  
  SaC = new visual.TextStim({
    win: psychoJS.window,
    name: 'SaC',
    text: 'Statement of Consent:\nI have read the above information. Select one of the two following options:',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.15)], draggable: false, height: 0.023,  wrapWidth: 1.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  consent = new visual.Slider({
    win: psychoJS.window, name: 'consent',
    startValue: undefined,
    size: [30, 60], pos: [(- 250), (- 280)], ori: 0.0, units: 'pix',
    labels: ["I consent to participation and am 18 years or older.", "I do not consent to participation or I am younger than 18 years old."], fontSize: 20.0, ticks: [],
    granularity: 1, style: ["RADIO"],
    color: new util.Color('Black'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Arial', bold: true, italic: false, depth: -3, 
    flip: true,
  });
  
  forward_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'forward_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.023,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  click_2 = new core.Mouse({
    win: psychoJS.window,
  });
  click_2.mouseClock = new util.Clock();
  // Initialize components for Routine "exclusion"
  exclusionClock = new util.Clock();
  ThanksText_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ThanksText_2',
    text: 'Sorry, you are not qualified for this experiment.\n\nThank you.\n\nYou can press the [ESC] button to leave.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "instructColor"
  instructColorClock = new util.Clock();
  confirmSign_click_14 = new core.Mouse({
    win: psychoJS.window,
  });
  confirmSign_click_14.mouseClock = new util.Clock();
  confirmSign_button_14 = new visual.TextStim({
    win: psychoJS.window,
    name: 'confirmSign_button_14',
    text: 'Click here to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], draggable: false, height: 0.023,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'After you click the continue button, \na green vertical rectangle and a red vertical rectangle will appear.\n\nClick on the red vertical rectangle.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.023,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, 1.0, 1.0]),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "RG_colorblind"
  RG_colorblindClock = new util.Clock();
  // Run 'Begin Experiment' code from code
  opposite = [(- 1), 1];
  
  green = new visual.ImageStim({
    win : psychoJS.window,
    name : 'green', units : 'pix', 
    image : 'resources/GV.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [25, 100],
    color : new util.Color([0.8, 0.8, 0.8]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  red = new visual.ImageStim({
    win : psychoJS.window,
    name : 'red', units : 'pix', 
    image : 'resources/RV.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [25, 100],
    color : new util.Color([0.8, 0.8, 0.8]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Initialize components for Routine "instructTrial"
  instructTrialClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'In the following task you will be presented with arrays of various colored rectangles (green and red). \n\nYour task is to search for a red vertical rectangle.\n \nPress the [P] key if the red vertical rectangle is PRESENT \nand the [A] key if the red vertical rectangle is ABSENT. \n\nPlease respond as quickly as possible, while minimizing errors.\n\nPress the [spacebar] when you are ready to begin.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.023,  wrapWidth: 1.1, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1.0, 1.0, 1.0]),  opacity: undefined,
    depth: -1.0 
  });
  
  Start = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "both_trials"
  both_trialsClock = new util.Clock();
  fixation_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation_3',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  
  
  targetRV_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'targetRV_2', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [25, 100],
    color : new util.Color([0.8, 0.8, 0.8]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  dist1img_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist1img_2', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : 1.0,
    color : new util.Color([0.8, 0.8, 0.8]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  dist2img_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist2img_2', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : 1.0,
    color : new util.Color([0.8, 0.8, 0.8]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  dist3img_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist3img_2', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : 1.0,
    color : new util.Color([0.8, 0.8, 0.8]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  dist4img_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist4img_2', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : 1.0,
    color : new util.Color([0.8, 0.8, 0.8]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -9.0 
  });
  dist5img_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist5img_2', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : 1.0,
    color : new util.Color([0.8, 0.8, 0.8]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -10.0 
  });
  dist6img_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist6img_2', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : 1.0,
    color : new util.Color([0.8, 0.8, 0.8]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -11.0 
  });
  dist7img_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist7img_2', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : 1.0,
    color : new util.Color([0.8, 0.8, 0.8]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -12.0 
  });
  dist8img_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist8img_2', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : 1.0,
    color : new util.Color([0.8, 0.8, 0.8]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -13.0 
  });
  dist9img_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist9img_2', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : 1.0,
    color : new util.Color([0.8, 0.8, 0.8]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -14.0 
  });
  dist10img_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist10img_2', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : 1.0,
    color : new util.Color([0.8, 0.8, 0.8]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -15.0 
  });
  dist11img_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist11img_2', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : 1.0,
    color : new util.Color([0.8, 0.8, 0.8]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -16.0 
  });
  dist12img_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist12img_2', units : 'pix', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : 1.0,
    color : new util.Color([0.8, 0.8, 0.8]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -17.0 
  });
  Response_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  fd = new visual.TextStim({
    win: psychoJS.window,
    name: 'fd',
    text: 'Incorrect',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1.0,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Rest"
  RestClock = new util.Clock();
  RestText = new visual.TextStim({
    win: psychoJS.window,
    name: 'RestText',
    text: '30 Second Rest\n\nRemember to find the red vertical rectangle.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "PreMEQ"
  PreMEQClock = new util.Clock();
  form = new visual.TextStim({
    win: psychoJS.window,
    name: 'form',
    text: 'Thank you for completing our tasks.\n\nPlease answer the following questions about yourself.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.023,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([1, 1, 1]),  opacity: undefined,
    depth: -1.0 
  });
  
  confirmSign_button_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'confirmSign_button_3',
    text: 'Click here to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.023,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  confirmSign_click_3 = new core.Mouse({
    win: psychoJS.window,
  });
  confirmSign_click_3.mouseClock = new util.Clock();
  // Initialize components for Routine "bestfeel_meq"
  bestfeel_meqClock = new util.Clock();
  confirmSign_click_4 = new core.Mouse({
    win: psychoJS.window,
  });
  confirmSign_click_4.mouseClock = new util.Clock();
  confirmSign_button_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'confirmSign_button_4',
    text: 'Click here to confirm\n[You will not be able to go back]',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], draggable: false, height: 0.023,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  best_feel_Q = new visual.TextStim({
    win: psychoJS.window,
    name: 'best_feel_Q',
    text: 'Considering only your own “best feeling” rhythm, at what time would you get up if you were entirely free to plan your day?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.22], draggable: false, height: 0.023,  wrapWidth: 1.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  best_feel = new visual.Slider({
    win: psychoJS.window, name: 'best_feel',
    startValue: undefined,
    size: [30, 250], pos: [(- 175), 0], ori: 0.0, units: 'pix',
    labels: ["10:45 AM - 12:00 PM", "9:30 AM - 10:45 AM", "7:45 AM - 9:30 AM", "6:30 AM - 7:45 AM", "5:00 AM - 6:30 AM"], fontSize: 18.0, ticks: [],
    granularity: 1, style: ["RADIO"],
    color: new util.Color('White'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Arial', bold: true, italic: false, depth: -4, 
    flip: true,
  });
  
  // Initialize components for Routine "wokentired_meq"
  wokentired_meqClock = new util.Clock();
  confirmSign_click_6 = new core.Mouse({
    win: psychoJS.window,
  });
  confirmSign_click_6.mouseClock = new util.Clock();
  confirmSign_button_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'confirmSign_button_6',
    text: 'Click here to confirm\n[You will not be able to go back]',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], draggable: false, height: 0.023,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  woken_tired_Q = new visual.TextStim({
    win: psychoJS.window,
    name: 'woken_tired_Q',
    text: 'After the first half hour after having woken in the morning, how tired do you feel?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.22], draggable: false, height: 0.023,  wrapWidth: 1.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  woken_tired = new visual.Slider({
    win: psychoJS.window, name: 'woken_tired',
    startValue: undefined,
    size: [30, 250], pos: [(- 175), 0], ori: 0.0, units: 'pix',
    labels: ["Very Refreshed", "Fairly Refreshed", "Fairly Tired", "Very Tired"], fontSize: 18.0, ticks: [],
    granularity: 1, style: ["RADIO"],
    color: new util.Color('White'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Arial', bold: true, italic: false, depth: -4, 
    flip: true,
  });
  
  // Initialize components for Routine "sleepytime_meq"
  sleepytime_meqClock = new util.Clock();
  confirmSign_click_7 = new core.Mouse({
    win: psychoJS.window,
  });
  confirmSign_click_7.mouseClock = new util.Clock();
  confirmSign_button_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'confirmSign_button_7',
    text: 'Click here to confirm\n[You will not be able to go back]',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], draggable: false, height: 0.023,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  sleepy_time_Q = new visual.TextStim({
    win: psychoJS.window,
    name: 'sleepy_time_Q',
    text: 'At what time in the evening would you feel tired and as a result in need of sleep?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.22], draggable: false, height: 0.023,  wrapWidth: 1.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  sleepy_time = new visual.Slider({
    win: psychoJS.window, name: 'sleepy_time',
    startValue: undefined,
    size: [30, 250], pos: [(- 175), 0], ori: 0.0, units: 'pix',
    labels: ["1:45 AM - 3:00 AM", "12:30 AM - 1:45 AM", "10:15 PM - 12:30 AM", "9:00 PM - 10:15 PM", "8:00 PM - 9:00 PM"], fontSize: 18.0, ticks: [],
    granularity: 1, style: ["RADIO"],
    color: new util.Color('White'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Arial', bold: true, italic: false, depth: -4, 
    flip: true,
  });
  
  // Initialize components for Routine "bestpeak_meq"
  bestpeak_meqClock = new util.Clock();
  confirmSign_click_8 = new core.Mouse({
    win: psychoJS.window,
  });
  confirmSign_click_8.mouseClock = new util.Clock();
  confirmSign_button_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'confirmSign_button_8',
    text: 'Click here to confirm\n[You will not be able to go back]',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], draggable: false, height: 0.023,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  best_peak_Q = new visual.TextStim({
    win: psychoJS.window,
    name: 'best_peak_Q',
    text: 'At what time of the day do you think that you reach your “feeling best” peak?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.22], draggable: false, height: 0.023,  wrapWidth: 1.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  best_peak = new visual.Slider({
    win: psychoJS.window, name: 'best_peak',
    startValue: undefined,
    size: [30, 250], pos: [(- 175), 0], ori: 0.0, units: 'pix',
    labels: ["9:30 PM - 4:30 AM", "4:30 PM - 9:30 PM", "9:30 AM - 4:30 PM", "7:30 AM - 9:30 AM", "4:30 AM - 7:30 AM"], fontSize: 18.0, ticks: [],
    granularity: 1, style: ["RADIO"],
    color: new util.Color('White'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Arial', bold: true, italic: false, depth: -4, 
    flip: true,
  });
  
  // Initialize components for Routine "persontype_meq"
  persontype_meqClock = new util.Clock();
  confirmSign_click_9 = new core.Mouse({
    win: psychoJS.window,
  });
  confirmSign_click_9.mouseClock = new util.Clock();
  confirmSign_button_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'confirmSign_button_9',
    text: 'Click here to confirm\n[You will not be able to go back]',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], draggable: false, height: 0.023,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  person_type_Q = new visual.TextStim({
    win: psychoJS.window,
    name: 'person_type_Q',
    text: 'One hears about morning and evening types of people. Which one of these types do you consider yourself to be? ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.22], draggable: false, height: 0.023,  wrapWidth: 1.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  person_type = new visual.Slider({
    win: psychoJS.window, name: 'person_type',
    startValue: undefined,
    size: [30, 250], pos: [(- 175), 0], ori: 0.0, units: 'pix',
    labels: ["Definitely an \"evening\" type", "Rather more a \"evening\" than a \"morning\" type", "Rather more a \"morning\" than an \"evening\" type", "Definitely a \"morning\" type"], fontSize: 18.0, ticks: [],
    granularity: 1, style: ["RADIO"],
    color: new util.Color('White'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Arial', bold: true, italic: false, depth: -4, 
    flip: true,
  });
  
  // Initialize components for Routine "what_age"
  what_ageClock = new util.Clock();
  confirmSign_click_10 = new core.Mouse({
    win: psychoJS.window,
  });
  confirmSign_click_10.mouseClock = new util.Clock();
  confirmSign_button_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'confirmSign_button_10',
    text: 'Click here after you have typed your age.\n[You will not be able to go back]',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.25)], draggable: false, height: 0.023,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  age_fill_Q = new visual.TextStim({
    win: psychoJS.window,
    name: 'age_fill_Q',
    text: 'Enter your age in the textbox below.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.06], draggable: false, height: 0.023,  wrapWidth: 1.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  age_Q = new visual.TextBox({
    win: psychoJS.window,
    name: 'age_Q',
    text: '',
    placeholder: 'Type your age here...',
    font: 'Arial',
    pos: [0, (- 0.05)], 
    draggable: false,
    letterHeight: 0.023,
    lineSpacing: 1.0,
    size: [0.8, 0.1],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -4.0 
  });
  
  // Initialize components for Routine "gender"
  genderClock = new util.Clock();
  confirmSign_click_11 = new core.Mouse({
    win: psychoJS.window,
  });
  confirmSign_click_11.mouseClock = new util.Clock();
  confirmSign_button_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'confirmSign_button_11',
    text: 'Click here to confirm\n[You will not be able to go back]',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.35)], draggable: false, height: 0.023,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  gender_Q = new visual.TextStim({
    win: psychoJS.window,
    name: 'gender_Q',
    text: 'With which gender do you identify?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.36], draggable: false, height: 0.023,  wrapWidth: 1.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  gender_c = new visual.Slider({
    win: psychoJS.window, name: 'gender_c',
    startValue: undefined,
    size: [30, 300], pos: [(- 175), 125], ori: 0.0, units: 'pix',
    labels: ["Other gender (please describe below)", "Transgender male", "Transgender female", "Gender non-binary/genderfluid/genderqueer", "Cisgender male", "Cisgender female"], fontSize: 18.0, ticks: [],
    granularity: 1, style: ["RADIO"],
    color: new util.Color('White'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Arial', bold: true, italic: false, depth: -4, 
    flip: true,
  });
  
  other_gender_text = new visual.TextBox({
    win: psychoJS.window,
    name: 'other_gender_text',
    text: '',
    placeholder: "(Please describe gender here if you chose 'another')",
    font: 'Arial',
    pos: [0, (- 0.2)], 
    draggable: false,
    letterHeight: 0.023,
    lineSpacing: 1.0,
    size: [0.95, 0.2],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -5.0 
  });
  
  // Initialize components for Routine "race_ethn"
  race_ethnClock = new util.Clock();
  confirmSign_click_13 = new core.Mouse({
    win: psychoJS.window,
  });
  confirmSign_click_13.mouseClock = new util.Clock();
  confirmSign_button_13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'confirmSign_button_13',
    text: 'Click here to confirm\n[You will not be able to go back]',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.35)], draggable: false, height: 0.023,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  race_Q = new visual.TextStim({
    win: psychoJS.window,
    name: 'race_Q',
    text: 'Which best describes your race/ethnicity?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.37], draggable: false, height: 0.023,  wrapWidth: 1.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  race_c = new visual.Slider({
    win: psychoJS.window, name: 'race_c',
    startValue: undefined,
    size: [30, 300], pos: [(- 175), 125], ori: 0.0, units: 'pix',
    labels: ["Multiple or Other race/ethnicity (please describe below)", "White", "Middle Eastern or North African", "American Indian or Alaskan Native", "Native Hawaiian or other Pacific Islander", "Asian or Asian-American", "Hispanic, Latinx, or Spanish Origin", "Black or African-American"], fontSize: 18.0, ticks: [],
    granularity: 1, style: ["RADIO"],
    color: new util.Color('White'), markerColor: new util.Color('Red'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Arial', bold: true, italic: false, depth: -4, 
    flip: true,
  });
  
  other_race_text = new visual.TextBox({
    win: psychoJS.window,
    name: 'other_race_text',
    text: '',
    placeholder: "(Please describe race/ethnicity here if you chose 'other')",
    font: 'Arial',
    pos: [0, (- 0.2)], 
    draggable: false,
    letterHeight: 0.023,
    lineSpacing: 1.0,
    size: [0.95, 0.2],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'white',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -5.0 
  });
  
  // Initialize components for Routine "Thanks"
  ThanksClock = new util.Clock();
  ThanksText = new visual.TextStim({
    win: psychoJS.window,
    name: 'ThanksText',
    text: 'Thank you for your participation.\n\nYou will be redirected to CloudResearch...',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var consentForm_1MaxDurationReached;
var gotValidClick;
var consentForm_1MaxDuration;
var consentForm_1Components;
function consentForm_1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'consentForm_1' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    consentForm_1Clock.reset();
    routineTimer.reset();
    consentForm_1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from showMouse
    document.body.style.cursor='auto';
    Consent_Form.setText('Hamilton College\nPsychology Department\n198 College Hill Rd.\nClinton, NY 13323\n\nParticipant Consent Form: Cognitive Fluctuations\n\nPurpose:\nThe purpose of this study is to examine how cognitive performance fluctuates for different people, at different times, while doing different tasks. This study is part of Prof. Alexandra List’s research.\n\nProcedure:\nIf you agree to be in this study, you will be asked to view simple images on a computer screen and respond with specific button presses. You will be asked to respond quickly and accurately. You will also be asked to answer a series of questions about when you prefer to be awake and performing various tasks, in addition to providing basic demographic information (i.e., age, gender, race/ethnicity).\n\nThe total time required to complete the study should be under 15 minutes. If you complete the study, you will receive $2.50 for participating in the study.\n\nBenefits/Risks to Participant:\nParticipants will learn about the empirical methodologies of and will help contribute to the body of knowledge in Psychology. Risks include any boredom you may feel while answering the questions. Breaks can be taken as needed.');
    forward.setText('Click here to continue');
    // setup some python lists for storing info about the click
    // current position of the mouse:
    click.x = [];
    click.y = [];
    click.leftButton = [];
    click.midButton = [];
    click.rightButton = [];
    click.time = [];
    click.clicked_name = [];
    gotValidClick = false; // until a click is received
    psychoJS.experiment.addData('consentForm_1.started', globalClock.getTime());
    consentForm_1MaxDuration = null
    // keep track of which components have finished
    consentForm_1Components = [];
    consentForm_1Components.push(Consent_Form);
    consentForm_1Components.push(forward);
    consentForm_1Components.push(click);
    
    for (const thisComponent of consentForm_1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
var _mouseXYs;
function consentForm_1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'consentForm_1' ---
    // get current time
    t = consentForm_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Consent_Form* updates
    if (t >= 0 && Consent_Form.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Consent_Form.tStart = t;  // (not accounting for frame time here)
      Consent_Form.frameNStart = frameN;  // exact frame index
      
      Consent_Form.setAutoDraw(true);
    }
    
    
    // *forward* updates
    if (t >= 3 && forward.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      forward.tStart = t;  // (not accounting for frame time here)
      forward.frameNStart = frameN;  // exact frame index
      
      forward.setAutoDraw(true);
    }
    
    // *click* updates
    if (t >= 0 && click.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      click.tStart = t;  // (not accounting for frame time here)
      click.frameNStart = frameN;  // exact frame index
      
      click.status = PsychoJS.Status.STARTED;
      click.mouseClock.reset();
      prevButtonState = click.getPressed();  // if button is down already this ISN'T a new click
      }
    if (click.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = click.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          click.clickableObjects = eval(forward)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(click.clickableObjects)) {
              click.clickableObjects = [click.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of click.clickableObjects) {
              if (obj.contains(click)) {
                  gotValidClick = true;
                  click.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              click.clicked_name.push(null);
          }
          _mouseXYs = click.getPos();
          click.x.push(_mouseXYs[0]);
          click.y.push(_mouseXYs[1]);
          click.leftButton.push(_mouseButtons[0]);
          click.midButton.push(_mouseButtons[1]);
          click.rightButton.push(_mouseButtons[2]);
          click.time.push(click.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of consentForm_1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function consentForm_1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'consentForm_1' ---
    for (const thisComponent of consentForm_1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('consentForm_1.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('click.x', click.x);
    psychoJS.experiment.addData('click.y', click.y);
    psychoJS.experiment.addData('click.leftButton', click.leftButton);
    psychoJS.experiment.addData('click.midButton', click.midButton);
    psychoJS.experiment.addData('click.rightButton', click.rightButton);
    psychoJS.experiment.addData('click.time', click.time);
    psychoJS.experiment.addData('click.clicked_name', click.clicked_name);
    
    // the Routine "consentForm_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var consentForm_2MaxDurationReached;
var consentForm_2MaxDuration;
var consentForm_2Components;
function consentForm_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'consentForm_2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    consentForm_2Clock.reset();
    routineTimer.reset();
    consentForm_2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from showMouse_8
    document.body.style.cursor='auto';
    Consent_Form_2.setText('Voluntary Nature of the Study/Confidentiality:\nYour participation in this study is entirely voluntary and you may refuse to complete the study at any point during the experiment, or refuse to answer or skip any questions with which you are uncomfortable. You may also stop at any time. Your name will never be connected to your results or to your responses; instead, a number will be used for data identification purposes. Information that would make it possible to identify you or any other participant will never be included in any sort of report. The data will be accessible only to those working on the project.\n\nContacts and Questions:\nIf you have questions, you may contact Dr. Alexandra List at 315-859-4308 or scct3045@hamilton.edu. Questions or concerns about institutional approval should be directed to Dr. Rachel White, Chair of the Institutional Review Board for Human Subjects, 315-859-4518 or iboard@hamilton.edu.\n\nI have been provided a link to\xa0Hamilton’s Privacy Notice\xa0(https://www.hamilton.edu/privacy) and have read and understood it. I consent to the processing of my personal data and special categories of personal data in accordance with the Privacy Notice and for the purposes of applying to and participating in Hamilton College research studies.');
    consent.reset()
    forward_2.setText('Click here to continue');
    // setup some python lists for storing info about the click_2
    // current position of the mouse:
    click_2.x = [];
    click_2.y = [];
    click_2.leftButton = [];
    click_2.midButton = [];
    click_2.rightButton = [];
    click_2.time = [];
    click_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    psychoJS.experiment.addData('consentForm_2.started', globalClock.getTime());
    consentForm_2MaxDuration = null
    // keep track of which components have finished
    consentForm_2Components = [];
    consentForm_2Components.push(Consent_Form_2);
    consentForm_2Components.push(SaC);
    consentForm_2Components.push(consent);
    consentForm_2Components.push(forward_2);
    consentForm_2Components.push(click_2);
    
    for (const thisComponent of consentForm_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function consentForm_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'consentForm_2' ---
    // get current time
    t = consentForm_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Consent_Form_2* updates
    if (t >= 0 && Consent_Form_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Consent_Form_2.tStart = t;  // (not accounting for frame time here)
      Consent_Form_2.frameNStart = frameN;  // exact frame index
      
      Consent_Form_2.setAutoDraw(true);
    }
    
    
    // *SaC* updates
    if (t >= 0.0 && SaC.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SaC.tStart = t;  // (not accounting for frame time here)
      SaC.frameNStart = frameN;  // exact frame index
      
      SaC.setAutoDraw(true);
    }
    
    
    // *consent* updates
    if (t >= 0 && consent.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consent.tStart = t;  // (not accounting for frame time here)
      consent.frameNStart = frameN;  // exact frame index
      
      consent.setAutoDraw(true);
    }
    
    
    // *forward_2* updates
    if ((consent.rating) && forward_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      forward_2.tStart = t;  // (not accounting for frame time here)
      forward_2.frameNStart = frameN;  // exact frame index
      
      forward_2.setAutoDraw(true);
    }
    
    // *click_2* updates
    if (t >= 0 && click_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      click_2.tStart = t;  // (not accounting for frame time here)
      click_2.frameNStart = frameN;  // exact frame index
      
      click_2.status = PsychoJS.Status.STARTED;
      click_2.mouseClock.reset();
      prevButtonState = click_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (click_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = click_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          click_2.clickableObjects = eval(forward_2)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(click_2.clickableObjects)) {
              click_2.clickableObjects = [click_2.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of click_2.clickableObjects) {
              if (obj.contains(click_2)) {
                  gotValidClick = true;
                  click_2.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              click_2.clicked_name.push(null);
          }
          _mouseXYs = click_2.getPos();
          click_2.x.push(_mouseXYs[0]);
          click_2.y.push(_mouseXYs[1]);
          click_2.leftButton.push(_mouseButtons[0]);
          click_2.midButton.push(_mouseButtons[1]);
          click_2.rightButton.push(_mouseButtons[2]);
          click_2.time.push(click_2.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of consentForm_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function consentForm_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'consentForm_2' ---
    for (const thisComponent of consentForm_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('consentForm_2.stopped', globalClock.getTime());
    psychoJS.experiment.addData('consent.response', consent.getRating());
    psychoJS.experiment.addData('consent.rt', consent.getRT());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('click_2.x', click_2.x);
    psychoJS.experiment.addData('click_2.y', click_2.y);
    psychoJS.experiment.addData('click_2.leftButton', click_2.leftButton);
    psychoJS.experiment.addData('click_2.midButton', click_2.midButton);
    psychoJS.experiment.addData('click_2.rightButton', click_2.rightButton);
    psychoJS.experiment.addData('click_2.time', click_2.time);
    psychoJS.experiment.addData('click_2.clicked_name', click_2.clicked_name);
    
    // the Routine "consentForm_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var exclusionMaxDurationReached;
var exclusionMaxDuration;
var exclusionComponents;
function exclusionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'exclusion' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    exclusionClock.reset();
    routineTimer.reset();
    exclusionMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from exclude_show
    if (consent.rating != "I do not consent to participation or I am younger than 18 years old.") {
        continueRoutine = false;
    }
    
    // Run 'Begin Routine' code from showMouse_9
    document.body.style.cursor='auto';
    psychoJS.experiment.addData('exclusion.started', globalClock.getTime());
    exclusionMaxDuration = null
    // keep track of which components have finished
    exclusionComponents = [];
    exclusionComponents.push(ThanksText_2);
    
    for (const thisComponent of exclusionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function exclusionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'exclusion' ---
    // get current time
    t = exclusionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ThanksText_2* updates
    if (t >= 0.0 && ThanksText_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ThanksText_2.tStart = t;  // (not accounting for frame time here)
      ThanksText_2.frameNStart = frameN;  // exact frame index
      
      ThanksText_2.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of exclusionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function exclusionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'exclusion' ---
    for (const thisComponent of exclusionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('exclusion.stopped', globalClock.getTime());
    // the Routine "exclusion" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instructColorMaxDurationReached;
var instructColorMaxDuration;
var instructColorComponents;
function instructColorRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructColor' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    instructColorClock.reset();
    routineTimer.reset();
    instructColorMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from exclude
    if (consent.rating == "I do not consent to participation or I am younger than 18 years old.") {
        continueRoutine = false;
    }
    
    // setup some python lists for storing info about the confirmSign_click_14
    // current position of the mouse:
    confirmSign_click_14.x = [];
    confirmSign_click_14.y = [];
    confirmSign_click_14.leftButton = [];
    confirmSign_click_14.midButton = [];
    confirmSign_click_14.rightButton = [];
    confirmSign_click_14.time = [];
    confirmSign_click_14.clicked_name = [];
    gotValidClick = false; // until a click is received
    psychoJS.experiment.addData('instructColor.started', globalClock.getTime());
    instructColorMaxDuration = null
    // keep track of which components have finished
    instructColorComponents = [];
    instructColorComponents.push(confirmSign_click_14);
    instructColorComponents.push(confirmSign_button_14);
    instructColorComponents.push(text_4);
    
    for (const thisComponent of instructColorComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructColorRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructColor' ---
    // get current time
    t = instructColorClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *confirmSign_click_14* updates
    if (t >= 0 && confirmSign_click_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_click_14.tStart = t;  // (not accounting for frame time here)
      confirmSign_click_14.frameNStart = frameN;  // exact frame index
      
      confirmSign_click_14.status = PsychoJS.Status.STARTED;
      confirmSign_click_14.mouseClock.reset();
      prevButtonState = confirmSign_click_14.getPressed();  // if button is down already this ISN'T a new click
      }
    if (confirmSign_click_14.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = confirmSign_click_14.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          confirmSign_click_14.clickableObjects = eval(confirmSign_button_10)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(confirmSign_click_14.clickableObjects)) {
              confirmSign_click_14.clickableObjects = [confirmSign_click_14.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of confirmSign_click_14.clickableObjects) {
              if (obj.contains(confirmSign_click_14)) {
                  gotValidClick = true;
                  confirmSign_click_14.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              confirmSign_click_14.clicked_name.push(null);
          }
          _mouseXYs = confirmSign_click_14.getPos();
          confirmSign_click_14.x.push(_mouseXYs[0]);
          confirmSign_click_14.y.push(_mouseXYs[1]);
          confirmSign_click_14.leftButton.push(_mouseButtons[0]);
          confirmSign_click_14.midButton.push(_mouseButtons[1]);
          confirmSign_click_14.rightButton.push(_mouseButtons[2]);
          confirmSign_click_14.time.push(confirmSign_click_14.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *confirmSign_button_14* updates
    if (t >= 2 && confirmSign_button_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_button_14.tStart = t;  // (not accounting for frame time here)
      confirmSign_button_14.frameNStart = frameN;  // exact frame index
      
      confirmSign_button_14.setAutoDraw(true);
    }
    
    
    // *text_4* updates
    if (t >= 0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructColorComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructColorRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructColor' ---
    for (const thisComponent of instructColorComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instructColor.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('confirmSign_click_14.x', confirmSign_click_14.x);
    psychoJS.experiment.addData('confirmSign_click_14.y', confirmSign_click_14.y);
    psychoJS.experiment.addData('confirmSign_click_14.leftButton', confirmSign_click_14.leftButton);
    psychoJS.experiment.addData('confirmSign_click_14.midButton', confirmSign_click_14.midButton);
    psychoJS.experiment.addData('confirmSign_click_14.rightButton', confirmSign_click_14.rightButton);
    psychoJS.experiment.addData('confirmSign_click_14.time', confirmSign_click_14.time);
    psychoJS.experiment.addData('confirmSign_click_14.clicked_name', confirmSign_click_14.clicked_name);
    
    // the Routine "instructColor" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var loop10_colorblind;
function loop10_colorblindLoopBegin(loop10_colorblindLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop10_colorblind = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 10, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'loop10_colorblind'
    });
    psychoJS.experiment.addLoop(loop10_colorblind); // add the loop to the experiment
    currentLoop = loop10_colorblind;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisLoop10_colorblind of loop10_colorblind) {
      snapshot = loop10_colorblind.getSnapshot();
      loop10_colorblindLoopScheduler.add(importConditions(snapshot));
      loop10_colorblindLoopScheduler.add(RG_colorblindRoutineBegin(snapshot));
      loop10_colorblindLoopScheduler.add(RG_colorblindRoutineEachFrame());
      loop10_colorblindLoopScheduler.add(RG_colorblindRoutineEnd(snapshot));
      loop10_colorblindLoopScheduler.add(loop10_colorblindLoopEndIteration(loop10_colorblindLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function loop10_colorblindLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop10_colorblind);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function loop10_colorblindLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var exp_loop;
function exp_loopLoopBegin(exp_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    exp_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'resources/experimentType.xlsx',
      seed: undefined, name: 'exp_loop'
    });
    psychoJS.experiment.addLoop(exp_loop); // add the loop to the experiment
    currentLoop = exp_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisExp_loop of exp_loop) {
      snapshot = exp_loop.getSnapshot();
      exp_loopLoopScheduler.add(importConditions(snapshot));
      const pracLoopScheduler = new Scheduler(psychoJS);
      exp_loopLoopScheduler.add(pracLoopBegin(pracLoopScheduler, snapshot));
      exp_loopLoopScheduler.add(pracLoopScheduler);
      exp_loopLoopScheduler.add(pracLoopEnd);
      const trial_48LoopScheduler = new Scheduler(psychoJS);
      exp_loopLoopScheduler.add(trial_48LoopBegin(trial_48LoopScheduler, snapshot));
      exp_loopLoopScheduler.add(trial_48LoopScheduler);
      exp_loopLoopScheduler.add(trial_48LoopEnd);
      exp_loopLoopScheduler.add(RestRoutineBegin(snapshot));
      exp_loopLoopScheduler.add(RestRoutineEachFrame());
      exp_loopLoopScheduler.add(RestRoutineEnd(snapshot));
      exp_loopLoopScheduler.add(exp_loopLoopEndIteration(exp_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var prac;
function pracLoopBegin(pracLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    prac = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'resources/pracConditions_4.xlsx',
      seed: undefined, name: 'prac'
    });
    psychoJS.experiment.addLoop(prac); // add the loop to the experiment
    currentLoop = prac;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPrac of prac) {
      snapshot = prac.getSnapshot();
      pracLoopScheduler.add(importConditions(snapshot));
      pracLoopScheduler.add(both_trialsRoutineBegin(snapshot));
      pracLoopScheduler.add(both_trialsRoutineEachFrame());
      pracLoopScheduler.add(both_trialsRoutineEnd(snapshot));
      pracLoopScheduler.add(feedbackRoutineBegin(snapshot));
      pracLoopScheduler.add(feedbackRoutineEachFrame());
      pracLoopScheduler.add(feedbackRoutineEnd(snapshot));
      pracLoopScheduler.add(pracLoopEndIteration(pracLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function pracLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(prac);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function pracLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trial_48;
function trial_48LoopBegin(trial_48LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trial_48 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'resources/trialConditions_48.xlsx',
      seed: undefined, name: 'trial_48'
    });
    psychoJS.experiment.addLoop(trial_48); // add the loop to the experiment
    currentLoop = trial_48;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_48 of trial_48) {
      snapshot = trial_48.getSnapshot();
      trial_48LoopScheduler.add(importConditions(snapshot));
      trial_48LoopScheduler.add(both_trialsRoutineBegin(snapshot));
      trial_48LoopScheduler.add(both_trialsRoutineEachFrame());
      trial_48LoopScheduler.add(both_trialsRoutineEnd(snapshot));
      trial_48LoopScheduler.add(feedbackRoutineBegin(snapshot));
      trial_48LoopScheduler.add(feedbackRoutineEachFrame());
      trial_48LoopScheduler.add(feedbackRoutineEnd(snapshot));
      trial_48LoopScheduler.add(trial_48LoopEndIteration(trial_48LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trial_48LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trial_48);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trial_48LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function exp_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(exp_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function exp_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var RG_colorblindMaxDurationReached;
var GV_xPos;
var RV_xPos;
var jitter_1;
var jitter_2;
var jitter_3;
var jitter_4;
var RG_colorblindMaxDuration;
var RG_colorblindComponents;
function RG_colorblindRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'RG_colorblind' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    RG_colorblindClock.reset();
    routineTimer.reset();
    RG_colorblindMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from exclude_2
    if (consent.rating == "I do not consent to participation or I am younger than 18 years old.") {
        continueRoutine = false;
    }
    
    // Run 'Begin Routine' code from code
    util.shuffle(opposite);
    
    var GV_xPos, RV_xPos;
    GV_xPos = (opposite[0] * 100);
    RV_xPos = (opposite[1] * 100);
    
    var jitter_1, jitter_2, jitter_3, jitter_4;
    
    jitter_1 = Math.floor(Math.random() * 45) - 45;;
    jitter_2 = Math.floor(Math.random() * 45) - 45;;
    jitter_3 = Math.floor(Math.random() * 45) - 45;;
    jitter_4 = Math.floor(Math.random() * 45) - 45;;
    
    green.setOpacity(1.0);
    green.setPos([(GV_xPos + jitter_1), jitter_2]);
    red.setOpacity(1.0);
    red.setPos([(RV_xPos + jitter_3), jitter_4]);
    // setup some python lists for storing info about the mouse
    // current position of the mouse:
    mouse.x = [];
    mouse.y = [];
    mouse.leftButton = [];
    mouse.midButton = [];
    mouse.rightButton = [];
    mouse.time = [];
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from showMouse_2
    document.body.style.cursor='auto';
    psychoJS.experiment.addData('RG_colorblind.started', globalClock.getTime());
    RG_colorblindMaxDuration = null
    // keep track of which components have finished
    RG_colorblindComponents = [];
    RG_colorblindComponents.push(green);
    RG_colorblindComponents.push(red);
    RG_colorblindComponents.push(mouse);
    
    for (const thisComponent of RG_colorblindComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function RG_colorblindRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'RG_colorblind' ---
    // get current time
    t = RG_colorblindClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *green* updates
    if (t >= 1 && green.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      green.tStart = t;  // (not accounting for frame time here)
      green.frameNStart = frameN;  // exact frame index
      
      green.setAutoDraw(true);
    }
    
    
    // *red* updates
    if (t >= 1 && red.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      red.tStart = t;  // (not accounting for frame time here)
      red.frameNStart = frameN;  // exact frame index
      
      red.setAutoDraw(true);
    }
    
    // *mouse* updates
    if (t >= 1 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse.clickableObjects = eval([green, red])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse.clickableObjects)) {
              mouse.clickableObjects = [mouse.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse.clickableObjects) {
              if (obj.contains(mouse)) {
                  gotValidClick = true;
                  mouse.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              mouse.clicked_name.push(null);
          }
          _mouseXYs = mouse.getPos();
          mouse.x.push(_mouseXYs[0]);
          mouse.y.push(_mouseXYs[1]);
          mouse.leftButton.push(_mouseButtons[0]);
          mouse.midButton.push(_mouseButtons[1]);
          mouse.rightButton.push(_mouseButtons[2]);
          mouse.time.push(mouse.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RG_colorblindComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function RG_colorblindRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'RG_colorblind' ---
    for (const thisComponent of RG_colorblindComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('RG_colorblind.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse.x', mouse.x);
    psychoJS.experiment.addData('mouse.y', mouse.y);
    psychoJS.experiment.addData('mouse.leftButton', mouse.leftButton);
    psychoJS.experiment.addData('mouse.midButton', mouse.midButton);
    psychoJS.experiment.addData('mouse.rightButton', mouse.rightButton);
    psychoJS.experiment.addData('mouse.time', mouse.time);
    psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name);
    
    // the Routine "RG_colorblind" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instructTrialMaxDurationReached;
var _Start_allKeys;
var instructTrialMaxDuration;
var instructTrialComponents;
function instructTrialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructTrial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    instructTrialClock.reset();
    routineTimer.reset();
    instructTrialMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from exclude_3
    if (consent.rating == "I do not consent to participation or I am younger than 18 years old.") {
        continueRoutine = false;
    }
    
    Start.keys = undefined;
    Start.rt = undefined;
    _Start_allKeys = [];
    // Run 'Begin Routine' code from hide_mouse_2
    document.body.style.cursor='none';
    psychoJS.experiment.addData('instructTrial.started', globalClock.getTime());
    instructTrialMaxDuration = null
    // keep track of which components have finished
    instructTrialComponents = [];
    instructTrialComponents.push(text);
    instructTrialComponents.push(Start);
    
    for (const thisComponent of instructTrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructTrialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructTrial' ---
    // get current time
    t = instructTrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // *Start* updates
    if (t >= 5 && Start.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Start.tStart = t;  // (not accounting for frame time here)
      Start.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Start.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Start.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Start.clearEvents(); });
    }
    
    if (Start.status === PsychoJS.Status.STARTED) {
      let theseKeys = Start.getKeys({keyList: ['space'], waitRelease: false});
      _Start_allKeys = _Start_allKeys.concat(theseKeys);
      if (_Start_allKeys.length > 0) {
        Start.keys = _Start_allKeys[_Start_allKeys.length - 1].name;  // just the last key pressed
        Start.rt = _Start_allKeys[_Start_allKeys.length - 1].rt;
        Start.duration = _Start_allKeys[_Start_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructTrialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructTrialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructTrial' ---
    for (const thisComponent of instructTrialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instructTrial.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Start.corr, level);
    }
    psychoJS.experiment.addData('Start.keys', Start.keys);
    if (typeof Start.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Start.rt', Start.rt);
        psychoJS.experiment.addData('Start.duration', Start.duration);
        routineTimer.reset();
        }
    
    Start.stop();
    // the Routine "instructTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var both_trialsMaxDurationReached;
var x_pos_Top;
var x_pos_Mid;
var x_pos_Bot;
var y_pos_fix;
var jitter_5;
var jitter_6;
var jitter_7;
var jitter_8;
var jitter_9;
var jitter_10;
var jitter_11;
var jitter_12;
var jitter_13;
var jitter_14;
var jitter_15;
var jitter_16;
var jitter_17;
var jitter_18;
var jitter_19;
var jitter_20;
var jitter_21;
var jitter_22;
var jitter_23;
var jitter_24;
var dist1_pos;
var dist2_pos;
var dist3_pos;
var dist4_pos;
var dist5_pos;
var dist6_pos;
var dist7_pos;
var dist8_pos;
var dist9_pos;
var dist10_pos;
var dist11_pos;
var dist12_pos;
var O_dist1_pos;
var O_dist2_pos;
var O_dist3_pos;
var O_dist4_pos;
var O_dist5_pos;
var O_dist6_pos;
var O_dist7_pos;
var O_dist8_pos;
var O_dist9_pos;
var O_dist10_pos;
var O_dist11_pos;
var O_dist12_pos;
var O_target_pos;
var targetFile;
var FileSet_1;
var FileSet_2;
var size_conj;
var distractors;
var dists_pos;
var dists_pos_jit;
var target_opacity;
var target_present;
var _Response_2_allKeys;
var both_trialsMaxDuration;
var both_trialsComponents;
function both_trialsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'both_trials' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    both_trialsClock.reset(routineTimer.getTime());
    routineTimer.add(4.500000);
    both_trialsMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from exclude_4
    if (consent.rating == "I do not consent to participation or I am younger than 18 years old.") {
        continueRoutine = false;
    }
    
    // Run 'Begin Routine' code from randomize_position_2
    var x_pos_Top, x_pos_Mid, x_pos_Bot, y_pos_fix;
    
    x_pos_Top = [(- 450), (- 150), 150, 450];
    x_pos_Mid = [(- 450), (- 150), 150, 450];
    x_pos_Bot = [(- 450), (- 150), 150, 450];
    y_pos_fix = [(- 300), 0, 300];
    
    if ((setSize === 6)) {
        x_pos_Top = [(- 150), 150];
        x_pos_Mid = [(- 150), 150];
        x_pos_Bot = [(- 150), 150];
        util.shuffle(x_pos_Top);
        util.shuffle(x_pos_Mid);
        util.shuffle(x_pos_Bot);
        for (var x, _pj_c = 0, _pj_a = util.range(2), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
            x = _pj_a[_pj_c];
            x_pos_Top.push(0);
            x_pos_Mid.push(0);
            x_pos_Bot.push(0);
        }
    } else {
        x_pos_Top = [(- 450), (- 150), 150, 450];
        x_pos_Mid = [(- 450), (- 150), 150, 450];
        x_pos_Bot = [(- 450), (- 150), 150, 450];
        util.shuffle(x_pos_Top);
        util.shuffle(x_pos_Mid);
        util.shuffle(x_pos_Bot);
    }
    
    var jitter_1, jitter_2, jitter_3, jitter_4, jitter_5, jitter_6, jitter_7, jitter_8, jitter_9, jitter_10, jitter_11, jitter_12;
    var jitter_13, jitter_14, jitter_15, jitter_16, jitter_17, jitter_18, jitter_19, jitter_20, jitter_21, jitter_22, jitter_23, jitter_24;
    jitter_1 = Math.floor(Math.random() * 45) - 45;
    jitter_2 = Math.floor(Math.random() * 45) - 45;
    jitter_3 = Math.floor(Math.random() * 45) - 45;
    jitter_4 = Math.floor(Math.random() * 45) - 45;
    jitter_5 = Math.floor(Math.random() * 45) - 45;
    jitter_6 = Math.floor(Math.random() * 45) - 45;
    jitter_7 = Math.floor(Math.random() * 45) - 45;
    jitter_8 = Math.floor(Math.random() * 45) - 45;
    jitter_9 = Math.floor(Math.random() * 45) - 45;
    jitter_10 = Math.floor(Math.random() * 45) - 45;
    jitter_11 = Math.floor(Math.random() * 45) - 45;
    jitter_12 = Math.floor(Math.random() * 45) - 45;
    jitter_13 = Math.floor(Math.random() * 45) - 45;
    jitter_14 = Math.floor(Math.random() * 45) - 45;
    jitter_15 = Math.floor(Math.random() * 45) - 45;
    jitter_16 = Math.floor(Math.random() * 45) - 45;
    jitter_17 = Math.floor(Math.random() * 45) - 45;
    jitter_18 = Math.floor(Math.random() * 45) - 45;
    jitter_19 = Math.floor(Math.random() * 45) - 45;
    jitter_20 = Math.floor(Math.random() * 45) - 45;
    jitter_21 = Math.floor(Math.random() * 45) - 45;
    jitter_22 = Math.floor(Math.random() * 45) - 45;
    jitter_23 = Math.floor(Math.random() * 45) - 45;
    jitter_24 = Math.floor(Math.random() * 45) - 45;
    // Run 'Begin Routine' code from position_vars_2
    var dist1_pos, dist2_pos, dist3_pos, dist4_pos, dist5_pos, dist6_pos, dist7_pos, dist8_pos, dist9_pos, dist10_pos, dist11_pos, dist12_pos;
    
    var y_pos_fix;
    y_pos_fix = [(- 300), 0, 300];
    
    dist1_pos = [(x_pos_Top[0] + jitter_1), (y_pos_fix[2] + jitter_2)];
    dist2_pos = [(x_pos_Mid[0] + jitter_3), (y_pos_fix[1] + jitter_4)];
    dist3_pos = [(x_pos_Bot[0] + jitter_5), (y_pos_fix[0] + jitter_6)];
    dist4_pos = [(x_pos_Top[1] + jitter_7), (y_pos_fix[2] + jitter_8)];
    dist5_pos = [(x_pos_Mid[1] + jitter_9), (y_pos_fix[1] + jitter_10)];
    dist6_pos = [(x_pos_Bot[1] + jitter_11), (y_pos_fix[0] + jitter_12)];
    dist7_pos = [(x_pos_Top[2] + jitter_13), (y_pos_fix[2] + jitter_14)];
    dist8_pos = [(x_pos_Mid[2] + jitter_15), (y_pos_fix[1] + jitter_16)];
    dist9_pos = [(x_pos_Bot[2] + jitter_17), (y_pos_fix[0] + jitter_18)];
    dist10_pos = [(x_pos_Top[3] + jitter_19), (y_pos_fix[2] + jitter_20)];
    dist11_pos = [(x_pos_Mid[3] + jitter_21), (y_pos_fix[1] + jitter_22)];
    dist12_pos = [(x_pos_Bot[3] + jitter_23), (y_pos_fix[0] + jitter_24)];
    
    var O_dist1_pos, O_dist2_pos, O_dist3_pos, O_dist4_pos, O_dist5_pos, O_dist6_pos, O_dist7_pos, O_dist8_pos, O_dist9_pos, O_dist10_pos, O_dist11_pos, O_dist12_pos, O_target_pos;
    O_dist1_pos = [x_pos_Top[0], y_pos_fix[2]];
    O_dist2_pos = [x_pos_Mid[0], y_pos_fix[1]];
    O_dist3_pos = [x_pos_Bot[0], y_pos_fix[0]];
    O_dist4_pos = [x_pos_Top[1], y_pos_fix[2]];
    O_dist5_pos = [x_pos_Mid[1], y_pos_fix[1]];
    O_dist6_pos = [x_pos_Bot[1], y_pos_fix[0]];
    O_dist7_pos = [x_pos_Top[2], y_pos_fix[2]];
    O_dist8_pos = [x_pos_Mid[2], y_pos_fix[1]];
    O_dist9_pos = [x_pos_Bot[2], y_pos_fix[0]];
    O_dist10_pos = [x_pos_Top[3], y_pos_fix[2]];
    O_dist11_pos = [x_pos_Mid[3], y_pos_fix[1]];
    O_dist12_pos = [x_pos_Bot[3], y_pos_fix[0]];
    O_target_pos = [targetPos_X, targetPos_Y];
    
    // Run 'Begin Routine' code from img_set
    var targetFile, FileSet_1, FileSet_2, size_conj;
    
    targetFile = 'resources/RV.png';
    FileSet_1 = 'resources/GV.png';
    FileSet_2 = 'resources/GV.png';
    size_conj = [25, 100];
    if (trialver === 1) {
        FileSet_1 = 'resources/RH.png';
        size_conj = [100, 25];
    }
    
    targetRV_2.setOpacity(targetopacity);
    targetRV_2.setPos([0, 0]);
    targetRV_2.setImage(targetFile);
    dist1img_2.setOpacity(opacity_1);
    dist1img_2.setPos(dist1_pos);
    dist1img_2.setSize(size_conj);
    dist1img_2.setImage(FileSet_1);
    dist2img_2.setOpacity(opacity_2);
    dist2img_2.setPos(dist2_pos);
    dist2img_2.setSize(size_conj);
    dist2img_2.setImage(FileSet_1);
    dist3img_2.setOpacity(opacity_3);
    dist3img_2.setPos(dist3_pos);
    dist3img_2.setSize(size_conj);
    dist3img_2.setImage(FileSet_1);
    dist4img_2.setOpacity(opacity_4);
    dist4img_2.setPos(dist4_pos);
    dist4img_2.setSize([25, 100]);
    dist4img_2.setImage(FileSet_2);
    dist5img_2.setOpacity(opacity_5);
    dist5img_2.setPos(dist5_pos);
    dist5img_2.setSize([25, 100]);
    dist5img_2.setImage(FileSet_2);
    dist6img_2.setOpacity(opacity_6);
    dist6img_2.setPos(dist6_pos);
    dist6img_2.setSize([25, 100]);
    dist6img_2.setImage(FileSet_2);
    dist7img_2.setOpacity(opacity_7);
    dist7img_2.setPos(dist7_pos);
    dist7img_2.setSize(size_conj);
    dist7img_2.setImage(FileSet_1);
    dist8img_2.setOpacity(opacity_8);
    dist8img_2.setPos(dist8_pos);
    dist8img_2.setSize(size_conj);
    dist8img_2.setImage(FileSet_1);
    dist9img_2.setOpacity(opacity_9);
    dist9img_2.setPos(dist9_pos);
    dist9img_2.setSize(size_conj);
    dist9img_2.setImage(FileSet_1);
    dist10img_2.setOpacity(opacity_10);
    dist10img_2.setPos(dist10_pos);
    dist10img_2.setSize([25, 100]);
    dist10img_2.setImage(FileSet_2);
    dist11img_2.setOpacity(opacity_11);
    dist11img_2.setPos(dist11_pos);
    dist11img_2.setSize([25, 100]);
    dist11img_2.setImage(FileSet_2);
    dist12img_2.setOpacity(opacity_12);
    dist12img_2.setPos(dist12_pos);
    dist12img_2.setSize([25, 100]);
    dist12img_2.setImage(FileSet_2);
    // Run 'Begin Routine' code from replace_2
    var distractors, dists_pos, dists_pos_jit, target_present, target_opacity;
    
    distractors = [dist1img_2, dist2img_2, dist3img_2, dist4img_2, dist5img_2, dist6img_2, dist7img_2, dist8img_2, dist9img_2, dist10img_2, dist11img_2, dist12img_2];
    dists_pos = [O_dist1_pos, O_dist2_pos, O_dist3_pos, O_dist4_pos, O_dist5_pos, O_dist6_pos, O_dist7_pos, O_dist8_pos, O_dist9_pos, O_dist10_pos, O_dist11_pos, O_dist12_pos];
    dists_pos_jit = [dist1_pos, dist2_pos, dist3_pos, dist4_pos, dist5_pos, dist6_pos, dist7_pos, dist8_pos, dist9_pos, dist10_pos, dist11_pos, dist12_pos];
    if (setSize == 6) {
        distractors = [dist1img_2, dist2img_2, dist3img_2, dist4img_2, dist5img_2, dist6img_2];
        dists_pos = [O_dist1_pos, O_dist2_pos, O_dist3_pos, O_dist4_pos, O_dist5_pos, O_dist6_pos];
        dists_pos_jit = [dist1_pos, dist2_pos, dist3_pos, dist4_pos, dist5_pos, dist6_pos];
    }
    
    target_opacity = targetopacity;
    target_present = false;
    if (target_opacity == 1) {
        target_present = true;
    }
    
    if (target_present) {
        for (let i = 0; i < dists_pos.length; i++) {
            if (dists_pos[i][0] == O_target_pos[0] && dists_pos[i][1] == O_target_pos[1]) {
                distractors[i].setOpacity(0.0);
                targetRV_2.setPos(dists_pos_jit[i]);
                break;
            }
        }
    }
    
    Response_2.keys = undefined;
    Response_2.rt = undefined;
    _Response_2_allKeys = [];
    psychoJS.experiment.addData('both_trials.started', globalClock.getTime());
    both_trialsMaxDuration = null
    // keep track of which components have finished
    both_trialsComponents = [];
    both_trialsComponents.push(fixation_3);
    both_trialsComponents.push(targetRV_2);
    both_trialsComponents.push(dist1img_2);
    both_trialsComponents.push(dist2img_2);
    both_trialsComponents.push(dist3img_2);
    both_trialsComponents.push(dist4img_2);
    both_trialsComponents.push(dist5img_2);
    both_trialsComponents.push(dist6img_2);
    both_trialsComponents.push(dist7img_2);
    both_trialsComponents.push(dist8img_2);
    both_trialsComponents.push(dist9img_2);
    both_trialsComponents.push(dist10img_2);
    both_trialsComponents.push(dist11img_2);
    both_trialsComponents.push(dist12img_2);
    both_trialsComponents.push(Response_2);
    
    for (const thisComponent of both_trialsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function both_trialsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'both_trials' ---
    // get current time
    t = both_trialsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_3* updates
    if (t >= 1 && fixation_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_3.tStart = t;  // (not accounting for frame time here)
      fixation_3.frameNStart = frameN;  // exact frame index
      
      fixation_3.setAutoDraw(true);
    }
    
    frameRemains = 1 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fixation_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_3.setAutoDraw(false);
    }
    
    
    // *targetRV_2* updates
    if (t >= 1.5 && targetRV_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      targetRV_2.tStart = t;  // (not accounting for frame time here)
      targetRV_2.frameNStart = frameN;  // exact frame index
      
      targetRV_2.setAutoDraw(true);
    }
    
    frameRemains = 1.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (targetRV_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      targetRV_2.setAutoDraw(false);
    }
    
    
    // *dist1img_2* updates
    if (t >= 1.5 && dist1img_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dist1img_2.tStart = t;  // (not accounting for frame time here)
      dist1img_2.frameNStart = frameN;  // exact frame index
      
      dist1img_2.setAutoDraw(true);
    }
    
    frameRemains = 1.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (dist1img_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dist1img_2.setAutoDraw(false);
    }
    
    
    // *dist2img_2* updates
    if (t >= 1.5 && dist2img_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dist2img_2.tStart = t;  // (not accounting for frame time here)
      dist2img_2.frameNStart = frameN;  // exact frame index
      
      dist2img_2.setAutoDraw(true);
    }
    
    frameRemains = 1.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (dist2img_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dist2img_2.setAutoDraw(false);
    }
    
    
    // *dist3img_2* updates
    if (t >= 1.5 && dist3img_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dist3img_2.tStart = t;  // (not accounting for frame time here)
      dist3img_2.frameNStart = frameN;  // exact frame index
      
      dist3img_2.setAutoDraw(true);
    }
    
    frameRemains = 1.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (dist3img_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dist3img_2.setAutoDraw(false);
    }
    
    
    // *dist4img_2* updates
    if (t >= 1.5 && dist4img_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dist4img_2.tStart = t;  // (not accounting for frame time here)
      dist4img_2.frameNStart = frameN;  // exact frame index
      
      dist4img_2.setAutoDraw(true);
    }
    
    frameRemains = 1.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (dist4img_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dist4img_2.setAutoDraw(false);
    }
    
    
    // *dist5img_2* updates
    if (t >= 1.5 && dist5img_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dist5img_2.tStart = t;  // (not accounting for frame time here)
      dist5img_2.frameNStart = frameN;  // exact frame index
      
      dist5img_2.setAutoDraw(true);
    }
    
    frameRemains = 1.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (dist5img_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dist5img_2.setAutoDraw(false);
    }
    
    
    // *dist6img_2* updates
    if (t >= 1.5 && dist6img_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dist6img_2.tStart = t;  // (not accounting for frame time here)
      dist6img_2.frameNStart = frameN;  // exact frame index
      
      dist6img_2.setAutoDraw(true);
    }
    
    frameRemains = 1.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (dist6img_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dist6img_2.setAutoDraw(false);
    }
    
    
    // *dist7img_2* updates
    if (t >= 1.5 && dist7img_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dist7img_2.tStart = t;  // (not accounting for frame time here)
      dist7img_2.frameNStart = frameN;  // exact frame index
      
      dist7img_2.setAutoDraw(true);
    }
    
    frameRemains = 1.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (dist7img_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dist7img_2.setAutoDraw(false);
    }
    
    
    // *dist8img_2* updates
    if (t >= 1.5 && dist8img_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dist8img_2.tStart = t;  // (not accounting for frame time here)
      dist8img_2.frameNStart = frameN;  // exact frame index
      
      dist8img_2.setAutoDraw(true);
    }
    
    frameRemains = 1.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (dist8img_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dist8img_2.setAutoDraw(false);
    }
    
    
    // *dist9img_2* updates
    if (t >= 1.5 && dist9img_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dist9img_2.tStart = t;  // (not accounting for frame time here)
      dist9img_2.frameNStart = frameN;  // exact frame index
      
      dist9img_2.setAutoDraw(true);
    }
    
    frameRemains = 1.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (dist9img_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dist9img_2.setAutoDraw(false);
    }
    
    
    // *dist10img_2* updates
    if (t >= 1.5 && dist10img_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dist10img_2.tStart = t;  // (not accounting for frame time here)
      dist10img_2.frameNStart = frameN;  // exact frame index
      
      dist10img_2.setAutoDraw(true);
    }
    
    frameRemains = 1.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (dist10img_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dist10img_2.setAutoDraw(false);
    }
    
    
    // *dist11img_2* updates
    if (t >= 1.5 && dist11img_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dist11img_2.tStart = t;  // (not accounting for frame time here)
      dist11img_2.frameNStart = frameN;  // exact frame index
      
      dist11img_2.setAutoDraw(true);
    }
    
    frameRemains = 1.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (dist11img_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dist11img_2.setAutoDraw(false);
    }
    
    
    // *dist12img_2* updates
    if (t >= 1.5 && dist12img_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dist12img_2.tStart = t;  // (not accounting for frame time here)
      dist12img_2.frameNStart = frameN;  // exact frame index
      
      dist12img_2.setAutoDraw(true);
    }
    
    frameRemains = 1.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (dist12img_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dist12img_2.setAutoDraw(false);
    }
    
    
    // *Response_2* updates
    if (t >= 1.5 && Response_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Response_2.tStart = t;  // (not accounting for frame time here)
      Response_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Response_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Response_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Response_2.clearEvents(); });
    }
    
    frameRemains = 1.5 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (Response_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Response_2.status = PsychoJS.Status.FINISHED;
        }
      
    if (Response_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = Response_2.getKeys({keyList: ['p', 'a'], waitRelease: false});
      _Response_2_allKeys = _Response_2_allKeys.concat(theseKeys);
      if (_Response_2_allKeys.length > 0) {
        Response_2.keys = _Response_2_allKeys[0].name;  // just the first key pressed
        Response_2.rt = _Response_2_allKeys[0].rt;
        Response_2.duration = _Response_2_allKeys[0].duration;
        // was this correct?
        if (Response_2.keys == correctAnswer) {
            Response_2.corr = 1;
        } else {
            Response_2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of both_trialsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function both_trialsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'both_trials' ---
    for (const thisComponent of both_trialsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('both_trials.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (Response_2.keys === undefined) {
      if (['None','none',undefined].includes(correctAnswer)) {
         Response_2.corr = 1;  // correct non-response
      } else {
         Response_2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Response_2.corr, level);
    }
    psychoJS.experiment.addData('Response_2.keys', Response_2.keys);
    psychoJS.experiment.addData('Response_2.corr', Response_2.corr);
    if (typeof Response_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Response_2.rt', Response_2.rt);
        psychoJS.experiment.addData('Response_2.duration', Response_2.duration);
        routineTimer.reset();
        }
    
    Response_2.stop();
    if (both_trialsMaxDurationReached) {
        both_trialsClock.add(both_trialsMaxDuration);
    } else {
        both_trialsClock.add(4.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedbackMaxDurationReached;
var correctness;
var response_time;
var feedbackMaxDuration;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedbackClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    feedbackMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from exclude_5
    if (consent.rating == "I do not consent to participation or I am younger than 18 years old.") {
        continueRoutine = false;
    }
    
    // Run 'Begin Routine' code from feedback_display
    var correctness, response_time;
    
    //if (trialver == 0) {
    //    correctness = Response_E.corr;
    //    response_time = Response_E.rt;
    //}
    //else {
    //    correctness = Response.corr;
    //    response_time = Response.rt;
    //}
    
    correctness = Response_2.corr
    response_time = Response_2.rt
    
    if (correctness == 1) {
        continueRoutine = false;
    }
    
    if (response_time == null) {
        fd.setText("Too Slow");
    } else {
        fd.setText("Incorrect");
    }
    
    psychoJS.experiment.addData('feedback.started', globalClock.getTime());
    feedbackMaxDuration = null
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(fd);
    
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback' ---
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fd* updates
    if (t >= 0 && fd.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fd.tStart = t;  // (not accounting for frame time here)
      fd.frameNStart = frameN;  // exact frame index
      
      fd.setAutoDraw(true);
    }
    
    frameRemains = 0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fd.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fd.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback' ---
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('feedback.stopped', globalClock.getTime());
    if (feedbackMaxDurationReached) {
        feedbackClock.add(feedbackMaxDuration);
    } else {
        feedbackClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var RestMaxDurationReached;
var RestMaxDuration;
var RestComponents;
function RestRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Rest' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    RestClock.reset(routineTimer.getTime());
    routineTimer.add(30.000000);
    RestMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from exclude_6
    if (consent.rating == "I do not consent to participation or I am younger than 18 years old.") {
        continueRoutine = false;
    }
    
    // Run 'Begin Routine' code from code_4
    if ((exp_loop.thisN === 1)) {
        continueRoutine = false;
    }
    
    psychoJS.experiment.addData('Rest.started', globalClock.getTime());
    RestMaxDuration = null
    // keep track of which components have finished
    RestComponents = [];
    RestComponents.push(RestText);
    
    for (const thisComponent of RestComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function RestRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Rest' ---
    // get current time
    t = RestClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *RestText* updates
    if (t >= 0.0 && RestText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RestText.tStart = t;  // (not accounting for frame time here)
      RestText.frameNStart = frameN;  // exact frame index
      
      RestText.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (RestText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      RestText.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RestComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function RestRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Rest' ---
    for (const thisComponent of RestComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Rest.stopped', globalClock.getTime());
    if (RestMaxDurationReached) {
        RestClock.add(RestMaxDuration);
    } else {
        RestClock.add(30.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var PreMEQMaxDurationReached;
var PreMEQMaxDuration;
var PreMEQComponents;
function PreMEQRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'PreMEQ' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    PreMEQClock.reset();
    routineTimer.reset();
    PreMEQMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from exclude_7
    if (consent.rating == "I do not consent to participation or I am younger than 18 years old.") {
        continueRoutine = false;
    }
    
    // setup some python lists for storing info about the confirmSign_click_3
    // current position of the mouse:
    confirmSign_click_3.x = [];
    confirmSign_click_3.y = [];
    confirmSign_click_3.leftButton = [];
    confirmSign_click_3.midButton = [];
    confirmSign_click_3.rightButton = [];
    confirmSign_click_3.time = [];
    confirmSign_click_3.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from showMouse_3
    document.body.style.cursor='auto';
    psychoJS.experiment.addData('PreMEQ.started', globalClock.getTime());
    PreMEQMaxDuration = null
    // keep track of which components have finished
    PreMEQComponents = [];
    PreMEQComponents.push(form);
    PreMEQComponents.push(confirmSign_button_3);
    PreMEQComponents.push(confirmSign_click_3);
    
    for (const thisComponent of PreMEQComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function PreMEQRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'PreMEQ' ---
    // get current time
    t = PreMEQClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *form* updates
    if (t >= 0 && form.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      form.tStart = t;  // (not accounting for frame time here)
      form.frameNStart = frameN;  // exact frame index
      
      form.setAutoDraw(true);
    }
    
    
    // *confirmSign_button_3* updates
    if (t >= 1.5 && confirmSign_button_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_button_3.tStart = t;  // (not accounting for frame time here)
      confirmSign_button_3.frameNStart = frameN;  // exact frame index
      
      confirmSign_button_3.setAutoDraw(true);
    }
    
    // *confirmSign_click_3* updates
    if (t >= 0 && confirmSign_click_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_click_3.tStart = t;  // (not accounting for frame time here)
      confirmSign_click_3.frameNStart = frameN;  // exact frame index
      
      confirmSign_click_3.status = PsychoJS.Status.STARTED;
      confirmSign_click_3.mouseClock.reset();
      prevButtonState = confirmSign_click_3.getPressed();  // if button is down already this ISN'T a new click
      }
    if (confirmSign_click_3.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = confirmSign_click_3.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          confirmSign_click_3.clickableObjects = eval(confirmSign_button_3)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(confirmSign_click_3.clickableObjects)) {
              confirmSign_click_3.clickableObjects = [confirmSign_click_3.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of confirmSign_click_3.clickableObjects) {
              if (obj.contains(confirmSign_click_3)) {
                  gotValidClick = true;
                  confirmSign_click_3.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              confirmSign_click_3.clicked_name.push(null);
          }
          _mouseXYs = confirmSign_click_3.getPos();
          confirmSign_click_3.x.push(_mouseXYs[0]);
          confirmSign_click_3.y.push(_mouseXYs[1]);
          confirmSign_click_3.leftButton.push(_mouseButtons[0]);
          confirmSign_click_3.midButton.push(_mouseButtons[1]);
          confirmSign_click_3.rightButton.push(_mouseButtons[2]);
          confirmSign_click_3.time.push(confirmSign_click_3.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PreMEQComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PreMEQRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'PreMEQ' ---
    for (const thisComponent of PreMEQComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('PreMEQ.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('confirmSign_click_3.x', confirmSign_click_3.x);
    psychoJS.experiment.addData('confirmSign_click_3.y', confirmSign_click_3.y);
    psychoJS.experiment.addData('confirmSign_click_3.leftButton', confirmSign_click_3.leftButton);
    psychoJS.experiment.addData('confirmSign_click_3.midButton', confirmSign_click_3.midButton);
    psychoJS.experiment.addData('confirmSign_click_3.rightButton', confirmSign_click_3.rightButton);
    psychoJS.experiment.addData('confirmSign_click_3.time', confirmSign_click_3.time);
    psychoJS.experiment.addData('confirmSign_click_3.clicked_name', confirmSign_click_3.clicked_name);
    
    // the Routine "PreMEQ" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var bestfeel_meqMaxDurationReached;
var bestfeel_meqMaxDuration;
var bestfeel_meqComponents;
function bestfeel_meqRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'bestfeel_meq' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    bestfeel_meqClock.reset();
    routineTimer.reset();
    bestfeel_meqMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from exclude_8
    if (consent.rating == "I do not consent to participation or I am younger than 18 years old.") {
        continueRoutine = false;
    }
    
    // setup some python lists for storing info about the confirmSign_click_4
    // current position of the mouse:
    confirmSign_click_4.x = [];
    confirmSign_click_4.y = [];
    confirmSign_click_4.leftButton = [];
    confirmSign_click_4.midButton = [];
    confirmSign_click_4.rightButton = [];
    confirmSign_click_4.time = [];
    confirmSign_click_4.clicked_name = [];
    gotValidClick = false; // until a click is received
    best_feel.reset()
    // Run 'Begin Routine' code from showMouse_4
    document.body.style.cursor='auto';
    psychoJS.experiment.addData('bestfeel_meq.started', globalClock.getTime());
    bestfeel_meqMaxDuration = null
    // keep track of which components have finished
    bestfeel_meqComponents = [];
    bestfeel_meqComponents.push(confirmSign_click_4);
    bestfeel_meqComponents.push(confirmSign_button_4);
    bestfeel_meqComponents.push(best_feel_Q);
    bestfeel_meqComponents.push(best_feel);
    
    for (const thisComponent of bestfeel_meqComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function bestfeel_meqRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'bestfeel_meq' ---
    // get current time
    t = bestfeel_meqClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *confirmSign_click_4* updates
    if (t >= 0 && confirmSign_click_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_click_4.tStart = t;  // (not accounting for frame time here)
      confirmSign_click_4.frameNStart = frameN;  // exact frame index
      
      confirmSign_click_4.status = PsychoJS.Status.STARTED;
      confirmSign_click_4.mouseClock.reset();
      prevButtonState = confirmSign_click_4.getPressed();  // if button is down already this ISN'T a new click
      }
    if (confirmSign_click_4.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = confirmSign_click_4.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          confirmSign_click_4.clickableObjects = eval(confirmSign_button_4)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(confirmSign_click_4.clickableObjects)) {
              confirmSign_click_4.clickableObjects = [confirmSign_click_4.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of confirmSign_click_4.clickableObjects) {
              if (obj.contains(confirmSign_click_4)) {
                  gotValidClick = true;
                  confirmSign_click_4.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              confirmSign_click_4.clicked_name.push(null);
          }
          _mouseXYs = confirmSign_click_4.getPos();
          confirmSign_click_4.x.push(_mouseXYs[0]);
          confirmSign_click_4.y.push(_mouseXYs[1]);
          confirmSign_click_4.leftButton.push(_mouseButtons[0]);
          confirmSign_click_4.midButton.push(_mouseButtons[1]);
          confirmSign_click_4.rightButton.push(_mouseButtons[2]);
          confirmSign_click_4.time.push(confirmSign_click_4.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *confirmSign_button_4* updates
    if ((best_feel.rating) && confirmSign_button_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_button_4.tStart = t;  // (not accounting for frame time here)
      confirmSign_button_4.frameNStart = frameN;  // exact frame index
      
      confirmSign_button_4.setAutoDraw(true);
    }
    
    
    // *best_feel_Q* updates
    if (t >= 0.0 && best_feel_Q.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      best_feel_Q.tStart = t;  // (not accounting for frame time here)
      best_feel_Q.frameNStart = frameN;  // exact frame index
      
      best_feel_Q.setAutoDraw(true);
    }
    
    
    // *best_feel* updates
    if (t >= 0 && best_feel.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      best_feel.tStart = t;  // (not accounting for frame time here)
      best_feel.frameNStart = frameN;  // exact frame index
      
      best_feel.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of bestfeel_meqComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function bestfeel_meqRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'bestfeel_meq' ---
    for (const thisComponent of bestfeel_meqComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('bestfeel_meq.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('confirmSign_click_4.x', confirmSign_click_4.x);
    psychoJS.experiment.addData('confirmSign_click_4.y', confirmSign_click_4.y);
    psychoJS.experiment.addData('confirmSign_click_4.leftButton', confirmSign_click_4.leftButton);
    psychoJS.experiment.addData('confirmSign_click_4.midButton', confirmSign_click_4.midButton);
    psychoJS.experiment.addData('confirmSign_click_4.rightButton', confirmSign_click_4.rightButton);
    psychoJS.experiment.addData('confirmSign_click_4.time', confirmSign_click_4.time);
    psychoJS.experiment.addData('confirmSign_click_4.clicked_name', confirmSign_click_4.clicked_name);
    
    psychoJS.experiment.addData('best_feel.response', best_feel.getRating());
    psychoJS.experiment.addData('best_feel.rt', best_feel.getRT());
    // the Routine "bestfeel_meq" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var wokentired_meqMaxDurationReached;
var wokentired_meqMaxDuration;
var wokentired_meqComponents;
function wokentired_meqRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'wokentired_meq' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    wokentired_meqClock.reset();
    routineTimer.reset();
    wokentired_meqMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from exclude_9
    if (consent.rating == "I do not consent to participation or I am younger than 18 years old.") {
        continueRoutine = false;
    }
    
    // setup some python lists for storing info about the confirmSign_click_6
    // current position of the mouse:
    confirmSign_click_6.x = [];
    confirmSign_click_6.y = [];
    confirmSign_click_6.leftButton = [];
    confirmSign_click_6.midButton = [];
    confirmSign_click_6.rightButton = [];
    confirmSign_click_6.time = [];
    confirmSign_click_6.clicked_name = [];
    gotValidClick = false; // until a click is received
    woken_tired.reset()
    psychoJS.experiment.addData('wokentired_meq.started', globalClock.getTime());
    wokentired_meqMaxDuration = null
    // keep track of which components have finished
    wokentired_meqComponents = [];
    wokentired_meqComponents.push(confirmSign_click_6);
    wokentired_meqComponents.push(confirmSign_button_6);
    wokentired_meqComponents.push(woken_tired_Q);
    wokentired_meqComponents.push(woken_tired);
    
    for (const thisComponent of wokentired_meqComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function wokentired_meqRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'wokentired_meq' ---
    // get current time
    t = wokentired_meqClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *confirmSign_click_6* updates
    if (t >= 0 && confirmSign_click_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_click_6.tStart = t;  // (not accounting for frame time here)
      confirmSign_click_6.frameNStart = frameN;  // exact frame index
      
      confirmSign_click_6.status = PsychoJS.Status.STARTED;
      confirmSign_click_6.mouseClock.reset();
      prevButtonState = confirmSign_click_6.getPressed();  // if button is down already this ISN'T a new click
      }
    if (confirmSign_click_6.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = confirmSign_click_6.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          confirmSign_click_6.clickableObjects = eval(confirmSign_button_6)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(confirmSign_click_6.clickableObjects)) {
              confirmSign_click_6.clickableObjects = [confirmSign_click_6.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of confirmSign_click_6.clickableObjects) {
              if (obj.contains(confirmSign_click_6)) {
                  gotValidClick = true;
                  confirmSign_click_6.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              confirmSign_click_6.clicked_name.push(null);
          }
          _mouseXYs = confirmSign_click_6.getPos();
          confirmSign_click_6.x.push(_mouseXYs[0]);
          confirmSign_click_6.y.push(_mouseXYs[1]);
          confirmSign_click_6.leftButton.push(_mouseButtons[0]);
          confirmSign_click_6.midButton.push(_mouseButtons[1]);
          confirmSign_click_6.rightButton.push(_mouseButtons[2]);
          confirmSign_click_6.time.push(confirmSign_click_6.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *confirmSign_button_6* updates
    if ((woken_tired.rating) && confirmSign_button_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_button_6.tStart = t;  // (not accounting for frame time here)
      confirmSign_button_6.frameNStart = frameN;  // exact frame index
      
      confirmSign_button_6.setAutoDraw(true);
    }
    
    
    // *woken_tired_Q* updates
    if (t >= 0.0 && woken_tired_Q.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      woken_tired_Q.tStart = t;  // (not accounting for frame time here)
      woken_tired_Q.frameNStart = frameN;  // exact frame index
      
      woken_tired_Q.setAutoDraw(true);
    }
    
    
    // *woken_tired* updates
    if (t >= 0 && woken_tired.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      woken_tired.tStart = t;  // (not accounting for frame time here)
      woken_tired.frameNStart = frameN;  // exact frame index
      
      woken_tired.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of wokentired_meqComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function wokentired_meqRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'wokentired_meq' ---
    for (const thisComponent of wokentired_meqComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('wokentired_meq.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('confirmSign_click_6.x', confirmSign_click_6.x);
    psychoJS.experiment.addData('confirmSign_click_6.y', confirmSign_click_6.y);
    psychoJS.experiment.addData('confirmSign_click_6.leftButton', confirmSign_click_6.leftButton);
    psychoJS.experiment.addData('confirmSign_click_6.midButton', confirmSign_click_6.midButton);
    psychoJS.experiment.addData('confirmSign_click_6.rightButton', confirmSign_click_6.rightButton);
    psychoJS.experiment.addData('confirmSign_click_6.time', confirmSign_click_6.time);
    psychoJS.experiment.addData('confirmSign_click_6.clicked_name', confirmSign_click_6.clicked_name);
    
    psychoJS.experiment.addData('woken_tired.response', woken_tired.getRating());
    psychoJS.experiment.addData('woken_tired.rt', woken_tired.getRT());
    // the Routine "wokentired_meq" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var sleepytime_meqMaxDurationReached;
var sleepytime_meqMaxDuration;
var sleepytime_meqComponents;
function sleepytime_meqRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'sleepytime_meq' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    sleepytime_meqClock.reset();
    routineTimer.reset();
    sleepytime_meqMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from exclude_10
    if (consent.rating == "I do not consent to participation or I am younger than 18 years old.") {
        continueRoutine = false;
    }
    
    // setup some python lists for storing info about the confirmSign_click_7
    // current position of the mouse:
    confirmSign_click_7.x = [];
    confirmSign_click_7.y = [];
    confirmSign_click_7.leftButton = [];
    confirmSign_click_7.midButton = [];
    confirmSign_click_7.rightButton = [];
    confirmSign_click_7.time = [];
    confirmSign_click_7.clicked_name = [];
    gotValidClick = false; // until a click is received
    sleepy_time.reset()
    psychoJS.experiment.addData('sleepytime_meq.started', globalClock.getTime());
    sleepytime_meqMaxDuration = null
    // keep track of which components have finished
    sleepytime_meqComponents = [];
    sleepytime_meqComponents.push(confirmSign_click_7);
    sleepytime_meqComponents.push(confirmSign_button_7);
    sleepytime_meqComponents.push(sleepy_time_Q);
    sleepytime_meqComponents.push(sleepy_time);
    
    for (const thisComponent of sleepytime_meqComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function sleepytime_meqRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'sleepytime_meq' ---
    // get current time
    t = sleepytime_meqClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *confirmSign_click_7* updates
    if (t >= 0 && confirmSign_click_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_click_7.tStart = t;  // (not accounting for frame time here)
      confirmSign_click_7.frameNStart = frameN;  // exact frame index
      
      confirmSign_click_7.status = PsychoJS.Status.STARTED;
      confirmSign_click_7.mouseClock.reset();
      prevButtonState = confirmSign_click_7.getPressed();  // if button is down already this ISN'T a new click
      }
    if (confirmSign_click_7.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = confirmSign_click_7.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          confirmSign_click_7.clickableObjects = eval(confirmSign_button_7)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(confirmSign_click_7.clickableObjects)) {
              confirmSign_click_7.clickableObjects = [confirmSign_click_7.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of confirmSign_click_7.clickableObjects) {
              if (obj.contains(confirmSign_click_7)) {
                  gotValidClick = true;
                  confirmSign_click_7.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              confirmSign_click_7.clicked_name.push(null);
          }
          _mouseXYs = confirmSign_click_7.getPos();
          confirmSign_click_7.x.push(_mouseXYs[0]);
          confirmSign_click_7.y.push(_mouseXYs[1]);
          confirmSign_click_7.leftButton.push(_mouseButtons[0]);
          confirmSign_click_7.midButton.push(_mouseButtons[1]);
          confirmSign_click_7.rightButton.push(_mouseButtons[2]);
          confirmSign_click_7.time.push(confirmSign_click_7.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *confirmSign_button_7* updates
    if ((sleepy_time.rating) && confirmSign_button_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_button_7.tStart = t;  // (not accounting for frame time here)
      confirmSign_button_7.frameNStart = frameN;  // exact frame index
      
      confirmSign_button_7.setAutoDraw(true);
    }
    
    
    // *sleepy_time_Q* updates
    if (t >= 0.0 && sleepy_time_Q.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sleepy_time_Q.tStart = t;  // (not accounting for frame time here)
      sleepy_time_Q.frameNStart = frameN;  // exact frame index
      
      sleepy_time_Q.setAutoDraw(true);
    }
    
    
    // *sleepy_time* updates
    if (t >= 0 && sleepy_time.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sleepy_time.tStart = t;  // (not accounting for frame time here)
      sleepy_time.frameNStart = frameN;  // exact frame index
      
      sleepy_time.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of sleepytime_meqComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function sleepytime_meqRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'sleepytime_meq' ---
    for (const thisComponent of sleepytime_meqComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('sleepytime_meq.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('confirmSign_click_7.x', confirmSign_click_7.x);
    psychoJS.experiment.addData('confirmSign_click_7.y', confirmSign_click_7.y);
    psychoJS.experiment.addData('confirmSign_click_7.leftButton', confirmSign_click_7.leftButton);
    psychoJS.experiment.addData('confirmSign_click_7.midButton', confirmSign_click_7.midButton);
    psychoJS.experiment.addData('confirmSign_click_7.rightButton', confirmSign_click_7.rightButton);
    psychoJS.experiment.addData('confirmSign_click_7.time', confirmSign_click_7.time);
    psychoJS.experiment.addData('confirmSign_click_7.clicked_name', confirmSign_click_7.clicked_name);
    
    psychoJS.experiment.addData('sleepy_time.response', sleepy_time.getRating());
    psychoJS.experiment.addData('sleepy_time.rt', sleepy_time.getRT());
    // the Routine "sleepytime_meq" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var bestpeak_meqMaxDurationReached;
var bestpeak_meqMaxDuration;
var bestpeak_meqComponents;
function bestpeak_meqRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'bestpeak_meq' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    bestpeak_meqClock.reset();
    routineTimer.reset();
    bestpeak_meqMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from exclude_11
    if (consent.rating == "I do not consent to participation or I am younger than 18 years old.") {
        continueRoutine = false;
    }
    
    // setup some python lists for storing info about the confirmSign_click_8
    // current position of the mouse:
    confirmSign_click_8.x = [];
    confirmSign_click_8.y = [];
    confirmSign_click_8.leftButton = [];
    confirmSign_click_8.midButton = [];
    confirmSign_click_8.rightButton = [];
    confirmSign_click_8.time = [];
    confirmSign_click_8.clicked_name = [];
    gotValidClick = false; // until a click is received
    best_peak.reset()
    psychoJS.experiment.addData('bestpeak_meq.started', globalClock.getTime());
    bestpeak_meqMaxDuration = null
    // keep track of which components have finished
    bestpeak_meqComponents = [];
    bestpeak_meqComponents.push(confirmSign_click_8);
    bestpeak_meqComponents.push(confirmSign_button_8);
    bestpeak_meqComponents.push(best_peak_Q);
    bestpeak_meqComponents.push(best_peak);
    
    for (const thisComponent of bestpeak_meqComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function bestpeak_meqRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'bestpeak_meq' ---
    // get current time
    t = bestpeak_meqClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *confirmSign_click_8* updates
    if (t >= 0 && confirmSign_click_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_click_8.tStart = t;  // (not accounting for frame time here)
      confirmSign_click_8.frameNStart = frameN;  // exact frame index
      
      confirmSign_click_8.status = PsychoJS.Status.STARTED;
      confirmSign_click_8.mouseClock.reset();
      prevButtonState = confirmSign_click_8.getPressed();  // if button is down already this ISN'T a new click
      }
    if (confirmSign_click_8.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = confirmSign_click_8.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          confirmSign_click_8.clickableObjects = eval(confirmSign_button_8)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(confirmSign_click_8.clickableObjects)) {
              confirmSign_click_8.clickableObjects = [confirmSign_click_8.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of confirmSign_click_8.clickableObjects) {
              if (obj.contains(confirmSign_click_8)) {
                  gotValidClick = true;
                  confirmSign_click_8.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              confirmSign_click_8.clicked_name.push(null);
          }
          _mouseXYs = confirmSign_click_8.getPos();
          confirmSign_click_8.x.push(_mouseXYs[0]);
          confirmSign_click_8.y.push(_mouseXYs[1]);
          confirmSign_click_8.leftButton.push(_mouseButtons[0]);
          confirmSign_click_8.midButton.push(_mouseButtons[1]);
          confirmSign_click_8.rightButton.push(_mouseButtons[2]);
          confirmSign_click_8.time.push(confirmSign_click_8.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *confirmSign_button_8* updates
    if ((best_peak.rating) && confirmSign_button_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_button_8.tStart = t;  // (not accounting for frame time here)
      confirmSign_button_8.frameNStart = frameN;  // exact frame index
      
      confirmSign_button_8.setAutoDraw(true);
    }
    
    
    // *best_peak_Q* updates
    if (t >= 0.0 && best_peak_Q.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      best_peak_Q.tStart = t;  // (not accounting for frame time here)
      best_peak_Q.frameNStart = frameN;  // exact frame index
      
      best_peak_Q.setAutoDraw(true);
    }
    
    
    // *best_peak* updates
    if (t >= 0 && best_peak.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      best_peak.tStart = t;  // (not accounting for frame time here)
      best_peak.frameNStart = frameN;  // exact frame index
      
      best_peak.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of bestpeak_meqComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function bestpeak_meqRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'bestpeak_meq' ---
    for (const thisComponent of bestpeak_meqComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('bestpeak_meq.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('confirmSign_click_8.x', confirmSign_click_8.x);
    psychoJS.experiment.addData('confirmSign_click_8.y', confirmSign_click_8.y);
    psychoJS.experiment.addData('confirmSign_click_8.leftButton', confirmSign_click_8.leftButton);
    psychoJS.experiment.addData('confirmSign_click_8.midButton', confirmSign_click_8.midButton);
    psychoJS.experiment.addData('confirmSign_click_8.rightButton', confirmSign_click_8.rightButton);
    psychoJS.experiment.addData('confirmSign_click_8.time', confirmSign_click_8.time);
    psychoJS.experiment.addData('confirmSign_click_8.clicked_name', confirmSign_click_8.clicked_name);
    
    psychoJS.experiment.addData('best_peak.response', best_peak.getRating());
    psychoJS.experiment.addData('best_peak.rt', best_peak.getRT());
    // the Routine "bestpeak_meq" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var persontype_meqMaxDurationReached;
var persontype_meqMaxDuration;
var persontype_meqComponents;
function persontype_meqRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'persontype_meq' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    persontype_meqClock.reset();
    routineTimer.reset();
    persontype_meqMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from exclude_12
    if (consent.rating == "I do not consent to participation or I am younger than 18 years old.") {
        continueRoutine = false;
    }
    
    // setup some python lists for storing info about the confirmSign_click_9
    // current position of the mouse:
    confirmSign_click_9.x = [];
    confirmSign_click_9.y = [];
    confirmSign_click_9.leftButton = [];
    confirmSign_click_9.midButton = [];
    confirmSign_click_9.rightButton = [];
    confirmSign_click_9.time = [];
    confirmSign_click_9.clicked_name = [];
    gotValidClick = false; // until a click is received
    person_type.reset()
    psychoJS.experiment.addData('persontype_meq.started', globalClock.getTime());
    persontype_meqMaxDuration = null
    // keep track of which components have finished
    persontype_meqComponents = [];
    persontype_meqComponents.push(confirmSign_click_9);
    persontype_meqComponents.push(confirmSign_button_9);
    persontype_meqComponents.push(person_type_Q);
    persontype_meqComponents.push(person_type);
    
    for (const thisComponent of persontype_meqComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function persontype_meqRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'persontype_meq' ---
    // get current time
    t = persontype_meqClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *confirmSign_click_9* updates
    if (t >= 0 && confirmSign_click_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_click_9.tStart = t;  // (not accounting for frame time here)
      confirmSign_click_9.frameNStart = frameN;  // exact frame index
      
      confirmSign_click_9.status = PsychoJS.Status.STARTED;
      confirmSign_click_9.mouseClock.reset();
      prevButtonState = confirmSign_click_9.getPressed();  // if button is down already this ISN'T a new click
      }
    if (confirmSign_click_9.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = confirmSign_click_9.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          confirmSign_click_9.clickableObjects = eval(confirmSign_button_9)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(confirmSign_click_9.clickableObjects)) {
              confirmSign_click_9.clickableObjects = [confirmSign_click_9.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of confirmSign_click_9.clickableObjects) {
              if (obj.contains(confirmSign_click_9)) {
                  gotValidClick = true;
                  confirmSign_click_9.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              confirmSign_click_9.clicked_name.push(null);
          }
          _mouseXYs = confirmSign_click_9.getPos();
          confirmSign_click_9.x.push(_mouseXYs[0]);
          confirmSign_click_9.y.push(_mouseXYs[1]);
          confirmSign_click_9.leftButton.push(_mouseButtons[0]);
          confirmSign_click_9.midButton.push(_mouseButtons[1]);
          confirmSign_click_9.rightButton.push(_mouseButtons[2]);
          confirmSign_click_9.time.push(confirmSign_click_9.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *confirmSign_button_9* updates
    if ((person_type.rating) && confirmSign_button_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_button_9.tStart = t;  // (not accounting for frame time here)
      confirmSign_button_9.frameNStart = frameN;  // exact frame index
      
      confirmSign_button_9.setAutoDraw(true);
    }
    
    
    // *person_type_Q* updates
    if (t >= 0.0 && person_type_Q.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      person_type_Q.tStart = t;  // (not accounting for frame time here)
      person_type_Q.frameNStart = frameN;  // exact frame index
      
      person_type_Q.setAutoDraw(true);
    }
    
    
    // *person_type* updates
    if (t >= 0 && person_type.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      person_type.tStart = t;  // (not accounting for frame time here)
      person_type.frameNStart = frameN;  // exact frame index
      
      person_type.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of persontype_meqComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function persontype_meqRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'persontype_meq' ---
    for (const thisComponent of persontype_meqComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('persontype_meq.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('confirmSign_click_9.x', confirmSign_click_9.x);
    psychoJS.experiment.addData('confirmSign_click_9.y', confirmSign_click_9.y);
    psychoJS.experiment.addData('confirmSign_click_9.leftButton', confirmSign_click_9.leftButton);
    psychoJS.experiment.addData('confirmSign_click_9.midButton', confirmSign_click_9.midButton);
    psychoJS.experiment.addData('confirmSign_click_9.rightButton', confirmSign_click_9.rightButton);
    psychoJS.experiment.addData('confirmSign_click_9.time', confirmSign_click_9.time);
    psychoJS.experiment.addData('confirmSign_click_9.clicked_name', confirmSign_click_9.clicked_name);
    
    psychoJS.experiment.addData('person_type.response', person_type.getRating());
    psychoJS.experiment.addData('person_type.rt', person_type.getRT());
    // the Routine "persontype_meq" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var what_ageMaxDurationReached;
var what_ageMaxDuration;
var what_ageComponents;
function what_ageRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'what_age' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    what_ageClock.reset();
    routineTimer.reset();
    what_ageMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from exclude_13
    if (consent.rating == "I do not consent to participation or I am younger than 18 years old.") {
        continueRoutine = false;
    }
    
    // setup some python lists for storing info about the confirmSign_click_10
    // current position of the mouse:
    confirmSign_click_10.x = [];
    confirmSign_click_10.y = [];
    confirmSign_click_10.leftButton = [];
    confirmSign_click_10.midButton = [];
    confirmSign_click_10.rightButton = [];
    confirmSign_click_10.time = [];
    confirmSign_click_10.clicked_name = [];
    gotValidClick = false; // until a click is received
    age_Q.setText('');
    age_Q.refresh();
    psychoJS.experiment.addData('what_age.started', globalClock.getTime());
    what_ageMaxDuration = null
    // keep track of which components have finished
    what_ageComponents = [];
    what_ageComponents.push(confirmSign_click_10);
    what_ageComponents.push(confirmSign_button_10);
    what_ageComponents.push(age_fill_Q);
    what_ageComponents.push(age_Q);
    
    for (const thisComponent of what_ageComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function what_ageRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'what_age' ---
    // get current time
    t = what_ageClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *confirmSign_click_10* updates
    if (t >= 0 && confirmSign_click_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_click_10.tStart = t;  // (not accounting for frame time here)
      confirmSign_click_10.frameNStart = frameN;  // exact frame index
      
      confirmSign_click_10.status = PsychoJS.Status.STARTED;
      confirmSign_click_10.mouseClock.reset();
      prevButtonState = confirmSign_click_10.getPressed();  // if button is down already this ISN'T a new click
      }
    if (confirmSign_click_10.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = confirmSign_click_10.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          confirmSign_click_10.clickableObjects = eval(confirmSign_button_10)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(confirmSign_click_10.clickableObjects)) {
              confirmSign_click_10.clickableObjects = [confirmSign_click_10.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of confirmSign_click_10.clickableObjects) {
              if (obj.contains(confirmSign_click_10)) {
                  gotValidClick = true;
                  confirmSign_click_10.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              confirmSign_click_10.clicked_name.push(null);
          }
          _mouseXYs = confirmSign_click_10.getPos();
          confirmSign_click_10.x.push(_mouseXYs[0]);
          confirmSign_click_10.y.push(_mouseXYs[1]);
          confirmSign_click_10.leftButton.push(_mouseButtons[0]);
          confirmSign_click_10.midButton.push(_mouseButtons[1]);
          confirmSign_click_10.rightButton.push(_mouseButtons[2]);
          confirmSign_click_10.time.push(confirmSign_click_10.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *confirmSign_button_10* updates
    if (t >= 2 && confirmSign_button_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_button_10.tStart = t;  // (not accounting for frame time here)
      confirmSign_button_10.frameNStart = frameN;  // exact frame index
      
      confirmSign_button_10.setAutoDraw(true);
    }
    
    
    // *age_fill_Q* updates
    if (t >= 0.0 && age_fill_Q.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      age_fill_Q.tStart = t;  // (not accounting for frame time here)
      age_fill_Q.frameNStart = frameN;  // exact frame index
      
      age_fill_Q.setAutoDraw(true);
    }
    
    
    // *age_Q* updates
    if (t >= 0.0 && age_Q.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      age_Q.tStart = t;  // (not accounting for frame time here)
      age_Q.frameNStart = frameN;  // exact frame index
      
      age_Q.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of what_ageComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function what_ageRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'what_age' ---
    for (const thisComponent of what_ageComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('what_age.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('confirmSign_click_10.x', confirmSign_click_10.x);
    psychoJS.experiment.addData('confirmSign_click_10.y', confirmSign_click_10.y);
    psychoJS.experiment.addData('confirmSign_click_10.leftButton', confirmSign_click_10.leftButton);
    psychoJS.experiment.addData('confirmSign_click_10.midButton', confirmSign_click_10.midButton);
    psychoJS.experiment.addData('confirmSign_click_10.rightButton', confirmSign_click_10.rightButton);
    psychoJS.experiment.addData('confirmSign_click_10.time', confirmSign_click_10.time);
    psychoJS.experiment.addData('confirmSign_click_10.clicked_name', confirmSign_click_10.clicked_name);
    
    psychoJS.experiment.addData('age_Q.text',age_Q.text)
    // the Routine "what_age" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var genderMaxDurationReached;
var genderMaxDuration;
var genderComponents;
function genderRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'gender' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    genderClock.reset();
    routineTimer.reset();
    genderMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from exclude_14
    if (consent.rating == "I do not consent to participation or I am younger than 18 years old.") {
        continueRoutine = false;
    }
    
    // setup some python lists for storing info about the confirmSign_click_11
    // current position of the mouse:
    confirmSign_click_11.x = [];
    confirmSign_click_11.y = [];
    confirmSign_click_11.leftButton = [];
    confirmSign_click_11.midButton = [];
    confirmSign_click_11.rightButton = [];
    confirmSign_click_11.time = [];
    confirmSign_click_11.clicked_name = [];
    gotValidClick = false; // until a click is received
    gender_c.reset()
    other_gender_text.setText('');
    other_gender_text.refresh();
    // Run 'Begin Routine' code from showMouse_6
    document.body.style.cursor='auto';
    psychoJS.experiment.addData('gender.started', globalClock.getTime());
    genderMaxDuration = null
    // keep track of which components have finished
    genderComponents = [];
    genderComponents.push(confirmSign_click_11);
    genderComponents.push(confirmSign_button_11);
    genderComponents.push(gender_Q);
    genderComponents.push(gender_c);
    genderComponents.push(other_gender_text);
    
    for (const thisComponent of genderComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function genderRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'gender' ---
    // get current time
    t = genderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *confirmSign_click_11* updates
    if (t >= 0 && confirmSign_click_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_click_11.tStart = t;  // (not accounting for frame time here)
      confirmSign_click_11.frameNStart = frameN;  // exact frame index
      
      confirmSign_click_11.status = PsychoJS.Status.STARTED;
      confirmSign_click_11.mouseClock.reset();
      prevButtonState = confirmSign_click_11.getPressed();  // if button is down already this ISN'T a new click
      }
    if (confirmSign_click_11.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = confirmSign_click_11.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          confirmSign_click_11.clickableObjects = eval(confirmSign_button_11)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(confirmSign_click_11.clickableObjects)) {
              confirmSign_click_11.clickableObjects = [confirmSign_click_11.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of confirmSign_click_11.clickableObjects) {
              if (obj.contains(confirmSign_click_11)) {
                  gotValidClick = true;
                  confirmSign_click_11.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              confirmSign_click_11.clicked_name.push(null);
          }
          _mouseXYs = confirmSign_click_11.getPos();
          confirmSign_click_11.x.push(_mouseXYs[0]);
          confirmSign_click_11.y.push(_mouseXYs[1]);
          confirmSign_click_11.leftButton.push(_mouseButtons[0]);
          confirmSign_click_11.midButton.push(_mouseButtons[1]);
          confirmSign_click_11.rightButton.push(_mouseButtons[2]);
          confirmSign_click_11.time.push(confirmSign_click_11.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *confirmSign_button_11* updates
    if ((gender_c.rating) && confirmSign_button_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_button_11.tStart = t;  // (not accounting for frame time here)
      confirmSign_button_11.frameNStart = frameN;  // exact frame index
      
      confirmSign_button_11.setAutoDraw(true);
    }
    
    
    // *gender_Q* updates
    if (t >= 0.0 && gender_Q.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      gender_Q.tStart = t;  // (not accounting for frame time here)
      gender_Q.frameNStart = frameN;  // exact frame index
      
      gender_Q.setAutoDraw(true);
    }
    
    
    // *gender_c* updates
    if (t >= 0 && gender_c.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      gender_c.tStart = t;  // (not accounting for frame time here)
      gender_c.frameNStart = frameN;  // exact frame index
      
      gender_c.setAutoDraw(true);
    }
    
    
    // *other_gender_text* updates
    if (t >= 0 && other_gender_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      other_gender_text.tStart = t;  // (not accounting for frame time here)
      other_gender_text.frameNStart = frameN;  // exact frame index
      
      other_gender_text.setAutoDraw(true);
    }
    
    // Run 'Each Frame' code from max_char_limit
    if ((other_gender_text.text.length > 500)) {
        other_gender_text.text = other_gender_text.text.slice(0, 500);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of genderComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function genderRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'gender' ---
    for (const thisComponent of genderComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('gender.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('confirmSign_click_11.x', confirmSign_click_11.x);
    psychoJS.experiment.addData('confirmSign_click_11.y', confirmSign_click_11.y);
    psychoJS.experiment.addData('confirmSign_click_11.leftButton', confirmSign_click_11.leftButton);
    psychoJS.experiment.addData('confirmSign_click_11.midButton', confirmSign_click_11.midButton);
    psychoJS.experiment.addData('confirmSign_click_11.rightButton', confirmSign_click_11.rightButton);
    psychoJS.experiment.addData('confirmSign_click_11.time', confirmSign_click_11.time);
    psychoJS.experiment.addData('confirmSign_click_11.clicked_name', confirmSign_click_11.clicked_name);
    
    psychoJS.experiment.addData('gender_c.response', gender_c.getRating());
    psychoJS.experiment.addData('gender_c.rt', gender_c.getRT());
    psychoJS.experiment.addData('other_gender_text.text',other_gender_text.text)
    // the Routine "gender" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var race_ethnMaxDurationReached;
var race_ethnMaxDuration;
var race_ethnComponents;
function race_ethnRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'race_ethn' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    race_ethnClock.reset();
    routineTimer.reset();
    race_ethnMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from exclude_15
    if (consent.rating == "I do not consent to participation or I am younger than 18 years old.") {
        continueRoutine = false;
    }
    
    // setup some python lists for storing info about the confirmSign_click_13
    // current position of the mouse:
    confirmSign_click_13.x = [];
    confirmSign_click_13.y = [];
    confirmSign_click_13.leftButton = [];
    confirmSign_click_13.midButton = [];
    confirmSign_click_13.rightButton = [];
    confirmSign_click_13.time = [];
    confirmSign_click_13.clicked_name = [];
    gotValidClick = false; // until a click is received
    race_c.reset()
    other_race_text.setText('');
    other_race_text.refresh();
    // Run 'Begin Routine' code from showMouse_7
    document.body.style.cursor='auto';
    psychoJS.experiment.addData('race_ethn.started', globalClock.getTime());
    race_ethnMaxDuration = null
    // keep track of which components have finished
    race_ethnComponents = [];
    race_ethnComponents.push(confirmSign_click_13);
    race_ethnComponents.push(confirmSign_button_13);
    race_ethnComponents.push(race_Q);
    race_ethnComponents.push(race_c);
    race_ethnComponents.push(other_race_text);
    
    for (const thisComponent of race_ethnComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function race_ethnRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'race_ethn' ---
    // get current time
    t = race_ethnClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *confirmSign_click_13* updates
    if (t >= 0 && confirmSign_click_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_click_13.tStart = t;  // (not accounting for frame time here)
      confirmSign_click_13.frameNStart = frameN;  // exact frame index
      
      confirmSign_click_13.status = PsychoJS.Status.STARTED;
      confirmSign_click_13.mouseClock.reset();
      prevButtonState = confirmSign_click_13.getPressed();  // if button is down already this ISN'T a new click
      }
    if (confirmSign_click_13.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = confirmSign_click_13.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          confirmSign_click_13.clickableObjects = eval(confirmSign_button_13)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(confirmSign_click_13.clickableObjects)) {
              confirmSign_click_13.clickableObjects = [confirmSign_click_13.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of confirmSign_click_13.clickableObjects) {
              if (obj.contains(confirmSign_click_13)) {
                  gotValidClick = true;
                  confirmSign_click_13.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              confirmSign_click_13.clicked_name.push(null);
          }
          _mouseXYs = confirmSign_click_13.getPos();
          confirmSign_click_13.x.push(_mouseXYs[0]);
          confirmSign_click_13.y.push(_mouseXYs[1]);
          confirmSign_click_13.leftButton.push(_mouseButtons[0]);
          confirmSign_click_13.midButton.push(_mouseButtons[1]);
          confirmSign_click_13.rightButton.push(_mouseButtons[2]);
          confirmSign_click_13.time.push(confirmSign_click_13.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *confirmSign_button_13* updates
    if ((gender_c.rating) && confirmSign_button_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confirmSign_button_13.tStart = t;  // (not accounting for frame time here)
      confirmSign_button_13.frameNStart = frameN;  // exact frame index
      
      confirmSign_button_13.setAutoDraw(true);
    }
    
    
    // *race_Q* updates
    if (t >= 0.0 && race_Q.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      race_Q.tStart = t;  // (not accounting for frame time here)
      race_Q.frameNStart = frameN;  // exact frame index
      
      race_Q.setAutoDraw(true);
    }
    
    
    // *race_c* updates
    if (t >= 0 && race_c.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      race_c.tStart = t;  // (not accounting for frame time here)
      race_c.frameNStart = frameN;  // exact frame index
      
      race_c.setAutoDraw(true);
    }
    
    
    // *other_race_text* updates
    if (t >= 0 && other_race_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      other_race_text.tStart = t;  // (not accounting for frame time here)
      other_race_text.frameNStart = frameN;  // exact frame index
      
      other_race_text.setAutoDraw(true);
    }
    
    // Run 'Each Frame' code from max_char_limit_2
    if ((other_race_text.text.length > 500)) {
        other_gender_text.text = other_gender_text.text.slice(0, 500);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of race_ethnComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function race_ethnRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'race_ethn' ---
    for (const thisComponent of race_ethnComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('race_ethn.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('confirmSign_click_13.x', confirmSign_click_13.x);
    psychoJS.experiment.addData('confirmSign_click_13.y', confirmSign_click_13.y);
    psychoJS.experiment.addData('confirmSign_click_13.leftButton', confirmSign_click_13.leftButton);
    psychoJS.experiment.addData('confirmSign_click_13.midButton', confirmSign_click_13.midButton);
    psychoJS.experiment.addData('confirmSign_click_13.rightButton', confirmSign_click_13.rightButton);
    psychoJS.experiment.addData('confirmSign_click_13.time', confirmSign_click_13.time);
    psychoJS.experiment.addData('confirmSign_click_13.clicked_name', confirmSign_click_13.clicked_name);
    
    psychoJS.experiment.addData('race_c.response', race_c.getRating());
    psychoJS.experiment.addData('race_c.rt', race_c.getRT());
    psychoJS.experiment.addData('other_race_text.text',other_race_text.text)
    // the Routine "race_ethn" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ThanksMaxDurationReached;
var ThanksMaxDuration;
var ThanksComponents;
function ThanksRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Thanks' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    ThanksClock.reset(routineTimer.getTime());
    routineTimer.add(5.000000);
    ThanksMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from exclude_16
    if (consent.rating == "I do not consent to participation or I am younger than 18 years old.") {
        continueRoutine = false;
    }
    
    // Run 'Begin Routine' code from showMouse_5
    document.body.style.cursor='auto';
    psychoJS.experiment.addData('Thanks.started', globalClock.getTime());
    ThanksMaxDuration = null
    // keep track of which components have finished
    ThanksComponents = [];
    ThanksComponents.push(ThanksText);
    
    for (const thisComponent of ThanksComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ThanksRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Thanks' ---
    // get current time
    t = ThanksClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ThanksText* updates
    if (t >= 0.0 && ThanksText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ThanksText.tStart = t;  // (not accounting for frame time here)
      ThanksText.frameNStart = frameN;  // exact frame index
      
      ThanksText.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (ThanksText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ThanksText.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ThanksComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ThanksRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Thanks' ---
    for (const thisComponent of ThanksComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Thanks.stopped', globalClock.getTime());
    if (ThanksMaxDurationReached) {
        ThanksClock.add(ThanksMaxDuration);
    } else {
        ThanksClock.add(5.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
