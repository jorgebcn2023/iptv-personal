import requests, yaml

cfg=yaml.safe_load(open('config/settings.yml'))
seen=set()
out=['#EXTM3U']

for source in open('sources.txt'):
    try:
        txt=requests.get(source.strip(),timeout=30).text
    except:
        continue
    lines=txt.splitlines()
    for i,l in enumerate(lines):
        if l.startswith('#EXTINF') and i+1 < len(lines):
            url=lines[i+1]
            block=(l+' '+url).lower()
            if url not in seen and any(x.lower() in block for x in cfg['keep']):
                out += [l,url]
                seen.add(url)

open('playlist.m3u','w',encoding='utf8').write('\n'.join(out))
print(len(seen))
