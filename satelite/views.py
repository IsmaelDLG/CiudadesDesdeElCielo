from django.shortcuts import render
from django.conf import settings
from pathlib import Path
import os
from django.core.files.storage import FileSystemStorage
import pathlib

# Create your views here.
def index(request):
    return render(request, Path('satelite/index.html'), {
        'sources' : os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), str(Path("TrainYourOwnYOLO/Data/Source_Images/Test_Images"))))
    })

def loadImage(request):
    if request.method == 'POST' and request.FILES['files']:
        for x in request.FILES.getlist('files'):
            myfile = x
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
    return render(request, 'satelite/index.html', {
        'sources' : os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), str(Path("TrainYourOwnYOLO/Data/Source_Images/Test_Images"))))
    })

def runDetector(request):
    # https://stackoverflow.com/questions/1853662/how-to-show-page-loading-div-until-the-page-has-finished-loading
    script = "Detector.py"
    script_path = Path(__file__).absolute().parent / Path("TrainYourOwnYOLO/3_Inference/")
    
    print("Launching Detector")
    res = os.system("cd " + str(script_path) + " && " + "python3.7 " + script)

    ret = []
    for res in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), str(Path("TrainYourOwnYOLO/Data/Source_Images/Test_Image_Detection_Results/")))):
        if res[-3:] != 'csv':
            f = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'ml', res)
            try:
                os.remove(f)
            except FileNotFoundError:
                pass
            os.rename(os.path.join(os.path.dirname(os.path.abspath(__file__)), str(Path("TrainYourOwnYOLO/Data/Source_Images/Test_Image_Detection_Results"))) + os.sep + res, f)
            ret.append('ml/' + res)
    
    return render(request, Path('satelite/results.html'), {
        'results': ret
    })

def deleteFiles(request):
    for to_delete in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), str(Path("TrainYourOwnYOLO/Data/Source_Images/Test_Images")))):
        print("Removing file: " + os.path.join(os.path.dirname(os.path.abspath(__file__)), str(Path("TrainYourOwnYOLO/Data/Source_Images/Test_Images/") / to_delete)))
        os.remove(os.path.join(os.path.dirname(os.path.abspath(__file__)), str(Path("TrainYourOwnYOLO/Data/Source_Images/Test_Images/") / to_delete)))
    return index(request)