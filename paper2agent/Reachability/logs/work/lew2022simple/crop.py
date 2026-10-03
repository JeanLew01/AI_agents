"""crop.py PAGE L T R B [dpi] [pad] -> SCRATCH/crop-pPP-L-T.png : renders bbox (PDF points) with pad, red outline at bbox."""
import sys, subprocess, os
from PIL import Image, ImageDraw
S=os.path.dirname(os.path.abspath(__file__))
D=os.path.expanduser('~/AI_agents/paper2agent/Reachability/paper-review/lew2022simple-paper/documents/s001-lew2022simple')
pg=int(sys.argv[1]); l,t,r,b=[float(x) for x in sys.argv[2:6]]
dpi=int(sys.argv[6]) if len(sys.argv)>6 else 200
pad=float(sys.argv[7]) if len(sys.argv)>7 else 14
sc=dpi/72
x0=max(0,l-pad); y0=max(0,t-pad); x1=min(612,r+pad); y1=min(792,b+pad)
out=f'{S}/crop-p{pg:02d}-{int(l)}-{int(t)}'
subprocess.run(['pdftoppm','-r',str(dpi),'-f',str(pg),'-l',str(pg),'-x',str(int(x0*sc)),'-y',str(int(y0*sc)),'-W',str(int((x1-x0)*sc)),'-H',str(int((y1-y0)*sc)),'-png','-singlefile',D+'/source.pdf',out],check=True)
im=Image.open(out+'.png').convert('RGB'); d=ImageDraw.Draw(im)
if pad>0:
    d.rectangle([(l-x0)*sc,(t-y0)*sc,(r-x0)*sc,(b-y0)*sc],outline=(255,0,0),width=1)
im.save(out+'.png'); print(out+'.png', im.size)
