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
from agent.lib.packagemgr import PackageMgr
import logging
import pylons
import shutil
import os

from agent.lib.agent_globals import stopAgentGlobals
from agent.lib.agent_globals import startAgentGlobals
from agent.tests.unit.test_util import commonSetup
from agent.tests.unit.test_util import commonTearDown

LOG = logging.getLogger(__name__)

class TestPackageMgr(TestController):

    def setUp(self):
        commonSetup()

    def tearDown(self):
        commonTearDown()

    def test_init(self):
        # test the init routine

        # make sure that the initial path is cleared out of IN Progress nodes
        tmpFile = os.path.join(PackageMgr.packagePath(), 'foo.inprogress')
        open(tmpFile, 'w').close()

        tmpFile2 = os.path.join(PackageMgr.packagePath(), 'foo2.inprogress')
        open(tmpFile2, 'w').close()

        stopAgentGlobals()
        startAgentGlobals()

        # we removed logic of clean up inprogress file
#        assert not os.path.exists(tmpFile)
#        assert not os.path.exists(tmpFile2)
