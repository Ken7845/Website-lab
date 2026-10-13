# REX Construction — Workflow Observations

## 2026-10-13 — Responsive homepage build

- Task reference: REX Construction Home U1–U3
- Request: Plan and build the REX homepage in Framer using the official website copy, organized local assets, a dark theme and bright hover highlights.
- Route selected: project entry → official Framer connection/task map → visual direction contract → `framer-components` → targeted image/layout references → `framer-qa`
- Actions: Built native color/text styles, an editable Inspection Button with gesture states, responsive Home sections, real links, metadata and Desktop/Tablet/Phone breakpoints using five approved assets.
- Verification: Clean final diagnostics; structural readback at 1200/810/390; full-page Desktop and Phone screenshots; preview readiness returned ready with no errors or warnings.
- Outcome: Partial — structural and visual Pass; runtime hover/focus/click proof and separate 320/1440 visual evidence unavailable.
- Later-discovered issue: None
- Correction: None
- Workflow candidate: Preview readiness may return no staging URL when staging is disabled; record runtime paths as Blocked instead of treating readiness as interaction proof.

## 2026-10-13 — Shared shell and trust revision

- Task reference: REX Construction Home U4
- Request: Repair Navbar/Footer component and responsive ownership, replace Confidence with a badge ticker, and add a Contact image.
- Route selected: live definition/instance/breakpoint audit → request contract → `framer-components` → native variants/effects → targeted visual QA
- Actions: Created native Site Navbar, Site Footer and Trust Bar components; added explicit Phone Closed/Open menu actions; used all five supplied badges in a duplicated native loop track; added a distinct project image to Contact.
- Verification: Definition → instance → breakpoint readback; Navbar state screenshots; focused Trust/Contact/Footer screenshots; structural evidence at 1200/810/390; preview readiness returned ready with no errors or warnings.
- Outcome: Pass for the authorized revision; live runtime click/focus proof remains unavailable because staging is disabled.
- Later-discovered issue: Multi-node insertion placed Trust before Hero and Footer before Contact; the first Contact photo contained a white capture artifact.
- Correction: Restored the canonical section order and replaced the photo with `home-with-roof-sign.webp`, then repeated bounded visual review.
- Workflow candidate: When inserting several replacements into one parent, calculate indexes against the post-insert tree or move the replacements to canonical positions before visual QA.

## 2026-10-13 — U5.1 Navbar, button, reviews and counters request

- Task reference: REX Construction Home U5, prompt 1
- Request: Use Submit Roofing as a reference for the Navbar and Phone Drawer; add a filling button hover; turn Reviews into a card selector from `reviews.md`; add Hero counters for Years of Experience, Roofs Installed and Client Rating.
- Route selected: reference-project readback → request contract → `framer-components` → advanced Counter pattern → `framer-qa`.
- Actions: Reorganized the Phone Drawer; created the reusable button filler and Review Selector; registered the reusable `Counter.tsx` component. Counter instances were held pending source-backed metric values.
- Verification: Component and catalog readback, selector and button state screenshots, full Desktop/Phone screenshots, and Framer preview readiness with no errors or warnings. Metric values and live runtime interactions were not verified.
- Outcome: Partial — the reusable design pieces were implemented, but the numeric Hero claims remained unapproved.
- Later-discovered issue: `reviews.md` was initially empty, and later prompts refined the selector behavior, CTA destination, and card sizing.
- Correction: Follow-up prompts supplied the review source and specified the later selector and CTA behavior; see U5.2, U5.4 and U5.6 below.
- Workflow candidate: Confirm source-backed numeric claims before placing them in reusable proof components.

## 2026-10-13 — U5.2 Phone navigation, Yellow filler and review-source follow-up

- Task reference: REX Construction Home U5, prompt 2
- Request: Remove Phone row hover; use the now-saved reviews; remove the button shadow; use a radius-matched Yellow filler moving left to right; add Yellow-filled Desktop navigation hover and white CTAs for Services, Selected Work and About Rex.
- Route selected: active request contract → `framer-components` → targeted component and breakpoint QA.
- Actions: Removed Phone row hover; configured the Yellow button filler and Desktop navigation hover; applied white CTA treatments to the requested sections; used the six saved reviews in the selector.
- Verification: Navbar/button definition readback, review-state mappings, component Hover screenshot, and Desktop/Phone captures. Live runtime interaction proof was unavailable because staging was disabled.
- Outcome: Partial — the requested treatments were added, while later prompts further corrected the button variant and radius requirements.
- Later-discovered issue: The next prompt clarified that the white treatment should be a variant of the existing Button rather than a separate component.
- Correction: The project record still describes a separate White Button component; this task history preserves the user’s correction, but does not claim that component-ownership issue was resolved.
- Workflow candidate: Record component ownership corrections separately from visual-state corrections.

## 2026-10-13 — U5.3 Square surfaces and existing Button variant correction

- Task reference: REX Construction Home U5, prompt 3
- Request: Remove radius from cards and buttons, and make the white treatment a variant in the existing Button component rather than a separate component.
- Route selected: follow-up request contract → existing Button and card component review.
- Actions: Updated the requested direction to square cards/buttons and an existing-Button variant. The following prompt restored radius specifically for the button and its filler.
- Verification: The later component readback covered button variants and screenshots; no standalone verification for this intermediate square-radius state was recorded.
- Outcome: Superseded — the next prompt revised the button/filler radius requirement.
- Later-discovered issue: The final project record names a separate White Button component, which conflicts with this prompt.
- Correction: No evidence in the referenced task confirms that the separate component was consolidated into the existing Button.
- Workflow candidate: Check component reuse after a user corrects the requested component structure.

## 2026-10-13 — U5.4 Review selector behavior, drawer row and filler geometry

- Task reference: REX Construction Home U5, prompt 4
- Request: Add arrow navigation beside the review card, abbreviate long excerpts, use a Button filler at L:-1px and 101% hover width, and make a text-row component for the Phone Navbar.
- Route selected: review-selector and Navbar readback → `framer-components` → targeted state and responsive QA.
- Actions: Built the six-state arrow selector; retained abbreviated review text; applied the filler geometry; used the reusable Phone navigation row. The next prompt later specified that “Read full review” should navigate to the Reviews page instead of expanding the full text.
- Verification: Selector mappings, component screenshots, and full Desktop/Phone screenshots; preview readiness returned no errors or warnings.
- Outcome: Partial — the selector and component work were implemented, while the full-review action was subsequently changed to a page link.
- Later-discovered issue: The in-card action still expanded the full-review variant, and the first card widths overlapped.
- Correction: U5.6 replaced the expand action with a `/testimonials` link and fixed the card width.
- Workflow candidate: Verify component-level width ownership when multiple card variants overlay.

## 2026-10-13 — U5.5 Image radius, filler documentation and native slideshow question

- Task reference: REX Construction Home U5, prompt 5
- Request: Remove radius from page images and frames; document the -1px initial filler position and 101% hover width in the repository; explain the native Framer image-switching approach before implementing it.
- Route selected: follow-up design direction → targeted image/frame and button review → native slideshow guidance.
- Actions: Applied the radius-free image/frame direction while retaining the button/filler radius requested in U5.2 and U5.4. The geometry note was created as an untracked `DESIGN_NOTES.md` in the separate REXconstruction workspace; it was not added to Website_Lab. Native slideshow guidance preceded the later autoplay implementation.
- Verification: The final Desktop/Phone screenshots and preview check covered the implemented page. The repository placement of the geometry note was checked and found to be outside Website_Lab.
- Outcome: Partial — the visual direction and guidance were handled, but the requested repository note was saved in the other workspace.
- Later-discovered issue: The requested filler guidance was not persisted in the Website_Lab repository.
- Correction: None in this Website_Lab history update; the geometry remains in the separate workspace note.
- Workflow candidate: Confirm the destination repository before documenting a reusable implementation detail.

## 2026-10-13 — U5.6 Autoplay and review-card/link follow-up

- Task reference: REX Construction Home U5, prompt 6
- Request: Add autoplay to the Hero image; add review avatars; link “Read full review” to the Reviews page without expanding the card; fix component width overlap; replace the text link with a white button.
- Route selected: live component readback → `framer-components` → targeted visual and preview QA.
- Actions: Added a three-image Hero slideshow with four-second autoplay; added reviewer avatars and abbreviated excerpts; fixed review cards to a consistent 300px width; linked “Read full review” to `/testimonials`; replaced “Read testimonials” with the white CTA; relabeled the third counter “Client Rating.”
- Verification: Review routes and state mappings read back; component and selector screenshots plus full Desktop/Phone screenshots reviewed; Framer preview readiness returned no errors or warnings. Runtime click/hover proof remained unavailable because staging was disabled.
- Outcome: Partial — requested visual and structural changes were implemented, but displayed values `10+`, `100+` and `5.0/5` remain unverified business claims.
- Later-discovered issue: Years of Experience, Roofs Installed, and Client Rating values lack authoritative confirmation.
- Correction: No numeric claim was approved or treated as verified; the site remained unpublished.
- Workflow candidate: Separate each user prompt in the observation when the user explicitly requests prompt-level history.
