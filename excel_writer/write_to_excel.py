import xlwings as xw

def write_plate_info_to_excel(plate_info, excel_path):
    with xw.App(visible=False) as app:
        book = app.books.add()
        
        # Create the "Mivan Report" sheet
        report_sheet = book.sheets.add("Report")
        report_sheet['A1'].value = 'Plate Name'
        report_sheet['B1'].value = 'Count'
        report_sheet['C1'].value = 'Layer Name'
        
        # Write plate information
        for i, info in enumerate(plate_info, start=2):
            report_sheet[f'A{i}'].value = info["Plate Name"]
            report_sheet[f'B{i}'].value = info["Count"]
            report_sheet[f'C{i}'].value = info["Layer Name"]
        
        # Auto-fit columns
        report_sheet.autofit()
        
        # Save the workbook
        book.save(excel_path)
        book.close()

