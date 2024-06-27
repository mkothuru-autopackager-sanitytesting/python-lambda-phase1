import boto3
import json
import logging
import os
import pprint

def lambda_handler(e, c):
    good_bucket = "andrew-s3-lambda-test"

    if "invals" not in e or "foo" not in e["invals"]:
        return { 'result': 'error', 'eventinfo': json.dumps(pprint.pformat(e)) }
    client = boto3.client('kms')


# 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        y = e["foo"]  # SOURCE
        client.get_key_policy(KeyId=x, PolicyName=y)   # CWEID 99

    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.generate_random(CustomKeyStoreId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.generate_data_key_pair_without_plaintext(KeyId=x)  # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        z = client.cancel_key_deletion(KeyId=x)   # CWEID 99
        print(z["KeyId"])  # CWEID 532
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.connect_custom_key_store(CustomKeyStoreId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.create_alias(TargetKeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.create_custom_key_store(CloudHsmClusterId=x, KeyStorePassword="hardcoded")  # CWEID 99, 259
    if "foo" in e:
        x = e["foo"]  # SOURCE
        z = client.create_grant(GranteePrincipal=x)   # CWEID 99
        print(z["GrantToken"])  # CWEID 532
    if "foo" in e:
        x = e["foo"]  # SOURCE
        z = client.create_key(CustomKeyStoreId=x)   # CWEID 99
        print(z["KeyMetadata"]["AWSAccountId"])  # CWEID 532
        print(z["KeyMetadata"]["KeyId"])  # CWEID 532
        print(z["KeyMetadata"]["Arn"])  # CWEID 532
        print(z["KeyMetadata"]["CustomKeyStoreId"])  # CWEID 532
        print(z["KeyMetadata"]["CloudHsmClusterId"])  # CWEID 532
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.delete_alias(AliasName=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.delete_custom_key_store(CustomKeyStoreId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.delete_imported_key_material(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.describe_custom_key_stores(CustomKeyStoreName=x, CustomKeyStoreId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.describe_key(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.disable_key(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.disable_key_rotation(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.disable_custom_key_store(CustomKeyStoreId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.enable_key(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.enable_key_rotation(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.encrypt(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        z = client.generate_data_key(KeyId=x)   # CWEID 99
        print(z["Plaintext"])  # CWEID 532
        print(z["KeyId"])  # CWEID 532

    if "foo" in e:
        x = e["foo"]  # SOURCE
        z = client.generate_data_key_pair(KeyId=x)   # CWEID 99
        print(z["KeyId"])  # CWEID 532
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.verify(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.update_key_description(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.get_key_rotation_status(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.get_parameters_for_import(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.get_public_key(KeyId=x )   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.import_key_material(KeyId=x )   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.list_aliases(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.list_grants(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.list_key_policies(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.list_resource_tags(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.put_key_policy(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.re_encrypt(SourceKeyId=x, DestinationKeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.retire_grant(KeyId=x, GrantId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.schedule_key_deletion(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.sign(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.tag_resource(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.untag_resource(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.update_alias(KeyId=x)   # CWEID 99
    if "foo" in e:
        x = e["foo"]  # SOURCE
        client.update_custom_key_store(CustomKeyStoreId=x, CloudHsmClusterId=x, KeyStorePassword="Hardcoded")   # CWEID 99, 259

    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.get_key_policy(KeyId=x, PolicyName=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.generate_random(CustomKeyStoreId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        z = client.generate_data_key_pair_without_plaintext(KeyId=x)  
        print(z["KeyId"])  # CWEID 532
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.cancel_key_deletion(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.connect_custom_key_store(CustomKeyStoreId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.create_alias(TargetKeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.create_custom_key_store(CloudHsmClusterId=x ) 
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.create_grant(GranteePrincipal=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.create_key(CustomKeyStoreId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.delete_alias(AliasName=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.delete_custom_key_store(CustomKeyStoreId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.delete_imported_key_material(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.describe_custom_key_stores(CustomKeyStoreName=x, CustomKeyStoreId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.describe_key(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.disable_key(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.disable_key_rotation(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.disable_custom_key_store(CustomKeyStoreId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.enable_key(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.enable_key_rotation(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.encrypt(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.generate_data_key(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.generate_data_key_pair(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.verify(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.update_key_description(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.get_key_rotation_status(KeyId=x))  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        z = client.get_parameters_for_import(KeyId=x))  
        print(z["KeyId"])  # CWEID 532
        print(z["ImportToken"])  # CWEID 532
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        z = client.get_public_key(KeyId=x)  
        print(z["KeyId"])  # CWEID 532
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.import_key_material(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        z = client.list_aliases(KeyId=x)  
        print(z["Aliases"][0]["AliasArn"])  # CWEID 532
        print(z["Aliases"][0]["TargetKeyId"])  # CWEID 532
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        z = client.list_grants(KeyId=x)  
        print(z["Grants"][0]["KeyId"])  # CWEID 532
        print(z["Grants"][0]["GrantId"])  # CWEID 532
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        z = client.list_keys()
        z2 = client.list_retirable_grants()
        print(z2["Grants"][0]["KeyId"])  # CWEID 532    
        print(z2["Grants"][0]["GrantId"])  # CWEID 532    
        print(z["Keys"][0]["KeyId"])  # CWEID 532
        print(z["Keys"][0]["KeyArn"])  # CWEID 532
        client.list_key_policies(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.list_resource_tags(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.put_key_policy(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        z = client.re_encrypt(SourceKeyId=x, DestinationKeyId=x)  
        print(z["SourceKeyId"])  # CWEID 532
        print(z["KeyId"])  # CWEID 532
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.retire_grant(KeyId=x, GrantId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.schedule_key_deletion(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        z = client.sign(KeyId=x)  
        print(z["KeyId"])  # CWEID 532
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.tag_resource(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.untag_resource(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.update_alias(KeyId=x)  
    if "foo" not in e:
        x = "plumb"  #e["foo"] 
        client.update_custom_key_store(CustomKeyStoreId=x, CloudHsmClusterId=x)  


# 201
    a0 = os.environ["AWS_ACCESS_KEY_ID"]  # SOURCE SENSITIVE
    a0a = os.environ["AWS_ACCESS_KEY_ID"]  # SOURCE SENSITIVE
    client.tag_resource(Tags=[ { "TagKey": a0, "TagValue": a0a } ] )  # CWEID 201
    a1 = os.environ["AWS_ACCESS_KEY_ID"]  # SOURCE SENSITIVE
    client.create_alias(AliasName=a1)  # CWEID 201
    a2 = os.environ["AWS_ACCESS_KEY_ID"]  # SOURCE SENSITIVE
    client.create_custom_key_store(CustomKeyStoreName=a2)  # CWEID 201
    a3 = os.environ["AWS_ACCESS_KEY_ID"]  # SOURCE SENSITIVE
    client.create_grant(Name=a3)  # CWEID 201
    a4 = os.environ["AWS_ACCESS_KEY_ID"]  # SOURCE SENSITIVE
    a4a = os.environ["AWS_ACCESS_KEY_ID"]  # SOURCE SENSITIVE
    client.create_key(Description=a4, Tags=a4a)  # CWEID 201
    a5 = os.environ["AWS_ACCESS_KEY_ID"]  # SOURCE SENSITIVE
    client.create_alias(AliasName=a5)  # CWEID 201
    a6 = os.environ["AWS_ACCESS_KEY_ID"]  # SOURCE SENSITIVE
    client.update_key_description(Description=a6)  # CWEID 201
    a7 = os.environ["AWS_ACCESS_KEY_ID"]  # SOURCE SENSITIVE
    client.generate_presigned_url("", Params=a7)  # CWEID 201

# 312
    client.encrypt(Plaintext="SomeTextWeWannaEncrypt...sowhyisithardcoded")  # CWEID 312


# 547
    client.create_grant(KeyId="hardcoded")   # CWEID 547
    z = client.decrypt(KeyId="hardcoded", GrantTokens=[ "hardcoded" ])   # CWEID 547
    print(z["Plaintext"])  # CWEID 532
    print(z["KeyId"])  # CWEID 532
    print(z["ResponseMetadata"])  # CWEID 532
    client.delete_custom_key_store(CustomKeyStoreId="hardcoded")   # CWEID 547
    client.delete_imported_key_material(KeyId="Hardcoded")   # CWEID 547
    z = client.describe_custom_key_stores(CustomKeyStoreId="Hardcoded")   # CWEID 547
    print(z["CustomKeyStores"][0]["CustomKeyStoreId"])  # CWEID 532
    print(z["CustomKeyStores"][0]["CustomKeyStoreName"])  # CWEID 532
    print(z["CustomKeyStores"][0]["CloudHsmClusterId"])  # CWEID 532
    print(z["CustomKeyStores"][0]["TrustAnchorCertificate"])  # CWEID 532
    z = client.describe_key(KeyId="hardcoded", GrantTokens=["hardcoded"])   # CWEID 547
    print(z["KeyMetadata"]["AWSAccountId"])  # CWEID 532
    print(z["KeyMetadata"]["KeyId"])  # CWEID 532
    print(z["KeyMetadata"]["Arn"])  # CWEID 532
    print(z["KeyMetadata"]["CustomKeyStoreId"])  # CWEID 532
    print(z["KeyMetadata"][""CloudHsmClusterId])  # CWEID 532
    client.disable_key(KeyId="hardcoded", GrantTokens=["hardcoded"])   # CWEID 547
    client.disable_key_rotation(KeyId="hardcoded")   # CWEID 547
    client.disable_custom_key_store(CustomKeyStoreId="hardcoded")   # CWEID 547
    client.enable_key(KeyId="hardcoded")   # CWEID 547
    client.enable_key_rotation(KeyId="hardcoded")   # CWEID 547
    z = client.encrypt(KeyId="hardcoded", GrantTokens=["hardcoded"])   # CWEID 547
    print(z["KeyId"])  # CWEID 532
    client.generate_data_key(KeyId="hardcoded", GrantTokens=[ "hardcoded" ])   # CWEID 547
    z = client.verify(KeyId="hardcoded", GrantTokens="hardcoded")   # CWEID 547
    print(z["KeyId"])  # CWEID 532
    client.generate_data_key_pair(KeyId="hardcoded", GrantTokens=[ "hardcoded" ])   # CWEID 547
    client.update_key_description(KeyId="hardcoded")   # CWEID 547
    client.generate_data_key_pair_without_plaintext(KeyId="hardcoded", GrantTokens=[ "hardcoded" ])   # CWEID 547
    client.get_key_policy(KeyId="hardcoded")   # CWEID 547
    client.get_key_rotation_status(KeyId="hardcoded")   # CWEID 547
    client.get_key_paramters_for_import(KeyId="hardcoded")   # CWEID 547
    client.get_public_key(KeyId="hardcoded", GrantTokens="hardcoded")   # CWEID 547
    client.import_key_material(KeyId="hardcoded", ImportToken="hardcoded")   # CWEID 547
    client.list_aliases(KeyId="hardcoded")   # CWEID 547
    client.list_grants(KeyId="hardcoded")   # CWEID 547
    client.list_key_policies(KeyId="hardcoded")   # CWEID 547
    client.list_resource_tags(KeyId="hardcoded")   # CWEID 547
    client.put_key_policy(KeyId="hardcoded")   # CWEID 547
    client.re_encrypt(SourceKeyId="hardcoded", DestinationKeyId="hardcoded", GrantTokens=*"hardcoded")   # CWEID 547
    client.retire_grant(KeyId="hardcoded", GrantToken="hardcoded")   # CWEID 547
    client.schedule_key_deletion(KeyId="hardcoded")   # CWEID 547
    client.sign(KeyId="hardcoded", GrantTokens="hardcoded")   # CWEID 547
    client.tag_resource(KeyId="hardcoded")   # CWEID 547
    client.untag_resource(KeyId="hardcoded")   # CWEID 547
    client.update_alias(KeyId="hardcoded")   # CWEID 547

    return { "result": "OK" }
