from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Covid
from .models import Patients
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail
from django.conf import settings
import random
import bs4
import requests

def index(request):
	try:
		return render(request,'Covid/index.html')
	except:
		return render(request,'Covid/NotFound.HTML')
def ContactUs(request):
	try:
		return render(request,'Covid/ContactUs.html')
	except:
		return render(request,'Covid/NotFound.HTML')

def AboutProject(request):
	try:
		return render(request,'Covid/AboutProject.html')
	except:
		return render(request,'Covid/NotFound.html')
def InsertPositionLogin(request):
	try:
		return render(request,'Covid/PositionLogin.html')

	except:
		return HttpResponse("<h1>You did Something wrong")
def InsertSimtermLogin(request):
	try:
		return render(request,'Covid/SimtermsLogin.html')

	except:
		return HttpResponse("<h1>You did Something wrong")

def LoginSimtermsValidation(request):
	try:
		user=request.POST.get('name','DefaultValue')
		password=request.POST.get('password','DefaultValue')
		if(user=="InsertSimtermsLogin1963" and password=="1963@Insert#SimtermsLogin1963"):
			request.session['simterms']=1
			return render(request,'Covid/InsertSimtermDataSet.html')
		else:
			return render(request,'Covid/NotFound.html')
	except:
		return render(request,'Covid/NotFound.html')

def LoginPositionValidation(request):
	print("jgh")
	try:

		user=request.POST.get('name','DefaultValue')
		password=request.POST.get('password','DefaultValue')
		if(user=="InsertPositionLogin1963" and password=="1963@Insert#PositionLogin1963"):
			request.session['position']=1
			return render(request,'Covid/InsertPosition.html')
		else:
			return render(request,'Covid/NotFound.html')
	except:
		return render(request,'Covid/NotFound.html')

def SubmissionInsertPosition(request):
	try:
		if(request.session['position']==1):
			print("dddddddddddddddddddjddffgfd")
			ci=request.POST.get('City','DeeaultValue')
			longti=request.POST.get('Longitude','DefaultValue')
			lati=request.POST.get('Latitude','DefaultValue')
			print(ci)
			patient=Patients(latitude=lati,longitude=longti,city=ci)
			patient.save()
			return HttpResponse("<center><h2>Data has been Saved</h2><br><a href='/'>Back to home</a></center>")
		else:
			return render(request,'Covid/PositionLogin.html')
	except:
		return render(request,'Covid/NotFound.html')

def SubmissionInsertSimterms(request):
	try:
		if(request.session['position']==1):
			print("dddddddddddddddddddjddffgfd")
			ag=request.POST.get('Age','DeeaultValue')
			brt=request.POST.get('Breath','DefaultValue')
			fvr=request.POST.get('Fever','DefaultValue')
			bp=request.POST.get('BodyPain','DeeaultValue')
			rn=request.POST.get('RunnyNose','DefaultValue')
			co=request.POST.get('Cough','DefaultValue')
			inf=request.POST.get('Infection','DefaultValue')
			
			
			miss=Covid(Age=ag,Fever=fvr,Cough=co,BodyPain=bp,RunnyNose=rn,Breath=brt,InfectionProb=inf)
			miss.save()
			return HttpResponse("<center><h2>Data has been Saved</h2><br><a href='/'>Back to home</a></center>")
		else:
			return render(request,'Covid/PositionLogin.html')
	except:
		return render(request,'Covid/NotFound.html')



def Landing(request):
	try:
		return render(request,'Covid/Landing.html')
	except:
		return render(request,'Covid/NotFound.HTML')
def login(request):
	try:	
		return render(request,'Covid/login.html')
	except:
		return render(request,'Covid/NotFound.HTML')
def Find(request):
	try:
		return render(request,'Covid/FindLocation.HTML')
	except:
		return render(request,'Covid/NotFound.HTML')
def FindLocation(request):
	try:
		la1=request.POST.get('Lat','DeeaultValue')
		long1=request.POST.get('Long','DeeaultValue')
		city=request.POST.get('city','DeeaultValue')
		dist=int(4500)
		d1=0
		d2=0
		d3=0
		d4=0
		d5=0
		from math import radians,cos,sin,asin,sqrt
		def distance(lat1,lat2,lon1,lon2):
		    lon1=radians(float(lon1))
		    lon2=radians(float(lon2))
		    lat1=radians(float(lat1))
		    lat2=radians(float(lat2))
		    dlon=lon2-lon1
		    dlat=lat2-lat1
		    a=sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlon/2)**2
		    c=2*asin(sqrt(a))
		    r=6371
		    return(c*r)
		try:
			per=Patients.objects.filter(Q(city=city))
		except:
			return render(request,'Covid/NotFound.HTML')
		#print("Latitude ============"+str(per))
		l=len(per)
		latt1=la1
		lonn1=long1
		lt=[]
		lo=[]
		BetwDis=[]
		for i in range(l):
			q1=per[i].latitude
			q2=per[i].longitude
			import math
			re=(math.floor(distance(latt1,q1,lonn1,q2)))
			print(re)		
			
			if dist>re:
				lt.append(q1)
				lo.append(q2)
				BetwDis=re
				if(re==5):
					d5=d5+1
				elif(re==4):
					d4=d4+1
				elif(re==3):
					d3=d3+1
				elif(re==2):
					d2=d2+1
				elif(re==1):
					d1=d1+1
				print(per[i].city)



		
		return render(request,'Covid/ShowPeople.html',{'dis':d1+d2+d3+d4+d5,'dis1':d1,'dis2':d2,'dis3':d3,'dis4':d5,'dis5':d5})#HttpResponse(f"Latitude = {latt1}\n Longitude = {lonn1} City ={city}")
	except:
		return render(request,'Covid/NotFound.HTML')

def process(request):
	try:
		mp=request.FILES['pic']
		email=request.POST.get('Email','DeeaultValue')
		name=request.POST.get('name','DeeaultValue')
		age=request.POST.get('Age','DeeaultValue')
		#gender=request.POST.get('Gender','DeeaultValue')
		fever=request.POST.get('Fever','DeeaultValue')
		bodypain=request.POST.get('BodyPain','DeeaultValue')
		cough=request.POST.get('Cough','DeeaultValue')
		runnynose=request.POST.get('RunnyNose','DeeaultValue')
		breath=request.POST.get('Breath','DeeaultValue')

		import pandas as pd
		import numpy as numpy
		from sklearn import linear_model
		per=Covid.objects.filter	()
		l=len(per)
		length=[]
		dAge=[]
		#dGender=[]
		dFever=[]
		dBreath=[]
		dBodyPain=[]
		dRunnyNose=[]
		dCough=[]
		dInfection=[]
		for i in range(l):
			dAge.append(per[i].Age)
			#dGender.append(per[i].Gender)
			dFever.append(per[i].Fever)
			dBodyPain.append(per[i].BodyPain)
			dRunnyNose.append(per[i].RunnyNose)
			dCough.append(per[i].Cough)
			dBreath.append(per[i].Cough)
			dInfection.append(per[i].InfectionProb)
			length=i
		#print("Hello")

		dict1={
			"Age":dAge,
			#"Gender":dGender,
			"Fever":dFever,
			"BodyPain":dBodyPain,
			"RunnyNose":dRunnyNose,
			"Cough":dCough,
			"Breath":dBreath,
			"InfectionProb":dInfection
		}
		for i in range(l):
				df=pd.DataFrame(dict1)
		
		df=df[df['InfectionProb']!=""]
		X=df.drop(['InfectionProb'],axis=1)
		Y=df.InfectionProb
		reg=linear_model.LogisticRegression()#print(df)
	#print(Y)
		reg.fit(X,Y)
		tst=dict()
		tst['ag']=age
		tst['fvr']=fever
		tst['bdypn']=bodypain
		tst['runnse']=runnynose
		tst['cou']=cough
		tst['breathProb']=breath
		rst=pd.DataFrame(tst,index=[0])
		Result=reg.predict(rst)
		
		if(Result=='0'):
			mess="you are absolute good we recommend you should not go for testing"
		elif(Result=='1'):
			mess="you are not so well we recommend you should go for testing"
		#
		
		

		#


		miss=Covid(pic=mp,Full_Name=name,Email=email,Age=age,Fever=fever,Cough=cough,BodyPain=bodypain,RunnyNose=runnynose,Breath=breath)
		miss.save()
		
		print("Result ="+str(Result))
		return render(request,"Covid/result.html",{'val':Result,'Name':name,'message':mess})
	except:
		return render(request,'Covid/NotFound.HTML')


def Analysis(request):
	try:
		url="https://www.worldometers.info/coronavirus/"
		data=requests.get(url)
		soup=bs4.BeautifulSoup(data.text,'html.parser')
		# Total Cases


		l=11
		totalCase=""
		NewCase=""
		DeathCase=""
		q="Total:"
		for i in soup.findAll('td'):
		    if(i.getText()==q):
		        l=l-1
		        #print(i.getText())
		     
		    elif(l==3):
		        totalCase=i.getText()
		        l=l-1
		    elif(l==2):
		        NewCase=i.getText()
		        l=l-1
		    elif(l==1):
		        DeathCase=i.getText()
		        l=l-1
		        break
		return render(request,"Covid/DataRepresentation.HTML",{'totalCase':totalCase,"NewCase":NewCase,"DeathCase":DeathCase,"Region":"World"})
	except:
		return render(request,'Covid/NotFound.HTML')

def Search(request):
	try:
		url="https://www.worldometers.info/coronavirus/"
		data=requests.get(url)
		soup=bs4.BeautifulSoup(data.text,'html.parser')
		
		q=request.POST.get('Search','DeeaultValue')
		l=0
		totalCase=""
		NewCase=""
		DeathCase=""
		for i in soup.findAll('td'):
		    if(i.getText().upper()==q.upper()):
		        l=4
		        #print(i.getText())
		    elif(l>1):
		        
		        if(l==4):
		            totalCase=i.getText()
		        elif(l==3):
		            NewCase=i.getText()
		        elif(l==2):
		            DeathCase=i.getText()
		            break
		            
		        l=l-1

		return render(request,"Covid/DataRepresentation.HTML",{'totalCase':totalCase,"NewCase":NewCase,"DeathCase":DeathCase,"Region":q})
	except:
		return render(request,'Covid/NotFound.HTML')
