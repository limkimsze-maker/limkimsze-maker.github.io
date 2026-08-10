from pathlib import Path

path = Path('index.html')
raw = path.read_bytes()
had_crlf = b'\r\n' in raw
text = raw.decode('utf-8').replace('\r\n', '\n')

url = 'https://limkimsze-maker.github.io/Phonograms-Toy-Castle-Game/'
if url in text:
    print('Toy Castle link already exists on homepage; no change needed.')
    raise SystemExit(0)

anchor = 'href="https://limkimsze-maker.github.io/P3-SDR-One-Stop-Hub/"'
pos = text.find(anchor)
if pos == -1:
    raise SystemExit('Could not find P3 SDR One Stop Hub card in English section.')
article_end = text.find('</article>', pos)
if article_end == -1:
    raise SystemExit('Could not find end of P3 SDR One Stop Hub card.')
article_end += len('</article>')

card = '''\n\n        <article class="card english">\n          <h3>Phonograms Toy Castle Game</h3>\n          <p>Practise phonograms through a colourful one- or two-player toy castle game.</p>\n          <div class="badges">\n            <span class="badge english">English</span><span class="badge sdr">SDR</span><span class="badge">Primary</span><span class="badge ready">SLS-ready</span>\n          </div>\n          <div class="actions">\n            <a class="btn primary" href="https://limkimsze-maker.github.io/Phonograms-Toy-Castle-Game/" target="_blank" rel="noopener">Open</a>\n          </div>\n          <div class="note">Build phonogram recognition through engaging game play.</div>\n        </article>'''

text = text[:article_end] + card + text[article_end:]
if had_crlf:
    text = text.replace('\n', '\r\n')
path.write_bytes(text.encode('utf-8'))
print('Added Phonograms Toy Castle Game under English.')
