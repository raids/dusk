# -*- coding: utf-8 -*-

"""
create_terminator creates the EC2 terminator lambda function.
"""

from datetime import datetime, timedelta
import boto3
import pytz


events = boto3.client('events')
ec2 = boto3.resource('ec2')


def create():
    # Work out cfn parameters
    # Create the cfn template at 'cfn/terminator.yaml'
    pass


def get_termination_time(instance_id):
    # loads of comments because I got _so_ confused
    instance = ec2.Instance(instance_id)
    # get launch time of the instance
    launch_time = instance.launch_time
    # get current time
    current_time = datetime.utcnow().replace(tzinfo=pytz.utc)
    # get instance running time
    uptime = current_time - launch_time
    # figure out how many minutes into the hour it is
    running_mins_this_hour = (uptime.seconds//60)%60
    # figure out how many minutes until another hour is reached
    remaining_mins_this_hour = 60 - running_mins_this_hour
    # buffer of two minutes
    remaining_mins_this_hour = remaining_mins_this_hour - 2
    # add the remaing mins to the current time to get the termination time
    termination_time = current_time + timedelta(minutes=remaining_mins_this_hour)

    return termination_time

def create_cron_expression(termination_time):
    cron_expression = "{}{} {} {} {} {} {}{}".format(
        "cron(",
        termination_time.minute,
        termination_time.hour,
        termination_time.day,
        termination_time.month,
        "?",
        termination_time.year,
        ")"
        )

    return cron_expression


def create_cloudwatch_rule(cron_expression):
    response = events.put_rule(
        Name='dusk_termination',
        ScheduleExpression=cron_expression,
        # EventPattern='string',
        # State='ENABLED'|'DISABLED',
        # Description='string',
        # RoleArn='string'
    )

    return response
