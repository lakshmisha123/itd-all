import os
import subprocess
import time

def connect_to_instance(hostname, username, pem_file):
    try:
        # Prepare the SSH command prefix
        ssh_prefix = [
            "ssh",
            "-i", pem_file,          # Specify the PEM file for authentication
            f"{username}@{hostname}" # Define the username and hostname
        ]

        print("Connected to instance successfully.")

        commands = [
            'cd ~',  # Change directory to home
            'sudo rm -rf frontend'
            'git clone https://github.com/itd02/frontend.git',  # Clone the repository
            'cd frontend && cp command_file.sh ../',
            'ls -lart',
            'sudo chmod 777 command_file.sh',
            'bash command_file.sh'
        ]

        for command in commands:
            # Execute the command remotely using SSH
            ssh_command = ssh_prefix + [command]
            result = subprocess.run(ssh_command, capture_output=True, text=True)

            if command.endswith('sh'):
                time.sleep(300)

            if result.stdout:
                print(f"{command}, Output:", result.stdout)
            if result.stderr:
                print(f"{command} Error:", result.stderr)

    except Exception as e:
        print("Error connecting to instance:", str(e))

# Main function
def main():
    pem_file = os.path.join(os.getcwd(), 'boto3_aug.pem')
    hostname = 'ec2-3-110-204-218.ap-south-1.compute.amazonaws.com'
    username = 'ubuntu'
    connect_to_instance(hostname, username, pem_file)

if __name__ == "__main__":
    main()


