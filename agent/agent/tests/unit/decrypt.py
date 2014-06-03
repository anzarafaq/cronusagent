'''
Copyright 2014 eBay Software Foundation

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
"""this is a really limited example that will create a new
key and sign it with the ca
"""
import pki
from pki.utils import plus_twentyyears
import datetime
now = datetime.datetime.now
from M2Crypto import Rand
from M2Crypto import X509, RSA

my_org = "AAA My Organization"
my_location = "My City and Country"
# in the certname you should give the hostname that will be used to
# access the protected resource ie: www.mysuperdomain.com
my_certname = "localhost"
my_caname = "AAA My Certificate Authority"

def ca_passphrase_callback(*args):
    """the password cannot be blank or the stack fails and you should really
    give some more secure and complicated password.
    """
    return "44"

def passphrase_callback(*args):
    """the password cannot be blank or the stack fails and you should really
    give some more secure and complicated password.
    """
    return "pass"

def create_x509_cert(ca_cert, cacert_privkey, serial):
    mynow = now()
    cert, pub, priv = pki.create_x509_certificate(ca_cert, cacert_privkey,
            cert_passphrase_callback=passphrase_callback,
            ca_passphrase_callback=ca_passphrase_callback,
            notbefore=mynow, notafter=plus_twentyyears(mynow),
            serial=serial,
            O=my_org, L=my_location,
            CN=my_certname)

    return cert, pub, priv

if __name__ == '__main__':
 
    # reload the certs from disk
    f = open('ca.cert', 'r')
    ca_cert_content = f.read()
    f.close()

    cert = X509.load_cert_string(ca_cert_content)
    pub = RSA.load_pub_key('pub')
    priv = RSA.load_key('priv', callback=passphrase_callback)

    # test some data encryption/decryption with the reloaded keys
    k = "BvTgG/RJf7AhMvz60+m+3vzThkpvNm6kOqKl1tTo4copVmJZIEI7FElWT+yQ+a8mEknicGUKg33jpluOEKSS5HQRFT66DpXJ08Z3tx2pJTMSwNQBA+RGjp4nSHESPxRfKD6VGOmOd311IRvrWVzFV+l6sjRM2gLsHIzq/r/86tCJpXAtyFNb7aYTecrRDYEEkqCcv2Hs0mgatdpOlOGrzLf9W60I+ZLB50Ce14a+QtozyHyy5NSiPECsoYm7wuhfGQwmA2TPNEXcyhAP6mFmXy18qS25JnrxFRsGdOxHb5OZU+DIkz1QJmkET8UeYgUeyOPVYyAPKtF8o4wxigQHQQ=="
    p = pki.decrypt(priv, k)
    print p

#    #Rand.load_file('randpool', -1)
#    f = open('ca_certificate.pem', 'r')
#    ca_cert_content = f.read()
#    ca_cert = X509.load_cert_string(ca_cert_content)
#
#    cacert_privkey = RSA.load_key('ca_privkey.pem', callback=ca_passphrase_callback)
#
#    # serial should be autocalculated from the repository of existing (past and present) keys
#    serial = 3
#    cert, pub, priv = create_x509_cert(ca_cert, cacert_privkey, serial)
#
#    # the client certificate
#    cert.save_pem('%03d_client_certificate.pem' % serial)
#    
#    pub.save_key('%03d_client_pubkey.pem' % serial)
#    # at the moment of saving the key to a file we do not want
#    # to put a password on it... this is because we have applications
#    # that cannot open keys with passwords... It is recommended that you
#    # set a password on your keyfiles if your applications know how to
#    # load a key with a password.
#    priv.save_key('%03d_client_privkey.pem' % serial, callback=passphrase_callback)
#    #Rand.save_file('randpool')