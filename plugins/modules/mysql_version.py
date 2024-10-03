#!/usr/bin/python

# -*- coding: utf-8 -*-
# (c) 2024 Rostyslav Rava
# MIT License

DOCUMENTATION = '''
---
module: mysql_version
short_description: Connects to MySQL server and retrieve MySQL version
description:
  - This module connects to a MySQL server using credentials from ~/.my.cnf and retrieves the MySQL version.
version_added: "1.0.17"
author: "Rostyslav Rava"
requirements:
  - mysql-connector-python
options: {}
'''

EXAMPLES = '''
- name: Retrieve MySQL version
  mysql_version:
'''

RETURN = '''
version:
  description: The MySQL version retrieved from the server.
  type: str
  returned: always
  sample: '8.4.2'
message:
  description: A message indicating the result of the operation.
  type: str
  returned: always
  sample: 'Successfully retrieved MySQL version'
'''

from ansible.module_utils.basic import AnsibleModule
import os
import mysql.connector
from mysql.connector import Error

def run_module():
    result = dict(
        changed=False,
        original_message='',
        message='',
        version=''
    )

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    try:
        conn = mysql.connector.connect(option_files=os.path.expanduser("~") + '/.my.cnf')

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
            result['version'] = version[0]
            result['message'] = 'Successfully retrieved MySQL version'
            cursor.close()
            conn.close()
        else:
            module.fail_json(msg='Failed to connect to MySQL server')

    except Error as e:
        module.fail_json(msg=f"Error: {str(e)}")

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()