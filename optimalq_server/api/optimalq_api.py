from distutils.command.config import config

from flask import Flask, request
from services.leads_service import LeadsService, ScoringDataService
from services.optimalq_service import OptimalQService

app = Flask(__name__)
app.run(host='0.0.0.0', port=5000, debug=True)

leads_service = LeadsService()
scoring_data_service = ScoringDataService()
optimalq_service = OptimalQService(scoring_data_service=scoring_data_service)


@app.route('/leads', methods=['POST'])
def add_leads():
    content = request.json
    leads_service.update_leads(customer_id=content['customer'],
                               leads=content['leads'])
    return "adding leads"


@app.route('/scoring_servers/percentage', methods=['POST'])
def update_percentage():
    content = request.json
    percentage = content['percentage']
    server_url = content['server_url']
    scoring_data_service.update_percentage(percentage=percentage,
                                           server_url=server_url)
    return "updating percentage"


@app.route('/<customer_id>/leads/<count>', methods=['GET'])
def get_optimal(customer_id, count=0):
    return optimalq_service.get_score_per_customer(customer_id=customer_id, count=count)


@app.route('/')
def get():
    return "hello from optimal Q server"

