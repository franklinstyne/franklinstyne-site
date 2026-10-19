# franklinstyne.com: project context

Personal website and brand materials for **Franklin Styne** (Franklin Styne Iyadurai), AI, Agentic AI & Automation Trainer, HRD Corp Accredited Trainer (ID 13169), based in Kuala Lumpur. Read this file before making any change.

## Who the site is for
1. **Organisations (corporate, government, education)** looking for AI training. This is the main audience. Home, Programmes, Track record and Credentials pages speak to them.
2. **Training providers (TPs)** who engage Franklin as a trainer. Only the **Training Partners** page (`training-providers.html`) and the Training Partner Kit speak to them.

Franklin also runs a separate company site, QuestAI Technologies (`franklinstyne/franklinstyne.github.io`, questaitech.com). Keep this site free of QuestAI branding and do not copy its wording; the two sites must not look duplicated.

## Hosting and publishing
- Plain static HTML and CSS, hosted on GitHub Pages from the `main` branch, root folder. Custom domain in `CNAME` (franklinstyne.com).
- DNS is managed in the Exabytes cPanel Zone Editor (mschosting nameservers): four A records for @ (185.199.108.153 / .109 / .110 / .111) and `www` CNAME to franklinstyne.github.io. Do not change the nameservers.
- Pushing to `main` publishes within a minute or two. The HTML files are the source of truth: edit them directly. `design/build_reference.py` is the generator originally used to create the pages, kept for reference only and may be out of date.

## Pages
- `index.html`: hero ("The future of work is changing. Are your teams ready?" kicker, headline "Turn everyday work into practical AI workflows."), two audience path buttons, stats, 1-minute Copilot lesson video, signature 4-step approach, programme route cards, why choose me, testimonial videos, organisations trained, about.
- `programmes.html`: "Where should we start?" table, then four programmes (AI Foundations, Microsoft 365 Copilot, AI Automation, AI Agents) with leave-with, prerequisites, software access and modules.
- `track-record.html`: stats, sectors, testimonial videos, TikTok clips (direct `tiktok.com/embed/v2/<id>` iframes), LinkedIn/TikTok links.
- `training-providers.html` (menu label "Training Partners"): partnership offer, HRD Corp note, proposal request button, Training Partner Kit download, engagement steps, FAQ.
- `credentials.html`: trainer profile, HRD Corp certificate, ICDL, Microsoft 365 Copilot and DMI certificates.

## Brand
- **Logo: "The Prompt"**: a gold `>` prompt, "Franklin Styne" (capitalised), a gold cursor `_`, tagline "AI, AGENTIC AI & AUTOMATION TRAINER". Icon: `>_` tile. Story: Franklin typed commands as a programmer in the 1980s; people now type prompts to AI. Files in `design/logo/` (SVG text is outlined; regenerate with `python3 design/logo/makelogo.py`, requires `fonttools`).
- **Colours**: ink green `#13302E`, gold `#D9901A` (bright gold `#F0B54A` on dark), gold text `#93590A`, background `#F4F6F5`, muted `#52605D`, line `#D9E0DE`.
- **Fonts**: Bricolage Grotesque (headings), Source Sans 3 (body), IBM Plex Mono (labels). TTFs in `design/fonts/`.

## Writing rules (Franklin's preferences)
- Website copy is in **first person** ("I design..."). Trainer profile and partner kit are in **third person**.
- Professional, natural tone. **No emojis, no em dashes.** Do not sound like a brochure or like pitching for work.
- Keep partnership wording positive and professional (delivered under the provider's brand, confidentiality).
- No half-day programmes. Programmes run 1-day or 2-day.
- Use "40 years" of experience. AI passion since the 1980s (programmer and systems analyst building expert systems). Former Head of International Business Development for a global company. Years in management, so he understands participants' pain points.
- Key messages: more than the tools, a mindset to work side by side with AI; learning AI is enjoyable, practical and jargon-free; network of trainers and facilitators for large groups; satisfied clients return to their training provider for repeat cohorts (e.g. Maybank and Osram Copilot cohorts, Low Yat Group's progression to agentic AI and automation).
- Keep "Microsoft 365 Copilot Certified" in bios (Franklin's decision).
- Stats: 200+ AI training sessions since 2023; 1,500+ participants and 90+ groups trained since 2025; 4 countries (Malaysia, Brunei, Indonesia, India).
- Contact: franklinstyne@gmail.com, +60 19-368 9798 (also WhatsApp), linkedin.com/in/franklinstyne, tiktok.com/@franklinstyne.

## Privacy
- The public HRD Corp certificate has the IC number removed (image-only PDF). Never publish the original certificate or Franklin's IC number.

## Design files (`design/`)
- `logo/`: logo SVG and PNG files plus `makelogo.py`.
- `profile/trainer-profile.html`: one-page trainer profile. Render to PDF with headless Chromium (`--print-to-pdf`, A4) and copy to `downloads/franklin-styne-trainer-profile.pdf`, then refresh `assets/certs/franklin-styne-trainer-profile.jpg`.
- `card/`: business card (90 x 54 mm, 3 mm bleed), HTML source and print PDF.
- `partner-kit/partner-kit-pages.html`: the two designed kit pages. The downloadable kit (`downloads/franklin-styne-training-partner-kit.pdf`) is these pages followed by the trainer profile and the redacted HRD Corp certificate (joined with `pdfunite`).

## Open items (as of October 2026)
1. Three case studies (Maybank, Osram, Low Yat Group): problem brought, what participants built, result demonstrated, what happened after, whether the client can be named. Waiting on Franklin's notes. Only publish time savings that have records.
2. Teaching videos with Franklin's voice: add the best one near the top of the home page.
3. One-line approved quotes for each testimonial video, shown as written captions.
4. Photos of real participant outputs to replace the lesson-video frames in steps 1 and 2 of the signature approach.
5. Franklin to confirm the prerequisites, software access and "leave with" lines on the Programmes page.
