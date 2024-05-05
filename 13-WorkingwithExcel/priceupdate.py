
import openpyxl
import openpyxl.workbook 


wb = openpyxl.load_workbook('/Users/farihaalam/produceSalescopy.xlsx')
sheet = wb['Sheet']


column_A_values = []
column_B_values = []
column_C_values = []
column_D_values = []


for cell in sheet['A']:
    column_A_values.append(cell.value) 
print(column_A_values)

for cell in sheet['B']:
    column_B_values.append(cell.value)
print(column_B_values)

for cell in sheet ['C']:
    column_C_values.append(cell.value)

for cell in sheet ['D']:
    column_D_values.append(cell.value)
    
   # print(column_A_values)
# print(column_B_values)
# print(column_C_values)
# print(column_D_values)

# print(column_D_values)

# p = column_A_values 
# c = column_B_values




 