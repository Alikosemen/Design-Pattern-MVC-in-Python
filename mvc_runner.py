import mvc_py

controller = mvc_py.Controller()

# Displaying Summary for defect id # 2

controller.getDefectSummary(2)

# Displaying defect list for 'ABC' Component

controller.getDefectList('ABC')
