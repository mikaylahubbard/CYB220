from scapy.all import sniff                                                    
                                                                               
def packet_callback(packet):                                                   
    print(packet.show())                                                       
                                                                               
def main():                                                                    
    sniff(filter="port 443 and host andersonuniversity.edu", prn=packet_callback, count = 10)                                                                 
                                                                               
if __name__ == '__main__':                                                     
    main()    
