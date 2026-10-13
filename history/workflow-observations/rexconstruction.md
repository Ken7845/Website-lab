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

## 2026-10-13 — Navigation, button, reviews and counters revision

- Task reference: REX Construction Home U5
- Request: Use Submit Roofing as an interaction/stack reference for the Navbar and Button, redesign Reviews as a card selector, and add three animated Hero counters.
- Route selected: reference-project readback → request contract → `framer-components` → advanced Counter pattern → `framer-qa`.
- Actions: Removed Phone row hover; created Yellow-filler red and white buttons plus Yellow-filling Desktop Navigation Button; applied the white variant to Services, Selected Work and About Rex; built a six-state selector from the saved reviews; preserved the reusable `Counter.tsx` code component.
- Verification: Button/Navbar definitions, routes, review-state mappings and catalog readback; component Hover and selector screenshots; full Desktop/Phone screenshots; preview readiness returned ready with no errors or warnings.
- Outcome: Partial — requested navigation, button and review work implemented; Hero Counter instances await exact metric values.
- Later-discovered issue: None in this follow-up.
- Correction: Updated prior checklist claims of missing reviews and bright-red filler to reflect the saved source and Yellow interactions.
- Workflow candidate: Treat authoritative content files and metric values as a precondition for testimonial and numeric-proof components; create reusable definitions without instantiating unverified claims.
