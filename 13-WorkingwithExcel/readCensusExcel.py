 
#readCensusExcel.py - Tabulates population and number of census tracts for each county

import openpyxl, pprint

print('Opening workbook...')

wb = openpyxl.load_workbook("/Users/farihaalam/censuspopdataa.xlsx")

sheet = wb['Population by Census Tract']
countyData = {}

print('Reading rows')

for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    print(state)
    print(county)
    print(pop)
    
#make nested dictionary 

    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    countyData[state][county]['tracts'] +=  1   #dictionary keys
    countyData[state][county]['pop'] += int(pop)      #dictionary keys

print('Writing results...')
resultFile = open('projects/census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done')


import os
import census2010 

census2010.allData['AK']['Anchorage']










