import requests
import requests.exceptions
from overwatchpy.objects import *
import overwatchpy.errors
import logging
import traceback

log = logging.getLogger(__name__)

null = None

class utils:
    def get(url, headers={}, user_agent=None, timeout=5000):
        if user_agent is None:
            user_agent = "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 OverwatchAPI/0.1.0"
        headers['user-agent'] = user-agent
        r = ""
        try:
            log.info("getting url {}".format(url))
            r = requests.get(url, headers=headers, timeout=timeout/1000)
            log.info("successfully retrieved url")
            log.debug("request returned:\n{}".format(r))
        except requests.exceptions.Timeout:
            log.error("request timed out")
            raise TimeoutError
        except Exception as e:
            log.error("request raised exception: {}".format(str(e)))
            log.error(traceback.format_exc())
            raise
        else:
            r = r.json()
            try:
                r.raise_for_status()
            except requests.exceptions.HTTPError as e:
                log.error("request returned error code {}: {}".format(e.status_code, e.reason))
                if str(e.status_code).startswith("4"):
                    raise overwatchpy.errors.ClientError(e.status_code, e.reason)
                elif str(e.status_code).startswith("5"):
                    raise overwatchpy.errors.ServerError(e.status_code, e.reason)
                else:
                    raise
            else:
                return r

        def get_abilities_from_json(ab):
            abilities = []
            for a in ab:
                abilities.append(Ability(a['id'], a['name'], a['description'], a['is_ultimate'], a['hero']))
            return abilities

        def get_brawls_from_json(br):
            brawls = []
            for b in br:
                brawls.append(Brawl(b['id'], b['start_date'], BrawlType(b['brawl_type']['id'], b['brawl_type']['name'])))

        def get_maps_from_json(ma):
            maps = []
            for m in ma:
                stages = []
                    for s in ma[len(maps)]['stages']:
                        stages.append(MapStage(s['id'], s['name']))
                maps.append(object.Map(m['id'], m['name'], m['location'], BrawlType(m['mode']['id']), stages, m['event']))
        def get_rewards_from_json(re):
            rewards = []
            for r in re:
                rewards.append(Reward(r['id'], r['name'], r['cost'], RewardType(r['type']['id'], r['type']['name']), r['hero'], r['quality'], r['event']))
            return rewards

        def get_hero_from_json(h):
            role = Role(h['role']['id'], h['role']['name'])
            sub_roles = []
            for sr in h['sub_roles']:
                sub_roles.append(Role(sr['id'], sr['name']))
            hero = Hero(h['id'], h['name'], h['description'], h['health'], h['armour'], h['shield'], h['real_name'], h['age'], h['height'], h['affiliation'], h['base_of_operations'], h['difficulty'], Role(h['role']['id'], h['role']['type']), get_subroles_from_json(h['sub_roles']), get_abilities_from_json(h['abilities']), get_rewards_from_json(h['rewards']))


class OWAPI:
    def __init__(self, headers={}, user_agent=None, api_version="v1"):
        self.headers
        self.user_agent = user_agent
        self.cache = cache
        self.api_version = api_version

    def get_ability(self, id):
        r = utils.get("https://overwatch-api.net/api/{0}/ability/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)
        r = r.json()
        h = Hero(r['hero']['id'], r['hero']['name'], None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        ability = Ability(r['id'], r['name'], r['description'], r['is_ultimate'], h)
        return ability

    def get_all_abilities(self):
        r = utils.get("https://overwatch-api.net/api/{0}/ability/?limit=999".format(self.api_version), self.headers, self.user_agent)
        r = r.json()
        abil = []
        for a in r['data']:
            abil.append(Ability(a['id'], a['name'], None, None, None))
        return abil

    def get_achievement(self, id):
        r = utils.get("https://overwatch-api.net/api/{0}/achievement/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)
        r = r.json()
        ach = Achievement(r['id'], r['name'], r['description'], Reward(r['reward']['id'], r['reward']['name'], r['reward']['cost'], RewardType(r['reward']['type']['id'], r['reward']['type']['name']), r['hero'], r['quality']['name'], event = None))
        return ach

    def get_all_achievements(self):
        r = utils.get("https://overwatch-api.net/api/{0}/achievement/?limit=999".format(self.api_version), self.headers, self.user_agent)
        r = r.json()
        ach = []
        for a in r['data']:
            ach.append(Achievement(a['id'], a['name'], None, None, None))
        return ach

    def get_brawl(self, id):
        r = utils.get("https://overwatch-api.net/api/{0}/brawl/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)
        r = r.json()
        br = Brawl(r['id'], r['start_date'], BrawlType(r['brawl_type']['id'], r['brawl_type']['name']))
        return br

    def get_all_brawls(self):
        r = utils.get("https://overwatch-api.net/api/{0}/brawl/?limit=999".format(self.api_version), self.headers, self.user_agent)
        r = r.json()
        ach = []
        for a in r['data']:
            ach.append(Brawl(a['id'], a['name'], None, None, None))
        return ach

    def get_brawltype(self, id):
        r = utils.get("https://overwatch-api.net/api/{0}/brawl-type/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)
        r = r.json()
        br = utils.get_brawls_from_json(r['brawls'])
        bt = BrawlType(r['id'], r['name'], br)
        return bt

    def get_all_brawltypes(self):
        r = utils.get("https://overwatch-api.net/api/{0}/brawl-type/?limit=999".format(self.api_version), self.headers, self.user_agent)
        r = r.json()
        ach = []
        for a in r['data']:
            ach.append(BrawlType(a['id'], a['name'], None))
        return ach

    def get_event(self, id):
        r = utils.get("https://overwatch-api.net/api/{0}/event/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)
        r = r.json()
        ev = Event(r['id'], r['name'], r['start_date'], r['end_date'], utils.get_maps_from_json(r['maps']), utils.get_rewards_from_json(r['rewards']))
        return ev

    def get_all_events(self):
        r = utils.get("https://overwatch-api.net/api/{0}/event/?limit=999".format(self.api_version), self.headers, self.user_agent)
        r = r.json()
        ach = []
        for a in r['data']:
            ach.append(Event(a['id'], a['name'], None, None, None, None))
        return ach

    def get_gamemode(self, id):
        r = utils.get("https://overwatch-api.net/api/{0}/game-mode/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)
        r = r.json()
        gm = GameMode(r['id'], r['name'])

    def get_all_gamemodes(self):
        r = utils.get("https://overwatch-api.net/api/{0}/game-mode/?limit=999".format(self.api_version), self.headers, self.user_agent)
        r = r.json()
        ach = []
        for a in r['data']:
            ach.append(GameMode(a['id'], a['name']))
        return ach

    def get_hero(self, id):
        r = utils.get("https://overwatch-api.net/api/{0}/hero/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)
        r = r.json()
        sub_roles = []
        for sr in h['sub_roles']:
            sub_roles.append(Role(sr['id'], sr['name']))
        he = Hero(r['id'], r['name'], r['description'], r['health'], r['armor'], r['shield'], r['real_name'], r['age'], r['height'], r['affiliation'], r['base_of_operations'], r['difficulty'], Role(r['role']['id'], r['role']['name']), sub_roles, utils.get_abilities_from_json(r['abilities']), utils.get_rewards_from_json(r['rewards']))
        return he

    def get_all_heroes(self):
        r = utils.get("https://overwatch-api.net/api/{0}/hero/?limit=999".format(self.api_version), self.headers, self.user_agent)
        r = r.json()
        ach = []
        for a in r['data']:
            ach.append(Hero(r['id'], r['name'], None, None, None, None, None, None, None, None, None, None, None, None, None, None))
        return ach

    def get_map(self, id):
        r = utils.get("https://overwatch-api.net/api/{0}/map/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)
        ma = r.json()
        stages = []
            for s in ma['stages']:
                stages.append(MapStage(s['id'], s['name']))
        mp = object.Map(ma['id'], ma['name'], ma['location'], BrawlType(ma['mode']['id']), stages, ma['event'])
        return mp

    def get_all_maps(self):
        r = utils.get("https://overwatch-api.net/api/{0}/map/?limit=999".format(self.api_version), self.headers, self.user_agent)
        r = r.json()
        ach = []
        for a in r['data']:
            ach.append(Map(a['id'], a['name'], None, None, None, None))
        return ach

    def get_platform(self, id):
        r = utils.get("https://overwatch-api.net/api/{0}/platform/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)
        r = r.json()
        return Platform(r['id'], r['name'])

    def get_all_platforms(self):
        r = utils.get("https://overwatch-api.net/api/{0}/platform/?limit=999".format(self.api_version), self.headers, self.user_agent)
        r = r.json()
        ach = []
        for a in r['data']:
            ach.append(Platform(a['id'], a['name']))
        return ach

    def get_reward(self, id):
        r = utils.get("https://overwatch-api.net/api/{0}/reward/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)
        r = r.json()
        h = Hero(r['hero']['id'], r['hero']['name'], None, None, None, None, None, None, None, None, None, None, None, None, None, None)
        re = Reward(r['id'], r['name'], r['cost']['value'], RewardType(r['type']['id'], r['type']['name']), h, r['quality']['name'], r['event'])

    def get_all_rewards(self):
        r = utils.get("https://overwatch-api.net/api/{0}/reward/?limit=9999".format(self.api_version), self.headers, self.user_agent)
        r = r.json()
        ach = []
        for a in r['data']:
            ach.append(Reward(a['id'], a['name'], None, None, None, None, None))
        return ach

    def get_rewardtype(self, id):
        r = utils.get("https://overwatch-api.net/api/{0}/reward-type/{1}".format(self.api_version, str(id)), self.headers, self.user_agent)
        r = r.json()
        return RewardType(r['id'], r['name'])

    def get_all_rewardtypes(self):
        r = utils.get("https://overwatch-api.net/api/{0}/reward-type/?limit=999".format(self.api_version), self.headers, self.user_agent)
        r = r.json()
        ach = []
        for a in r['data']:
            ach.append(RewardType(a['id'], a['name']))
        return ach
