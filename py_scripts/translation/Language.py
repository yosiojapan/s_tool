# -*- coding: utf-8 -*-
import json
import os
import sys

def Language_import(key,type_):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path,'Language.json')
    
    try:
        if sys.version_info[0] < 3:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
        else:
            with open(file_path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
        result = data[key][type_]
        return result
    
    except OSError:
        print("Error: {} FileNotFound".format(file_path))
        return ''
    except IOError:
        print("Error: {} IOError".format(file_path))
        return ''
    except KeyError:
        return ''
    except ValueError:
        print("Error: {} no json".format(file_path))
    except UnicodeDecodeError:
        print("Error: {} UnicodeDecodeError".format(file_path))
    return