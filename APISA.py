import requests
from requests.auth import HTTPBasicAuth
import xml.etree.ElementTree as ET
import time
from datetime import datetime, timedelta
import pytz
#import csv

# POST to Create WeatherData Request
def createxml(xmlfile, sitename, latitude, longitude):
    url = "https://service.solaranywhere.com/api/v2/WeatherData"
    userName = "Borrego.Client@borregosolar.com"
    password = "beef8b118f560850bb8b88777QA!ff3789"

    querystring = {"key": "95Bo#4r10"}

    payload = """<CreateWeatherDataRequest xmlns="http://service.solaranywhere.com/api/v2">
    <Sites>
     <Site Name=\""""+sitename+"""\" Latitude=\""""+latitude+"""\" Longitude=\""""+longitude+"""\" />
    </Sites>
    <Options
     WeatherDataSource="SolarAnywhereTGY2020"
     PerformTimeShifting="true"
     SpatialResolution_Degrees="0.1"
     TimeResolution_Minutes="60"
     OutputFields="StartTime,EndTime,ObservationTime,
            GlobalHorizontalIrradiance_WattsPerMeterSquared,
            DirectNormalIrradiance_WattsPerMeterSquared,
            AmbientTemperature_DegreesC,
            WindSpeed_MetersPerSecond,
            RelativeHumidity_Percent,
            DiffuseHorizontalIrradiance_WattsPerMeterSquared,
            Albedo_Unitless"/>
    </CreateWeatherDataRequest>"""

    # license does not allow to grab these values
    # IrradianceObservationType,ClearSkyGHI_WattsPerMeterSquared,ClearSkyDNI_WattsPerMeterSquared,

    headers = {
     'content-type': "text/xml; charset=utf-8",
     'content-length': "length",
     }

    response = requests.post(url,auth = HTTPBasicAuth(userName,password),data=payload,
               headers=headers,params=querystring)

    root = ET.fromstring(response.content)
    print(response.content)
    print("-----")

    publicId = root.attrib.get("WeatherRequestId")
    print(publicId)

    # GET WeatherDataResult
    url2 = "https://service.solaranywhere.com/api/v2/WeatherDataResult/"
    requestNumber = 0
    MAX_requestNumber = 100

    while(requestNumber < MAX_requestNumber):
        time.sleep(5)
        data = requests.get(url2 + publicId,auth = HTTPBasicAuth(userName,password))
        radicle = ET.fromstring(data.content)
        status = radicle.attrib.get("Status")
        print (status) ##(radicle)
        if status == "Done":
            root=ET.ElementTree(radicle)
            with open(xmlfile,"wb") as myfile:
                root.write(myfile)
            break
        else:
            requestNumber = requestNumber + 1
        
    return (xmlfile)

# Write in PVSyst CSV Format
def convertXmlCsv(csv_dir,sitename,latitude,longitude):
    
    xml_dir = csv_dir.replace('.csv', '.xml')
    xml_file = createxml(xml_dir, sitename, latitude, longitude)
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    with open(csv_dir, 'w', newline='') as csvfile:
        Data_Ver = "3.4"
        weatherrequestid = root.attrib.get('WeatherRequestId')
        sitename = root[0][0].attrib.get('SiteName')
        elevation = root[0][0][0].attrib.get('Elevation_Meters')
        latitude = root[0][0][0].attrib.get('Latitude')
        longitude = root[0][0][0].attrib.get('Longitude')
        timeresolution = root[0][0][1].attrib.get('TimeResolution_Minutes')
        tz_utc = str(int(root[0][0][1][0].attrib.get('ObservationTime')[19:22]))
        first_line="0,"+sitename+","+tz_utc+","+latitude+","+longitude+","+elevation+",Data Version: "+Data_Ver+" / Type: Typical Year / LatLon Resolution: 0.100 / Time Resolution: "+timeresolution+" minutes / Averaging Method: End of Period / Copyright 2010-2020 Clean Power ResearchÂ®,L.L.C. DownloadID="+weatherrequestid+"\n"
        csvfile.write(first_line)
        headers_line = "ObservationTime(LST),"
        headers_line += "Global Horizontal Irradiance (GHI) W/m2,"
        headers_line += "Direct Normal Irradiance (DNI) W/m2,"
        headers_line += "AmbientTemperature (deg C),"
        headers_line += "WindSpeed (m/s),"
        headers_line += "Relative Humidity (%),"
        headers_line += "Liquid Precipitation (kg/m2),"
        headers_line += "Solid Precipitation (kg/m2),"
        headers_line += "Snow Depth (m),"
        headers_line += "Clear Sky GHI,"
        headers_line += "Clear Sky DNI,"
        headers_line += "Clear Sky DHI,"
        headers_line += "IrradianceObservationType,"
        headers_line += "LeadTime,"
        headers_line += "DataVersion,"
        headers_line += "ObservationTime(GMT),"
        headers_line += "Diffuse Horizontal Irradiance (DIF) W/m2,"
        headers_line += "AmbientTemperatureObservationType,"
        headers_line += "WindSpeedObservationType,"
        headers_line += "Albedo"+"\n"
        csvfile.write(headers_line)
        startDate=datetime.fromisoformat(root[0][0][1].attrib.get('FirstStartTime'))
        first_row = True
        for wdp in root[0][0][1]:
            ObsStrDate = wdp.attrib.get('ObservationTime')
            ObsObjDate = datetime.strptime(ObsStrDate,'%Y-%m-%dT%H:%M:%S%z') + timedelta(hours=0, minutes=30)
            ObservationTime_LST = datetime.strftime(ObsObjDate,'%m/%d/%Y %H:%M')
            GHI_W_m2 = wdp.attrib.get('GlobalHorizontalIrradiance_WattsPerMeterSquared')
            DNI_W_m2 = wdp.attrib.get('DirectNormalIrradiance_WattsPerMeterSquared')
            AmbientTemperature_C = wdp.attrib.get('AmbientTemperature_DegreesC')
            WindSpeed_M_S = wdp.attrib.get('WindSpeed_MetersPerSecond')
            RelativeHumidity = wdp.attrib.get('RelativeHumidity_Percent')
            LiquidPrecipitation_KG_M2 = ""
            SolidPrecipitation_KG_M2 = ""
            SnowDepth_M = ""
            ClearSkyGHI = ""
            ClearSkyDNI = ""
            ClearSkyDHI = ""
            if int(GHI_W_m2) == 0:
                IrradianceObservationType = "AN"
            else:
                IrradianceObservationType = "AD"
            LeadTime = ""
            DataVersion = Data_Ver
            ObservationTime_GMT = datetime.strftime(datetime.fromisoformat(wdp.attrib.get('ObservationTime')).astimezone(pytz.utc)+timedelta(hours=0, minutes=30),'%m/%d/%Y %H:%M')
            DiffuseHorizontalIrradiance_W_M2 = wdp.attrib.get('DiffuseHorizontalIrradiance_WattsPerMeterSquared')
            AmbientTemperatureObservationType = "O"
            WindSpeedObservationType = "O"
            AlbedoUnitless = wdp.attrib.get('Albedo_Unitless')
            data_row = ObservationTime_LST+","+GHI_W_m2+","+DNI_W_m2+","+AmbientTemperature_C+","+WindSpeed_M_S+","
            data_row += RelativeHumidity+","+LiquidPrecipitation_KG_M2+","+SolidPrecipitation_KG_M2+","+SnowDepth_M+","
            data_row += ClearSkyGHI+","+ClearSkyDNI+","+ClearSkyDHI+","+IrradianceObservationType+","+LeadTime+","
            data_row += DataVersion+","+ObservationTime_GMT+","+DiffuseHorizontalIrradiance_W_M2+","+AmbientTemperatureObservationType+","
            data_row += WindSpeedObservationType+","+AlbedoUnitless+"\n"
            if first_row:
                data_first_row = data_row
                first_row = False
            else:
                csvfile.write(data_row)

        csvfile.write(data_first_row)
        
if __name__ == "__main__":
    sitename="Rear Somers Rd"
    latitude="42.05" 
    longitude="-72.45"
    filedir="C:\\Users\\luizm\\OneDrive\\Documents\\UiPath\\Call API New\\Data\\Rear Somers Rd SolarAnywhere Typical GHI Year Lat_42_05 Lon_-72_45 SA format-PY.csv"
    print(sitename,"\n",latitude,"\n",longitude)
    convertXmlCsv(filedir,sitename,latitude,longitude)
