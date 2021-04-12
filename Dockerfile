FROM python:3
LABEL maintainer="msenin94@gmail.com"
EXPOSE 8000/tcp

WORKDIR /cert_exporter/
RUN pip install --no-cache-dir poetry==1.1.5
COPY . .
RUN poetry install

CMD [ "poetry", "run", "cert-exporter", "--root-certs-path",  "/etc/kubernetes/pki/" ]