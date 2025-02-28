import json 

with open('C:\Code\python-files\python-univ\Lab4\sample-data.json', 'r') as file:
    parsed_f = json.load(file)
print("Interface status")
print("=" * 70)
print("DN", " " * 40, "Description", " " * 10, "Speed", "  ", "MTU")
print("-" * 42, "-" * 22, "-" * 5, " ", "-" * 5,)
for x in parsed_f.get("imdata"):
    print(x.get("l1PhysIf").get("attributes").get("dn"), end=" ")
    if(x.get("l1PhysIf").get("attributes").get("descr") == ""):
        print(" " * 20, end=" ")
    else:
        print(x.get("l1PhysIf").get("attributes").get("descr"), end=" ")
    print(x.get("l1PhysIf").get("attributes").get("speed"), end=" ")
    print(x.get("l1PhysIf").get("attributes").get("mtu"))