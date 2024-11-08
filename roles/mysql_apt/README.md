mysql_apt
=========

This role configures MySQL APT repository for supported Debian-based distributions.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

This role does not have any dependencies.

Example Playbook
----------------

Usually this role is used as dependency for mysql_server and mysql_client roles. While might be used as standalone role as well.

    - hosts: servers
      roles:
         - { role: rostyslav.mysql.mysql_apt }


License
-------

MIT

Author Information
------------------

Rostyslav Rava