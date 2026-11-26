## Contents

- [Main hypothesis of the paper](#main-hypothesis-of-the-paper)
- [Overview of experiments](#overview-of-experiments)
- [Experiment 1: Familiar-Size Stroop Task](#experiment-1-familiar-size-stroop-task)
- [Experiment 2: Single-Item Stroop Task](#experiment-2-single-item-stroop-task)
- [Experiment 3: Rule-Learning Stroop Task](#experiment-3-rule-learning-stroop-task)
- [Decision summary (Exp. 1-3)](#8-decision-summary-exp-1-3)

---

## Main hypothesis of the paper

When we recognise a familiar object, we automatically access its real-world size, just as we automatically access its basic-level category.

**Test:** a Stroop-like paradigm. Observers make a purely VISUAL size judgment ("which object is bigger / smaller ON THE SCREEN?"). The identity and real-world size of the objects are completely irrelevant to the task.

**Prediction:** visual size judgments are faster (and more accurate) when the visual sizes are congruent with the objects' real-world sizes (e.g., horse shown big, alarm clock shown small) than when they are incongruent (horse small, alarm clock big).

**Logic:** if task-irrelevant real-world size slows down a simple visual judgment, real-world size must be accessed automatically and obligatorily upon recognition (analogous to word meaning in the classic Stroop task).

**Analogy with the classic Stroop task:**

|                    | Classic Stroop         | Familiar-size Stroop      |
|--------------------|------------------------|---------------------------|
| Relevant dimension | ink colour             | size on the screen        |
| Irrelevant dim.    | word meaning           | real-world size of object |
| Congruent          | "GREEN" in green ink   | chair big, shoe small     |
| Incongruent        | "GREEN" in pink ink    | chair small, shoe big     |

## Overview of experiments

**Exp. 1 — Familiar Object Stroop Task** (two objects side by side)
- Q: Is real-world size accessed automatically?
- 1a: visual size set by bounding-box diagonal
- 1b: visual size set by pixel area
- Result: Stroop effect 38 ms (1a), 21 ms (1b); all observers.

**Exp. 2 — Single-Item Stroop Task** (one object, "big or small on screen?")
- Q: Is direct comparison of two objects necessary?
- Result: Stroop effect 17 ms; no effect on rectangles covering the objects.

**Exp. 3 — Rule-Learning Stroop Task** (novel block objects, size by colour)
- Q: Is an explicitly learned rule sufficient, or is experience needed?
- Result: no effect (-4 ms), reliably smaller than for familiar objects.

**Overall conclusion:** real-world size is automatically accessed for familiar objects; this requires extensive experience, not just fact-based knowledge.

**Decision summary for our study:** see the end of Experiment 3, [section 8](#8-decision-summary-exp-1-3).

---

## Experiment 1: Familiar-Size Stroop Task

### 1. Hypotheses

**H0:** Real-world size is not accessed automatically. RT (and error rate) do not differ between congruent and incongruent trials: `RT_incongruent - RT_congruent = 0`.

**H1:** Real-world size is accessed automatically and interferes with visual size judgments. `RT_incongruent > RT_congruent`, and there are more errors on incongruent trials.

**Secondary questions:**
- Main effect of task: are "bigger" judgments faster than "smaller" ones?
- Task x congruency interaction: does the Stroop effect differ between the two tasks?
- Exp. 1a only: does the effect depend on aspect-ratio pairing (matched vs. pseudo-paired)?
- Exp. 1b: does the effect survive when pixel area is controlled?

### 2. Definitions

- **RT:** time from stimulus onset to key press (ms).
- **RT_congruent / RT_incongruent:** each participant's mean RT over correct, non-excluded trials in that condition.
- **Stroop effect (per participant):** `RT_incongruent - RT_congruent`.

### 3. Statistical tests

#### 3.1 Main test: paired t-test (RT_incongruent vs. RT_congruent, across participants)

- Equivalent to a one-sample t-test of the Stroop effect against 0.
- Expected for Exp. 1a: 38 ms, SEM = 6, t(16) ~ 6, p < .001.
- Assumptions:
  - Paired data: both conditions come from the same participants (within-subject design).
  - Participants are independent of each other.
  - The per-participant differences are roughly normal. This matters because N is small. Check with Shapiro-Wilk or a Q-Q plot.
  - RT is on an interval/ratio scale (satisfied).
- Fallback if normality fails: Wilcoxon signed-rank test.
- Also report Cohen's d_z = mean(effect) / SD(effect). Paper reports d = 1.5 (1a) and 1.4 (1b).

#### 3.2 2 x 2 repeated-measures ANOVA (congruency x task)

- Tests the main effects of congruency and task, and their interaction.
- Assumptions:
  - Normality of residuals / cell differences.
  - Sphericity: automatically satisfied (each factor has 2 levels).
- **WARNING:** the paper reports F(1, 67) and F(1, 63). With N = 17 and N = 16, a correct RM-ANOVA gives F(1, 16) and F(1, 15). The paper's df look like 4 cells x N were treated as independent observations. Use the correct within-subject error terms.

#### 3.3 Follow-up paired t-tests

- Stroop effect within each task separately ("smaller", "bigger").
- Exp. 1a: Stroop effect in matched vs. pseudo-paired trials, and a comparison between them.

#### 3.4 Error analysis: paired t-test on error counts (incongruent vs. congruent)

- Error counts are small and skewed, so a Wilcoxon signed-rank test is a reasonable robustness check.

#### 3.5 Between-experiment comparison: independent-samples t-test (Stroop effect in 1a vs. 1b, overall RT, overall errors)

- Assumes independent groups and roughly equal variances. Use Welch's t-test to be safe.

### 4. Methodology

#### 4.1 Participants

- **What:** N = 18 (1a; 17 analysed), N = 16 (1b), age 18-35.
- **Why:** Fully within-subject design with hundreds of trials per person, so each participant serves as their own control. The large effect (d ~ 1.5) gives enough power with a small N.

#### 4.2 Apparatus

- **What:** viewing distance 57 cm, screen 29 x 39.5 cm, 1024 x 768 px, Psychtoolbox.
- **Why:**
  - At 57 cm, 1 cm on screen ~ 1 deg of visual angle, so stimulus sizes are defined in retinal terms.
  - Psychtoolbox gives precise timing, needed because the effect is only 20-40 ms.

#### 4.3 Trial structure

- **Fixation cross, 700 ms.**
  Why: centres gaze, so both objects are equidistant from fixation at onset; same starting point on every trial.
- **Two objects side by side, one visually big and one visually small.**
  Why: pairwise comparison makes the decision simple and unambiguous.
- **Display stays on until response.**
  Why: measures natural decision time; no missed trials.
- **Response keys:** `c` = left object (left index finger), `m` = right object (right index finger).
  Why: spatially compatible mapping avoids Simon-type interference and mapping errors.
- **Inter-trial interval of 900 ms after a correct response.**
  Why: separates trials and resets attention.
- **After an error: feedback plus a 5 s timeout.**
  Why: penalises errors and discourages a speed-accuracy trade-off.

#### 4.4 Instructions: "as fast as possible while maintaining high accuracy"

- **Why:** keeps accuracy high (~98%) while RT stays sensitive to interference.

#### 4.5 Task factor: "which is visually bigger?" vs. "which is visually smaller?"

- **What:** both tasks are run on the same displays; task order counterbalanced across participants.
- **Why:**
  - Separates congruency from response identity. In the "bigger" task the correct congruent answer is the real-world big object; in the "smaller" task it is the real-world small object.
  - So the effect cannot simply be faster responses to real-world big objects; it must reflect a match or conflict between the two sizes.
  - Counterbalancing task order controls for practice and fatigue.

#### 4.6 Congruency factor

- **What:** the same object pair is shown both congruently (big object big, small object small) and incongruently (reversed).
- **Why:** item identity is held constant across conditions, so RT differences cannot come from differences in object recognisability.

#### 4.7 Side of the correct answer (left/right)

- **What:** the correct object appears equally often on the left and the right.
- **Why:** controls for hand-speed asymmetries and response biases; makes side orthogonal to congruency.

#### 4.8 Defining visual size: Exp. 1a (bounding-box diagonal)

- **What:** objects are scaled so the diagonal of their bounding box is 35% (small, ~11 deg) or 60% (big, ~18 deg) of screen height.
- **Why the diagonal:** less sensitive to aspect ratio than height or width.

**Aspect-ratio matched pairs (first half):**
- **What:** 36 big + 36 small objects, paired so the difference in width/height is <= 0.2 (e.g., car-pizza cutter, ladder-hammer). Every participant sees the same pairs.
- **Why:** a wide object looks smaller than a tall one at the same diagonal. Matching shape within a pair removes this confound.

**Pseudo-random pairs (second half):**
- **What:** new pairings, different for each participant, balanced across trials (a tall-big + wide-small pair is offset by a tall-small + wide-big pair).
- **Why:** doubles the trial count (more power) using the same images. The ratio of aspect ratios is balanced across congruent and incongruent trials, so shape cannot drive the effect. Also tests whether exact shape matching is needed (result: it is not).

#### 4.9 Defining visual size: Exp. 1b (pixel area)

- **Why:** real-world big objects tend to fill more of their bounding box (tree vs. flower). In Exp. 1a, congruent displays may therefore have had a larger pixel-area difference and been visually easier. Exp. 1b rules this out.
- **What:**
  - New set of 20 big + 20 small objects.
  - Object pixel area set to 20% or 48% of a 440 x 440 frame, i.e., 4.9% vs. 11.8% of the screen.
  - Relative pixel area is identical across congruent and incongruent displays.
- **Item selection:**
  - No objects with holes (ring, shopping cart) or partial holes (slide, nutcracker): unclear whether interior background pixels should count as part of the area.
  - Objects that cannot fill 48% of the frame (extreme aspect ratios, e.g., pen, floor lamp) are excluded automatically.

#### 4.10 Design and trial counts

- Exp. 1a: 36 pairs x 2 congruency x 2 side x 2 task x 2 pairing sets = 576 trials (288 congruent / 288 incongruent).
- Exp. 1b: 20 x 2 x 2 x 2 x 2 = 320 trials (160 / 160).
- Block order: pairing set 1 (both tasks) -> pairing set 2 (both tasks).

**Why a fully crossed design:** congruency is orthogonal to item, side, task and pairing. Many trials per cell are needed because RT is noisy and the effect is small.

#### 4.11 Data preprocessing

- **Exclude error trials from the RT analysis.**
  Why: they reflect a different process; errors are analysed separately.
- **Exclude RT < 200 ms.**
  Why: anticipations or accidental presses, too fast for recognition plus decision.
- **Exclude RT > 1500 ms.**
  Why: lapses of attention; they distort means.
- Exclusion rates: 3.8% of trials (1a), 1.4% (1b). One participant in 1a was excluded for a computer error.

---

## Experiment 2: Single-Item Stroop Task

### 0. Purpose

Tests whether the direct perceptual comparison of two objects (required in Exp. 1) is necessary for the familiar-size Stroop effect. Only one object is shown per trial; observers judge whether it is big or small ON THE SCREEN.

### 1. Hypotheses

**Main:**

**H0:** In a single-item visual size task, `RT_incongruent = RT_congruent`. (The Exp. 1 effect required comparing two objects.)

**H1:** `RT_incongruent > RT_congruent`. Real-world size is accessed automatically even without a second object.

**Control ("hidden" Stroop on rectangles):**
- During practice, black filled rectangles (the bounding boxes of real object images) are shown. Trials are labelled "congruent" or "incongruent" according to the hidden object; observers are blind to this.
- Expected: NO effect.
- Logic: if an effect appeared on rectangles, it would be driven by low-level features of the bounding box (shape, aspect ratio), not by object recognition.

**Secondary:**
- Main effect of real-world size: are responses faster for real-world big or small objects?
- Real-world size x congruency interaction.

### 2. Definitions

- **Visual sizes:** only two exist (bounding-box diagonal = 35% or 60% of screen height, as in Exp. 1a).
- **Congruent:** real-world big object shown big, or real-world small object shown small.
- **Incongruent:** real-world big object shown small, or real-world small object shown big.
- **RT_congruent / RT_incongruent:** each participant's mean RT over correct, non-excluded trials in that condition.
- **Stroop effect (per participant):** `RT_incongruent - RT_congruent`.

**Example (main phase):**

| Display              | Answer  | Condition   |
|----------------------|---------|-------------|
| horse, shown big     | "big"   | congruent   |
| horse, shown small   | "small" | incongruent |
| alarm clock, small   | "small" | congruent   |
| alarm clock, big     | "big"   | incongruent |

**Note:** the design is real-world size (2) x visual size (2). Congruency is the INTERACTION of these two factors. The paper re-parametrises the ANOVA as congruency x real-world size; then the main effect of visual size corresponds to the real-world size x congruency interaction.

### 3. Statistical tests

#### 3.1 Main test: paired t-test (RT_incongruent vs. RT_congruent, across participants)

- Equivalent to a one-sample t-test of the Stroop effect against 0.
- Paper: 17 ms, SEM = 6, d = 0.65 -> t(18) ~ 2.8.
- Assumptions: paired (within-subject) data; independent participants; per-participant differences roughly normal (check Shapiro-Wilk / Q-Q).
- Fallback: Wilcoxon signed-rank test.

#### 3.2 2 x 2 repeated-measures ANOVA (congruency x real-world size)

- Main effects of congruency and real-world size, and their interaction.
- Sphericity automatically satisfied (2 levels per factor).

#### 3.3 Control test: paired t-test on rectangle trials ("congruent" vs. "incongruent" rectangles)

- Paper: 7 ms, SEM = 5, t(18) = 1.38, ns.

#### 3.4 Note on degrees of freedom (applies to Exp. 1 and Exp. 2)

- Correct RM-ANOVA error df for a 2-level within-subject factor = N - 1.

  | Experiment      | Should be | Paper reports |
  |-----------------|-----------|---------------|
  | Exp. 1a (N = 17) | F(1, 16) | F(1, 67)      |
  | Exp. 1b (N = 16) | F(1, 15) | F(1, 63)      |
  | Exp. 2 (N = 19)  | F(1, 18) | F(1, 75)      |

- Paper's df = 4N - 1 in every case, i.e., the TOTAL df of the ANOVA table (4 cells x N - 1), not the error df. Most likely a reporting error.
- Check: for a 2-level factor, F = t^2 in a correct RM-ANOVA.

  | Experiment | t^2                  | Reported F | Verdict |
  |------------|----------------------|------------|---------|
  | Exp. 1b    | (21 / 3.8)^2 = 30.5  | 31.0       | consistent |
  | Exp. 2     | (17 / 6)^2 = 8.0     | 8.1        | consistent |
  | Exp. 1a    | (38 / 6)^2 = 40.1    | 18.2       | inconsistent (likely a typo in SEM or F) |

- So the F values themselves are probably from a correct RM-ANOVA; only the df labels are wrong.
- With correct df all effects remain significant: Exp. 1a: p ~ .0006; Exp. 1b: p ~ .00005; Exp. 2: p ~ .011.
- For our implementation: use a standard RM-ANOVA. Sanity check: F for congruency should equal t^2 from the paired t-test. Compare with the paper on effect size (ms, d), not on F or p.

### 4. Methodology

#### 4.1 Participants

- **What:** N = 19, age 18-35.
- **Why:** larger than Exp. 1, presumably because a smaller effect was expected without direct comparison (result: d = 0.65 vs. 1.5 in Exp. 1a).

#### 4.2 Stimuli

- **What:** the same 36 big + 36 small objects as Exp. 1a. Visual size set the same way (bounding-box diagonal = 35% or 60% of screen height).
- **Why:** keeps results comparable with Exp. 1a; only the task changes (one object instead of two).
- **Not controlled:**
  - No pairing, so no aspect-ratio matching.
  - Pixel area not controlled (Exp. 1a set, not 1b). For a single item this matters more, since how much an object fills its bounding box directly affects perceived size. The rectangle control only addresses bounding-box shape, not fill.

#### 4.3 Task and instructions

- **What:** "Is this small or big on the screen?" Observers keep track of the average size and judge whether each item is smaller or larger than the average. As fast as possible while maintaining high accuracy.
- **Why:** a single-item task needs an internal reference; the instruction makes it explicit (the average size).

#### 4.4 Response

- **What:** two index fingers on `c` and `m` = "big on screen" / "small on screen". Key assignment counterbalanced across observers.
- **Why:** unlike Exp. 1, the response is not spatial (not left/right object). If "big" were always the right hand, congruency could be confounded with hand or with space-magnitude associations (e.g., right = more).

#### 4.5 Trial timing

- **What:** same as Exp. 1: fixation 700 ms -> stimulus until response -> 900 ms after correct response; error feedback + 5 s after error.
- **Why:** so the only difference from Exp. 1 is the number of objects.

#### 4.6 Initialization phase (rectangles)

**Block 1: 24 alternating trials**
- **What:** black filled rectangles = bounding boxes of 6 big + 6 small objects, each at both visual sizes (12 x 2 = 24). Trials alternate systematically in visual size and in the real-world size of the hidden object.
- **Why:**
  - Teaches the two visual sizes, so observers form a reference for "average". Without it, "big" is undefined in a single-item task.
  - Rectangles are neutral (no real-world size), so the reference is formed without object influence.
  - Using real objects' bounding boxes exposes observers to the range of shapes they will see later, in an unbiased way.

**Blocks 2-3: 48 randomized trials**
- **What:** the same 24 rectangles, twice, in random order.
- **Why:**
  - Practice speed and accuracy when visual size is unpredictable.
  - Hidden control: each rectangle maps to an object, so trials can be labelled congruent/incongruent while observers are blind to it. Tests whether bounding-box shape alone can produce the effect.

#### 4.7 Main phase

- **What:** 288 trials = 36 objects x 2 real-world sizes (i.e., all 72 objects) x 2 visual sizes x 2 repetitions -> 144 congruent / 144 incongruent.
- **Why:** fully crossed; every object is shown both big and small, so congruency is not confounded with item.

#### 4.8 Data preprocessing

- Same as Exp. 1: exclude errors and RT < 200 ms or > 1500 ms.
- 3.9% of trials removed.

### 5. Results (paper)

- Stroop effect (objects): 17 ms, SEM = 6, d = 0.65, p < .05.
- Effect in expected direction: 17 of 19 observers.
- Main effect of real-world size: faster for real-world big objects (e.g., piano); F = 7.2, p < .05.
- Real-world size x congruency: no interaction (F = 1.1, ns).
- Hidden Stroop (rectangles): 7 ms, SEM = 5, t(18) = 1.38, ns.

**Authors' conclusion:** the effect survives without direct comparison of two objects, but is about half the size (17 ms vs. 38 ms in Exp. 1a). No effect on rectangles -> object recognition is required.

### 6. Weaknesses to keep in mind

1. "No effect on rectangles" is a null result, not evidence of absence. 7 ms is not zero. The paper does not test whether the rectangle effect (7 ms) differs from the object effect (17 ms). Proper test: stimulus type x congruency interaction, or an equivalence test.
2. Rectangles are confounded with order and practice: always first, during learning, with fewer trials (48-72 vs. 288). Noisier RTs may hide an effect.
3. Pixel area not controlled (Exp. 1a stimulus set).
4. df error in the ANOVA (F(1, 75) instead of F(1, 18)); see 3.4.
5. Accuracy/errors not analysed (unlike Exp. 1).

### 7. Implications for our study (N = 5)

Smaller effect (d = 0.65) and half the trials per condition (144).

- Group paired t-test, N = 5: power ~20% (two-tailed), ~33% (one-tailed).
- Per-participant analysis (144 trials/condition, 17 ms effect, trial SD 80-120 ms): power per person ~33-56%. Expect the effect in ~2-3 of 5 participants, which is indistinguishable from chance (P(>= 4 of 5 by chance) ~ 19%).
- Rectangle control: not interpretable at N = 5.

**Conclusion:** at N = 5, Exp. 2 is very likely to be uninformative; neither a positive nor a negative result can be trusted.

**Options:**
1. Skip it and focus on Exp. 1.
2. Run it as a pilot/demo, stating in advance that no statistical conclusions will be drawn.
3. Increase trials per person (e.g., 4 repetitions instead of 2 -> 576 trials, ~20 min). Per-person power rises to ~55-80%, but the group-level inference at N = 5 remains weak.

---

## Experiment 3: Rule-Learning Stroop Task

### 0. Purpose

Exp. 1-2 showed that real-world size of familiar objects is accessed automatically. Exp. 3 asks WHERE this automaticity comes from.

**Two accounts:**
1. **Experience / expertise:** knowledge of object size comes from extensive visual experience with objects in the world; this experience is required for automatic activation of familiar size.
2. **Conceptual level (cognitive penetrability):** the interference arises at an abstract, fact-based level. Then simply TELLING people that some objects are big and others small should be enough to produce a Stroop effect.

**Approach:** novel objects with no prior experience. Size is defined by a colour rule. In "block world", blue-red block objects are big and yellow-green block objects are small (rule reversed for half of the observers).

### 1. Hypotheses

**H0:** For objects whose size is known only from a learned rule, `RT_incongruent = RT_congruent`.
-> More extensive experience is required (account 1).

**H1:** `RT_incongruent > RT_congruent`.
-> Known size is rapidly incorporated into object knowledge from a rule and minimal exposure (account 2).

**Key difference from Exp. 1-2:** BOTH outcomes are theoretically informative. A null result supports account 1. Therefore a null result must be backed by adequate power (see 3.2).

**Secondary:**
- Task x congruency interaction.
- Between-experiment comparison: does the Stroop effect differ between familiar objects (Exp. 1a / 1b) and rule-learned objects (Exp. 3)?

### 2. Definitions

- **Task:** as in Exp. 1 (two objects side by side; "which is visually bigger / smaller on the screen?").
- **"Real-world size"** is IMPLIED by colour (according to the learned rule).
- **Congruent:** the implied-big object is bigger on the screen than the implied-small object.
- **Incongruent:** the implied-small object is bigger on the screen.
- **RT_congruent / RT_incongruent and the Stroop effect:** as in Exp. 1.

### 3. Statistical tests

#### 3.1 Main test: paired t-test / 2 x 2 RM-ANOVA (congruency x task)

- As in Exp. 1.
- Paper: -4 ms, SEM = 3, d = -0.3, F = 1.7, p = .21 (ns).

#### 3.2 Power analysis (to make the null result interpretable)

- Paper reports power of this design to detect:
  - an effect of the Exp. 1 magnitude: > 99%
  - an effect half that size: 83%
  - at 99% power: d = 1.0 (~12 ms Stroop effect)
- The power for Exp. 1-based effects appears to use the Exp. 1 variance.
- Additional check (not in the paper): 95% CI of the effect = -4 +/- 2.12 x 3 = [-10, +2] ms -> effects larger than ~2 ms in the expected direction are excluded. This is a strong null, not just non-significance.
- Stricter alternative: equivalence test (TOST) with a pre-specified smallest effect size of interest.

#### 3.3 Between-experiment comparison: mixed ANOVA

- Factors: experiment (familiar vs. bicolor objects; between-subjects) x congruency (within-subjects).
- Key test: experiment x congruency INTERACTION.
- Why the interaction: "significant in Exp. 1, non-significant in Exp. 3" is not by itself evidence that the effects differ. The difference must be tested directly.
- Follow-up: independent-samples t-test on Stroop effects (Exp. 1a vs. 3; Exp. 1b vs. 3). Assumes independent groups; use Welch's t-test to be safe.
- Also: main effect of experiment on overall RT (checks that groups were equally fast overall).

#### 3.4 Note on degrees of freedom

- Main ANOVA: paper reports F(1, 67) with N = 17 (= 4N - 1, total df). Correct: F(1, 16). F = 1.7 matches t^2 = (4/3)^2 = 1.8, and p = .21 matches F(1, 16) -> analysis correct, df mislabelled.
- Between-experiment ANOVA: paper reports F(1, 67) with 17 + 17 = 34 participants (= 2 x 34 - 1) and F(1, 65) with 16 + 17 = 33 (= 2 x 33 - 1). Correct: F(1, 32) and F(1, 31), matching the df of the paper's own t-tests. Check: t^2 = 6.06^2 = 36.7 = interaction F.

### 4. Methodology

#### 4.1 Participants

- **What:** N = 17, new participants, age 18-35.
- **Why new:** participants from earlier experiments could have guessed the hypothesis or carried over strategies.

#### 4.2 Physical reference objects

- **What:** two real block objects in the testing room, one big and one small.
- **NOTE:** typo in the paper. Text says small ~120 x 75 cm and large ~30 x 18 cm; obviously swapped. Big ~120 x 75 cm, small ~30 x 18 cm.
- **Why physical objects:** gives the rule a real, embodied size, not just a verbal statement; approximates real-world experience as closely as possible within a short session.

#### 4.3 Familiarization phase (~30 min)

**Goal:** maximise exposure to the colour-size rule in a short time.

**Step 1: Drawing (3 min per reference object)**
- **What:** colour drawing of each reference object with pencil and markers.
- **Why:** forces long, careful inspection of the objects, including colour.

**Step 2: Change detection (3 trials per reference object)**
- **What:** 10 s to study the object -> observer closes eyes -> one or more blocks (same colours) are added -> three guesses to identify added blocks, with feedback.
- **Why:** more active engagement with the objects. Added blocks always match the object's colours, reinforcing "these colours = this object".

**Step 3: On-screen familiarization (32 trials)**
- **What:** observer turns to look at the big or small reference object -> looks back at the screen -> picture of a new block object of the same size class (same colours) shown for 500 ms -> judge whether it would be slightly taller or shorter than the reference object, if placed beside it in the world. 32 pictures in random order.
- **Why:**
  - Exposes observers to all 32 objects used in the main task.
  - Main point: forces observers to conceive of each depicted object's physical size in the world, anchored to the real reference object.
  - 500 ms is too short to count rows of blocks, so the judgment must rely on a holistic impression of size, not counting.

#### 4.4 Stimuli

- **What:** 32 bicolor block objects built in LEGO Digital Designer. Every shape exists in both colour schemes (blue-red and yellow-green). Each observer sees 16 yellow-green and 16 blue-red objects. Pairs matched in aspect ratio as in Exp. 1a.
- **Why aspect-ratio matching:** same control as Exp. 1a; shape should not affect perceived size within a pair.
- **Not stated:** how visual size on screen was set (presumably bounding-box diagonal as in Exp. 1a).

#### 4.5 Main task design

- **What:** as in Exp. 1. Fixation -> two objects -> "which is bigger / smaller on the screen?" -> `c` / `m` (left / right) -> feedback.
- **Trials:** 512 = 16 pairs x 2 congruency x 2 side x 2 task x 4 repetitions (256 congruent / 256 incongruent).
- **Why 4 repetitions:** fewer objects than Exp. 1a (16 vs. 36 pairs), so they are repeated more to reach enough trials.

#### 4.6 Counterbalancing (key part)

**Colour <-> size, across observers:**
- **What:** for half of the observers, the rule is reversed (reference objects built from the other colours; separate testing room).
- **Why:** otherwise congruency would be confounded with colour. Blue-red might look bigger or more salient for purely perceptual reasons (brightness, contrast, warmth). With counterbalancing, the SAME display is congruent for one half of observers and incongruent for the other, so any effect of colour itself cancels out.

**Shape <-> colour <-> size, item level:**
- **What:** across observers, each shape appears in both colour schemes and as both implied-big and implied-small.
- **Why:** no specific shape (e.g., a bulkier-looking one) is tied to one condition.

#### 4.7 Data preprocessing

- As in Exp. 1: exclude errors and RT < 200 ms or > 1500 ms.
- 3.7% of trials removed.

### 5. Results (paper)

**Main task:**
- Stroop effect: -4 ms, SEM = 3, d = -0.3, F = 1.7, p = .21 (ns).
- "Smaller" task: -12 ms, SEM = 6. "Larger" task: +4 ms, SEM = 7.
- Task x congruency: ns (F = 1.9, p = .19).
- Direction: 7 of 17 observers in the expected direction, 10 opposite.

**Between-experiment comparison (Exp. 1a vs. Exp. 3):**
- Main effect of congruency: F = 25.1, p < .001.
- Experiment x congruency interaction: F = 36.7, p < .001. Familiar objects: 38 ms (SEM 6); bicolor objects: -4 ms (SEM 3).
- Two-sample t-test: t(32) = 6.06, p < .0001.
- No difference in overall RT between experiments (F = 0.4, p = .53).

**Between-experiment comparison (Exp. 1b vs. Exp. 3):**
- Main effect of congruency: F = 12.6, p < .001.
- Familiar vs. bicolor (overall RT): F = 3.2, p = .09.
- Interaction: F = 27.2, p < .001.
- Two-sample t-test: t(31) = 5.21, p < .0001.

**Authors' conclusion:** explicitly learned, fact-based knowledge of size (even when known with certainty) is not sufficient to produce a detectable Stroop effect. More extensive experience and learning is required for known size to have a strong, automatic impact (supports account 1).

### 6. Weaknesses to keep in mind

1. No manipulation check: the paper says observers "know this rule with certainty", but no test of rule knowledge is reported.
2. The between-experiment comparison confounds many differences. Familiar objects vs. block objects differ not only in experience but also in:
   - diversity (36 different categories vs. homogeneous block world);
   - size being coded by COLOUR (a separate feature) rather than by object identity;
   - having a name / basic-level category (a "chair" has one, a block object does not);
   - photos vs. renders, different participants, different stimuli.

   So "experience is required" is one possible explanation. An alternative: size must be a property of the object's category, not of an arbitrary feature.
3. "Smaller" task: -12 ms, SEM 6 (t ~ -2), a near-significant REVERSE effect in one task, not discussed. Probably noise (interaction ns)..
4. Power analysis is based on Exp. 1 variance rather than on a pre-specified smallest effect of interest. TOST would be stricter, though the CI in 3.2 gives a similar conclusion.
5. df mislabelled in all ANOVAs

### 7. Implications for our study (N = 5)

**Main problem:** the key result is a NULL, and a null is hard to establish with N = 5.

**What is still possible:**
- In Exp. 3 the between-person SD of the effect is small (~12 ms). At N = 5 the expected 95% CI is about +/- 15 ms.
- CAN show: the effect is smaller than for familiar objects (~38 ms); such an effect would be excluded.
- CANNOT exclude an effect of the Exp. 2 magnitude (~17 ms).
- CANNOT claim there is no effect at all.

**Best option with our resources:**
- Run the SAME 5 participants in both Exp. 1 and Exp. 3. The familiar vs. rule-learned comparison then becomes WITHIN-subject, which is much more powerful than the between-subject comparison in the paper. The paper's main contrast can be tested in every person.
- Order: Exp. 3 first, then Exp. 1, so participants do not guess the hypothesis from familiar objects. (Counterbalancing order is possible but gives unequal groups at N = 5.)
- Colour-size counterbalancing at N = 5 will be 3 vs. 2. Not ideal, but acceptable if reported.

**Cost:** highest of the three experiments.
- Physical block objects (big one ~120 x 75 cm), two reference sets (both colour schemes).
- 32 stimuli in two colour versions (LEGO Digital Designer is no longer supported; BrickLink Studio is an alternative???; check whether the stimuli are available on Konkle's website).
- ~30 min one-on-one familiarization per participant.

### 8. Decision summary (Exp. 1-3)

**What each experiment answers:**
- Exp. 1: Is real-world size accessed automatically? (core claim)
- Exp. 2: Is direct comparison of two objects necessary?
- Exp. 3: Is a learned rule sufficient, or is experience needed?

**Exp. 1: CANNOT be dropped.**
- Core claim; Exp. 2-3 build on it.
- The only experiment with a realistic chance of a reliable result at N = 5.
- 1a only: larger effect (38 ms), higher power; pixel-area confound remains.
- 1b only: stricter control, but smaller effect (21 ms) and fewer trials (160/condition); per-person power ~50-60%, risky at N = 5.
- Best: both on the same participants (~30 min total).

**Exp. 2: CAN be dropped.**
- At N = 5 almost certainly uninformative (power ~20-33%).
- Narrow question (conditions of the effect, not the effect itself).
- Its key control (hidden Stroop) is a null that cannot be interpreted at N = 5.
- Cost of dropping: cannot rule out that the effect depends on pairwise comparison (state as a limitation).

**Exp. 3: CAN be dropped, but it is a substantive loss.**
- Most expensive; key result is a null; unequal counterbalancing.
- Cost of dropping: lose the theoretical part of the paper. We would replicate the fact ("the effect exists") but not the explanation ("it requires experience, not rule knowledge").

**Options:**
- **Minimal:** Exp. 1a + 1b. Replicates the core finding, ~30-40 min per participant.
- **Extended:** Exp. 1a + 1b + 3 on the same participants. Replicates both the fact and the explanation; heavy preparation.
- **Exp. 2:** not recommended at N = 5; better to spend the time on more trials in Exp. 1
