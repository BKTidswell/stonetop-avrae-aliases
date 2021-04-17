class lookup:
  def __init__(self, key, title, desc, footer):
    self.key = key
    self.title = title
    self.desc = desc
    self.footer = footer

# Regex [^\x00-\x7F]

#\n \uaa5c
# \u25c7 (diamond)
# \u20de (square)
# \u20de (circle)
# \uaa5c (spiral)
# \u2611 (checked box)
# \u27a4 (arrow)
# \u27A5 (indent arrow)
#

steading = [lookup("aurochshunting",
                   "Aurochs Hunting",
                   "Larger herds form on the Flats each spring. The Hillfolk hunt them, but none from Stonetop have learned to do so.\n\nRequires 2 of the following:\n\u20de A Herd of Horses (and hunters to ride them)\n\u20de Cooperating with the Hillfolk\n\u20de A cunning plan\nAnd then:\n\u20de A successful first hunt (played out in detail)\n\nWhen you meet the requirements, add 'Aurochs hunting (meat, hide, horn)' to the Resources list.\nHenceforth, when you lead the aurochs hunt in spring, roll +Fortunes: on a 10+, gain 1d4 Surplus; on a 7-9, gain 1d4 Surplus but pick 1 from the list below:\n\uaa5c 1d4 of the town's horses are lamed or killed\n\uaa5c A number of townsfolk are injured; take -1 Fortunes\n\uaa5c The GM picks an NPC present for the hunt; they are killed\n\uaa5c The Hillfolk are somehow offended\n\uaa5c The herd is weak; if you hunt next year they'll be wiped out",
                   ""),
            lookup("expandedhousing",
                   "Expanded Housing",
                   "Things are getting crowded. We could use more room to live.\n\nRequires either:\n\u20de An engineer/foreman of considerable skill, to design much roomier houses on the current land\nor:\n\u20de Building on parts of the fields, resulting in a -1 Surplus generated with each autumn's harvest\nAnd then:\n\u20de\u20de\u20de\u20de\u20de Pulling together 5 times, each requiring 1 season, 1 Surplus, and a cartload of timber and other supplies (Value 2), to (re)build homes.\n\nWhen you mark all the requirements, increase Fortunes by 1 and add 'Expanded Housing' to the Resources list.\nHenceforth, when a season ends and your Fortunes are +3, reset Fortunes to +1 (instead of +0).",
                   ""),
            lookup("divertingthestream",
                   "Diverting the Stream",
                   "A shallow creek flows just below the town. If only it could be harnessed!\n\nRequires 2 of the following:\n\u20de Some method of making water flow uphill\n\u20de A series of aqueducts, from the stream's source back to Stonetop\n\u20de A reservoir to contain the diverted water\n\nWhen you mark at least 2 requirements, add them to the map and the Resources list and increase Fortunes by 1.\nHenceforth, you when you roll +Fortunes for the Seasons Changing to spring, summer, or autumn, you have advantage.",
                   ""),
            lookup("farreachingreputation",
                   "Far-Reaching Reputation",
                   "Few have heard of Stonetop's heroes. Yet. Requires any 3 of the following:\n\u20de Impressing a tribe of Hillfolk with your bravery and prowess\n\u20de Braving a lake and coming back with proof\n\u20de Saving many Marshedge residents' lives\n\u20de Saving someone from beyond Marshedge\n\u20de Paying a wandering minstrel a purse of silver to tell your tales\n\nWhen you mark at least 3 of the requirements, increase Fortunes by 1.\nHenceforth, when you first meet someone from outside of Stonetop, whoever is most renowned rolls +Fortunes: on a 10+, say what they have heard about you or Stonetop, and gain advantage on you next move against them; on a 7-9, say what they've heard; on a 6-, the GM says what they've heard.",
                   ""),
            lookup("greaterharvest",
                   "Greater Harvest",
                   "Beyond the Old Wall, the prairie grass of the Flats chokes out any crops we try to grow.\n\nRequires 1 of the following:\n\u20de Doubling the yield of crops inside the Old Wall\n\u20de Clearing and cultivating new farmland beyond the Old Wall\n\nWhen you mark either of the requirements, increase Fortunes by 1.\nHenceforth, when the autumn harvest is complete, gain +1d4 Surplus.",
                   ""),
            lookup("herdofhorses",
                   "Herd of Horses",
                   "Sure, we've got these two nags. But imagine what we could do with a dozen or so fine steeds.\n\nRequires all of the following:\n\u20de A designated building site for a proper stable\n\u20de Pulling Together to build the stable, which requires a season, 1 Surplus, and a cartload of timber (Value 2). Add it to the map when done.\n\u20de Someone skilled in riding and training horses \n\u20de Acquiring a small herd of horses, about a dozen (through trade or by catching wild ones) \n\u20de Training/breaking them to the saddle and plow \n\u20de Additional saddles, harness, plows, etc. (Value 2) \n\u20de Pulling Together to have couple dozen villagers learn to ride, requiring 1 Season and 1 Surplus. \n\u20de Someone to mind the herd and stable, full time\n\nWhen you mark all of the requirements, increase Fortunes by 1 and replace 'a pair of sturdy draft horses' with 'a herd of horses (X)' on the Assets list (where 'X' is the number of trained horses you have). You gain the following benefits:\n\nWhen you leverage the horses to Pull Together, treat Population as 1 higher than it currently is.\nWhen the Seasons Change to summer, the herd gains d4+Fortunes foals (Value 1). Any foals from last year become yearlings (Value 2). Any yearlings from last year become horses, ready to be trained. Update the herd size accordingly. A trained horse is Value 3.\nWhen you Requisition half the herd or less, treat a 6- as a 7-9.\nWhen winter grips the land, the herd consumes 1 Surplus per 6 grown or yearling horses. For every Surplus not consumed, 1d6 horses are lost.",
                   ""),
            lookup("rainwatercollection",
                   "Improved Rainwater Collection",
                   "Filling the ancient cistern takes a lot of work. Surely we can do better!\n\nRequires all of the following, in order:\n\u20de An engineer/foreman of some skill, to design a cunning system of roofs and gutters\n\u20de Enough slate or terracotta to roof the buildings in town and build the gutters (Value 3)\n\u20de\u20de\u20de Pulling Together 3 times, each requiring 1 season and 1 Surplus\n\nWhen you mark all of the requirements, increase Fortunes by 1, add 'Improved Rainwater Collection' to the Resources list.\nHenceforth, you get +1 to all rolls to generate Surplus.",
                   ""),
            lookup("inn",
                   "Inn",
                   "The public house offers a common room and shelter for a few horses, but it's hardly a proper inn.\n\nRequires all of the following, in order: \n\u20de A designated building site\n\u20de An engineer/foreman of moderate skill \n\u20de Furnishings, equipment, and material (Value 3)\n\u20de\u20de Pulling Together 2 times, each requiring 1 season, 1 Surplus, and timber/supplies (Value 2) \n\u20de A small, devoted staff (innkeep, cook, ostler, etc.)\n\nWhen you mark all of the requirements, increase Fortunes by 1. Name the inn, add it to both the Resources list and map.\nHenceforth, when the seasons change, whoever is friendliest rolls +Fortunes: on a 10+, ask the GM 3 questions about the wider world; on a 7-9, ask 1 ques- tion; on a 6-, ask 1 question, but the GM describes some trouble that stems from the inn or its guests.",
                   ""),
            lookup("marketplace",
                   "Marketplace",
                   "Stonetop is at most an afterthought for traders in the area. We need to change that.\n\nRequires 1 of the following:\n\u20de A compelling product or service unavailable elsewhere\n\u20de Establishing some other reason to visit Stonetop (place of pilgrimage, etc.)\nand at least 2 of these:\n\u20de A proper Inn\n\u20de A dedicated site for the market itself\n\u20de A trusted arbiter, able to enforce their own rulings on matters of trade\n\nWhen you mark the necessary requirements, increase Fortunes by 1, add 'Market' to the Resources list, and add its location to the map. You gain these benefits:\n\nWhen the market has been active for at least one season, you have advantage to Trade & Barter.\nWhen the Seasons Change to spring, summer, or au- tumn and the market is active, the Market generates Surplus equal to Population (minimum 0).",
                   ""),
            lookup("mill",
                   "Mill",
                   "Hand-grinding flour takes forever. We've got plenty of potential millstones, and with a mill we'd have better bread and more time for other crafts.\n\nRequires all of the following:\n\u20de An engineer/foreman of considerable skill\n\u20de A convenient and consistently available source of power (wind on a hill, a waterwheel, a Herd of Horses, or some sort of magic)\n\u20de A designated building site that can hardness your power source.\n\u20de\u20de Pulling Together 2 times, each requiring 1 season, 1 Surplus, a cartload of timber (Value 2), and bunch of rope and supplies (Value 2). A full-time miller\n\nWhen you mark all of the requirements, increase Fortunes by 1, add 'Mill' to the Resources list, and draw it on the map. You gain these benefits:\n\nWhen you Outfit from Stonetop or Have What You Need after doing so, each of supplies has 1 extra use.\nWhen you Trade & Barter to acquire special items with a Value of 0 or 1, you have advantage.",
                   ""),
            lookup("palisade",
                   "Palisade",
                   "A wall of sharpened logs, 10' tall and encompassing all the homes on the original map.\n\nRequires all of the following, in order:\n\u20de A lot of good timber (~1,000 logs), much more than scraps from the Great Wood can provide (Value 3)\n\u20de An engineer/foreman of moderate skill\n\u20de Lots of rope, nails, pitch, and other supplies (Value 2)\n\u20de Pulling Together, costing 1 season and 1 Surplus\n\nWhen you mark all of the requirements, increase Fortunes by 1, add 'Wooden Palisade' to the Fortifica- tions list, and draw it on the map.\nWhen you take advantage of the palisade, you get advantage to Deploy.",
                   ""),
            lookup("stonewall",
                   "Stone Wall",
                   "No mere palisade of wood, but a mighty rampart around our homes. We have the stone, after all...\n\nRequires all of the following, in order:\n\u20de An engineer/foreman of exceptional skill\n\u20de A stonecutter of considerable skill Equipment, tools, and material (Value 3)\n\u20de\u20de\u20de\u20de Pulling Together 4 times, each costing 1 season, 1 Surplus, and supplies (Value 2)\n\nWhen you mark all of the requirements, add 'Stone Wall' to the Fortifications list (erase 'Palisade' if you had it), draw it on the map. You gain these benefits:\n\nWhen you take advantage of the stone wall, you get advantage to Deploy.\nWhen winter grips the land, the steading consumes 1 less Surplus than normal.",
                   ""),
            lookup("township",
                   "Township",
                   "Will this ever be more than a backwater village?\n\nRequires all of the following:\n\u20de\u20de\u20de\u20dePopulation +2 for 4 consecutive seasons\n\u20de Expanded Housing\n\u20de A formal government of some sort \n\u20de Improved Rainwater Collection OR Diverting the Stream\n\u20de\u20de Achieve 2 other improvements (other than Weapons of War or Well-Trained Militia)\n\nWhen you mark all of the requirements, change Stonetop's Size to +1 and its Population to +0. It is now possible to increase Defenses and Prosperity to a max of +2.\nHenceforth, when the season changes to spring or summer, the steading generates Surplus equal to Population+1. But when winter grips the land, roll 2d6 to reduce Surplus instead of 1d4.",
                   ""),
            lookup("weaponsofwar",
                   "Weapons of War",
                   "Spears are great, but how about axes, picks, swords?\n\nRequires either this:\n\u20de Acquiring a few dozen good swords, battleaxes, maces, flails, warhammers, etc. (Value 3)\nOr all of these:\n\u20de A smith of considerable skill, with an able staff\n\u20de A cartload of good iron ore (Value 2)\n\u20de\u20de\u20de\u20de 4 seasons of work by the smith \nAnd then:\n\u20de Pulling Together to train and drill the militia with these new weapons, requiring a season and 1 Surplus.\n\nWhen you mark all of the requirements, increase Fortunes by 1 and add 'Weapons of War' to the Fortifications list. You gain these benefits:\n\nWhen you Outfit from Stonetop or Have What You Need after doing so, you can treat maces, flails, battleaxes, all types of swords, and warhammers as common items, as if they were already on the inven- tory inserts. Battleaxes and swords have 'x piercing,' where x is the steading's current Prosperity.\nWhen you Deploy the militia by having them directly engage a foe with inferior weapons, you are acting from a positition of strength-on a 7-9, you choose the option instead of the GM.",
                   ""),
            lookup("welltrainedmilita",
                   "Well-Trained Milita",
                   "Everyone can use a spear and shield, but some hard drilling could make us a force to be reckoned with.\n\nRequires one of the following:\n\u20de A Marshal, held in high regard by the village\n\u20de A veteran warrior/tactition, able to command a crowd's respect\n\nFor each tactic below, you must then Pull Together, requiring a season of drills and practice, plus 1 Suprlus (for gear, food, and first aid).\n\n\u20de Archery: barrages, ranged ambushes, sniping, etc.\n\u20de Cavalry (requires a Herd of Horses): fighting from horseback, charges\n\u20de Formations: shield walls, wedges, phallanx, etc. \n\u20de Readiness: patrolling, reacting quickly to alarms \n\u20de Skrimishing: ambushes, harrassing, hit-and-run\n\nWhen you rely on or take advantage of a tactic that steading has trained in, you get advantage to Deploy.",
                   "")
]