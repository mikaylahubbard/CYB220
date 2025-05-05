#! /usr/bin/env python
from scapy.all import sniff
from tkinter import ttk, filedialog
import tkinter
from threading import Thread
from PIL import Image, ImageGrab
import io
import img2pdf


class PacketGUI:
    def __init__(self, root):
     
        self.num_captures=0
        #create a frame for the text
        self.textFrame = ttk.Frame(root)
        #add columns to the frame - 2 equal columns
        self.textFrame.columnconfigure(0, weight = 2)
        self.textFrame.columnconfigure(1, weight = 2)

        # put a label into the frame
        self.text = ttk.Label(self.textFrame, wraplength=500, anchor="center",
                     text = "Choose a Protocol below to sniff and recieve your packet!")
        #grid it in into the frame, with a columnspan so it is centered
        self.text.grid(row=0, column=0, columnspan = 2, sticky = "wens", padx=70, pady=20)

        #pack the text frame
        self.textFrame.pack()

        #button frame - like the textFrame, but 3 equal cols
        self.btnFrame = ttk.Frame(root)
        self.btnFrame.columnconfigure(0, weight = 1)
        self.btnFrame.columnconfigure(1, weight=1)
        self.btnFrame.columnconfigure(2, weight=1)

        #create and gird 3  buttons: for tcp, udp, or icmp - we can add more later?
        self.b1 = ttk.Button(self.btnFrame, padding=10, text="tcp", command = lambda:self.startSniffing('tcp'))
        self.b2 = ttk.Button(self.btnFrame, padding=10, text="udp", command = lambda:self.startSniffing('udp'))
        self.b3 = ttk.Button(self.btnFrame, padding=10, text="icmp", command = lambda:self.startSniffing('icmp'))
    
        #grid in the buttons
        self.b1.grid(row=0, column=0, sticky="wens", padx=10)
        self.b2.grid(row=0, column=1, sticky="wens", padx=10)
        self.b3.grid(row=0, column=2, sticky="wens", padx=10)

        self.btnFrame.pack()

        #import button
        self.importFrame = ttk.Frame(root)
        self.importFrame.columnconfigure(0, weight=2)
        self.importFrame.columnconfigure(1, weight=2)

        self.importBtn = ttk.Button(self.importFrame, padding=10, text="Import PCAP",
                                    command = lambda:self.importPcap())
        self.importBtn.grid(row=0, column=0, columnspan=2, sticky="wens", padx=10, pady=10)

        self.importFrame.pack()


        #another text frame for updates or titles
        self.textFrame2 = ttk.Frame(root)

        self.textFrame2.columnconfigure(0, weight = 2)
        self.textFrame2.columnconfigure(1, weight = 2)

        self.message = ttk.Label(self.textFrame2, text = "", anchor = "center")
        self.message.grid(row=0, column=0, columnspan = 2, sticky = "wens", padx=70, pady=20)


        self.textFrame2.pack()

        
   
        #create the table frame, with columns for the different table columns/bits
        self.tblFrame = ttk.Frame(root)
        for i in range(33):
            self.tblFrame.columnconfigure(i, weight=1)

        # labels


        self.c1 = ttk.Label(self.tblFrame, text = "Bit offset", anchor="center", borderwidth=2, relief=         "solid")
        self.c2 = ttk.Label(self.tblFrame, text="0-3", anchor="center", borderwidth=2, relief="solid")
        self.c3 = ttk.Label(self.tblFrame, text="4-7", anchor="center", borderwidth=2, relief="solid")
        self.c4 = ttk.Label(self.tblFrame, text="8-15", anchor="center", borderwidth=2, relief="solid")
        self.c5 = ttk.Label(self.tblFrame, text="16-18", anchor="center", borderwidth=2, relief="solid"         )
        self.c6 = ttk.Label(self.tblFrame, text="19-31", anchor="center", borderwidth=2, relief="solid"         )
        self.c1.grid(row=0, column=0, sticky="wens", ipady=10)
        self.c2.grid(row=0, column=1, columnspan=4, sticky="wens", ipady=10)
        self.c3.grid(row=0, column=5, columnspan=4, sticky="wens", ipady=10)
        self.c4.grid(row=0, column=9, columnspan=8, sticky="wens", ipady=10)
        self.c5.grid(row=0, column=17, columnspan=3,  sticky="wens", ipady=10)
        self.c6.grid(row=0, column=20, columnspan=13, sticky="wens", ipady=10)

        #self.tblFrame.pack(expand=True, fill="both", pady=10, padx=10)   


        #Reset btn grid + image save button
        self.rFrame = ttk.Frame(root)

        self.rFrame.columnconfigure(0, weight = 2)
        self.rFrame.columnconfigure(1, weight = 2)

        self.rBtn = ttk.Button(self.rFrame, padding=10, text="Reset", command = lambda:self.reset())
        self.saveBtn = ttk.Button(self.rFrame, padding=10, text="Save as png", command = lambda:self.capture_widget(self.tblFrame))

        self.rBtn.grid(row=0, column=0, sticky = "wens", padx=70, pady=20)
        self.saveBtn.grid(row=0, column=1, sticky="wens", padx=70, pady=20)

        self.rFrame.pack(side="bottom")



    
    def importPcap(self):
        filename = filedialog.askopenfilename(title="Select a PCAP")
        try:
            sniff(offline=filename, prn=self.display, store=0, count=1)
        except:
            print("cannot read file")
            pass
        
    
    def reset(self):
        self.tblFrame.pack_forget() 
        self.message.config(text="")
        self.saveBtn.configure(text="Save as png")


    def startSniffing(self, filter):
        self.message.config(text="sniffing...")
        self.message.update_idletasks()
        def sniffPackets(self, filter):
            sniff(filter=filter, prn=self.display, count=1)
            self.message.config(text="IP Header:")
        Thread(target=sniffPackets, args=(self, filter), daemon=True).start()


    def display(self, packet):
        print("displaying graph of captured packet")
        print(packet.show(dump=True))
        #cinfigure the captured data 

        #row1

        self.rc11 = ttk.Label(self.tblFrame, text = "0", anchor="center", 
                              borderwidth=2,relief = "solid")
        self.rc12 = ttk.Label(self.tblFrame, text = f"Version: {packet.version}", anchor="center", 
                              borderwidth=2,relief = "solid")
        self.rc13 = ttk.Label(self.tblFrame, text = f"HDR Length: {packet.ihl}", anchor="center", 
                              borderwidth=2,relief = "solid")
        self.rc14 = ttk.Label(self.tblFrame, text = f"Type of Service: {packet.tos}", anchor="center", 
                              borderwidth=2,relief = "solid")
        self.rc15 = ttk.Label(self.tblFrame, text=f"Total Length: {packet.len}", anchor="center",
                              borderwidth=2, relief = "solid")

        self.rc11.grid(row=1, column=0, sticky="wens", ipady=10)
        self.rc12.grid(row=1, column=1, columnspan=4, sticky="wens", ipady=10)
        self.rc13.grid(row=1, column=5, columnspan=4, sticky="wens", ipady=10)
        self.rc14.grid(row=1, column=9, columnspan=8, sticky="wens", ipady=10)
        self.rc15.grid(row=1, column=17, columnspan=16, sticky="wens", ipady=10)

        #row2 
        self.rc21 = ttk.Label(self.tblFrame, text = "32", anchor="center", 
                              borderwidth=2,relief = "solid")
        self.rc22 = ttk.Label(self.tblFrame, text = f"ID: {packet.id}", anchor="center", 
                              borderwidth=2,relief = "solid")
        self.rc23 = ttk.Label(self.tblFrame, text = f"Flags: {packet.flags}", anchor="center", 
                              borderwidth=2,relief = "solid")
        self.rc24 = ttk.Label(self.tblFrame, text = f"Fragment Offset: {packet.frag}", anchor="center",
                              borderwidth=2,relief = "solid")


        self.rc21.grid(row=2, column=0, sticky="wens", ipady=10)
        self.rc22.grid(row=2, column=1, columnspan=16, sticky="wens", ipady=10)
        self.rc23.grid(row=2, column=17, columnspan=3, sticky="wens", ipady=10)
        self.rc24.grid(row=2, column=20, columnspan=13, sticky="wens", ipady=10)

        #row3
        self.rc31 = ttk.Label(self.tblFrame, text = "64", anchor="center", 
                              borderwidth=2,relief = "solid")
        self.rc32 = ttk.Label(self.tblFrame, text = f"Time to Live: {packet.ttl}", anchor="center", 
                              borderwidth=2,relief = "solid")
        self.rc33 = ttk.Label(self.tblFrame, text = f"Protocol: {packet.proto}", anchor="center", 
                              borderwidth=2,relief = "solid")
        self.rc34 = ttk.Label(self.tblFrame, text = f"Header Checksum: {packet.chksum}", anchor="center",
                              borderwidth=2,relief = "solid")


        self.rc31.grid(row=3, column=0, sticky="wens", ipady=10)
        self.rc32.grid(row=3, column=1, columnspan=8, sticky="wens", ipady=10)
        self.rc33.grid(row=3, column=9, columnspan=8, sticky="wens", ipady=10)
        self.rc34.grid(row=3, column=17, columnspan=16, sticky="wens", ipady=10)


        #row4
        
        self.rc41 = ttk.Label(self.tblFrame, text = "96", anchor="center", 
                              borderwidth=2,relief = "solid")
        self.rc42 = ttk.Label(self.tblFrame, text = f"Source IP Adress: {packet[0][1].src}", 
                              anchor="center", 
                              borderwidth=2,relief = "solid")


        self.rc41.grid(row=4, column=0, sticky="wens", ipady=10)
        self.rc42.grid(row=4, column=1, columnspan=32, sticky="wens", ipady=10)

        


        #row5
        self.rc51 = ttk.Label(self.tblFrame, text = "128", anchor="center", 
                              borderwidth=2,relief = "solid")
        self.rc52 = ttk.Label(self.tblFrame, text = f"Destination IP Adress: {packet[0][1].dst}", 
                              anchor="center", 
                              borderwidth=2,relief = "solid")


        self.rc51.grid(row=5, column=0, sticky="wens", ipady=10)
        self.rc52.grid(row=5, column=1, columnspan=32, sticky="wens", ipady=10)


        #row6 - needs to be unique for the different protocols
        self.rc61 = ttk.Label(self.tblFrame, text = "160", anchor="center", 
                              borderwidth=2,relief = "solid")
        self.rc62 = ttk.Label(self.tblFrame, text = f"Options: {packet[0][1].options}", 
                              anchor="center", 
                              borderwidth=2,relief = "solid")


        self.rc61.grid(row=6, column=0, sticky="wens", ipady=10)
        self.rc62.grid(row=6, column=1, columnspan=32, sticky="wens", ipady=10)



        #pack table frame
        self.tblFrame.pack(expand=True, fill="both", pady=10, padx=10)
        

    def capture_widget(self, widget):
        widget.update()
        widget.focus()

        x0 = widget.winfo_rootx()
        y0 = widget.winfo_rooty()
        x1 = x0 + widget.winfo_width()
        y1 = y0 + widget.winfo_height()

        img = ImageGrab.grab((x0, y0, x1, y1))
        #return img
        img.save(f"packet{self.num_captures}.png")
        self.num_captures = self.num_captures + 1
        self.saveBtn.configure(text="saved!")


if __name__ == '__main__':
    #startSniffing("tcp")
    root = tkinter.Tk()
    root.geometry("800x600")
    display = PacketGUI(root=root)
    root.mainloop()
