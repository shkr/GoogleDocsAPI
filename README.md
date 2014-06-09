Google Spreadsheet API
=======================

The python-api provides a single class to write and read to a GoogleSpreadSheet.

-Step 0. Install dependencies

    pip install -r requirements.txt

-Step 1. Connecting to an existing spreadsheet

    from gdoc_api import spreadsheet
    MySpreadSheet = spreadsheet ( uid = 'shashank@jharkhand.com', name='MyPrivateSheet', mode= .. ,columns = .. )

-Step 2. Writing

    MySpreadSheet = spreadsheet ( uid = 'shashank@jharkhand.com', name='MyPrivateSheet', mode='w',columns=['column A','column B','column C'])
    MySpreadSheet.write_row(['A is good','B is okay','C is bad'])

-Step 3. Reading

    MySpreadSheet = spreadsheet ( uid = 'shashank@jharkhand.com', name='MyPrivateSheet', mode='r')
    MySpreadsheet.read_row([1])  #Outputs first row Note : 0th row is header row
    MySpreadsheet.read_row([1],[0,1])  #Outputs first row's only 0th & 1st column Note : 0th row is header row
    MySpreadsheet.wks.col_values(0)    #Outputs the first column as a list

-Step 4. Appending

    MySpreadSheet = spreadsheet ( uid = 'shashank@jharkhand.com', name='MyPrivateSheet', mode='a', columns = 3)
    MySpreadSheet.write_row(['A is nice','B is average','C is pathetic'])

-Additionally for help on the terminal use spreadsheet.help() for guidelines
    
    from gdoc_api import spreadsheet
    spreadsheet.help()
