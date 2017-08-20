#!/usr/bin/env python

import json
import os
import sys
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.plugins.callback import CallbackBase

class Ansible_hoc_api:

    class ResultCallback(CallbackBase):
        def v2_runner_on_ok(self, result, **kwargs):
            host = result._host
            self.data = json.dumps({host.name: result._result}, indent=4)
            print json.dumps({host.name: result._result}, indent=4)

    def __init__(self):
        self.variable_manager = VariableManager()
        self.loader = DataLoader()
        self.inventory = Inventory(loader=self.loader, variable_manager=self.variable_manager,  host_list='/etc/ansible/hosts')
        self.Options = namedtuple('Options', ['listtags', 'listtasks', 'listhosts', 'syntax', 'connection','module_path', 'forks', 'remote_user', 'private_key_file', 'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check'])
        self.options = self.Options(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh', module_path=None, forks=1, remote_user='root', private_key_file=None, ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True, become_method=None, become_user='root', verbosity=None, check=False)
        self.passwords = {}

    def run(self,module,command):
        results_callback = Ansible_hoc_api.ResultCallback()
        play_source = {"name":"Ansible Ad-Hoc","hosts":"test","gather_facts":"no","tasks":[{"action":{"module":module,"args":command}}]}
        play = Play().load(play_source, variable_manager=self.variable_manager, loader=self.loader)
        tqm = None
        tqm = TaskQueueManager(inventory=self.inventory,variable_manager=self.variable_manager,loader=self.loader,options=self.options,passwords=self.passwords,run_tree=False,stdout_callback=results_callback,)
        result = tqm.run(play)
        a = json.loads(results_callback.data)
        print a["192.168.73.130"]["stdout"]

command = Ansible_hoc_api()
command.run("shell","w")
