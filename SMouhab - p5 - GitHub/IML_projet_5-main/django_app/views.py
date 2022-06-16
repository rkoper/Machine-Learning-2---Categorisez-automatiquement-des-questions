import warnings

import pandas as pd
import pickle5 as pickle
from django.shortcuts import render
from joblib import load

from .forms import ContactForm

warnings.simplefilter(action='ignore', category=Warning)

clf = load('/Users/soso/Desktop/IML_P5/clf.joblib')


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            print('*********')
            print(subject)
            str_1,str_2,str_3 = _tag_finder(subject)
            return render(request, "email.html", {'posts_1': str_1,
                                                  'posts_2': str_2,
                                                  'posts_3': str_3,
                                                  'form': form})
    return render(request, "email.html", {'form': form})

y_test = pd.read_csv('/Users/soso/Desktop/IML_P5/y_test.csv')
vectorizer = pickle.load(open("/Users/soso/Desktop/IML_P5/vetorizar.pickle", "rb"))

def _tag_finder(xxx):
    xxx_1 = [xxx]
    xxx_2 = vectorizer.transform(xxx_1)
    xxx_3 = clf.predict_proba(xxx_2)
    xxx_4 = pd.DataFrame(xxx_3, columns=[y_test.columns])
    xxx_5 = xxx_4.T
    xxx_6 = xxx_5.sort_values(by=[0], ascending=False)
    xxx_7 = xxx_6.reset_index().head(3)
    xxx_8 = xxx_7.level_0.values.tolist()
    lst_a = []
    k = 1
    for i in xxx_8:
        b = '#' + str(k) + '    ' + i
        k = k + 1
        lst_a.append(b)

    str_1 = lst_a[0]
    str_2 = lst_a[1]
    str_3 = lst_a[2]

    return str_1,str_2,str_3
