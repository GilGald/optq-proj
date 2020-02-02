from flask import Flask

from services.scoring_service import ScoringService

app = Flask(__name__)
app.run(host='0.0.0.0', port=8080, debug=True)

scoring_service = ScoringService()


@app.route('/<customer_id>/scores', methods=['GET'])
def get_optimal(customer_id):
    return scoring_service.get_score_per_customer(customer_id=customer_id)


@app.route('/')
def get():
    return "hello from scoring service"
