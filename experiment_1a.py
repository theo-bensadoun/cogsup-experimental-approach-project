import expyriment as xpy

import config1a

xpy.control.set_develop_mode()

exp = xpy.design.Experiment(
    name=config1a.EXPERIMENT_NAME,
    background_colour=config1a.BLACK,
    foreground_colour=config1a.WHITE,
)

exp.data_variable_names = [
    "run_type",
    "response",
    "key",
    "rt_ms",
]

xpy.control.initialize(exp)

fixation_cross = xpy.stimuli.FixCross(size=config1a.CROSS_SIZE, line_width=config1a.LINE_WIDTH_CROSS, colour=config1a.WHITE)
fixation_cross_screen = xpy.stimuli.BlankScreen(colour=config1a.BLACK)
fixation_cross.plot(fixation_cross_screen)

instructions = xpy.stimuli.TextScreen(
    heading="Experiment 1a",
    text="Press SPACE to start.",
)

response_screen = xpy.stimuli.TextScreen(
    heading="Which of the two items is bigger on the screen?",
    text="C = left item\nM = right item",
)

end_screen = xpy.stimuli.TextScreen(
    heading="Thank you!",
    text="Press SPACE to finish experiment.",
)

for stimulus in (instructions, fixation_cross_screen, response_screen, end_screen):
    stimulus.preload()

xpy.control.start(skip_ready_screen=True)

instructions.present()
exp.keyboard.wait(keys=[xpy.misc.constants.K_SPACE])

fixation_cross_screen.present()
exp.clock.wait(config1a.FIXATION_CROSS_MS)

# TODO: putting images

response_screen.present()
key, rt = exp.keyboard.wait(
    keys=[xpy.misc.constants.K_c, xpy.misc.constants.K_m]
)

if key == xpy.misc.constants.K_c:
    response = config1a.C_KEY
else:
    response = config1a.M_KEY

end_screen.present()
exp.keyboard.wait(keys=[xpy.misc.constants.K_SPACE])

exp.data.add(["VOID (will be congruent or incongruent later)", response, key, rt])
exp.data.save()

xpy.control.end()
