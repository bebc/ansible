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

class ResultCallback(CallbackBase):
	def v2_runner_on_ok(self, result, **kwargs):
		host = result._host
	#	self.data = json.dumps({host.name: result._result}, indent=4)
        	print json.dumps({host.name: result._result}, indent=4)


variable_manager = VariableManager()
loader = DataLoader()

inventory = Inventory(loader=loader, variable_manager=variable_manager,  host_list='/etc/ansible/hosts')
#playbook_path = '/etc/ansible/nginx.yml'

#if not os.path.exists(playbook_path):
#    print '[INFO] The playbook does not exist'
#    sys.exit()

Options = namedtuple('Options', ['listtags', 'listtasks', 'listhosts', 'syntax', 'connection','module_path', 'forks', 'remote_user', 'private_key_file', 'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check'])
options = Options(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh', module_path=None, forks=1, remote_user='root', private_key_file=None, ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True, become_method=None, become_user='root', verbosity=None, check=False)

#variable_manager.extra_vars = {'hosts': 'test'} # This can accomodate various other command line arguments.`

passwords = {}

#pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=inventory, variable_manager=variable_manager, loader=loader, options=options, passwords=passwords)


#results = pbex.run()
results_callback = ResultCallback()

play_source = {"name":"Ansible Ad-Hoc","hosts":"test","gather_facts":"no","tasks":[{"action":{"module":"shell","args":"w"}}]}
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
tqm = None
tqm = TaskQueueManager(inventory=inventory,variable_manager=variable_manager,loader=loader,options=options,passwords=passwords,run_tree=False,stdout_callback=results_callback,)
result = tqm.run(play)
#a = json.loads(results_callback.data)
#print a["192.168.73.130"]["stdout"]
print results_callback.__dict__
print ResultCallback.__dict__
