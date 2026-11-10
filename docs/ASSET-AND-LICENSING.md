# Third-party assets and licensing review

This game contains original team work alongside software, media and fonts obtained from third parties.

## Assets included in the publication archive

- **65 images:** retained from the 2024 group project.
- **10 audio files:** retained from the group project. The original report refers to Pixabay as one source of sound effects.
- **SugarCube and macro code:** the bundled `index.html` retains upstream code and in-file attribution. The original project used open-source story-format and macro components; their original notices should be preserved.


## Font assets omitted

The original archive contained seven font files: `Neothic.ttf`, `ancientscript.ttf`, `Social-Media-Circled.otf`, and four `OpenDyslexic-*.otf` styles. **Those font binaries are intentionally not redistributed in this package.** CSS references to them remain in the unmodified game files; browser/system fallbacks are used in their absence.

If you want to restore the original typography, obtain or copy the relevant font files yourself **only after confirming the licence for the specific font files and any required licence notices**. Preserve their exact original filenames under `fonts/`. Rights can differ between versions and distribution sources.

- [OpenDyslexic official site](https://opendyslexic.org/) states that the current font is distributed under the SIL Open Font License; verify the terms applicable to the exact archived binaries.
- Other display fonts have varying third-party licensing claims; do not assume bundling is permitted without evidence from the relevant rightsholder/distributor.
- The game's external Linearicons stylesheet and Google Fonts requests may fail when offline; those services are not required for the basic branching story, but they affect presentation.

## Collaboration and software licence

The source and game are the result of a group assignment.

For project identity and original-file handling, see [PROVENANCE.md](PROVENANCE.md).
