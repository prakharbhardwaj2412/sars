from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('firstApp/index.html')
    return HttpResponse(template.render())

def inputData(request):
    if request.method == "GET":
        print("###############################################################")
        data = request.GET['input_data']
        return_data = POS(data)
        template = loader.get_template('firstApp/index.html')
        print(return_data)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        return HttpResponse(template.render({'data': return_data}, request))





##################################################################################################

def POS(data):
#     ====================================================================================================
    def step1Fun(para1):
        para1.strip()
        return((para1.strip()).split('।\PU'))
#     ====================================================================================================
    def step2Fun(para2):
        arr2 = []
        for i in para2:
            for j in ((i.strip()).split('\CSB')):
                for k in (j.split('-\PU')):
                    arr2.append(k)
        return(arr2)
#     ======================================================================================================
    def step3Fun(para3):
        arr3 = []
        arr3a = []
        arr3b = []
        arr3c = []
        for i in para3:
            if ( (i.find('\V.act') != -1) or (i.find('\V.pass') != -1) ):
                arr3a.append(i)
            if ( (i.find('KDP') != -1 ) or (i.find('KDG') != -1) ):
                a = ((i.strip()).split(" "))
                if ( a[-1].find("KDP") != -1 or a[-1].find('KDG') != -1 ):
                    arr3b.append(i)
                if (  (a[-2].find("KDP") != -1 or a[-2].find('KDG') != -1) and ( a[-2].find("च") != -1 )  ):
                    arr3c.append(i)
        arr3.append(arr3a)
        arr3.append(arr3b)
        arr3.append(arr3c)
        return(arr3)
#     ======================================================================================================
    def step4Fun(para4):
        tagset1 = [
            #     NP
            "NP.mas.sg.nom", "NP.fem.sg.nom", "NP.neu.sg.nom",
            "NP.mas.du.nom", "NP.fem.du.nom", "NP.neu.du.nom",
            "NP.mas.pl.nom", "NP.fem.pl.nom", "NP.neu.pl.nom",
            #     \NC
            "NC.mas.sg.nom", "NC.fem.sg.nom", "NC.neu.sg.nom",
            "NC.mas.du.nom", "NC.fem.du.nom", "NC.neu.du.nom",
            "NC.mas.pl.nom", "NC.fem.pl.nom", "NC.neu.pl.nom",
            #     \PPR
            "PPR.mas.sg.nom", "PPR.fem.sg.nom", "PPR.neu.sg.nom",
            "PPR.mas.du.nom", "PPR.fem.du.nom", "PPR.neu.du.nom",
            "PPR.mas.pl.nom", "PPR.fem.pl.nom", "PPR.neu.pl.nom"
        ]
        tagset2 = [
            "NP.mas.sg.nom", "NP.fem.sg.nom", "NP.neu.sg.nom",
            "NC.mas.sg.nom", "NC.fem.sg.nom", "NC.neu.sg.nom",
            "PPR.mas.sg.nom", "PPR.fem.sg.nom", "PPR.neu.sg.nom"
        ]
        tagset3 = [
            "NP.mas.du.nom", "NP.fem.du.nom", "NP.neu.du.nom",
            "NC.mas.du.nom", "NC.fem.du.nom", "NC.neu.du.nom",
            "PPR.mas.du.nom", "PPR.fem.du.nom", "PPR.neu.du.nom",
        ]
        tagset4 = [
            "NP.mas.pl.nom", "NP.fem.pl.nom", "NP.neu.pl.nom",
            "NC.mas.pl.nom", "NC.fem.pl.nom", "NC.neu.pl.nom",
            "PPR.mas.pl.nom", "PPR.fem.pl.nom", "PPR.neu.pl.nom"
        ]
        #     step 4
        arr1 = []
        loop4 = para4[0]
        for i in range(len(loop4)):
            flag = 0
            for j in tagset1:
                if( loop4[i].find(j) != -1 ):
                    flag = 1
                    break
                else:
                    if(i==1):
                        if ( loop4[i-1].find(j) != -1 ):
                            arr1.append({
                                "id": i,
                                "C": loop4[i],
                                "Status": loop4[i-1]
                            })
                            flag = 2
                            break
                    elif(i>2):
                        for k in range (i-1, i-4, -1):
                            if ( loop4[k].find(j) != -1 ):
                                if ( loop4[i-1].find(j+".i नाम") != -1 ):
                                    arr1.append({
                                        "id": i,
                                        "C": loop4[i],
                                        "Status": loop4[k]
                                    })
                                    flag =2
                                    break
                                else:
                                    arr1.append({
                                        "id": i,
                                        "C": loop4[i],
                                        "Status": loop4[k]
                                    })
                                    flag = 2
                                    break
                if(flag == 2):
#                     arr1.append({
#                         "id": i,
#                         "C": loop4[i],
#                         "Status": "unknown"
#                     })
                    break
                                
            if( flag == 1 ):
                arr1.append({
                    "id": i,
                    "C": loop4[i],
                    "Status": "unknown"
                })
                continue
        #     step 4a
        loop4a = step3[1]
        for i in loop4a:
            flag = 0
            if ( i.find("\V.act.du") != -1 ):
                for j in range(length(tagset2)):
                    if ( i.find(tagset3[j]) != -1  or i.count(tagset2[j]) == 2 ):
                        flag = 1
                        break
                    else:
                        if(i>2):
                            for k in range (i-1, i-4, -1):
                                if ( i.find(tagset3[j]) == -1  or i.count(tagset2[j]) != 2 ):
                                    arr1.append({
                                        "id": i,
                                        "C": loop4a[i],
                                        "Status": loop4a[k]
                                    })
                                    flag = 2
                                    break
                    if flag == 2:
                        break
                                    
                if flag == 1:
                    arr1.append({
                        "id": i,
                        "C": loop4a[i],
                        "Status": "unknown"
                    })
                    continue
                       
        #     step 4b
        loop4b = step3[2]
        for i in loop4b:
            flag = 0
            if ( i.find("\V.act.pl") != -1 ):
                for j in range(len(tagset2)):
                    if ( i.find(tagset4[j]) != -1 or i.find(tagset2[j]) >= 3 ):
                        flag = 1
                        break
                    else:
                        if(i>2):
                            for k in range (i-1, i-4, -1):
                                if ( i.find(tagset4[j]) == -1 or i.find(tagset2[j]) >= 3 ):
                                    arr1.append({
                                        "id": i,
                                        "C": loop4b[i],
                                        "Status": loop4b[k]
                                    })
                                    flag = 2
                                    break
                    if flag == 2:
                        break
                if flag==1:
                    arr1.append({
                        "id": i,
                        "C": loop4b[i],
                        "Status": "unknown"
                    })
                    continue
        return arr1
#     ======================================================================================================
    def step6Fun (para6):
        tagset1 = [
            #     NP
            "NP.mas.sg.nom", "NP.fem.sg.nom", "NP.neu.sg.nom",
            "NP.mas.du.nom", "NP.fem.du.nom", "NP.neu.du.nom",
            "NP.mas.pl.nom", "NP.fem.pl.nom", "NP.neu.pl.nom",
            #     \NC
            "NC.mas.sg.nom", "NC.fem.sg.nom", "NC.neu.sg.nom",
            "NC.mas.du.nom", "NC.fem.du.nom", "NC.neu.du.nom",
            "NC.mas.pl.nom", "NC.fem.pl.nom", "NC.neu.pl.nom",
            #     \PPR
            "PPR.mas.sg.nom", "PPR.fem.sg.nom", "PPR.neu.sg.nom",
            "PPR.mas.du.nom", "PPR.fem.du.nom", "PPR.neu.du.nom",
            "PPR.mas.pl.nom", "PPR.fem.pl.nom", "PPR.neu.pl.nom"
        ]
        tagset2 = [
            "NP.mas.sg.nom", "NP.fem.sg.nom", "NP.neu.sg.nom",
            "NC.mas.sg.nom", "NC.fem.sg.nom", "NC.neu.sg.nom",
            "PPR.mas.sg.nom", "PPR.fem.sg.nom", "PPR.neu.sg.nom"
        ]
        tagset3 = [
            "NP.mas.du.nom", "NP.fem.du.nom", "NP.neu.du.nom",
            "NC.mas.du.nom", "NC.fem.du.nom", "NC.neu.du.nom",
            "PPR.mas.du.nom", "PPR.fem.du.nom", "PPR.neu.du.nom",
        ]
        tagset4 = [
            "NP.mas.pl.nom", "NP.fem.pl.nom", "NP.neu.pl.nom",
            "NC.mas.pl.nom", "NC.fem.pl.nom", "NC.neu.pl.nom",
            "PPR.mas.pl.nom", "PPR.fem.pl.nom", "PPR.neu.pl.nom"
        ]
#         print(len(para6))
        arr1 = []
        for i in range (0, len(para6)):
            a= (para6[i].strip()).split(" ")
            if ( (a[-1].find("उवाच\V.act") != -1) or (a[-1].find("प्रोवाच\V.act") != -1) or (a[-1].find("ऊचुः\V.act") != -1) or (a[-1].find("प्रोचुः\V.act") != -1) or (a[-1].find("ऊचे\V.act") != -1) or (a[-1].find("आह\V.act") != -1) or (a[-1].find("प्राह\V.act") != -1) ):
                if(i>2):
                    for j in range(i-1, i-4, -1):
                        for k in tagset1:
                            if(para6[j].find(k) != -1):
                                arr1.append({
                                    "id": i,
                                    "C": para6[i],
                                    "Status": para[k]
                                })
                                flag = 1
                                break
                        if flag == 1:
                            break
        return
#     =======================================================================================================
    def step7Fun (para7):
        return
#     =========================================================================================================
    def step8Fun(para8):
        return
#     =========================================================================================================
    step1 = step1Fun(data)
    step2 = step2Fun(step1)
    step3 = step3Fun(step2)
    step4 = step4Fun(step3)
    step6 = step6Fun(step3[0])
    if( step6 is None ):
        print("hello")
    else:
        for i in step6:
            step4.append(i)
#         print("##")
    
    for i in step4:
        a = (i['C']).split(" ")
        i["code"] = a[1]
    for i in step4:
        a = (i['Status']).split(" ")
        for j in a:
            if (j.find("NP") != -1 or j.find("NC") != -1 or j.find("PPR") != -1):
                i["S"] = j
                break
            else:
                i["S"] = ""
   
    return step4