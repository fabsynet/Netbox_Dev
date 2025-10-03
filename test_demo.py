from extras.scripts import *
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
from typing import Tuple

from dcim.choices import DeviceStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Site, Platform, Interface, Manufacturer, VirtualChassis
from ipam.models import IPAddress, VLAN, VLANGroup 
from extras.models import ConfigTemplate



class DeviceOnboarding(Script):

    class Meta:
        name = "Device Onboarding"
        description = "Provision a New switch to Site"
        commit_default = False
    
    device_name = StringVar(
        description="Device hostname",
        label='Device Name'
    )
    switch_model = ObjectVar(
        description="Access switch model",
        model=DeviceType,
        label='Device Model'
    )
    mgmt_address = IPAddressWithMaskVar(
        description="Device Mgmt IP example: 192.168.20.10/23",
        label='Mgmt IP Address'
    )
    gateway_address = StringVar(
        description="Default Gateway. example: 10.10.10.1",
        label='Default Gateway',
    )
    is_stack_switch = BooleanVar(
        description="Is this a stack switch",
        default=False,
        label='is_stack',
    )


    def run(self, data, commit):
        pass
