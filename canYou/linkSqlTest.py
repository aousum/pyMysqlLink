from mineMod import DBconfig
dbInfo=DBconfig.mysqlInfo
(db, cursor)=dbInfo.linkSql('')

def mapInsert():
    addMap={'name':'xuyupeng','type':'1','content':'nishishei'}
    res=dbInfo.Insert('cy_question',addMap,db,cursor)
    print(res)

def mapSelect():
    requestArr=['name','content','id']
    whereMap = {'name': 'xuyupeng', 'type': '1'}
    res = dbInfo.Select('cy_question', whereMap,requestArr, db, cursor)
    print(res)

def mapUpdate():
    updateMap = {'name': 'xuyupeng', 'type': '1', 'content': 'souzhuyi'}
    whereMap = {'type': '1'}
    res = dbInfo.Update('cy_question', whereMap, updateMap, db, cursor)
    print(res)

def mapDelete():
    whereMap = {'name': 'xuyupeng', 'type': '1'}
    res = dbInfo.Delect('cy_question', whereMap, db, cursor)
    print(res)


#mapInsert()
mapSelect()
#mapUpdate()
#mapDelete()