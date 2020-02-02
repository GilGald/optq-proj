import redis
import random
import json


class ScoringService(object):
    def __init__(self):
        self.conn = redis.StrictRedis(host='redis1',decode_responses=True)

    def get_score_per_customer(self, customer_id):
        all_data = self.conn.hgetall(customer_id)

        data_by_score = {}
        for data in all_data.keys():
            data_by_score[data] = random.uniform(0, 1)

        data_by_score = sorted(data_by_score.items(), key=lambda x: x[1], reverse=True)
        dumps = json.dumps(data_by_score)
        return dumps


print(ScoringService().get_score_per_customer("bezeq"))
