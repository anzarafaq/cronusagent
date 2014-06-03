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
from agent.tests import TestController
from agent.lib.utils import getHostIP
from agent.tests.unit.test_util import checkStatus, commonSetup, commonTearDown
from pylons import url
import json
import logging
import os
import pylons
import re
import shutil
import time

#from murder_tracker import MurderTracker

LOG = logging.getLogger(__name__)

class TestDistributionController(TestController):
    __tracker = None

    def __init__ (self, args):
        TestController.__init__(self, args)

    def setUp(self):
        commonSetup()
        try:
            shutil.rmtree(pylons.config['repo_root'])
        except:
            pass
        try:
            os.makedirs(pylons.config['repo_root'])
        except:
            pass

        assert os.path.exists(pylons.config['agent_root'])
        assert os.path.exists(pylons.config['repo_root'])


    def tearDown(self):
        time.sleep(1)
        commonTearDown()

    def test_startdownload_with_packageloc(self):
        package = "perlserver-1.0.0.unix.cronus"
        packageloc = "testPkg-0.0.1.unix.cronus"
        body = json.dumps({'package': 'http://repository.qa.ebay.com/cronus/test-data/agent/' + package, 'packageloc': packageloc})
        response = self.app.post(url(controller = 'distribution', action = 'startdownload', service = "dist"),
                                 headers = {'Content-Type' : 'application/json'},
                                 params = body, expect_errors = True)

        assert response.status_int == 200, 'good http download assert'
        checkStatus(self, "http_download", response, 100)
        assert os.path.exists(os.path.join(pylons.config['repo_root'], packageloc))
        assert os.path.exists(os.path.join(pylons.config['repo_root'], packageloc + '.prop'))

    def test_ipaddr(self):
        ipaddr = getHostIP()
        if ipaddr is None or ipaddr == '127.0.0.1':
            raise
        #now check it is ipv4 and not ipv6
        ipRe = re.compile('([0-9]+).([0-9]+).([0-9]+).([0-9]+)')
        match = ipRe.match(ipaddr)
        assert match is not None
        assert match.group(0) == ipaddr
