import requests
import lxml.html as lh
import pandas as pd

def extract(url):
    '''
    Gets data from the online table
    tr_elements: Stores relevant data
    '''
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    tr_elements = doc.xpath('//tr')
    return tr_elements


def getTable(tr_elements):
    col = []
    i = 0
    for t in tr_elements[0]:
        i+=1
        name = t.text_content()
        col.append((name, []))
    
    for j in range(1,len(tr_elements)): 
        T=tr_elements[j]
        if len(T)!=4:
            break    
        i=0
        for t in T.iterchildren():
            data=t.text_content()
            if i>0:
                try:
                    data = int(data)
                except:
                    pass
            col[i][1].append(data)
            i+=1
    Dict={title:column for (title,column) in col}
    df=pd.DataFrame(Dict)
    df.to_csv('ability.csv')

URL = "https://pokemondb.net/ability"
tr_elements = extract(URL)
getTable(tr_elements)
