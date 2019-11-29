
class Phone:

    def __init__(self, name, description, extension, alerting_name):
        # AXL
        self.name = name
        if name.startswith('SEP') or name.startswith('ATA'):
            self.mac = name[3:]
        else:
            self.mac = 'unknown'
        self.description = description
        self.extension = extension
        self.alerting_name = alerting_name
        self.device_type = "unknown"

        # RIS
        self.status = "unknown"
        self.timestamp = "unknown"

        # DB
        self.responsible_person = "unknown"
        self.outlet_id = "unknown"
        self.outlet_status = "unknown"
        self.outlet_usedFor = "unknown"

        # Networking
        self.switchport = "unknown"
        self.switchport_status = "unknown"
        self.switchport_power_status = "unknown"
        self.switchport_cabling = "unknown"
        self.switchport_found_mac = "unknown"
        self.switchport_macs = []


    def print_device_axl(self):
        print("{}, {}, {}, {}, {}".format(self.name, self.description, self.extension, self.alerting_name, self.device_type))

    def print_device_ris(self):
        print("{}, {}, {}, {}, {}, {}, {}".format(self.name, self.description, self.extension, self.alerting_name, \
                                                  self.device_type, self.status, self.timestamp))
    def print_device_full(self):
        print("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.name, self.description, self.extension, self.alerting_name,
                                                                      self.device_type, self.status, self.timestamp,
                                                                      self.responsible_person, self.outlet_id, self.outlet_status, self.outlet_usedFor, \
                                                                      self.switchport))

    def print_device_full_net(self):
        print("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.name, self.description, self.extension, self.alerting_name, \
                                                                                  self.device_type, self.status, self.timestamp, \
                                                                                  self.responsible_person, self.outlet_id, self.outlet_status, self.outlet_usedFor, \
                                                                                  self.switchport, self.switchport_status, self.switchport_power_status,
                                                                                  self.switchport_cabling, self.switchport_found_mac, self.switchport_macs))

