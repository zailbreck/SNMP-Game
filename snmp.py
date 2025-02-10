import subprocess

# Static values
IP = "192.168.19.2"
COMMUNITY = "zabbix_new"
OID = ".1.3.6.1.2.1.2.2.1.7.11" # Eth 6

def snmp_set(oid, value):
    cmd = ["bin/SnmpSet.exe", f"-r:{IP}", "-v:2c", f"-c:{COMMUNITY}", f"-o:{oid}",  f"-val:{value}", f"-tp:int"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print("SNMP SET Result:", result.stdout)

if __name__ == "__main__":
    value = int(input("1: Enable, 2: Disable: "))
    snmp_set(OID, value)