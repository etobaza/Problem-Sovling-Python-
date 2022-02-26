import json

file = open("data.json")
dict = json.load(file)
imdata = dict["imdata"]

print(
    "============================================================================" "\n"
    "DN                                 Description       Speed           MTU" "\n"
    "----------------------------------------------------------------------------")

for i in imdata:
    dn = i["l1PhysIf"]["attributes"]["dn"]
    descr = i["l1PhysIf"]["attributes"]["descr"]
    speed = i["l1PhysIf"]["attributes"]["speed"]
    mtu = i ["l1PhysIf"]["attributes"]["mtu"]
    print("{0:5} {1:10} {2:15} {3:20}".format(dn, descr, speed, mtu))