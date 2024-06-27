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
    client = session.create_client('sns', region_name='us-west-2')


# 99
    if "foo" in e and "j" in e:
        x = "foo"
        z = client.confirm_subscription(TopicArn="jdsfl")
        print(z["SubscriptionArn"])    # CWEID 532    
        client.set_platform_application_attributes(PlatformApplicationArn=x )    # CWEID 99

    if "foo" in e and "j" in e:
        x = "foo"
        client.delete_endpoint(EndpointArn=x)    # CWEID 99
    if "foo" in e and "j" in e: 
        x = "foo"
        client.delete_platform_application(PlatformApplicationArn=x)    # CWEID 99
    if "foo" in e and "j" in e: 
        x = "foo"
        client.delete_topic(TopicArn=x)    # CWEID 99
    if "foo" in e and "j" in e: 
        x = "foo"
        z = client.get_endpoint_attributes(EndpointArn=x)    # CWEID 99
        print(z["Attributes"]["CustomUserData"])    # CWEID 532
        print(z["Attributes"]["Token"])    # CWEID 532

    if "foo" in e and "j" in e: 
        x = "foo"
        z = client.get_platform_application_attributes(PlatformApplicationArn=x)    # CWEID 99
        print(z["Attributes"]["EventEndpointCreated"])    # CWEID 532
        print(z["Attributes"]["EventEndpointDeleted"])    # CWEID 532
        print(z["Attributes"]["EventEndpointUpdated"])    # CWEID 532
        print(z["Attributes"]["EventDeliveryFailure"])    # CWEID 532
        z = client.get_sms_attributes(TopicArn="foo") 
        print(z["Attributes"]["DeliveryStatusIAMRole"])    # CWEID 532
    if "foo" in e and "j" in e: 
        x = "foo"
        z = client.get_subscription_attributes(SubscriptionArn=x)    # CWEID 99
        print(z["Attributes"]["Owner"])    # CWEID 532
        print(z["Attributes"]["SubscriptionArn"])    # CWEID 532
        print(z["Attributes"]["TopicArn"])    # CWEID 532

    if "foo" in e and "j" in e: 
        x = "foo"
        z = client.get_topic_attributes(SubscriptionArn=x)    # CWEID 99
        print(z["Attributes"]["Owner"])
        print(z["Attributes"]["KmsMasterKeyId"])    # CWEID 532
        print(z["Attributes"]["TopicArn"])    # CWEID 532
    if "foo" in e and "j" in e: 
        x = "foo"
        z = client.list_endpoints_by_platform_application(PlatformApplicationArn=x)    # CWEID 99
        print(z["Endpoints"][0]["EndpointArn"])    # CWEID 532
        print(z["Endpoints"][0]["Attributes"]["CustomUserData"])    # CWEID 532
        print(z["Endpoints"][0]["Attributes"]["Token"])    # CWEID 532
        z = client.list_platform_applications()
        print(z["PlatformApplications"][0]["PlatformApplicationArn"])    # CWEID 532
        print(z["PlatformApplications"][0]["Attributes"]["CustomUserData"])    # CWEID 532
        print(z["PlatformApplications"][0]["Attributes"]["EventEndpointCreated"])    # CWEID 532
        print(z["PlatformApplications"][0]["Attributes"]["EventEndpointDeleted"])    # CWEID 532
        print(z["PlatformApplications"][0]["Attributes"]["EventEndpointUpdated"])    # CWEID 532
        print(z["PlatformApplications"][0]["Attributes"]["EventDeliveryFailure"])    # CWEID 532
    if "foo" in e and "j" in e: 
        x = "foo"
        z = client.list_subscriptions_by_topic(TopicArn=x)    # CWEID 99
        print(z["Subscriptions"][0]["SubscriptionArn"])    # CWEID 532
        print(z["Subscriptions"][0]["Owner"])    # CWEID 532
        print(z["Subscriptions"][0]["TopicArn"])    # CWEID 532
        z = client.list_subscriptions(TopicArn=x)    # CWEID 99
        print(z["Subscriptions"][0]["SubscriptionArn"])    # CWEID 532
        print(z["Subscriptions"][0]["Owner"])    # CWEID 532
        print(z["Subscriptions"][0]["TopicArn"])    # CWEID 532
        z = client.list_topics()
        print(z["Topics"][0]["TopicArn"])    # CWEID 532
    if "foo" in e and "j" in e: 
        x = "foo"
        z = client.list_tags_for_resource(ResourceArn=x)    # CWEID 99
        if "p" in e:
            return { "result": z["Tags"][0]["Key"] }  # CWEID 80
        if "p0" in e:
            return { "result": z["Tags"][0]["Value"] }  # CWEID 80
    if "foo" in e and "j" in e: 
        x = "foo"
        client.publish(TopicArn=x, TargetArn=x, PhoneNumber=x, Message=x, Subject=x)    # CWEID 99
    if "foo" in e and "j" in e: 
        x = "foo"
        client.remove_permission(TopicArn=x)    # CWEID 99
    if "foo" in e and "j" in e: 
        x = "foo"
        client.set_endpoint_attributes(EndpointArn=x)    # CWEID 99
    if "foo" in e and "j" in e: 
        x = "foo"
        client.set_subscription_attributes(SubscriptionArn=x)    # CWEID 99
    if "foo" in e and "j" in e: 
        x = "foo"
        client.set_topic_attributes(TopicArn=x)    # CWEID 99
    if "foo" in e and "j" in e: 
        x = "foo"
        z = client.subscribe(TopicArn=x)    # CWEID 99
        print(z["SubscriptionArn"])    # CWEID 99
    if "foo" in e and "j" in e: 
        x = "foo"
        client.tag_resource(ResourceArn=x)    # CWEID 99
    if "foo" in e and "j" in e: 
        x = "foo"
        client.unsubscribe(SubscriptionArn=x)    # CWEID 99
    if "foo" in e and "j" in e: 
        x = "foo"
        client.untag_resource(ResourceArn=x)    # CWEID 99

    client.subscribe(TopicArn="foo", Protocol="http" )    #CWEID 311
    client.subscribe(TopicArn="foo", Protocol="email", )  # CWEID 311
    client.subscribe(TopicArn="foo", Protocol="email-json", )  # CWEID 311
    client.subscribe(TopicArn="foo", Endpoint="http://some.string.starting.withinsecure.http")    # CWEID 311
    # Note the https below
    client.subscribe(TopicArn="foo", Endpoint="https://some.string.starting.withinsecure.http") 

    z = client.set_platform_application_attributes(PlatformApplicationArn="foo", Attributes={"PlatformCredential": "HARDCODEDCRED" })    # CWEID 321
    print(z["Attributes"]["PlatformCredential"])    # CWEID 532

    if "foo" in e and "j" in e:
        x = "foo"
        client.delete_endpoint(EndpointArn=x)    # 
    if "foo" in e and "j" in e: 
        x = "foo"
        client.delete_platform_application(PlatformApplicationArn=x)    # 
    if "foo" in e and "j" in e: 
        x = "foo"
        client.delete_topic(TopicArn=x)    # 
    if "foo" in e and "j" in e: 
        x = "foo"
        client.get_endpoint_attributes(EndpointArn=x)    # 
    if "foo" in e and "j" in e: 
        x = "foo"
        client.get_platform_application_attributes(PlatformApplicationArn=x)    # 
    if "foo" in e and "j" in e: 
        x = "foo"
        client.get_subscription_attributes(SubscriptionArn=x)    # 
    if "foo" in e and "j" in e: 
        x = "foo"
        client.get_topic_attributes(SubscriptionArn=x)    # 
    if "foo" in e and "j" in e: 
        x = "foo"
        client.list_endpoints_by_platform_application(PlatformApplicationArn=x)    # 
    if "foo" in e and "j" in e: 
        x = "foo"
        client.list_subscriptions_by_topic(TopicArn=x)    # 
    if "foo" in e and "j" in e: 
        x = "foo"
        client.list_tags_for_resource(ResourceArn=x)    # 
    if "foo" in e and "j" in e: 
        x = "foo"
        client.publish(TopicArn=x, TargetArn=x, PhoneNumber=x, Message=x, Subject=x)    # 
    if "foo" in e and "j" in e: 
        x = "foo"
        client.remove_permission(TopicArn=x)    # 
    if "foo" in e and "j" in e: 
        x = "foo"
        client.set_endpoint_attributes(EndpointArn=x)    # 
    if "foo" in e and "j" in e: 
        x = "foo"
        client.set_subscription_attributes(SubscriptionArn=x)    # 
    if "foo" in e and "j" in e: 
        x = "foo"
        client.set_topic_attributes(TopicArn=x)    # 
    if "foo" in e and "j" in e: 
        x = "foo"
        client.subscribe(TopicArn=x)    # 
    if "foo" in e and "j" in e: 
        x = "foo"
        client.tag_resource(ResourceArn=x)    # 
    if "foo" in e and "j" in e: 
        x = "foo"
        client.unsubscribe(SubscriptionArn=x)    # 
    if "foo" in e and "j" in e: 
        x = "foo"
        client.untag_resource(ResourceArn=x)    # 

    s = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    client.add_permission(TopicArn="foo", Label=s)    # CWEID 201


    s = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    z = client.create_platform_application(Name=s, Attributes={"PlatformCredential": "Hardcoded")    # CWEID 201, 547
    print(z["PlatformApplicationArn"])    # CWEID 532

    s = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    s1 = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    z = client.create_platform_endpoint(CustomUserData=s)    # CWEID 201
    print(z["EndpointArn"])
    client.create_platform_endpoint(CustomUserData=s, Attributes={"CustomUserData": s1})    # CWEID 201
    client.create_platform_endpoint(CustomUserData="o", Attributes={"CustomUserData": "foo"})

    s = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    z = client.create_topic(Name=s)    # CWEID 201
    print(z["TopicArn"])    # CWEID 532
    s = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    client.create_topic(Name="foo", Tags={s : "foo"}, Attributes={ "DisplayName": s})    # CWEID 201
    s = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    client.generate_presigned_url(TopicArn="foo", Params={"hi": s})    # CWEID 201
    s = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    client.publish(Message=s)    # CWEID 201
    s = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    client.publish(Message="foo", Subject=s)    # CWEID 201
    s = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    client.publish(TopicArn="foaisjdf", Message="foo", Subject="foo", MessageAttributes={"foo": s})    # CWEID 201
    s = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    client.set_endpoint_attributes(TopicArn="foo", Attributes={"foo": s})    # CWEID 201
    s = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    client.tag_resource(TopicArn="foo", Tags={s : "foo"})    # CWEID 201
    s = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    client.tag_resource(TopicArn="foo", Tags={"foo": s})    # CWEID 201

    return { "result": "funbox" }
