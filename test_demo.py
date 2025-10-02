from extras.scripts import *
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
from typing import Tuple

from dcim.choices import DeviceStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Site, Platform, Interface, Manufacturer, VirtualChassis
from ipam.models import IPAddress, VLAN, VLANGroup 
from extras.models import ConfigTemplate
