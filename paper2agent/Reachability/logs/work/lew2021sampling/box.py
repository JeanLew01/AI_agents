import sys,os,subprocess
from PIL import Image, ImageDraw
S=os.path.expanduser('~/AI_agents/paper2agent/Reachability/logs/work/lew2021sampling')
PDF=os.path.expanduser('~/AI_agents/paper2agent/Reachability/paper-review/lew2021sampling-paper/documents/s001-lew2021sampling/source.pdf')
DPI=200
def page(n):
    f=f'{S}/hi-{n:02d}.png'
    if not os.path.exists(f):
        subprocess.run(['pdftoppm','-r',str(DPI),'-f',str(n),'-l',str(n),'-png','-singlefile',PDF,f[:-4]],check=True)
    return Image.open(f).convert('RGB')
n=int(sys.argv[1]); x0,y0,x1,y1=map(float,sys.argv[2:6]); name=sys.argv[6]; pad=float(sys.argv[7]) if len(sys.argv)>7 else 12
im=page(n); s=DPI/72
d=ImageDraw.Draw(im); d.rectangle([x0*s,y0*s,x1*s,y1*s],outline=(255,0,255),width=1)
c=im.crop((int((x0-pad)*s),int((y0-pad)*s),int((x1+pad)*s),int((y1+pad)*s)))
c.save(f'{S}/{name}.png'); print(c.size)
