import requests

lCounties = ["Albany", "Allegany", "Bronx", "Broome", "Cattaraugus", "Cayuga", "Chautauqua", "Chemung", "Chenango", "Clinton", "Columbia", "Cortland", "Delaware", "Dutchess", "Erie", "Essex", "Franklin", "Fulton", "Genesee", "Greene", "Hamilton", "Herkimer", "Jefferson", "Kings", "Lewis", "Livingston", "Madison", "Monroe", "Montgomery", "Nassau", "New York", "Niagara", "Oneida", "Onondaga", "Ontario", "Orange", "Orleans", "Oswego", "Otsego", "Putnam", "Queens", "Rensselaer", "Richmond", "Rockland", "Saint Lawrence", "Saratoga", "Schenectady", "Schoharie", "Schuyler", "Seneca", "Steuben", "Suffolk", "Sullivan", "Tioga", "Tompkins", "Ulster", "Warren", "Washington", "Wayne", "Westchester", "Wyoming", "Yates"]

for sCounty in lCounties:
    sFileName = sCounty + "BridgeData.pdf"
    sUrl = "https://www.dot.ny.gov/main/bridgedata/repository/" + sFileName
    r = requests.get(sUrl, stream=True)
    with open("/data-pdf/" + sFileName, "wb") as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)
