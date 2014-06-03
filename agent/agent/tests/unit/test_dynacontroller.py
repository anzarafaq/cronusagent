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
from agent.tests import *
import logging

from agent.tests.unit.test_util import commonSetup, createManifest,\
    activateManifest, deactivateManifest
from agent.tests.unit.test_util import commonTearDown
import sys

LOG = logging.getLogger(__name__)

class TestDynaController(TestController):


    def setUp(self):
        commonSetup()

    def tearDown(self):
        commonTearDown()

    def testdynautils(self):
        pass

    def test_activateDynaController(self):
        pass
        #createManifest(self, packages = ["http://github.com/yubin154/cronusagent/blob/master/agent/agent/tests/unit/packages/discoverservice-1.0.5.unix.cronus"], manifest = "baz")
        #activateManifest(self, manifest = "baz")
        #assert 'discoverservice.controllers.discoverService' in sys.modules
        #response = self.app.get('/appservices/%s/index' % 'discoverService',
        #                        headers = {'Content-Type' : 'application/json', 'AUTHZ_TOKEN' : 'donoevil'})
        #assert response.status_int == 200, 'Dyna controller assert'

        #LOG.debug('response body = %s' % response.body)
        #deactivateManifest(self, manifest = "baz")
        #assert 'discoverservice.controllers.discoverService' not in sys.modules
        #response = self.app.get('/appservices/%s/index' % 'discoverService',
        #                        headers = {'Content-Type' : 'application/json', 'AUTHZ_TOKEN' : 'donoevil'},
        #                        expect_errors = True)
        #assert response.status_int == 404, 'Dyna controller assert'
