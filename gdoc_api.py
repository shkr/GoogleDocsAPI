""" This receives a uid, spread_sheet name, mode, categories (header row)
    for initializing the google spreadsheet built on top of gspread (available on github)"""

import gspread
import string
from getpass import getpass

class spreadsheet:

    def __init__(self,uid,name,mode,columns=[]):
        self.connect_gspread(name,uid)
        self.row_id=1
        if mode=='w':
            self.categories=categories
            self.columns=len(categories)
            self.update_cell_list()
            self.write_row(categories)
        elif mode=='a':
            if type(columns) is int:
              self.columns = len(categories)
            elif type(columns) is list:
              self.categories = categories
            else:
              raise ValueError('Expected list of column names or number of columns in append mode')
            self.update_cell_list()
            while self.wks.cell(self.row_id,1).value!=None:
                self.change_row()
        elif mode=='r':
            print 'Guidelines :'
            print '1. For reading complete columns, use : <object_name>.wks.col_values(col_id)'
            print '2. For reading a row, execute <object_name>.read_row([list of row indices],[list of col indices])'

    @staticmethod
    def help():

        print 'Guidelines for writing/appending:'
        print '1. At initialization you must provide col. names <columns = [...]> when using in writing (w) mode. \n In append mode (a) you may only provide no. of columns <columns = natural number> \n  You must provide same number of col items to write_row as no. of columns, or right most column entries will be left empty for the row.'
        print '2. For writing a row, use : <object_name>.write_row([col1_item,col2_item,.....,colN_item])'

        print 'Guidelines for reading:'
        print '1. For reading complete columns, use : <object_name>.wks.col_values(col_id)'
        print '2. For reading a row, execute <object_name>.read_row([list of row indices],[list of col indices])'

    def read_row(self,row_ids,col_ids=[]):
        """For reading complete columns, use : self.wks.col_values(col_id) """
        values = []
        for rid in row_ids:
            if col_ids==[]:
                values.append(self.wks.row_values(rid))
            else:
                for cid in col_ids:
                    values.append(self.wks.cell(rid,cid).value)
        return values

    def col_range(self,char='A',columns=-1):
        """ char = Starting column; columns = length of columns """
        columns = self.columns if columns==-1 else columns
        """Example (return) : Arow_id:Frow_id"""
        return str( char+str(self.row_id)+':'+chr(ord(char)+columns-1)+str(self.row_id))

    def update_cell_list(self):
        self.cell_list = self.wks.range(self.col_range())

    def change_row(self,ct=1):
        self.row_id = self.row_id+ct

    def connect_gspread(self,name,uid):
        """This function connects to your google account spreadsheet
        and returns the file handle for the spreadsheet"""


        try:
            passwd = getpass(prompt='Hi! %s Enter your google account password :'%uid)
        except gspread.exceptions.AuthenticationError:
            passwd = getpass(prompt='Try again ? :')

        gc = gspread.login(uid,passwd)

        #Spreadsheet information
        self.wks = gc.open(name).sheet1

    def write_row(self,row):
        for i in range(0,self.columns):
            self.cell_list[i].value=row[i]
        self.wks.update_cells(self.cell_list)

        #Update Cell-list
        self.change_row()
        self.update_cell_list()
