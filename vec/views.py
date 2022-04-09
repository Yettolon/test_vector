import os
import csv
import pyexcel
from io import TextIOWrapper
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from vector.settings import MEDIA_ROOT


from .utilities import count_vectorizer, tfid_vectorizer, word_vectorizer


def index(request):
    if request.method == 'GET':
        c = [[1,2],[2,3],[3,4]]
        return render(request,'index.html', {'c':c})
    if request.method == 'POST' and request.FILES['file']:
        if request.FILES['file'].name[-5:] == '.xlsx':
            myfile = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            list_data = pyexcel.get_array(file_name=MEDIA_ROOT + '/' + filename)
            os.remove(MEDIA_ROOT + '/' + filename)
        else:
            myfile = TextIOWrapper(request.FILES['file'].file,
                                    encoding=request.encoding)
            file_reader = csv.reader(myfile, delimiter = ",")
            list_data = [[i[0],i[1],i[2]] for i in file_reader]
        if '_wordvec' in request.POST:
            list_data = word_vectorizer(list_data)
        elif '_tfidfvectorizer' in request.POST:
            list_data = tfid_vectorizer(list_data)
        elif '_countvectorizer' in request.POST:
            list_data = count_vectorizer(list_data)
        x = [i[3][0] for i in list_data]
        y = [i[3][1] for i in list_data]
        colors = [i[4] for i in list_data]
        context = {'x':x,'y':y,'coloors':colors}
        return render(request,'index.html', context)



