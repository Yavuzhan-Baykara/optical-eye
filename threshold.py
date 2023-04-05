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
    def set_threshold(self, error_type, threshold):
        self.thresholds[error_type] = threshold

class SATEN(Fabric):
    def __init__(self):
        super().__init__("SATEN")
        self.thresholds['delik'] = 0.5
        self.thresholds['leke'] = 0.5

class RANFORCE(Fabric):
    def __init__(self):
        super().__init__("RANFORCE")
        self.thresholds['leke'] = 0.5
        self.thresholds['delik'] = 0.45
        
class WF(Fabric):
    def __init__(self):
        super().__init__("WF")
        self.thresholds['delik'] = 0.65
        self.thresholds['leke'] = 0.5

class IF(Fabric):
    def __init__(self):
        super().__init__("IF")
        self.thresholds['delik'] = 0.69
        self.thresholds['leke'] = 0.5

class DC(Fabric):
    def __init__(self):
        super().__init__("DC")
        self.thresholds['delik'] = 0.5
        self.thresholds['leke'] = 0.5

class GB(Fabric):
    def __init__(self):
        super().__init__("GB")
        self.thresholds['delik'] = 0.45
        self.thresholds['leke'] = 0.5

class JF(Fabric):
    def __init__(self):
        super().__init__("JF")
        self.thresholds['delik'] = 0.69
        self.thresholds['leke'] = 0.5
        self.thresholds['kirik'] = 0.5
        self.thresholds['iplik'] = 0.5

def selected_Fabric(item):
    options = {
        "JF": JF,
        "GB": GB,
        "DC": DC,
        "IF": IF,
        "WF": WF,
        "RANFORCE(RA-RF-RI-RS-RN-IR) ": RANFORCE,
        "SATEN(IS-SN)": SATEN
    }
    return options[item]().thresholds
