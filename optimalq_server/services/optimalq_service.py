import json

import requests as req

from services.leads_service import ScoringDataService


class OptimalQService(object):
    def __init__(self, scoring_data_service: ScoringDataService):
        # list of all the scoring services
        self.scoring_data_service = scoring_data_service
        self._scoring_services = {"http://scoring_server:8080"}

    def get_score_per_customer(self, customer_id, count=10):
        responses = list()
        percentage_per_server = list()
        for service_url in self._scoring_services:
            url = f"{service_url}/{customer_id}/scores"
            response = req.get(url=url)
            # return response.content
            percentage_per_service = self.scoring_data_service.get_percentage_per_service(server_name=service_url)
            percentage_per_server.append(percentage_per_service)
            responses.append(dict(json.loads(response.content)))

        return self._calc_top_leads(responses=responses, count=count, percentage_per_server=percentage_per_server)

    def _calc_top_leads(self, responses, percentage_per_server, count=10):
        # this is just a mock but should iterarte over every response and add take into account the percentage
        return json.dumps(list((responses[0]).items())[0:int(count)])
