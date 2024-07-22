import os
import traceback
import time
from flask import Flask, render_template, request, redirect, url_for, send_file
from dxf_reader.extract_coords import extract_plate_info
from excel_writer.write_to_excel import write_plate_info_to_excel

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'dxf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            return redirect(url_for('processing', filename=file.filename))
    return render_template('upload.html')

@app.route('/processing/<filename>')
def processing(filename):
    return render_template('processing.html', filename=filename)

@app.route('/process_file/<filename>')
def process_file(filename):
    try:
        dxf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        excel_path = os.path.join(app.config['UPLOAD_FOLDER'], 'report.xlsx')
        
        # Simulate processing time
        time.sleep(5)
        plate_info = extract_plate_info(dxf_path)
        if not plate_info:
            return "No plate information found in the DXF file.", 400
        write_plate_info_to_excel(plate_info, excel_path)
        return redirect(url_for('result', filename='report.xlsx'))
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Traceback:")
        traceback.print_exc()
        return "An error occurred while processing the file.", 500

@app.route('/result/<filename>')
def result(filename):
    return render_template('result.html', filename=filename)

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
