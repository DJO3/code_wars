"""
The citizens of Chima need your help. Their weapons got mixed up!
They need you to write a program that accepts the name of a character in
Chima then tells which weapon he/she owns. For example: your program
should return a solution in the format: "Gorzan-Cudjak".
You must complete the following characters: Laval(Shado Valious),
Cragger(Vengdualize), Lagravis(Blazeprowlor), Crominus(Grandorius),
Tormak(Tygafyre), and LiElla(Roarburn). Return "Not a character"
for invalid inputs.
"""

def identify_weapon(character):
    inventory = {
            "Laval":"Shado Valious",
            "Cragger":"Vengdualize",
            "Lagravis":"Blazeprowlor",
            "Crominus":"Grandorius",
            "Tormak":"Tygafyre",
            "LiElla":"Roarburn"}
            
    if character in inventory.keys():
        return "{0}-{1}".format(character, inventory[character])
    return "Not a character"
