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
Created on Aug 10, 2011

@author: srengarajan
'''
from agent.tests import *
import logging

from agent.tests.unit.test_util import commonSetup
from agent.tests.unit.test_util import commonTearDown
import re


LOG = logging.getLogger(__name__)

class TestValidateInternals(TestController):

    def setUp(self):
        commonSetup()

    def tearDown(self):
        commonTearDown()


    def test_password_masks(self):
        response = self.app.get(url('/agent/ValidateInternals.html'))
        assert response.status_int == 200, 'Agent validate internals pass'
        pattern = re.compile('.*(password.*\\*{6}).*', re.MULTILINE|re.DOTALL)
        assert pattern.match(response.body) is not None, 'Password is not masked'

    def test_getlog(self):
        response = self.app.get(url('/agent/logs'))
        assert response.status_int == 200, 'Agent log page pass'
        response = self.app.get(url('/agent/logs/agent.log'))
        assert response.status_int == 200, 'Agent log detail page pass'

    def test_getagenthealth(self):
        response = self.app.get(url('/agent/agenthealth'))
        assert response.status_int == 200, 'Agent health page pass'

    def test_getmonitors(self):
        response = self.app.get(url('/agent/monitors'))
        assert response.status_int == 200, 'Agent monitors page pass'

    def test_getthreads(self):
        response = self.app.get(url('/agent/threads'))
        assert response.status_int == 200, 'Agent thread page pass'
