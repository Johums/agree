# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

from utils import conf
from utils import configer
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
        parser = configer.baseparser("conf/db.conf")
        section = parser[conf.DEV_ENV]
        content = {
            "afa_user" : section.user,
            "afa_pwd"  : section.password,
            "afa_sid"  : section.sid,
            "sysname"  : "gkzjzf",
            "tables"   : tableList
        }
        response.write(template.render(content))
    return response
