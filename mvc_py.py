
""""
Let‘s consider a case of a test management system (TMS) that queries for a list of defects.
Here are two typical scenarios that work with any test management system.
* If the user queries for a particular defect, the test management system displays
the summary of the defect to the user in a prescribed format.
* If the user searches for a component it shows list of all defects logged against
that component.
"""


import sqlite3

class DefectModel:
    def getDefectList(self, component):
        query = "select ID from TMS where Component = ?"
        defectlist = self._dbselect(query, (component,))
        the_list = [row[0] for row in defectlist]
        return the_list

    def getSummary(self, id):
        query = "select Summary from TMS where ID = ?"
        summary = self._dbselect(query, (id,))
        return summary[0][0] if summary else None

    def _dbselect(self, query, params):
        connection = sqlite3.connect('TMS.db')
        cursorObj = connection.cursor()
        results = cursorObj.execute(query, params).fetchall()
        cursorObj.close()
        connection.close()
        return results

class DefectView:
    def summary(self, summary, defectid):
        if summary:
            print(f"#### Defect Summary for defect# {defectid}####\n{summary}")
        else:
            print(f"No summary available for defect# {defectid}")

    def defectList(self, the_list, category):
        if the_list:
            print(f"#### Defect List for {category}####")
            for defect in the_list:
                print(defect)
        else:
            print(f"No defects found for {category}")

class Controller:
    def __init__(self):
        self.model = DefectModel()
        self.view = DefectView()

    def getDefectSummary(self, defectid):
        summary_data = self.model.getSummary(defectid)
        self.view.summary(summary_data, defectid)
  
    def getDefectList(self, component):
        defectlist_data = self.model.getDefectList(component)
        self.view.defectList(defectlist_data, component) 
