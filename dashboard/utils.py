import OpenSSL

class certTasks():
    def handle_uploaded_file(f):
        with open('dashboard/test.txt', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    def sniQuery(servicename, port):
        # produces a certificate DER hash
        cert = ssl.get_server_certificate((servicename,port))
        # returns the components of the subject line
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
        x509.get_subject().get_components()
