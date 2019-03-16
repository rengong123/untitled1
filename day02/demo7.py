if __name__ == '__main__':
    mdict={'name':'good','age':'18',('addr'):'gun'}
    print(mdict)
    aditc=({'one':1,'two':2,'three':3})
    print('create not null way1->type=',aditc)
    pass
    bditc=dict({'one':1,'tow':2,'three':3})
    print('create not null way2->type=',bditc)
    pass
    cdict=dict(one=1,tow=2,three=3)
    print('create not null way3->type=',cdict)
    ddict=dict([('one',1),('tow',2),('three',3)])
    print('create not null way4->type=',ddict)
    alien_0={'color':'green'}
    print(alien_0['color'])
    pass
    edict={'name':'good','age':'18'}
    edict['addr']='beijing-haidian'
    print(edict)
    del edict['addr']
    print(edict)
    del edict['name']
    print(edict)
    edict.__len__()
    print(edict)
    print(edict.__len__())
    edict['addr']='aaaaa'
    print(edict)
    print(edict.__len__())
    edict['name']='good'
    print(edict)
    print(edict.__len__())
    print(edict.__str__())
    print(type(edict))
    fdict={'name':'lucky','age':'20',('addr'):'gun'}
    mstrdict=str(fdict)
    print(type(mstrdict))
    print('mstrdict = ',mstrdict)
    pass
    jdict={'name':'lucky',"age":'20',('addr'):'gun'}
    dictlen=len(jdict)
    print(dictlen)
    print(jdict)
    pass
    hdict={'name':'lucky','age':'20',('addr'):'gun'}
    mtype=(type(hdict))
    print(mtype)
    pass
    idict=dict([('one',1),('tow',2),('three',3),('four',4),('five',5),('six',6)])
    print('creat not null way4->type = ',idict)
    m1=idict['one']
    print('idict[one]=',m1)
    pass
    gdict=dict([('one',1),('tow',2),('thrre',3),('four',4),("five",5),('six',6)])
    print('create not null way4->type=',gdict)
    pass
    del gdict['one']
    print('after del dict = ',gdict)
    pass
    kdict=dict([('one',1),('tow',2),('three',3),('four',4),('five',5),('six',6)])
    for k in  kdict:
        print('way1->dict[{0}]={1}'.format(k,kdict))
    pass
    ldict =dict([('one',1),('tow',2),('three',3),('four',4),('five',5),('six',6)])
    for k in ldict.keys():
        print('way2->dict[{0}]={1}'.format(k,ldict))
    pass
    for v in ldict.values():
        print('way3->ldict[{1}]={0}'.format(v.__index__(),v))
    pass
    ndict=dict([('one',1),('tow',2),('three',3),('four',4),('five',5),('six',6)])
    for k,v in ndict.items():
        print('way4->ndict[{1}]={0}'.format(v,k))
    pass
    odict={k:v for k,v in mdict.items()}
    print('odict = ',odict)
    odict = {k: v for k, v in mdict.items()}
    print('odict = ', odict)
    pass
    pdict = {k:v for k,v in ldict.items() if v % 2 == 0 }
    print('pdict with option = ', pdict)
    pass
    print(ldict.__len__())
    mlen=len(ldict)
    print('len of dict = ',mlen)
    pass
    maxdict=max(ldict)
    print('max of  dict = ',maxdict)
    mindict =min(ldict)
    print('min of dict = ',mindict)
    pass
    di=ldict.items()
    print('type of items = ',type(di))
    print(di)
    pass
    nk=ldict.keys()
    print('type of keys = ',type(nk))
    print(nk)
    pass
    nk =ndict.values()
    print('type of values = ',type(nk))
    print(nk)
    pass
    abdict={'name':'lucky','age':'20'}
    abdict['addr']='beijing haidain'
    print(abdict)
    del abdict['addr']
    print(abdict)
    pass
    acdict={'name':'good',"age":"20"}
    del acdict
    #print(acdict)
    pass
    ng=ldict.get('tow')
    print('type of get = ',type(ng))
    print(ng)
    pass
    ldict.clear()
    print('after clear of dict = ',ldict)
    pass



