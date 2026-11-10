# Source provenance and publication decisions

## Original source

This package was assembled from a retained snapshot of the group's 2024 Twine game. The archive contained `Home.twee`, `index.html`, image, audio and font directories, plus an embedded Git metadata directory and macOS-generated artifacts.

## Copied unchanged

- `Home.twee`
- `index.html`
- All non-hidden files in `images/` (65)
- All non-hidden files in `music/` (10)

The SHA-256 checksums of the above files match the byte sequences found in the source ZIP. A manifest accompanies this package.

## Not included

- The extracted `.git/` directory and its commit/remote metadata: this publication does not transplant repository history.
- `.DS_Store`, `__MACOSX/` and resource-fork metadata: operating-system artifacts not required by the project.
- Original font binaries: see the [asset and licensing review](ASSET-AND-LICENSING.md).

## Added for publication

- This repository's README and documentation.
- Cropped screenshots from a render of the original compiled game, with no modification to game source or media.
- A standard-library static validation script and checksum manifest.
- `.gitignore` and `.nojekyll` for maintainability and GitHub Pages compatibility.

## Attribution

The work is jointly authored by Leah Weldon, Anthony Rowe, Aoife Hayes, Holly Kennelly, Yuuv Jauhari and Rishi R. Kataria. The submitted group report supplies the roles documented in [CONTRIBUTORS.md](CONTRIBUTORS.md).