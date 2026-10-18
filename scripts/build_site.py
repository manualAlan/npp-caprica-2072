"""Build the NPP 2072 static campaign pages. Run with Python 3; no dependencies."""
from html import escape as esc
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
SITE = 'https://manualalan.github.io/npp-caprica-2068/'

# 2072 proposals, not a claim of achievements during the 2068–2072 opposition term.
POLICIES = [
    dict(id='care', label='Public care', title='Care is a right.', image='2072/care.jpg',
         alt='A doctor talking with a patient in a clinic', position='50% 40%', size='half',
         line='Good care, close to home. Whoever you are.',
         pledges=[('A stronger public health service', 'Recruit and retain care teams, expand local clinics and publish waiting-time data so investment follows need.'),
                  ('Support before crisis', 'Bring mental healthcare into primary care and guarantee access to essential medicines.'),
                  ('Time to care', 'Pool the cost of parental and long-term illness leave through social insurance, supporting families and small employers alike.')]),
    dict(id='homes', label='Affordable homes', title='A place to call yours.', image='2072/housing.jpg',
         alt='Sunlit apartment balconies with plants and outdoor seating', position='50% 55%', size='half',
         line='Secure renting. More homes. Room to put down roots.',
         pledges=[('Build where life happens', 'Allow more homes near jobs and public transport, with clear planning rules and strong safety standards.'),
                  ('Homes for the long term', 'Expand public and cooperative housing, funded through transparent investment and a fairer tax on land value.'),
                  ('Security for renters', 'Enforce decent standards and fair tenancy procedures. Put empty homes to use and introduce a progressive levy from the third residential property onward.')]),
    dict(id='work', label='Fair work', title='A fair share.\nA real voice.', image='2072/work.jpg',
         alt='A carpenter at work in a woodworking shop', position='50% 50%', size='third',
         line='Rights at work. Freedom to organise. A stake in change.',
         pledges=[('A voice you choose', 'Protect collective bargaining and elected worker representation, with secret ballots and the freedom to join or leave a union.'),
                  ('Security through change', 'Offer paid retraining and benefits that follow workers between jobs. Help people share in new technology’s gains.'),
                  ('Fair rules, fairly enforced', 'Tackle wage theft and unsafe work. Give small firms practical compliance support and proportionate penalties for honest paperwork errors.')]),
    dict(id='learning', label='Learning & discovery', title='Talent is everywhere.', image='2072/learning.jpg',
         alt='Students reading together in a sunlit classroom', position='50% 35%', size='third',
         line='Opportunity should be, too.',
         pledges=[('Start with every child', 'Strengthen public early-years provision and schools, with better teacher pay, training and retention.'),
                  ('Keep learning open', 'Protect publicly funded access to university and technical education. Make retraining possible throughout working life.'),
                  ('Give discovery room', 'Back independent research, regional laboratories and accessible R&D support for small firms. Require human accountability when AI affects people’s rights.')]),
    dict(id='freedom', label='An open society', title='Your life.\nYour liberty.', image='2072/library.jpg',
         alt='A reader studying among the shelves of a bright public library', position='50% 55%', size='third',
         line='Government should answer to you.',
         pledges=[('Put limits on secret power', 'Replace sweeping intelligence powers with targeted, judge-authorised surveillance. Ban torture, scrutinise budgets in Parliament and require independent reviews of secrecy.'),
                  ('Equal citizenship', 'Defend expression, peaceful assembly, privacy and equal treatment. Keep the press and courts independent of government.'),
                  ('Power in the open', 'Require public asset declarations, transparent appointments and a citizens’ constitutional convention on accountable parliamentary government.')]),
    dict(id='climate', label='Climate & clean energy', title='A future worth sharing.', image='2072/energy.jpg',
         alt='Solar panels collecting clean energy', position='50% 50%', size='wide',
         line='Clean power. Warmer homes. Good jobs.',
         pledges=[('Build clean, reliable power', 'Invest in renewables, nuclear energy, storage and the grid. Give communities a share in new clean-energy projects.'),
                  ('Make the transition fair', 'Insulate homes and prioritise households facing high energy costs. Fund practical retraining where industries change.'),
                  ('Make every investment count', 'Set a firm emissions cap and create a green investment bank with published lending criteria, independent audits and clear public returns.')]),
    dict(id='transport', label='Connected communities', title='Closer to what matters.', image='2072/rail.jpg',
         alt='A passenger train at a station', position='50% 50%', size='third',
         line='Reliable journeys. More time for life.',
         pledges=[('Make everyday travel work', 'Strengthen public transport, with reliable local services, coordinated timetables and simpler fares.'),
                  ('Connect every region', 'Build rail links in costed stages towards a network between state capitals. Improve rural bus and rail connections.'),
                  ('Streets for people', 'Create safer walking and cycling routes, accessible stations and useful links to homes, schools and clinics.')]),
    dict(id='world', label='Caprica & the world', title='Stronger, together.', image='2072/partnership.jpg',
         alt='Pedestrians and cyclists crossing a bridge over a harbour', position='50% 50%', size='half',
         line='A confident Caprica in the Columbian Union.',
         pledges=[('Stay engaged. Shape reform.', 'Keep Caprica in the Columbian Union and pursue democratic, federalist reform through cooperation. Put negotiations under parliamentary scrutiny.'),
                  ('Make partnership tangible', 'Expand research, education and clean-energy cooperation. Support open trade with enforceable labour and environmental standards.'),
                  ('Security with accountability', 'Maintain a professional defence force under civilian control. Put diplomacy, international law and human rights at the centre of foreign policy.')]),
]

def shell(title, description, path, body, active=''):
    base = '../' if path else './'
    nav = ''.join(f'<a href="{base}{href}"' + (' aria-current="page"' if key == active else '') + f'>{label}</a>' for key, href, label in [
        ('vision', 'vision/', 'Our vision'), ('plan', 'plan/', 'Our plan'), ('together', '#together', 'Take part')])
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)} | NPP 2072</title>
<meta name="description" content="{esc(description, quote=True)}">
<meta name="theme-color" content="#f7f6f2">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:title" content="{esc(title, quote=True)} | NPP 2072">
<meta property="og:description" content="{esc(description, quote=True)}">
<meta property="og:type" content="website"><meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}assets/2072/community.jpg">
<link rel="icon" href="{base}assets/npp-logo.png">
<link rel="stylesheet" href="{base}styles.css?v=2072">
<script src="{base}app.js?v=2072" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="header wrap">
  <a class="brand" href="{base}" aria-label="New Progressive Party home"><img src="{base}assets/npp-logo.png" alt="NPP" width="144" height="48"><span>New Progressive<br>Party</span></a>
  <nav class="desktop-nav" aria-label="Main navigation">{nav}<span class="year">2072</span></nav>
  <details class="mobile-nav"><summary>Menu <span aria-hidden="true">+</span></summary><nav aria-label="Mobile navigation">{nav}<span class="year">Caprica / 2072</span></nav></details>
</header>
<main id="main">{body}</main>
<footer class="footer wrap">
  <p class="footer-name">A freer, fairer Caprica.<br><em>Together.</em></p>
  <nav aria-label="Footer navigation"><a href="{base}plan/">Our 2072 programme</a><a href="{base}vision/">What we believe</a><a href="{base}#together">Take part</a><a href="{base}photography/">Photography</a></nav>
  <div class="footer-meta"><span>New Progressive Party / 2072</span><details class="archive-links"><summary>2068 archive</summary><div><a href="{base}assets/manifesto.pdf">2068 manifesto</a><a href="{base}klinton-arkas/">Klinton Arkas · 2068 campaign</a></div></details></div>
</footer>
</body></html>'''

def photo(policy, base='./', eager=False):
    loading = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<img src="{base}assets/{policy["image"]}" alt="{esc(policy["alt"], quote=True)}" {loading} decoding="async" style="object-position:{policy["position"]}" width="1200" height="900">'

def photo_card(p, eager=False):
    title = esc(p['title']).replace('\n', '<br>')
    return f'''<a class="photo-card {p['size']}" href="./plan/#{p['id']}">
    {photo(p, eager=eager)}<span class="category">{esc(p['label'])}</span>
    <div class="photo-copy"><h2>{title}</h2><span class="card-arrow" aria-hidden="true">↗</span></div></a>'''

def write(path, content):
    dest = DIST / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content, encoding='utf-8')

community = dict(image='2072/community.jpg', alt='People spending time together beneath the trees in a public park', position='50% 55%')
home = '''
<section class="intro wrap">
  <p class="eyebrow">Caprica / 2072</p>
  <h1>Freedom to be yourself.<br>A fair chance to thrive.</h1>
  <p class="intro-note">Four years in opposition. Ready to move Caprica forward.</p>
</section>
<section class="photo-grid wrap" aria-label="Our priorities for Caprica">'''
home += '\n'.join(photo_card(p, i < 2) for i, p in enumerate(POLICIES))
home += f'''<a class="photo-card half" href="./vision/">{photo(community)}<span class="category">What we believe</span><div class="photo-copy"><h2>A country for<br>all of us.</h2><span class="card-arrow" aria-hidden="true">↗</span></div></a></section>
<section class="invitation wrap" id="together"><div><p class="eyebrow">The next chapter</p><h2>Progress starts<br><em>with us.</em></h2></div><div class="invitation-actions"><a class="button" href="./plan/">Explore our 2072 programme <span aria-hidden="true">↗</span></a><div class="resource-links"><a href="./assets/npp-conversation-guide.txt" download>Get the conversation guide ↓</a><button type="button" id="share">Share our vision ↗</button><a href="./assets/npp-logo.png" download="NPP-logo.png">Download the NPP logo ↓</a></div><p id="share-status" role="status" aria-live="polite"></p></div></section>'''
write('index.html', shell('A freer, fairer Caprica', 'The New Progressive Party’s 2072 campaign. Civil liberties, strong public services and a fair chance for everyone, after four years in opposition.', '', home))

plan = '''<section class="page-intro wrap"><p class="eyebrow">Our programme / 2072</p><h1>Freedom. Fairness.<br>A future we share.</h1><p>Our plan for the next term. A fresh start after four years in opposition.</p></section>
<nav class="topic-nav wrap" aria-label="Programme topics">'''
plan += ''.join(f'<a href="#{p["id"]}">{esc(p["label"])}</a>' for p in POLICIES)
plan += '</nav><div class="programme wrap">'
for i, p in enumerate(POLICIES):
    pledges = ''.join(f'<li><h3>{esc(title)}</h3><p>{esc(copy)}</p></li>' for title, copy in p['pledges'])
    plan += f'''<article class="policy" id="{p['id']}"><figure>{photo(p, '../', i < 2)}</figure><div class="policy-copy"><p class="eyebrow">{i+1:02d} / {esc(p['label'])}</p><h2>{esc(p['title']).replace(chr(10), ' ')}</h2><p class="policy-line">{esc(p['line'])}</p><details><summary>Our commitments <span aria-hidden="true">+</span></summary><ul>{pledges}</ul></details></div></article>'''
plan += '''</div><section class="funding wrap"><p class="eyebrow">A promise worth keeping</p><h2>Ambition, with accountability.</h2><p>Phase new commitments, publish independent costings and identify funding before each budget. Protect essential services, report progress openly and change what isn’t working.</p><a class="text-link" href="../#together">Help share the plan ↗</a></section>'''
write('plan/index.html', shell('Our 2072 programme', 'Explore the NPP’s centre-left liberal programme for public care, affordable homes, fair work, democratic freedoms and cooperation.', 'plan/', plan, 'plan'))

vision = f'''<section class="page-intro wrap"><p class="eyebrow">Our shared conviction</p><h1>Freedom, with the<br>means to use it.</h1><p>Liberal in our values. Progressive in our purpose.</p></section>
<figure class="vision-photo wrap">{photo(community, '../', True)}</figure>
<section class="vision-copy wrap"><div><p class="eyebrow">New Progressive Party / 2072</p><h2>An open society.<br>A fairer everyday life.</h2></div><div><p class="lead">You should be free to live as yourself — and have the care, education and security to make that freedom real.</p><p>We are Caprica’s centre-left liberal party. We believe strong public services, free institutions and a fair economy belong together.</p><p>Since 2068, the NPP has been in opposition. In 2072, we are asking for a mandate to change course: limit secret state power, protect workers’ rights and freedom of association, and strengthen our place in the Columbian Union.</p><p>That means a government you can question. A home you can afford. A community you can count on. And a future in which progress reaches everyone.</p><a class="button" href="../plan/">Read our 2072 programme <span aria-hidden="true">↗</span></a></div></section>
<section class="values wrap" aria-label="Our principles"><div><span class="eyebrow">01 / Liberty</span><h2>Room to be yourself.</h2><p>Equal rights, privacy and an independent press.</p></div><div><span class="eyebrow">02 / Solidarity</span><h2>Someone in your corner.</h2><p>Public care, good schools and security through change.</p></div><div><span class="eyebrow">03 / Progress</span><h2>A world to build together.</h2><p>Clean energy, discovery and international cooperation.</p></div></section>'''
write('vision/index.html', shell('What we believe', 'The NPP is Caprica’s centre-left liberal opposition: an open society, a fairer everyday life and a shared future.', 'vision/', vision, 'vision'))

guide = 'NEW PROGRESSIVE PARTY\nA freer, fairer Caprica. Together.\nConversation guide | 2072\n\n'
guide += 'OUR PURPOSE\nA centre-left liberal programme after four years in opposition: freedom to be yourself and a fair chance to thrive. These are proposals for the next term.\n\n'
for p in POLICIES:
    guide += p['label'].upper() + '\n' + p['line'] + '\n'
    guide += '\n'.join('- ' + text for _, text in p['pledges']) + '\n\n'
guide += 'START BY LISTENING\nAsk what matters in your community. Discuss the proposals honestly, without presenting them as achievements or making unsupported claims.\n\nREAD THE CURRENT PROGRAMME\n' + SITE + 'plan/\n\nThe 2068 manifesto and candidate speeches remain historical archive material.\n'
write('assets/npp-conversation-guide.txt', guide)

ledger = json.loads((DIST / 'assets/2072/sources.json').read_text())
credits = '<section class="page-intro wrap"><p class="eyebrow">Photography</p><h1>Life, in the frame.</h1><p>Real photographs, with thanks to their creators.</p></section><div class="credits wrap">'
for item in ledger['images']:
    credits += f'<article><h2>{esc(item["description"])}</h2><p>{esc(item["photographer"])} · <a href="{esc(item["source"], quote=True)}">Source photograph</a> · <a href="{esc(item["license"], quote=True)}">Licence</a></p></article>'
credits += '<p class="credit-note">Photographs illustrate our themes; they do not imply an endorsement by the people shown.</p></div>'
write('photography/index.html', shell('Photography', 'Photography credits for the NPP 2072 website.', 'photography/', credits))
print('Built homepage, programme, vision, photography credits and 2072 conversation guide.')
