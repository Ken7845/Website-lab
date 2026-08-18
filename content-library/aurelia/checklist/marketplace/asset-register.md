# AURELIA Asset and License Register

Status: **Release blocked until every `Unverified` license row is resolved.**  
Canvas readback: 2026-08-16. Framer delivery URLs identify the file currently on the Canvas; they are not evidence of original authorship or Marketplace redistribution rights.

## Fixed Canvas image assets

| Asset / Canvas usage | Current Framer delivery URL | Original source and redistribution license | Alt owner | Buyer replacement path |
|---|---|---|---|---|
| Chef Portrait — Home | `AZwvKmPt6EEVg8dGNK44wmOjEJs.webp` | Unverified | Image layer / page audit | Replace Home image and its Alt together |
| AURELIA Exterior — Home | `nrzp97zHgqaXxZcyEs3NtQoEE2A.webp` | Unverified | Image layer / page audit | Replace Home image and its Alt together |
| AURELIA Dining Room — Home; Private Table — About | `wfFGRrcrYTrshOk6UQRTl7ExJwk.webp` | Unverified | Image layer / page audit | Replace affected page image and its Alt together |
| Craft Detail — Home | `TTX9xStWIOXWlTvkJ8w7pZ6aiKM.webp` | Unverified | Image layer / page audit | Replace Home image and its Alt together |
| Hero — Home; Exterior — About | `FTczavwDHMzsdhFLYo7uDeq8hWY.webp` | Unverified | Home Hero has explicit Alt; About requires replacement check | Replace per-page image and Alt together |
| Opening Menu Image — Menu | `5agHXLkAkWA4wATr6APoN6SDLIU.webp` | Unverified | Image layer / page audit | Replace Menu image and its Alt together |
| Kitchen Image — Menu | `pIyZ5Q2OQly5SCHLyeVmWexzJU.webp` | Unverified | Image layer / page audit | Replace Menu image and its Alt together |
| Food Plating Image — About | `8QxWbHKnoMcwO7h7y2UK5nrASQ.webp` | Unverified | Image layer / page audit | Replace About image and its Alt together |
| Handheld Dish Image — About | `LPotbMcojjsLOwu0CiqF9LxSLQ.webp` | Unverified | Image layer / page audit | Replace About image and its Alt together |
| Table Setting — About, Home Experience, EveningChapterRow | `utD9JrakIQWhi1wCW9BRXApOfLA.webp` | Unverified; original filename reports `pexels-lu-pir-515205238-16413122.webp` | `EveningChapterRow` → `Chapter Image Alt`; page images need final audit | Replace each page/component image and Alt together |

## Component image assets

| Component | Current image entry | Image delivery/original file clue | Alt owner | Status |
|---|---|---|---|---|
| DishSelector | Dish 01–07 Image | 7 current files; dimensions range from `1600×900` to `6199×8265` | `Dish 01–07 Image Alt` | Source/license/weight unverified; test portrait and landscape replacement |
| MenuDishCard | Dish Image | `pIyZ5Q2OQly5SCHLyeVmWexzJU.webp` (`5501×4401`) | `Image Alt` | Source/license/weight unverified |
| ChefStoryRow | Portrait | `chefs-portrait-01.webp` (`3589×5383`) | `Portrait Alt` | Source/license/weight unverified |
| EveningChapterRow | Chapter Image | `pexels-lu-pir-515205238-16413122.webp` (`6000×4000`) | `Chapter Image Alt` | Confirm original Pexels license and Marketplace redistribution position |
| ChapterCursorPreview | Arrival / First Plates / From the Kitchen / After Preview Image | Four `aurelia-chapter-*.jpg` files (`1000px` long edge) | Pending explicit decorative decision | Determine whether these cursor-only images should use empty Alt or be hidden from assistive technology |

## Fonts and external components

| Asset | Current use | License / buyer setup | Release action |
|---|---|---|---|
| Inter | Body/interface text | Verify current license and bundled/hosted behavior | Record source and whether buyer setup is required |
| League Gothic | Display typography | Verify current license and bundled/hosted behavior | Record source and whether buyer setup is required |
| Science Gothic | Display/brand typography | Verify current license and bundled/hosted behavior | Record source and whether buyer setup is required |
| Lenis | Smooth scrolling external Marketplace component | Free Marketplace content is not automatically redistributable inside a competing Marketplace template | Obtain the original creator's explicit template-redistribution permission, or remove/replace before release |
| Text Reveal on Scroll | Text motion external Marketplace component | Free Marketplace content is not automatically redistributable inside a competing Marketplace template | Obtain the original creator's explicit template-redistribution permission, or remove/replace before release |

## Marketplace component redistribution rule

Framer's Community Terms permit Free Content in an end user's own commercial project or client work, but prohibit using that Free Content to create or offer templates, components, or design assets that compete with Framer Community. AURELIA is intended to be a Framer Marketplace template, so a free Marketplace component may remain only if its original creator provides a separate, explicit right to redistribute it within a Marketplace template (or if Framer confirms a different first-party license for that exact component).

Record the original component listing URL, creator name, license text, and written permission here before clearing either external-component row. Do not treat the `Copy Component` action or a free price as that permission.

## Required evidence to clear the blocker

- [ ] Original creator/source URL or invoice for every shipped image.
- [ ] License terms that explicitly permit inclusion and redistribution in a paid or free Framer template.
- [ ] Original font source/license and buyer setup requirement.
- [ ] Encoded file weight and target display dimensions for each image; replace or optimize oversized files.
- [ ] External-component license/compatibility and Reduced Motion evidence.
- [ ] Final Alt decision and replacement test recorded for every meaningful image.
