
head = ("config firewall service custom")
pro = ('set protocol TCP/UDP/SCTP')
fend= ("end")

f=open('ports.txt', 'r') 



f1 = open('udp.txt','w')
for data in f:
    add=("edit UDP-" + str(data))
    por = ("set udp-portrange " + str(data))
    f1.write(head +'\n')
    f1.write(add)
    f1.write(pro +'\n')
    f1.write(por)
    f1.write(fend +'\n')



    