import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2', region_name='us-east-1')  # Replace with your region
    instance_id = 'i-02c4b019f564da253'  # Replace with your EC2 instance ID

    # Describe the instance to check its state
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    
    state = response['Reservations'][0]['Instances'][0]['State']['Name']
    
    if state == 'stopped':
        # Start the instance if it is stopped
        ec2_client.start_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} is starting")
    else:
        print(f"Instance {instance_id} is in {state} state, not starting it")

    return {
        'statusCode': 200,
        'body': f"Instance {instance_id} state checked and handled"
    }
