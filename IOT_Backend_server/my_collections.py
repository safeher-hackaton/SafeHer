class Device:

    def __init__(self, doc=None):
        if doc:
            self.SSID = doc.get('SSID', '')
            self.Owner = doc.get('Owner', '')
            self.Type = doc.get('Type', '')
        else:
            self.SSID = ""
            self.Owner = ""
            self.Type = ""

    @staticmethod
    def list_from_doc(doc):
        if doc is None:
            return []
        devices = []
        for device in doc:
            devices.append(Device(device))
        return devices

    def to_json(self):
        return {
            "SSID": self.SSID,
            "Owner": self.Owner,
            "Type": self.Type,
        }

    def to_dict(self):
        return self.to_json()


class Contact:

    def __init__(self, doc=None):
        if doc:
            self.first_name = doc.get("first_name")
            self.last_name = doc.get("last_name")
            self.phone = doc.get("phone")
        else:
            self.first_name = ""
            self.last_name = ""
            self.phone = "+972503305021"

    @staticmethod
    def list_from_doc(doc):
        if doc is None:
            return []
        contacts = []
        for contact in doc:
            contacts.append(Contact(contact))
        return contacts

    def to_json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
        }

    def to_dict(self):
        return self.to_json()


class User:
    def __init__(self, doc: dict = None):
        if doc is not None:
            self.username = doc.get('username', '')
            self.password = doc.get('password', '')
            self.first_name = doc.get('first_name', '')
            self.last_name = doc.get('last_name', '')
            self.id = doc.get('id', '')
            self.device = Device.list_from_doc(doc.get('devices', None))
            self.address = doc.get('address', '')
            self.emergency_contacts = Contact.list_from_doc(doc.get('contacts', None))
            self.phone = doc.get('phone', '')
            self.safe_word = doc.get('safe', '')
            self.last_call = doc.get('last_alert', '')
        else:
            self.username = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
            self.id = ""
            self.device = []
            self.address = ""
            self.emergency_contacts = []
            self.phone = ""
            self.safe_word = ""
            self.last_call = ""

    def to_json(self):
        j_devices = []
        j_contact = []
        for d in self.device:
            j_devices.append(d.to_dict())
        for c in self.emergency_contacts:
            j_contact.append(c.to_dict())

        return {
            'username': self.username,
            'password': self.password,
            'id': self.id,
            'phone': self.phone,
            'safe': self.safe_word,
            'devices': j_devices,
            'address': self.address,
            'contacts': j_contact,
            'first_name': self.first_name,
            'last_name': self.last_name,
        }

    def to_dict(self):
        return self.to_json()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
