import ezdxf
from collections import defaultdict
import re

def clean_plate_name(name):
    name = re.sub(r'\\[A-Za-z0-9]+;', '', name)
    name = re.sub(r'\{[^}]*\}', '', name)
    
    match = re.search(r'\((\d+)X(\d+)\)', name)
    if match:
        return f"{match.group(1)} D {match.group(2)}"
    
    name = re.sub(r'[^\w\s]', '', name)
    name = ' '.join(name.split())
    name = re.sub(r'(?<=\D)(?=\d)|(?<=\d)(?=\D)', ' ', name)
    
    return name

def extract_plate_info(dxf_path):
    try:
        doc = ezdxf.readfile(dxf_path)
        msp = doc.modelspace()

        plate_info = defaultdict(lambda: {"Count": 0, "Layer Name": ""})

        for entity in msp.entity_space:
            plate_name = None
            layer_name = entity.dxf.layer

            if entity.dxftype() == 'INSERT':
                plate_name = entity.dxf.name
            elif entity.dxftype() == 'TEXT':
                plate_name = entity.dxf.text
            elif entity.dxftype() == 'MTEXT':
                plate_name = entity.text

            if plate_name:
                plate_name = clean_plate_name(plate_name)

            if plate_name:
                plate_info[plate_name]["Count"] += 1
                plate_info[plate_name]["Layer Name"] = layer_name

        result = [
            {"Plate Name": name, "Count": info["Count"], "Layer Name": info["Layer Name"]}
            for name, info in plate_info.items()
        ]

        if not result:
            print("No plate information found in the DXF file.")
        return result
    except Exception as e:
        print(f"Error reading DXF file: {e}")
        return None
