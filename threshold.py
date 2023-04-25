class Fabric:
    def __init__(self, name):
        self.name = name
        self.thresholds = {
            'delik': 0.4,
            'leke': 0.4,
            'kirik': 0.4,
            'iplik': 0.4,
            'dikis': 0.6
        }
        self.error_types = []
    def set_threshold(self, error_type, threshold):
        self.thresholds[error_type] = threshold

class SATEN(Fabric):
    def __init__(self):
        super().__init__("SATEN")
        self.thresholds['delik'] = 0.5
        self.thresholds['leke'] = 0.5
        self.error_types = ['delik', 'kirik']

class PI(Fabric):
    def __init__(self):
        super().__init__("SATEN")
        self.thresholds['delik'] = 0.5
        self.thresholds['leke'] = 0.5
        self.error_types = ['delik', 'kirik']

class IV(Fabric):
    def __init__(self):
        super().__init__("IV")
        self.thresholds['delik'] = 0.5
        self.thresholds['leke'] = 0.5
        self.thresholds['dikis'] = 0.52
        self.error_types = ['delik', 'kirik']

class RANFORCE(Fabric):
    def __init__(self):
        super().__init__("RANFORCE")
        self.thresholds['leke'] = 0.5
        self.thresholds['delik'] = 0.45
        self.error_types = ['delik', 'kirik']
        
class WF(Fabric):
    def __init__(self):
        super().__init__("WF")
        self.thresholds['delik'] = 0.67
        self.thresholds['leke'] = 0.5
        self.error_types = ['kirik']

class IF(Fabric):
    def __init__(self):
        super().__init__("IF")
        self.thresholds['delik'] = 0.69
        self.thresholds['leke'] = 0.5
        self.error_types = ['kirik']

class DC(Fabric):
    def __init__(self):
        super().__init__("DC")
        self.thresholds['delik'] = 0.5
        self.thresholds['leke'] = 0.5
        self.error_types = ['kirik']

class DD(Fabric):
    def __init__(self):
        super().__init__("DD")
        self.thresholds['delik'] = 0.5
        self.thresholds['leke'] = 0.5
        self.error_types = ['kirik']

class GB(Fabric):
    def __init__(self):
        super().__init__("GB")
        self.thresholds['delik'] = 0.45
        self.thresholds['leke'] = 0.5
        self.error_types = ['delik', 'kirik']

class JF(Fabric):
    def __init__(self):
        super().__init__("JF")
        self.thresholds['delik'] = 0.69
        self.thresholds['leke'] = 0.5
        self.thresholds['kirik'] = 0.5
        self.thresholds['iplik'] = 0.5
        self.error_types = ['kirik']

class FL(Fabric):
    def __init__(self):
        super().__init__("FL")
        self.thresholds['delik'] = 0.6
        self.thresholds['leke'] = 0.5
        self.thresholds['kirik'] = 0.5
        self.thresholds['iplik'] = 0.5
        self.error_types = ['kirik']

class BF(Fabric):
    def __init__(self):
        super().__init__("FL")
        self.thresholds['delik'] = 0.6
        self.thresholds['leke'] = 0.5
        self.thresholds['kirik'] = 0.5
        self.thresholds['iplik'] = 0.5
        self.error_types = ['kirik']


def selected_Fabric(item):
    options = {
        "JF": JF,
        "GB": GB,
        "DC": DC,
        "IF": IF,
        "WF": WF,
        "FL": FL,
        "RANFORCE(RA-RF-RI-RS-RN-IR) ": RANFORCE,
        "SATEN(IS-SN)": SATEN,
        "IV": IV,
        "DD": DD,
        "BF": BF,
        "PI": PI,
    }
    fabric_instance = options[item]()
    return fabric_instance.thresholds, fabric_instance.error_types
