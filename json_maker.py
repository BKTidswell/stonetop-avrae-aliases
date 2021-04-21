
import json
from PyToJSON.moves import *
from PyToJSON.tags import *
from PyToJSON.minor_arcana import *
from PyToJSON.major_arcana import *
from PyToJSON.gm import *
from PyToJSON.players import *
from PyToJSON.steading import *
from PyToJSON.playbooks import *
from PyToJSON.invocations import *


#-f \"{footer}|_ _

json_format = """-title \"{title}\" -desc \"{desc}\""""

outDict = {}

toJSON = [moves,tags,minor_arcana,major_arcana,gm,players,steading,playbooks,invocations]
names = ["moves.json","tags.json","minor_arcana.json","major_arcana.json","gm.json","players.json","steading.json","playbooks.json","invocations.json"]

for i,collection in enumerate(toJSON):

    outDict = {}

    for entry in collection:
        outDict[entry.key] = json_format.format(title = entry.title, desc = entry.desc, footer = entry.footer)

    with open("JSON/"+names[i], 'w') as outfile:
        json.dump(outDict, outfile, indent=4)