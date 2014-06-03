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
from agent.lib.scheduler import ThreadedScheduler
from agent.lib.agent_globals import stopAgentGlobals

import time

import logging
LOG = logging.getLogger(__name__)

class TestScheduler(TestController):
    def setUp(self):
        self.flag = False

    def tearDown(self):
        stopAgentGlobals()

    def testDelay(self):
        def setFlag(flag):
            self.flag = True

        self.flag = False
        sheduler = ThreadedScheduler()
        sheduler.add_interval_task(setFlag, "sleep second", 2, 1, [True], None)
        sheduler.start()

        time.sleep(1)
        assert not self.flag

        time.sleep(2)
        assert self.flag

        sheduler.stop()

    def testScheduler(self):
        def flipFlag():
            self.flag = not self.flag

        self.flag = False
        sheduler = ThreadedScheduler()
        sheduler.add_interval_task(flipFlag, "sleep second", 1, 2, [], None)
        sheduler.start()

        assert not self.flag

        time.sleep(2)
        assert self.flag

        time.sleep(2)
        assert not self.flag

    def testScheduler_start_first(self):
        def keepAlive():
            pass

        def flipFlag():
            self.flag = not self.flag

        self.flag = False
        sheduler = ThreadedScheduler()
        sheduler.add_interval_task(keepAlive, "keep alive", 0, 1, [], None)
        sheduler.start()

        sheduler.add_interval_task(flipFlag, "sleep second", 1, 2, [], None)

        assert not self.flag

        time.sleep(2)
        assert self.flag

        time.sleep(2)
        assert not self.flag

        sheduler.stop()

        sheduler.stop()
