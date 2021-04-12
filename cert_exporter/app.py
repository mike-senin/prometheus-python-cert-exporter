import argparse
from datetime import datetime

from prometheus_client import Gauge, start_http_server

from cert_exporter.helper import check_certs_recursively

EXPIRATION_TIME = Gauge('k8s_cert_expiration_time',
                        'Certificate expiration time',
                        ['cert_file_path'])


def parse_certs_time_expiration(root_certs_path):
    now = datetime.now()
    check_certs_recursively(root_certs_path, now, EXPIRATION_TIME)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root-certs-path", type=str,
                        default="/etc/kubernetes/pki/",
                        help="Specify path to k8s certs")
    args = parser.parse_args()
    return args


def main():
    options = parse_args()
    # Start up the server to expose the metrics.
    start_http_server(8000)
    while True:
        parse_certs_time_expiration(options.root_certs_path)


if __name__ == '__main__':
    main()