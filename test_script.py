from extras.scripts import *
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType

from dcim.choices import DeviceStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Site, Platform, Interface, Manufacturer
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

class AddDevices(Script):

    class Meta:
        name = "Add New Device To Site"
        description = "Provision a New switch to Site"
        commit_default = False
        fieldsets = (
            ('Device Object', ('device_name','switch_model'))
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
