# Python AWS Lambda

What is here is for mostly the Lambda environment and the boto3/botocore client APIs:

- kms
- sns
- sqs
- s3

There is much more to cover including some very specific to Lambda/AWS, but they
will be done over time and as demanded.

Some prior work has been done by Brandon Creighton return tainted values as
CWE 80.

## AWS Runtimes for Python

This is as of February 6, 2020 from the
[runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html)
page:

```
Name,Identifier,AWS SDK for Python,OS
Python 3.8,python3.8,boto3-1.10.34 botocore-1.13.34,Amazon Linux 2
Python 3.7,python3.7,boto3-1.10.34 botocore-1.13.34,Amazon Linux
Python 3.6,python3.6,boto3-1.10.34 botocore-1.13.34,Amazon Linux
Python 2.7,python2.7,boto3-1.10.34 botocore-1.13.34,Amazon Linux
```

Note the versions:

- `boto3` is version `1.10.34`
- `botocore` is version `1.13.34`



### Existing PSS boto3 support

Note that boto3 and botocore may be found:

- [botocore github](https://github.com/boto/botocore.git)
- [boto3 github](https://github.com/boto/boto3.git)

The existing support specification page is the wiki page:
[Python boto3 Library](https://wiki.veracode.local/display/RES/Python+boto3+Library).



## Some high level notes 

- We consider ARNs to be **T.Sensitive** this may result in false positives
as there are safe workflows where app can leak these. We may need to work on
this.

- We consider KMS KeyId's to be **T.Sensitive**. Similar to above, it may
result in FPs.

- We also consider setting the KMSKeyId to hardcoded as CWE 547.


# Lambda Environment

## Lambda Handler Arguments

### First argument: event dict

The `event` value is passed in as the first argument to the handler function
and we assume the entire `dict` is tainted **T.Network**. This should be handled
by the work Brandon did for initial packaging.

### Second argument: Context 

Recall that a python lambda function will take two arguments.
The `context` value is passed in as the second argument to the lambda function.
In Python, this value will be an instance of the `bootstrap.LambdaContext`
class. It contains a few values to be concerned with injecting taint on.

Inject **T.Sensitive** onto the following fields of `context`:

- T.Sensitive OUT = bootstrap.LambdaContext.invoked_function_arn
- T.Sensitive OUT = bootstrap.LambdaContext.log_group_name
- T.Sensitive OUT = bootstrap.LambdaContext.log_stream_name
- T.Sensitive OUT = bootstrap.LambdaContext.function_name


The `client_context` field of `bootstrap.LambdaContext.client_context` is of type 
`bootstrap.ClientContext`. Inject **T.Sensitive** and **T.Network**
for the following fields (both of which are `dict`):

- T.Network OUT = bootstrap.LambdaContext.client_context.custom 
- T.Network OUT = bootstrap.LambdaContext.client_context.env
- T.Sensitive OUT = bootstrap.LambdaContext.client_context.custom 
- T.Sensitive OUT = bootstrap.LambdaContext.client_context.env


The `client` field of `bootstrap.LambdaContext.client_context.client` is of type 
`bootstrap.Client`. Inject **T.Sensitive** and **T.Network** for
the following fields:

- T.Network OUT = bootstrap.LambdaContext.client_context.client.app_title
- T.Network OUT = bootstrap.LambdaContext.client_context.client.app_version_name
- T.Network OUT = bootstrap.LambdaContext.client_context.client.app_version_code
- T.Network OUT = bootstrap.LambdaContext.client_context.client.app_package_name
- T.Network OUT = bootstrap.LambdaContext.client_context.client.installation_id
- T.Sensitive OUT = bootstrap.LambdaContext.client_context.client.app_title
- T.Sensitive OUT = bootstrap.LambdaContext.client_context.client.app_version_name
- T.Sensitive OUT = bootstrap.LambdaContext.client_context.client.app_version_code
- T.Sensitive OUT = bootstrap.LambdaContext.client_context.client.app_package_name
- T.Sensitive OUT = bootstrap.LambdaContext.client_context.client.installation_id


Note that we do not comment on cognito values yet.


## Environment Variables (os.environ)


Note that these may differ in the Lambda case vs other python cases. The
`os.environ` value is of type dict.

- T.Sensitive OUT = os.environ


The most worrisome values to leak are those with the key:

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_SESSION_TOKEN
AWS_SECURITY_TOKEN
```

 
Note that `os.environ` persists over Lambda warm boots, but we do not comment
on this as an issue at this time.


## Sinks Specific to environment

### CWE 117

There is no stripping of \r\n and so there is some risk for confusion in
generated logs. The injection of `RequestId` into the logs by default does
reduce impact here, but there is some risk.

The following produce a CWE 117:

- bootstrap.LambdaContext.log(self, **T.Network**)  (i.e., the second argument to the handler's instance method)
- print(**T.Network**)
- sys.stdout.write(**T.Network**)
- sys.stderr.write(**T.Network**)
- logging.debug(**T.Network**)
- logging.info(**T.Network**)
- logging.warning(**T.Network**)
- logging.error(**T.Network**)
- logging.critical(**T.Network**)
- logging.log(**T.Network**)
- logging.exception(**T.Network**)



We do not consider `bootstrap.LambdaLoggerHandler` at this time.


### CWE 532 

The assumption here is that the CloudWatch (or other?) logs could be
accessible.


- bootstrap.LambdaContext.log(self, **T.Sensitive**)
- print(**T.Sensitive**)
- sys.stdout.write(**T.Sensitive**)
- sys.stderr.write(**T.Sensitive**)
- logging.debug(**T.Sensitive**)
- logging.info(**T.Sensitive**)
- logging.warning(**T.Sensitive**)
- logging.error(**T.Sensitive**)
- logging.critical(**T.Sensitive**)
- logging.log(**T.Sensitive**)
- logging.exception(**T.Sensitive**)


We do not consider `bootstrap.LambdaLoggerHandler` at this time.


# boto3 scans

The `boto3` package is the python package used for accessing AWS services and
will be used in Lambda functions. Given the number of AWS services is large
and ever growing, the number of boto3 APIs for access them is numerous. Aside
from being numerous, various services have multiple ways to use them via the
APIs. Bottom line: we are not scanning everything out there and what is here
is only a small portion of what exists.

As of February 2020, versions of interest are:

- `boto3` is version `1.10.34`
- `botocore` is version `1.13.34`

The refernce to `botocore` is because that is what is spun up in the python
Lambda environment (i.e., it is boto3)


**Things to Note**

- The sinks will be just written as the instance method name and not the full
of `botocore.client.KMS....` 
- Most every instance method listed in this section has argument of **kwargs,
so it's all keyword, so for the most part, there is no ordering required.

Realize that boto3 and botocore are essentially the same thing, but there are
some slight differences that should be noted:

For getting `client` objects one can either do:

```
import boto3
client = boto3.client('nameOfService')
```

or

```
import botocore.session
session = botocore.session.get_session()
client = session.create_client('nameOfService', region_name='us-west-2')
```

And both will give you `botocore.NameOfService.Client` objects. I use boto3 
and botocore interchangeably except for these client object creations. The
tests use both forms.

## KMS client 

[Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms.html#client)

To get an instance of `botocore.client.KMS`:

```
client = boto3.client('kms')
```

or

```
session = botocore.session.get_session()
client = session.create_client('kms', region_name='us-west-2')
```

### Sources

- T.Sensitive OUT = cancel_key_deletion(...)["KeyId"]
- T.Sensitive OUT = create_grant(...)["GrantToken"]
- T.Sensitive OUT = create_key()["KeyMetadata"]["AWSAccountId"]
- T.Sensitive OUT = create_key()["KeyMetadata"]["KeyId"]
- T.Sensitive OUT = create_key()["KeyMetadata"]["Arn"]
- T.Sensitive OUT = create_key()["KeyMetadata"]["CustomKeyStoreId"]
- T.Sensitive OUT = create_key()["KeyMetadata"]["CloudHsmClusterId"]
- T.Sensitive OUT = decrypt()["Plaintext"]
- T.Sensitive OUT = decrypt()["KeyId"]
- T.Sensitive OUT = decrypt()["ResponseMetadata"]
- T.Sensitive OUT = describe_custom_key_stores()["CustomKeyStores"][i]["CustomKeyStoreId"] for some index *i*
- T.Sensitive OUT = describe_custom_key_stores()["CustomKeyStores"][i]["CustomKeyStoreName"]
- T.Sensitive OUT = describe_custom_key_stores()["CustomKeyStores"][i]["CloudHsmClusterId"]
- T.Sensitive OUT = describe_custom_key_stores()["CustomKeyStores"][i]["TrustAnchorCertificate"]
- T.Sensitive OUT = describe_custom_key_stores()["CustomKeyStores"][i]["TrustAnchorCertificate"]
- T.Sensitive OUT = describe_key()["KeyMetadata"]["AWSAccountId"]
- T.Sensitive OUT = describe_key()["KeyMetadata"]["KeyId"]
- T.Sensitive OUT = describe_key()["KeyMetadata"]["Arn"]
- T.Sensitive OUT = describe_key()["KeyMetadata"]["CustomKeyStoreId"]
- T.Sensitive OUT = describe_key()["KeyMetadata"][""CloudHsmClusterId]
- T.Sensitive OUT =  encrypt()["KeyId"]
- T.Sensitive OUT = generate_data_key()["Plaintext"]
- T.Sensitive OUT = generate_data_key()["KeyId"]
- T.Sensitive OUT = generate_data_key_pair()["KeyId"]
- T.Sensitive OUT = generate_data_key_pair_without_plaintext()["KeyId"]
- T.Sensitive OUT = get_parameters_for_import()["KeyId"]
- T.Sensitive OUT = get_parameters_for_import()["ImportToken"]
- T.Sensitive OUT = get_public_key()["KeyId"]
- T.Sensitive OUT = list_aliases()["Aliases"][i]["AliasArn"]
- T.Sensitive OUT = list_aliases()["Aliases"][i]["TargetKeyId"]
- T.Sensitive OUT = list_grants()["Grants"][i]["KeyId"]
- T.Sensitive OUT = list_grants()["Grants"][i]["GrantId"]
- T.Sensitive OUT = list_keys()["Keys"][i]["KeyId"]
- T.Sensitive OUT = list_keys()["Keys"][i]["KeyArn"]
- T.Sensitive OUT = list_retirable_grants()["Grants"][i]["KeyId"]
- T.Sensitive OUT = list_retirable_grants()["Grants"][i]["GrantId"]
- T.Sensitive OUT = re_encrypt()["SourceKeyId"]
- T.Sensitive OUT = re_encrypt()["KeyId"]
- T.Sensitive OUT = sign()["KeyId"]
- T.Sensitive OUT = verify()["KeyId"]



### Sinks


**CWE 99**

- get_key_policy(KeyId=**T.Network**,PolicyName=**T.Network** 
- generate_random(CustomKeyStoreId=**T.Network**)
- generate_data_key_pair_without_plaintext(KeyId=**T.Network**,..)
- cancel_key_deletion(KeyId=**T.Network**)
- connect_custom_key_store(CustomKeyStoreId=**T.Network**)
- create_alias(TargetKeyId=**T.Network**)
- create_custom_key_store(CloudHsmClusterId=**T.Network**, ..)
- create_grant(GranteePrincipal=**T.Network**)
- create_key(CustomKeyStoreId=**T.Network**,)
- delete_alias(AliasName=**T.Network**)
- delete_custom_key_store(CustomKeyStoreId=**T.Network**)
- delete_imported_key_material(KeyId=**T.Network**)
- describe_custom_key_stores(CustomKeyStoreName=**T.Network**, CustomKeyStoreId=**T.Network**)
- describe_key(KeyId=**T.Network**)
- disable_key(KeyId=**T.Network**)
- disable_key_rotation(KeyId=**T.Network**)
- disable_custom_key_store(CustomKeyStoreId=**T.Network**)
- enable_key(KeyId=**T.Network**)
- enable_key_rotation(KeyId=**T.Network**)
- encrypt(KeyId=**T.Network**..)
- generate_data_key(KeyId=**T.Network**,..)
- generate_data_key_pair(KeyId=**T.Network**,..)
- verify(KeyId=**T.Network**,) 
- update_key_description(KeyId=**T.Network**,) 
- get_key_rotation_status(KeyId=**T.Network**, ))
- get_parameters_for_import(KeyId=**T.Network**, ))
- get_public_key(KeyId=**T.Network**, )
- import_key_material(KeyId=**T.Network**, )
- list_aliases(KeyId=**T.Network**, )
- list_grants(KeyId=**T.Network**, )
- list_key_policies(KeyId=**T.Network**, )
- list_resource_tags(KeyId=**T.Network**, )
- put_key_policy(KeyId=**T.Network**, )
- re_encrypt(SourceKeyId=**T.Network**, DestinationKeyId=**T.Network**)
- retire_grant(KeyId=**T.Network**, GrantId=**T.Network**)
- schedule_key_deletion(KeyId=**T.Network**,) 
- sign(KeyId=**T.Network**,) 
- tag_resource(KeyId=**T.Network**,) 
- untag_resource(KeyId=**T.Network**,) 
- update_alias(KeyId=**T.Network**,) 
- update_custom_key_store(CustomKeyStoreId=**T.Network**, CloudHsmClusterId=**T.Network**) 

**CWE 201**


- tag_resource(.., Tags=XXX) where XXX is a list of dicts and XXX[i]["TagKey] == T.Sensitive or XXX[i]["TagValue"] == T.Sensitive
- create_alias(AliasName=**T.Sensitive**)
- create_custom_key_store(CustomKeyStoreName=**T.Sensitive**,,.)
- create_grant(Name=**T.Sensitive**, ...)
- create_key(Description=**T.Sensitive**, Tags=**T.Sensitive**,..)
- create_alias(AliasName=**T.Sensitive**)
- update_key_description(Description=**T.Sensitive**)
- generate_presigned_url(, Params=**T.Sensitive**, )



**CWE 259**

- update_custom_key_store(, KeyStorePassword=**HARDCODED**, )
- create_custom_key_store(KeyStorePassword=**HARDCODED**, .)

**CWE 321 XXX Not sure if proper CWE**
- create_custom_key_store(TrustAnchor=**HARDCODED**)
 
**CWE 547**

- create_grant(KeyId=**HARDCODED**,,..)
- decrypt(KeyId=**HARDCODED**, GrantTokens=[ **HARDCODED** ], )
- delete_custom_key_store(CustomKeyStoreId=**HARDCODED**)
- delete_imported_key_material(KeyId=**HARDCODE**)
- describe_custom_key_stores(CustomKeyStoreId=**HARDCODE**)
- describe_key(KeyId=**HARDCODED**, GrantTokens=[..**HARDCODED**..])
- disable_key(KeyId=**HARDCODED**, GrantTokens=[..**HARDCODED**..])
- disable_key_rotation(KeyId=**HARDCODED**)
- disable_custom_key_store(CustomKeyStoreId=**HARDCODED**)
- enable_key(KeyId=**HARDCODED**)
- enable_key_rotation(KeyId=**HARDCODED**)
- encrypt(KeyId=**HARDCODED**, GrantTokens=[...**HARDCODED**])
- generate_data_key(KeyId=**HARDCODED**, GrantTokens=[ ..**HARDCODED**.. ], )
- verify(KeyId=**HARDCODED**, GrantTokens=**HARDCODED**)
- generate_data_key_pair(KeyId=**HARDCODED**, GrantTokens=[ ..**HARDCODED**.. ], )
- update_key_description(KeyId=**HARDCODED**, )
- generate_data_key_pair_without_plaintext(KeyId=**HARDCODED**, GrantTokens=[ ..**HARDCODED**.. ], )
- get_key_policy(KeyId=**HARDCODED**, ..)
- get_key_rotation_status(KeyId=**HARDCODED**, )
- get_key_paramters_for_import(KeyId=**HARDCODED**, )
- get_public_key(KeyId=**HARDCODED**, GrantTokens=**HARDCODED**)
- import_key_material(KeyId=**HARDCODED**, ImportToken=**HARDCODED**)
- list_aliases(KeyId=**HARDCODED**,) 
- list_grants(KeyId=**HARDCODED**,) 
- list_key_policies(KeyId=**HARDCODED**,) 
- list_resource_tags(KeyId=**HARDCODED**,) 
- put_key_policy(KeyId=**HARDCODED**,) 
- re_encrypt(SourceKeyId=**HARDCODED**, DestinationKeyId=**HARDCODED**, GrantTokens=**HARDCODED*) 
- retire_grant(KeyId=**HARDCODED**, GrantToken=**HARDCODED**)
- schedule_key_deletion(KeyId=**HARDCODED**,)
- sign(KeyId=**HARDCODED**, GrantTokens=**HARDCODED**)
- tag_resource(KeyId=**HARDCODED**, )
- untag_resource(KeyId=**HARDCODED**, )
- update_alias(KeyId=**HARDCODED**, )


**CWE 312**

- encrypt(Plaintext=**HARDCODED**)


## SNS client

[Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html#client)

To get an instance of the client class `botocore.client.SNS`

```
client = boto.client('sns')
```

Or

```
session = botocore.session.get_session()
client = session.create_client('sns', region_name='us-west-2')
```

### Sources

- T.Sensitive OUT = confirm_subscription()["SubscriptionArn"]
- T.Sensitive OUT = create_platform_application()["PlatformApplicationArn"]
- T.Sensitive OUT = create_platform_endpoint()["EndpointArn"]
- T.Sensitive OUT = create_topic()["TopicArn"]
- T.Sensitive OUT = get_endpoint_attributes()["Attributes"]["CustomUserData"]
- T.Sensitive OUT = get_endpoint_attributes()["Attributes"]["Token"]
- T.Sensitive OUT = get_platform_application_attributes()["Attributes"]["EventEndpointCreated"]
- T.Sensitive OUT = get_platform_application_attributes()["Attributes"]["EventEndpointDeleted"]
- T.Sensitive OUT = get_platform_application_attributes()["Attributes"]["EventEndpointUpdated"]
- T.Sensitive OUT = get_platform_application_attributes()["Attributes"]["EventDeliveryFailure"]
- T.Sensitive OUT = get_sms_attributes()["attributes"]["DeliveryStatusIAMRole"]
- T.Sensitive OUT = get_subscription_attributes()["Attributes"]["Owner"]
- T.Sensitive OUT = get_subscription_attributes()["Attributes"]["SubscriptionArn"]
- T.Sensitive OUT = get_subscription_attributes()["Attributes"]["TopicArn"]
- T.Sensitive OUT = get_topic_attributes()["Attributes"]["Owner"]
- T.Sensitive OUT = get_topic_attributes()["Attributes"]["TopicArn"]
- T.Sensitive OUT = get_topic_attributes()["Attributes"]["KmsMasterKeyId"]
- T.Sensitive OUT = list_endpoints_by_platform_application()["Endpoints"][i]["EndpointArn"] for some index *i*
- T.Sensitive OUT = list_endpoints_by_platform_application()["Endpoints"][i]["Attributes"]["CustomUserData"] for some index *i*
- T.Sensitive OUT = list_endpoints_by_platform_application()["Endpoints"][i]["Attributes"]["Token"] for some index *i*
- T.Sensitive OUT = list_platform_applications()["PlatformApplications"][i]["PlatformApplicationArn"] for some index *i*
- T.Sensitive OUT = list_platform_applications()["PlatformApplications"][i]["Attributes"]["CustomUserData"] for some index *i*
- T.Sensitive OUT = list_platform_applications()["PlatformApplications"][i]["Attributes"]["EventEndpointCreated"] for some index *i*
- T.Sensitive OUT = list_platform_applications()["PlatformApplications"][i]["Attributes"]["EventEndpointDeleted"] for some index *i*
- T.Sensitive OUT = list_platform_applications()["PlatformApplications"][i]["Attributes"]["EventEndpointUpdated"]  for some index *i*
- T.Sensitive OUT = list_platform_applications()["PlatformApplications"][i]["Attributes"]["EventDeliveryFailure"]  for some index *i*
- T.Sensitive OUT = list_subscriptions()["Subscriptions"][i]["SubscriptionArn"] for some index *i*
- T.Sensitive OUT = list_subscriptions()["Subscriptions"][i]["Owner"] for some index *i*
- T.Sensitive OUT = list_subscriptions()["Subscriptions"][i]["TopicArn"] for some index *i*
- T.Sensitive OUT = list_subscriptions_by_topic()["Subscriptions"][i]["SubscriptionArn"] for some index *i*
- T.Sensitive OUT = list_subscriptions_by_topic()["Subscriptions"][i]["Owner"] for some index *i*
- T.Sensitive OUT = list_subscriptions_by_topic()["Subscriptions"][i]["TopicArn"] for some index *i*
- T.Sensitive OUT = list_topics()["Topics"][i]["TopicArn"] for some index *i*
- T.Sensitive OUT = set_platform_application_attributes()["Attributes"]["PlatformCredential"]
- T.Sensitive OUT = subscribe()["SubscriptionArn"]


- T.Network OUT = list_tags_for_resource()["Tags"][i]["Key"] 
- T.Network OUT = list_tags_for_resource()["Tags"][i]["Value"] 



### Sinks

**CWE 547**

- confirm_subscription(, Token=**HARDCODED**, ..)
- create_platform_application(, Attributes=XXX, ..) where XXX is a dict and has:
  - XXX["PlatformCredential"] == **HARDCODED**
- create_platform_endpoint(, Token=**HARDCODED**, )

**CWE 201**

- add_permission(, Label=**T.Sensitive**, ..)
- create_platform_application(Name=**T.Sensitive**,
- create_platform_endpoint(, CustomUserData=**T.Sensitive**, Attributes=XXX,) where XXX is a dict with:
  - XXX["CustomUserData"] = **T.Sensitive**
- create_topic(Name=**T.Sensitive**, Attributes=XXX,  Tags=YYY) where XXX and YYY are dicts with:
  - for Attributes["DisplayName"] = **T.Sensitive**
  - for Tags[T.Sensitive] = **T.Sensitive**
- generate_presigned_url(, Params=**T.Sensitive**, )
- publish(, Message=**T.Sensitive**, Subject=**T.Sensitive**, MessageAttributes=**T.Sensitive**)
  - for MessageAttributes we look for:
    -  MessageAttributes[**T.Sensitive**]
    -  MessageAttributes[key]["DataType"] = T.Sensitive
    -  MessageAttributes[key]["StringValue"] = T.Sensitive
    -  MessageAttributes[key]["BinaryValue"] = T.Sensitive
- set_endpoint_attributes(, Attributes=**T.Sensitive**, )
  - Attributes[T.Sensitive]
  - Attributes[key] = T.Sensitive
- set_platform_application_attributes(, Attributes=**T.Sensitive**, )
  - Attributes[T.Sensitive]
  - Attributes[key] = T.Sensitive
- set_sms_attributes(, Attributes=**T.Sensitive**, )
  - Attributes[T.Sensitive]
  - Attributes[key] = T.Sensitive
- set_subscription_attributes(, AttributeValue=**T.Sensitive**, )
- set_topic_attributes(, AttributeValue=**T.Sensitive**, )
- subscribe(, Attributes=**T.Sensitive**, ) 
  - Attributes[T.Sensitive]
  - Attributes[key] = T.Sensitive
- tag_resource(,Tags=**T.Sensitive**,)
  - notes Tags is a list of dicts so we are concerned with:
    - Tags[i]["Key"] = T.Sensitive
    - Tags[i]["Value"] = T.Sensitive

**CWE 99**

- delete_endpoint(EndpointArn=**T.Network**)
- delete_platform_application(PlatformApplicationArn=**T.Network**)
- delete_topic(TopicArn=**T.Network**)
- get_endpoint_attributes(EndpointArn=**T.Network**)
- get_platform_application_attributes(PlatformApplicationArn=**T.Network**)
- get_subscription_attributes(SubscriptionArn=**T.Network**)
- get_topic_attributes(SubscriptionArn=**T.Network**)
- list_endpoints_by_platform_application(PlatformApplicationArn=**T.Network**)
- list_subscriptions_by_topic(TopicArn=**T.Network**)
- list_tags_for_resource(ResourceArn=**T.Network**)
- publish(TopicArn=**T.Network**, TargetArn=**T.Network**, PhoneNumber=**T.Network**, Message=**T.Network**, Subject=**T.Network**)
- remove_permission(TopicArn=**T.Network**)
- set_endpoint_attributes(EndpointArn=**T.Network**)
- set_platform_application_attributes(PlatformApplicationArn=**T.Network**)
- set_subscription_attributes(SubscriptionArn=**T.Network**)
- set_topic_attributes(TopicArn=**T.Network**)
- subscribe(TopicArn=**T.Network**)
- tag_resource(ResourceArn=**T.Network**)
- unsubscribe(SubscriptionArn=**T.Network**)
- untag_resource(ResourceArn=**T.Network**)

**CWE 321**

- set_platform_application_attributes["PlatformCredential"] = **HARDCODED**

**CWE 311**

- subscribe(, Protocol="http", )
- subscribe(, Protocol="email", ) XXX
- subscribe(, Protocol="email-json", ) XXX
- subscribe(, Endpoint="http://some.string.starting.withinsecure.http") 







## SQS client 

[Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#client)

To get an instance of the client class `botocore.client.SQS`

```
import boto3

client = boto3.client('sqs')
```

or

```
session = botocore.session.get_session()
client = session.create_client('sqs', region_name='us-west-2')
```

### Sources

- T.Sensitive OUT = get_queue_attributes()["QueueArn"]
- T.Sensitive OUT = get_queue_attributes()["RedrivePolicy"]["deadLetterTargetArn"]
- T.Sensitive OUT = get_queue_attributes()["KmsMasterKeyId"]
- T.Sensitive OUT = receive_message()["Messages"][i]["Body"] for some list index *i*.
- T.Sensitive OUT = receive_message()["Messages"][i]["Attributes"]["KmsMasterKeyId"] for some list index *i*.
- T.Sensitive OUT = receive_message()["Messages"][i]["Attributes"]["QueueArn"] for some list index *i*.

- T.Network OUT = list_queue_tags()["Tags"]

### Sinks

**CWE 99**

- add_permission(..., QueueUrl=**T.Network**, ...)
- change_message_visibility(..., QueueUrl=**T.Network**, ...)
- chang_message_visibility_batch(..., QueueUrl=**T.Network**, ...)
- create_queue(, QueueName=**T.Network**, ..)
- delete_message(QueueUrl=**T.Network**,) 
- delete_message_batch(QueueUrl=**T.Network**,) 
- delete_queue(QueueUrl=**T.Network**)
- get_queue_attributes(QueueUrl=**T.Network**, ..)
- get_queue_url(.., QueueUrl=**T.Network**, ..)
- list_dead_letter_source_queues(.., QueueUrl=**T.Network**, ..)
- list_queue_tags(QueueUrl=**T.Network**)
- list_queues(QueueNamePrefix=**T.Network**)
- purge_queue(QueueNamePrefix=**T.Network**)
- receive_message(QueueUrl=**T.Network**, .., MessageAttributeNames=**T.Network**, )
- remove_permission(.., QueueUrl=**T.Network**, ..)
- send_message(.., QueueUrl=**T.Network**, ..)
- send_message_batch(.., QueueUrl=**T.Network**, ..)
- set_queue_attributes(QueueUrl=**T.Network**..)
- tag_queue(QueueUrl=**T.Network**..)
- untag_queue(QueueUrl=**T.Network**..)

**CWE 284**

- add_permission(, AWSAccountIds=**T.Network**, Actions=**T.Network**, ..)
- add_permission(,  Actions=**CheckForAsterisk**, ..) ... if the `Actions` list contains a hardcoded value of `"*"`
- remove_permission(.., Label=**T.Network**, ..)

**CWE 201**

- add_permission(..., Label=**T.Sensitive**, ...)
- create_queue(, QueueName=**T.Sensitive**, tags=**T.Sensitive**, ..) where `tags` is a dict and either key or value is sensitive
- generate_presigned_url(, Params=**T.Sensitive**, )
- send_message(.., MessageBody=**T.Sensitive**, MessageAttributes=**T.Sensitive**, MessageSystemAttributes=**T.Sensitive**, ..) the attributes if any value is sensitive, then ...
- send_message(.., Entries=**T.Sensitive**, ..) where Entries is a list of dicts and we are looking at Entries[i]["MessageBody"] = sensitive, or the Entries[i]["MessageAttributes"] and Entries[i]["MessageSystemAttributes"] contains sensitive data
- set_queue_attributes(.., Attributes=**T.Sensitive**) any key or value being sensitive
- tag_queue(.., Tags=**T.Sensitive**)

**CWE 547**

- create_queue(, Attribute=XXX,...) where XXX is a dict with XXX["KmsMasterKeyId"] = **HARDCODED**
- set_queue_attributes(..., Attributes=XXX, ..) where XXX is a dict with XXX["KmsMasterKeyId"] = **HARDCODED**
 

## S3 client 

[Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#client)

To get an instance of the client class `botocore.client.S3`

```
import boto3

client = boto3.client('s3')
```

or


```
session = botocore.session.get_session()
client = session.create_client('s3', region_name='us-west-2')
```

### Sources

- T.Sensitive OUT = complete_multipart_upload()["SSEKMSKeyId"]
- T.Sensitive OUT = get_bucket_encryption()['ServerSideEncryptionConfiguration']['Rules'][i]['ApplyServerSideEncryptionByDefault']['KMSMasterKeyID'] for some list
      index *i*.
- T.Sensitive OUT = get_bucket_inventory_configuration()['InventoryConfiguration']['Destination']['S3BucketDestination']['AccountId']
- T.Sensitive OUT = get_bucket_inventory_configuration()['InventoryConfiguration']['Destination']['S3BucketDestination']['Encryption']['SSEKMS']['KeyId']
- T.Sensitive OUT = get_bucket_inventory_configuration()['InventoryConfiguration']['Destination']['S3BucketDestination']['Encryption']['SSES3']
- T.Sensitive OUT = get_bucket_logging()['LoggingEnabled']['TargetGrants'][i]['Grantee']['EmailAddress'] for some index *i*
- T.Sensitive OUT = get_bucket_logging()['LoggingEnabled']['TargetGrants'][i]['Grantee']['ID'] for some index *i*
- T.Sensitive OUT = get_bucket_notification_configuration()['TopicConfigurations']['TopicArn']
- T.Sensitive OUT = get_bucket_notification_configuration()['QueueConfigurations']['QueueArn']
- T.Sensitive OUT = get_bucket_notification_configuration()['LambdaFunctionConfigurations']['LambdaFunctionArn']
- T.Sensitive OUT = get_object_acl()["Owner"]["ID"]
- T.Sensitive OUT = get_object_acl()["Grants"][i]["Grantee"]["EmailAddress"]
- T.Sensitive OUT = get_object_acl()["Grants"][i]["Grantee"]["ID"]
- T.Sensitive OUT = head_object()['SSECustomerKey']
- T.Sensitive OUT = put_object()["SSEKMSKeyId"]
- T.Sensitive OUT = put_object()["SSEKMSEncryptionContext"]
- T.Sensitive OUT = upload_part()['SSEKMSKeyId'] 
- T.Sensitive OUT = upload_part_copy()['SSEKMSKeyId']


- T.Network OUT = get_object()['Body']  is of type StreamingBody()
- T.Network OUT = get_object()['Metadata']  is of type dict
- T.Network OUT = get_object_tagging()['TagSet'][i]['Key']
- T.Network OUT = get_object_tagging()['TagSet'][i]['Value']
- T.Network OUT = get_object_torrent()['Body'] is of type StreamingBody()

See the "more complicated" steps below for some other cases


### Sinks

**CWE 99 (Resource Injection)**

- get_object_acl(Bucket=**T.Network**, Key=**T.Network**) 
- get_object_legal_hold(Bucket=**T.Network**, Key=**T.Network**) 
- get_object_lock_configuration(Bucket=**T.Network**, Key=**T.Network**)
- get_object_retention(Bucket=**T.Network**, Key=**T.Network**)
- get_object_tagging(Bucket=**T.Network**, Key=**T.Network**) 
- get_object_torrent(Bucket=**T.Network**, Key=**T.Network**)
- get_public_access_block(Bucket=**T.Network**, ...)
- head_bucket(Bucket= **T.Network**, ...)
- head_object(Bucket=**T.Network**, Key=**T.Network**,  ...)
- list_bucket_analytics_configurations(Bucket=**T.Network**, ..)
- list_bucket_inventory_configurations(Bucket=**T.Network**, ..)
- list_bucket_metrics_configurations(Bucket=**T.Network**, ..)
- list_multipart_uploads(Bucket=**T.Network**, Delimiter=**T.Network**, Prefix=**T.Network**, ..)
- list_object_versions(Bucket=**T.Network**, Delimiter=**T.Network**, Prefix=**T.Network**, ...) 
- list_objects(Bucket=**T.Network**, Delimiter=**T.Network**, Prefix=**T.Network**, ...) 
- list_objects_v2(Bucket=**T.Network**, Delimiter=**T.Network**, Prefix=**T.Network**, ...) 
- list_parts(Bucket=**T.Network**, Key=**T.Network**, ...) 
- put_bucket_accelerate_configuration(Bucket=**T.Network**, ...)
- put_bucket_acl(Bucket=**T.Network**, ...)
- put_bucket_analytics_configuration(Bucket=**T.Network**, Id=**T.Network**)   Note that for the *AnalyticsConfiguration*, we are looking for AnalyticsConfiguration["StorageClassAnalysis"]["DataExport"]["Destination"]["Bucket"] == T.Network
- put_bucket_cors(Bucket=**T.Network**, ...)
- put_bucket_lifecycle(Bucket=**T.Network**, ...)
- put_bucket_lifecycle_configuration(Bucket=**T.Network**, Id=**T.Network**)   where for *InventoryConfiguration* we are concerned with if InventoryConfiguration["Destination"]["S3BucketDestination"]["Bucket"] == T.Network 
- put_bucket_encryption(Bucket=**T.Network**, ...)
- put_bucket_inventory_configuration(Bucket=**T.Network**, ...)
- put_bucket_logging(Bucket=**T.Network**, BucketLoggingStatus=**T.Network**) where *BucketLoggingStatus* we are looking to see if BucketLoggingSTatus["LoggingEnabled"]["TargetBucket"] == T.Network 
- put_bucket_metrics_configuration(Bucket=**T.Network**, Id=**T.Network**, )
- put_bucket_notification(Bucket=**T.Network**, ...) 
- put_bucket_notification_configuration(Bucket=**T.Network**, ...) 
- abort_multipart_upload(Bucket=**T.Network**, Key=**T.Network**,)  
- complete_multipart_upload(Bucket=**T.Network**, Key=**T.Network**, )  
- client.copy(CopySource=**T.Network**, Bucket=**T.Network**, Key=**T.Network**,  ...)
- copy_object(Bucket=**T.Network**, Key=**T.Network**, CopySource=**T.Network**, )
- create_bucket(Bucket=**T.Network**, ...)
- create_multipart_upload(Bucket=**T.Network**, Key=**T.Network**, ...)
- delete_bucket(Bucket=**T.Network**)
- delete_bucket_analytics_configuration(Bucket=**T.Network**, Id=**T.Network**)
- delete_bucket_cors(Bucket=**T.Network**)
- delete_bucket_encryption(Bucket=**T.Network**)
- delete_bucket_inventory_configuration(Bucket=**T.Network**, Id=**T.Network**)
- delete_bucket_lifecycle(Bucket=**T.Network**)
- delete_bucket_metrics_configuration(Bucket=**T.Network**, Id=**T.Network**)
- delete_bucket_policy(Bucket=**T.Network**)
- delete_bucket_replication(Bucket=**T.Network**)
- delete_bucket_tagging(Bucket=**T.Network**)
- delete_bucket_website(Bucket=**T.Network**)
- delete_bucket_object(Bucket=**T.Network**, Key=**T.Network**)
- delete_object_tagging(Bucket=**T.Network**, Key=**T.Network**)
- delete_objects(Bucket=**T.Network**, Delete=**T.Network**)
- delete_public_access_block(Bucket=**T.Network**)
- download_file(Bucket=**T.Network**, Key=**T.Network**, ...)  Note that Bucket, Key are required in that order
- download_file_obj(Bucket=**T.Network**, Key=**T.Network**, ...)  Note that Bucket, Key are required in that order
- put_bucket_policy(Bucket=**T.Network**, ...) 
- put_bucket_replication(Bucket=**T.Network**, ...) 
- put_bucket_request_payment(Bucket=**T.Network**, ...) 
- put_bucket_request_tagging(Bucket=**T.Network**, ...) 
- put_bucket_versioning(Bucket=**T.Network**, ...) 
- put_bucket_website(Bucket=**T.Network**,  ...)
- put_object(Bucket=**T.Network**, Key=**T.Network**,  ...)
- put_object_acl(Bucket=**T.Network**, Key=**T.Network**,  ...)
- put_object_legal_hold(Bucket=**T.Network**, Key=**T.Network**,  ...)
- put_object_lock_configuration(Bucket=**T.Network**,  ...)
- put_object_retention(Bucket=**T.Network**,  Key=**T.Network**) 
- put_object_tagging(Bucket=**T.Network**,  Key=**T.Network**, ...)
- put_public_access_block(Bucket=**T.Network**,  ...)
- restore_object(Bucket=**T.Network**, Key=**T.Network**,  ...)
- select_object_content(Bucket=**T.Network**, Key=**T.Network**, ...)
- upload_file(.., Bucket=**T.Network**, Key=**T.Network**, ...)
- upload_fileobj(.., Bucket=**T.Network**, Key=**T.Network**, ...)
- upload_part(Bucket=**T.Network**, Key=**T.Network**,...)
- upload_part_copy(Bucket=**T.Network**, Key=**T.Network**,...)
- download_fileobj(Bucket=**T.Network**, Key=**T.Network**, ...)
- generate_presigned_post(Bucket=**T.Network**, Key=**T.Network**, ...)
- get_bucket_accelerate_configuration(Bucket=**T.Network**,  ...)
- get_bucket_acl(Bucket=**T.Network**,  ...)
- get_bucket_analytics_configuration(Bucket=**T.Network**, Id=**T.Network**) 
- get_bucket_cors(Bucket=**T.Network**)
- get_bucket_encryption(Bucket=**T.Network**)
- get_bucket_inventory_configuration(Bucket=**T.Network**)
- get_bucket_lifecycle(Bucket=**T.Network**)
- get_bucket_lifecycle_configuration(Bucket=**T.Network**)
- get_bucket_location(Bucket=**T.Network**)  XXX Hrmf, i guess usable to scan buckets (open bucket scanner)
- get_bucket_logging(Bucket=**T.Network**) 
- get_bucket_metrics_configuration(Bucket=**T.Network**) 
- get_bucket_notification(Bucket=**T.Network**) 
- get_bucket_notification_configuration(Bucket=**T.Network**) 
- get_bucket_policy(Bucket=**T.Network**) 
- get_bucket_policy_status(Bucket=**T.Network**) 
- get_bucket_replication(Bucket=**T.Network**) 
- get_bucket_request_payment(Bucket=**T.Network**) 
- get_bucket_request_payment(Bucket=**T.Network**) 
- get_bucket_versioning(Bucket=**T.Network**) 
- get_bucket_website(Bucket=**T.Network**) 
- get_object(Bucket=**T.Network**, Key=**T.Network**) 


**CWE 284**

- put_bucket_acl(... , ACL=**T.Network**, ...)
- put_object(... , ACL=**T.Network**, ...)
- put_object_acl(... , ACL=**T.Network**, ...)
- copy_object(... , ACL=**T.Network**, ...)
- copy_object(..., ACL='public-read-write', ..) 
- create_bucket(... , ACL=**T.Network**, ...)
- create_bucket(... , ACL='public-read-write', ..)  <- hardcoded bad value
- create_bucket(... , ACL='public-read', ..)  <- hardcoded bad value
- create_multipart_upload(... , ACL=**T.Network**, ...)


**CWE 73 (Path manipulation)**

- upload_file(Filename=**T.Network**, ...)
- download_file(..., Filename=**T.Network**, ...)

**CWE 312**

- download_file(..., Filename=**T.Sensitive**, ...)

**CWE Access Controls ??? XXX**

- put_bucket_acl(..., AccessControlPolicy=X, ...) where (X["Grants"][i]["Grantee"]["URI"] == http://acs.amazonaws.com/groups/global/AuthenticatedUsers) or (X["Grants"][i]["Grantee"]["URI"] == http://acs.amazonaws.com/groups/global/AllUsers AND where X["Grants"][i]["Grantee"]["Type"] does not contain any of following: "WRITE", "WRITE_ACP", "FULL_CONTROL")
  
XXX no test

  

**CWE 942**

- put_bucket_cors(.., CORSConfiguration=XXX, ..) XXX is a dict with a list of dicts.
      and we must look at the dicts in the list to determine if one contains something like:
      This includes:
```
  { "CORSRules" :
    [
      {
        'AllowedOrigins' : "*"
      },
    ...
    ]
  }
``` 


**CWE 547**

- put_bucket_encryption(..., ServerSideEncryptionConfiguration={'Rules' : [ { ApplyServerSideEncryptionByDefault': { 'KMSMasterKeyID' : **HARDCODED** } }], .. })  So, of the list of Rules, the KMSMasterKeyID in one of them under ApplyServerSideEncryptionByDefault shoudl not be hardcoded.
- put_bucket_inventory_configuration(.., InventoryConfiguration=XXX ...) where XXX is a dict with encryption fields we dont want hardcoded:
```
InventoryConfiguration={
        'Destination': {
            'S3BucketDestination': {
                'AccountId': 'string',
                'Bucket': 'string',
                'Format': 'CSV'|'ORC'|'Parquet',
                'Prefix': 'string',
                'Encryption': {
                    'SSES3': {}
                    ,
                    'SSEKMS': {
                        'KeyId': 'string'
....
   }
```
      So we are interested in if Encryption["SSES3"] or Encryption["SSEKMS"]["KeyId"] are **HARDCODED**
- put_object(..., SSEKMSKeyId=**HARDCODED**, ...)
- restore_object(,,, RestoreRequest=XXX, ...) XXX is a dict where XXX['OutputLocation']['Encryption']['KMSKeyId'] = **HARDCODED**
- copy_object(..., SSEKMSKeyId=**HARDCODED**, ..)
- create_multipart_upload(... SSEKMSKeyId=**HARDCODED**, ...)
  


**CWE 201**

- client.copy(..,  Key=**T.Sensitive**, ...)  
- copy_object(...,  Metadata=**T.Sensitive**,  ...)  
- create_bucket(Bucket=**T.Sensitive**, ...)
- create_multipart_upload(.., Key=**T.Sensitive**, Tagging=**T.Sensitive**, ...) Tagging here is type str. 
- create_multipart_upload(..., SSECustomerKey=**HARDCODED**, ..., CopySourceSSECustomerKey=**HARDCODED**)
- put_bucket_analytics_configuration(..., AnalyticsConfiguration=**T.Sensitive**...) Note that for the *AnalyticsConfiguration*, we are looking for AnalyticsConfiguration["StorageClassAnalysis"]["DataExport"]["Destination"]["Prefix"] == T.Sensitive
- put_bucket_lifecycle_configuration(... Id=**T.Sensitive**, InventoryConfiguration=**T.Sensitive**, ...) where for *InventoryConfiguration* we are concerned with if (InventoryConfiguration["Destination"]["S3BucketDestination"]["Prefix"] == T.Sensitive) or (InventoryConfiguration["Id"] == T.Sensitive)
- generate_presigned_url(, Params=**T.Sensitive**, )
- put_bucket_logging(, BucketLoggingStatus=**T.Sensitive**)  where for *BucketLoggingStatus* we are looking to see if BucketLoggingStatus["LoggingEnabled"]["TargetPrefix"] == T.Sensitive
- put_bucket_metrics_configuration(, MetricsConfiguration=**T.Sensitive**, ..) where for *MetricsConfiguration* we are looking at whether (MetricsConfiguration["Id"] == T.Sensitive) 
- put_bucket_request_tagging(.., Tagging=**T.Sensitive**, ...)  `Tagging` is list of dicts with 2 keys "Bucket" and "Key" whose values if tainted sensitive so if either Tagging[i]["Bucket"] == T.Sensitive or Tagging[i]["key"] == T.Sensitive for some index *i*.
- put_bucket_website( WebsiteConfiguration=**T.Sensitive**) where we check if either (WebsiteConfiguration["RedirectAllRequestsTo"]["HostName"] = **T.Sensitive**) or (WebsiteConfiguration["RoutingRules"]["Redirect"]["HostName"]  = **T.Sensitive**) 
- put_object(...,  WebsiteRedirectLocation = **T.Sensitive**, Metadata=**T.Sensitive**, Tagging=**T.Sensitive*,  ...)
- put_object_tagging(..., Tagging=**T.Sensitive**, ...) ... where either Tagging["TagSet"][i]["Bucket"] == T.Sensitive or Tagging["TagSet"][i]["Key"] == T.Sensitive for any index *i*.
- upload_file(... Key=**T.Sensitive**,...)
- upload_fileobj(... Key=**T.Sensitive**,...)
- upload_part_copy(... Key=**T.Sensitive**,...)
- upload_part(... Key=**T.Sensitive**,...)



**CWE 321**

- put_object(..., SSECustomerKey=**HARDCODED**, ...)
- put_object_lock_configuration(..., Token=**HARDCODED**, ...)
- select_object_content(... SSECustomerKey=**HARDCODED**,...)
- upload_part(... SSECustomerKey=**HARDCODED**,...)
- upload_part_copy(... SSECustomerKey=**HARDCODED**,..., CopySourceSSECustomerKey=**HARDCODED**)
- get_object(.., SSECustomerKey=**HARDCODED**, ..)
- head_object(..., SSECustomerKey=**HARDCODED**, ...)
- copy_object(..., SSECustomerKey=**HARDCODED**, CopySourceSSECustomerKey=**HARDCODED**,...) 


**CWE 89 XXX**

- select_object_content(..., ExpressionType='SQL', Expression=**T.Network** ...) ... ExpressionType *must* be SQL along with tainted Expression value.


**CWE 601 (Redirect)**

- copy_object(..., WebsiteRedirectLocation=**T.Network**, ...) 
- put_bucket_website(  WebsiteConfiguration=**T.Network**)
  - Note we look for WebsiteConfiguration["RedirectAllRequestsTo"]["HostName"] == T.Network 
  - or WebsiteConfiguration["RoutingRules"]["Redirect"]["HostName"] == T.Network
- put_object(...,  WebsiteRedirectLocation = **T.Network**, ...)
- create_multipart_upload(.. WebsiteRedirectLocation=**T.Network**, ..)

**CWE 311**

- put_bucket_website(  WebsiteConfiguration=XXX) where
  - we look for XXX["RedirectAllRequestsTo"]["Protocol"] == "http"  and not https
  - or XXX["RoutingRules"]["Redirect"]["Protocol"] == "http"  and not https
- put_object(...,  WebsiteRedirectLocation = "http:// ..." , ...)  String beginning with "http:"
- copy_object(..., WebsiteRedirectLocation="http://...", ..) String beginning with "http:"
- create_multipart_upload(.. WebsiteRedirectLocation="http://" ) String beginning with "http:"


### Slightly more complicated

If we download a file from S3, we should consider it tainted. This may require a bit of extra
work to scan these properly (and if we cannot do it until a later time at which the scanner
is more mature, then that is fine **BUT** we must note that).

- download_file(..., Filename=SomeFileString)

The pattern we are looking at is something like:

```
	client = boto3.client('s3')
	s3.download_file(Bucket=good_bucket, Key=good_key, Filename="LocalFile")
	with open("LocalFile", "r") as oh:
		data = oh.read() # SOURCE
		return {
			"result" : data
		} # CWEID 80 
```

The CWEID 80 is just an example, the important point is that we can taint data
being read from the download S3 file.

Similarly we have the instance method:

- download_fileobj(...., Fileobj=N)

The pattern we are looking at is something like:

```
	client = boto3.client('s3')
	with open("LocalFile", "r") as oh:
		s3.download_file(Bucket=good_bucket, Key=good_key, Fileobj=oh)
		oh.seek(0)
		data = oh.read() # SOURCE
		return {
			"result" : data
		} # CWEID 80 
```
	
