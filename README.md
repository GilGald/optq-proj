# optimal q

in project directory run:
```
docker network create my_app &&
docker build -f DockerFileScoring -t scoring_server:1.0 . &&
docker build -f DockerFile -t optq_server:1.0 . &&
docker run -d -p 6379:6379 --net my_app --name redis1 redis &&
docker run -d -p 8080:8080 --net my_app --name scoring_server  scoring_server:1.0 &&
docker run -d -p 5000:5000 --net my_app --name optimalq_server  optq_server:1.0
```


add leads:
``` 

curl -d '{ "leads":{"name1": "some_data1", "name2": "some_data2", "name3": "some_data3", "name4": "some_data4", "name5": "some_data5", "name6": "some_data6", "name7":"some_data7"} ,"customer":"bezeq"}' -H "Content-Type: application/json" -X POST http://localhost:5000/leads 

will add a mock of leads just for demo purposes in redis db and customer id is bezeq
```

get optimal per client
```
http://localhost:5000/<customer_id>/leads/<leads_count>
http://localhost:5000/bezeq/leads/

```

scoring server API:
```
http://0.0.0.0:8080/<customer_id>/scores
http://0.0.0.0:8080/bezeq/scores
```


update percentage :
```
curl -d '{ "percentage":0.5,"server_url":"http://scoring_server:8080"}' -H "Content-Type: application/json" -X POST http://localhost:5000/scoring_servers/percentage 

```