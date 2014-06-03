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
'''
Created on Feb 21, 2014

@author: biyu
'''
import logging
import unittest

import pki
import os
from M2Crypto import X509, RSA

my_org = "My Organization"
my_location = "My City and Country"
my_certname = "My Certificate"
my_caname = "My Certificate Authority"

def passphrase_callback(*args):
    """this is a callback that will return the password for the ca
    when called. In real life you'll use an equivalent mechanism but
    will make sure you get the password from the user or from a secured
    file somewhere...
    """
    return 'pass'

LOG = logging.getLogger(__name__)

class TestPkiutil(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
        
    def test_decrypt_using_files(self):
        ca_cert, pubkey, privkey = pki.create_certificate_authority(
                                                                    passphrase_callback=passphrase_callback,
                                                                    O=my_org,
                                                                    L=my_location,
                                                                    CN=my_caname)

        cert, pub, priv = pki.create_x509_certificate(ca_cert, privkey,
                                                          cert_passphrase_callback=passphrase_callback,
                                                          ca_passphrase_callback=passphrase_callback,
                                                          O=my_org, L=my_location,
                                                          CN=my_certname)

        # save the files to disk
        cert.save_pem('ca.cert')
        pub.save_key('pub')
        priv.save_key('priv', callback=passphrase_callback)
    
        # remove references from memory
        del cert
        del pub
        del priv

        # reload the certs from disk
        f = open('ca.cert', 'r')
        ca_cert_content = f.read()
        f.close()

        cert = X509.load_cert_string(ca_cert_content)
        pub = RSA.load_pub_key('pub')
        priv = RSA.load_key('priv', callback=passphrase_callback)

        # remove the files from disk
        os.unlink('ca.cert')
        os.unlink('pub')
        os.unlink('priv')

        # test some data encryption/decryption with the reloaded keys
        clear_data = 'clear_data'
        k = pki.encrypt(cert.get_pubkey(), clear_data)
        p = pki.decrypt(priv, k)
        assert p == clear_data
        
if __name__ == "__main__":
    unittest.main()
