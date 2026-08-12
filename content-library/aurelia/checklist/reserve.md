# Reserve Page Checklist

Page: Reserve  
Path: `/reserve`  
Status: To do; booking integration Blocked  
Primary CTA: `Reserve a seat`

## Definition of Ready

- [x] Page purpose and structural direction are approved in `PROJECT.md`.
- [ ] Decide whether the final action is instant booking, an external provider handoff, or an enquiry request.
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

- [ ] Exactly one h1.
- [ ] Keep the opening concise and inside the initial viewport.
- [ ] State the action directly; avoid atmospheric copy that delays booking.
- [ ] Do not add decorative image, eyebrow, trust strip, or fake availability counter.

### 2. Booking explanation

- [ ] Clearly distinguish request, confirmation, and external-provider behavior.
- [ ] Do not imply availability or confirmation before the provider confirms it.
- [ ] Identify Demo state when no live service is connected.

### 3. Booking provider or form

- [ ] Choose one primary path: embed, external handoff, or native form.
- [ ] Third-party dependency, account requirement, privacy, and paid plan are documented.
- [ ] If external, the CTA destination is real and its open/new-tab behavior is intentional.
- [ ] If native, collect only required information.

### 4. Native form requirements, when used

- [ ] Visible label above every input; placeholder never substitutes for a label.
- [ ] Fields: name, email, preferred date, party size, booking type, and message only when needed.
- [ ] Correct input types and required/optional indicators.
- [ ] Shared Reservation Field component or a clearly maintainable field system.
- [ ] Shared Button component for Submit.
- [ ] States: default, focus, filled, invalid, disabled, submitting, success, service failure, and incomplete.
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
- [ ] Phone uses `tel:`, email uses `mailto:`, and address uses a real map URL.
- [ ] Long information is grouped into meaningful clusters, not a dense bordered table.
- [ ] Practical information is available in the body, not only Footer.

## Shared system and responsive

- [ ] Use shared Layout Template, Navbar, Footer, Button, and field system.
- [ ] Navigation and all Home reservation CTAs point to the real `/reserve` destination once this Page is ready.
- [ ] Desktop uses a quiet two-zone composition with clear width ownership.
- [ ] Tablet keeps form and supporting information readable without squeezing columns.
- [ ] Phone is a strict single column with the action before secondary facts.
- [ ] Inputs, selects, date controls, text area, and Submit have approximately 44px touch targets.
- [ ] 320/390 labels, errors, dates, emails, and button text do not overflow.
- [ ] Verify 320, 390, 810, 1200, and 1440+.

## SEO, accessibility, motion, and performance

- [ ] Unique Page Title and Meta Description.
- [ ] Exactly one h1 and logical h2/h3 hierarchy.
- [ ] Form contrast, placeholder contrast, Focus rings, labels, helper text, and errors meet reading needs.
- [ ] Screen-reader names describe every control and result.
- [ ] Error is not communicated by color alone.
- [ ] Reduced Motion does not delay or hide form feedback.
- [ ] Motion is limited to clear state transitions and feedback.
- [ ] Provider embed does not create unexpected CLS, overflow, or inaccessible focus traps.
- [ ] No unnecessary background image or heavy media competes with the form.

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
- [ ] `PROJECT.md` status, blockers, and recovery state are updated.

## Latest Part Result

Scope: Page plan  
Status: Blocked

Blocked:
- Booking provider, form endpoint, data handling, response time, policies, address, phone, email, and fallback contact are missing.
