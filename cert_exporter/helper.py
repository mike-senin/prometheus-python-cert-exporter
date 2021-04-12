import os
from datetime import datetime
from os import walk

import OpenSSL.crypto as crypto


def check_certs_recursively(root_dir, now_time, gauge):
    extensions = ('crt')
    for (dirpath, dirnames, filenames) in walk(root_dir):
        for filename in filenames:
            if not filename.endswith(extensions):
                continue
            cert_file_path = os.path.join(root_dir, filename)
            with open(cert_file_path, 'rt') as cert_file:
                st_cert = cert_file.read()
                cert = crypto.load_certificate(crypto.FILETYPE_PEM, st_cert)
                expirationDate = datetime.strptime(
                    cert.get_notAfter().decode("utf-8"), "%Y%m%d%H%M%SZ"
                )
                delta = expirationDate - now_time
                gauge.labels(
                    cert_file_path=cert_file_path
                ).set(delta.days)
        for directory in dirnames:
            new_root = os.path.join(root_dir, directory)
            check_certs_recursively(new_root, now_time, gauge)
        break
    return
