# -*- coding: utf-8 -*-
import os

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from utils import conf
from utils import configer
from utils.table import table


def storeHouse(request):
    return render(request, "bigdata/storeHouse.html")


def dataStore(request):
    if request.method == "POST":
        sysid = request.POST["sysid"]
        tableList = [request.POST[tb] for tb in request.POST.keys() if "table" in tb]
        tables = map(lambda x: table(x), tableList)

        save_dir = os.path.join("temp", sysid)

        if not os.path.exists(save_dir):
            os.mkdir(save_dir)

        parser = configer.baseparser("conf/db.conf")
        section = parser[conf.DEV_ENV]
        content = {
            "afa_user" : section.user,
            "afa_pwd"  : section.password,
            "afa_sid"  : section.sid,
            "sysname"  : "gkzjzf",
            "tables"   : tables
        }

        init_template = get_template("odbs_init.tmp")
        init_file = os.path.join(save_dir, "i{0}_to_odbs_init.sh".format(sysid))
        init_content = init_template.render(Context(content))
        with open(init_file, 'wb') as fi:
            fi.write(init_content.encode(conf.SH_ENCODING))

        response = HttpResponse(content_type="application/x-sh")
        response["Content-Disposition"] = "attachment; filename='i{0}_to_odbs_init.sh'".format(sysid)
        response.write(init_content)
    return response
