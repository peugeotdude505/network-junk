from tkinter import *
from tkinter import scrolledtext,filedialog
from jinja2 import Environment, FileSystemLoader, Template
import csv
import os

MenuLabel_1 = 'L2 VLAN'
MenuLabel_2 = 'L2 Switchports'
MenuLabel_3 = 'L3 Interfaces'
MenuLabel_4 = 'Baseline Config for Device'
MenuLabel_5 = 'BGP Neighbor'
MenuLabel_6 = 'Generic Single Element'
MenuLabel_7 = 'Generic Multiple Items from CSV'
MenuLabel_8 = 'S2S VPN'

Subfolder = os.getcwd() + '\\templates\\'
TemplateFile_1 = 'single-vlan.j2'
TemplateFile_2 = 'switchport-interface.j2'
TemplateFile_3 = 'l3-interface.j2'
TemplateFile_4 = 'device-base.j2'
TemplateFile_5 = 'bgp-neighbor.j2'
TemplateFile_6 = 'single-generic.j2'
TemplateFile_7 = 'csv-generic.j2'
TemplateFile_8 = 'vpn.j2'

def mb1_clicked():

	def renderTemplate():
	#Calls the Jinja template function
		GeneratedConfig = VLANTemplate(vlanID.get(),vlanDesc.get(),mode.get(),type.get(),vlanAssoc.get())
	#Clears the text box	
		OutputText.delete(1.0,END)
		OutputText.insert(INSERT,GeneratedConfig)
		
	def closeWindow():
		subwindow.withdraw()
		
	def openTemplateFile():
	#Open the Jinja template for viewing/editing
		os.startfile(Subfolder + TemplateFile_1)

	#Open a new window for this 	
	subwindow = Toplevel()
	subwindow.title(MenuLabel_1)
	#Add items to the new window
	sublabel = Label(subwindow, text=MenuLabel_1, font=("Arial Bold",10))
	vlanID_label = Label(subwindow, text="VLAN ID(1-4096):")
	vlanDesc_label = Label(subwindow, text="VLAN Name(max 32 chars):")
	text3_label = Label(subwindow, text="Mode:")
	text4_label = Label(subwindow, text="PVLAN Type:")
	vlanAssoc_label = Label(subwindow, text="If Primary, What is Secondary VLAN association?:")
	mode = IntVar()
	mode.set(1)
	mode1 = Radiobutton(subwindow,text="FabricPath", value=1, variable=mode)
	mode2 = Radiobutton(subwindow,text="Normal", value=0, variable=mode)
	type = IntVar()
	type.set(0)
	typeN = Radiobutton(subwindow,text="Normal",value=0, variable=type)
	typePR = Radiobutton(subwindow,text="Primary",value=1, variable=type)
	typeIS = Radiobutton(subwindow,text="Secondary Isolated",value=2, variable=type)
	typeCO = Radiobutton(subwindow,text="Secondary Community",value=3, variable=type)
	vlanID = Entry(subwindow,width=5)
	vlanDesc = Entry(subwindow,width=20)
	vlanAssoc = Entry(subwindow,width=5)
	Generate = Button(subwindow, text="Generate",command=renderTemplate)
	GoBack = Button(subwindow, text="Back to Main",command=closeWindow)
	ShowTemplate = Button(subwindow, text="View/Edit J2 template",command=openTemplateFile)
	OutputText = scrolledtext.ScrolledText(subwindow,width=80,height=10)
	#layout the elements on a grid pattern
	OutputText.grid(columnspan=2,column=0, row=7)
	sublabel.grid(column=0, row=0)
	vlanID_label.grid(column=0,row=1)
	vlanDesc_label.grid(column=0,row=2)
	text3_label.grid(column=0,row=3)
	text4_label.grid(column=0,row=4)
	vlanAssoc_label.grid(column=0,row=5)
	vlanID.grid(column=1, row=1)
	vlanDesc.grid(column=1,row=2)
	vlanAssoc.grid(column=1,row=5)
	mode1.grid(column=1,row=3)
	mode2.grid(column=2, row=3)
	typeN.grid(column=1,row=4)
	typePR.grid(column=2,row=4)
	typeIS.grid(column=3,row=4)
	typeCO.grid(column=4,row=4)
	Generate.grid(column=0,row=6)
	ShowTemplate.grid(column=1,row=6)
	GoBack.grid(column=2,row=6)
	subwindow.mainloop()
	
def mb2_clicked():

	#Default selection for input file - Comma Seperated Values
	source_file = "switch-ports.csv"
	
	def selectCSV():
		subwindow.filename = filedialog.askopenfilename(title = "Select Input File",filetypes = (("Comma Seperated Values","*.csv"),("all files","*.*")))
		sel_csv_file = subwindow.filename
		text1.delete(0,END)
		text1.insert(INSERT,sel_csv_file)
			
	def renderTemplate():
	#Calls the Jinja template function
		myCSV = text1.get()
		GeneratedConfig = SwitchPortTemplate(myCSV)
	#Clears the text box	
		OutputText.delete(1.0,END)
		OutputText.insert(INSERT,GeneratedConfig)
		
	def closeWindow():
		subwindow.withdraw()
		
	def openTemplateFile():
	#Open the Jinja template for viewing/editing
		os.startfile(Subfolder + TemplateFile_2)
	
	#Open a new window for this 
	subwindow = Toplevel()
	subwindow.title(MenuLabel_2)
	#Add items to the new window
	sublabel = Label(subwindow, text=MenuLabel_2 + ": Configure from .CSV file", font=("Arial Bold",10))
	text1_label = Label(subwindow, text="Select CSV file")
	mode = IntVar()
	mode.set(1)
	mode1 = Radiobutton(subwindow,text="Nexus", value=1, variable=mode)
	mode2 = Radiobutton(subwindow,text="Regular IOS", value=0, variable=mode)
	text1 = Entry(subwindow,width=20)
	text1.insert(INSERT,source_file)
	SelectFile = Button(subwindow, text="Select Input File",command=selectCSV)
	Generate = Button(subwindow, text="Generate",command=renderTemplate)
	GoBack = Button(subwindow, text="Back to Main",command=closeWindow)
	ShowTemplate = Button(subwindow, text="View/Edit J2 template",command=openTemplateFile)
	OutputText = scrolledtext.ScrolledText(subwindow,width=80,height=50)
	#layout the elements on a grid pattern
	OutputText.grid(columnspan=3,column=0, row=7)
	sublabel.grid(column=0, row=0)
	text1_label.grid(column=0,row=1)
	text1.grid(column=1, row=1)
	mode1.grid(column=1,row=3)
	mode2.grid(column=2, row=3)
	SelectFile.grid(column=0,row=6)
	Generate.grid(column=1,row=6)
	ShowTemplate.grid(column=2,row=6)
	GoBack.grid(column=3,row=6)
	subwindow.mainloop()
	
def mb3_clicked():


	#Default selection for input file - Comma Seperated Values
	source_file	= "l3-interfaces.csv"
	
	def selectCSV():
		subwindow.filename = filedialog.askopenfilename(title = "Select Input File",filetypes = (("Comma Seperated Values","*.csv"),("all files","*.*")))
		sel_csv_file = subwindow.filename
		text1.delete(0,END)
		text1.insert(INSERT,sel_csv_file)
		
	def renderTemplate():
	#Calls the Jinja template function
		myCSV = text1.get()
		GeneratedConfig = L3PortTemplate(myCSV)
	#Clears the text box	
		OutputText.delete(1.0,END)
		OutputText.insert(INSERT,GeneratedConfig)
		
	def closeWindow():
		subwindow.withdraw()
			
	def openTemplateFile():
		#Open the Jinja template for viewing/editing
		os.startfile(Subfolder + TemplateFile_3)
	
	
	#Open a new window for this 
	subwindow = Toplevel()
	subwindow.title(MenuLabel_3)
	#Add items to the new window
	sublabel = Label(subwindow, text=MenuLabel_3 + ": Configure from .CSV file", font=("Arial Bold",10))
	text1_label = Label(subwindow, text="Select CSV file")
	mode = IntVar()
	mode.set(1)
	mode1 = Radiobutton(subwindow,text="Nexus", value=1, variable=mode)
	mode2 = Radiobutton(subwindow,text="Regular IOS", value=0, variable=mode)
	text1 = Entry(subwindow,width=20)
	text1.insert(INSERT,source_file)
	SelectFile = Button(subwindow, text="Select Input File",command=selectCSV)
	Generate = Button(subwindow, text="Generate",command=renderTemplate)
	GoBack = Button(subwindow, text="Back to Main",command=closeWindow)
	ShowTemplate = Button(subwindow, text="View/Edit J2 template",command=openTemplateFile)
	OutputText = scrolledtext.ScrolledText(subwindow,width=80,height=50)
	#layout the elements on a grid pattern
	OutputText.grid(columnspan=3,column=0, row=7)
	sublabel.grid(column=0, row=0)
	text1_label.grid(column=0,row=1)
	text1.grid(column=1, row=1)
	mode1.grid(column=1,row=3)
	mode2.grid(column=2, row=3)
	SelectFile.grid(column=0,row=6)
	Generate.grid(column=1,row=6)
	ShowTemplate.grid(column=2,row=6)
	GoBack.grid(column=3,row=6)
	subwindow.mainloop()
	
def mb4_clicked():

	
	def renderTemplate():
		#Calls the Jinja template function
		GeneratedConfig = DeviceTemplate(hostname.get(),mgmt_if.get(),mgmt_ip.get(),mgmt_mask.get())
		#Clears the text box	
		OutputText.delete(1.0,END)
		OutputText.insert(INSERT,GeneratedConfig)
	
	def closeWindow():
		subwindow.withdraw()
	
	def openTemplateFile():
	#Open the Jinja template for viewing/editing
		os.startfile(Subfolder + TemplateFile_4)	
	
	#Open a new window for this 
	subwindow = Toplevel()
	subwindow.title(MenuLabel_4)
	#Add items to the new window
	sublabel = Label(subwindow, text=MenuLabel_4, font=("Arial Bold",10))
	hostname_label = Label(subwindow, text="hostname:")
	mgmt_if_label = Label(subwindow, text="management interface")
	mgmt_ip_label = Label(subwindow, text="management IP")
	mgmt_mask_label = Label(subwindow, text="management netmask:")
	hostname = Entry(subwindow,width=20)
	mgmt_if = Entry(subwindow,width=12)
	mgmt_ip = Entry(subwindow,width=18)
	mgmt_mask = Entry(subwindow,width=18)
	Generate = Button(subwindow, text="Generate",command=renderTemplate)
	GoBack = Button(subwindow, text="Back to Main",command=closeWindow)
	ShowTemplate = Button(subwindow, text="View/Edit J2 template",command=openTemplateFile)
	OutputText = scrolledtext.ScrolledText(subwindow,width=80,height=50)	
	#Layout Elements on the window grid
	OutputText.grid(columnspan=3,column=0, row=7)
	sublabel.grid(column=0, row=0)
	hostname_label.grid(column=0,row=1)
	mgmt_if_label.grid(column=0,row=2)
	hostname.grid(column=1, row=1)
	mgmt_if.grid(column=1,row=2)
	mgmt_ip_label.grid(column=0,row=3)
	mgmt_mask_label.grid(column=0,row=4)
	mgmt_ip.grid(column=1, row=3)
	mgmt_mask.grid(column=1,row=4)
	Generate.grid(column=0, row=5)
	GoBack.grid(column=3, row=5)
	ShowTemplate.grid(column=2,row=5)
	subwindow.mainloop()

def mb5_clicked():


	def renderTemplate():
	#Calls the Jinja template function
		GeneratedConfig = BGPTemplate(localAS.get(),RouterID.get(),Neighbor_IP.get(),Neighbor_AS.get(),Neighbor_Desc.get(),BGP_PW.get(),RM_IN.get(),RM_OUT.get())
	#Clears the text box	
		OutputText.delete(1.0,END)
		OutputText.insert(INSERT,GeneratedConfig)
		
	def closeWindow():
		subwindow.withdraw()
		
	def openTemplateFile():
	#Open the Jinja template for viewing/editing
		os.startfile(Subfolder + TemplateFile_5)

	#Open a new window for this 	
	subwindow = Toplevel()
	subwindow.title(MenuLabel_5)
	#Add items to the new window
	sublabel = Label(subwindow, text=MenuLabel_5, font=("Arial Bold",10))
	localAS_label = Label(subwindow, text="Local AS#")
	RouterID_label = Label(subwindow, text="Local Router ID:")
	Neighbor_IP_label = Label(subwindow, text="Remote Router IP:")
	Neighbor_AS_label = Label(subwindow, text="Remote Router AS#:")
	Neighbor_Desc_label = Label(subwindow, text="Description:")
	BGP_PW_label = Label(subwindow, text="Password:")
	RM_IN_label = Label(subwindow, text="route-map IN")
	RM_OUT_label = Label(subwindow, text="route-map OUT")
	localAS = Entry(subwindow,width=12)
	RouterID = Entry(subwindow,width=20)
	Neighbor_IP = Entry(subwindow,width=12)
	Neighbor_AS = Entry(subwindow,width=12)
	Neighbor_Desc = Entry(subwindow,width=20)
	BGP_PW = Entry(subwindow,width=12)
	RM_IN = Entry(subwindow,width=12)
	RM_OUT = Entry(subwindow,width=12)
	Generate = Button(subwindow, text="Generate",command=renderTemplate)
	GoBack = Button(subwindow, text="Back to Main",command=closeWindow)
	ShowTemplate = Button(subwindow, text="View/Edit J2 template",command=openTemplateFile)
	OutputText = scrolledtext.ScrolledText(subwindow,width=80,height=50)
	#layout the elements on a grid pattern
	OutputText.grid(columnspan=2,column=0, row=7)
	sublabel.grid(column=0, row=0)
	localAS_label.grid(column=0,row=1)
	RouterID_label.grid(column=0,row=2)
	Neighbor_IP_label.grid(column=0,row=3)
	Neighbor_AS_label.grid(column=0,row=4)

	localAS.grid(column=1,row=1)
	RouterID.grid(column=1,row=2)
	Neighbor_IP.grid(column=1,row=3)
	Neighbor_AS.grid(column=1,row=4)

	Neighbor_Desc_label.grid(column=2, row=1)
	BGP_PW_label.grid(column=2,row=2)
	RM_IN_label.grid(column=2,row=3)
	RM_OUT_label.grid(column=2,row=4)

	Neighbor_Desc.grid(column=3, row=1)
	BGP_PW.grid(column=3,row=2)
	RM_IN.grid(column=3,row=3)
	RM_OUT.grid(column=3,row=4)

	Generate.grid(column=0,row=6)
	ShowTemplate.grid(column=1,row=6)
	GoBack.grid(column=2,row=6)
	subwindow.mainloop()
	
def mb6_clicked():
	
	def selectTFile():
		subwindow.filename = filedialog.askopenfilename(title = "Select Input File",filetypes = (("Jinja2 Template","*.j2"),("all files","*.*")))
		sel_template_file = subwindow.filename
		text1.delete(0,END)
		text1.insert(INSERT,sel_template_file)
		TemplateFile_6 = sel_template_file
	
	def renderTemplate():
		TemplateFile_6 = text1.get()
		#Calls the Jinja template function
		GeneratedConfig = GenericTemplate(value1.get(),value2.get(),value3.get(),value4.get())
		#Clears the text box	
		OutputText.delete(1.0,END)
		OutputText.insert(INSERT,GeneratedConfig)
	
	def closeWindow():
		subwindow.withdraw()
	
	def openTemplateFile():
		TemplateFile_6 = text1.get()
	#Open the Jinja template for viewing/editing
		os.startfile(Subfolder + TemplateFile_6)	
	
	#Open a new window for this 
	subwindow = Toplevel()
	subwindow.title(MenuLabel_6)
	#Add items to the new window
	sublabel = Label(subwindow, text=MenuLabel_6, font=("Arial Bold",10))
	text1_label = Label(subwindow, text="Template File:")
	value1_label = Label(subwindow, text="Variable1:")
	value2_label = Label(subwindow, text="Variable2:")
	value3_label = Label(subwindow, text="Variable3:")
	value4_label = Label(subwindow, text="Variable4:")
	value1 = Entry(subwindow,width=20)
	value2 = Entry(subwindow,width=20)
	value3 = Entry(subwindow,width=20)
	value4 = Entry(subwindow,width=20)
	text1 = Entry(subwindow,width=20)
	text1.insert(INSERT,TemplateFile_6)
	SelectFile = Button(subwindow, text="Select Input File",command=selectTFile)
	Generate = Button(subwindow, text="Generate",command=renderTemplate)
	GoBack = Button(subwindow, text="Back to Main",command=closeWindow)
	ShowTemplate = Button(subwindow, text="View/Edit J2 template",command=openTemplateFile)
	OutputText = scrolledtext.ScrolledText(subwindow,width=80,height=50)	
	#Layout Elements on the window grid
	OutputText.grid(columnspan=3,column=0, row=7)
	sublabel.grid(column=0, row=0)
	text1_label.grid(column=0,row=1)
	text1.grid(column=1,row=1)
	value1_label.grid(column=0,row=2)
	value2_label.grid(column=0,row=3)
	value3_label.grid(column=0,row=4)
	value4_label.grid(column=0,row=5)
	value1.grid(column=1,row=2)
	value2.grid(column=1,row=3)
	value3.grid(column=1,row=4)
	value4.grid(column=1,row=5)
	SelectFile.grid(column=1,row=6)
	Generate.grid(column=0, row=6)
	GoBack.grid(column=3, row=6)
	ShowTemplate.grid(column=2,row=6)
	subwindow.mainloop()
	
	
def mb7_clicked():
	#Default selection for input file - Comma Seperated Values
	source_file = ""
	
	def selectCSV():
		subwindow.filename = filedialog.askopenfilename(title = "Select Input File",filetypes = (("Comma Seperated Values","*.csv"),("all files","*.*")))
		sel_csv_file = subwindow.filename
		text1.delete(0,END)
		text1.insert(INSERT,sel_csv_file)
	
	def selectTFile():
		subwindow.filename = filedialog.askopenfilename(title = "Select Input File",filetypes = (("Jinja2 Template","*.j2"),("all files","*.*")))
		sel_template_file = subwindow.filename
		text1.delete(0,END)
		text1.insert(INSERT,sel_template_file)
		TemplateFile_7 = sel_template_file
			
	def renderTemplate():
	#Calls the Jinja template function
		myCSV = text1.get()
		GeneratedConfig = GenericCSVTemplate(myCSV)
	#Clears the text box	
		OutputText.delete(1.0,END)
		OutputText.insert(INSERT,GeneratedConfig)
		
	def closeWindow():
		subwindow.withdraw()
		
	def openTemplateFile():
	#Open the Jinja template for viewing/editing
		os.startfile(Subfolder + TemplateFile_7)
		
	
	#Open a new window for this 
	subwindow = Toplevel()
	subwindow.title(MenuLabel_7)
	#Add items to the new window
	sublabel = Label(subwindow, text=MenuLabel_7, font=("Arial Bold",10))
	text1_label = Label(subwindow, text="Select CSV file")
	text1 = Entry(subwindow,width=20)
	text1.insert(INSERT,source_file)
	text2_label = Label(subwindow, text="Template File:")
	text2 = Entry(subwindow,width=20)
	text2.insert(INSERT,TemplateFile_7)
	SelectFile = Button(subwindow, text="Select Input File",command=selectCSV)
	SelectTemplate = Button(subwindow, text="Select Input File",command=selectTFile)
	Generate = Button(subwindow, text="Generate",command=renderTemplate)
	GoBack = Button(subwindow, text="Back to Main",command=closeWindow)
	ShowTemplate = Button(subwindow, text="View/Edit J2 template",command=openTemplateFile)
	OutputText = scrolledtext.ScrolledText(subwindow,width=80,height=50)
	#layout the elements on a grid pattern
	OutputText.grid(columnspan=3,column=0, row=7)
	sublabel.grid(column=0, row=0)
	text1_label.grid(column=0,row=1)
	text1.grid(column=1, row=1)
	text2_label.grid(column=0,row=2)
	text2.grid(column=1,row=2)
	SelectFile.grid(column=0,row=6)
	SelectTemplate.grid(column=1,row=6)
	Generate.grid(column=2,row=6)
	ShowTemplate.grid(column=3,row=6)
	GoBack.grid(column=4,row=6)
	subwindow.mainloop()
	
	
def mb8_clicked():
	print ("Not yet implemented.")
		
def showHelp_About():

	def CloseWindow():
		helpwindow.withdraw()
	
	helpwindow = Toplevel()
	helpwindow.title("DooHickey Version 0.0.0.1")
	helplabel = Label(helpwindow, text="About This Software", font=("Arial Bold",10))
	vlanID_label = Label(helpwindow, text="This is just a little something I have been working on - Evan Munro Sept 2019")
	vlanDesc_label = Label(helpwindow, text="evanmunro33@gmail.com")
	GoBack = Button(helpwindow, text="Back to Main",command=CloseWindow)
	helplabel.grid(column=0, row=0)
	vlanID_label.grid(column=0,row=1)
	vlanDesc_label.grid(column=0, row=2)
	GoBack.grid(column=0, row=3)
	helpwindow.mainloop()
	
def doQuit():
	quit()

def VLANTemplate(ID,Desc,IsFP,Type,Assoc):
	#This line uses the subdirectory 
	file_loader = FileSystemLoader(Subfolder)
	# Load the enviroment
	env = Environment(loader=file_loader,trim_blocks=True,lstrip_blocks=True)
	template = env.get_template(TemplateFile_1)
	output = template.render(vlan=ID,name=Desc,fpmode=IsFP,vlanType=Type,vlan_assoc=Assoc)
#	print(output)
	return(output)
	
def DeviceTemplate(Hostname,Mgmt_Int,Mgmt_IP,Mgmt_Mask):
	#This line uses the subdirectory
	file_loader = FileSystemLoader(Subfolder)
	# Load the enviroment
	env = Environment(loader=file_loader,trim_blocks=True,lstrip_blocks=True)
	template = env.get_template(TemplateFile_4)
	output = template.render(hostname=Hostname,interface=Mgmt_Int,ip=Mgmt_IP,mask=Mgmt_Mask)
#	print(output)
	return(output)
	
def BGPTemplate(localAS,RouterID,Neighbor_IP,Neighbor_AS,Neighbor_Desc,password,RM_IN,RM_OUT):
	#This line uses the subdirectory
	file_loader = FileSystemLoader(Subfolder)
	# Load the enviroment
	env = Environment(loader=file_loader,trim_blocks=True,lstrip_blocks=True)
	template = env.get_template(TemplateFile_5)
	output = template.render(localas=localAS,router_id=RouterID,neighbor_ip=Neighbor_IP,neighbor_desc=Neighbor_Desc,remote_as=Neighbor_AS,bgp_pw=password,rm_inbound=RM_IN,rm_outbound=RM_OUT)
#	print(output)
	return(output)
	
def GenericTemplate(value1,value2,value3,value4,value5):
	#This line uses the subdirectory
	file_loader = FileSystemLoader(Subfolder)
	# Load the enviroment
	env = Environment(loader=file_loader,trim_blocks=True,lstrip_blocks=True)
	template = env.get_template(TemplateFile_6)
	output = template.render(variable1=value1,variable2=value2,variable3=value3,variable4=value4,variable5=value5)
#	print(output)
	return(output)
	

	
	
def SwitchPortTemplate(source_CSV):


# String that will hold final full configuration of all interfaces
	interface_configs = ""

# Open up the Jinja template file (as text) and then create a Jinja Template Object 
	with open(Subfolder + TemplateFile_2) as f:
		interface_template = Template(f.read(),keep_trailing_newline=True, trim_blocks=True,lstrip_blocks=True)

# Open up the CSV file containing the data 
	with open(source_CSV) as f:
		# Use DictReader to access data from CSV 
		reader = csv.DictReader(f)
		# For each row in the CSV, generate an interface configuration using the jinja template 
		for row in reader:
			interface_config = interface_template.render(
				interface = row["Interface"],
				vlan = row["VLAN"],
				server = row["Server"],
				link = row["Link"],
				comment = row["Comment"],
				allowed = row["Trunk_Allowed"]
			)

        # Append this interface configuration to the full configuration 
			interface_configs += interface_config

#strip the "" from output		
	for char in '"':
		interface_configs = interface_configs.replace(char,'')
	
	return(interface_configs)
	
	
def L3PortTemplate(source_CSV):


# String that will hold final full configuration of all interfaces
	l3_configs = ""

# Open up the Jinja template file (as text) and then create a Jinja Template Object 
	with open(Subfolder + TemplateFile_3) as f:
		interface_template = Template(f.read(), keep_trailing_newline=True,trim_blocks=True,lstrip_blocks=True)

# Open up the CSV file containing the data 
	with open(source_CSV) as f:
		# Use DictReader to access data from CSV 
		reader = csv.DictReader(f)
		# For each row in the CSV, generate an interface configuration using the jinja template 
		for row in reader:
			l3_config = interface_template.render(
				interface = row["Interface"],
				hostname = row["Remote_Hostname"],
				link = row["Link"],
				comment = row["Comment"],
				ipv4 = row["IP Address"],
				ipv4_mask = row["Netmask"],
				ipv6 = row["IPV6 Address"],
				ipv6_mask = row["IPV6 Netmask"],
				MTU = row["MTU"]
			)

        # Append this interface configuration to the full configuration 
			l3_configs += l3_config

#strip the "" from output		
	for char in '"':
		l3_configs = l3_configs.replace(char,'')
	
	return(l3_configs)
	
	
	
def GenericCSVTemplate(source_CSV):


# String that will hold final full configuration of all interfaces
	generic_configs = ""

# Open up the Jinja template file (as text) and then create a Jinja Template Object 
	with open(Subfolder + TemplateFile_7) as f:
		generic_template = Template(f.read(), keep_trailing_newline=True,trim_blocks=True,lstrip_blocks=True)

# Open up the CSV file containing the data 
	with open(source_CSV) as f:
		# Use DictReader to access data from CSV 
		reader = csv.DictReader(f)
		# For each row in the CSV, generate an interface configuration using the jinja template 
		for row in reader:
			generic_config = generic_template.render(
				variable1 = row["variable1"],
				variable2 = row["variable2"],
				variable3 = row["variable3"],
				variable4 = row["variable4"],
				variable5 = row["variable5"],
				variable6 = row["variable6"]
			)

        # Append this interface configuration to the full configuration 
			generic_configs += generic_config

#strip the "" from output		
	for char in '"':
		generic_configs = generic_configs.replace(char,'')
	
	return(generic_configs)
	
	
#Main program starts here	
#Draw a window with a label and some buttons	
window = Tk()
window.title("deviceConfig generator")
window.geometry('500x350')
mylabel = Label(window, text="DooHickey Version 0.0.0.1", font=("Arial Bold",10))
mylabel.grid(column=0, row=0)
mylabel1 = Label(window, text="Selected Jinja2 Templates:", font=("Arial",10))
mylabel1.grid(column=0, row=1)
MenuButton1 = Button(window, text=MenuLabel_1, command=mb1_clicked)
MenuButton1.grid(column=0, row=2)
MenuButton2 = Button(window, text=MenuLabel_2, command=mb2_clicked)
MenuButton2.grid(column=0, row=3)
MenuButton3 = Button(window, text=MenuLabel_3, command=mb3_clicked)
MenuButton3.grid(column=0, row=4)
MenuButton4 = Button(window, text=MenuLabel_4, command=mb4_clicked)
MenuButton4.grid(column=1, row=2)
MenuButton5 = Button(window, text=MenuLabel_5, command=mb5_clicked)
MenuButton5.grid(column=1, row=3)
MenuButton8 = Button(window, text=MenuLabel_8, command=mb8_clicked)
MenuButton8.grid(column=1, row=4)

MenuButton6 = Button(window, text=MenuLabel_6, command=mb6_clicked)
mylabel2 = Label(window, text="Generic Templating Functions:", font=("Arial",10))
mylabel2.grid(column=0, row=5)
MenuButton6.grid(column=0, row=6)
MenuButton7 = Button(window, text=MenuLabel_7, command=mb7_clicked)
MenuButton7.grid(column=1, row=6)


#Main Menu bar
menu = Menu(window)
quit_item = Menu(menu)
quit_item.add_command(label="Quit",command=doQuit)
menu.add_cascade(label='File', menu=quit_item)
help_item = Menu(menu)
help_item.add_command(label="About",command=showHelp_About)
menu.add_cascade(label='Help', menu=help_item)

window.config(menu=menu)
window.mainloop()