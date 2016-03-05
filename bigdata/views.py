# -*- coding: utf-8 -*-

from django.shortcuts import render
# from django.http import HttpResponse

def storeHouse(request):
    return render(request, "bigdata/storeHouse.html")


def dataStore(request):
    if request.method == "POST":
        form_len = len(request.POST.keys())
        input_text_len = form_len - 2

        for num in xrange(input_text_len):
            print "table" + str(num), request.POST.get("table" + str(num), "").strip()
    return render(request, "bigdata/storeHouse.html")
