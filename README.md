## Budowanie obrazu
$ docker build -t ghcr.io/piotronwork/flask-img-dashboard:1-0-1 .

## Push do registry
$ docker push ghcr.io/piotronwork/flask-img-dashboard:1-0-1

## Generowanie secretow - uzupelnic o usera i token
kubectl create secret docker-registry ghcr-secret \
  --docker-server=ghcr.io \
  --docker-username=user_do_dockerhuba \
  --docker-password='token_do_dockerhuba' \
  --docker-email=piotr.on.work@gmail.com \
  --dry-run=client -o yaml > secrets.yaml

## Namespace
kubectl create ns flask-dashboard

## Deploy aplikacji
kubectl apply -f secrets.yaml -n flask-dashboard 
kubectl apply -f deployment.yaml -n flask-dashboard 
kubectl apply -f service.yaml -n flask-dashboard 

## Forwardowanie portu
kubectl port-forward service/flask-dashboard 8080:8080 -n flask-dashboard

