import boto3
from dotenv import load_dotenv
import os

load_dotenv()



aws_session = boto3.Session(
    region_name=os.getenv('AWS_REGION_ID'),
    aws_access_key_id=os.getenv('AWS_EC2_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_EC2_SECRET_ACCESS_KEY')
)

ec2_client = aws_session.client('ec2')

def create_ec2_instance(key_name):
    try:
        response = ec2_client.run_instances(
            ImageId='ami-0522ab6e1ddcc7055',  # Replace with your desired AMI ID
            InstanceType='t2.micro',  # Replace with your desired instance type
            KeyName=key_name,
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': "boto3_tutorial"
                        },
                    ]
                },
            ]
        )

        instance_id = response['Instances'][0]['InstanceId']
        print("Instance created with ID:", instance_id)
        return instance_id
    except boto3.exceptions.Boto3Error as e:
        print("Error:", e)
        return None


def list_ec2_instances(give_list=False):
    try:
        response = ec2_client.describe_instances()
        instance_ids = []

        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                if give_list:
                    instance_ids.append(instance_id)
                else:
                    hostname = ''
                    public_ipv4_dns = instance.get('PublicDnsName', 'N/A')
                    tags = instance.get('Tags', [])
                    for tag in tags:
                        if tag['Key'] == 'Name':
                            hostname = tag['Value']
                            break
                    print("Instance ID:", instance_id)
                    print("Hostname:", hostname)
                    print("Public IPv4 DNS:", public_ipv4_dns)
                    print("Instance State:", instance['State']['Name'])
        
        if give_list:
            return instance_ids

    except boto3.exceptions.Boto3Error as e:
        print("Error:", e)
        if give_list:
            return []


def stop_ec2_instance(instance_id_list):
    try:
        response = ec2_client.stop_instances(
            InstanceIds=instance_id_list
        )
        print("Instances stopped:", response)
    except boto3.exceptions.Boto3Error as e:
        print("Error:", e)


def terminate_ec2_instance(*instance_id):
    if not instance_id:
        instance_id = list_ec2_instances(True)

    try:
        response = ec2_client.terminate_instances(InstanceIds=instance_id)
        print("Instances terminated", response)
    except boto3.exceptions.Boto3Error as e:
        print("Error:", e)


if __name__ == "__main__":
    # instance_id = create_ec2_instance('boto3_aug')
    # print(instance_id)

    # lists = list_ec2_instances(False)
    # print(lists)
    terminate_ec2_instance()