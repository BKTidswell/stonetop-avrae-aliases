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

players = [lookup("agenda",
             "Your Agenda",
             "As a player, your chief goals should be to...\n\uaa5c Portray a compelling character\n\uaa5c Engage with the fictional world\n\uaa5c Play to find out what happens",
             ""),
      lookup("principles",
             "Your Principles",
             "The game works best if you...\n\uaa5c **Begin and end with the fiction.** Tell us how you do what you do, what it looks like.\n\uaa5c **Connect with the other PCs.** Explore your relationships. Play out scenes together. \n\uaa5c **Show us what’s important to you.** Who and what will your character fight for? \n\uaa5c **Have goals and pursue them.** Don’t just react to threats that the GM presents.\n\uaa5c **Be bold, take risks.** If you don’t act like a hero, who will?\n\uaa5c **Embrace difficulty, setback, and failure.** Show us how your character deals with it. \n\uaa5c **Participate in worldbuilding.** Answer the GM’s questions with color and life.\n\uaa5c **Build on what others have said.** Let yourself be inspired by your fellow players. \n\uaa5c **Give others a chance to shine.** Don’t hog the spotlight. Set others up for greatness! \n\uaa5c **Participate in the conversation.** Pay attention, ask questions, offer suggestions.",
             ""),
      lookup("content",
             "content",
             "By default, this game features:\n\uaa5c Fairly graphic violence\n\uaa5c Kidnapping, abductions, families in danger\n\uaa5c Bigotry, racial tensions\n\uaa5c Horror elements, mind control, possession\n\uaa5c Personal corruption (esp. for the Seeker)\n\uaa5c Starvation (or the threat thereof )\n\nOther disturbing and emotional topics are certainly possible. Talk to your group about any topics that you wish to exclude, veil, or handle in a specific way.",
             "")
]