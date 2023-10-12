#######
#  Main UI to control RPA Solar Modeling jobs in UiPath Orchestrator - Bots are calling via API in the program
#  CallSolarAPI imported here. ShowJson also imported here is used to edit Json File before submitting it
#######

from json.decoder import JSONDecoder
# import CallSolarAPI
import CallBot
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import json

# from PIL import Image, ImageTk      ### pip install pillow

def refresh(self):
    self.destroy()
    self.__init__()

def chosejob():
    root = tk.Tk()
    root.geometry("700x150")    
    root.configure(background='#fafafa')
    root.title("Solar Modeling Simulation")
    
    jobname=StringVar()
    global jsonOK
    
    def exitfunc():
        root.destroy()
        SystemExit()

    def callbot():
        global file_path
        global jsonOK

######  Display JSON content and update it with users changes
        def showjson(json_file):
            global jsonOK
            fjson = open(json_file, "r")
            jsontxt = fjson.read()
            # jsontxt = jsontxt.replace(chr(47)+chr(47),chr(47))
            # jsontxt = jsontxt.replace(chr(47), chr(47)+chr(47))
            jsontxt = jsontxt.replace(chr(92)+chr(92),chr(92))
            jsontxt = jsontxt.replace(chr(92), chr(92)+chr(92))
            jsonobj = json.loads(jsontxt)
            fjson.close()

            js_sitename = StringVar(ws, value=str(jsonobj['SiteName']))
            js_latitude = IntVar(ws, value=jsonobj['Latitude'])
            js_longitude = IntVar(ws, value=jsonobj['Longitude'])
            js_csvdir = StringVar(ws, value=str(jsonobj['SolarAnywhereFilePath']))
            js_impfile = StringVar(ws, value=str(jsonobj['Variant'][0]['NearShading']['ImportedFile']))

            #####
            for vars in jsonobj['Variant']:
                print(vars['variant_name'])
                for suba in jsonobj['Variant'][0]['System']['SubArrays']:
                    print (suba["SubArray_Name"])
            #####

            sitename = Entry(ws, textvariable=js_sitename, justify=LEFT, width=50,)
            latitude = Entry(ws, textvariable=js_latitude)
            longitude = Entry(ws, textvariable=js_longitude)
            csvdir = Entry(ws, textvariable=js_csvdir, justify=LEFT, width=50, xscrollcommand=True)
            impfile = Entry(ws, textvariable=js_impfile, justify=LEFT, width=50, xscrollcommand=True)

            sitename_lbl = Label(ws, text='Site Name', bg='#f5f5f5',)
            latitude_lbl = Label(ws, text='Latitude', bg='#f5f5f5',)
            longitude_lbl = Label(ws, text='Longitude', bg='#f5f5f5',)
            csvdir_lbl = Label(ws, text='SolarAnywhere File Path', bg='#f5f5f5',)
            impfile_lbl = Label(ws, text='Near Shading File Path', bg='#f5f5f5',)

            sitename_lbl.place(x=2,y=10)
            sitename.place(x=140,y=10)
            latitude_lbl.place(x=2,y=40)
            latitude.place(x=140,y=40)
            longitude_lbl.place(x=2,y=70)
            longitude.place(x=140,y=70)
            csvdir_lbl.place(x=2,y=100)
            csvdir.place(x=140,y=100)
            impfile_lbl.place(x=2,y=130)
            impfile.place(x=140,y=130)
            
            def confJson():
                global jsonOK
                jsonOK = True
                jsonobj['SiteName'] = sitename.get()
                jsonobj['Latitude'] = latitude.get()
                jsonobj['Longitude'] = longitude.get()
                jsonobj['SolarAnywhereFilePath'] = csvdir.get()
                jsonobj['Variant'][0]['NearShading']['ImportedFile'] = impfile.get()
                fjson = open(json_file, "w") 
                json.dump(jsonobj,fjson)
                fjson.close()
                ws.quit()
                
            btnConf = Button(ws, text='Confirm', bg="#3258EF", fg="white", command=confJson)
            btnConf.place(x=180, y=170)

            btnCancel = Button(ws, text='Cancel', bg="#F73B3B", fg="white", command=lambda: ws.quit())
            btnCancel.place(x=250, y=170)

        ### Call RPA API for each choosen json_file 
        for item in file_path:
            if jobname.get() == "Select a Process":
                jobname.set("SolarModelingAPI")
                jobmsg = "SolarModelingAPI (Default)"
            else:
                jobmsg = jobname.get()
            ### Edit JSON File for adjustments and confirmation
            
            ws = tk.Tk()
            ws.title('Json File')
            ws.geometry('500x50+600+200')
            ws.config(bg='#f5f5f5')
            # ScrolledText(ws).pack()

            jsonOK = False

            showjson(item)

            ws.mainloop()
            ws.destroy()

            ### Define if process is ready and call RPA via API
            if jsonOK:
                submConf = messagebox.askyesno("Confirm Simulation", message="Do you confirm the simulation for?\n\nJob Name: "+jobmsg+"\nJson File: "+item)
                if submConf:
                    CallBot.main(jobname.get(), item)
                    # CallSolarAPI.main(jobname.get(), item)
                else:
                    messagebox.showinfo("Information","Simulation was not submitted for:\n\nJob Name: "+jobmsg+"\n\nJson File: "+item)


    def chosefile():
        global file_path
        file_path=""
        file_path = filedialog.askopenfilenames(filetypes=[("json format", ".json")])
        label3=Label(root,text=file_path,fg="black",bg='#fafafa', font=("arial",10),)
        label3.place(x=35,y=40)
                
        def choseprocess():
        ### Chose Job Name
            label2=Label(root,text="Process Name",fg="black",bg='#fafafa', font=("arial",10, "bold"))
            label2.place(x=40,y=80)
            joblist = ["SolarModelingAPI", "solar_performance_modeling_process", "Solar_Large", "Solar_Medium", "Solar_Low"]
            droplist=OptionMenu(root,jobname,*joblist)
            jobname.set("Select a Process")
            droplist.config(width=15)
            droplist.place(x=135,y=75)

            Btnframe = Frame(root, width=400, height=40, bd=2, bg='#f5f5f5')
            Btnframe.place(x=0,y=110)

        ### Call Bot
            confirmBtn=Button(root, text="Confirm", font=("arial",10), bg="#3258EF", fg="white", command=callbot)
            confirmBtn.place(x=250,y=118)
            # confirmBtn['relief'] = 'solid'

        ### Cancel Job
            exitBtn=Button(root, text="Cancel", font=("arial",10), bg="#F73B3B", fg="white", command=exitfunc)
            exitBtn.place(x=320,y=118)
            # exitBtn['relief'] = 'solid'

        choseprocess()
        
### Chose Json File
    label1=Label(root,text="Json File", bg='#fafafa', font=("arial",10, "bold"))
    label1.place(x=35,y=10)
    fileBtn=Button(root, text="Chose a File", font=("arial",10), command=chosefile)
    fileBtn.place(x=130,y=10)

    root.mainloop()
    
if __name__ == "__main__":
    jsonOK = False
    chosejob()