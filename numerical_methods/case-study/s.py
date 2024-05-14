#fast fourier transform
import numpy as np
import matplotlib.pyplot as mp
import scipy.fftpack

while True:
	inp=input("Input either 'yearly', 'monthly-smoothed', 'monthly', or 'daily':\n").lower()
	if(inp=="yearly"):
		file = open("SN_y_tot_V2.0.txt", "r")
		content,year,sunspots=[],[],[]

		ctr=0
		while True:
			line=file.readline()
			if not line:
				break
			content.append(list(filter(None,line.split(" "))))
			year.append(float(content[ctr][0]))
			sunspots.append(float(content[ctr][1]) if float(content[ctr][1])!=-1 else 0)
			ctr+=1
		print("Year data:\n",year,'\n')
		print("Sunspots data:\n",sunspots,'\n\n')
		divider=1
		break
	elif(inp=="monthly-smoothed"):
		file = open("SN_ms_tot_V2.0.txt", "r")
		content,year,sunspots=[],[],[]

		ctr=0
		while True:
			line=file.readline()
			if not line:
				break
			content.append(list(filter(None,line.split(" "))))
			year.append(float(content[ctr][2]))
			sunspots.append(float(content[ctr][3]) if float(content[ctr][3])!=-1 else 0)
			ctr+=1
		print("Year data:\n",year,'\n')
		print("Sunspots data:\n",sunspots,'\n\n')
		divider=12
		break
	elif(inp=="monthly"):
		file = open("SN_m_tot_V2.0.txt", "r")
		content,year,sunspots=[],[],[]

		ctr=0
		while True:
			line=file.readline()
			if not line:
				break
			content.append(list(filter(None,line.split(" "))))
			year.append(float(content[ctr][2]))
			sunspots.append(float(content[ctr][3]) if float(content[ctr][3])!=-1 else 0)
			ctr+=1
		print("Year data:\n",year,'\n')
		print("Sunspots data:\n",sunspots,'\n\n')
		divider=12
		break
	elif(inp=="daily"):
		file = open("SN_d_tot_V2.0.txt", "r")
		content,year,sunspots=[],[],[]

		ctr=0
		while True:
			line=file.readline()
			if not line:
				break
			content.append(list(filter(None,line.split(" "))))
			year.append(float(content[ctr][3]))
			sunspots.append(float(content[ctr][4]) if float(content[ctr][4])!=-1 else 0)
			ctr+=1
		print("Year data:\n",year,'\n')
		print("Sunspots data:\n",sunspots,'\n\n')
		divider=0
		break

file.close()

fig,data=mp.subplots()
data.title.set_text('Plot of Wolf sunspot number versus year')
data.set_xlabel('Year')
data.set_ylabel('Sunspots')
data.plot(year,sunspots)


y=scipy.fftpack.fft(sunspots)
n=len(y)

period,power=[],[]
for i in range(1,n//2):
	if(int(year[i])%4==0 and (int(year[i])%100!=0 or int(year[i])%400==0) and not divider):
		divider=366
	elif(not divider):
		divider=365

	period.append(n/i/divider)
	power.append(abs(y[i])**2)
print("Period data:\n",period,'\n')
print("Power data:\n",power,'\n\n')

print("Peak of sunspots:",period[power.index(max(power))],"years")

fig,fourier=mp.subplots()
fourier.title.set_text('Power spectrum for Wolf sunspot numbers')
fourier.set_xlabel('Period (years)')
fourier.set_ylabel('Power')
mp.xlim(0,30)
fourier.plot(period,power)
mp.show()