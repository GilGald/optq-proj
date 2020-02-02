from typing import Dict

import redis


class LeadsService(object):

    def __init__(self):
        self.conn = redis.StrictRedis(host='redis1', decode_responses=True)

    def update_leads(self, customer_id, leads):
        self.conn.hmset(customer_id, leads)

    def remove_leads(self, customer_id, leads: Dict):
        self.conn.hdel(customer_id, leads.keys())


class ScoringDataService(object):

    def __init__(self):
        self.conn = redis.StrictRedis(host='redis1', decode_responses=True)

    def update_percentage(self, server_url, percentage):
        self.conn.hset("ScoringDataService", server_url, percentage)

    def get_percentage_per_service(self, server_name):
        hget = self.conn.hget("ScoringDataService", server_name)
        if hget is None:
            return 1
        else:
            return int(hget)
