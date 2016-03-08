# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

from  table import table


def storeHouse(request):
    return render(request, "bigdata/storeHouse.html")


def dataStore(request):
    if request.method == "POST":
        # form_len = len(request.POST.keys())
        # input_text_len = form_len - 2
        table0 = table(request.POST.get("table0", "").strip())
        # for num in xrange(input_text_len):
            # print "table" + str(num), request.POST.get("table" + str(num), "").strip()
        response = HttpResponse(content_type="application/x-sh")
        response["Content-Disposition"] = "attachment; filename='a.sh'"
        template = get_template("odbs_init.tmp")
        content = {
            "afa_user": "afa",
            "afa_pwd": "afadb",
            "afa_sid": "smnx",
            "sysname": "gkzjzf",
            "tables": [table0 ]
        }
        response.write(template.render(content))
        # print html
    return response
    # return render(request, "bigdata/storeHouse.html")
