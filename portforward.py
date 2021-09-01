import os
import configparser


#Reset all iptables
os.system("iptables -F")
os.system("iptables -t nat -F")
os.system("iptables -t mangle -F")
os.system("iptables -P INPUT ACCEPT")
os.system("iptables -P FORWARD ACCEPT")
os.system("iptables -P OUTPUT ACCEPT")

#I use wlp2s0 as my interface
#read text file and craft text commands to make masquerade rules
#interfacename
#interfaces = []
with open("interfaces.txt") as fp1:
    for line in fp1:
        #interface = "iptables -A POSTROUTING -t nat -o interfaceName -j MASQUERADE"
        interface = "iptables -A POSTROUTING -t nat -o " + line + " -j MASQUERADE"
        print(interface)
        os.system(interface)
        #interfaces.append(interface)

#read text file and craft the text commands to make prerouting rules for port forwarding
#srcNIC srcIP srcDport dstIP dstDport 
#rules = []
with open("forward.txt") as fp2:
    for line in fp2:
        p = line.split()
        #[0] = srcIP, [1] = srcDport, [2] = dstIP, [3] = dstDport
        #rule = "iptables -A PREROUTING -t nat -s " + srcIP + " -p tcp --dport " + srcDport + " -j DNAT --to-destination " + dstIP + ":" + dstDport
        #rule = "iptables -A PREROUTING -t nat -s " + p[0] + " -p tcp --dport " + p[1] + " -j DNAT --to-destination " + p[2] + ":" + p[3]
        rule = "iptables -A PREROUTING -t nat -s " + p[0] + " -p tcp --dport " + p[1] + " -j DNAT --to-destination " + p[2] + ":" + p[3]
        print(rule)
        os.system(rule)
        #rules.append(rule)

