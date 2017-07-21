class Ability:
    def __init__(self, id, name, description, is_ult, hero):
        self.id = id
        self.name = name
        self.description = description
        self.is_ult = is_ult
        self.hero = hero

class Achievement:
    def __init__(self, id, name, description, reward, hero = None):
        self.id = id
        self.name = name
        self.description = description
        self.reward = reward
        self.hero = hero

class Brawl:
    def __init__(self, id, start_date, brawl_type):
        self.id = id
        self.start_date = start_date
        self.brawl_type = brawl_type

class BrawlType:
    def __init__(self, id, name, brawls = []):
        self.id = id
        self.name = name
        self.brawls = brawls

class Event:
    def __init__(self, id, name, start_date, end_date, maps, rewards):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.maps = maps
        self.rewards = rewards

class GameMode:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Hero:
    def __init__(self, id, name, description, health, armor, shield, real_name, age, height, affiliation, base_of_operations, difficulty, role, sub_roles, abilities, rewards):
        self.id = id
        self.name = name
        self.description = description
        self.health = health
        self.armor = armor
        self.shield = shield
        self.real_name = real_name
        self.age = age
        self.height = height
        self.affiliation = affiliation
        self.base_of_operations = base_of_operations
        self.difficulty = difficulty
        self.role = role
        self.sub_roles = sub_roles
        self.abilities = abilities
        self.rewards = rewards

class Map:
    def __init__(self, id, name, location, mode, stages, event):
        self.id = id
        self.name = name
        self.location = location
        self.mode = mode
        self.stages = stages
        self.event = event

class MapStage:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Object:
    def __init__(self, id, name, **kwargs):
        self.id = id
        self.name = name
        self.properties = kwargs

class Platform:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Reward:
    def __init__(self, id, name, cost, _type, hero, quality, event = None):
        self.id = id
        self.name = name
        self.cost = cost
        self.type = _type
        self.hero = hero
        self.quality = quality
        self.event = event

class RewardType:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Role:
    def __init__(self, id, name):
        self.id = id
        self.name = name
