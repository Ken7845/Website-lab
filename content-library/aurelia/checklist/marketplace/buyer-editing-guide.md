# AURELIA Buyer Editing Guide — Draft

Status: Draft. This guide describes the current Canvas and flags release items still awaiting verification.

## Start here

1. Replace the demo brand name and logo through the shared Navigation/Footer and `AURELIA` brand-mark component.
2. Update global colors and type through the shared Color Tokens and Text Styles before changing local layers.
3. Replace fictional copy, contact details, imagery, and reservation handling before publishing for a real business.
4. Publish a private Preview and test Desktop, Tablet, and Phone before going live.

## Where to edit

| Need | Current editing location |
|---|---|
| Brand colors and typography | Shared Color Tokens and Text Styles |
| Navigation and footer | Shared `Navigation` and `Footer` components / Template |
| Buttons | `Button` component; choose descriptive diagonal variants |
| Home chapter rows | `EveningChapterRow` instances on Home |
| Home dish sequence | `DishSelector` instance on Home |
| Menu dishes | Seven `MenuDishCard` instances on Menu |
| Chef profiles | Three `ChefStoryRow` instances on Chefs |
| Shared reservation CTA | `Reservation Handoff` instances on Home, Menu, and Chefs |
| Reservation form | Reserve page and `ReservationSubmit` component |
| Reservation FAQ | Eight `FAQ Row` instances on Reserve; edit Question and Answer in instance Properties |
| Missing-page experience | `/404` page |

## Image replacement checklist

- Replace image and its Alt text together when the image conveys information.
- Use empty Alt only for images that are purely decorative.
- Check crop and focal point with both portrait and landscape source images.
- Recheck Desktop, Tablet, and Phone after every replacement.
- Current release note: Home Hero, MenuDishCard, ChefStoryRow, DishSelector, and EveningChapterRow have explicit Alt handling. The decorative/meaningful decision for ChapterCursorPreview still needs completion before release.

## Content limits to test

- Long restaurant and navigation names
- Long dish and chef names
- Body copy at roughly double the demo length
- Empty optional chef role
- Portrait and landscape replacement imagery

## Before publishing

- Replace all fictional operational facts.
- Configure and test the real form destination, privacy copy, and response behavior.
- Add favicon and social/OG image.
- Verify page metadata, links, keyboard behavior, motion preferences, and all responsive breakpoints.
- Confirm asset/font licenses permit template redistribution.

## Intended editing model

Normal content replacement should happen through page instances, shared Styles, and clearly named Properties. Buyers should not need to edit breakpoint replicas or component internals for routine brand, copy, image, or link changes.
