#!/usr/bin/env python3
"""build_pub_cards.py — render the publication thumbnail cards.

Each card is an SVG (deep color plate, engraved hatch, serif glyph, cream line
drawing of the paper's mechanism) rendered with headless Chrome and saved as
assets/img/publication_preview/card-<name>.jpg. Reference a card from
_bibliography/papers.bib with `preview = {card-<name>.jpg}`.

To add a paper: write a motif with the helpers below, call card(...), re-run.
Requires Google Chrome and Pillow (`pip install pillow`).
"""
import os, subprocess, tempfile
REPO=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST=os.path.join(REPO,"assets","img","publication_preview")
OUT=tempfile.mkdtemp(prefix="pubcards-")
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CREAM="#f3e9d2"; ACC="#f0b37e"

def robot(x,y,w=90,h=74,stroke=CREAM,sw=4,acc=None):
    a=acc or stroke
    return f'''<g stroke="{stroke}" stroke-width="{sw}" fill="none" stroke-linecap="round" stroke-linejoin="round">
<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h*0.22}"/>
<line x1="{x+w/2}" y1="{y}" x2="{x+w/2}" y2="{y-h*0.28}"/><circle cx="{x+w/2}" cy="{y-h*0.36}" r="{h*0.08}" fill="{a}" stroke="{a}"/>
<circle cx="{x+w*0.32}" cy="{y+h*0.45}" r="{h*0.09}" fill="{stroke}"/><circle cx="{x+w*0.68}" cy="{y+h*0.45}" r="{h*0.09}" fill="{stroke}"/>
<line x1="{x+w*0.33}" y1="{y+h*0.75}" x2="{x+w*0.67}" y2="{y+h*0.75}"/></g>'''

def person(cx,y,s=1.0,stroke=CREAM,sw=4):
    return f'''<g stroke="{stroke}" stroke-width="{sw}" fill="none" stroke-linecap="round">
<circle cx="{cx}" cy="{y+22*s}" r="{22*s}"/><path d="M{cx-42*s},{y+100*s} Q{cx-40*s},{y+52*s} {cx},{y+52*s} Q{cx+40*s},{y+52*s} {cx+42*s},{y+100*s}"/></g>'''

def doc(x,y,w=62,h=80,rot=0):
    lines="".join(f'<line x1="{x+12}" y1="{y+18+i*14}" x2="{x+w-12-(i%2)*14}" y2="{y+18+i*14}"/>' for i in range(4))
    return f'''<g transform="rotate({rot} {x+w/2} {y+h/2})" stroke="{CREAM}" stroke-width="3" fill="none" stroke-linecap="round">
<path d="M{x},{y} h{w-16} l16,16 v{h-16} h-{w} z"/>{lines}</g>'''

def arrow_defs(color,id_):
    return f'<marker id="{id_}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{color}"/></marker>'

def sub(word):
    return f'τ<tspan font-size="62" font-style="italic" dy="34" dx="6">{word}</tspan>'

CARDS=[]

def card(name,bg,glyph,tagline,motif,glyph_size=230,glyph_y=330):
    CARDS.append(name)
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="600" viewBox="0 0 900 600">
<defs>
<pattern id="hatch" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
<line x1="0" y1="0" x2="0" y2="7" stroke="#ffffff" stroke-opacity="0.055" stroke-width="1.2"/></pattern>
<radialGradient id="vig" cx="35%" cy="40%" r="80%"><stop offset="0" stop-color="#ffffff" stop-opacity="0.08"/><stop offset="1" stop-color="#000000" stop-opacity="0.25"/></radialGradient>
{arrow_defs(CREAM,"ac")}{arrow_defs(ACC,"aa")}
</defs>
<rect width="900" height="600" fill="{bg}"/>
<rect width="900" height="600" fill="url(#hatch)"/>
<rect width="900" height="600" fill="url(#vig)"/>
<rect x="22" y="22" width="856" height="556" fill="none" stroke="{CREAM}" stroke-opacity="0.35" stroke-width="2"/>
<rect x="30" y="30" width="840" height="540" fill="none" stroke="{CREAM}" stroke-opacity="0.18" stroke-width="1"/>
<text x="70" y="{glyph_y}" font-family="'EB Garamond','STIX Two Text','STIX Two Math',serif" font-size="{glyph_size}" fill="{CREAM}">{glyph}</text>
<line x1="72" y1="452" x2="160" y2="452" stroke="{ACC}" stroke-width="4"/>
<text x="72" y="500" font-family="'Inter','Helvetica Neue',sans-serif" font-weight="600" font-size="23" letter-spacing="3.2" fill="{CREAM}" fill-opacity="0.92">{tagline}</text>
<g transform="translate(450,95)">{motif}</g>
</svg>'''
    html=f'''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,500;1,500&family=Inter:wght@600&display=block" rel="stylesheet">
<style>html,body{{margin:0;padding:0;background:{bg}}} svg{{display:block}}</style></head><body>{svg}</body></html>'''
    open(os.path.join(OUT,name+'.html'),'w').write(html)

# ---- Hyper-tau: agents that build agents
m=doc(0,40,rot=-10)+doc(20,175,rot=7)+doc(90,300,rot=-4)
m+=f'''<g stroke="{CREAM}" stroke-width="3" fill="none" stroke-linecap="round">
<path d="M120,0 h120 a14,14 0 0 1 14,14 v40 a14,14 0 0 1 -14,14 h-80 l-22,20 v-20 h-18 a14,14 0 0 1 -14,-14 v-40 a14,14 0 0 1 14,-14 z"/></g>
<g fill="{CREAM}"><circle cx="160" cy="34" r="5"/><circle cx="180" cy="34" r="5"/><circle cx="200" cy="34" r="5"/></g>
<g stroke="{CREAM}" stroke-width="2.5" stroke-dasharray="3 9" stroke-linecap="round" fill="none" stroke-opacity="0.8">
<path d="M75,90 Q150,120 200,170"/><path d="M90,220 Q150,215 195,210"/><path d="M150,320 Q190,300 215,258"/><path d="M185,90 Q200,130 225,160"/></g>
{robot(195,165,110,90)}
<g stroke="{ACC}" stroke-width="4" fill="none" stroke-linecap="round" marker-end="url(#aa)"><path d="M300,265 Q330,300 318,320"/></g>
<rect x="268" y="325" width="110" height="88" rx="10" fill="none" stroke="{ACC}" stroke-width="3" stroke-dasharray="10 7"/>
{robot(293,350,60,48,stroke=ACC,sw=3.5)}
<circle cx="372" cy="330" r="17" fill="{ACC}"/><path d="M364,330 l6,6 l11,-12" stroke="#2b2350" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''
card('hypertau','#2d2a5e','τ<tspan font-size="130" dy="-95">τ</tspan>','AGENTS THAT BUILD AGENTS',m)

# ---- tau2: dual control
m=robot(10,110,110,92)+person(330,90,1.2)
m+=f'''<g stroke="{CREAM}" stroke-width="3" fill="none" stroke-linecap="round">
<path d="M150,20 h80 a12,12 0 0 1 12,12 v26 a12,12 0 0 1 -12,12 h-56 l-16,14 v-14 h-8 a12,12 0 0 1 -12,-12 v-26 a12,12 0 0 1 12,-12 z"/>
<path d="M250,96 h-80 a12,12 0 0 0 -12,12 v26 a12,12 0 0 0 12,12 h56 l16,14 v-14 h8 a12,12 0 0 0 12,-12 v-26 a12,12 0 0 0 -12,-12 z" stroke-opacity="0.75"/></g>
<rect x="105" y="270" width="200" height="130" rx="16" fill="none" stroke="{CREAM}" stroke-width="4"/>
<text x="205" y="300" text-anchor="middle" font-family="'Inter',sans-serif" font-weight="600" font-size="15" letter-spacing="3" fill="{CREAM}" fill-opacity="0.8">WORLD</text>
<g stroke="{CREAM}" stroke-width="3.5" fill="none"><rect x="135" y="320" width="56" height="28" rx="14"/><rect x="220" y="320" width="56" height="28" rx="14"/><rect x="135" y="360" width="141" height="14" rx="7" stroke-opacity="0.6"/></g>
<circle cx="177" cy="334" r="10" fill="{ACC}"/><circle cx="234" cy="334" r="10" fill="{CREAM}"/>
<g stroke="{ACC}" stroke-width="5" fill="none" stroke-linecap="round" marker-end="url(#aa)">
<path d="M70,215 Q80,300 125,325"/><path d="M340,225 Q335,300 290,325"/></g>'''
card('tau2','#0e5a61','τ²','DUAL-CONTROL AGENTS',m)

# ---- tau-voice: full-duplex
def wave(y,amp,color,phase=0,n=46,x0=0,dx=8,op=1):
    import math
    pts=[]
    for i in range(n):
        a=amp*(0.35+0.65*abs(math.sin(i*0.55+phase)))*(1 if (i+int(phase*3))%9 else 0.15)
        x=x0+i*dx
        pts.append(f'<line x1="{x}" y1="{y-a}" x2="{x}" y2="{y+a}"/>')
    return f'<g stroke="{color}" stroke-width="4.5" stroke-linecap="round" stroke-opacity="{op}">'+"".join(pts)+'</g>'
m=person(30,60,0.8)+robot(4,262,58,48,stroke=ACC,sw=3.5)
m+=wave(140,44,CREAM,0.3,x0=110,n=34)+wave(290,38,ACC,1.7,x0=110,n=34)
m+=f'''<g font-family="'Inter',sans-serif" font-weight="600" font-size="15" letter-spacing="3" fill-opacity="0.85">
<text x="0" y="200" fill="{CREAM}">USER</text><text x="-6" y="352" fill="{ACC}">AGENT</text></g>
<g stroke="{CREAM}" stroke-width="2" stroke-dasharray="4 8" stroke-opacity="0.5"><line x1="110" y1="215" x2="380" y2="215"/></g>
<g font-family="'Inter',sans-serif" font-weight="600" font-size="14" letter-spacing="2.5" fill="{CREAM}" fill-opacity="0.7"><text x="110" y="395">BOTH TALKING AT ONCE</text></g>'''
card('voice','#7a2f2a',sub('voice'),'FULL-DUPLEX VOICE',m)

# ---- NAACL: answers -> explanations (causal graph)
nodes={'Q':(30,200),'A':(140,80),'B':(140,320),'C':(260,140),'D':(260,300),'E':(370,215)}
def edge(a,b,col=CREAM,w=3.5,dash=None,mk="ac"):
    (x1,y1),(x2,y2)=nodes[a],nodes[b]
    import math
    d=math.hypot(x2-x1,y2-y1); ux,uy=(x2-x1)/d,(y2-y1)/d; r=28
    da=f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1+ux*r}" y1="{y1+uy*r}" x2="{x2-ux*(r+6)}" y2="{y2-uy*(r+6)}" stroke="{col}" stroke-width="{w}"{da} marker-end="url(#{mk})"/>'
m=edge('Q','B')+edge('B','D')+edge('D','E')+edge('A','D',dash="8 8")
m+=edge('Q','A',ACC,6,mk="aa")+edge('A','C',ACC,6,mk="aa")+edge('C','E',ACC,6,mk="aa")
for k,(x,y) in nodes.items():
    col=ACC if k in 'QACE' else CREAM
    m+=f'<circle cx="{x}" cy="{y}" r="26" fill="none" stroke="{col}" stroke-width="4"/>'
m+=f'<circle cx="{nodes["E"][0]}" cy="{nodes["E"][1]}" r="34" fill="none" stroke="{ACC}" stroke-width="2.5"/>'
m+=f'''<g font-family="'EB Garamond',serif" font-size="34" fill="{CREAM}" text-anchor="middle">
<text x="78" y="128">+</text><text x="212" y="98">+</text><text x="330" y="160">+</text><text x="70" y="290">−</text><text x="212" y="330">−</text><text x="330" y="285">+</text></g>
<text x="30" y="212" text-anchor="middle" font-family="'EB Garamond',serif" font-size="30" fill="{ACC}">?</text>'''
card('naacl','#8a3a14','∴','ANSWERS → EXPLANATIONS',m)

# ---- LLM-ARC: actor <-> critic
m=f'''<g stroke="{CREAM}" stroke-width="4" fill="none"><circle cx="90" cy="170" r="78"/><circle cx="300" cy="170" r="78" stroke="{ACC}"/></g>
<g font-family="'EB Garamond',serif" font-size="40" text-anchor="middle"><text x="90" y="182" fill="{CREAM}">LLM</text><text x="300" y="182" fill="{ACC}">ASP</text></g>
<g font-family="'Inter',sans-serif" font-weight="600" font-size="14" letter-spacing="2.5" text-anchor="middle" fill="{CREAM}" fill-opacity="0.8"><text x="90" y="72">ACTOR</text><text x="300" y="72">CRITIC</text><text x="195" y="22">PROGRAM</text><text x="195" y="330">FAILURES</text></g>
<g stroke="{CREAM}" stroke-width="4" fill="none" stroke-linecap="round"><path d="M130,95 Q195,40 258,95" marker-end="url(#ac)"/></g>
<g stroke="{ACC}" stroke-width="4" fill="none" stroke-linecap="round"><path d="M258,245 Q195,300 130,245" marker-end="url(#aa)"/></g>
<g transform="translate(110,350)" stroke="{CREAM}" stroke-width="3" fill="none" stroke-linecap="round">
<rect x="0" y="0" width="170" height="44" rx="8"/>
<path d="M14,22 l7,7 l13,-14"/><path d="M58,22 l7,7 l13,-14"/><path d="M104,14 l14,14 M118,14 l-14,14" stroke="{ACC}"/><path d="M144,22 l7,7 l13,-14" stroke-opacity="0.35"/></g>'''
card('llmarc','#2f5234','⊢','LLM ACTOR · LOGIC CRITIC',m)

# ---- Multi-step inference
nodes={'A':(130,60),'B':(190,200),'C':(300,110),'D':(360,300)}
m=doc(-10,170,rot=-6)+doc(5,190,rot=3)+doc(20,210,rot=-1)
m+=f'<g stroke="{CREAM}" stroke-width="2.5" stroke-dasharray="3 9" stroke-linecap="round" fill="none" stroke-opacity="0.75">'
for k,(x,y) in nodes.items():
    m+=f'<path d="M70,240 Q{(70+x)/2},{y+60} {x-24},{y+10}"/>'
m+='</g>'
seq=['A','B','C','D']
import math
for i in range(3):
    (x1,y1),(x2,y2)=nodes[seq[i]],nodes[seq[i+1]]
    d=math.hypot(x2-x1,y2-y1); ux,uy=(x2-x1)/d,(y2-y1)/d
    m+=f'<line x1="{x1+ux*26}" y1="{y1+uy*26}" x2="{x2-ux*32}" y2="{y2-uy*32}" stroke="{ACC}" stroke-width="5" marker-end="url(#aa)"/>'
    mx,my=(x1+x2)/2+uy*26,(y1+y2)/2-ux*26
    m+=f'<circle cx="{mx}" cy="{my}" r="15" fill="{ACC}"/><text x="{mx}" y="{my+6}" text-anchor="middle" font-family="Inter,sans-serif" font-weight="600" font-size="17" fill="#4a2340">{i+1}</text>'
for k,(x,y) in nodes.items():
    m+=f'<circle cx="{x}" cy="{y}" r="24" fill="none" stroke="{CREAM}" stroke-width="4"/>'
m+=f'<circle cx="360" cy="300" r="32" fill="none" stroke="{ACC}" stroke-width="2.5"/>'
card('multistep','#5a2849','⇝','MULTI-STEP INFERENCE',m,glyph_size=200)

# ---- tau-i18n: languages
words=[("Hola",20,30,96,0),("Olá",270,20,86,0),("नमस्ते",0,175,124,0),("안녕하세요",254,170,146,0),("你好",50,310,86,0),("Hello",262,300,106,1)]
m=""
for w,x,y,wd,acc in words:
    col=ACC if acc else CREAM
    m+=f'''<g><rect x="{x}" y="{y}" width="{wd}" height="60" rx="16" fill="none" stroke="{col}" stroke-width="3"/>
<text x="{x+wd/2}" y="{y+41}" text-anchor="middle" font-family="'EB Garamond','Kohinoor Devanagari','Apple SD Gothic Neo','PingFang SC',serif" font-size="30" fill="{col}">{w}</text></g>'''
m+=robot(156,182,64,54,stroke=ACC,sw=3.5)
card('i18n','#1c4570',sub('i18n'),'VOICE AGENTS ACROSS LANGUAGES',m)

# ---- tau-Entity: getting the details right
letters="MARSH"
m=f'''<g transform="translate(6,22) scale(0.42)" stroke="{CREAM}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round">
<path d="M18,40 q-10,0 -10,12 q4,58 52,104 q46,44 104,52 q12,0 12,-10 v-28 q0,-8 -8,-10 l-30,-8 q-7,-2 -12,4 l-12,14 q-34,-16 -52,-52 l14,-12 q6,-5 4,-12 l-8,-30 q-2,-8 -10,-8 z"/></g>
<text x="96" y="70" font-family="'Inter',sans-serif" font-weight="600" font-size="15" letter-spacing="2.5" fill="{CREAM}" fill-opacity="0.85">“HOW DO YOU SPELL THAT?”</text>
<g font-family="'EB Garamond',serif" font-size="46" text-anchor="middle">'''
for i,ch in enumerate(letters):
    x=40+i*72; y=200
    m+=f'<rect x="{x-28}" y="{y-44}" width="56" height="64" rx="8" fill="none" stroke="{CREAM}" stroke-width="3"/><text x="{x}" y="{y+6}" fill="{CREAM}">{ch}</text>'
m+="</g>"
m+=f'''<g font-family="'EB Garamond',serif" font-size="46" text-anchor="middle">
<rect x="12" y="290" width="56" height="64" rx="8" fill="none" stroke="{ACC}" stroke-width="3" stroke-dasharray="7 6"/><text x="40" y="340" fill="{ACC}">N</text></g>
<line x1="20" y1="302" x2="60" y2="342" stroke="{ACC}" stroke-width="4" stroke-linecap="round"/>
<g stroke="{ACC}" stroke-width="4" fill="none" stroke-linecap="round"><line x1="40" y1="286" x2="40" y2="232" marker-end="url(#aa)"/></g>
<text x="86" y="328" font-family="'Inter',sans-serif" font-weight="600" font-size="15" letter-spacing="2.5" fill="{ACC}">READ BACK · REPAIR</text>
<circle cx="384" cy="150" r="17" fill="{ACC}"/><path d="M376,150 l6,6 l11,-12" stroke="#5a450e" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''
card('entity','#6b5313',sub('entity'),'GETTING THE DETAILS RIGHT',m)

# ---- tau-Knowledge: agents over unstructured knowledge
m=""
for i in range(5):
    x=10+i*12; y=60+i*14
    m+=f'<path d="M{x},{y} h96 l18,18 v110 h-114 z" fill="{"#6b2340" if True else "none"}" stroke="{CREAM}" stroke-width="3"/>'
for j in range(5):
    m+=f'<line x1="{70}" y1="{150+j*14}" x2="{150-(j%2)*20}" y2="{150+j*14}" stroke="{CREAM}" stroke-width="3" stroke-linecap="round"/>'
m+=f'''<g stroke="{ACC}" stroke-width="5" fill="none" stroke-linecap="round"><circle cx="160" cy="250" r="34"/><line x1="184" y1="274" x2="214" y2="304"/></g>
<g stroke="{CREAM}" stroke-width="2.5" stroke-dasharray="3 9" stroke-linecap="round" fill="none" stroke-opacity="0.8"><path d="M196,226 Q250,190 278,165"/></g>'''
m+=robot(270,110,90,74)
m+=f'''<g stroke="{CREAM}" stroke-width="3" fill="none" stroke-linecap="round">
<path d="M250,250 h110 a12,12 0 0 1 12,12 v26 a12,12 0 0 1 -12,12 h-86 l-16,14 v-14 h-8 a12,12 0 0 1 -12,-12 v-26 a12,12 0 0 1 12,-12 z"/></g>
<g stroke="{CREAM}" stroke-width="3" stroke-linecap="round"><line x1="262" y1="270" x2="345" y2="270"/><line x1="262" y1="284" x2="320" y2="284"/></g>'''
m+=person(330,330,0.55)
card('knowledge','#6b2340',sub('knowledge'),'AGENTS OVER RAW KNOWLEDGE',m)

# ---- AgentBeats: agentified agent assessment
m=robot(140,10,110,90,stroke=ACC,sw=4)
m+=f'''<g stroke="{ACC}" stroke-width="3" fill="none" stroke-linecap="round"><rect x="268" y="18" width="70" height="86" rx="8"/>
<path d="M282,44 l6,6 l10,-12"/><line x1="306" y1="45" x2="326" y2="45"/><path d="M282,70 l6,6 l10,-12"/><line x1="306" y1="71" x2="326" y2="71"/></g>
<g font-family="'Inter',sans-serif" font-weight="600" font-size="14" letter-spacing="2.5" fill="{ACC}" text-anchor="end"><text x="128" y="52">ASSESSOR</text><text x="128" y="72">AGENT</text></g>
<rect x="20" y="170" width="350" height="44" rx="22" fill="none" stroke="{CREAM}" stroke-width="3.5"/>
<text x="195" y="199" text-anchor="middle" font-family="'Inter',sans-serif" font-weight="600" font-size="16" letter-spacing="4" fill="{CREAM}">A2A · MCP</text>
<g stroke="{ACC}" stroke-width="4" stroke-linecap="round"><line x1="195" y1="112" x2="195" y2="166"/></g>
<g stroke="{CREAM}" stroke-width="3.5" stroke-linecap="round"><line x1="70" y1="214" x2="70" y2="262"/><line x1="195" y1="214" x2="195" y2="262"/><line x1="320" y1="214" x2="320" y2="262"/></g>'''
m+=robot(36,282,68,56)+robot(161,282,68,56)+robot(286,282,68,56)
m+=f'<g font-family="Inter,sans-serif" font-weight="600" font-size="14" letter-spacing="2.5" fill="{CREAM}" fill-opacity="0.8"><text x="112" y="392">ANY AGENT, SAME TEST</text></g>'
card('agentbeats','#3a3f47','AAA','AGENTIFIED ASSESSMENT',m,glyph_size=150,glyph_y=300)

# ---- Template Construction Grammar (2017): constructions as form-meaning schemas
def node(x,y,w,label,col=CREAM):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="46" rx="23" fill="none" stroke="{col}" stroke-width="3.5"/>'
            f'<text x="{x+w/2}" y="{y+31}" text-anchor="middle" font-family="Inter,sans-serif" font-weight="600" font-size="17" letter-spacing="2" fill="{col}">{label}</text>')
m=node(0,10,110,"WOMAN")+node(145,10,100,"KICK",ACC)+node(280,10,100,"BALL")
m+=f'''<g stroke="{CREAM}" stroke-width="3" marker-end="url(#ac)"><line x1="145" y1="33" x2="116" y2="33"/><line x1="245" y1="33" x2="274" y2="33"/></g>
<g font-family="'EB Garamond',serif" font-style="italic" font-size="19" fill="{CREAM}" fill-opacity="0.8" text-anchor="middle"><text x="128" y="84">agent</text><text x="262" y="84">patient</text></g>
<rect x="0" y="140" width="380" height="140" rx="12" fill="none" stroke="{CREAM}" stroke-width="2.5" stroke-dasharray="9 7" stroke-opacity="0.8"/>
<text x="190" y="274" text-anchor="middle" font-family="Inter,sans-serif" font-weight="600" font-size="12" letter-spacing="3" fill="{CREAM}" fill-opacity="0.75">CONSTRUCTION</text>
<g font-family="'EB Garamond',serif" font-size="30" text-anchor="middle">
<rect x="20" y="200" width="100" height="54" rx="6" fill="none" stroke="{CREAM}" stroke-width="3"/><text x="70" y="237" fill="{CREAM}">NP</text>
<rect x="145" y="200" width="100" height="54" rx="6" fill="none" stroke="{ACC}" stroke-width="3"/><text x="195" y="236" font-style="italic" fill="{ACC}">kicks</text>
<rect x="270" y="200" width="100" height="54" rx="6" fill="none" stroke="{CREAM}" stroke-width="3"/><text x="320" y="237" fill="{CREAM}">NP</text></g>
<g stroke="{ACC}" stroke-width="2.5" stroke-dasharray="4 7" stroke-linecap="round"><line x1="55" y1="58" x2="70" y2="198"/><line x1="195" y1="58" x2="195" y2="198"/><line x1="330" y1="58" x2="320" y2="198"/></g>
<text x="190" y="345" text-anchor="middle" font-family="'EB Garamond',serif" font-style="italic" font-size="32" fill="{CREAM}">the woman kicks the ball</text>'''
card('tcg','#4a3a28','TCG','CONSTRUCTIONS AS SCHEMAS',m,glyph_size=150,glyph_y=300)

# ---- Template Construction Grammar (2014): from visual scenes to sentences
m=f'''<rect x="0" y="20" width="190" height="170" rx="10" fill="none" stroke="{CREAM}" stroke-width="3"/>
<g stroke="{CREAM}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round">
<circle cx="70" cy="62" r="14"/><line x1="70" y1="76" x2="70" y2="122"/><line x1="70" y1="92" x2="46" y2="108"/><line x1="70" y1="92" x2="94" y2="104"/>
<line x1="70" y1="122" x2="56" y2="166"/><line x1="70" y1="122" x2="112" y2="146"/></g>
<circle cx="140" cy="152" r="16" fill="none" stroke="{CREAM}" stroke-width="4"/>
<g stroke="{ACC}" stroke-width="2.5" fill="none"><polyline points="66,58 128,148 92,104 70,118" stroke-dasharray="5 6"/></g>
<g fill="{ACC}"><circle cx="66" cy="58" r="9"/><circle cx="128" cy="148" r="9"/><circle cx="92" cy="104" r="9"/><circle cx="70" cy="118" r="9"/></g>
<g stroke="{ACC}" stroke-width="5" fill="none" stroke-linecap="round"><line x1="205" y1="105" x2="238" y2="105" marker-end="url(#aa)"/></g>'''
m+=node(255,20,120,"WOMAN")+node(255,82,120,"KICK",ACC)+node(255,144,120,"BALL")
m+=f'''<g stroke="{CREAM}" stroke-width="3" marker-end="url(#ac)"><line x1="315" y1="82" x2="315" y2="72"/><line x1="315" y1="128" x2="315" y2="138"/></g>
<g stroke="{ACC}" stroke-width="5" fill="none" stroke-linecap="round"><path d="M315,200 Q315,240 270,262" marker-end="url(#aa)"/></g>
<text x="190" y="305" text-anchor="middle" font-family="'EB Garamond',serif" font-style="italic" font-size="32" fill="{CREAM}">the woman kicks the ball</text>
<text x="190" y="352" text-anchor="middle" font-family="'EB Garamond',serif" font-style="italic" font-size="24" fill="{ACC}" fill-opacity="0.9">woman … kick … ball</text>
<text x="190" y="380" text-anchor="middle" font-family="Inter,sans-serif" font-weight="600" font-size="12" letter-spacing="3" fill="{ACC}" fill-opacity="0.8">AGRAMMATIC</text>'''
card('tcg-scene','#2c4a5a','TCG','FROM SCENES TO SENTENCES',m,glyph_size=150,glyph_y=300)

from PIL import Image
for name in CARDS:
    png=os.path.join(OUT,name+".png")
    subprocess.run([CHROME,"--headless=new","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=2",
                    "--virtual-time-budget=6000","--window-size=900,600",f"--screenshot={png}",
                    "file://"+os.path.join(OUT,name+".html")],check=True,capture_output=True)
    Image.open(png).convert("RGB").resize((1200,800),Image.LANCZOS).save(
        os.path.join(DEST,f"card-{name}.jpg"),quality=86,optimize=True,progressive=True)
    print("wrote", f"card-{name}.jpg")
