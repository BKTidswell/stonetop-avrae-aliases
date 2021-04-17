
#Sets the stat of choice
!servalias setstat embed
<drac2>
args = &ARGS&

out_str = ""
stats = ['str', 'dex', 'int', 'wis', 'con', 'cha']

usage_message = "To use `!setstat` do so in the form `!setstat [stat] [score]` where stat is one of `STR`, `DEX`, `INT`, `WIS`, `CON`, or `CHA`, and score is the score you are setting it to."

#check to make sure there are at least two args
if len(args) < 2:
    out_str = usage_message
else:
    args[0] = args[0].lower()
    #check that the first arg is a stat
    if args[0][0:3] not in stats:
        out_str = usage_message
    else:
        if not args[1].lstrip('+-').isdigit():
            out_str = usage_message
        else:
            out_str = "Stat " + args[0].upper() + " was set to " + args[1]
            set_uvar("st"+args[0][0:3],args[1])

</drac2>
-title "Set Stonetop Stats"
-desc "{{ out_str }}"
-color <#4d97c4>
-thumb <https://cdn.discordapp.com/attachments/829185108157530152/829936258565668954/stonetop.png>


#Sets the stat of choice
!servalias showstats embed
<drac2>
args = &ARGS&

out_str = ""
stats = ['str', 'dex', 'int', 'wis', 'con', 'cha']

for stat in stats:
    if uvar_exists("st"+stat):
        out_str += stat.upper() + ": " + get("st"+stat) + "\n"
    else:
        out_str += stat.upper() + ": 0\n"
        set_uvar("st"+stat,0)

</drac2>
-title "Stonetop Stats"
-desc "{{ out_str }}"
-color <#4d97c4>
-thumb <https://cdn.discordapp.com/attachments/829185108157530152/829936258565668954/stonetop.png>


#Rolls, allowing you to add stats, adv/dis, and bonus or negatives
!servalias sroll embed
<drac2>
args = &ARGS&

args = [a.lower() for a in args]
stats = ['str', 'dex', 'int', 'wis', 'con', 'cha']

usage_message = "To use `!sroll` to roll 2d6 with modifiers in the form `!sroll [stat] [adv/dis] [mod]` where stat is one of `STR`, `DEX`, `INT`, `WIS`, `CON`, or `CHA`, adv/dis gives you advantage or disadvantage, and the mod is a modifier to the roll. \nThose are all optional parameters, and can be used in any order, but do not use more than one of each."

adv = "adv" in args
dis = "dis" in args

stat_list = [a in stats for a in args]

if True in stat_list:
    stat_name = args[stat_list.index(True)]
    stat = get("st"+stat_name)
else:
    stat_name = ""
    stat = "0"

mod_list = [a.lstrip('+-').isdigit() for a in args]

if True in mod_list:
    mod = args[mod_list.index(True)]
else:
    mod = "0"

if adv:
    roll_str = "3d6kh2+"+stat+"+"+mod
elif dis:
    roll_str = "3d6kl2+"+stat+"+"+mod
else:
    roll_str = "2d6+"+stat+"+"+mod

if stat_name != "":
    out_str = "Rolling with " + stat_name.upper() + "\n\n"
else:
    out_str = ""

out_str += vroll(roll_str.replace("+0",""))
</drac2>
-title "Stonetop Roll"
-desc "{{ out_str }}"
-color <#4d97c4>
-thumb <https://cdn.discordapp.com/attachments/829185108157530152/829936258565668954/stonetop.png>



