from django.shortcuts import render

# Create your views here.
def moviesinfo(request):
    my_dict={'head_msg':'Movies Information','sub_msg1':'this is charan kumar','sub_msg2':'how are u'

    }
    return render(request,'news.html',context=my_dict)

def sportsinfo(request):
    my_dict={'head_msg':'Sports Information',
             'sub_msg1':'page information',
             'sub_msg2':'i m not hero'

    }
    return render(request,'news.html',context=my_dict)

def index(request):
    return render(request,'index.html')