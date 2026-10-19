"""Generates the franklinstyne.com static pages with a shared header, contact band and footer."""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "franklinstyne-site")
SITE = "https://franklinstyne.com/"
EMAIL = "franklinstyne@gmail.com"
PHONE_DISPLAY = "+60 19-368 9798"
PHONE = "+60193689798"
WA = "https://wa.me/60193689798?text=Hi%20Franklin%2C%20I%27d%20like%20to%20discuss%20an%20AI%20training%20programme"
LINKEDIN = "https://www.linkedin.com/in/franklinstyne"
TIKTOK = "https://www.tiktok.com/@franklinstyne"

NAV = [
    ("index.html", "Home"),
    ("programmes.html", "Programmes"),
    ("track-record.html", "Track record"),
    ("training-providers.html", "Training Partners"),
    ("credentials.html", "Credentials"),
]

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' rx='7' fill='%2313302E'/%3E"
           "%3Ctext x='16' y='22' font-family='Arial' font-weight='700' font-size='15' fill='%23F0B54A' text-anchor='middle'%3EFS%3C/text%3E%3C/svg%3E")

WA_ICON = '<svg viewBox="0 0 32 32" fill="#fff" aria-hidden="true"><path d="M16.01 3C9.38 3 4 8.38 4 15.01c0 2.35.64 4.55 1.76 6.44L4 29l7.73-1.7a11.9 11.9 0 0 0 4.28.79h.01c6.63 0 12.01-5.38 12.01-12.01C28.03 8.38 22.65 3 16.01 3zm0 21.9h-.01a9.9 9.9 0 0 1-5.05-1.38l-.36-.21-4.58 1.01 1.01-4.46-.24-.38A9.85 9.85 0 0 1 5.9 15c0-5.58 4.54-10.11 10.11-10.11 2.7 0 5.24 1.05 7.15 2.96a10.05 10.05 0 0 1 2.96 7.16c0 5.58-4.54 10.09-10.11 10.09zm5.55-7.57c-.3-.15-1.79-.89-2.07-.99-.28-.1-.48-.15-.68.15-.2.3-.78.99-.96 1.19-.18.2-.35.22-.65.07-.3-.15-1.28-.47-2.44-1.5-.9-.8-1.51-1.79-1.69-2.09-.18-.3-.02-.46.13-.61.14-.14.3-.35.45-.53.15-.18.2-.3.3-.5.1-.2.05-.38-.02-.53-.08-.15-.68-1.63-.93-2.24-.24-.58-.49-.5-.68-.51h-.58c-.2 0-.53.07-.8.38-.28.3-1.05 1.03-1.05 2.5s1.08 2.9 1.23 3.1c.15.2 2.13 3.24 5.15 4.55.72.31 1.28.5 1.72.63.72.23 1.38.2 1.9.12.58-.09 1.79-.73 2.04-1.44.25-.71.25-1.31.18-1.44-.07-.13-.28-.2-.58-.35z"/></svg>'


def head(title, desc, path):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}{'' if path == 'index.html' else path}">
<meta property="og:image" content="{SITE}assets/franklin-styne.jpg">
<meta name="theme-color" content="#13302E">
<link rel="icon" type="image/svg+xml" href="assets/logo/franklinstyne-icon.svg">
<link rel="apple-touch-icon" href="assets/logo/franklinstyne-icon-512.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=IBM+Plex+Mono:wght@500;600&family=Source+Sans+3:wght@400;600;700&display=swap">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<a class="wa" href="{WA}" target="_blank" rel="noopener" aria-label="Message Franklin on WhatsApp">{WA_ICON}</a>
"""


ICON_INLINE = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 94 94" aria-hidden="true" class="mark"><rect x="0" y="0" width="94" height="94" rx="20" fill="#13302E"/><path d="M24 29 L45 47 L24 65" fill="none" stroke="#F0B54A" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/><rect x="51" y="60" width="24" height="8" rx="1.5" fill="#EEF3F1"/></svg>'


def header(path):
    links = "".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if href == path else ""}>{label}</a></li>'
        for href, label in NAV
    )
    return f"""<header class="site-header">
  <nav class="wrap nav" aria-label="Main">
    <a class="brand" href="index.html" aria-label="Franklin Styne, AI, Agentic AI and Automation Trainer, home">{ICON_INLINE}<span class="names"><b>Franklin Styne</b><span>AI, Agentic AI &amp; Automation Trainer</span></span></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav-links">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"></path></svg>Menu
    </button>
    <ul class="nav-links" id="nav-links">{links}<li><a class="btn btn-accent" href="#contact">Get in touch</a></li></ul>
  </nav>
</header>
<main>
"""


CONTACT_CLIENT = ("Planning AI training for your team? Let&rsquo;s talk.",
                  "Tell me about your team, the work they do and what you want AI to improve, with preferred dates and the number of participants. I will recommend a programme and send a course outline.")
CONTACT_PARTNER = ("Planning an AI programme for a client? Let&rsquo;s talk.",
                   "Share the client&rsquo;s industry, preferred dates, number of participants and the topic. I will respond with a recommended programme, course outline and trainer profile.")


def contact(variant):
    h, lede = variant
    return f"""<section class="ink" id="contact">
  <div class="wrap contact-grid">
    <div class="stack">
      <p class="label">Get in touch</p>
      <h2>{h}</h2>
      <p class="lede">{lede}</p>
      <div class="actions">
        <a class="btn btn-accent" href="{WA}" target="_blank" rel="noopener">Message on WhatsApp</a>
        <a class="btn btn-line" href="credentials.html">Download trainer profile</a>
      </div>
    </div>
    <ul class="contact-list">
      <li><span class="t">Email</span><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><span class="t">Phone and WhatsApp</span><a href="tel:{PHONE}">{PHONE_DISPLAY}</a></li>
      <li><span class="t">LinkedIn</span><a href="{LINKEDIN}" target="_blank" rel="noopener">linkedin.com/in/franklinstyne</a></li>
      <li><span class="t">Based in</span><span>Kuala Lumpur. Delivering across Malaysia, Brunei, Indonesia and India.</span></li>
    </ul>
  </div>
</section>
"""


def footer():
    links = "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in NAV)
    return f"""</main>
<footer>
  <div class="wrap foot">
    <span>&copy; <span class="yr">2026</span> Franklin Styne. HRD Corp Accredited Trainer, ID 13169.</span>
    <ul>{links}</ul>
  </div>
</footer>
<script>
(function(){{
  var y=document.querySelectorAll('.yr');for(var i=0;i<y.length;i++){{y[i].textContent=new Date().getFullYear();}}
  var b=document.querySelector('.menu-toggle'),l=document.getElementById('nav-links');
  if(b&&l){{b.addEventListener('click',function(){{var o=l.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false');}});
    l.addEventListener('click',function(e){{if(e.target.closest('a')){{l.classList.remove('open');b.setAttribute('aria-expanded','false');}}}});}}
}})();
</script>
</body>
</html>
"""


def page(path, title, desc, body):
    variant = CONTACT_PARTNER if path == "training-providers.html" else CONTACT_CLIENT
    with open(os.path.join(OUT, path), "w") as f:
        f.write(head(title, desc, path) + header(path) + body + contact(variant) + footer())


STATS = """<dl class="stats">
      <div><dt>AI training sessions delivered since 2023</dt><dd>200<span>+</span></dd></div>
      <div><dt>Participants trained since 2025</dt><dd>1,500<span>+</span></dd></div>
      <div><dt>Groups trained since 2025</dt><dd>90<span>+</span></dd></div>
      <div><dt>Countries: Malaysia, Brunei, Indonesia, India</dt><dd>4</dd></div>
    </dl>"""

CLIENTS = ["Maybank", "Intel", "Altera", "Keysight", "Osram", "Unicharm", "DSG", "Maxell Tohshin", "KMWE", "Kiswire",
           "Oryx", "Technip Energies", "Mitsui &amp; Co", "Ministry of Education", "JKR", "HRD Corp", "PSDC", "Malaysia Airports", "Jabatan Penerangan Malaysia", "RTM", "TV3",
           "Bernama", "UNITEN", "Taylor&rsquo;s University", "Swinburne University", "Low Yat Group"]
CLIENT_LIST = '<ul class="client-list">' + "".join(f"<li>{c}</li>" for c in CLIENTS) + "</ul>"


def video(t, who, org):
    return f"""<figure>
        <video controls preload="none" playsinline poster="assets/testimonials/{t}.jpg" aria-label="Testimonial video: {who}, {org}">
          <source src="assets/testimonials/{t}.mp4" type="video/mp4">
        </video>
        <figcaption><strong>{who}</strong><span>{org}</span></figcaption>
      </figure>"""


# ---------------- Home ----------------
page("index.html",
     "Franklin Styne | AI Training",
     "Hands-on AI training that turns everyday work into practical AI workflows. Generative AI, Microsoft 365 Copilot, AI automation and AI agents, with 40 years of technology and business experience. HRD Corp Accredited Trainer, ID 13169.",
     f"""<section class="hero">
  <div class="wrap hero-grid">
    <div class="stack">
      <p class="kicker">The future of work is changing. Are your teams ready?</p>
      <h1>Turn everyday work into <em>practical AI workflows</em>.</h1>
      <p class="lede">Your teams learn AI by improving their own reports, spreadsheets, presentations and processes, and leave with results they can use the next day. More than the tools, I help people build the mindset to work side by side with AI.</p>
      <p class="proof">40 years in technology<span aria-hidden="true">/</span>Building AI systems since the 1980s<span aria-hidden="true">/</span>HRD Corp Accredited Trainer</p>
      <div class="paths">
        <a class="path" href="#programmes"><span class="k">For organisations</span><strong>Find training for my team</strong></a>
        <a class="path path-alt" href="training-providers.html"><span class="k">For training providers</span><strong>Partner with me</strong></a>
      </div>
    </div>
    <figure class="hero-photo">
      <img src="assets/training-photo.jpg" alt="Franklin Styne guiding participants through a hands-on AI exercise in a corporate training room" width="570" height="720">
      <figcaption class="id-tag"><span class="t">HRD Corp Accredited Trainer</span><span class="v">ID <span>13169</span></span></figcaption>
    </figure>
  </div>
</section>

<section class="ink tight" aria-label="Track record">
  <div class="wrap">
    {STATS}
  </div>
</section>

<section id="lesson">
  <div class="wrap lesson">
    <div class="stack">
      <p class="label">Watch a 1-minute lesson</p>
      <h2>From an Excel list to an interactive PowerPoint dashboard with Copilot.</h2>
      <p class="lede">This is how I teach: a real workplace task, a clear method you can follow and a result you can use the same day.</p>
      <ol class="mini-steps">
        <li>Start with your data in Excel</li>
        <li>Give Copilot a structured prompt</li>
        <li>Get a working, filterable dashboard slide</li>
      </ol>
    </div>
    <figure class="lesson-video">
      <video controls preload="none" playsinline poster="assets/lesson/poster.jpg" aria-label="Lesson video: creating an interactive dashboard with Copilot in PowerPoint">
        <source src="assets/lesson/copilot-powerpoint-dashboard.mp4" type="video/mp4">
      </video>
      <figcaption>Microsoft 365 Copilot lesson, 70 seconds. Sample data only.</figcaption>
    </figure>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="head">
      <p class="label">My signature approach</p>
      <h2>Learn it. Apply it. Present it.</h2>
      <p class="lede">Every programme follows the same four steps, so participants leave the room having already used AI on their own work.</p>
    </div>
    <ol class="journey">
      <li><img src="assets/lesson/step-challenge.jpg" alt="An Excel sheet of employee records, the starting point of an exercise" loading="lazy"><div><h3>Bring a work challenge</h3><p>Teams start with a real task from their own job: a report, a dataset, a presentation or a slow process.</p></div></li>
      <li><img src="assets/lesson/step-method.jpg" alt="A structured Copilot prompt shown during a lesson" loading="lazy"><div><h3>Learn the method</h3><p>A structured prompting framework and the right tool for the task, practised hands-on from the first hour.</p></div></li>
      <li><img src="assets/group-project-1.jpg" alt="Participants building an AI solution together in a group" loading="lazy"><div><h3>Build a solution</h3><p>Groups apply AI to their challenge and build a working output, with coaching as they go.</p></div></li>
      <li><img src="assets/group-project-2.jpg" alt="A participant presenting the group's AI solution to the class" loading="lazy"><div><h3>Demonstrate the result</h3><p>Each group presents what they built and the time it saves, so the organisation sees the result before the day ends.</p></div></li>
    </ol>
  </div>
</section>

<section id="programmes">
  <div class="wrap">
    <div class="head">
      <p class="label">Programmes</p>
      <h2>Where should your team start?</h2>
      <p class="lede">Each programme runs as a 1-day or 2-day session, in-house, public or live online, and is HRD Corp claimable when delivered through a registered training provider.</p>
    </div>
    <div class="grid-2">
      <a class="card route" href="programmes.html#foundations"><p class="label">New to AI</p><h3>AI Foundations for Workplace Productivity</h3><p>Prompting, checking AI output and using ChatGPT, Gemini and Claude for writing, analysis and everyday tasks.</p><span class="more">See the programme</span></a>
      <a class="card route" href="programmes.html#copilot"><p class="label">Using Microsoft 365</p><h3>Microsoft 365 Copilot</h3><p>Copilot inside Word, Excel, PowerPoint, Outlook and Teams, applied to your own documents and meetings.</p><span class="more">See the programme</span></a>
      <a class="card route" href="programmes.html#automation"><p class="label">Reduce repetitive steps</p><h3>AI Automation</h3><p>Working automations with n8n and Power Automate that take manual steps out of reporting, email and approvals.</p><span class="more">See the programme</span></a>
      <a class="card route" href="programmes.html#agents"><p class="label">Ready for agents</p><h3>AI Agents for the Workplace</h3><p>Designing agents with clear goals, tools and guardrails, and keeping people in control of the results.</p><span class="more">See the programme</span></a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap split">
    <div class="stack">
      <p class="label">Why organisations choose me</p>
      <h2>Technology, business and teaching, in one trainer.</h2>
      <p class="lede">Years in management mean I understand the pain points your people face, from reporting and approvals to meetings and team communication.</p>
    </div>
    <ul class="checks">
      <li><div><strong>A mindset for working with AI</strong><span>Participants learn to work side by side with AI and build it into their daily workflows, beyond any single tool.</span></div></li>
      <li><div><strong>Proven programme design</strong><span>Refined over more than 200 sessions, with clear outcomes and a structured prompt engineering framework.</span></div></li>
      <li><div><strong>Engaging and approachable</strong><span>Lively, interactive and jargon-free, so participants enjoy the learning and leave confident, whatever their starting point.</span></div></li>
      <li><div><strong>Capacity for large groups</strong><span>A network of experienced trainers and facilitators delivers organisation-wide rollouts with consistent quality.</span></div></li>
      <li><div><strong>Long-term partnerships</strong><span>Organisations consistently return for further cohorts and advanced programmes as their AI adoption grows.</span></div></li>
    </ul>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="head">
      <p class="label">In their words</p>
      <h2>What participants say.</h2>
    </div>
    <div class="videos">
      {video("t15", "Participant", "Maybank")}
      {video("t1", "Participant", "OSRAM procurement and supply chain")}
      {video("t7", "Assistant Director, Cyber Media", "Jabatan Penerangan Malaysia")}
    </div>
    <p style="margin-top:28px"><a class="btn btn-line" href="track-record.html">See full track record</a></p>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="head">
      <p class="label">Organisations trained</p>
      <h2>Trusted across sectors and the region.</h2>
    </div>
    {CLIENT_LIST}
  </div>
</section>

<section>
  <div class="wrap split">
    <img src="assets/franklin-styne.jpg" alt="Portrait of Franklin Styne" width="301" height="384" style="border-radius:var(--radius);width:min(100%,320px)">
    <div class="stack">
      <p class="label">About Franklin</p>
      <h2>Passionate about AI since the 1980s.</h2>
      <p class="muted"><strong style="color:var(--fg)">MBA, MCIM, PhD (Candidate).</strong> I began my career as a computer programmer and systems analyst building expert systems, an early form of AI, then led international market expansion as Head of International Business Development for a global company. Over 40 years, that combination has given me a deep understanding of how technology works, how businesses run and how adults learn.</p>
      <p class="muted">Today I help corporate, government and education teams across Malaysia, Brunei, Indonesia and India save time on repetitive work with the right AI tools. I am an ICDL AI and Microsoft 365 Copilot certified productivity coach, an HRD Corp Accredited Trainer and an adjunct MBA lecturer.</p>
      <p><a href="credentials.html">Credentials and downloads</a></p>
    </div>
  </div>
</section>

""")

# ---------------- Programmes ----------------
def prog(pid, label, name, intro, outcomes, modules, tools, audience, leave, prereq, access):
    mods = "".join(f"<li><div><strong>{m}</strong><span>{d}</span></div></li>" for m, d in modules)
    outs = "".join(f"<li><div><span>{o}</span></div></li>" for o in outcomes)
    return f"""<article class="prog" id="{pid}">
      <div class="intro">
        <p class="label">{label}</p>
        <h2>{name}</h2>
        {intro}
        <p class="leave"><strong>Participants leave with:</strong> {leave}</p>
        <dl class="facts">
          <div><dt>Tools</dt><dd>{tools}</dd></div>
          <div><dt>Duration</dt><dd>1-day or 2-day</dd></div>
          <div><dt>Delivery</dt><dd>In-house, public or live online</dd></div>
          <div><dt>Funding</dt><dd>HRD Corp claimable via a registered training provider</dd></div>
          <div><dt>Prerequisites</dt><dd>{prereq}</dd></div>
          <div><dt>Software access</dt><dd>{access}</dd></div>
          <div style="grid-column:1/-1"><dt>Suitable for</dt><dd>{audience}</dd></div>
        </dl>
        <h3 style="margin-top:10px">Participants will be able to</h3>
        <ul class="checks">{outs}</ul>
        <div class="actions"><a class="btn btn-accent" href="mailto:{EMAIL}?subject=Course%20outline%20request%3A%20{name.replace(' ', '%20').replace('&amp;', 'and')}">Request the full outline</a></div>
      </div>
      <div class="stack">
        <p class="label">Typical 2-day modules</p>
        <ol class="modules">{mods}</ol>
      </div>
    </article>"""

ROUTES = [
    ("&ldquo;Our employees are new to AI.&rdquo;", "foundations", "AI Foundations for Workplace Productivity", "Confident everyday use of AI for writing, analysis and research"),
    ("&ldquo;We use Microsoft 365 and have Copilot.&rdquo;", "copilot", "Microsoft 365 Copilot", "Copilot workflows in Word, Excel, PowerPoint, Outlook and Teams"),
    ("&ldquo;We want to reduce repetitive steps.&rdquo;", "automation", "AI Automation", "A working automation for a real process"),
    ("&ldquo;We are ready to explore agents.&rdquo;", "agents", "AI Agents for the Workplace", "A designed and tested workplace agent with guardrails"),
]
ROUTE_ROWS = "".join(f'<tr><td>{s}</td><td><a href="#{a}">{n}</a></td><td>{l}</td></tr>' for s, a, n, l in ROUTES)

page("programmes.html",
     "Programmes | Franklin Styne, AI Training",
     "AI Foundations, Microsoft 365 Copilot, AI automation and AI agent training programmes by Franklin Styne, with outcomes, modules, prerequisites and formats for corporate, government and education teams.",
     f"""<section class="page-hero">
  <div class="wrap stack">
    <p class="label">Programmes</p>
    <h1>Proven programmes, refined over 200+ sessions.</h1>
    <p class="lede">Each programme has been delivered and refined many times with corporate, government and education teams. Every programme is tailored to your industry and job roles, and a detailed course outline is available on request.</p>
  </div>
</section>
<section class="tight">
  <div class="wrap">
    <div class="head" style="margin-bottom:24px">
      <p class="label">Where should we start?</p>
      <h2>Find the right starting point.</h2>
    </div>
    <div class="table-wrap">
      <table class="routes">
        <thead><tr><th scope="col">Your situation</th><th scope="col">Suggested programme</th><th scope="col">Participants leave with</th></tr></thead>
        <tbody>{ROUTE_ROWS}</tbody>
      </table>
    </div>
    <p class="muted" style="margin-top:16px">Not sure? Tell me about your team and I will recommend a starting point.</p>
  </div>
</section>
<section style="padding-block:24px 64px" class="alt">
  <div class="wrap">
    {prog("foundations", "Starting point", "AI Foundations for Workplace Productivity",
          "<p>For teams new to AI. Participants learn how generative AI works, how to write effective prompts and how to check AI output, then apply ChatGPT, Gemini and Claude to their own everyday tasks.</p>",
          ["Write clear, structured prompts that produce reliable results",
           "Draft emails, reports and proposals faster",
           "Summarise documents, research topics and analyse data with AI",
           "Choose the right AI tool for each task",
           "Check AI output for accuracy and use AI responsibly at work"],
          [("How generative AI works", "What large language models can and cannot do, and where they fit in daily work."),
           ("Prompt engineering framework", "A repeatable structure for prompts, with practice on the participants' own tasks."),
           ("Writing and communication", "Emails, reports, proposals and minutes."),
           ("Research and analysis", "Summarising documents, comparing options and working with data."),
           ("Presentations and content", "Turning ideas into slides, briefs and content."),
           ("Responsible AI", "Accuracy checks, data privacy and company policy."),
           ("Group project and presentation", "Teams solve a real work problem with AI and present the time saved.")],
          "ChatGPT, Google Gemini, Claude",
          "Executives, managers, admin, HR, finance, sales and operations teams",
          "a personal prompt toolkit and finished outputs from their own work tasks",
          "None. Suitable for complete beginners.",
          "A free or paid account for at least one AI assistant; access set up before the session")}
    {prog("copilot", "Microsoft 365", "Microsoft 365 Copilot for Productivity",
          "<p>For organisations using Microsoft 365. Participants apply Copilot inside the apps they already use, on their own documents, spreadsheets, presentations and meetings. <a href='index.html#lesson'>Watch a 1-minute Copilot lesson</a>.</p>",
          ["Draft and refine documents with Copilot in Word",
           "Analyse data, build summaries and create formulas with Copilot in Excel",
           "Create presentations and interactive slides with Copilot in PowerPoint",
           "Manage email and meetings with Copilot in Outlook and Teams",
           "Check AI output for accuracy and follow company data policy"],
          [("Copilot essentials", "How Copilot works with your organisation's data, and what it can and cannot see."),
           ("Prompt engineering framework", "A repeatable structure for Copilot prompts, practised on real tasks."),
           ("Word and Outlook", "Drafting, rewriting and summarising documents and email threads."),
           ("Excel", "Analysis, formulas, summaries and insights from your own data."),
           ("PowerPoint and Teams", "Building presentations and capturing meeting recaps and actions."),
           ("Responsible AI", "Accuracy checks, data privacy and company policy."),
           ("Group project and presentation", "Teams build a Copilot workflow for a real task and present the result.")],
          "Microsoft 365 Copilot, Copilot Chat",
          "Organisations rolling out or already using Microsoft 365 Copilot",
          "Copilot workflows for their own documents, data and meetings",
          "Basic familiarity with Word, Excel, PowerPoint and Outlook.",
          "Microsoft 365 Copilot licence for full features; Copilot Chat for the basic licence")}
    {prog("automation", "Advanced", "AI Automation for the Workplace",
          "<p>For teams ready to move beyond prompting. Participants build working automations that connect everyday apps and use AI to handle repetitive steps in reporting, email, data handling and approvals.</p>",
          ["Map a manual process and spot the steps worth automating",
           "Build automated workflows in n8n and Power Automate",
           "Add AI steps to classify, extract, summarise and draft",
           "Connect email, spreadsheets, forms and business apps",
           "Test, monitor and maintain automations safely"],
          [("Process mapping", "Find the repetitive steps in the participants' own workflows."),
           ("Automation building blocks", "Triggers, actions, conditions and data handling."),
           ("First workflow", "A working automation built step by step in n8n or Power Automate."),
           ("Adding AI to workflows", "Classify, extract, summarise and draft with AI inside the flow."),
           ("Connecting business apps", "Email, spreadsheets, forms and approvals."),
           ("Testing and maintenance", "Error handling, monitoring and safe rollout."),
           ("Group project and presentation", "Each team builds and demonstrates an automation for their department.")],
          "n8n, Power Automate, Claude",
          "Operations, admin and support teams, analysts, process owners and IT teams",
          "a working automation for a real process in their department",
          "Comfortable using AI assistants; AI Foundations or Copilot recommended first.",
          "n8n or Power Automate accounts; IT approval to connect business apps")}
    {prog("agents", "Advanced", "AI Agents for the Workplace",
          "<p>AI agents can research, draft, summarise and act across several steps. This programme shows teams how to design agents for real business tasks and how to keep people in control of the results.</p>",
          ["Explain what AI agents are and where they add value",
           "Design an agent with clear goals, tools and instructions",
           "Build agents for research, reporting and customer response tasks",
           "Set human review points, guardrails and data safeguards",
           "Plan how to roll out agents across a team"],
          [("From assistants to agents", "What changes when AI can plan and act across several steps."),
           ("Use case discovery", "Identify agent opportunities in the participants' own department."),
           ("Agent design", "Goals, instructions, tools and knowledge sources."),
           ("Building agents", "Hands-on builds for research, reporting and customer response."),
           ("Guardrails and oversight", "Human review points, data safeguards and failure handling."),
           ("Rollout planning", "Piloting, measuring and scaling agents across a team."),
           ("Group project and presentation", "Teams design and demonstrate an agent for a real task.")],
          "Claude, Copilot agents, n8n",
          "Managers and team leads, knowledge workers, innovation, IT and digital teams",
          "a designed and tested agent for a real task, with a rollout plan",
          "Comfortable using AI assistants; automation experience helpful.",
          "Claude or Microsoft Copilot Studio access, depending on your environment")}
  </div>
</section>
<section class="tight">
  <div class="wrap split">
    <div class="stack">
      <p class="label">Custom programmes</p>
      <h2>Need something specific for your team?</h2>
    </div>
    <p class="lede">I also design programmes for specific audiences, such as AI for educators, AI for HR or finance teams, and Level 2 programmes covering large language models, machine learning and automation. Tell me the audience and the outcomes you want, and I will propose an outline.</p>
  </div>
</section>
""")

# ---------------- Track record ----------------
def sector(name, desc, orgs):
    return f'<article class="card"><h3>{name}</h3><p>{desc}</p><ul class="client-list">' + "".join(f"<li>{o}</li>" for o in orgs) + "</ul></article>"

page("track-record.html",
     "Track Record | Franklin Styne, AI Training",
     "200+ AI training sessions since 2023, 1,500+ participants and 90+ groups trained since 2025, across Malaysia, Brunei, Indonesia and India.",
     f"""<section class="page-hero">
  <div class="wrap stack">
    <p class="label">Track record</p>
    <h1>200+ sessions delivered since 2023.</h1>
    <p class="lede">Corporate, government and education teams across Malaysia, Brunei, Indonesia and India, trained to turn hours of work into minutes with AI.</p>
  </div>
</section>
<section class="ink tight" aria-label="Track record in numbers">
  <div class="wrap">{STATS}</div>
</section>
<section>
  <div class="wrap">
    <div class="head">
      <p class="label">Sectors</p>
      <h2>Where I have trained.</h2>
    </div>
    <div class="grid-2">
      {sector("Manufacturing and engineering", "AI for production, engineering, quality, procurement and supply chain, plus HR, finance and sales teams.", ["Osram", "Intel", "Altera", "Oryx", "Technip Energies", "Keysight", "Unicharm", "DSG", "Maxell Tohshin", "KMWE", "Kiswire"])}
      {sector("Banking and financial services", "AI productivity, Microsoft 365 Copilot and responsible AI for banking and investment teams.", ["Maybank", "Mitsui &amp; Co"])}
      {sector("Government, public sector and media", "AI literacy and workplace productivity for agencies, public bodies and broadcast media.", ["Ministry of Education", "JKR", "JKR Sarawak", "HRD Corp", "PSDC", "Malaysia Airports", "Jabatan Penerangan Malaysia", "RTM", "TV3", "Bernama"])}
      {sector("Education", "AI for lecturers, administrators and teachers, covering teaching, assessment and administration.", ["UNITEN", "Taylor&rsquo;s University", "Swinburne University of Technology", "CB Learning Centre", "Dignity Schools", "Harvest International School"])}
    </div>
  </div>
</section>
<section class="alt">
  <div class="wrap">
    <div class="head">
      <p class="label">Testimonials</p>
      <h2>What participants say after the programme.</h2>
      <p class="lede">Shared with permission from each participant and their organisation.</p>
    </div>
    <div class="videos">
      {video("t15", "Participant", "Maybank")}
      {video("t1", "Participant", "OSRAM procurement and supply chain")}
      {video("t2", "Participant", "OSRAM procurement and supply chain")}
      {video("t6", "Participant", "Jabatan Penerangan Malaysia")}
      {video("t7", "Assistant Director, Cyber Media", "Jabatan Penerangan Malaysia")}
      {video("t13", "Teacher", "Government school")}
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="head">
      <p class="label">In the room</p>
      <h2>See the training sessions in action.</h2>
      <p class="lede">Short clips from recent programmes: hands-on practice, group projects and final presentations.</p>
    </div>
    <div class="tt-grid">
      <figure class="tt">
        <iframe src="https://www.tiktok.com/embed/v2/7632737725816360213" title="Brunei AI training, April 2026" loading="lazy" allow="encrypted-media; fullscreen; picture-in-picture" allowfullscreen></iframe>
        <figcaption>Brunei AI training, April 2026 <a href="https://www.tiktok.com/@franklinstyne/video/7632737725816360213" target="_blank" rel="noopener">Open on TikTok</a></figcaption>
      </figure>
      <figure class="tt">
        <iframe src="https://www.tiktok.com/embed/v2/7663836431630060820" title="Indonesia AI training, July 2026" loading="lazy" allow="encrypted-media; fullscreen; picture-in-picture" allowfullscreen></iframe>
        <figcaption>Indonesia AI training, July 2026 <a href="https://www.tiktok.com/@franklinstyne/video/7663836431630060820" target="_blank" rel="noopener">Open on TikTok</a></figcaption>
      </figure>
      <figure class="tt">
        <iframe src="https://www.tiktok.com/embed/v2/7696675442979245332" title="Bernama AI training, October 2026" loading="lazy" allow="encrypted-media; fullscreen; picture-in-picture" allowfullscreen></iframe>
        <figcaption>Bernama AI training, October 2026 <a href="https://www.tiktok.com/@franklinstyne/video/7696675442979245332" target="_blank" rel="noopener">Open on TikTok</a></figcaption>
      </figure>
    </div>
  </div>
</section>
<section>
  <div class="wrap split">
    <div class="stack">
      <p class="label">Latest sessions</p>
      <h2>Follow the training floor.</h2>
      <p class="lede">I post photos, clips and takeaways from each programme, including recent sessions in Brunei, Indonesia and with Bernama.</p>
    </div>
    <div class="actions" style="align-self:center">
      <a class="btn btn-accent" href="{LINKEDIN}" target="_blank" rel="noopener">Follow on LinkedIn</a>
      <a class="btn btn-line" href="{TIKTOK}" target="_blank" rel="noopener">Watch clips on TikTok</a>
    </div>
  </div>
</section>
""")

# ---------------- Training providers ----------------
page("training-providers.html",
     "Training Partners | Franklin Styne, AI Training",
     "How Franklin Styne partners with HRD Corp registered training providers to design and deliver AI training, supported by a network of trainers and facilitators for large groups.",
     f"""<section class="page-hero">
  <div class="wrap stack">
    <p class="label">For training providers</p>
    <h1>A trusted partner for AI training delivery.</h1>
    <p class="lede">I work alongside training providers to design and deliver high-quality AI programmes for their clients. For large groups and multi-batch rollouts, I am supported by a network of experienced trainers and facilitators.</p>
    <p class="lede">In Malaysia, I work with HRD Corp registered training providers, so programmes are claimable by eligible employers under HRD Corp schemes. As an HRD Corp Accredited Trainer (ID 13169), I provide the trainer documents required for the grant application. Outside Malaysia, I deliver programmes with partners in Brunei, Indonesia and India.</p>
    <div class="actions">
      <a class="btn btn-accent" href="mailto:{EMAIL}?subject=Partner%20proposal%20request&amp;body=Client%20industry%3A%0APreferred%20dates%3A%0ANumber%20of%20participants%3A%0AProgramme%20or%20topic%3A%0ADelivery%20(in-house%2C%20public%20or%20online)%3A%0AHRD%20Corp%20claimable%20(yes%2Fno)%3A">Check dates and request a proposal</a>
      <a class="btn btn-line" href="downloads/franklin-styne-training-partner-kit.pdf" download>Download the Training Partner Kit</a>
    </div>
  </div>
</section>
<section>
  <div class="wrap split">
    <div class="stack">
      <p class="label">What I bring</p>
      <h2>Support at every stage of the programme.</h2>
    </div>
    <ul class="checks">
      <li><div><strong>Course outline in your format</strong><span>Objectives, modules, schedule and methodology, adapted to your template.</span></div></li>
      <li><div><strong>Trainer documents</strong><span>Trainer profile and HRD Corp trainer certificate (ID 13169) for your proposal and grant application.</span></div></li>
      <li><div><strong>Workflow-focused materials</strong><span>Slides, exercises and datasets built around the client&rsquo;s industry, job roles and daily workflows, informed by years of management experience.</span></div></li>
      <li><div><strong>A proven record of repeat business</strong><span>Satisfied clients regularly return to their training provider for additional cohorts and advanced levels, such as multiple Copilot cohorts for Maybank and Osram, and Low Yat Group&rsquo;s progression from AI foundations to agentic AI and automation.</span></div></li>
      <li><div><strong>Delivery records</strong><span>Attendance, assessments and evaluation forms completed as your process requires.</span></div></li>
      <li><div><strong>Trainers and facilitators for large groups</strong><span>A network of experienced trainers and facilitators, so large cohorts and parallel batches run with the same programme design and consistent quality.</span></div></li>
      <li><div><strong>Delivered under your brand</strong><span>Programmes can be delivered under your organisation&rsquo;s brand and materials, aligned with your training standards.</span></div></li>
      <li><div><strong>Confidentiality</strong><span>Client information, training materials and commercial arrangements are handled in confidence.</span></div></li>
      <li><div><strong>Post-training summary</strong><span>A short report on group projects and outcomes, with recommendations for the client&rsquo;s next stage of AI adoption.</span></div></li>
    </ul>
  </div>
</section>
<section class="ink">
  <div class="wrap">
    <div class="head">
      <p class="label">How an engagement runs</p>
      <h2>From enquiry to claim.</h2>
    </div>
    <ol class="steps">
      <li><h3>Enquire</h3><p>Share the client&rsquo;s industry, dates, participant numbers and topic.</p></li>
      <li><h3>Propose</h3><p>I recommend a programme and provide the outline and trainer documents.</p></li>
      <li><h3>Tailor</h3><p>A short call with you or the client to understand roles and pain points.</p></li>
      <li><h3>Deliver</h3><p>Hands-on training with group projects, in-house or online.</p></li>
      <li><h3>Close out</h3><p>Attendance, assessments and evaluations for your claim submission.</p></li>
    </ol>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="head">
      <p class="label">Common questions</p>
      <h2>Frequently asked questions.</h2>
    </div>
    <div class="faq">
      <details><summary>Are your programmes HRD Corp claimable?</summary><p>Yes, when delivered through an HRD Corp registered training provider. I am an HRD Corp Accredited Trainer (ID 13169), and I provide the trainer documents you need for the grant application.</p></details>
      <details><summary>Can you deliver under our brand?</summary><p>Yes. Programmes can be delivered under your organisation&rsquo;s brand, using your templates and training standards, or co-branded if you prefer.</p></details>
      <details><summary>Can you train large groups?</summary><p>Yes. For large cohorts and multi-batch rollouts, I work with a network of experienced trainers and facilitators who use the same programme design and materials, so every group receives consistent quality.</p></details>
      <details><summary>Do you deliver outside Malaysia?</summary><p>Yes. I have delivered in Malaysia, Brunei, Indonesia and India, in person and live online. HRD Corp funding applies only to eligible Malaysian employers.</p></details>
      <details><summary>How much notice do you need?</summary><p>Two to three weeks is ideal for a tailored programme. Shorter timelines can often be accommodated for established programmes.</p></details>
      <details><summary>Can the programme be customised for one client?</summary><p>Yes. Most programmes are adapted to the client's industry, job roles and tools, including Microsoft 365 or Google Workspace environments.</p></details>
    </div>
  </div>
</section>
""")

def doc(slug, title, desc, meta, btn):
    return f"""<article class="card cert">
        <a class="thumb" href="downloads/{slug}.pdf" target="_blank" rel="noopener"><img src="assets/certs/{slug}.jpg" alt="Preview of {title}" loading="lazy"></a>
        <h3>{title}</h3>
        <p>{desc}</p>
        <p class="meta">{meta}</p>
        <div class="actions"><a class="btn btn-line" href="downloads/{slug}.pdf" download>{btn}</a></div>
      </article>"""

# ---------------- Credentials ----------------
page("credentials.html",
     "Credentials | Franklin Styne, AI Training",
     "Franklin Styne's trainer profile, HRD Corp accreditation, AI certifications and qualifications.",
     f"""<section class="page-hero">
  <div class="wrap stack">
    <p class="label">Credentials and downloads</p>
    <h1>Credentials and certifications.</h1>
    <p class="lede">My trainer profile, HRD Corp accreditation and professional certifications, available to view and download.</p>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="head">
      <p class="label">Profile and accreditation</p>
      <h2>Trainer profile and HRD Corp accreditation.</h2>
    </div>
    <div class="grid-2">
      {doc("franklin-styne-trainer-profile", "Trainer Profile", "One-page profile with background, training focus, certifications, track record and organisations trained.", "PDF, 1 page", "Download profile")}
      {doc("franklin-styne-hrdcorp-certificate", "HRD Corp Accredited Trainer Certificate", "Trainer ID 13169, valid 29 January 2024 to 29 January 2027. Scan the QR code on the certificate to verify it with HRD Corp.", "PDF, 1 page. IC number removed for privacy.", "Download certificate")}
    </div>
  </div>
</section>
<section class="alt">
  <div class="wrap">
    <div class="head">
      <p class="label">Certifications</p>
      <h2>AI and professional certifications.</h2>
    </div>
    <div class="grid-3">
      {doc("franklin-styne-icdl-artificial-intelligence", "ICDL Artificial Intelligence", "ICDL Profile Certificate, Artificial Intelligence module. Issued by ICDL Asia, January 2025.", "PDF, 1 page", "Download")}
      {doc("franklin-styne-microsoft-365-copilot", "Microsoft 365 Copilot", "Introduction to Microsoft 365 Copilot, completed on Microsoft Learn, February 2025.", "PDF, 1 page", "Download")}
      {doc("franklin-styne-dmi-digital-marketing-professional", "Certified Digital Marketing Professional", "Digital Marketing Institute (DMI Pro), syllabus version 6.0. Awarded January 2018.", "PDF, 1 page", "Download")}
    </div>
  </div>
</section>
<section>
  <div class="wrap split">
    <div class="stack">
      <p class="label">Qualifications</p>
      <h2>Academic and professional background.</h2>
      <p class="lede">Over 40 years across technology, business development, leadership training and higher education.</p>
    </div>
    <ul class="checks">
      <li><div><strong>HRD Corp Accredited Trainer</strong><span>Trainer ID 13169</span></div></li>
      <li><div><strong>ICDL Artificial Intelligence</strong><span>ICDL Asia, 2025</span></div></li>
      <li><div><strong>Microsoft 365 Copilot</strong><span>Microsoft Learn, 2025</span></div></li>
      <li><div><strong>MBA</strong><span>Master of Business Administration, and adjunct MBA lecturer</span></div></li>
      <li><div><strong>Certified Digital Marketing Professional</strong><span>Digital Marketing Institute, UK</span></div></li>
      <li><div><strong>MCIM</strong><span>Member, Chartered Institute of Marketing</span></div></li>
      <li><div><strong>PhD (Candidate)</strong><span>Doctoral research in progress</span></div></li>
    </ul>
  </div>
</section>
""")
print("built", sorted(os.listdir(OUT)))
