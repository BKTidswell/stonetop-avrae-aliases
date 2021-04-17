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
# \u25ef (square)
# \uaa5c (spiral)
# \u2611 (checked box)
# \u27a4 (arrow)
# \u27A5 (indent arrow)
#

gm = [lookup("moves",
             "GM Moves",
             "Announce trouble (future or offscreen) \n\u27a4 Reveal an unwelcome truth\n\u27a4 Ask a provocative question\n\u27a4 Put someone in a spot\n\u27a4 Use up their resources\n\u27a4 Turn their move back on them\n\u27a4 Demonstrate a downside\n\u27a4 Hurt someone\n\u27a4 Separate them\n\u27a4 Capture someone\n\u27a4 Offer an opportunity (with or without a cost) \n\u27a4 Tell them the consequences/requirements\n\u27a4 Advance towards impending doom\n\n**Exploration**\n\u27a4 Provide a choice of paths\n\u27a4 Hint at more than meets the eye\n\u27a4 Offer riches at a price\n\u27a4 Present a discovery\n\u27a4 Point to a looming danger\n\u27a4 Introduce a danger, person, or faction \n\u27a4 Bar the way\n\n**Homefront**\n\u27a4 Present a want or need\n\u27a4 Show how others really feel\n\u27a4 Remind them of their obligations\n\u27a4 Introduce someone interesting\n\u27a4 Reveal simmering tensions\n\u27a4 Quicken a threat or crisis\n\u27a4 Play them against each other\n\u27a4 Change a relationship\n\u27a4 Show the passing of time",
             ""),
      lookup("agenda",
             "GM Agenda",
             "Portray a rich, mysterious world\n\uaa5c Punctuate the PCs' lives with adventure\n\uaa5c Play to find out what happens",
             ""),
      lookup("coreloop",
             "The Core Loop",
             "**1) Establish the situation**\n\uaa5c Frame the action\n\uaa5c Describe the environment Give details & specifics\n\uaa5c Ask questions, ask for input\n\uaa5c Portray NPCs and monsters\n\uaa5c Answer questions, clarify\n\n**2) Make a soft GM move:** provoke action and/or increase tension.\n\n**3) Ask, 'What do you do?'**\n\n**4) Resolve their actions**\n\uaa5c If they trigger a player move, do what the move says.\n\uaa5c If they roll a 6-, make a hard GM move (establish badness).\n\uaa5c If they ignore trouble, make a hard GM move (establish badness).\n\uaa5c Otherwise, say what happens.\n\n**5) Repeat**\n\uaa5c Is the situation clear and grabby? Can the PC(s) act? Back to step 3.\n\uaa5c Is the situation clear, but escalating before the PCs act? Back to step 2.\n\uaa5c Is the situation clear, but needs a nudge? Back to step 2.\n\uaa5c Is the situation unlcear? Does it need clarification, recapping, or updating? Back to step 1.\n\uaa5c Is the current scene or situation over? Wrap up, look for the next one. Back to step 1.",
             ""),
      lookup("principles",
             "Principles",
             "\uaa5c Follow the rules\n\uaa5c Begin and end with the fiction\n\uaa5c Address the characters, not the players\n\uaa5c Ask questions and build on the answers\n\uaa5c Be a fan of the player characters\n\uaa5c Embrace the fantastic and the mundane\n\uaa5c Exploit the setting guide\n\uaa5c Respect your prep\n\uaa5c Give your characters life\n\uaa5c Think offscreen, too\n\uaa5c Bring it home\n\uaa5c Let things breathe\n\uaa5c Let things burn",
             ""),
      lookup("content",
             "Content",
             "Keep this in sync with the steading playbook. Review it at the start of each session.\nWhen anyone calls 'time out,' play stops. Step out of character, check in with each other, maybe take a break. Discuss what's wrong, player-to-player.\nIf content was included that shouldn't have been, acknowledge the mistake, fix the fiction, and move on.\nIf someone realizes they need content to be excluded, veiled, or handled in a particular way, then update the lists. Clarify specifics, now or later, but don't ask reasons. Fix the fiction. Check in with the player(s). When everyone is ready, move on.",
             ""),
      lookup("damage",
             "Damage & Debilities",
             "Deal damage when your GM move has some- one getting hurt, banged up, knocked around, injured. If it's caused by a danger, deal damage per its stats. Otherwise:\n\n**What would it do to a normal person?**\nBruises & scrapes; pain; light burns d4\nNasty flesh wounds/bruises/burns d6\nBroken bones; deep/wide burns d8n\nDeath or dismemberment d10\n\nInflict a debility when your GM move would leave a PC weakened, dazed, or miserable.\n**Weakened:** fatigued, tired, sluggish, shaky. Disadvantage to STR and DEX.\n**Dazed:** out of it, befuddled, not thinking clearly. Disadvantage to INT and WIS.\n**Miserable:** distressed, grumpy, unwell, in pain. Disadvantage to CON and CHA.",
             ""),
      lookup("recover",
             "Recover",
             "When you take time to catch your breath and tend to what ails you, expend 1 use of supplies and recover HP equal to 4+Prosperity. You can't gain this benefit again until you take more damage.\nWhen you tend to a debility or a prob- lematic wound, say how. The GM will either say that it's taken care of or tell you what's required to do so (Defying Danger, expending supplies or some other resource, finding \_\_\_\_\_, Making Camp, etc.).\n\nWhen they tend to a debility or problematic wound, additional requirements might include:\n\uaa5c Knowing Things about how to treat this\n\uaa5c Defying Danger, the danger being...\n... the pain\n... them thrashing as you work\n... the wound/condition getting worse\n... that \_\_\_\_\_ arrives/happens before you finish ... drawing the attention of \_\_\_\_\_\n... that you need to use up/use more \_\_\_\_\_\n\uaa5c Expending (more) supplies, whisky, etc. Finding \_\_\_\_\_ (an herb, the antivenom, fresh water, something to use as a stent, etc.)\n\uaa5c Making Camp/letting them rest\n\uaa5c Doing something drastic (cauterizing, amputating, field surgery, etc.)\n\nCombine with 'and' and 'or' as you see fit.",
             ""),
      lookup("discoveries",
             "Discoveries",
             "**Random loot**\nRoll the danger's damage, and if it's...\n... a hoarder roll twice, take both/either\n...lording over others +1d4 to roll\n... ancient and noteworthy +1d4 to roll\n\nIf there's no associated danger, roll 1d6.\n\n**Loot**\n1 Roll again with +1d6 to roll\n2 A curiosity/trophy/thing to show the kids 3 Supplies, gear, or provisions (Value 0)*\n4 Specialized, uncommon gear or supplies\n(Value 0 or 1)*-poison, reagents, etc.\n5 Clue, foreshadowing, or useful info*\n6-7 Goods, gear, or supplies (Value 1)*\n8-9 Finery, artifacts, goods, or gear (Value 2)* 10 strange material, an item or raw amount* 11 Minor arcanum (roll lore, origin & theme) 12 Minor arcanum (roll d4+2 for nature)\n13 Minor arcanum (roll d8+4 for nature)\n14 Treasure, finery, artifacts, or goods (Value 3)* 15 A immovable resource, exploitable with effort (a mine, a power source, a vault, etc.) 16 Riches, treasure, artifacts, or finery (Value 4) 17 Major arcanum (pick 1)\n18+ A hoard (Value 5, immobile) + roll again\n\n*Roll 1d6: 1=small; 2=portable (\u25c7); 3=portable but big (\u25c7\u25c7), maybe clumsy; 4=immobile; 5=hard to extract/transport, and roll again; 6=hard to find a buyer, and roll again.\n\n**Strange materials**\n1d10 Material\n1 Orichalcum: a bronze-like metal; flashes red with fire and burns away the impure.\n2 Makerglass: cut into wondrous shapes, unbreakable/unworkable by mortal means\n3 Dark ice: purplish ice, which stays cold and frozen except in the hottest furnace\n4 Aetherium: an alloy of copper and lightning 5 Red crystal: pulsing, warm, thirsting for blood, like cruelty solidified\n6 Moonstone: a pale glassy gem, which reveals shapeshifters and illusions\n7 Black iron: hard, heavy, worked like steel and utterly immune to all magic\n8 Redwood: natural tether to spirits of the wild 9-10 Something else; something new or something very, very old",
             ""),
      lookup("npcs",
             "NPCs",
             "Sometimes you need to come up with a new character suddenly. These tables and guides should allow you to make a useful or compelling one interesting. You can make one by getting a Name, a Trait, a Relationship, some Impressions, an Instict, and then you can include some optional details as well.\n\nThese commands will get you to all that information:\n`!st gm names`\n`!st gm traits`\n`!st gm relations`\n`!st gm impressions`\n`!st gm insticts`\n`!st gm othernpc`",
             ""),
      lookup("names",
             "Names",
             "Pick one, make one up, or ask a player to.\n\n**Stonetop names (Welsh):** Aderyn, Aeronwen, Afanen, Afon, Alun, Andras, Aneirin, Awstin, Bedwyr, Berwyn, Betrys, Braith, Briallen, Bronwen, Bryn, Cadi, Cadoc, Cadwygan, Caron, Cefin, Ceinwen, Ceridwyn, Cerys, Colwyn, Deiniol, Dilwen, Dylis, Eifion, Eirlys, Eluned, Emrys, Enfys, Eurwen, Gaenor, Garet, Gethin, Glyndir, Heledd, Hywel, Ifan, Iorwerth, Iwan, Lewela, Leuca, Linos, Mado, Maldwyn, Malon, Mared, Marged, Martyn, Meirion, Menwen, Mererid, Neirin, Nia, Ofydd, Olwyn, Owain, Padrig, Parry, Pryder, Pryce, Rheinal, Rhisiart, Rhosyn, Rydderch, Sawyl, Siana, Sioned, Talfryn, Tegid, Tiwlip, Tomos, Tudyr, Winifred, Yorath\n\n**Marshedge names (Irish):** Abben, Ailen, Brin, Brogan, Catlin, Coln, Daedre, Dermos, Ennin, Finnen, Gilor, Isbeal, Kiran, Lile, Lim, Mathuin, Mirne, Noren, Owan, Ragan, Renan, Seadha, Seann, Tierney, Ulliam\n\n**Hillfolk names (Breton, missing vowels, clipped):** Adm, Blej, Cirl, Davth, Elst, Gwilm, Gwenl, Henri, Ines, Jenfir, Jown, Juda, Kiln, Laurl, Loic, Merrn, Maikl, Nanzl, Nolwn, Quent, Reegn, Ropr, Sabi, Stren, Yanz\n\n**Southern names (Greek, Hebrew, Persian, Arabic):** Agatte, Aref, Alix, Baraz, Canan, Darya, Demetra, Elene, Elios, Fotios, Faruza, Golza, Iasos, Iona, Kyriakos, Marika, Maayan, Osher, Natasa, Nivola, Rinat, Stamat, Thecla, Zhaleh\n\n**Manmarcher names (Germanic):** Alfher, Bathhilde, Berkhard, Bertrim, Clothar, Dag- mar, Elfrida, Ganter, Gerhild, Hartig, Hilde, Hiltrude, Hramn, Ludig, Luise, Meike, Modd, Sabrinne, Swanhilde, Ulrike, Urrsla, Weillem, Wiland, Wulfrim\n\n**Barrier Pass names (Tibetan, Nepali):** Choden, Dawa, Dorji, Duga, Jamya, Kunza, Lhamo, Norbu, Nyado, Passan, Sonam, Tashi, Tenzi, Tseri, Wanchu, Yonta",
             ""),
      lookup("traits",
             "Traits",
             "all thumbs\nambitious\nbeloved by everyone\nbeatiful singing voice\nbest cook\nbest weaver\nblind\nbraved the Ruin Tower\ncautious\nchronic cough\ncobbler\ncomplains too much\ncowardly\ncraves recognition\ncurious\ndallied with the fae years ago\ndeaf\ndesperately wants a child\ndistills the best whisky\ndoesn't pull their weight\ndrunkard\neagle-eye\nfearless\nfoundling\ngathers herbs from the Wood\ngets the best deals\ngifted storyteller\ngods-fearing\ngood with children\nhappy-go-lucky\nhas a beef with Marshedge\nhas a good heart\nhas a lot of backbone\nhas a wandering eye\nhas a way with animals\nhas fae blood in their veins\nhas just terrible luck\nhas lost their nerve\nhas no respect for their elders\nhas terrible nightmares\nhas the most children\nhas their head in the clouds\nhates the Hillfolk\nhears voices\nhumorless\nimmaculate appearance\njealous\njust got married\nkeeps to themselves\nknows all the gossip\nlame\nlikes to hurt things\nlived among the Forest Folk\nlost all their children \nlovesick\nloves their dogs\nloyal friend\nmost handsome\nmoved here recently\nmust approve any marriages\nmute\nnot afraid of deep water\nnot too bright\noldest\norphan\noverprotective\nprettiest\nprideful\nreckless\nrefuses to marry\nresents their lot in life\nruns everywhere\nsensitive\nsimpleton\nslew many crinwin\nstoic\nstubborn\nsuffers from fits\nswears they met the Pale Hunter\ntells the best jokes\ntender-hearted\ntends the Gods' Pavilion\ntends to the sick & injured\ntouched\nvery strong\nwants to have kids\nwell-read\nwell-traveled\nwidowed\nwill eat anything\n",
             ""),
      lookup("relationships",
             "Relationships",
             "For locals, or people the PCs know well:\n\uaa5c Are you related to them? How?\n\uaa5c What's their family situation? (Married? Kids? Parents? Siblings? Grandparents/kids?) Who else are they close to? Who cares about them?\n\uaa5c What do you like/dislike about them?\n\uaa5c What are they respected for?\n\uaa5c What do others say behind their back?\n\uaa5c What's their most notable feature?\n\uaa5c How have they always treated you?\n\uaa5c What do they seem to like or enjoy?\n\uaa5c What do they grumble about?\n\nFor outsiders that the PCs know:\n\uaa5c When and how did you first meet them? When did you last see them?\n\uaa5c What do you know of their family?\n\uaa5c How would you describe them to someone else?\n\uaa5c What do you expect to find yourselves talking/arguing/reminiscing about?\n\uaa5c Why are you (not) looking forward to seeing them again?\n\uaa5c How have they changed since last you met?\n\nFor folks the PCs have heard of:\n\uaa5c What are they known for?\n\uaa5c What's said to be their most notable feature?\n\uaa5c Who do you know who's actually met them?\n\uaa5c How are they different from what you expected?",
             ""),
      lookup("impressions",
             "Impressions",
             "Give up to 3, from a different areas. Most should reflect their nature; maybe 1 should contrast.\n\n**Face:** angular, broken nose, dimpled, freckles, hawk nose, leathery, missing teeth, paint, scar, scowl, soft, sunburnt, tattoo, warts, etc.\n\n**Eyes:** big, bright, cool, cloudy, dark, deep, droopy, missing, pale, small, squinty, quick, watery, etc.\n\n**Hair:** bald, curly, greasy, straight, thick, thin, etc. Body: big, heavyset, little, lithe, meaty, missing \_\_\_\_\_, round, short, stooped, tall, thick, thin, wiry, etc.\n\n**Presence:** alert, brooding, cheery, elegant, fidgety, friendly, haughty, hunched, intense, serene, etc.\n\n**Scent:** earthy, musky, floral, ripe, sour, smoky, etc. \n\n**Cloths:** boots, charms, [color], dirty, embroidery,ribbons, ring, tidy, torc, threadbare, unkempt, etc.\n\n**Voice:** breathy, clipped, crass, gruff, high, hoarse, lilting, lisping, monotone, mumbly, nasally, quavery, rumbling, shrill, soft, stutter, etc.",
             ""),
      lookup("instincts",
             "Instinct",
             "What do they naturally do?\n\nIf they're a monster or a threat, it should bring them into conflict with others.\n\nIf they're a follower, it should causes trouble for the PC who leads them.\n\nFor anyone else, it should reflect their basic outlook and how they approach the world.\n\nWrite it as 'to \_\_\_\_\_' (e.g. 'to protect her family').",
             ""),
      lookup("othernpc",
             "Optional Details",
             "**Tags & moves**\nAssign tags as you see fit. Tags are adjectives or nouns that describe their nature, their capabili- ties (or lack thereof ), or their notable traits. (e.g. cunning, gullible, cautious, bold, athletic, bumbling, brave, cowardly, etc.).\nWrite up to 3 GM moves for the NPC, reflect- ing a skill or ability, a specific manifestation of a tag, or just something they're likely to do.\n\n**Connections**\nAsk yourself some or all of the following:\n\uaa5c What do they think of the PCs?\n\uaa5c Who are they related to? Friends with?\n\uaa5c Who are they loyal to, and why?\n\uaa5c Who do they dislike, and why?\n\n**Motivations**\nAsk yourself some of the following:\n\uaa5c What do they fear?\n\uaa5c What angers them?\n\uaa5c What do they long for?\n\uaa5c What do they think they deserve? \n\uaa5c What do want from the PCs?\n\uaa5c What would enrage them?\n\uaa5c What do they aspire to do or be?\n\n**Personification**\nConsider using one or more tricks to embody an NPC in play:\n\nPick an actor or character from TV, film, or theater. Try to portray them, but don't tell anyone who it's supposed to be.\nPick someone you know, personally. Try to impersonate them, but don't tell anyone.\nPick a way of speaking/tweaking your voice, a catch phrase, or a physical tic or behavior for this NPC. Use it whenever you portray them.\nFind or create a picture of them. Display it when portraying this NPC.",
             ""),
      lookup("persuade",
             "Persuading NPCs",
             "Things that might convince an NPC:\n\uaa5c A promise/oath/vow\n\uaa5c A chance to do it safely/freely/discretely\n\uaa5c Appeasing or appealing to their ego/ honor/conscience/fears\n\uaa5c A convincing deception\n\uaa5c A better/fair/excessive offer\n\uaa5c Helping them/doing it with them\n\uaa5c Violence (or a credible threat thereof )\n\uaa5c Something they want or need (coin/ food/booze/etc.) Assurance/proof/corroboration Pressure/permission/help from \_\_\_\_\_\n\uaa5c Or anything else that makes sense\n\nMake your choices based on your sense of the NPC, their instinct, their motives, and your prep. The PC might not be able to convince them right now, but a 7+ should always at least reveal a path forward.\nIt's okay to offer alternatives on how the NPC could be convinced. 'He's waiting for a bribe; a few coppers would do it. Or you could rough him up a bit, you're pretty sure that'd work, too.'",
             ""),
      lookup("homefront",
             "Homefront",
             "**People:**\n\uaa5c ~300 people live in Stonetop (~50 families) Most adults work the fields or keep a home; ~a dozen ply the Great Wood\n\uaa5c Few tradesfolk: a smith, cobbler, tanner, publican, midwife (plus apprentices)\n\uaa5c Other crafts (carpentry, weaving, pottery, distilling, etc.) done on the side.\n\n**Home & hearth:**\n\uaa5c Homes are squat, stone (from the Old Wall), thatched roofs; 1-3 buildings per family\n\uaa5c Each family keeps a garden and livestock\n\uaa5c No mill; folks grind grain with quern-stones\n\uaa5c Most families keep a whisky still\n\uaa5c Water comes from cistern; fill with rain/snow\n\uaa5c Folks wash at the Stream, but rarely go alone\n\n**Trade & commerce:**\n\uaa5c Most crops go to the granary for public use\n\uaa5c Mostly barter; coin comes from outisders \n\uaa5c Merchants come at least once a season (except winter)\n\uaa5c Gordin's Delve brings metal & tools\n\uaa5c Marshedge brings textiles, herbs, glass, finer goods from the south.\n\uaa5c By compact with the Forest Folk, no one fells living trees in the Great Wood (but the Forest Folk haven't been seen in a decade).\n\n**Protection & governance**\n\uaa5c Every able body drills with the militia, keeps a spear handy, takes a turn at the watchtowers.\n\uaa5c No nobles, no elected officials; decisions made by the wise, the cunning, the brave.\n\n**Questions to ask**\n\uaa5c What task or chore are you working on?\n\uaa5c What's the best/worst thing about this chore?\n\uaa5c What's cooking on the hearthfire?\n\uaa5c What here makes the place feel like home?\n\uaa5c What about your home would you change if you could?\n\uaa5c How does Stonetop mark or celebrate the coming of spring/summer/autumn/winter?\n\uaa5c What's your (least) favorite thing about this season?\n\uaa5c What's your favorite tale of Stonetop's history?\n\uaa5c What's the scariest story that the elders tell?\n\uaa5c How do the villagers mark or celebrate a birth?\n\uaa5c How do the villagers mark one's coming of age?\n\uaa5c What do the villagers do with their dead?\n\n\nSee the jobs that people do around Stonetop by using `!st dm homefront jobs`",
             ""),
      lookup("homefrontjobs",
             "Homefront Jobs",
             "**Spring**\n\uaa5c Harvesting winter potatoes\n\uaa5c Spreading seed, planting beans/potatoes\n\uaa5c Harrowing soil (to cover seeds, plantings)\n\uaa5c Chasing birds from the fields (childs' work)\n\uaa5c Spreading manure & plowing fallow fields\n\uaa5c Kidding goats, sheep\n\uaa5c Picking spring vegetables\n\uaa5c Clearing and planting gardens\n\uaa5cHarvesting/cutting deadfall for firewood\n\uaa5c Fur trapping, light hunting (for meat)\n\n**Summer**\n\uaa5c Haymaking (from Flats-grass, fallow fields)\n\uaa5c Weeding crops/gardens\n\uaa5c Spreading manure & replowing fallow fields\n\uaa5c Weaning goat kids & lambs\n\uaa5c Milking goats, shearing sheep\n\uaa5c Picking summer vegetables\n\uaa5c Berry-picking from gardens and the Wood\n\uaa5c Light hunting/trapping (for meat, not fur)\n\n**Autumn**\n\uaa5c Harvesting beans, barley, oats, potatoes\n\uaa5c Gleaning fallen seed from fields (childs' work)\n\uaa5c Threshing, winnowing, sieving, storing crops\n\uaa5c Plowing fallows & planting winter potatoes\n\uaa5c Picking & preserving autumn vegetables\n\uaa5c Breeding goats, sheep\n\uaa5c Foraging for nuts, fruits in the Wood\n\uaa5c Heavy hunting/trapping (fur & meat)\n\uaa5c (If able): harvesting timber from Foothills\n\n**Winter**\n\uaa5c Collecting snow for the cistern\n\uaa5c Spinning, weaving, hand-crafts\n\uaa5c Distilling & casking whisky\n\uaa5c Tending to livestock, stockpiling manure\n\uaa5c Heavy trapping (for fur)\n\uaa5c Hunting as able (for meat)\n\uaa5c Slaughting/butchering livestock as needed\n\n**Always**\n\uaa5c Cooking, grinding grain, baking\n\uaa5c Rendering fat, making oil & rushlights\n\uaa5c Cleaning pens, coops, homes, clothes\n\uaa5c Collecting & hauling water, to & from cistern\n\uaa5c Smithing, tanning, cobbling, midwifery\n\uaa5c Maintenance (buildings, clothes, tools, etc.)\n\uaa5c Manning the watchtowers at night; drilling",
             ""),
      lookup("makeaplan",
             "Make a Plan",
             "Clarify exactly what they hope to achieve and how they plan to go about it. Then tell them 1-4 requirements, connected with 'and' and 'or' as you see fit. Example requirements:\n\n\uaa5c You must learn/figure out \_\_\_\_\_\n\uaa5c You must find/locate/obtain \_\_\_\_\_\n\uaa5c You must decipher/fix/solve \_\_\_\_\_\n\uaa5c You must create/design/establish \_\_\_\_\_ You'll need to talk to \_\_\_\_\_ (and get their help/support/approval)\n\uaa5c You must wait until/for \_\_\_\_\_\n\uaa5c You must travel to \_\_\_\_\_\n\uaa5c It'll take days/weeks/months/years\n\uaa5c The best you can get/do is \_\_\_\_\_\n\uaa5c It will cost \_\_\_\_\_\n\uaa5c You'll risk \_\_\_\_\_\n\uaa5c The steading must Pull Together \_\_\_\_\_ times, each requiring \_\_\_\_\_\n\nIf they ask you how to achieve one of the requirements, break it down into a further 1-4 requirements from the list above.",
             ""),
      lookup("relativevalue",
             "Relative Value",
             "Exchange rates are not standard, but...\n\n**A Value 0 item is generally worth:**\n\uaa5c Up to a few purses of copper coins\n\uaa5c A favor\n\uaa5c A day to a week of unskilled labor\n\uaa5c A common, mundane item\n\n**A Value 1 item is generally worth:**\n\uaa5c 1-4 handfuls of silver coins\n\uaa5c A season (or so) of unskilled labor\n\uaa5c A day or week of skilled labor\n\uaa5c A unit of trade goods (a sack of grain, a pouch of salt, a stack of pelts, etc.)\n\uaa5c A bit of finery ( a richly embroidered cloak, a silk scarf, a silver comb, etc.)\n\n**A Value 2 item is generally worth:**\n\uaa5c 1-4 purses of silver coins\n\uaa5c 1-2 Surplus for a village (Size +0)\n\uaa5c A year (or so) of unskilled labor\n\uaa5c A season (or so) of skilled labor\n\uaa5c A cartload of common trade goods\n\uaa5c An item of luxury or status (gold ring, artful silver torc, gemstone, etc.)\n\n**A Value 3 item is generally worth:**\n\uaa5c 1-4 handfuls of gold coins\n\uaa5c 1-2 Surplus for a town (Size +1)\n\uaa5c A year (or so) of skilled labor\n\uaa5c A unit of exotic trade goods ( a bolt of silk, a pouch of spices, etc.)\n\uaa5c A precious item (ruby ring, gold torc, etc.)\n\n**A Value 4 item is generally worth:**\n\uaa5c 1-4 purses of gold coins, or... or... 1-2 Surplus for a city (Size +2),\n\uaa5c A cartload of exotic trade goods\n\uaa5c A 'priceless' item (huge flawless gemstone, gold statuette, bejeweled scepter, etc.)\n\nA \u25c7 purse of coins contains ~5 handfuls of coins. A handful is ~10-15 individual coins, and so a purse has ~50-75 coins in it.\nOne silver coin is worth a purse of coppers (about 50-75 copper coins). And one gold coin is worth a purse silvers (about 50-75 silver coins, or an absolute pile of coppers).\nRemember, trade is based more on barter, debts, and honor than standard currency.",
             ""),
      lookup("traveltimes",
             "Travel Times",
             "**From Stonetop via the Roads to...**\nthe Crossroads (3-4 hours)\nthe Foothills (2 days)\nTitan Bones (2 days)\nGordin's Delve (4 days)\nBarrier Pass (4 days)\nthe Steplands (4 days)\n Marshedge (8 days)\n\n**From Stonetop to...**\nthe Maw (2-3 hours)\nthe cave bears' den (2-3 hours)\n the Red Grove (3-4 hours)\nthe Golden Oak (14 days)\n\n**From the Crossroads to...**\nthe Ruined Tower (4-5 hours)\n\n**From the north edge of the Steplands to...**\nBlackwater Lake (2 days)\nThree-Coven Lake (2 days)\n\n**From Marshedge to...**the ruins on the Dread River (2 days)\nthe northern Manmarch (4 days)\nThree-Coven Lake (4 days)\nLygos (30 days)\n\n**To Tor's Fist from...**\nthe Foothills Barrier Pass (5 days)\nWhen they make camp (6 days)",
             ""),
      lookup("hazards",
             "Hazards",
             "**As a detailed description**\nJust describe what it is, what it looks like, what it does, how it works.\n\n**As GM moves**\nWrite one or more GM move that reflect each of the following, as makes sense for the hazard:\n\uaa5c How its presence is foreshadowed or revealed\n\uaa5c How it harms or hinders\n\uaa5c How it escalates or gets worse\n\uaa5c How it thwarts attempts to overcome it\n\nIf dynamic, changing: give it an instinct, written as 'to \_\_\_\_\__' (e.g. 'to bury everything').\n\n**As an impending doom**\nWrite down the ultimate bad thing that can hap- pen (e.g. tunnel collapses, they roll Death's Door).\nWrite 1-4 events describing how it starts and esca- lates; assign each event one or more check boxes.\nOptional: write a trigger that causes it to advance, fictional ('Each time the pillars are damaged') or mechanical ('Each time someone rolls doubles').\n\n**As player moves**\nWrite a fictional trigger ('When you <trigger the hazard>, ...') and resolution, using any combo of the following that makes sense:\n\uaa5c \_\_\_\_\__ happens (and \_\_\_\_\__ is bad) Pick X from a list\n\uaa5c Tell us \_\_\_\_\__\n\uaa5c Lose \_\_\_\_\__\n\uaa5c Take damage/suffer a debility/Death's Door\n\uaa5c Roll +STAT (or something); on a 10+, \_\_\_\_\__; on a 7-9, \_\_\_\_\__; (optionally) on a 6-, \_\_\_\_\__\n\n**If it deals damage**What would it do to a typical person? (pick 1) Bruises & scrapes; pain; light burns d4\nNasty flesh wounds, bruises, burns d6\nBroken bones, bad burns, terrible pain d8\nDeath or dismemberment d10\n\nIf... (choose all that apply)\n... armor can't protect them (ignores armor)\n... it cuts through leather/hide (1 piercing, messy)\n... it tears metal apart (3 piercing, messy)\n... it knocks them around (forceful)\n... it's big/vicious/scary (+2 damage)\n... they've taken precautions (+disadvantage)\n... they're caught off-guard (+advantage)",
             ""),
      lookup("expeditions",
             "Expeditions",
             "**Requirements**\n\uaa5c You must first travel to \_\_\_\_\_, and from there to your destination\n\uaa5c You must wait until \_\_\_\_\_\n\uaa5c You need a knowledgeable guide/ accurate map/detailed directions\n\uaa5c It'll take at least \_\_\_\_\_ days (and a corresponding amount of supplies)\n\uaa5c You'll need to bring \_\_\_\_\_\n\n**Challenges**\n\uaa5c You need to watch out for \_\_\_\_\_\n\uaa5c The way is perilous, plagued with danger\n\uaa5c You risk getting lost\n\uaa5c You must surmount/cross/brave \_\_\_\_\_\n\uaa5c The terrain itself is treacherous; you risk injury on the way\n\uaa5c The way will be grueling; you risk exhausting yourselves/your resources\n\uaa5c You risk drawing the attention of \_\_\_\_\_\n\nPresent each challenge once, at a fitting time/ place. Once overcome, don't make them deal with it again except as a hard GM move. ('The way is perilous' is an exception, see `!st gm alongtheway`)",
             ""),
      lookup("alongtheway",
             "Along the Way",
             "\n\n**When the way is perilous**\nOn each leg of travel, point to a looming danger or introduce a danger. Maybe roll a Die of Fate.\n\n1 A danger springs on them, unavoidable\n2-3 Introduce a danger, right in front of them\n4-5 Point to a looming danger\n6 Point to a looming danger, but also present a discovery\n\n**When they make camp**\n\uaa5c How will you avoid attention/spot danger?\n\uaa5c How do you plan to keep warm?\n\uaa5c Do you start a fire? What do you use for fuel?\n\nIf you know something will happen, it happens. If you think something might happen, but aren't sure, then ask someone to roll the Die of Fate.\n\n1 Something dangerous approaches, inclined to do harm\n 2 Something dangerous approaches, curious but not aggressive\n3 Something annoying happens (critters in the food, rain, an argument, etc.)\n4-5 The night passes uneventfully\n6 They observe something interesting, find something useful, or otherwise gain some small boon; or the night passes uneventfully\n\n**Legs of travel**\nIf familiar, short, uneventful: gloss over it.\nIf unfamiliar: describe it, give impressions.\n\nTo create a sense ot time passing: ask questions and/or have them Keep Company.\n\uaa5c What's the most striking thing that you notice?\n\uaa5c What's the best/worst/most unexpected part of this journey?\n\uaa5c What have you heard about this place?\n\uaa5c When were you here last?\n\uaa5c How has it changed?\n\uaa5c How are you dealing with the weather?\n\uaa5c What are you looking forward to?\n\uaa5c What's the most striking thing that you notice?\n\nPortray NPCs, add details, answer questions.\n\uaa5c Make a soft GM move:\n\uaa5c Present a challenge from Chart a Course Present some other encounter\n\uaa5c Have an NPC/follower get into/cause trouble Stir up conflict between PCs\n\uaa5c Offer an opportunity to do something as they travel, or arrive at next point of interest\n\n'What do you do?' Resolve. Repeat or move on.\n\n**Points of interest**\n\uaa5c Landmarks not yet seen in play\n\uaa5c Where you plan to frame scenes, make moves\n\uaa5c Their destination\n\nIf you want to build tension: frame the scene with the location in sight but at a distance. Other- wise, frame the scene with them already there.\nIf unfamiliar: describe, give impressions. If the PCs know or picked this place, ask them instead?\n\nOn the first visit to a landmark, ask questions.\n\uaa5c What's the most striking thing that you notice?\n\uaa5c What's here tells you that this is a place where/of/that __?\n\uaa5c What have you heard about this place?\n\uaa5c When were you here last? How has it changed? How does this place make you feel?\n\uaa5c What are you thinking/worrying about?\n\n Portray NPCs, add details, answer questions. Maybe draw/provide a map.\nIf this is just a landmark, with no challenges or encounters: offer an opportunity to do something here or else move on to the next leg of travel.\nOtherwise, make a soft GM move. 'What do you do?' Resolve actions. Repeat or move on.",
             ""),
      lookup("weather",
             "Random Weather",
             "You decide the weather, but if you want, ask a player to roll the Die of Fate.\n\nLate winter/early spring\n1 Snow/sleet/hail; an early thuderstorm; or cold, soaking rain\n2-3 Cold and windy, maybe some showers\n4 Clouds on the horizon & steady wind, roll again later with disadvantage\n5-6 A fine, sunny spring day; clouds/wind gusts\n\nSpring/early summer\n1 Heavy storm (wind, hail, thunder, lightning)\n2 Steady, chilly rain\n3-4 Warm & windy, maybe some brief showers\n5-6 Warm, sunny, pleasant\n\nSummer\n1 Heavy storm (wind, hail, thunder, lightning, tornadoes)\n2 Blazing heat, still air, not a cloud in sight\n3 Hot & humid, with brief, drenching thunder storms\n4-5 Hot & dry by day; cooler/windy at night\n6 Warm, sunny, breezy, perfect\n\nLate summer/early autumn\n1 Powerful thunderstorm or cold, soaking rain\n2 Windy with a few rain showers\n3 Warm, clouds on horizon, steady wind; roll again later with disadvantage\n4-5 Hot & dry by day; cooler/windy at night\n6 Warm, sunny, breezy, perfect\nAutumn\n1 Cold, drenching rain and/or sleet\n2 Cold, windy, an early snowfall\n3 Clouds on the horizon & steady wind, roll again later with disadvantage\n4 A fine, sunny spring day; clouds/wind gusts\n5-6 Crisp, breezy\n\nWinter\n1 Blizzard: wind, snow, all of it\n2 Intense cold and wind\n3 Very cold, very clear, very still\n4 Cold and snowy, or cold and windy\n5 Some snow, but mostly just dreary\n6 Warm (for winter) and sunny",
             "")
]