from azure.identity import AzureCliCredential,DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.storage.blob import BlobClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient


import os



credential = AzureCliCredential()

subscription_id = os.environ["SUBSCRIPTION_ID"]

resource_client = ResourceManagementClient(credential, subscription_id)

SUBSCRIPTION_ID = os.environ.get("SUBSCRIPTION_ID", None)
GROUP_NAME = "olliExample-rg"
STORAGE_ACCOUNT = "olliexamplestrg"
SUBNET = "ollisubnet"
BLOB_CONTAINER = "olliblobexample"
VIRTUAL_NETWORK_NAME = "ollivnettesti"
INTERFACE_NAME = "interfaceolli"
NETWORK_NAME = "ollivnettesti"
VIRTUAL_MACHINE_EXTENSION_NAME = "ollivmextensionx"
VIRTUAL_MACHINE_NAME = "lsolli01vm"


resource_client = ResourceManagementClient(
    credential=DefaultAzureCredential(),
    subscription_id=SUBSCRIPTION_ID
)
storage_client = StorageManagementClient(
    credential=DefaultAzureCredential(),
    subscription_id=SUBSCRIPTION_ID
)
network_client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id=SUBSCRIPTION_ID
    )
compute_client = ComputeManagementClient(
    credential=DefaultAzureCredential(),
    subscription_id=SUBSCRIPTION_ID
)


def listrgs():

# Retrieve the list of resource groups

    group_list = resource_client.resource_groups.list()



# Show the groups in formatted output

    column_width = 40



    print("Resource Group".ljust(column_width) + "Location")

    print("-" * (column_width * 2))



    for group in list(group_list):

        print(f"{group.name:<{column_width}}{group.location}")

def createrg(rgname):
    GROUP_NAME = rgname
    resource_client.resource_groups.create_or_update(
        GROUP_NAME,
        {"location": "westeurope"}
    )
        
    
def createstorageaccount(storagename):
    STORAGE_ACCOUNT = storagename
    storage_client.storage_accounts.begin_create(
        GROUP_NAME,
        STORAGE_ACCOUNT,
        {
          "sku": {
            "name": "Standard_GRS"
          },
          "kind": "StorageV2",
          "location": "westeurope",
          "encryption": {
            "services": {
              "file": {
                "key_type": "Account",
                "enabled": True
              },
              "blob": {
                "key_type": "Account",
                "enabled": True
              }
            },
            "key_source": "Microsoft.Storage"
          },
          "tags": {
            "createdBy": "olli",
            "inspiredBy": "Gainz"
          }
        }
    ).result()
    return

def getstorageaccount():
    storage_account = storage_client.storage_accounts.get_properties(
        GROUP_NAME,
        STORAGE_ACCOUNT
    )
    print("Get storage account:\n{}".format(storage_account))
    return

def listblobcontainers():
    blobcontainers_list = storage_client.blob_containers.list(GROUP_NAME,STORAGE_ACCOUNT)

    column_width = 40



    print("Blob containers".ljust(column_width))

    print("-" * (column_width * 2))


    for group in list(blobcontainers_list):

        print(f"{group.name:<{column_width}}")
    return

def createblobcontainer(containername):
    BLOB_CONTAINER = containername
    blob_container = storage_client.blob_containers.create(
        GROUP_NAME,
        STORAGE_ACCOUNT,
        BLOB_CONTAINER,
        {}
    )
    print("Create blob container:\n{}".format(blob_container))
    return

def getblobcontainer():
    blob_container = storage_client.blob_containers.get(
        GROUP_NAME,
        STORAGE_ACCOUNT,
        BLOB_CONTAINER
    )
    print("Get blob container:\n{}".format(blob_container))
    return

def deleteblobcontainer(containername):    
    BLOB_CONTAINER = containername
    blob_container = storage_client.blob_containers.delete(
        GROUP_NAME,
        STORAGE_ACCOUNT,
        BLOB_CONTAINER
    )
    print("Delete blob container:\n{}".format(blob_container))

def DeleteRgGroup(groupname):
    GROUP_NAME = groupname
    resource_client.resource_groups.begin_delete(
        GROUP_NAME
    ).result()
    return

def uploadBlob(tiedosto):
    blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=olliexamplestrg;AccountKey=5NryBBupvbScggzen7+m1nihPyMqQ28OM0SYW7TOdsuoXg5H5yJRxcJs2kyLyPZ8MmKjGghrOus4+AStxV6k9w==;EndpointSuffix=core.windows.net", container_name="olliblobexample", blob_name="testi.txt")
    
    with open(tiedosto, "rb") as data:
        blob.upload_blob(data)

    return

def downloadBlob(ladattava):
    blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=olliexamplestrg;AccountKey=5NryBBupvbScggzen7+m1nihPyMqQ28OM0SYW7TOdsuoXg5H5yJRxcJs2kyLyPZ8MmKjGghrOus4+AStxV6k9w==;EndpointSuffix=core.windows.net", container_name="olliblobexample", blob_name=ladattava)

    with open("./BlockDestination.txt", "wb") as my_blob:
        blob_data = blob.download_blob()
        blob_data.readinto(my_blob)

    return

def deleteblob(poistettava):
    blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=olliexamplestrg;AccountKey=5NryBBupvbScggzen7+m1nihPyMqQ28OM0SYW7TOdsuoXg5H5yJRxcJs2kyLyPZ8MmKjGghrOus4+AStxV6k9w==;EndpointSuffix=core.windows.net", container_name="olliblobexample", blob_name=poistettava)
    blob.delete_blob()

    return

def deleteblobcontainer(poistettava):
    BLOB_CONTAINER = poistettava
    blob_container = storage_client.blob_containers.delete(
        GROUP_NAME,
        STORAGE_ACCOUNT,
        BLOB_CONTAINER
    )
    print("Delete blob container.\n")    
    return

def createvnet(vnet):
    VIRTUAL_NETWORK_NAME = vnet
    network = network_client.virtual_networks.begin_create_or_update(
        GROUP_NAME,
        VIRTUAL_NETWORK_NAME,
        {
          "address_space": {
            "address_prefixes": [
              "10.0.0.0/16"
            ]
          },
          "location": "westeurope"
        }
    ).result()
    print("Create virtual network:\n{}".format(network))

    return

def createsubnet(vnet,subnet):
    VIRTUAL_NETWORK_NAME = vnet
    SUBNET = subnet
    subnet = network_client.subnets.begin_create_or_update(
        GROUP_NAME,
        VIRTUAL_NETWORK_NAME,
        SUBNET,
        {
          "address_prefix": '10.0.0.0/24'
        }
    ).result()
    print("Create subnet:\n{}".format(subnet))

    return


def deletesubnet(subnet):
    SUBNET = subnet
    subnet = network_client.subnets.begin_delete(
        GROUP_NAME,
        VIRTUAL_NETWORK_NAME,
        SUBNET
    ).result()
    print("Delete subnet.\n")

def deletevnet(vnet):
    VIRTUAL_NETWORK_NAME = vnet
    network_client.virtual_networks.begin_delete(
        GROUP_NAME,
        VIRTUAL_NETWORK_NAME
    ).result()
    print("Delete virtual network.\n")

def listvnets():

    vnet_list = network_client.virtual_networks.list(GROUP_NAME)

    column_width = 40
    print("Vnets".ljust(column_width) + "Location")
    print("-" * (column_width * 2))

    for group in list(vnet_list):

        print(f"{group.name:<{column_width}}{group.location}")
    return
def createnetworkinterface():
    network_client.network_interfaces.begin_create_or_update(
        GROUP_NAME,
        INTERFACE_NAME,
        {
            'location': "westeurope",
            'ip_configurations': [{
                'name': 'MyIpConfig',
                'subnet': {
                    'id': "/subscriptions/397dc614-480f-46f5-a35f-d4e5d10d1095/resourceGroups/olliExample-rg/providers/Microsoft.Network/virtualNetworks/ollivnettesti/subnets/ollisubnet"
                }
            }]
        } 
    ).result()

def create_vm(vmname):
    VIRTUAL_MACHINE_NAME = vmname
    vm = compute_client.virtual_machines.begin_create_or_update(
        GROUP_NAME,
        VIRTUAL_MACHINE_NAME,
        {
            "location": "westeurope",
            "hardware_profile": {
            "vm_size": "Standard_D2_v2"
            },
            "storage_profile": {
            "image_reference": {
                "sku": "2016-Datacenter",
                "publisher": "MicrosoftWindowsServer",
                "version": "latest",
                "offer": "WindowsServer"
            },
            "os_disk": {
                "caching": "ReadWrite",
                "managed_disk": {
                "storage_account_type": "Standard_LRS"
                },
                "name": "myVMosdisk",
                "create_option": "FromImage"
            },
            "data_disks": [
                {
                "disk_size_gb": "1023",
                "create_option": "Empty",
                "lun": "0"
                },
                {
                "disk_size_gb": "1023",
                "create_option": "Empty",
                "lun": "1"
                }
            ]
            },
            "os_profile": {
            "admin_username": "olli",
            "computer_name": VIRTUAL_MACHINE_NAME,
            "admin_password": "Salainen!123",
            "windows_configuration": {
                "enable_automatic_updates": True  # need automatic update for reimage
            }
            },
            "network_profile": {
            "network_interfaces": [
                {
                "id": "/subscriptions/" + SUBSCRIPTION_ID + "/resourceGroups/" + GROUP_NAME + "/providers/Microsoft.Network/networkInterfaces/" + INTERFACE_NAME + "",
                # "id": NIC_ID,
                "properties": {
                    "primary": True
                }
                }
            ]
            }
        }
    ).result()
    print("Create virtual machine:\n{}".format(vm))

def stopvm(Vmname):
    VIRTUAL_MACHINE_NAME = Vmname
    compute_client.virtual_machines.begin_power_off(
        GROUP_NAME,
        VIRTUAL_MACHINE_NAME
    ).result()

def startvm(vmname):
    VIRTUAL_MACHINE_NAME = vmname
    compute_client.virtual_machines.begin_start(
        GROUP_NAME,
        VIRTUAL_MACHINE_NAME
    ).result()




def getsubnet():
    subnet = network_client.subnets.get(
        GROUP_NAME,
        VIRTUAL_NETWORK_NAME,
        SUBNET
    )
    print("Get subnet:\n{}".format(subnet.id))
startvm(VIRTUAL_MACHINE_NAME)