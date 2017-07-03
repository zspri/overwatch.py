# Overwatch.py Examples

## Ability Search
```python
import overwatchpy
client = overwatchpy.OWAPI()

hero = input("Enter hero name: ")

if hero == "Ana":
    hero = overwatchpy.Heroes.ana
elif hero == "McCree":
    hero = overwatchpy.Heroes.mccree
# ...

result = client.get_hero(hero)

desc = "{}'s abilities are ".format(result.name)
for a in result.abilities:
    if a == result.abilities[len(result.abilities) - 1]:
        desc += ("and " + a.name + ".")
    else:
        desc += (a.name + ", ")

print(desc)
