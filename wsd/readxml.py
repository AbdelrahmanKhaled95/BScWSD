# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 22:01:47 2017

@author: AbdelrahmanHussein
"""
def readinputfile():
    from xml.dom import minidom
    xmldoc = minidom.parse(r'.\semeval_2015_task_13_(multilingual)\trial\trialInput.xml')
    itemlist = xmldoc.getElementsByTagName('wf')
    #print(len(itemlist))
    #print(itemlist[0].attributes['lemma'].value)
    sentence=''
    for s in itemlist:
        sentence=sentence+' '+str((s.attributes['lemma'].value)) 
    return str(sentence)
    