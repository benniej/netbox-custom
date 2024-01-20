from extras.reports import Report
from dcim.models import Device

class JennyCSLocalContextReport(Report):
    description = "Check if devices with 'jenny-cs' tag contain a local context"

    def test_cs_data(self):

        for device in Device.objects.filter(tags="2"):
            if device.local_context_data:
                self.log_success(device)
            else:
                self.log_failure(device, "Check device name in Netbox and UISP")
