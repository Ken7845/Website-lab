# Reserve Page Checklist

Page: Reserve  
Path: `/reserve`  
Status: Native reservation-request form in progress; live submission Blocked  
Primary CTA: `Reserve a seat`

## Definition of Ready

- [x] Page purpose and structural direction are approved in `PROJECT.md`.
- [x] Final action: native reservation-request form; no external booking embed or handoff.
- [ ] Supply the real booking provider, destination URL, form endpoint, or approved integration.
- [ ] Supply verified response time, availability rules, cancellation policy, address, arrival instructions, accessibility, email, and phone as applicable.
- [ ] Approve the exact opening title and confirmation language.
- [ ] Confirm privacy statement and where submitted data goes.

## Page narrative

```text
Direct decision
→ what this action does
→ booking or enquiry
→ result and fallback
→ verified practical information
```

Reserve is the most operational page. It should be shorter and clearer than Home while retaining the same typography, tokens, and restraint.

## Section build checklist

### 1. Compact opening

- [x] Exactly one h1.
- [x] Keep the opening concise and inside the initial viewport.
- [x] State the action directly; avoid atmospheric copy that delays booking.
- [x] Do not add decorative image, eyebrow, trust strip, or fake availability counter.

### 2. Booking explanation

- [x] Clearly distinguish request, confirmation, and external-provider behavior.
- [x] Do not imply availability or confirmation before the provider confirms it.
- [x] Identify Demo state when no live service is connected.

### 3. Booking provider or form

- [x] Primary path: native reservation-request form.
- [ ] Third-party dependency, account requirement, privacy, and paid plan are documented.
- [ ] If external, the CTA destination is real and its open/new-tab behavior is intentional.
- [x] Native form collects only request essentials: name, email, preferred date, party size, booking type, and optional message.

### 4. Native form requirements, when used

- [x] Visible label above every input; placeholder never substitutes for a label.
- [x] Fields: name, email, preferred date, party size, booking type, and optional message.
- [x] Correct input types and required/optional indicators.
- [x] Clearly named, maintainable Reservation Field system.
- [x] Shared `ReservationSubmit` component for Submit.
- [x] Button structures exist for default, incomplete, submitting, success, and service-failure states; live state behavior remains unverified until a data destination exists.
- [ ] Error text appears beside or below the affected field and uses accessible contrast.
- [ ] Submit label describes the result, for example `Send request` when it is not instant booking.
- [ ] Keyboard order, Tab, Shift-Tab, Enter submission, and error return path work.
- [ ] A real successful submission is tested. If impossible, mark the integration Blocked and do not claim Pass.

### 5. Result and fallback

- [ ] Success language does not claim a confirmed seat unless the service confirms one.
- [ ] Service failure provides a verified alternate contact method.
- [ ] Missing email or phone is hidden rather than invented.
- [ ] Focus moves to or announces the result appropriately.

### 6. Practical information

- [ ] Address, arrival time, cancellation, accessibility, response time, phone, and email appear only when verified.
- [x] Phone uses `tel:`, email uses `mailto:`, and address uses a map URL; all current values are explicitly Demo.
- [x] Long information is grouped into meaningful clusters, not a dense bordered table.
- [x] Practical information is available in the body, not only Footer.

### 7. Reservation FAQ

- [x] Add an editorial FAQ section after the native request form and before Footer.
- [x] Use one reusable `FAQ Row` component with buyer-editable Question and Answer properties; default instances remain Closed.
- [x] Add eight buyer-editable fictional reference answers covering booking window, changes, dietary needs, party size, private dining, accessibility, arrival, and reservation contact; do not leave instruction-style `Demo answer` placeholders in the visible accordion.
- [x] Use existing Type/Caption, Type/Heading 3, Type/Body Large question, and smaller Type/Body answer styles plus Feather Plus/Minus icons.
- [x] Keep the FAQ in a separate full-width soft-grey surface; its outer section and bordered-row list have no `max-width`. `FAQ Row` owns its own horizontal padding; the non-component introduction retains its own readable measure and breakpoint padding.
- [x] Use the existing Surface, Text and Muted color system for the light FAQ surface; preserve a quieter answer hierarchy and a restrained light-grey Hover surface.
- [x] Use the established `spring-physics 250 30 1 0s` transition across FAQ states and a subtle `0.98` press scale.
- [ ] Preview-test Open, Closed, Hover, keyboard, Focus, touch, long-copy and Reduced Motion states on Desktop, Tablet and Phone.
- [ ] Verify all fictional reference answers are replaced by the restaurant’s verified policy before production publication.
- [ ] Follow the detailed [Reserve FAQ build and QA checklist](./reserve-faq-build-checklist.md) before marking the page complete.

## Shared system and responsive

- [x] Use the shared Layout Template, Navbar, Footer, Button, native labelled field system, and `ReservationSubmit` state component; production data destination, validation/error behavior, privacy handling, and result behavior remain Blocked.
- [x] Shared Navigation and Footer plus the Home, Menu, and Chefs Reservation Handoffs point to `/reserve`.
- [x] Desktop uses a quiet two-zone composition with clear width ownership.
- [x] Tablet keeps the request and supporting information readable without squeezing columns.
- [x] Phone is a strict single column with the action before secondary facts.
- [ ] Inputs, selects, date controls, text area, and Submit have approximately 44px touch targets.
- [ ] 320/390 labels, errors, dates, emails, and button text do not overflow.
- [ ] Verify 320, 390, 810, 1200, and 1440+.

## SEO, accessibility, motion, and performance

- [ ] Apply the standard line-by-line `onInView` text appearance effect to editorial headings only. Use About Phone → Opening Content → Opening Heading as the visual and timing reference; keep long-form Story/body copy static to avoid scroll lag, and exclude navigation, buttons, controls, form labels, and other functional UI text.
- [x] Unique Page Title and Meta Description.
- [x] Exactly one h1 and logical h2 hierarchy.
- [ ] Form contrast, placeholder contrast, Focus rings, labels, helper text, and errors meet reading needs.
- [ ] Screen-reader names describe every control and result.
- [ ] Error is not communicated by color alone.
- [ ] Reduced Motion does not delay or hide form feedback.
- [ ] Motion is limited to clear state transitions and feedback.
- [ ] Provider embed does not create unexpected CLS, overflow, or inaccessible focus traps.
- [x] No unnecessary background image or heavy media competes with the request action.

## Marketplace stress tests

- [ ] Switch booking type between restaurant seat and private-dining enquiry.
- [ ] Test a long email, long validation message, and long confirmation response.
- [ ] Test all optional practical facts hidden.
- [ ] Test provider missing or service failure state.
- [ ] Replace provider URL or form destination through a documented editing path.
- [ ] Editing instructions explain provider setup, fields, success/error copy, privacy, fallback contact, and CTA links across Home/Navbar/Footer.

## Targeted Preview

- [ ] Desktop: Navbar → explanation → complete form/provider path → success or destination → fallback → Footer.
- [ ] Phone: Menu open/close → every field → validation error → correction → Submit → result.
- [ ] Keyboard: full form path without pointer.
- [ ] Failure: service unavailable or endpoint error produces usable feedback.

## Reserve Page Done

- [ ] Booking behavior and data destination are real and documented.
- [ ] Every Section and form state passed its routed checklist.
- [ ] Shared systems, links, semantics, responsive, Focus, keyboard, Reduced Motion, and performance pass.
- [ ] Five widths and successful, error, and close/return paths pass.
- [ ] Marketplace integration replacement test passes.
- [ ] All site-wide `Reserve a seat` links are updated and checked.
- [ ] `STATUS.md` contains current page status/blockers, and `RECOVERY.md` contains only the latest continuation pointer.

## Latest Part Result

Scope: Rebuilt Demo request page and existing cross-page Reserve routing  
Status: Partial Pass; native form and FAQ structure built, live submission remains Blocked

Passed:
- The separately drawn Reserve controls were consolidated: Home, Menu, and Chefs use the shared Reservation Handoff, while shared Navigation and Footer also route to `/reserve`.
- After the prior Reserve content was removed, `/reserve` was rebuilt from an empty canvas with Desktop 1200, Tablet 810, and Phone 390 layouts, one h1, direct request language, a Demo disclaimer, an editorial mailto action, and body-level Demo email/telephone/map fallbacks.
- The rebuild uses one compact main scope rather than the prior non-brand-aligned two-section approach. Desktop is a quiet two-zone composition; Phone is a strict title → action → fallback reading sequence.
- The Demo email, telephone, and address use a local 15px Inter exception so new Phone contact information does not inherit the current 11px `Type/Body` preset.
- The approved native request path is now represented by a labelled reservation form with Name, Email, Preferred date, Party size, Booking type, and optional Message. Date and party size share a Desktop row and stack on Phone.
- `ReservationSubmit` provides Default, Incomplete, Pending, Success, and Error variants and is bound as the form submit control. The page explicitly states that the Demo form cannot send requests until a data destination and privacy notice are configured.
- Desktop and Tablet use a balanced two-column reservation form. The first column holds Name, Email, and Booking type; its Date-and-party row fills exactly the same column width. The second column holds Message with the `Request a table` action directly beneath it. Phone stacks both columns and its Date-and-party fields into one clear action sequence. Every input fills its allocated column; the Demo notice sits outside the form.
- Desktop and Phone canvas screenshots were visually checked after the final CTA refinement. No publish was performed.
- A new `Reservation FAQ` sits after the existing request/form/fallback content on its own full-width soft-grey surface. It uses eight default-Closed instances of `FAQ Row`; each exposes Question and Answer properties, toggles through connected Closed/Open variants, and uses Feather Plus/Minus with a pointer hover variant. Questions and icons use the dark Text system; answers use the smaller Muted hierarchy; dividers use the original light-grey stroke. All FAQ states use `spring-physics 250 30 1 0s` with a subtle `0.98` press scale. The visible answers are now complete fictional restaurant-policy examples rather than editing instructions; the section introduction still tells buyers to replace them with verified production policy.

Blocked:
- Form data destination, data handling, response time, policies, verified address, verified phone, verified email, privacy language, and live confirmation/failure behavior are missing.
- 320, 1440+, keyboard/focus, Reduced Motion, FAQ interaction, and live click-path Preview checks remain.
