# Overwatch.py

A Python wrapper for https://overwatch-api.net

> NOTE: Overwatch.py is in early-Alpha and all features may not work as intended.

## How to Install
Use pip:

```
pip install -U overwatchpy
```

Source code:

[Download master.zip](https://github.com/Nanomotion/overwatch.py/archive/master.zip)

## Example

```python
import overwatchpy
client = overwatchpy.OWAPI() # Initialize the OWAPI client

ability = client.get_ability(1) # Get ability 1
print("{} is one of {}'s abilities.'".format(ability.description, ability.hero.name))
```

This will return: `Biotic Rifle is one of Ana's abilities.`

## Requirements
 - Python 3 (3.5 or higher is recommended)
 - requests
 - urllib3

Read the [Documentation](http://nanomotion.xyz/overwatch.py)

Join the [Discord](https://discord.gg/Tz6ztvX)
