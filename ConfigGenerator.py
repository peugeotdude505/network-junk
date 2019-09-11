from tkinter import *
from tkinter import scrolledtext,filedialog
from jinja2 import Environment, FileSystemLoader, Template
import csv
import os

MenuLabel_1 = 'L2 VLAN'
MenuLabel_2 = 'L2 Switchports'
MenuLabel_3 = 'L3 Interfaces'
MenuLabel_4 = 'Baseline Config for Device'
MenuLabel_5 = 'BGP configuration'

TemplateFile_1 = 'single-vlan.j2'
TemplateFile_2 = 'switchport-interface.j2'
TemplateFile_3 = 'l3-interface.j2'
TemplateFile_4 = 'device-base.j2'


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
		os.startfile(TemplateFile_1)

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
		source_file = subwindow.filename
		text1.delete(0,END)
		text1.insert(INSERT,source_file)
		
	def renderTemplate():
	#Calls the Jinja template function
		GeneratedConfig = SwitchPortTemplate(source_file)
	#Clears the text box	
		OutputText.delete(1.0,END)
		OutputText.insert(INSERT,GeneratedConfig)
		
	def closeWindow():
		subwindow.withdraw()
		
	def openTemplateFile():
	#Open the Jinja template for viewing/editing
		os.startfile(TemplateFile_2)
	
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
	source_file = "l3-interfaces.csv"
	
	def selectCSV():
		subwindow.filename = filedialog.askopenfilename(title = "Select Input File",filetypes = (("Comma Seperated Values","*.csv"),("all files","*.*")))
		source_file = subwindow.filename
		text1.delete(0,END)
		text1.insert(INSERT,source_file)
		
	def renderTemplate():
	#Calls the Jinja template function
		GeneratedConfig = L3PortTemplate(source_file)
	#Clears the text box	
		OutputText.delete(1.0,END)
		OutputText.insert(INSERT,GeneratedConfig)
		
	def closeWindow():
		subwindow.withdraw()
			
	def openTemplateFile():
		#Open the Jinja template for viewing/editing
		os.startfile(TemplateFile_3)
	
	
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
		os.startfile(TemplateFile_4)	
	
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
	mgmt_ip = Entry(subwindow,width=20)
	mgmt_mask = Entry(subwindow,width=12)
	Generate = Button(subwindow, text="Generate",command=renderTemplate)
	GoBack = Button(subwindow, text="Back to Main",command=closeWindow)
	ShowTemplate = Button(subwindow, text="View/Edit J2 template",command=openTemplateFile)
	ShowTemplate.grid(column=2,row=6)
	OutputText = scrolledtext.ScrolledText(subwindow,width=80,height=50)	
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
	GoBack.grid(column=1, row=5)
	subwindow.mainloop()
	
	
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
	#This line uses the current directory
	file_loader = FileSystemLoader('.')
	# Load the enviroment
	env = Environment(loader=file_loader,trim_blocks=True,lstrip_blocks=True)
	template = env.get_template(TemplateFile_1)
	output = template.render(vlan=ID,name=Desc,fpmode=IsFP,vlanType=Type,vlan_assoc=Assoc)
#	print(output)
	return(output)
	
def DeviceTemplate(Hostname,Mgmt_Int,Mgmt_IP,Mgmt_Mask):
	#This line uses the current directory
	file_loader = FileSystemLoader('.')
	# Load the enviroment
	env = Environment(loader=file_loader,trim_blocks=True,lstrip_blocks=True)
	template = env.get_template(TemplateFile_4)
	output = template.render(hostname=Hostname,interface=Mgmt_Int,ip=Mgmt_IP,mask=Mgmt_Mask)
#	print(output)
	return(output)
	
	
def SwitchPortTemplate(source_CSV):


# String that will hold final full configuration of all interfaces
	interface_configs = ""

# Open up the Jinja template file (as text) and then create a Jinja Template Object 
	with open(TemplateFile_2) as f:
		interface_template = Template(f.read(), keep_trailing_newline=True)

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
	with open(TemplateFile_3) as f:
		interface_template = Template(f.read(), keep_trailing_newline=True)

# Open up the CSV file containing the data 
	with open(source_CSV) as f:
		# Use DictReader to access data from CSV 
		reader = csv.DictReader(f)
		# For each row in the CSV, generate an interface configuration using the jinja template 
		for row in reader:
			l3_config = interface_template.render(
				interface = row["Interface"],
				hostname = row["Hostname"],
				link = row["Link"],
				comment = row["Comment"],
				ipv4 = row["IP Address"],
				ipv4_mask = row["Netmask"]
			)

        # Append this interface configuration to the full configuration 
			l3_configs += l3_config

#strip the "" from output		
	for char in '"':
		l3_configs = l3_configs.replace(char,'')
	
	return(l3_configs)
	
#Draw a window with a label and some buttons	
window = Tk()
window.title("deviceConfig generator")
window.geometry('500x350')
mylabel = Label(window, text="DooHickey Version 0.0.0.1", font=("Arial Bold",10))
mylabel.grid(column=0, row=0)
MenuButton1 = Button(window, text=MenuLabel_1, command=mb1_clicked)
MenuButton1.grid(column=0, row=1)
MenuButton2 = Button(window, text=MenuLabel_2, command=mb2_clicked)
MenuButton2.grid(column=0, row=2)
MenuButton3 = Button(window, text=MenuLabel_3, command=mb3_clicked)
MenuButton3.grid(column=1, row=1)
MenuButton4 = Button(window, text=MenuLabel_4, command=mb4_clicked)
MenuButton4.grid(column=1, row=2)

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