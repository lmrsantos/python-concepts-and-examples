from os import kill
import requests
import json
import APISA
from os.path import exists
from tkinter import messagebox

def getToken():

    url = "https://account.uipath.com/oauth/token"

    payload = json.dumps({
      "grant_type": "refresh_token",
      "client_id": "8DEv1AMNXczW3y4U15LL3jYf62jK93n5",
      "refresh_token": "RtgCOwmRA3Xqc_W7szMOD8g6TrJdS8KbfBwr-mi2QzcS2"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    jobj = response.json()

    if 'error' in jobj:
        messagebox.showerror("Error Message", message=jobj['error_description'])
        data="none"
    else:
        data = jobj['access_token']

    # print("gettoken - 111111111")
    # print (response.text)
    return data

def ReleaseKey(token, jobname):

    accessToken = token
    name = jobname
    process_key = "SOLAR_MODELING_API"  ##It is the package name at Orchestrator and/or UiPath Studio
    url = "https://cloud.uipath.com/lmsolbheqmvi/DefaultTenant/odata/Releases?$filter=Name eq "+"'"+jobname+"'"
    
    payload = {}
    headers = {
        'X-UIPATH-TenantName': 'DefaultTenant',
        'X-UIPATH-OrganizationUnitId': '',
        'accept': 'application/json',
        'contentType': 'application/json',
        'authorization': 'Bearer ' + accessToken
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print("release key - 222222")
    # print(response.text)
    
    key = "none"
    data = response.json()
    itens = data['@odata.count']

    for x in range(itens):

        if data['value'][x]['Name'] == name and \
        data['value'][x]['ProcessKey'] == process_key:
            key = data['value'][x]['Key']
            orgid = data['value'][x]['OrganizationUnitId']
            break

    return key, orgid


def StartProcess(key_release, token, argument):

    key = key_release[0]
    orgid = str(key_release[1])
    accessToken = token
    argument = argument
    url = "https://cloud.uipath.com/lmsolbheqmvi/DefaultTenant/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs"

    payload = json.dumps({
        "startInfo": {
            "ReleaseKey": key,
            "Strategy": "ModernJobsCount",
            "JobsCount": 1,
            "InputArguments": argument
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'X-UIPATH-TenantName': 'DefaultTenant',
        'X-UIPATH-OrganizationUnitId': orgid,
        'authorization': 'Bearer ' + accessToken
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print("gettoken - 333333")
    # print(response.text)

def main(jobname="SolarModelingAPI", json_path=""):

    jsonpath = json_path
    # print (jsonpath, jobname)

    fjson = open(jsonpath, "r")
    argument1 = fjson.read()
    argument1 = argument1.replace(chr(92), chr(92)+chr(92))

    # parse file to call SolarAnywhere
    obj = json.loads(argument1)

    sitename = str(obj['SiteName'])
    latitude = str(obj['Latitude'])
    longitude = str(obj['Longitude'])
    csvdir = str(obj['SolarAnywhereFilePath'])
    csvdir = csvdir.replace('.csv', '')
    # print (csvdir, sitename, latitude, longitude)

    if not exists(csvdir):
        APISA.convertxmlcsv(csvdir, sitename, latitude, longitude)
    
######## Start Calling the Bot
    token = getToken()

    if token != "none":
        key_release = ReleaseKey(token, jobname)
        if key_release != "none":
            messagebox.showinfo("Information","Your job was successfuly submitted. You are going to receive an email with the results soon.")
            StartProcess(key_release, token,  '{\'argument1\':\'' + argument1 + '\'}')
        else:
            messagebox.showerror("Error Message", message="Cannot find a job or json file. Please try again.")

if __name__ == "__main__":
    main()
