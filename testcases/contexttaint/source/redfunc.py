import boto3
import json
import logging
import os
import pprint

def lambda_handler(e, c):
    good_bucket = "andrew-s3-lambda-test"

    sensi00 = c.invoked_function_arn # SOURCE SENSITIVE
    print(sensi00) # CWEID 532
    sensi01 = c.log_group_name # SOURCE SENSITIVE
    c.log(sensi01) # CWEID 532
    sensi02 = c.log_stream_name # SOURCE SENSITIVE
    sys.stdout.write(sensi02) # CWEID 532
    sensi03 = c.function_name    # SOURCE SENSITIVE
    sys.stderr.write(sensi03) # CWEID 532

    taint00 = c.client_context.custom["foo"] # SOURCE, SOURCE SENSITIVE
    print(taint00) # CWEID 117, 532
    taint01 = c.client_context.env["bar"] # SOURCE, SOURCE SENSITIVE
    c.log(taint01) # CWEID 117, 532


    taint02 = c.client_context.client.app_title # SOURCE, SOURCE SENSITIVE
    sys.stdout.write(taint02) # CWEID 117, 532
    taint03 = c.client_context.client.app_version_name # SOURCE, SOURCE SENSITIVE
    sys.stderr.write(taint03) # CWEID 117, 532
    taint04 = c.client_context.client.app_version_code # SOURCE, SOURCE SENSITIVE
    logging.debug(taint04) # CWEID 117, 532
    taint05 =  c.client_context.client.app_package_name # SOURCE, SOURCE SENSITIVE
    logging.info(taint05) # CWEID 117, 532
    taint06 =  c.client_context.client.installation_id # SOURCE, SOURCE SENSITIVE
    logging.log(taint06) # CWEID 117, 532
    taint07 =  c.client_context.client.installation_id # SOURCE, SOURCE SENSITIVE
    logging.warning(taint07) # CWEID 117, 532
    taint08 =  c.client_context.client.installation_id # SOURCE, SOURCE SENSITIVE
    logging.error(taint08) # CWEID 117, 532
    taint09 =  c.client_context.client.installation_id # SOURCE, SOURCE SENSITIVE
    logging.exception(taint09) # CWEID 117, 532

    sensi11 = os.environ["AWS_ACCESS_KEY_ID"] # SOURCE SENSITIVE
    print(sensi11) # CWEID 532
    sensi12 = os.environ["AWS_SECRET_ACCESS_KEY"] # SOURCE SENSITIVE
    print(sensi12) # CWEID 532
    sensi13 = os.environ["AWS_SESSION_TOKEN"] # SOURCE SENSITIVE
    print(sensi13) # CWEID 532
    sensi14 = os.environ["AWS_SECURITY_TOKEN"] # SOURCE SENSITIVE
    print(sensi14) # CWEID 532

    if "invals" not in e or "foo" not in e["invals"]:
        return {
          'result': 'error',
          'eventinfo': json.dumps(pprint.pformat(e)),
        }

