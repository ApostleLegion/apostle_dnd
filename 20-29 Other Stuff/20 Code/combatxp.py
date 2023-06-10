from math import floor

def combatxp(xp: int, downtime: bool=False, help=False)->str:
    if not help:
        if xp > 99:
            new_xp = floor(xp*0.01)
            if downtime:
                new_xp = floor(new_xp/2)
        else:
            new_xp = "1 (Minimum Combat Experience)"
        print(f'Total Combat Experience\n=================\n{xp} \* 0.01 = {new_xp}')
    else:
        print('This would be the help menu!')
    
combatxp(1100, downtime=True)