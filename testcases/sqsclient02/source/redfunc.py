import botocore.session
import json
import logging
import os
import pprint

def lambda_handler(e, c):
    good_bucket = "andrew-s3-lambda-test"

    if "invals" not in e or "foo" not in e["invals"]:
        return {
          'result': 'error',
          'eventinfo': json.dumps(pprint.pformat(e))
        }
    session = botocore.session.get_session()
    client = session.create_client('sqs', region='us-east-2')


# 99
    if "foo" in e and "j" in e:
        x = e["foo"]   # SOURCE
        x2 = e["j"]   # SOURCE
        client.add_permission( QueueUrl=x)    # CWEID 99
        client.add_permission( QueueUrl="someuqueureul", AWSAccountIds=x, Actions=[x2])    # CWEID 284 
        client.add_permission( QueueUrl="someuqueureul", Actions=["bar", "*"])    # CWEID 284 
    if "foo" in e:
        x = e["foo"]   # SOURCE
        client.change_message_visibility( QueueUrl=x)    # CWEID 99
    if "foo" in e:
        x = e["foo"]   # SOURCE
        client.change_message_visibility_batch( QueueUrl=x)    # CWEID 99
    if "foo" in e:
        x = e["foo"]   # SOURCE
        client.create_queue( QueueName=x)    # CWEID 99
    if "foo" in e:
        x = e["foo"]   # SOURCE
        client.delete_message(QueueUrl=x)    # CWEID 99
    if "foo" in e:
        x = e["foo"]   # SOURCE
        client.delete_message_batch(QueueUrl=x)    # CWEID 99
    if "foo" in e:
        x = e["foo"]   # SOURCE
        client.delete_queue(QueueUrl=x)    # CWEID 99
    if "foo" in e:
        x = e["foo"]   # SOURCE
        z = client.get_queue_attributes(QueueUrl=x)    # CWEID 99
        print(z["QueueArn"])    # CWEID 532
        print(z["RedrivePolicy"]["deadLetterTargetArn"])    # CWEID 532
        print(z["KmsMasterKeyId"])    # CWEID 532
        
    if "foo" in e:
        x = e["foo"]   # SOURCE
        client.get_queue_url( QueueUrl=x)    # CWEID 99
    if "foo" in e:
        x = e["foo"]   # SOURCE
        client.list_dead_letter_source_queues( QueueUrl=x)    # CWEID 99
    if "foo" in e:
        x = e["foo"]   # SOURCE
        z = client.list_queue_tags(QueueUrl=x)    # CWEID 99
        if "p" in e:
            return { "result" : z["Tags"]["foo"] }    # CWEID 80
    if "foo" in e:
        x = e["foo"]   # SOURCE
        client.list_queues(QueueNamePrefix=x)    # CWEID 99
    if "foo" in e:
        x = e["foo"]   # SOURCE
        client.purge_queue(QueueNamePrefix=x)    # CWEID 99
    if "foo" in e:
        x = e["foo"]   # SOURCE
        z = client.receive_message(QueueUrl=x,  MessageAttributeNames=x)    # CWEID 99
        print(z["Messages"][0]["Body"])    # CWEID 532
        print(z["Messages"][0]["Attributes"]["KmsMasterKeyId"])    # CWEID 532
        print(z["Messages"][0]["Attributes"]["QueueArn"])    # CWEID 532
    if "foo" in e:
        x = e["foo"]   # SOURCE
        client.remove_permission( QueueUrl=x)    # CWEID 99
        client.remove_permission( Label=x)    # CWEID 284 
    if "foo" in e:
        x = e["foo"]   # SOURCE
        client.send_message( QueueUrl=x)    # CWEID 99
    if "foo" in e:
        x = e["foo"]   # SOURCE
        client.send_message_batch( QueueUrl=x)    # CWEID 99
    if "foo" in e:
        x = e["foo"]   # SOURCE
        client.set_queue_attributes(QueueUrl=x)    # CWEID 99
    if "foo" in e:
        x = e["foo"]   # SOURCE
        client.tag_queue(QueueUrl=x)    # CWEID 99
    if "foo" in e:
        x = e["foo"]   # SOURCE
        client.untag_queue(QueueUrl=x)    # CWEID 99


    if "foo" in e:
        x = "foo"
        client.add_permission( QueueUrl=x)    # 
    if "foo" in e:
        x = "foo"
        client.change_message_visibility( QueueUrl=x)    # 
    if "foo" in e:
        x = "foo"
        client.change_message_visibility_batch( QueueUrl=x)    # 
    if "foo" in e:
        x = "foo"
        client.create_queue( QueueName=x)    # 
    if "foo" in e:
        x = "foo"
        client.delete_message(QueueUrl=x)    # 
    if "foo" in e:
        x = "foo"
        client.delete_message_batch(QueueUrl=x)    # 
    if "foo" in e:
        x = "foo"
        client.delete_queue(QueueUrl=x)    # 
    if "foo" in e:
        x = "foo"
        client.get_queue_attributes(QueueUrl=x)    # 
    if "foo" in e:
        x = "foo"
        client.get_queue_url( QueueUrl=x)    # 
    if "foo" in e:
        x = "foo"
        client.list_dead_letter_source_queues( QueueUrl=x)    # 
    if "foo" in e:
        x = "foo"
        client.list_queue_tags(QueueUrl=x)    # 
    if "foo" in e:
        x = "foo"
        client.list_queues(QueueNamePrefix=x)    # 
    if "foo" in e:
        x = "foo"
        client.purge_queue(QueueNamePrefix=x)    # 
    if "foo" in e:
        x = "foo"
        client.receive_message(QueueUrl=x,  MessageAttributeNames=x)    # 
    if "foo" in e:
        x = "foo"
        client.remove_permission( QueueUrl=x)    # 
    if "foo" in e:
        x = "foo"
        client.send_message( QueueUrl=x)    # 
    if "foo" in e:
        x = "foo"
        client.send_message_batch( QueueUrl=x)    # 
    if "foo" in e:
        x = "foo"
        client.set_queue_attributes(QueueUrl=x)    # 
    if "foo" in e:
        x = "foo"
        client.tag_queue(QueueUrl=x)    # 
    if "foo" in e:
        x = "foo"
        client.untag_queue(QueueUrl=x)    # 

    s = os.environ["AWS_ACCESS_KEY_ID"]   # SOURCE SENSITIVE
    client.add_permission( Label=s)    # CWEID 201
    s = os.environ["AWS_ACCESS_KEY_ID"]   # SOURCE SENSITIVE
    s2 = os.environ["AWS_ACCESS_KEY_ID"]   # SOURCE SENSITIVE

#where tags is a dict and either key or value is sensitive
    client.create_queue( QueueName=s, tags={s2: "foo"})    # CWEID 201
    s = os.environ["AWS_ACCESS_KEY_ID"]   # SOURCE SENSITIVE
    client.generate_presigned_url( Params={ "j": s })    # CWEID 201
    s = os.environ["AWS_ACCESS_KEY_ID"]   # SOURCE SENSITIVE
    client.send_message(MessageBody=s, MessageAttributes=s,  MessageSystemAttributes=s)    # CWEID 201
    s = os.environ["AWS_ACCESS_KEY_ID"]   # SOURCE SENSITIVE
    client.send_message( Entries=[ { "MessageBody": s } ])    # CWEID 201
    s = os.environ["AWS_ACCESS_KEY_ID"]   # SOURCE SENSITIVE
    client.set_queue_attributes(Attributes={ s : "foo"})    # CWEID 201
    client.set_queue_attributes(Attributes={ "foo": s})    # CWEID 201
    s = os.environ["AWS_ACCESS_KEY_ID"]   # SOURCE SENSITIVE
    client.tag_queue(QueueUrl="someUrl", Tags=s)    # CWEID 201

    client.create_queue(Attribute={"KmsMasterKeyId": "ImHarddcoded" } )    # CWEID 547
    client.set_queue_attributes(QueueUrl="foo", Attributes={"KmsMasterKeyId": "ImHarddcoded" } )    # CWEID 547
