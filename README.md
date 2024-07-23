# IPO Generator

IPO Generator is a web application that allows users to upload DXF files, process them to extract plate information, and download the results in an Excel format. This tool streamlines the conversion of DXF files to Excel reports, making it easier to manage and analyze plate data.

## Features

- Upload DXF files
- Extract plate information from DXF files
- Download the extracted data as an Excel file
- User-friendly web interface

## Technologies Used

- Python
- Flask
- ezdxf
- xlwings
- HTML/CSS
- JavaScript

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ipo-generator.git
   cd ipo-generator
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3. Install the required packages:
   ```bash
   pip install -r requirements.txt

4. Ensure the uploads directory exists:
   ```bash
   mkdir -p uploads


5. Running the Application

   1. Start the Flask application:
      ```bash
      python app.py

   2. Open your web browser and navigate to:
      ```bash
      http://127.0.0.1:5000/


6. Folder Structure
```bash
ipo_generator/
├── dxf_reader/
│   ├── __init__.py
│   ├── extract_coords.py
├── excel_writer/
│   ├── __init__.py
│   ├── write_to_excel.py
├── static/
│   ├── styles.css
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── upload.html
│   ├── processing.html
│   ├── result.html
│   ├── error.html
├── uploads/
├── app.py
├── requirements.txt
```
7. Usage

  1. Navigate to the home page and click "Get Started".
  2. Upload your DXF file.
  3. Wait while the file is processed.
  4. Download the generated Excel report.

8. Error Handling

1. If there is an error during processing or if no plate information is found in the DXF file, an error page will be displayed with a corresponding message.
9. License
This project is licensed under the MIT License - see the LICENSE file for details.
Contact
For any inquiries or support, please contact 27manavgandhi@gmail.com.