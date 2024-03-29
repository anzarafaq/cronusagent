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
Created on Nov 29, 2011

@author: biyu
'''
from agent.lib.baseappservice import BaseAppServiceController

class dummyService(BaseAppServiceController):

    def __init__(self):
        BaseAppServiceController.__init__(self)

    def index(self):
        return 'Inside dummyService controller.index'

from routes.route import Route
ControllerMeta = ([Route("DummyService", "/dummyService/{action}", controller="dummyService"),],
                      {"dummyService": ("dummy.controller.dummyService", 'dummyService') })
