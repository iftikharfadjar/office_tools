import pandas as pd

def rewrite_components(module):
    result = "NA"
    if module is None:
        return result

    match module:
        case m if "proxy" in m.lower():
            result = "HSM-PROXY"
        case m if "admin" in m.lower():
            result = "HSM-EADMIN"
        case m if "cps" in m.lower():
            result = "HSM-CPS"
        case m if "pkcs" in m.lower():
            result = "HSM-PKCS#11"
        case m if "fips" in m.lower():
            result = "HSM-FIPS"
        case m if "kmv2" in m.lower():
            result = "HSM-KMv2"
        case m if "factory" in m.lower():
            result = "HSM-FACTORYTOOL"
        case _:
            result = "NA"
    return result

def rewrite_estimation(estimate):
    return pd.to_numeric(estimate, errors='coerce') * 8 * 60 * 60

def dod(next=""):
    return f""" Definition Of Done :
- SRS/Design/Specification doc is updated
- Code implementation/Test scenario is reviewed by Tech Lead or Architect
- Unit test by developer is passed
- All known issues/JIRA tickets raised in this sprint are analyzed (no Open JIRA ticket, no Critical/Blocking issue)

Acceptance Criteria :
- {next}
"""


def rewrite_description(desc):
    # print(f"type desc = {desc} and type desc {type(desc)}")
    if type(desc) is str:
        if "refer to dod" in desc.lower():
            return  dod()
        else:
            return dod(desc)

def rewrite_assignee(name):
    result = "NA"
    if type(name) is not str:
        return result

    # print(f"type desc = {name} and type desc {type(name)}")
    match name:
        case m if "faizal" in m.lower():
            result = "faizanur"
        case m if "krisna" in m.lower():
            result = "krisnwij"
        case m if "dean" in m.lower():
            result = "MohamAJI"
        case m if "ulima" in m.lower():
            result = "ulimaaza"
        case m if "lukman" in m.lower():
            result = "lukmahak"
        case m if "ulil" in m.lower():
            result = "AhmadAMR"
        case m if "nauval" in m.lower():
            result = "nauvaSHA"
        case m if "ecryna" in m.lower():
            result = "ecrynhut"
        case m if "radip" in m.lower():
            result = "RadipCAN"
        case m if "radit" in m.lower():
            result = "radithen"
        case m if "dewi" in m.lower():
            result = "dewilest"
        case m if "iyas" in m.lower():
            result = "suriyrat"
        case m if "adam" in m.lower():
            result = "AdamRION"
        case m if "etha" in m.lower() or "maretha" in m.lower():
            result = "maretvel"
        case m if "windy" in m.lower():
            result = "windymer"
        case m if "sultan" in m.lower():
            result = "SultaZUH"
        case m if "raja" in m.lower():
            result = "rajabatu"
        case m if "nuzul" in m.lower():
            result = "NuzulRAM"
        case m if "danny" in m.lower():
            result = "dannypat"
        case m if "rud" in m.lower():
            result = "rudyarud"
        case m if "yuh" in m.lower():
            result = "ghayuput"
        case m if "budi" in m.lower():
            result = "budimsan"
        case m if "fadjar" in m.lower():
            result = "fadjaift"
        case m if "gita" in m.lower():
            result = "gitaputr"
        case m if "dihanto" in m.lower():
            result = "dihandih"
        case m if "yosef" in m.lower():
            result = "yosefkur"
        case m if "enha" in m.lower():
            result = "nurhaang"
        case m if "malik" in m.lower():
            result = "wicakmal"
        case m if "ilham" in m.lower():
            result = "ilhamHAM"
        case _:
            result = "NA"
    return result