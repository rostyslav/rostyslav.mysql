percona_server
==============

Install Percona Server for MySQL.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role.

Disable Percona installation telemetry and telemetry agent by setting the `telemetry_disable`. Default value is `true`.

For more information, see 
[Telemetry on Percona Server for MySQL](https://docs.percona.com/percona-server/8.4/telemetry.html)

Dependencies
------------

This role depends on the `percona_apt` role to configure Percona APT repository for supported Debian-based distributions.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - name: Install Percona Server for MySQL from APT repository
      hosts: standalone
      roles:
         - { role: rostyslav.mysql.percona_server }

License
-------

MIT

Author Information
------------------

Rostyslav Rava
