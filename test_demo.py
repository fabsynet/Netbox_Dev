from extras.scripts import *
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
from typing import Tuple

from dcim.choices import DeviceStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Site, Platform, Interface, Manufacturer, VirtualChassis
from ipam.models import IPAddress, VLAN, VLANGroup 
from extras.models import ConfigTemplate

CHOICES = (
    ('TenGigabitEthernet1/1/1', 'Te1/1/1'),
    ('TenGigabitEthernet1/1/2', 'Te1/1/2'),
    ('TenGigabitEthernet1/1/3', 'Te1/1/3'),
    ('TenGigabitEthernet1/1/4', 'Te1/1/4'),
    ('TwentyFiveGigabitEthernet1/1/1', 'Twe1/1/1'),
    ('TwentyFiveGigabitEthernet1/1/2', 'Twe1/1/2'),
    ('GigabitEthernet1/1', 'Gi1/1'),
    ('GigabitEthernet1/2', 'Gi1/2'),
)

LAG_CHOICES = (
    ('Po1', 'Po1'),
    ('Po2', 'Po2'),
    ('Po3', 'Po3'),
)

choices1 = (
    ('TenGigabitEthernet1/1/1', 'Te1/1/1'),
    ('TenGigabitEthernet1/1/2', 'Te1/1/2'),
    ('TenGigabitEthernet1/1/3', 'Te1/1/3'),
    ('TenGigabitEthernet1/1/4', 'Te1/1/4'),
)

choices2 = (
    ('GigabitEthernet1/1/1', 'Gi1/1/1'),
    ('GigabitEthernet1/1/2', 'Gi1/1/2'),
    ('TenGigabitEthernet1/1/3', 'Te1/1/3'),
    ('TenGigabitEthernet1/1/4', 'Te1/1/4'),
)

choices3 = (
    ('TwentyFiveGigabitEthernet1/1/1', 'Twe1/1/1'),
    ('TwentyFiveGigabitEthernet1/1/2', 'Twe1/1/2'),
    ('TwentyFiveGigabitEthernet1/1/3', 'Twe1/1/3'),
    ('TwentyFiveGigabitEthernet1/1/4', 'Twe1/1/4'),
)

choices4 = (
    ('GigabitEthernet1/1', 'Gi1/1'),
    ('GigabitEthernet1/2', 'Gi1/2'),
    ('GigabitEthernet1/3', 'Gi1/3'),
    ('GigabitEthernet1/4', 'Gi1/4'),
)

class PlayGround(Script):

    class Meta:
        name = "Device Onboarding Play Ground"
        description = "Provision a New switch to Site"
        commit_default = False
        fieldsets = (
            ('Device Object', ('device_name', 'switch_model', 'mgmt_address', 'gateway_address', 'is_stack_switch')),
            ('Site Object', ('site', 'mgmt_vlan', 'blan_vlan', 'guest_vlan')),
            ('Connected Access Point', ('ap_count',)),
            ('Wired Guest', ('guest_count',)),
            ('Uplink Port 1', ('uplink_1', 'uplink_desc_a',)),
            ('Uplink Port 2', ('uplink_2', 'uplink_desc_b',)),
            ('Lag Interface', ('lag_name', 'lag_desc')),
        )
    
    device_name = StringVar(
        description="Device hostname",
        label='Device Name'
    )
    switch_model = ObjectVar(
        description="Access switch model",
        model=DeviceType,
        label='Device Model'
    )
    site = ObjectVar(
        description="Choose Site name from drop-down",
        model=Site,
        label='Site Name'
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
    mgmt_vlan = IntegerVar(
        description="Mgmt VLAN ID example: 60",
        label='Mgmt VLAN ID',
        default=60,
        min_value=2,
        max_value=4096,
    )
    blan_vlan = IntegerVar(
        description="Business LAN VLAN ID example: 1101",
        label='BLAN VLAN ID',
        min_value=2,
        max_value=4096,
    )
    guest_vlan = IntegerVar(
        description="Guest VLAN ID example: 3101",
        label='Guest VLAN ID',
        min_value=2,
        max_value=4096,
    )
    ap_count = IntegerVar(
        description="Number of access point to be install on the switch",
        label='AP Count',
        required=False,
        min_value=1,
        max_value=10,
    )
    guest_count = IntegerVar(
        description="Number of wired guest users that need access on the switch",
        label='Guest Count',
        required=False,
        min_value=1,
        max_value=10,
    )
    uplink_1 = ObjectVar(
		model=DeviceType
        query_params= {'switch_filter': $switch_model,
						'uplink': DeviceType.objects.get(model=$switch_model).interfacetemplates.filter(type__icontains='SFP')
		}
        description="Uplink Interface drop-down",
        label='Uplink Interface',
    )
    uplink_desc_a = StringVar(
        description="Uplink Port 1 Interface Description",
        label='Uplink Interface Description',
        default='remotehost=os-z07-41ra0043-01-sw-lef-a; port=xe-0/0/18',
    )
    uplink_2 = ChoiceVar(
        choices=CHOICES,
        description="Uplink Interface drop-down",
        label='Uplink Interface',
    )
    uplink_desc_b = StringVar(
        description="Uplink Port 2 Interface Description",
        label='Uplink Interface Description',
        default='remotehost=os-z07-41ra0043-01-sw-lef-b; port=xe-0/0/18'
    )
    lag_name  = ChoiceVar(
        choices=LAG_CHOICES,
        description="Uplink Port 1/2 Lag Interface drop-down. example: Po1/ae1",
        label='Lag Interface Name',
        default='Po1',
    )
    lag_desc = StringVar(
        description="Uplink Port 1/2 Lag Interface description",
        label='Lag Interface Description',
        default='remotehost=os-z07-41ra0043-01-sw-lef-a/b; port=ae18'
    )
    def run(self, data, commit):
        pass



