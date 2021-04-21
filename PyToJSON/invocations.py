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

invocations = [lookup("bathofhealinglight",
                      "\u20de Bath of Healing Light",
                      "Cup your hands around your light and focus it. Your patient... (pick 2):\n\uaa5c Regains 5 HP (can pick this twice)\n\uaa5c Clears a debility (can pick this twice)\n\uaa5c Has one of their problematic wounds stabilized \n\uaa5c Recovers from a minor condition (drunk, etc.)\n\nReduced: pick only 1 (instead of 2). \n\nEmpowered: add these to your possible choices:\n\uaa5c Regains 10 HP (can pick this twice)\n\uaa5c Fully recovers from a problematic wound\n\uaa5c Is cured of a dire affliction, poison, or disease",
                      ""),
               lookup("blindinglight",
                      "\u20de Blinding Light",
                      "(ongoing)\nYour light blazes. Any in range who look at it are temporarily blinded. Those not looking at it directly must avert their eyes. You are unaffected.\n\nReduced: the light flares only for a moment. \n\nEmpowered: if you wish, your allies are unaffected.",
                      ""),
               lookup("cleansinglight",
                      "\u20de Cleansing Light",
                      "Your light flares, dispelling magic within range. Po- tent, lasting magics are merely suppressed, and slowly return to power once removed from your light.\n\nReduced: potent, lasting magics are unaffected; other magic is merely suppressed.\n\nEmpowered: the invocation is ongoing; while it lasts, any magic brought into range is dispelled/ suppressed.",
                      ""),
               lookup("coldlightofday",
                      "\u20de Cold Light of Day",
                      "(ongoing)\nAll in your light appears as it really is, without the benefit of illusion, shapeshifting, or disguise.\n\nReduced: it lasts only a few moments, just long enough to glimpse the truth.\n\nEmpowered: illusions in the light are dispelled and shapeshifters in the light are momentarily stunned.",
                      ""),
               lookup("dancinglight",
                      "\u20de Dancing Light",
                      "(ongoing)\nYour light takes to the air, floating as you direct it, untethered from its fuel. You can move it anywhere that you can see it, and even change its shape or color.\n\nReduced: it dims, reducing its range by one step.\n\nEmpowered: you can use another Invocation through the Dancing Light while it is ongoing.",
                      ""),
               lookup("gobacktotheshadow",
                      "\u20de Go Back to the Shadow",
                      "Spirits of darkness in your light take 2d8 damage (ignores armor). Roll damage for each spirit separately. A spirit reduced to 0 HP is either banished from this world or back to whatever tethers it here.\n\nReduced: affected spirits take only 1d8 damage.\n\nEmpowered: a spirit reduced to 0 HP is either utterly destroyed OR it's banished from the world and anything tethering it here is destroyed (GM's choice).",
                      ""),
               lookup("holdbackthedarkness",
                      "\u20de Hold Back the Darkness",
                      "(ongoing)\nSpirits and creatures of darkness are repelled by your light and cannot approach. The cowardly or mindless flee outright. Those forced into range of your light deal damage with disadvantage.\n\nReduced: you must maintain an unbroken litany of prayers in order to maintain the effect.\n\nEmpowered: affected entities that are forced into range of your light are vulnerable to mundane weapons, their supernatural defenses suppressed.",
                      ""),
               lookup("mothtoaflame",
                      "\u20de Moth to a Flame",
                      "(ongoing)\nName an individual or type of mortal creature. They gaze raptly at your light and will follow it, slowly. The effect ends if they take damage.\n\nReduced: it lasts only briefly OR only some of the named creatures are affected (GM's choice).\n\nEmpowered: the effect continues for a few mo- ments after they first take damage. Taking damage a second time ends the effect immediately.",
                      ""),
               lookup("terribleasthedawn",
                      "\u20de Terrible as the Dawn",
                      "(ongoing)\nName an individual or type of mortal creature. Your light fills them with dread, causing them to recoil and back away. The cowardly flee outright.\n\nReduced: all mortal creatures but you are affected, including your allies.\n\nEmpowered: even the brave must cower or flee.",
                      ""),
               lookup("warmthofthesun",
                      "\u20de Warmth of the Sun",
                      "(ongoing)\nWhile in your light, you and your allies are free of fear and doubt, and unharmed by extreme cold.\n\nReduced: only one person in the light is protected.\n\nEmpowered: the light also protects from necro- mantic and life-draining effects.",
                      "")
]