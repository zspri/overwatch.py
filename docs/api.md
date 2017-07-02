# API Reference

# Setting up logging

   A basic tutorial for setting up logging.

```python
import logging
logging.basicConfig(level=logging.INFO) # We want to show info, warnings, and errors.

log.info("Hello, world!") # This prints "INFO:root: Hello, world!" to the console.
```

# overwatchpy.OWAPI

   The main class for Overwatch.py. (In `overwatchpy.core`)

   > NOTE: https://overwatch-api.net ratelimits its users to 500 requests per hour. It is recommended that you store data from the API as a backup.

## Instances

   You can make an instance of OWAPI like this:

```python
from overwatchpy.core import OWAPI
client = OWAPI()
```

Usage: `OWAPI(headers={}, user_agent=None, api_version="v1")`

## Methods

   All raw responses from https://overwatch-api.net come in JSON.

| Method                     | Description                       | Returns                   |
| -------------------------- | --------------------------------- | ------------------------- |
| `get_ability(id)`          | Gets an `Ability` by id.          | `overwatchpy.Ability`     |
| `get_all_abilities(id)`    | Gets all `Ability` in a list.     | `list`                    |
| `get_achievement(id)`      | Gets an `Achievement` by id.      | `overwatchpy.Achievement` |
| `get_all_achievements(id)` | Gets all `Achievement` in a list. | `list`                    |
| `get_brawl(id)`            | Gets a `Brawl` by id.             | `overwatchpy.Brawl`       |
| `get_all_brawls(id)`       | Gets all `Brawl` in a list.       | `list`                    |
| `get_brawltype(id)`        | Gets a `BrawlType` by id.         | `overwatchpy.BrawlType`   |
| `get_all_brawltypes(id)`   | Gets all `BrawlType` in a list.   | `list`                    |
| `get_event(id)`            | Gets an `Event` by id.            | `overwatchpy.Event`       |
| `get_all_events(id)`       | Gets all `Event` in a list.       | `list`                    |
| `get_gamemode(id)`         | Gets a `GameMode` by id.          | `overwatchpy.GameMode`    |
| `get_all_gamemodes(id)`    | Gets all `GameMode` in a list.    | `list`                    |
| `get_hero(id)`             | Gets a `Hero` by id.              | `overwatchpy.Hero`        |
| `get_all_heroes(id)`       | Gets all `Hero` in a list.        | `list`                    |
| `get_map(id)`              | Gets a `Map` by id.               | `overwatchpy.Map`         |
| `get_all_maps(id)`         | Gets all `Map` in a list.         | `list`                    |
| `get_platform(id)`         | Gets a `Platform` by id.          | `overwatchpy.Platform`    |
| `get_all_platforms(id)`    | Gets all `Platform` in a list.    | `list`                    |
| `get_reward(id)`           | Gets a `Reward` by id.            | `overwatchpy.Reward`      |
| `get_all_rewards(id)`      | Gets all `Reward` in a list.      | `list`                    |
| `get_rewardtype(id)`       | Gets a `RewardType` by id.        | `overwatchpy.RewardType`  |
| `get_all_rewardtypes(id)`  | Gets all `RewardType` in a list.  | `list`                    |

# Data Classes

   The Data Classes for Overwatch.py

## overwatchpy.Ability

   A hero ability.

### Parameters

 - `id` - The object's id.
 - `name` - The object's name.
 - `description` - The object's description.
 - `is_ult` - Whether or not the ability is its hero's ultimate.
 - `hero` - A truncated `Hero` object. (Returns just the ID and Name, see [overwatchpy.Hero](#overwatchpy.hero))

### Example

```python
from overwatchpy.core import OWAPI
from overwatchpy.objects import *

client = OWAPI()

ability = client.get_ability(1) # Gets ability number 1
print("{} is one of {}'s abilities.".format(ability.description, ability.hero.name))
```

This will print *`Biotic Rifle is one of Ana's abilities.`*

## overwatchpy.Achievement

   A player achievement.

### Parameters

- `id` - The object's id.
- `name` - The object's name.
- `description` - The object's description.
- `reward` - A truncated `Reward` object.
- `hero` - A truncated `Hero` object. Could be none.

## overwatchpy.Brawl

   A brawl.

### Parameters

 - `id` - The object's id.
 - `start_date` - The time and date that the brawl started.
 - `brawl_type` - A `BrawlType` object.

## overwatchpy.BrawlType

   A type of brawl.

### Parameters

- `id` - The object's id.
- `name` - The object's name.
- `brawls` - A list of `Brawl`. Could be none.

## overwatchpy.Event

   An event.

### Parameters

 - `id` - The object's id.
 - `name` - The object's name.
 - `start_date` - The time and date that the event started.
 - `end_date` - The time and date that the event ended. Could be none.
 - `maps` - A list of `Map`
 - `rewards` - A list of `Reward`

## overwatchpy.GameMode

   A game mode.

### Parameters

- `id` - The object's id.
- `name` - The object's name.

## overwatchpy.Hero

   A hero.

### Parameters

- `id` - The object's id.
- `name` - The object's name. (E.g. Reaper)
- `description` - The object's description.
- `health` - The hero's health. (E.g. 200)
- `armor` - The hero's armor points.
- `shield` - The hero's shield points.
- `real_name` - The hero's actual name. (E.g. Gabriel Reyes)
- `age` - The hero's age. Could be none.
- `height` - The hero's height. Could be none if unknown.
- `affiliation` - The hero's affiliation. Could be none. (E.g. Overwatch)
- `base_of_operations` - The hero's Base of Operations. Could be none.
- `difficulty` - The hero's difficulty. Integer from 1 to 3
- `role` - A `Role` object.
- `sub_roles` - A `list` of `Role`. Could be none.
- `abilities` - A `list` of `Ability`.
- `rewards` - A `list` of `Reward`.

## overwatchpy.Map

   A map.

### Parameters

- `id` - The object's id.
- `name` - The object's name. (E.g. Illios)
- `location` - The map's location. (E.g. Greece)
- `mode` - A `BrawlType`.
- `stages` - A `list` of `MapStage`.
- `event` - The event the map was used for. Could be none.

## overwatchpy.MapStage

   A map stage.

### Parameters

- `id` - The object's id.
- `name` - The object's name.

## overwatchpy.Object

   A generic object.

### Parameters

- `id` - The object's id.
- `name` - The object's name.
- `properties` - A `dict` of extra properties.

## overwatchpy.Platform

   A game platform.

### Parameters

- `id` - The object's id.
- `name` - The object's name.

## overwatchpy.Reward

   A reward.

### Parameters

- `id` - The object's id.
- `name` - The object's name.
- `cost` - The cost in currency for the reward.
- `type` - A `RewardType` object.
- `hero` - The `Hero` that you get the reward from. Could be none.
- `quality` - The quality of the reward. (E.g. common)
- `event` - The event the reward was used for. Could be none.

## overwatchpy.RewardType

   A reward type.

### Parameters

- `id` - The object's id.
- `name` - The object's name.

## overwatchpy.Role

   A hero role.

### Parameters

- `id` - The object's id.
- `name` - The object's name.

# Exceptions

## overwatchpy.ClientError

   A client error occurred (Status code 4xx) while fetching a url.

### Parameters

 - `code` - The status code that was returned. (E.g. 404)
 - `message` - The message that was sent from the server. (E.g. Page Not Found)

## overwatchpy.ServerError

   A server error occurred (Status code 5xx) while fetching a url.

### Parameters

- `code` - The status code that was returned. (E.g. 500)
- `message` - The message that was sent from the server. (E.g. Internal Server Error)

## overwatchpy.RateLimitReached

   You have reached the rate limit of 500 requests per 60 minutes.

# Utilities

| Method                     | Description                                    | Returns            |
| -------------------------- | ---------------------------------------------- | ------------------ |
| get_abilities_from_json(a) | Gets a `list` of `Ability` from a JSON source. | `list`             |
| get_brawls_from_json(b)    | Gets a `list` of `Brawl` from a JSON source.   | `list`             |
| get_maps_from_json(m)      | Gets a `list` of `Map` from a JSON source.     | `list`             |
| get_rewards_from_json(r)   | Gets a `list` of `Reward` from a JSON source.  | `list`             |
| get_hero_from_json(h)      | Gets a `Hero` from a JSON source.              | `overwatchpy.Hero` |
