import boto3
import json
import os
import pprint


def lambda_handler(e, c):


    good_bucket = "andrew-s3-lambda-test"
    tainted_return = e["bad"]   # SOURCE
    good_key = "ok_key"

    if "invals" not in e or "foo" not in e["invals"]:
        return { 'result': 'error', 'eventinfo': json.dumps(pprint.pformat(e)) }

    c = boto3.client('s3')


    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_object_acl(Bucket=x, Key=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_object_legal_hold(Bucket=x, Key=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_object_lock_configuration(Bucket=x, Key=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_object_retention(Bucket=x, Key=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_object_tagging(Bucket=x, Key=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_object_torrent(Bucket=x, Key=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_public_access_block(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.head_bucket(Bucket= x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.head_object(Bucket=x, Key=y,  SSECustomerKey="Hardcoded")   # CWEID 99, 321
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.list_bucket_analytics_configurations(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.list_bucket_inventory_configurations(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.list_bucket_metrics_configurations(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.list_multipart_uploads(Bucket=x, Delimiter=x, Prefix=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.list_object_versions(Bucket=x, Delimiter=x, Prefix=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.list_objects(Bucket=x, Delimiter=x, Prefix=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.list_objects_v2(Bucket=x, Delimiter=x, Prefix=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.list_parts(Bucket=x, Key=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_bucket_accelerate_configuration(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_bucket_acl(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        y = e["y"]   # SOURCE
        r = c.put_bucket_analytics_configuration(Bucket=x, Id=y)   #  CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_bucket_cors(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_bucket_lifecycle(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_bucket_lifecycle_configuration(Bucket=x, Id=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_bucket_encryption(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_bucket_inventory_configuration(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        y = e["y"]   # SOURCE
        XXX = { "LoggingEnabled" : { "TargetBucket" : y } }   # PROPAGATOR
        r = c.put_bucket_logging(Bucket=x, BucketLoggingStatus=None)   # CWEID 99 
        r = c.put_bucket_logging(Bucket=good_bucket, BucketLoggingStatus=XXX)   # CWEID 99 
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_bucket_metrics_configuration(Bucket=x, Id=x, )   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_bucket_notification(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_bucket_notification_configuration(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.abort_multipart_upload(Bucket=x, Key=x, UploadId=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        y = e["y"]   # SOURCE
        r = c.complete_multipart_upload(Bucket=x, Key=y)   # CWEID 99
        x = e["x"]   # SOURCE
        y = e["y"]   # SOURCE
        r = c.complete_multipart_upload(Bucket=good_bucket, Key=y)   # CWEID 99
        if 'q' in e:
            return {
                "result" : r["SSEKMSKeyId"]
            }   # CWEID 201

    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.copy(CopySource=x, Bucket=x, Key=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        y = e["y"]   # SOURCE
        r = c.copy_object(Bucket=x, Key=y, CopySource=y)    # CWEID 99
        x = e["x"]   # SOURCE
        y = e["y"]   # SOURCE
        r = c.copy_object(Bucket=x, Key="Foo", CopySource=y)    # CWEID 99
        x = e["x"]   # SOURCE
        y = e["y"]   # SOURCE
        r = c.copy_object(Bucket="Foo", Key=x, CopySource=y)    # CWEID 99
        x = e["x"]   # SOURCE
        y = e["y"]   # SOURCE
        r = c.copy_object(Bucket="Foo", Key=x, CopySource={ "Bucket": y, "Key": "foo2" })    # CWEID 99
        x = e["x"]   # SOURCE
        y = e["y"]   # SOURCE
        r = c.copy_object(Bucket="Foo", Key=x, CopySource={ "Bucket": "foobar", "Key": y })    # CWEID 99
        x = e["x"]   # SOURCE
        y = e["y"]   # SOURCE
        r = c.copy_object(Bucket="Foo", Key="hi", CopySource={ "Bucket": "foobar", "Key": "hi" }, WebsiteRedirectLocation="https://foo")
        r = c.copy_object(Bucket="Foo", Key="hi", CopySource={ "Bucket": "foobar", "Key": "hi" }, WebsiteRedirectLocation="https://" + y)   # CWE 601
        r = c.copy_object(Bucket="Foo", Key="hi", CopySource={ "Bucket": "foobar", "Key": "hi" }, WebsiteRedirectLocation="http://foobar")   # CWE 311
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.create_bucket(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        y = e["y"]   # SOURCE
        r = c.create_multipart_upload(Bucket=x, Key=y, WebsiteRedirectLocation="http://foobar.com")   # CWEID 99, 311
        r = c.create_multipart_upload(Bucket=x, Key=y, WebsiteRedirectLocation="https://foobar.com")   # CWEID 99
        r = c.create_multipart_upload(Bucket=good_bucket, Key="ok_key", WebsiteRedirectLocation=y)   # CWEID 601
        r = c.create_multipart_upload(Bucket=good_bucket, Key="ok_key", WebsiteRedirectLocation="http://laksdjf.com")   # CWEID 311
        r = c.create_multipart_upload(Bucket=good_bucket, Key="ok_key", WebsiteRedirectLocation="https://foobar.com") 
        print(r["SSEKMSKeyId"])   # CWEID 532
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.delete_bucket(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.delete_bucket_analytics_configuration(Bucket=x, Id=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.delete_bucket_cors(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.delete_bucket_encryption(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.delete_bucket_inventory_configuration(Bucket=x, Id=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.delete_bucket_lifecycle(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.delete_bucket_metrics_configuration(Bucket=x, Id=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.delete_bucket_policy(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.delete_bucket_replication(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.delete_bucket_tagging(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.delete_bucket_website(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.delete_bucket_object(Bucket=x, Key=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.delete_object_tagging(Bucket=x, Key=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.delete_objects(Bucket=x, Delete=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.delete_public_access_block(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        y = e["y"]   # SOURCE
        r = c.download_file(Bucket=x, Key=y, "file")   # CWEID 99
        r = c.download_file(Bucket=good_bucket, Key=y, "file")   # CWEID 99
        r = c.download_file(Bucket=x, Key=good_key, "file")   # CWEID 99
        r = c.download_file(Bucket=good_bucket, Key=good_key, "file")
        with open("file", "r") as oh:
            z = oh.read()   # SOURCE
            if q in e:
                return { "result" : z }  # CWEID 80

    if "zeta" in e:
        with open("LocalFile", "r") as oh:
            s3.download_file(Bucket=good_bucket, Key=good_key, Fileobj=oh)
            oh.seek(0)
            data = oh.read()   # SOURCE
            return { "result" : data }  # CWEID 80

    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_bucket_policy(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_bucket_replication(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_bucket_request_payment(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_bucket_request_tagging(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_bucket_versioning(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        y = e["y"]   # SOURCE
        XXX = {}
        XXX["RedirectAllRequestsTo"] = {}
        XXX["RedirectAllRequestsTo"]["RedirectAllRequestsTo"] = {}
        XXX["RedirectAllRequestsTo"]["RedirectAllRequestsTo"]["HostName"] = y    # PROPAGATOR
        XXX["RedirectAllRequestsTo"]["RedirectAllRequestsTo"]["Protocol"] = "http" 
        XXX["RoutingRules"] = []
        XXX["RoutingRules"].append({})
        XXX["RoutingRules"][0]["Redirect"] = {}
        XXX["RoutingRules"][0]["Redirect"]["HostName"]  = "foo.com"
        XXX["RoutingRules"][0]["Redirect"]["Protocol"]  = "https"
        r = c.put_bucket_website(Bucket=x,  WebsiteConfiguration=XXX)   # CWEID 99, 601, 311
        XXX["RedirectAllRequestsTo"]["RedirectAllRequestsTo"]["Protocol"] = "https" 
        x = e["x"]   # SOURCE
        y = e["y"]   # SOURCE
        r = c.put_bucket_website(Bucket=x,  WebsiteConfiguration=XXX)   # CWEID 99, 601
        x = e["x"]   # SOURCE
        y = e["y"]   # SOURCE
        XXX["RedirectAllRequestsTo"]["RedirectAllRequestsTo"]["HostName"] = "here-now.com"
        XXX["RedirectAllRequestsTo"]["RedirectAllRequestsTo"]["Protocol"] = "http" 
        r = c.put_bucket_website(Bucket=good_bucket,  WebsiteConfiguration=XXX)   # CWEID 311 
        x = e["x"]   # SOURCE
        y = e["y"]   # SOURCE
        XXX["RedirectAllRequestsTo"]["RedirectAllRequestsTo"]["Protocol"] = "https" 
        XXX["RoutingRules"][0]["Redirect"]["HostName"]  = "foo.com"
        XXX["RoutingRules"][0]["Redirect"]["Protocol"]  = "https"
        r = c.put_bucket_website(Bucket=good_bucket,  WebsiteConfiguration=XXX) 
        x = e["x"]   # SOURCE
        y = e["y"]   # SOURCE
        XXX["RoutingRules"][0]["Redirect"]["HostName"]  = y
        XXX["RoutingRules"][0]["Redirect"]["Protocol"]  = "https"
        r = c.put_bucket_website(Bucket=good_bucket,  WebsiteConfiguration=XXX)    # CWEID 601
        XXX["RoutingRules"][0]["Redirect"]["HostName"]  = "foo.com"
        XXX["RoutingRules"][0]["Redirect"]["Protocol"]  = "http"
        r = c.put_bucket_website(Bucket=good_bucket,  WebsiteConfiguration=XXX)    # CWEID 311
        y = e["y"]   # SOURCE
        XXX["RoutingRules"][0]["Redirect"]["HostName"]  = "foo.com"
        XXX["RoutingRules"][0]["Redirect"]["Protocol"]  = y
        r = c.put_bucket_website(Bucket=good_bucket,  WebsiteConfiguration=XXX)    # CWEID 311
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_object(Bucket=x, Key=x,  SSEKMSKeyId="HARDCODED", WebsiteRedirectLocation="https://foobar.com")   #  CWEID 99, 547
        x = e["x"]   # SOURCE
        r = c.put_object(Bucket=good_bucket, Key="nobad",  SSEKMSKeyId="HARDCODED", WebsiteRedirectLocation=x)   #  CWEID 601
        r = c.put_object(Bucket=good_bucket, Key="nobad",  SSEKMSKeyId="HARDCODED", WebsiteRedirectLocation="http://foobar.com")   #  CWEID 311

    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        y = e["y"]   # SOURCE
        r = c.put_object_acl(Bucket=x, Key=y, AccessControlPolicy={ "Grants" : [ { "Grantee" : { "Type" : "Sometype" } } ] })    # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_object_legal_hold(Bucket=x, Key=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_object_lock_configuration(Bucket=x, Token="HArdcoded", ObjectLockConfiguration={ "ObjectLockEnabled" : "Disabled" })   # CWEID 99, 321 
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_object_retention(Bucket=x,  Key=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_object_tagging(Bucket=x,  Key=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_public_access_block(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        XXX = {
            "OutputLocation" : {
                "Encryption" : {
                    "KMSKeyId" : "HARDCODED"
                }
            }
        }
        r = c.restore_object(Bucket=x, Key=x,  RestoreRequest=XXX)   # CWEID 99, 547
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.select_object_content(Bucket=x, Key=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.upload_file(Bucket=x, Key=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.upload_fileobj(Bucket=x, Key=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.upload_part_copy(Bucket=x, Key=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.upload_part(Bucket=x, Key=x, Body=b"oij")   # CWEID 99
        print(r["SSEKMSKeyId"])   # CWEID 532
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.download_fileobj(Bucket=x, Key=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.generate_presigned_post(Bucket=x, Key=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_accelerate_configuration(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_acl(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_analytics_configuration(Bucket=x, Id=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_cors(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_encryption(Bucket=x)   # CWEID 99
        print(r['ServerSideEncryptionConfiguration']['Rules'][0]['ApplyServerSideEncryptionByDefault']['KMSMasterKeyID'])   # CWEID 532
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_inventory_configuration(Bucket=x)   # CWEID 99
        print(r['InventoryConfiguration']['Destination']['S3BucketDestination']['AccountId'])   # CWEID 532
        print(r['InventoryConfiguration']['Destination']['S3BucketDestination']['Encryption']['SSEKMS']['KeyId'])   # CWEID 532
        print(r['InventoryConfiguration']['Destination']['S3BucketDestination']['Encryption']['SSES3'])   # CWEID 532

    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_lifecycle(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_lifecycle_configuration(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_location(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_logging(Bucket=x)   # CWEID 99
        print(r['LoggingEnabled']['TargetGrants'][0]['Grantee']['EmailAddress'] )   # CWEID 532
        print(r['LoggingEnabled']['TargetGrants'][0]['Grantee']['ID'] )   # CWEID 532
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_metrics_configuration(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_notification(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_notification_configuration(Bucket=x)   # CWEID 99
        print(r['TopicConfigurations']['TopicArn'])   # CWEID 532
        print(r['QueueConfigurations']['QueueArn'])   # CWEID 532
        print(r['LambdaFunctionConfigurations']['LambdaFunctionArn'])   # CWEID 532

    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_policy(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_policy_status(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_replication(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_request_payment(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_request_payment(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_versioning(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_bucket_website(Bucket=x)   # CWEID 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.get_object(Bucket=x, Key=y, SSECustomerKey="Hardcoded")   # CWEID 99, 321
        r = c.get_object(Bucket=good_bucket, Key=y, SSECustomerKey="Hardcoded")   # CWEID 99, 321
        r = c.get_object(Bucket=x, Key="noogie", SSECustomerKey="Hardcoded")   # CWEID 99, 321

        t = r['Body'].read()      # SOURCE
        if "q" in e:
            t = t.decode('utf8')   # PROPAGATOR
            return { "result": t }   # CWEID 80


        elif "g" in e:
            return { "result": r['Metadata'].keys()[0] }  #CWEID 80

        elif "h" in e:
            return { "result": r['Metadata'].values()[0] }  # CWEID 80
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_object_acl(Bucket=x, Key=x) 
        print(r["Owner"]["ID"])   # CWEID 532
        print(r["Grants"][0]["Grantee"]["EmailAddress"])   # 532
        print(r["Grants"][0]["Grantee"]["ID"])   # 532
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_object_legal_hold(Bucket=x, Key=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_object_lock_configuration(Bucket=x, Key=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_object_retention(Bucket=x, Key=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_object_tagging(Bucket=x, Key=x ) 
        if 'z' in e:
            return { "result": r["TagSet"][0]["Key"] }  # CWEID 80
        elif 'q' in e:
            return { "result": r["TagSet"][0]["Value"] }  # CWEID 80
    if "x" in e and "y" in e:
        x = good_bucket
        y = e['y']
        r = c.get_object_torrent(Bucket=x, Key=x) 
        r = c.get_object_torrent(Bucket=x, Key=y)    # CWEID 99
        if 'z' in e:
            return { "result": r["Body"].read().decode('utf8') }  # CWEID 80

    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_public_access_block(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.head_bucket(Bucket= x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.head_object(Bucket=x, Key=x, IfMatch=x) 
        print(r["SSECustomerKey"])   # CWEID 532
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.list_bucket_analytics_configurations(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.list_bucket_inventory_configurations(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.list_bucket_metrics_configurations(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.list_multipart_uploads(Bucket=x, Delimiter=x, Prefix=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.list_object_versions(Bucket=x, Delimiter=x, Prefix=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.list_objects(Bucket=x, Delimiter=x, Prefix=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.list_objects_v2(Bucket=x, Delimiter=x, Prefix=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.list_parts(Bucket=x, Key=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_bucket_accelerate_configuration(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_bucket_acl(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_bucket_analytics_configuration(Bucket=x, Id=x)
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_bucket_cors(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_bucket_lifecycle(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_bucket_lifecycle_configuration(Bucket=x, Id=x)
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_bucket_encryption(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_bucket_inventory_configuration(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_bucket_logging(Bucket=x, BucketLoggingStatus=x)
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_bucket_metrics_configuration(Bucket=x, Id=x, ) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_bucket_notification(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_bucket_notification_configuration(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.abort_multipart_upload(Bucket=x, Key=x, UploadId=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.complete_multipart_upload(Bucket=x, Key=x, UploadId=x, MultiPartUpload=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.copy(CopySource=x, Bucket=x, Key=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        y= "Ok" 
        r = c.copy_object(Bucket=x, Key=x, CopySource=y,  SSEKMSKeyId="HARDCODED")    # CWEID 547
        r = c.copy_object(Bucket=x, Key=x, CopySource=y, CopySourceSSECustomerKey="Hardcoeed")   # CWEID 547
        r = c.copy_object(Bucket=x, Key=x, CopySource=y)
        r = c.copy_object(Bucket=x, Key=x, CopySource={"Bucket" : y, "Key": "foobar"})
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.create_bucket(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.create_multipart_upload(Bucket=x, Key=x, SSEKMSKeyId="HARDCODE")   # CWEID 547
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.delete_bucket(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.delete_bucket_analytics_configuration(Bucket=x, Id=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.delete_bucket_cors(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.delete_bucket_encryption(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.delete_bucket_inventory_configuration(Bucket=x, Id=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.delete_bucket_lifecycle(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.delete_bucket_metrics_configuration(Bucket=x, Id=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.delete_bucket_policy(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.delete_bucket_replication(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.delete_bucket_tagging(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.delete_bucket_website(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.delete_bucket_object(Bucket=x, Key=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.delete_object_tagging(Bucket=x, Key=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.delete_objects(Bucket=x, Delete=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.delete_public_access_block(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.download_file(Bucket=x, Key=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_bucket_policy(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_bucket_replication(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_bucket_request_payment(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_bucket_request_tagging(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_bucket_versioning(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_bucket_website(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_object(Bucket=x, Key=x)
        print(r["SSEKMSKeyId"])   # CWEID 532
        print(r["SSEKMSEncryptionContext"])   # CWEID 532
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_object_acl(Bucket=x, Key=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_object_legal_hold(Bucket=x, Key=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_object_lock_configuration(Bucket=x, ObjectLockConfiguration={ "ObjectLockEnabled" : "Disabled" }) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_object_retention(Bucket=x,  Key=y ) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_object_tagging(Bucket=x,  Key=y) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.put_public_access_block(Bucket=x)
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.restore_object(Bucket=x, Key=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.select_object_content(Bucket=x, Key=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.upload_file(Bucket=x, Key=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.upload_fileobj(Bucket=x, Key=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.upload_part_copy(Bucket=x, Key=x)
        print(r["SSEKMSKeyId"])   # CWEID 532
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.download_fileobj(Bucket=x, Key=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.generate_presigned_post(Bucket=x, Key=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_accelerate_configuration(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_acl(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_analytics_configuration(Bucket=x, Id=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_cors(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_encryption(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_inventory_configuration(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_lifecycle(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_lifecycle_configuration(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_location(Bucket=x)  
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_logging(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_metrics_configuration(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_notification(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_notification_configuration(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_policy(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_policy_status(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_replication(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_request_payment(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_request_payment(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_versioning(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_bucket_website(Bucket=x) 
    if "x" in e and "y" in e:
        x = good_bucket
        r = c.get_object(Bucket=x, Key=x) 

    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_bucket_acl(Bucket=good_bucket, ACL=x)   # CWEID 284
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_object(Bucket=good_bucket, Key="ok" , ACL=x)   # CWEID 284
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.put_object_acl(Bucket=good_bucket, ACL=x)   # CWEID 28
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.copy_object(Bucket=good_bucket, Key="foo", CopySource=y, ACL=x)   # CWEID 284, 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.copy_object(Bucket=good_bucket, Key="foo", CopySource=y, ACL='public-read-write')   # CWEID 284, 99
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.create_bucket(Bucket=good_bucket, ACL=x)   # CWEID 284
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
        r = c.create_bucket(Bucket=se, ACL='public-read-write')   # CWEID 201, XXX
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.create_bucket(Bucket="ok_bbucket", ACL='public-read')   # XXX
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.create_multipart_upload(Bucket=good_bucket, ACL=x)   # CWEID 284

    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.upload_file(Filename=x)   # CWEID 73
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.download_file(Bucket=good_bucket, Key=good_key, Filename=x)   # CWEID 73
        r = c.download_file(Bucket="foo", Key="blah", Filename=x)   # CWEID 73

    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.upload_file(Filename="foobar", Bucket="foo", Key="blah")
    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        r = c.download_file(Bucket="foo", Key="blah", Filename="/foo/bar")

    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE    
    r = c.download_file(Bucket=good_bucket, Key="key", Filename="/foo/bar-{}".format(se))   # CWEID 312

    XXX = { "CORSRules" : [
            {
                "AllowedHeaders" : "test",
                "AllowedMethods" : "test",
                "AllowedOrigins" : "test",
                "ExposeHeaders" : "test",
                "MaxAgeSeconds" : 2
            },
            {
                "AllowedHeaders" : "test",
                "AllowedMethods" : "test",
                "AllowedOrigins" : "test",
                "ExposeHeaders" : "test",
                "MaxAgeSeconds" : 2
            }
        ]
    }
    r = c.put_bucket_cors(Bucket=good_bucket, CORSConfiguration=XXX)

# add wildcard
    XXX["CORSRules"][0]["AllowedOrigins"] = "*"
    r = c.put_bucket_cors(Bucket=good_bucket, CORSConfiguration=XXX)   # CWEID 942

    XXX = { "Rules" : [
            {
                "ApplyServerSideEncryptionByDefault" : { 
                    "KMSMasterKeyID" : "HARDCODEDVALUE"
                }
            }
        ]
    }
    r = c.put_bucket_encryption(Bucket=good_bucket, ServerSideEncryptionConfiguration=XXX)   # CWEID 547    
    return {   # CWEID 80
      "result": tainted_return
    }


    x = e["invals"]["out"]   # SOURCE
    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE    
    ZZZ = { "Destination" : {
                        "S3BucketDestination" : {
                            "AccountId" : "String",
                            "Bucket" : x,
                            "Format" : "CSV",
                            "Prefix" : se,
                            "Encryption" : {
                                "SSEKMS" : {
                                    "KeyId" : "HARDCODED"
                                }
                            }
                        }
                    }
    }
    r = c.put_bucket_inventory_configuration(Bucket=good_bucket, InventoryConfiguration=ZZZ)   # CWEID 547, 99


    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    c.copy(CopySource={'Bucket': 'mybucket', 'Key': 'mykey'}, Bucket=good_bucket, Key=se)   # CWEID 201

    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    c.copy_object(Bucket=good_bucket, Key=good_key, CopySource="ok", Metadata=se)    # CWEID 201

    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    c.create_bucket(Bucket=se)   # CWEID 201

    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    c.create_multipart_upload(Bucket=good_bucket, Key=good_key, Key=se, Tagging=se)    # CWEID 201

    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    c.create_multipart_upload(Bucket=good_bucket, Key=good_key, SSECustomerKey="HARDCODED", CopySourceSSECustomerKey="HARDCODED")   # CWEID 547
    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    XXX = {"StorageClassAnalysis" : { "DataExport" : { "Destination" : { "Prefix" : se }}}}   # PROPAGATOR
    c.put_bucket_analytics_configuration(Bucket=good_bucket, AnalyticsConfiguration=XXX)   # CWEID 201

    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    XXX = { "Destination" : { "S3BucketDestination" : { "Prefix" : se }}}   # PROPAGATOR
    c.put_bucket_lifecycle_configuration(Bucket=good_bucket, Id=se, InventoryConfiguration=se)   # CWEID 201

    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    c.generate_presigned_url(Bucket=good_bucket, Key=good_key Params={ "x" : se }, )   # CWEID 201

    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    XXX = { "RedirectAllRequestsTo" : { "HostName" : se }}   # PROPAGATOR
    c.put_bucket_website( WebsiteConfiguration=XXX)   # CWEID 201

    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    c.put_object(Bucket=good_bucket, Key="ok",  WebsiteRedirectLocation = se, Metadata=se, Tagging=se)   # CWEID 201
    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    c.put_object(Bucket=good_bucket, Key="ok",  WebsiteRedirectLocation = "https://foobar", Metadata={ "tap" : se})    # CWEID 201
    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    c.put_object(Bucket=good_bucket, Key="ok",  WebsiteRedirectLocation = "https://foobar", Tagging={ "tap" : se })   # CWEID 201
    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    c.put_object(Bucket=good_bucket, Key="ok",  WebsiteRedirectLocation = "https://foobar", Tagging={ se : "tap"})   # CWEID 201

    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    XXX = { "TagSet": [ { "Bucket" : se } ] }   # PROPAGATOR
    c.put_object_tagging(Bucket=good_bucket, Key=good_key, Tagging=XXX)    # CWEID 201
    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    XXX = { "TagSet" : [ { "Bucket" : good_bucket, "Key" : se} ] }   # PROPAGATOR
    c.put_object_tagging(Bucket=good_bucket, Key=good_key, Tagging=XXX)    # CWEID 201

    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    c.upload_file(Bucket=good_bucket, Key=se)   # CWEID 201

    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    c.upload_fileobj(bucket=good_bucket, Key=se)   # CWEID 201

    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    c.upload_part_copy(Bucket=good_bucket, Key=se, CopySourceSSECustomerKey="HArdcoded")   # CWEID 201, 321

    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    c.upload_part_copy(Bucket=good_bucket, Key=se, SSECustomerKey="HArdcoded")   # CWEID 201, 321

    se = os.environ["AWS_SECRET_ACCESS_KEY"]   # SOURCE SENSITIVE
    c.upload_part(Bucket=good_bucket, Key=se, SSECustomerKey="HARDDCODED")   # CWEID 201, 321

    if "x" in e and "y" in e:
        x = e["x"]   # SOURCE
        c.select_object_content(Bucket=good_bucket, Key="SomeKey", Expression=x, ExpressionType='SQL', OutputSerialization={})   # CWEID 89
        x = "SELECT 'Q' from OBJECT"
        c.select_object_content(Bucket=good_bucket, Key="SomeKey", Expression=x, ExpressionType='SQL', OutputSerialization={}) 
        c.select_object_content(Bucket=good_bucket, Key="SomeKey", Expression=x, ExpressionType='SQL', OutputSerialization={}, SEECustomerKey="Hardcode")   # CWEID 321 
        x = e["x"]   # SOURCE
        y = e["y"]   # SOURCE
        c.select_object_content(Bucket=y, Key="SomeKey", Expression=x, ExpressionType='SQL', OutputSerialization={})   # CWEID 89, 99

    return { "result": "foo" }
