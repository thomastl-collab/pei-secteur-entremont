import json,sys
from shapely.geometry import shape, mapping
from shapely.ops import transform
from pyproj import Transformer
d=sys.argv[1]
to93=Transformer.from_crs(4326,2154,always_xy=True).transform
to84=Transformer.from_crs(2154,4326,always_xy=True).transform
codes={'61445','61070','61078','61281','61292','14174'}
fs=[]
for dep in ('61','14'):
    fs+=json.load(open(f'{d}/com_{dep}.geojson'))['features']
com=[]
for f in fs:
    p=f['properties']
    if p['code'] not in codes: continue
    g=transform(to93,shape(f['geometry'])).simplify(15)
    polys=[g] if g.geom_type=='Polygon' else list(g.geoms)
    rings=[[[round(x),round(y)] for x,y in pl.exterior.coords] for pl in polys]
    c=g.representative_point()
    com.append({'code':p['code'],'nom':p['nom'],'pop':p.get('population'),'rings':rings,'lab':[round(c.x),round(c.y)]})
pei=[]
o=json.load(open(f'{d}/data61.json'))
for r in o['rows']:
    m=dict(zip(o['cols'],r))
    lon,lat=to84(m['x'],m['y'])
    nat=m['nature']
    k={'Poteau incendie':'PI','Bouche incendie':'BI','Point d\'eau naturel':'PN','Point d\'eau artificiel':'PA','Dispositif d\'aspiration':'DA'}[nat]
    pei.append({'id':m['num'],'k':k,'nat':nat,'deci':m['deci'],'adr':m['adresse'],'cpl':m['compl'] or '','insee':m['insee'],'cis':m['cis'].replace('CIS ',''),
      'ps':m['pstat'],'pd':m['pdyn'],'q':m['debit'],'dn':(m['diam'] or '').replace('DIAM','') or None,'cap':m['cap'] if k in('PN','PA','DA') else None,
      'st':m['dispo'],'ano':m['anomalies'] or '','rop':m['rop'],'ctp':m['ctp'],'x':round(m['x']),'y':round(m['y']),'lat':round(lat,6),'lon':round(lon,6),'src':'61'})
c=json.load(open(f'{d}/data14.json'))
fam={1:('PI','Poteau incendie'),2:('BI','Bouche incendie'),3:('PA','Réserve incendie')}
for r in c['rows']:
    m=dict(zip(c['cols'],r)); k,nat=fam[m['famille']]
    lon,lat=to84(m['x'],m['y'])
    pei.append({'id':m['num'],'k':k,'nat':nat,'code':m['type'],'deci':None,'adr':'','cpl':'','insee':'14174','cis':'SDIS 14',
      'ps':None,'pd':None,'q':None,'dn':None,'cap':None,'st':'D' if m['etat']=='DI' else 'I','ano':'','rop':m['ro'],'ctp':m['ct'],
      'x':m['x'],'y':m['y'],'lat':round(lat,6),'lon':round(lon,6),'src':'14'})
print('const COM='+json.dumps(com,ensure_ascii=False,separators=(',',':'))+';')
print('const PEI='+json.dumps(pei,ensure_ascii=False,separators=(',',':'))+';')
