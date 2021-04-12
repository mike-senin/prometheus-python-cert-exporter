# prometheus-python-cert-exporter

docker build -t prometheus-python-cert-exporter .
docker tag prometheus-python-cert-exporter:latest docker-registry:5000/prometheus-python-cert-exporter:latest
docker push docker-registry:5000/prometheus-python-cert-exporter:latest
docker run -it --rm --name prometheus-python-cert-exporter --expose=8000 -p 8000:8000 -v /etc/kubernetes/pki/:/etc/kubernetes/pki/ prometheus-python-cert-exporter