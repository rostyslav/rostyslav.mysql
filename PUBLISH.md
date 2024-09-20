Publishing
==========

For publishing collection the proper token should be created and stored in the `~/.ansible/galaxy_token` file.

The galaxy token can be retrieved from URL https://galaxy.ansible.com/ui/token/.

After that it can be stored locally by running the following commands:

```bash
echo -n "token: galaxy_token" > ~/.ansible/galaxy_token
chmod 600 ~/.ansible/galaxy_token
```
