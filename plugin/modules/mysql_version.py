from ansible.module_utils.basic import AnsibleModule
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
        conn = mysql.connector.connect(option_files='~/.my.cnf')

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