from pg import *
from refs import REFS
old={i['id']:i for i in load(10)['items']}
items=[]
ids={22:'b000',23:'b001',24:'b002',25:'b003',26:'b004',27:'b005',28:'b006',29:'b007',30:'b008',31:'n01',32:'b009',33:'b010',34:'b011',35:'b012',36:'b013',37:'b014',38:'b015',39:'b016',40:'b017',41:'b018',42:'b019',43:'b020',44:'b021',45:'b022'}
for n in range(22,46):
    i='p0010-'+ids[n]
    if n==30: bbox=[107,308,505,328]
    elif n==31: bbox=[107,331,505,353]
    else: bbox=old[i]['bbox']
    items.append(T(i,bbox,REFS[n]))
items.append(O('p0010-b023',[296,740,316,753],'Page number "10" in the footer.'))
save(10, items, 'Compared with a 130 dpi render and the authors\' .bbl. References [22]-[45], one entry per item; all 24 entries read against the page. Corrections of extraction damage: [30] and [31] were merged into one item and are split; accents restored in [25] (Ábrahám; the extractor left a stray <sup>´</sup>) and [32] (Büeler); in [25] the title word is "non-linear" (hyphen confirmed in the .bbl, the extractor removed it at the line wrap); URLs in [28], [35], [37], [40] written without code markup; list-bullet prefixes removed. Page ranges use en dashes as printed.')
