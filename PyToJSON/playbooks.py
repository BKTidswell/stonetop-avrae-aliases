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
# \u25ef (circle)
# \uaa5c (spiral)
# \u2611 (checked box)
# \u27a4 (arrow)
# \u27A5 (indent arrow)
#

playbooks= [lookup("blessed",
                   "Blessed",
                   "The Blessed's maximum HP is 18 and their base damage is d6.\nThe Blessed starts with Spirit Tongue, Call the Spirits, 1 from their background, and 1 of their choice\n\nThese are playbook specific details to decide on:\n\nSee the Blessed's background, drive, appearence, playbook specific details, possessions, and introductory questions with these commands:\n`!st playbooks blessed backstory`\n`!st playbooks blessed drive`\n`!st playbooks blessed appearence`\n`!st playbooks blessed details`\n`!st playbooks blessed intro`\n`!st playbooks blessed items`\n\n\n_Danu, the Great Mother, provides. We need only learn her secrets: the names by which the trees call each other; the mark made with redberry juice to ward off impure spirits; the language of the wolves. A thousand such secrets Danu keeps, to share with only her true children. Her Blessed._",
                   ""),
            lookup("blessedbackstory",
                   "Blessed Background",
                   "\u20de **Initiate**\nStonetop has long been home to a sacred order, keepers of the old ways and speakers for Danu. You are one such initiate, the most gifted in generations. You gain the Rites of the Land move.\nThere are other initiates in Stonetop, serving the goddess and the village. They aid you as followers— see the Initiates of Danu insert. Who are they? Choose 2 or 3:\n\u20de Enfys, your acolyte, beloved by birds \n\u20de Afon, strange and fae-touched\n\u20de Gwendyl, your mentor, a talented healer \n\u20de Olwin, your anointed lover, seer of fates \n\u20de Seren the Eldest, wise and hard as winter\n\n**Raised by Wolves**\nMaybe not by wolves, but you grew up in the wild. Beasts of land and air were your siblings. The sighing wind taught you language. The trees and rocks were your home. Were you one of the Forest Folk? Abandoned or orphaned? Lured into the Wood?\nRegardless, you get the Trackless Step move (go mark it now). Also, when you Forage, you have advantage.\nFor some reason, you’ve made yourself known to Stonetop and perhaps you even call it home. But the ways of humans are still strange to you. Once per session, when your wild ways offend or alienate you from someone, mark XP.\n\n**Vessel**\nA seed of Danu’s power has taken root in your soul. Perhaps it has always been there and only recently sprouted. Or maybe it was planted in you during some portentous event.\nRegardless, your dreams have been haunted by strange markings and symbols. You feel the mystic power in plants, stones, and soil. And you’ve felt the growing wrath of the Earth Mother as foul things begin to move about. Take the Danu’s Grasp move (go mark it now).\nDanu’s power flows through you, but at great cost. When you would spend 1 Stock from your sacred pouch, you may choose to lose 2d4 HP instead.",
                   ""),
            lookup("blesseddrive",
                   "Blessed Drive",
                   "At the end of a session, if you’ve met your drive’s requirement, mark XP.\n\u20de Conciliation: Calm, soothe, or mollify a hostile spirit or beast.\n\u20de Cultivation: Help an NPC learn, grow, or improve themselves.\n\u20de Preservation: Convince others to protect something of natural beauty or of importance to Danu.\n\u20de Renewal: Restore someone or thing to its prior, untainted state, or defeat a perversion of the natural order.",
                   ""),
            lookup("blessedappearence",
                   "Blessed Appearence",
                   "Choose 1 on each line, or make something up:\n\n\u20de fresh faced \u20de hale & hardy\u20de gray & wizened\n\u20de imperious voice\u20de raspy voice \u20de soothing voice\n\u20de curvy \u20de strapping \u20de rail-thin \u20de solid \u20de willowy \u20de ceremonial robes \u20de furs, leather \u20de work clothes",
                   ""),
            lookup("blesseddetails",
                   "Blessed Playbook Specific Details",
                   "**Sacred Pouch**\nYour sacred pouch (magical) doesn’t take up space in your inventory. It can hold up to 3 Stock (sacred herbs, powders, stones, pigments, chalks, clay, and so forth). Each time you gain an even-numbered level, your pouch can hold +1 Stock. When anyone but you looks inside you sacred pouch and touches the materials therein, the Stock is ruined.\nWhen you have a few days of downtime in familiar terrain, you may replenish your Stock.\nWhen you Forage, you can produce Stock instead of provisions.\n\nYour sacred pouch is... (choose 1 on each line)\n\u20de an heirloom \u20de made just for you \u20de your own work \n\u20de fur \u20de drakescale \u20de leather \u20de woven \u20de demonflesh \n\u20de unadorned \u20de beadwork \u20de rich dyes \u20de runes\n\nWhat remarkable trait does it possess? (choose 1)\n\u20de It cannot be cut, torn, or burned by any natural means.\n\u20de Unless someone is specifically searching for your pouch, they will ignore its presence.\n\u20de So long as the pouch is sealed, nothing within can be detected or found by magic, nor can anything within escape or affect the outside world. \n\u20de Unnatural and unclean creatures cannot bear to touch it.\n\n**The Earth Mother**\nDanu has long been revered by all peoples, though not always worshipped or served by priests. In Stonetop’s Pavilion of the Gods, Danu’s shrine is... (choose 1)\n\u20de ... loved, well-used, dripping with offerings and petitions.\n\u20de ... little more than a token of respect, for her holy places are anywhere but here.\n\u20de ... given wide berth by most, and approached only with care and propitiation.\n\u20de ... neglected and all but forgotten, except by a few.\n\nWhat do the folk of Stonetop leave as offerings? (choose 2-3)\n\u20de fruits of harvest \n\u20de whisky/spirits \n\u20de pure rain water \n\u20de blood/burnt flesh\n\u20de figurines/effigies \n\u20de salt/crystals \n\u20de metal nails/tools \n\u20de incense/sage bark",
                   ""),
            lookup("blessedintro",
                   "Blessed Intro Questions",
                   "Answer two of the following, naming one or more NPCs who live in Stonetop.\n\u20de Who is your closest kin?\n\u20de Whose heart & soul is entwined with yours?\n\u20de Who taught you the secret ways?\n\u20de Who is beloved by the goddess, your charge to nurture/guide/protect/heal?\n\nask your fellow PCs two of these. When others ask you, answer as you like. \n\u20de Which one of you do the spirits whisper of? \n\u20de Which one of you has joined me in a sacred rite? \n\u20de Which of you has made a blood-oath with me? \n\u20de Which one of you doubts the power of Danu?",
                   ""),
            lookup("blesseditems",
                   "Blessed Special Possessions",
                   "(Pick 2, in addition to your sacred pouch)\n\n\u20de Sacred pouch (magical): `!st playbooks blessed details`. Stock: \u25ef\u25ef\u25ef\u25ef\u25ef\u25ef\u25ef\u25ef\u25ef\u25ef\u25ef\u25ef\u25ef\u25ef\u25ef\u25ef\n\n\u20de Apiary: beeswax, candles (close, lasts ~1 hr), honey, \u25c7 bee smokers, \u25c7 hat & veils, etc. \n\n\u20de Collected offerings (\u25ef\u25ef\u25ef uses): Expend a use to produce something valuable to a spirit of the wild. Restore 1 use each season.\n\n\u20de Goat herd: milk, cheese, pelts, meat, blood, horn, wool, etc. Each season, 1 in 4 chance of having a bezoar (swallow it to cure poison).\n\n\u20de Herb garden: shears, mortars & pestles, herbs, seeds, remedies, mild poisons, \u25c7 spades, etc. Each spring, d4 uses of bendis root (reach, area, burns ~1 hr, fumes repel perversions of nature). \n\n\u20de Hounds, 2-3 in number: watchdogs, keen-nosed, tough, fierce; Loyalty +2; Damage d6; HP 8; Moves: scent trouble on the wind, stand guard; Instinct: to bark & threaten; Cost: affection.",
                   ""),



            lookup("fox",
                   "Fox",
                   "The Fox's maximum HP is 16 and their base damage is d8.\nThe Fox starts with Ambush OR Skill at Arms; Danger Sense OR Perceptive, and 1 of their choice\n\nThese are playbook specific details to decide on:\n\nSee the Blessed's background, drive, appearence, playbook specific details, possessions, and introductory questions with these commands:\n`!st playbooks fox backstory`\n`!st playbooks fox drive`\n`!st playbooks fox appearence`\n`!st playbooks fox details`\n`!st playbooks fox intro`\n`!st playbooks fox items`\n\n\n_The elders tell a story about Fox, who knows lots of tricks, and Hedgehog, who knows one: how to curl up into a ball when there’s danger. Fox can’t eat Hedgehog when he’s all curled up, so in the story Fox goes hungry. But you’re not that Fox, and this is no story. You want that Hedgehog? Go get a knife._",
                   ""),
            lookup("foxbackstory",
                   "Fox Background",
                   "\u20de The Natural\nYou grew up around here, and always picked things up quickly. Reading and numbers, sure, but more. Hide and seek. Throwing stones. Climbing. Fighting. Whatever you tried, you were good at it. As good as anyone else, if not better.\nSure, you’ve got a reputation for bending the rules. Playing dirty. But why play if you don’t play to win, right? And who do they come to when there’s a problem needs solving? You, that’s who.\nWhen you Seek Insight, you may roll +INT instead of +WIS and add 'What opportunity does no one else see?' to the list of possible questions.\n\n\u20de A Life of Crime\nYou’re new to Stonetop, having left behind a... colorful past. How did you get into that life? Why and how did you get out? Who and what did you leave behind?\nRegardless, these people have taken you in. Time to lead an honest life, right?\nYou start with either Burgle or Light Fingers (your choice) as an extra move, and either burglar tools or a hidden stash (your choice) as an additional special possession. Go mark them now.\n\n\u20de The Prodigal Returned\nYou left long ago, travelling far and living by your wits. Why did you leave? What deeds do you boast of, and which do you regret?\nYou always longed to return to Stonetop, and return you have. You’re a bit of a celebrity now, and you’ve got friends (or close enough) strewn about the known world.\nWhen you declare that you know someone outside of Stonetop, someone who can help, name them and roll +CHA: on a 10+, yeah, they can help (tell us why they’re willing); on a 7-9, they can help but pick 1 from the list below; on a 6-, the GM chooses 1 and then some.\n\uaa5c They still hold a grudge\n\uaa5c They’re going to need something from you first\n\uaa5c They swore off this sort of thing long ago\n\uaa5c You can’t exactly, y’know, trust them",
                   ""),
            lookup("foxdrive",
                   "Fox Drive",
                   "At the end of a session, if you’ve met your drive’s requirement, mark XP.\n\u20de Conscience: Forego comfort or advantage to do the right thing.\n\u20de Excitement: Cause an ally trouble by taking an unnecessary risk.\n\u20de Glory: Show off in front of NPCs who will tell your tale.\n\u20de Romance:Get intimate with someone you’re attracted to.\n\u20de Trickery: Get someone or thing to act on false information.",
                   ""),
            lookup("foxappearence",
                   "Fox Appearence",
                   "Choose 1 on each line, or make something up:\n\u20de young pup \u20de “responsible” adult \u20de cagey old-timer \n\u20de a pleasant voice \u20de sharp & nasally \u20de well-spoken \n\u20delithe \u20de heavyset \u20de gangly \u20de like a whippin’ stick \n\u20de a light step \u20de a brisk stride \u20de more like a strut",
                   ""),
            lookup("foxdetails",
                   "Fox Playbook Specific Details",
                   "Someone like you gets into all sorts of trouble, whether you mean to or not. Mix and match the following to come up with a couple of your more memorable adventures, and write them down in the space at the bottom of this column.\n\nThere was that time that you... (choose 1 per tale)\n\u20de ... got lost in (choose 1) \u20de the Great Wood \u20de the Flats \u20de the Steplands Ferrier’s Fen \u20de the Foothills \u20de the Hufel Peaks\n\u20de ... were on watch when the crinwin raided\n\u20de ... dared each other to explore the Ruined Tower \n\u20de ... managed to rile up a small band of Hillfolk \n\u20de ... braved the Labyrinth, just a little\n\u20de ... stole that crazy old man’s book\n\u20de ... went poking about the old Barrow Mounds\n\nAnd you ended up... (choose 1 or 2 per tale)\n\u20de ... running for your life from \_\_\_\_\_\_\n\u20de ... landing a well-placed blow\n\u20de ... interrupting a strange, creepy gathering \n\u20de ... stumbling on a beast, bigger’n anything \n\u20de ... with a sack full of treasure\n\u20de ... getting \_\_\_\_\_\_ to fight them for you \n\u20de ... face to face with a ghost/fae/demon\n\u20de ... finding those strange old runes\n\u20de ... getting to know that fine-looking fellow/lady/person/couple\n\nBut all you’ve got left to show for it is...\n\u20de ... a story no one believes.\n\u20de ... a nasty scar; wanna see?\n\u20de ... the occasional nightmare.\n\u20de ... this map with runes no one can read. \n\u20de ... this key that opens who-knows-what.",
                   ""),
            lookup("foxintro",
                   "Fox Intro Questions",
                   "Answer two of the following, naming one or more NPCs who live in Stonetop.\n\u20de Who is your closest kin?\n\u20de Who holds the reins to your heart?\n\u20de Whose respect means the world to you?\n\u20de To whom do you owe a debt that cannot be repaid? \n\nAsk your fellow PCs two of these. When others ask you, answer as you like. \n\u20de Which one of you joined me in my latest hijinx? \n\u20de Which one of you brings your problems to me? \n\u20de Which one of you saved my bacon, mor’n once? \n\u20de Which one of you trusts me not one bit?",
                   ""),
            lookup("foxitems",
                   "Fox Special Possessions",
                   "\u20de Burglar’s kit: picks, files, snippers, wire, \u25c7 prybars, \u25c7 hacksaws, \u25c7 a lantern (\u25ef\u25ef\u25ef\u25ef\u25ef hours, reach, area), a grappling hook, etc. \n\u20de Carpenter’s tools: chisels, files, nails, pitch, \u25c7 prybars, \u25c7 saws, \u25c7\u25c7 firkins, barrels, etc.\n\u20de Distillery: skins of fine whisky (\u25ef\u25ef uses, grants advantage to Persuade), copper tubes, malt, \u25c7\u25c7 firkins, stills, barrels, etc.\n\u20de Hidden stash (\u25ef\u25ef\u25ef uses): each use produces valuables worth a purse of silvers\n\u20de Mummer’s kit: juggling balls, whirlybird seeds, motley, ribbons, bells, \u25c7 puppets, \u25c7 a fiddle, etc. \n\u20de Scribe’s tools: parchment, ink, pigments, vials, quills, \u25c7 a notebook, etc.\n\u20de Tannery (or access to it): lime, acid, salts, thick gloves, \u25c7 a boiled leather cuirass (1 armor), etc. \n\u20de Trading contacts: small amounts of salt, glass, silk, spice, medicinal herbs, pigments, ivory, etc.",
                   ""),



            lookup("",
                   "",
                   "The Blessed's maximum HP is 18 and their base damage is d6.\nThe Blessed starts with Spirit Tongue, Call the Spirits, 1 from their background, and 1 of their choice\n\nThese are playbook specific details to decide on:\n\nSee the Blessed's background, drive, appearence, playbook specific details, possessions, and introductory questions with these commands:\n`!st playbooks blessed backstory`\n`!st playbooks blessed drive`\n`!st playbooks blessed appearence`\n`!st playbooks blessed details`\n`!st playbooks blessed intro`\n`!st playbooks blessed items`",
                   ""),
            lookup("backstory",
                   " Background",
                   "",
                   ""),
            lookup("drive",
                   " Drive",
                   "",
                   ""),
            lookup("appearence",
                   " Appearence",
                   "",
                   ""),
            lookup("details",
                   " Playbook Specific Details",
                   "",
                   ""),
            lookup("intro",
                   " Intro Questions",
                   "Answer two of the following, naming one or more NPCs who live in Stonetop.\n\u20de \n\nAsk your fellow PCs two of these. When others ask you, answer as you like. \n\u20de ",
                   ""),
            lookup("items",
                   " Special Possessions",
                   "",
                   ""),



            lookup("",
                   "",
                   "The Blessed's maximum HP is 18 and their base damage is d6.\nThe Blessed starts with Spirit Tongue, Call the Spirits, 1 from their background, and 1 of their choice\n\nThese are playbook specific details to decide on:\n\nSee the Blessed's background, drive, appearence, playbook specific details, possessions, and introductory questions with these commands:\n`!st playbooks blessed backstory`\n`!st playbooks blessed drive`\n`!st playbooks blessed appearence`\n`!st playbooks blessed details`\n`!st playbooks blessed intro`\n`!st playbooks blessed items`",
                   ""),
            lookup("backstory",
                   " Background",
                   "",
                   ""),
            lookup("drive",
                   " Drive",
                   "",
                   ""),
            lookup("appearence",
                   " Appearence",
                   "",
                   ""),
            lookup("details",
                   " Playbook Specific Details",
                   "",
                   ""),
            lookup("intro",
                   " Intro Questions",
                   "Answer two of the following, naming one or more NPCs who live in Stonetop.\n\u20de \n\nAsk your fellow PCs two of these. When others ask you, answer as you like. \n\u20de ",
                   ""),
            lookup("items",
                   " Special Possessions",
                   "",
                   ""),



            lookup("",
                   "",
                   "The Blessed's maximum HP is 18 and their base damage is d6.\nThe Blessed starts with Spirit Tongue, Call the Spirits, 1 from their background, and 1 of their choice\n\nThese are playbook specific details to decide on:\n\nSee the Blessed's background, drive, appearence, playbook specific details, possessions, and introductory questions with these commands:\n`!st playbooks blessed backstory`\n`!st playbooks blessed drive`\n`!st playbooks blessed appearence`\n`!st playbooks blessed details`\n`!st playbooks blessed intro`\n`!st playbooks blessed items`",
                   ""),
            lookup("backstory",
                   " Background",
                   "",
                   ""),
            lookup("drive",
                   " Drive",
                   "",
                   ""),
            lookup("appearence",
                   " Appearence",
                   "",
                   ""),
            lookup("details",
                   " Playbook Specific Details",
                   "",
                   ""),
            lookup("intro",
                   " Intro Questions",
                   "Answer two of the following, naming one or more NPCs who live in Stonetop.\n\u20de \n\nAsk your fellow PCs two of these. When others ask you, answer as you like. \n\u20de ",
                   ""),
            lookup("items",
                   " Special Possessions",
                   "",
                   ""),



            lookup("",
                   "",
                   "The Blessed's maximum HP is 18 and their base damage is d6.\nThe Blessed starts with Spirit Tongue, Call the Spirits, 1 from their background, and 1 of their choice\n\nThese are playbook specific details to decide on:\n\nSee the Blessed's background, drive, appearence, playbook specific details, possessions, and introductory questions with these commands:\n`!st playbooks blessed backstory`\n`!st playbooks blessed drive`\n`!st playbooks blessed appearence`\n`!st playbooks blessed details`\n`!st playbooks blessed intro`\n`!st playbooks blessed items`",
                   ""),
            lookup("backstory",
                   " Background",
                   "",
                   ""),
            lookup("drive",
                   " Drive",
                   "",
                   ""),
            lookup("appearence",
                   " Appearence",
                   "",
                   ""),
            lookup("details",
                   " Playbook Specific Details",
                   "",
                   ""),
            lookup("intro",
                   " Intro Questions",
                   "Answer two of the following, naming one or more NPCs who live in Stonetop.\n\u20de \n\nAsk your fellow PCs two of these. When others ask you, answer as you like. \n\u20de ",
                   ""),
            lookup("items",
                   " Special Possessions",
                   "",
                   ""),



            lookup("",
                   "",
                   "The Blessed's maximum HP is 18 and their base damage is d6.\nThe Blessed starts with Spirit Tongue, Call the Spirits, 1 from their background, and 1 of their choice\n\nThese are playbook specific details to decide on:\n\nSee the Blessed's background, drive, appearence, playbook specific details, possessions, and introductory questions with these commands:\n`!st playbooks blessed backstory`\n`!st playbooks blessed drive`\n`!st playbooks blessed appearence`\n`!st playbooks blessed details`\n`!st playbooks blessed intro`\n`!st playbooks blessed items`",
                   ""),
            lookup("backstory",
                   " Background",
                   "",
                   ""),
            lookup("drive",
                   " Drive",
                   "",
                   ""),
            lookup("appearence",
                   " Appearence",
                   "",
                   ""),
            lookup("details",
                   " Playbook Specific Details",
                   "",
                   ""),
            lookup("intro",
                   " Intro Questions",
                   "Answer two of the following, naming one or more NPCs who live in Stonetop.\n\u20de \n\nAsk your fellow PCs two of these. When others ask you, answer as you like. \n\u20de ",
                   ""),
            lookup("items",
                   " Special Possessions",
                   "",
                   ""),



            lookup("",
                   "",
                   "The Blessed's maximum HP is 18 and their base damage is d6.\nThe Blessed starts with Spirit Tongue, Call the Spirits, 1 from their background, and 1 of their choice\n\nThese are playbook specific details to decide on:\n\nSee the Blessed's background, drive, appearence, playbook specific details, possessions, and introductory questions with these commands:\n`!st playbooks blessed backstory`\n`!st playbooks blessed drive`\n`!st playbooks blessed appearence`\n`!st playbooks blessed details`\n`!st playbooks blessed intro`\n`!st playbooks blessed items`",
                   ""),
            lookup("backstory",
                   " Background",
                   "",
                   ""),
            lookup("drive",
                   " Drive",
                   "",
                   ""),
            lookup("appearence",
                   " Appearence",
                   "",
                   ""),
            lookup("details",
                   " Playbook Specific Details",
                   "",
                   ""),
            lookup("intro",
                   " Intro Questions",
                   "Answer two of the following, naming one or more NPCs who live in Stonetop.\n\u20de \n\nAsk your fellow PCs two of these. When others ask you, answer as you like. \n\u20de ",
                   ""),
            lookup("items",
                   " Special Possessions",
                   "",
                   ""),



            lookup("",
                   "",
                   "The Blessed's maximum HP is 18 and their base damage is d6.\nThe Blessed starts with Spirit Tongue, Call the Spirits, 1 from their background, and 1 of their choice\n\nThese are playbook specific details to decide on:\n\nSee the Blessed's background, drive, appearence, playbook specific details, possessions, and introductory questions with these commands:\n`!st playbooks blessed backstory`\n`!st playbooks blessed drive`\n`!st playbooks blessed appearence`\n`!st playbooks blessed details`\n`!st playbooks blessed intro`\n`!st playbooks blessed items`",
                   ""),
            lookup("backstory",
                   " Background",
                   "",
                   ""),
            lookup("drive",
                   " Drive",
                   "",
                   ""),
            lookup("appearence",
                   " Appearence",
                   "",
                   ""),
            lookup("details",
                   " Playbook Specific Details",
                   "",
                   ""),
            lookup("intro",
                   " Intro Questions",
                   "Answer two of the following, naming one or more NPCs who live in Stonetop.\n\u20de \n\nAsk your fellow PCs two of these. When others ask you, answer as you like. \n\u20de ",
                   ""),
            lookup("items",
                   " Special Possessions",
                   "",
                   ""),

]