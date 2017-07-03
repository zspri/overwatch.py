import requests
import requests.exceptions
from overwatchpy.objects import *
import logging
import traceback

log = logging.getLogger(__name__)

def get(url, headers={}, user_agent=None, timeout=5000):
    if user_agent is None:
        user_agent = "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 OverwatchAPI/0.1.0"
    headers['user-agent'] = user_agent
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
        re = r.json()
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            log.error(traceback.format_exc())
            raise
        except:
            raise
        else:
            return re

def get_abilities_from_json(ab):
    abilities = []
    hero = ""
    for a in ab:
        try:
            if 1 == a['hero']:
                pass
            hero = a['hero']
        except KeyError:
            hero = None
        abilities.append(Ability(a['id'], a['name'], a['description'], a['is_ultimate'], hero))
    return abilities

def get_brawls_from_json(br):
    brawls = []
    for b in br:
        brawls.append(Brawl(b['id'], b['start_date'], BrawlType(b['brawl_type']['id'], b['brawl_type']['name'])))
    return brawls

def get_maps_from_json(ma):
    maps = []
    for m in ma:
        stages = []
        for s in m['stages']:
            stages.append(MapStage(s['id'], s['name']))
        maps.append(object.Map(m['id'], m['name'], m['location'], BrawlType(m['mode']['id']), stages, m['event']))
    return maps

def get_rewards_from_json(re):
    rewards = []
    hero = ""
    for r in re:
        try:
            if 1 == r['hero']:
                pass
            hero = r['hero']
        except KeyError:
            hero = None
        rewards.append(Reward(r['id'], r['name'], r['cost'], RewardType(r['type']['id'], r['type']['name']), hero, r['quality'], r['event']))
    return rewards

def get_hero_from_json(h):
    role = Role(h['role']['id'], h['role']['name'])
    sub_roles = []
    for sr in h['sub_roles']:
        sub_roles.append(Role(sr['id'], sr['name']))
    hero = Hero(h['id'], h['name'], h['description'], h['health'], h['armour'], h['shield'], h['real_name'], h['age'], h['height'], h['affiliation'], h['base_of_operations'], h['difficulty'], Role(h['role']['id'], h['role']['name']), sub_roles, get_abilities_from_json(h['abilities']), get_rewards_from_json(h['rewards']))
    return hero
