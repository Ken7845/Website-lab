# Dutch Treat Restaurant Demo — Handoff

## 1. Project Reference

- Project type: local restaurant website demo
- Framer project: [Dutch Treat Restaurant](https://framer.com/projects/Dutch-Treat-Reataurant--uzIjvVnkTygP0HFIE6UL-fymea)
- Main content folder: `content-library/dutch-treat-restaurant/dutch-treat-rrestaurant/`
- Image folder: `content-library/dutch-treat-restaurant/dutch-treat-rrestaurant/images/`
- Primary pages: Home, Menu, Gallery, Contact
- Duplicate Menu, Gallery and Contact pages were identified during the project. The intended public pages are `/menu`, `/gallery` and `/contact`; duplicate `-2` pages should remain draft or be removed only after verification.

## 2. Project Goal

The demo should present Dutch Treat as a friendly, established neighborhood restaurant in Lynden rather than a polished luxury restaurant or generic AI-generated hospitality template.

The experience should communicate:

- generous breakfast and comfort food;
- an approachable local-diner personality;
- a sense of place and real restaurant atmosphere;
- practical information that helps visitors decide, browse the menu and plan a visit;
- clear calls to action without becoming sales-heavy.

## 3. Requirements and Feedback Emphasized During the Project

### Information architecture

- Do not keep vague or redundant sections such as “Restaurant Introduction” and “Menu Highlights” when they do not serve a clear user task.
- The homepage menu area should be an entry to the full Menu page.
- Menu content must be extracted from menu screenshots and rebuilt as readable text. Do not use photographed menu pages as the main reading interface.
- Gallery must be a real page with meaningful categories, not an unstructured image dump.
- Gallery access must appear in both navigation and the homepage “Food and Atmosphere Gallery” section.
- Avoid duplicate Menu, Gallery and Contact pages.
- Footer should contain detailed restaurant information, especially address, hours, contact and useful page links.

### Hero

- Hero content must not cover the building or other important photographic subjects.
- This is especially important on mobile, where a desktop overlay can obscure nearly the entire image.
- CTA hierarchy should prioritize useful restaurant actions.
- The former “Get Directions” primary CTA was replaced with “Reserve a Table.”
- Navigation and Hero both include a reservation CTA that scrolls to the reservation section.

### Gallery

- Categories currently used: Breakfast Favorites, Fresh Donuts and Dining Room.
- Never leave empty category containers above the real categories. Duplicate empty category structures caused large blank areas during iteration and must be checked after every batch edit.
- Gallery composition should not become a rigid set of identical boxes.
- Desktop may use varied spans and cropped proportions to create rhythm.
- Tablet should simplify the cross-column relationships.
- Phone should usually use a clear single-column sequence with separately calibrated heights.
- The homepage four-image food gallery should retain an editorial, asymmetrical composition on desktop rather than a mechanical equal grid.

### Reviews

- Google review screenshots are sources, not final UI elements.
- Extract the visible review text and rebuild it as real typography.
- Extract the associated food photo separately.
- Do not place Google avatars, star bars, share controls, app icons or the entire screenshot inside the review card.
- Current review sources:
  - Review 02: Chris Campos; burger, hot dog and fries.
  - Review 03: Gerald Patterson; breakfast plate with eggs, hashbrowns, toast and large sausages.

### Visit section

- The Visit Us exterior visual was changed to `google-exterior-04-angled-daylight-screenshot.png` using a cleaned crop for the website.
- Preserve the restaurant building, entrance and recognizable signage when selecting the crop.

### Reservation preview

- A “Reserve a Table” section was added to the homepage.
- It currently shows a visual reservation experience only; no form submission is connected.
- Displayed fields include name, party size, date, time, and phone or email.
- Navigation and Hero CTAs scroll to this section.
- Desktop uses an introduction/form two-column layout.
- Tablet uses a tighter two-column layout.
- Phone uses a single-column layout with vertically stacked fields.

### Interaction

- Buttons need clear hover feedback.
- Avoid hover scaling in constrained areas such as the footer, because enlarged content can be clipped by its frame.
- Prefer small color, opacity or shadow changes; if scale is used, keep it subtle and verify overflow.

## 4. Image Strategy Learned

The governing rule is **content expression first**, not “always crop” or “never crop.”

Before setting an image container, identify what the image needs to communicate:

- the complete dish and important sides;
- the building entrance and signage;
- a meaningful interior relationship;
- readable factual text when the image is being used as a source.

Cropping and cover behavior are appropriate when the important content remains clear. Mixed aspect ratios, controlled zoom, cross-column images and asymmetric grids are encouraged when they improve composition without damaging meaning.

Do not crop when it would:

- cut through the principal dish;
- remove important sides or context;
- hide the restaurant entrance or sign;
- destroy an interior spatial relationship;
- conceal text required for factual extraction.

“Preserve the content” does not mean every image must use `contain`, its native aspect ratio or the same box size. Each breakpoint needs a fresh composition decision.

## 5. Source Image Organization

Facebook images were renamed by subject and should be preferred for polished food presentation:

- `facebook-brand-*`
- `facebook-breakfast-*`
- `facebook-donuts-*`

Google screenshots were retained as source/reference material and classified as:

- `google-menu-*`
- `google-food-*`
- `google-interior-*`
- `google-exterior-*`
- `google-review-*`
- `google-contact-*`
- `google-listing-*`
- `google-collage-*`

Files containing Google UI remain screenshots even when their subject is useful. Extract or clean the needed content before website use.

## 6. Mandatory Image Inspection Workflow

- Never open full-size source images directly with a visual inspection tool.
- Never place several originals into model context at once.
- First create compressed derivatives with a longest edge no greater than 1200px and JPEG quality around 50–60%.
- Build one contact sheet no larger than 1MB.
- Inspect no more than one compressed contact sheet per round.
- Preserve all originals; write crops, cleaned images and uploads to a separate working directory.
- For OCR and review extraction, screenshots may be processed programmatically, but only compressed derivatives or a compliant contact sheet should be visually inspected.

This workflow was introduced after several reconnects and long-running image uploads significantly reduced project efficiency.

## 7. Responsive Rules

Every major page and section must be checked independently on Desktop, Tablet and Phone.

- Do not assume Framer breakpoint propagation produces an acceptable composition.
- Re-read each replica after creating or moving complex structures.
- Desktop cross-column spans must be reset or simplified on Tablet.
- Single-column mobile galleries should use vertical stacks rather than a one-column grid when possible.
- Long headings, card padding, image height and button labels must be reduced deliberately on smaller screens.
- Mobile navigation should not retain a wide desktop link group alongside the primary CTA.
- After changes, check for duplicate propagated nodes, empty containers, inherited grid spans and stale fixed heights.

## 8. Problems Encountered and Lessons

### Duplicate propagated structures

Batch creation across Framer breakpoints produced duplicate Gallery categories and duplicate CTAs more than once. Empty category grids appeared above the real photo categories and looked like unexplained whitespace.

For future work:

1. Create the base structure once.
2. Immediately read Desktop, Tablet and Phone replicas.
3. Count children and confirm which containers actually hold content.
4. Delete empty duplicates before styling.
5. Avoid rerunning a creation script after an uncertain timeout without first reading the canvas.

### Upload and reconnect problems

Large PNG screenshots and sequential uploads sometimes exceeded the connection window. Some writes succeeded even when the command returned no useful output.

For future work:

- create web-sized JPEG derivatives before uploading;
- upload a small, named batch;
- store returned URLs in session state;
- check session state and live nodes before retrying;
- use fresh Framer sessions after the relay connection becomes stale;
- never interpret silence as proof that a write failed or succeeded.

### Mechanical image fitting

An attempted correction interpreted “do not crop away content” as “show every image at its full native ratio.” This created oversized, rigid layouts and removed the editorial rhythm the user preferred.

The correct principle is to preserve meaning while using intentional cropping and varied proportions where safe.

## 9. User Design Preferences Learned

- Prefers websites with strong art direction but practical usability.
- Dislikes generic AI-template sections, vague headings and unnecessary explanatory content.
- Prefers real brand content over invented storytelling.
- Wants clear information hierarchy and purposeful CTA placement.
- Likes editorial image composition with controlled variation rather than repetitive card grids.
- Notices excessive whitespace, empty containers and weak section transitions quickly.
- Expects typography, spacing and composition to feel intentional at every breakpoint.
- Prefers a warm, honest and local brand voice rather than luxury language or exaggerated marketing copy.
- Wants design decisions to be explained by what they help the visitor understand or do.

## 10. Recommended Workflow for the Next Bakery Demo

1. Read repository `AGENTS.md` completely.
2. Read the current taste skill completely.
3. Read the bakery brief, brand voice, style guide and available content.
4. Inventory and rename images before entering Framer.
5. Generate one compliant contact sheet for classification.
6. Define the bakery’s visitor tasks before choosing sections: browse products, understand freshness/craft, find hours/location, place an order or request a custom order.
7. Decide the page map and CTA hierarchy before building.
8. Build Desktop first, then deliberately adapt Tablet and Phone.
9. For product galleries, combine image ratios based on subject integrity rather than forcing equal boxes.
10. Treat screenshots as source material; extract text and photos instead of embedding external-app UI.
11. Add hover behavior only after layout and overflow are stable.
12. After every structural Framer operation, read back all breakpoints and check for duplicates before continuing.

## 11. Current Scope Boundary

- The reservation section is a visual prototype only.
- No reservation backend, validation, confirmation state or external booking service is connected.
- Do not imply that reservations can currently be submitted.
- Publishing was not requested as part of this handoff.

