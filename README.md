# CodeGenerator
This repo contains the basic implementation of the pyQT5 program which reads the configuration file .json extracted from the ML process. 
What the ML process does is UI Elements detection on a subject GUI screenshot and generate the .json file containing the boundary boxes,
class names and some more important information about the object detected such as image width and height. The program expect a single 
parameter,```config_json_file_path``` which is the path to .json file. The .json file is referenced from ```data directory``` by default. At minimum, the .json file should bear the following format.
```python3
file_name = {"image_id": int # The image number if you are detecting in a batch,else it is 0
             "image_name": str,
             "image_height":int # Pixels,
             "image_width": int # Pixels,
             "bounds":List of List (2D Array) # Contains the location of each detected element [[xmin,ymin,xmax,ymax],..],
             "classes":List of int # Contains the index of class for each ui element detected,
             "classes_names": List of str # Names of all classes supported
             }

```
The following classes are supported until now.
```python3
    "classes_names": [
        "Checkbox",
        "Date Picker",
        "Image",
        "Input",
        "List Item",
        "Map View",
        "Multi-Tab",
        "On/Off Switch",
        "Radio Button",
        "Slider",
        "Text",
        "Text Button"
    ]
```
| ℹ️  | Just Clone this repo to your environment, install the requirements.txt and you are all set |
| --- | --- |
| ℹ️  | You may edit the .py files in uiElements directory to decorate the outlook of components|
| ℹ️  | Download the codes (GUI codes are stored [here](./codes) once the app is run) to get started with your favourite GUI|

##  Examples
The whole GUI Generation Process.
| GUI Screenshot | Config file from ML Process | pyQT5 GUI Generated | pyQT5 Codes Generated |
| --- | --- | --- | --- |
|![37815.jpg](examples/37815.jpg) | [Check the json file here](data/37815.json) |![37815_1.jpg](examples/37815_1.JPG) |[pyQT codes](./codes/37815.py)|

