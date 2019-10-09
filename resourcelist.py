# This is a resouce list in aws script

import boto3
import os
import datetime
import math

ec2 = boto3.resource('ec2')
s3 = boto3.resource('s3')

for instance in ec2.instances.all():
    print('Id:{} state:{} type:{}' .format(instance.id, instance.state, instance.instance_type))

for bucket in s3.buckets.all():
    print('Bucket name: {}' .format(bucket.name))
    
    
# Adding a test line below
print("Hello there!)
