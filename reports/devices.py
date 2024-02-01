import re

from extras.reports import Report
from dcim.models import Device

class JENNY_Radio_Sector(Report):
    description = "Check various attributes on a Jenny Customer Sector"

    def test_JRS_device_primary_IP(self):

        for device in Device.objects.filter(tags="2"):
            if device.primary_ip:
                self.log_success(device)
            else:
                self.log_failure(device, "Check device primary IP")

    def test_JRS_device_naming(self):

        for device in Device.objects.filter(tags="2"):
            if re.match("^J-[A-Z0-9]{3}-CZ2[0-5][0-9]-(?:UBT|LTU|WAV|MIK|MIM|CAM|RAD|OLT)-[5-9][0-9]\.[0-9]{0,3}(?:-[a-zA-Z0-9_-]*)?", str(device.name)):
                self.log_success(device)
            else:
                self.log_failure(device, "Check device name")

    def test_JRS_wireless_details_exist(self):

        for device in Device.objects.filter(tags="2"):
            if device.local_context_data:
                self.log_success(device)
            else:
                self.log_failure(device, "Check device name in Netbox and UISP")
