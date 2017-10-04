# Overwatch.py

A Python wrapper for https://overwatch-api.net

> This project is deprecated and should no longer be used, as the [Overwatch API](https://github.com/jamesmcfadden/overwatch-api) is no longer being maintained.

> NOTE: Overwatch.py is in early-Alpha and all features may not work as intended.

## How to Install
Use pip:

```
pip install git+https://github.com/Nanomotion/overwatch.py.git
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
