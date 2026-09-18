---
name: review-manga-storyboards
description: Review manga/comic storyboards against their source prose or script, with filename-based natural page order and explicit right-bound, right-to-left reading. Use for thumbnail, name, rough storyboard, or finished comic page image sets when checking panel and balloon order, composition, negative space, camera choices, visual flow, panel-to-panel beats, pacing, staging, continuity, dialogue, adaptation choices, or requested draftsmanship issues. Do not use for generating or redrawing comic art.
---

# Review Manga Storyboards

Review the pages as a reader first, then as an adaptation editor. Keep observations, uncertain readings, and recommendations distinct.

## 1. Establish the inputs

Identify:

- the directory or files containing storyboard pages;
- the reading direction;
- the corresponding prose, script, or canonical project text;
- the user-designated source of truth: storyboard, manuscript, or neither;
- whether the supplied pages are a complete scene or a partial batch.

Honor the user's authority decision above all project naming conventions. If the storyboard is authoritative, review its internal logic and comics craft as canon; classify differences in prose as **manuscript sync items**, not storyboard errors. If the manuscript is authoritative, conflicting storyboard beats may be revision issues. If neither is designated, report the alternatives neutrally and ask for a decision only when it materially changes the recommendation.

Default to the user's stated direction. For a right-bound manga workflow, use these rules unless the user overrides them:

- Sort pages by filename using natural numeric order: `1, 2, ... 10`, never lexical order `1, 10, 2`.
- Treat the filename as the page number; ignore modification time, EXIF order, and directory listing order.
- Read page bands from top to bottom.
- Within the same band, read panels from right to left.
- Within a panel, read vertical balloons and text from right to left; read each vertical text column from top to bottom.
- Use balloon tails, character positions, and conversational logic to identify speakers. Mark ambiguous speakers rather than guessing.

Run the bundled manifest script before visual review:

```bash
python3 scripts/storyboard_manifest.py /path/to/pages
```

Resolve relative script paths against this skill directory.

## 2. Locate the matching source text

Use a source path supplied by the user when available. Otherwise:

1. Search the workspace with `rg` using the scene name and two or three distinctive dialogue fragments.
2. Prefer a project index or README that identifies the canonical manuscript.
3. Prefer files explicitly named as current正文, manuscript, or script over backups, raw exports, discussion logs, and derivative copies.
4. If multiple plausible versions differ, name them and state which version is used. Do not silently combine versions.
5. Read enough text before and after the matched passage to catch setup and later payoffs.

Record the exact source path and line where the scene starts. Treat prose as evidence, not as an automatic command: an adaptation may improve on it, but causal and continuity changes must be called out.

## 3. Build a reader-order map

Inspect every page at sufficient resolution. For each page, note:

- panel order in actual reading order;
- balloon/dialogue order and speaker;
- the dramatic beat delivered by the page;
- the final image or line before the page turn;
- any text or staging whose reading is uncertain.

Also inspect every panel as part of the page's visual route:

- where the dominant face, hand, prop, or other focal subject sits;
- where negative space is held and whether it invites balloons, isolates a figure, delays information, or changes emotional pressure;
- how faces, gestures, value contrast, motion vectors, panel borders, and balloons hand the eye to the next panel;
- whether the resulting whole-page path supports the intended right-to-left order or tempts the eye to skip ahead.

Do not treat correct panel geometry as proof of correct flow. A high-contrast shape, large face, or isolated balloon can override the nominal order. Conversely, an unusual path may be successful when it deliberately creates interruption, simultaneity, or unease. Describe the experienced path and its narrative effect before recommending normalization.

Test the page without relying on knowledge from the manuscript. A page fails flow if the intended order only becomes clear after reading the source.

Before declaring a page's flow sound, audit every row of side-by-side panels: state the first balloon in the right panel, then the first balloon in the left panel, in that order. This literal playback must not produce an answer before its question or a reaction before its cause. Zoom or crop rough handwriting when needed; if words remain illegible, report the uncertainty instead of passing the row.

Include a compact **讀序抽查** in the report for every page containing side-by-side dialogue, even when the row passes. Use `pN: 右「首句片段」→ 左「首句片段」` and label illegible fragments `不確定`. Do not replace this evidence with a general claim that the pages read smoothly.

Check especially for:

- an answer placed before its question;
- a balloon that pulls the eye into the wrong panel;
- crossed or missing tails;
- two same-height panels that imply the wrong right-to-left order;
- focal art on the left that makes the eye skip the rightmost starting panel;
- an important reveal exposed before the page turn;
- a silent reaction that is too small, too early, or emotionally ambiguous.

## 4. Compare storyboard and source beat by beat

Create an internal ledger with these statuses:

- **Match**: same action, information, and consequence.
- **Adaptation**: phrasing or staging changes while function and continuity remain intact.
- **Addition**: new material; judge whether it clarifies, slows, or changes intent.
- **Omission**: a source beat is absent; judge whether it is expendable or required for payoff.
- **Conflict**: motive, chronology, rule, prop, speaker, or consequence contradicts the source or later continuity.
- **Unclear**: the rough art or handwriting does not support a reliable conclusion.

Apply authority after identifying a conflict:

- **Storyboard authoritative**: keep the storyboard beat; point to manuscript lines that must be updated. Do not put the storyboard under **Must fix** solely for disagreeing with prose.
- **Manuscript authoritative**: recommend the smallest storyboard change that restores the source's causal chain.
- **No authority designated**: explain the narrative effect of each version without choosing silently.

Prioritize causal continuity over verbatim fidelity. Verify:

- setup and payoff objects;
- decisions and their stated rules;
- who knows what and when;
- whether an encounter is accidental or planned;
- repeated motifs and later callback dialogue;
- action geography, handedness, props, costume, and screen/phone state;
- emotional state shown by pose, eye line, hands, and reaction timing.

Do not label a beat omitted merely because a partial batch ends before it. If the storyboard depicts closure—such as ending a call, leaving the location, or cutting to the next scene—then a missing required beat is a real omission.

## 5. Judge composition, camera, and comics craft

Review at rough-storyboard altitude. Focus on choices that would be expensive to fix after pencils:

- page and panel rhythm;
- right-to-left eye path;
- balloon placement and text density;
- establishing geography and 180-degree continuity;
- shot-size variation and repeated talking heads;
- reaction-shot duration;
- page-turn suspense or impact;
- focal hierarchy and silhouette clarity;
- whether the image adds information instead of merely duplicating dialogue.

For every panel, identify the camera choice internally even when it does not need to be listed in the final report:

- shot size: insert, extreme close-up, close-up, medium, full figure, or wide/establishing shot;
- viewpoint: high angle, low angle, eye level, overhead, frontal, profile, rear, over-the-shoulder, or another materially relevant orientation;
- dramatic function: distance, exposure, dominance, vulnerability, intimacy, surveillance, disorientation, or withheld information.

Then read each transition from the preceding panel as a beat. Useful descriptions include continuation, tightening, hold, interruption, release, reveal, punch, or deliberate rupture. Judge whether the transition feels continuous, abruptly cut, suspended, or like a breath, and whether that sensation serves the scene. Do not infer meaning from an angle in isolation; evaluate it with character blocking, eye lines, shot scale, and the panels before and after it.

Surface composition and camera findings selectively. For a short batch or a request centered on visual language, a compact page-by-page sweep is useful. For a long batch, report the patterns and the panels where they materially affect reading, pacing, or emotion rather than producing a mechanical catalog.

Do not critique draft line quality unless it prevents reading the panel, character, prop, or expression.

## 6. Optional draftsmanship check

Enable this only when the user explicitly asks for a drawing, anatomy, face, or sketch check. A general storyboard review does not activate it.

When enabled:

- inspect concrete construction issues such as facial centerline and feature alignment, skull/jaw/neck connection, eye and ear placement, foreshortening, high- or low-angle perspective, limb proportion, hand contact, and pose balance;
- locate every note by page and panel, describe the visible symptom, and give the smallest useful correction direction;
- distinguish a drawing problem from a staging or silhouette problem;
- respect intentional stylization and asymmetry;
- do not use vague judgments such as "the anatomy is off" or expand into a general rendering critique.

When disabled, mention draftsmanship only when the image cannot be reliably read, and frame it as a readability uncertainty.

## 7. Report by revision priority

Lead with a concise verdict. Then report:

1. **Must fix** — contradictions, broken reading order, missing causal beats, or unusable page turns.
2. **Worth adjusting** — pacing, staging, balloon clarity, or emotional emphasis.
3. **Already working** — successful page turns, reactions, motifs, and visual compression.
4. **Page notes** — only pages with actionable or especially successful decisions.
5. **Composition and camera** — explain the important whole-page eye paths, framing patterns, and panel-to-panel beats; use a compact page sweep when visual language is the focus.
6. **Source comparison** — cite the manuscript path, state which artifact is authoritative, and distinguish canon decisions from reviewer inference.
7. **讀序抽查** — show right-panel-to-left-panel first-balloon evidence for every side-by-side dialogue row.
8. **Draftsmanship** — include only when the optional check was explicitly requested.

For every criticism, give a concrete revision direction. Prefer the smallest fix that preserves strong existing pages. If dialogue is uncertain, quote only the confidently legible part and label the rest uncertain.

Respond in the user's language; use Traditional Chinese when the request is in Traditional Chinese. Do not edit the manuscript or image files unless the user explicitly asks.
