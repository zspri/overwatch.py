import requests
import requests.exceptions
from overwatchpy.objects import *
import overwatchpy.utils
import overwatchpy.errors
import logging
import traceback

log = logging.getLogger(__name__)

null = None

class OWAPI:
    def __init__(self, headers={}, user_agent=None, api_version="v1"):
        self.headers = headers
        self.user_agent = user_agent
        self.api_version = api_version
        log.debug("Created new OWAPI instance " + str(self))

    def get_ability(self, id):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/ability/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)

        h = Hero(r['hero']['id'], r['hero']['name'], None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        ability = Ability(r['id'], r['name'], r['description'], r['is_ultimate'], h)
        return ability

    def get_all_abilities(self):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/ability/?limit=999".format(self.api_version), self.headers, self.user_agent)

        abil = []
        for a in r['data']:
            abil.append(Ability(a['id'], a['name'], None, None, None))
        return abil

    def get_achievement(self, id):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/achievement/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)

        ach = Achievement(r['id'], r['name'], r['description'], Reward(r['reward']['id'], r['reward']['name'], r['reward']['cost'], RewardType(r['reward']['type']['id'], r['reward']['type']['name']), r['hero'], r['quality']['name'], event = None))
        return ach

    def get_all_achievements(self):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/achievement/?limit=999".format(self.api_version), self.headers, self.user_agent)

        ach = []
        for a in r['data']:
            ach.append(Achievement(a['id'], a['name'], None, None, None))
        return ach

    def get_brawl(self, id):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/brawl/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)

        br = Brawl(r['id'], r['start_date'], BrawlType(r['brawl_type']['id'], r['brawl_type']['name']))
        return br

    def get_all_brawls(self):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/brawl/?limit=999".format(self.api_version), self.headers, self.user_agent)

        ach = []
        for a in r['data']:
            ach.append(Brawl(a['id'], a['name'], None, None, None))
        return ach

    def get_brawltype(self, id):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/brawl-type/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)

        br = overwatchpy.utils.get_brawls_from_json(r['brawls'])
        bt = BrawlType(r['id'], r['name'], br)
        return bt

    def get_all_brawltypes(self):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/brawl-type/?limit=999".format(self.api_version), self.headers, self.user_agent)

        ach = []
        for a in r['data']:
            ach.append(BrawlType(a['id'], a['name'], None))
        return ach

    def get_event(self, id):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/event/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)

        ev = Event(r['id'], r['name'], r['start_date'], r['end_date'], overwatchpy.utils.get_maps_from_json(r['maps']), overwatchpy.utils.get_rewards_from_json(r['rewards']))
        return ev

    def get_all_events(self):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/event/?limit=999".format(self.api_version), self.headers, self.user_agent)

        ach = []
        for a in r['data']:
            ach.append(Event(a['id'], a['name'], None, None, None, None))
        return ach

    def get_gamemode(self, id):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/game-mode/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)

        gm = GameMode(r['id'], r['name'])
        return gm

    def get_all_gamemodes(self):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/game-mode/?limit=999".format(self.api_version), self.headers, self.user_agent)

        ach = []
        for a in r['data']:
            ach.append(GameMode(a['id'], a['name']))
        return ach

    def get_hero(self, id):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/hero/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)
        h =  overwatchpy.utils.get_hero_from_json(r)
        return h

    def get_all_heroes(self):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/hero/?limit=999".format(self.api_version), self.headers, self.user_agent)

        ach = []
        for a in r['data']:
            ach.append(Hero(r['id'], r['name'], None, None, None, None, None, None, None, None, None, None, None, None, None, None))
        return ach

    def get_map(self, id):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/map/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)
        ma = r.json()
        stages = []
        for s in ma['stages']:
            stages.append(MapStage(s['id'], s['name']))
        mp = object.Map(ma['id'], ma['name'], ma['location'], BrawlType(ma['mode']['id']), stages, ma['event'])
        return mp

    def get_all_maps(self):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/map/?limit=999".format(self.api_version), self.headers, self.user_agent)

        ach = []
        for a in r['data']:
            ach.append(Map(a['id'], a['name'], None, None, None, None))
        return ach

    def get_platform(self, id):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/platform/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)
        return Platform(r['id'], r['name'])

    def get_all_platforms(self):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/platform/?limit=999".format(self.api_version), self.headers, self.user_agent)

        ach = []
        for a in r['data']:
            ach.append(Platform(a['id'], a['name']))
        return ach

    def get_reward(self, id):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/reward/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)

        h = Hero(r['hero']['id'], r['hero']['name'], None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        re = Reward(r['id'], r['name'], r['cost']['value'], RewardType(r['type']['id'], r['type']['name']), h, r['quality']['name'], r['event'])
        return re

    def get_all_rewards(self):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/reward/?limit=9999".format(self.api_version), self.headers, self.user_agent)

        ach = []
        for a in r['data']:
            ach.append(Reward(a['id'], a['name'], None, None, None, None, None))
        return ach

    def get_rewardtype(self, id):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/reward-type/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)

        return RewardType(r['id'], r['name'])

    def get_all_rewardtypes(self):
        r = overwatchpy.utils.get("https://overwatch-api.net/api/{0}/reward-type/?limit=999".format(self.api_version), self.headers, self.user_agent)

        ach = []
        for a in r['data']:
            ach.append(RewardType(a['id'], a['name']))
        return ach
