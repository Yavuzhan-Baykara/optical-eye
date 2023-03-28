class Fabric:
    def __init__(self, name):
        self.name = name
        self.thresholds = {
            'delik': 0.4,
            'leke': 0.4,
            'kirik': 0.4,
            'iplik': 0.4,
            'dikis': 0.4
        }

    def set_threshold(self, error_type, threshold):
        self.thresholds[error_type] = threshold

class SATEN(Fabric):
    def __init__(self):
        super().__init__("SATEN")

class RANFORCE(Fabric):
    def __init__(self):
        super().__init__("RANFORCE")
        self.thresholds['leke'] = 0.5
        
class WF(Fabric):
    def __init__(self):
        super().__init__("WF")

class IF(Fabric):
    def __init__(self):
        super().__init__("IF")

class DC(Fabric):
    def __init__(self):
        super().__init__("DC")

class GB(Fabric):
    def __init__(self):
        super().__init__("GB")

class JF(Fabric):
    def __init__(self):
        super().__init__("JF")
        self.thresholds['delik'] = 0.55
        self.thresholds['leke'] = 0.5
        self.thresholds['kirik'] = 0.5
        self.thresholds['iplik'] = 0.5
        self.thresholds['dikis'] = 0.5

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

# jf = JF()
# jf_thresholds = jf.thresholds
# print(jf_thresholds)