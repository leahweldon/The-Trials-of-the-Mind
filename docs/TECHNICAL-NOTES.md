# Technical notes

## Story and narrative design

The original game was created for TEU00062 to examine user engagement through branching narrative, audiovisual feedback, exploration and consequences of player decisions. The opening passage (`Awakening`) offers multiple choices; one leads to `KeyDiscovery` and further choices involving a key and central podium. The preserved source also contains the Arena, Labyrinth and forest/temple routes.

## What is in the archive

- **`Home.twee`** is the retained Twine source: narrative passages, special passages, JavaScript, CSS and story metadata.
- **`index.html`** is the compiled game. It contains the SugarCube runtime and the game's passages.
- **`images/`** contains 65 files, including the original logo and opponent illustration.
- **`music/`** contains 10 MP3 files.
- **`fonts/`** documents omitted font binaries and restoration conditions.

The source declares SugarCube **2.36.1** and the `Awakening` start passage. It contains 98 unique passage declarations including metadata and support passages, and 154 `[[...]]` wiki-link occurrences.

## Implementation

The team used SugarCube macros for conditional links, gameplay state and non-deterministic transitions. The source includes an inventory setup, audio registration, a custom sidebar, responsive styling, and illustration display. The contemporary report discusses Simple Inventory 3 and Chapel's macro collection.

The report explicitly says inventory usage was rudimentary and a planned battle/rock-paper-scissors mechanism was not finished. These ideas remain design context, not advertised completed gameplay.


## Historical quirks retained

The original `StoryInit` registers a track named `thinking` with the `suspense.mp3` path although a separate `thinking.mp3` asset exists. The source remains unchanged; users seeking a corrected build can review that mapping and rebuild consistently from the source.

Some visual elements depend on third-party stylesheets and font files. See [asset review](ASSET-AND-LICENSING.md).

## Local verification

```bash
python3 tests/verify_project.py
python3 -m http.server 8000
```

The validator is a static integrity test, **not** a complete browser end-to-end test.
