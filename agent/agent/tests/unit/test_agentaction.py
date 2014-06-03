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
from agent.lib import agenthealth, utils
from agent.tests import TestController
from agent.tests.unit.test_util import commonSetup, commonTearDown
import logging

LOG = logging.getLogger(__name__)

class TestActionController(TestController):


    def setUp(self):
        commonSetup()

    def tearDown(self):
        commonTearDown()
        
    def test_get_linux_distro(self):
        linux_distro = utils.get_linux_distro()
        assert linux_distro is not None

    def test_load_version(self):
        wiri = agenthealth.loadVersion()
        assert wiri is not None
        
    def test_check_agent_version_startup(self):
        agenthealth.checkAgentVersion(True)
