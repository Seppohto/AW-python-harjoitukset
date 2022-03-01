from azure.identity import DefaultAzureCredential

from azure.mgmt.resource import ResourceManagementClient

import os
def listRG():

    SUBSCRIPTION_ID = os.environ.get("SUBSCRIPTION_ID", None)



    # Create client

    # For other authentication approaches, please see: https://pypi.org/project/azure-identity/

    resource_client = ResourceManagementClient(

        credential=DefaultAzureCredential(),

        subscription_id=SUBSCRIPTION_ID

    )



    # List resource groups

    resource_groups = list(resource_client.resource_groups.list())

    #print("List resource groups:\n{}".format(resource_groups))

   

    for i in resource_groups:

        print(i)

        print("Name: {}\nLocation: {}\nTags: {}\n".format(i.name, i.location, i.tags))

listRG()