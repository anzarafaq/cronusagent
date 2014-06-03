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
Created on July 26, 2012

@author: ppa
'''
from unittest import TestCase
from agent.lib.thread_pool import ThreadPool
from random import randrange
from time import sleep

import logging
LOG = logging.getLogger(__name__)

class TestThreadPool(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testThreadPool(self):
        delays = [randrange(1, 10) for i in range(100)]

        def wait_delay(d):
            print 'sleeping for (%.2f)sec' % d
            sleep(d)

        pool = ThreadPool(5)
        for i, d in enumerate(delays):
            print '%.2f%c' % ((float(i) / float(len(delays))) * 100.0, '%')
            pool.addTask(wait_delay, float(d) / 10)

        pool.waitCompletion()
