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

tags = [lookup("area",
               "Area",
               "Affects everything in an area.",
               ""),
        lookup("narmor",
               "N Armor",
               "When you take damage, subtract the indicated amount; doesn't stack.",
               ""),
        lookup("+narmor",
               "+ N Armor",
               "Increases your armor value by the indicated amount; stacks.",
               ""),
        lookup("awkward",
               "Awkward",
               "Unwieldy, requires space, gets stuck",
               ""),
        lookup("clumsy",
               "Clumsy",
               "Take disadvantage on all rolls while wearing/carrying/using it.",
               ""),
        lookup("crude",
               "Crude",
               "Prone to break, wear out, stop working, etc.",
               ""),
        lookup("+ndamage",
               "+ N Damage",
               "Increase the damage you deal with that weapon.",
               ""),
        lookup("dangerous",
               "Dangerous",
               "Causes trouble and collateral damage if you aren't careful (and maybe if you are).",
               ""),
        lookup("forceful",
               "Forceful",
               "Can knock someone around, maybe even off their feet.",
               ""),
        lookup("immobile",
               "Immobile",
               "You can't really carry it on your person",
               ""),
        lookup("Messy",
               "messy",
               "Does particularly destructive damage, ripping people and things apart.",
               ""),
        lookup("xpiercing",
               "X Piercing",
               "when you deal damage, subtract x from the target's armor for that attack where x = the steading's current Prosperity.",
               ""),
        lookup("precise",
               "Precise",
               "when you Clash with a precise weapon, you can roll +DEX instead of +STR",
               ""),
        lookup("reload",
               "Reload",
               "After it's used, it takes time/effort to reset",
               ""),
        lookup("requires",
               "Requires",
               "If you don't meet the requirements, it works poorly or not at all.",
               ""),
        lookup("slow",
               "Slow",
               "Takes minutes or more to use; unlikely to be useful in the middle of a fight.",
               ""),
        lookup("thrown",
               "Thrown",
               "You can Let Fly with it (at near range), but on a 7-9 you can't choose to deplete ammo. Once you throw it, it's gone until retrieved.",
               ""),
        lookup("warm",
               "Warm",
               "Will keep you warm in cold weather, but it's uncomfortable and exhausting (and possibly dangerous) in hot weather.",
               ""),
        lookup("hand",
               "Hand",
               "Tight quarters; up close and personal.",
               ""),
        lookup("close",
               "Close",
               "Melee range, 1-2 steps away.",
               ""),
        lookup("reach",
               "Reach",
               "3-4 steps away.",
               ""),
        lookup("near",
               "Near",
               "Up to 30 or so steps away",
               ""),
        lookup("far",
               "Far",
               "Quite the distance; 100 steps, maybe more.",
               ""),
        lookup("horde",
               "Horde",
               "Fights in large groups (6 or more)",
               ""),
        lookup("group",
               "Group",
               "Fights in small groups (2-5 per group)",
               ""),
        lookup("solitary",
               "Solitary",
               "Fights by itself",
               ""),
        lookup("tiny",
               "Tiny",
               "It is cat-sized or smaller",
               ""),
        lookup("small",
               "Small",
               "It is the size of a human child",
               ""),
        lookup("large",
               "Large",
               "It is the size of a horse, cart, etc.",
               ""),
        lookup("huge",
               "Huge",
               "It is the size of an elephant or bigger",
               ""),
        lookup("spirit",
               "Spirit",
               "It lacks physical form",
               ""),
        lookup("fae",
               "Fae",
               "It is between physical and spiritual",
               ""),
        lookup("construct",
               "Construct",
               "It is made by someone",
               ""),
        lookup("planar",
               "Planar",
               "It is alien to this world",
               ""),
        lookup("undead",
               "Undead",
               "It is dead but in denial",
               ""),
        lookup("hoarder",
               "Hoarder",
               "It is notable for amassing trinkets and treasure",
               ""),
        lookup("cautious",
               "Cautious",
               "It is notable for avoiding fights, fleeing early",
               ""),
        lookup("cunning",
               "Cunning",
               "It is notable for its intelligence",
               ""),
        lookup("terrifying",
               "Terrifying",
               "It is notable for its disturbing, terrible presence",
               ""),
        lookup("stealthy",
               "Stealthy",
               "It is notable for sneaking, surprising, ambushing",
               ""),
        lookup("magical",
               "Magical",
               "It is notable for using spells or magic",
               ""),
        lookup("organized",
               "Organized",
               "It is notable for working well in groups",
               "")
]