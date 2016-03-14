# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

from utils.table import table


def storeHouse(request):
    return render(request, "bigdata/storeHouse.html")


def dataStore(request):
    if request.method == "POST":
        sysid = request.POST["sysid"]
        tableList = [table(request.POST[l]) for l in request.POST.keys() if "table" in l]
        response = HttpResponse(content_type="application/x-sh")
        response["Content-Disposition"] = "attachment; filename='i{0}_to_odbs_init.sh'".format(sysid)
        template = get_template("odbs_init.tmp")
        content = {
            "afa_user": "afa",
            "afa_pwd": "afadb",
            "afa_sid": "smnx",
            "sysname": "gkzjzf",
            "tables":  tableList
        }
        response.write(template.render(content))
    return response
