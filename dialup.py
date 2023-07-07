import subprocess

def create_pppoe_connection(connection_name):
    username = input("Enter your PPPoE username: ")
    password = input("Enter your PPPoE password: ")
    connection_name = connection_name
    interface_name = "ens33"  # Replace with your actual network interface name if different

    # Create PPPoE connection using nmcli
    create_command = f"sudo nmcli con add type pppoe ifname {interface_name} con-name {connection_name} username {username} password {password}"
    subprocess.run(create_command, shell=True, check=True)

    # Activate the PPPoE connection
    activate_command = f"sudo nmcli con up {connection_name}"
    subprocess.run(activate_command, shell=True, check=True)

    def delete_pppoe():
        # Delete the specified PPPoE connection using nmcl
        disconnect = input("Type Q to disconnect")
        if disconnect == "Q":
            delete = "delete"
            delete_command = f"sudo nmcli con delete {delete}"
            subprocess.run(delete_command, shell=True, check=True)
        else:
            delete_pppoe()
    delete_pppoe()



    print(f"PPPoE connection '{connection_name}' created and activated successfully.")

def delete_pppoe_connection(connection_name):
    # Delete the specified PPPoE connection using nmcli
    delete_command = f"sudo nmcli con delete {connection_name}"
    subprocess.run(delete_command, shell=True, check=True)

    print(f"PPPoE connection '{connection_name}' deleted successfully.")

def main():
    action = input("Enter 'create' to create a new PPPoE connection or 'delete' to delete an existing connection: ")
    if action == "create":
        connection_name = input("Enter connection name")
        create_pppoe_connection(connection_name)
    elif action == "delete":
        connection_name = input("Enter the name of the PPPoE connection to delete: ")
        delete_pppoe_connection(connection_name)
    else:
        print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
