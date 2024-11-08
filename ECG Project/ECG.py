# -*- coding: utf-8 -*-
"""BMD201_ECG_Lab.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wK-2NoV9LVAXB1hTMYmbTSG-BKNG38XN

# ECG Lab

**Part 1:**
Reading CSV File
"""

import pandas as pd

data= pd.read_csv("/samples.csv")

data

"""**Part 2**: Data Engineering"""

type(data)

#Skip first row

data= pd.read_csv("/samples.csv", skiprows=[0])

data

#rename columns
data = data.rename(columns = {data.columns[0]:"Time"	,data.columns[1]:"ECG",data.columns[2]:"ECGFiltered"})

data

data.Time

#PLot Data
import matplotlib.pyplot  as plt

type(data.Time)

type(data.Time[0])

#plot original signal
fig = plt.figure(figsize=(15,4))
figure_details = fig.add_subplot()
figure_details.set_ylabel('mV')
figure_details.set_xlabel('seconds')
figure_details.set_title('ECG Signal')
figure_details.plot(data.Time,data.ECG)
plt.show()

#plot original signal [zoom in]
fig = plt.figure(figsize=(15,4))
figure_details = fig.add_subplot()
figure_details.set_ylabel('mV')
figure_details.set_xlabel('seconds')
figure_details.set_title('ECG Signal')
figure_details.plot(data.Time[0:15],data.ECG[0:15])
plt.show()

#determine sapling rate by observation delta t= 0.002 => fs= 1/0.002= 500 hz
fs= 500

#first way to change time axis
## generate time using numpy array
import numpy as np

time= np.arange(0,10, 0.002)

time

#second way to change time axis
## modify orginal time column

print(data.Time[0].split(":"))

time2=data.Time.map(lambda x: x.replace("'", ""))

type(time2[0])

time2[0].split(":")

time3=time2.map(lambda x:x.split(":"))

time3

time4 = time3.map(lambda x:x[1])

time4

type(time4[0])

time5= time4.map(lambda x:float(x))

time5

#plot original signal using 1st way
fig = plt.figure(figsize=(15,4))
figure_details = fig.add_subplot()
figure_details.set_ylabel('mV')
figure_details.set_xlabel('seconds')
figure_details.set_title('ECG Signal')
figure_details.plot(time,data.ECG)
plt.show()

#plot original signal 2nd way
fig = plt.figure(figsize=(15,4))
figure_details = fig.add_subplot()
figure_details.set_ylabel('mV')
figure_details.set_xlabel('seconds')
figure_details.set_title('ECG Signal')
figure_details.plot(time5,data.ECG)
plt.show()

"""**Part 3**: Creating a Dummy Window    """

# create 2 varibles window_start , window_end [default window] we took a sample every 0.002 second => at one second we have 500 samples
window_start=0
window_end=fs  #1sec

window_end

#plot first second samples
fig = plt.figure(figsize=(12,8))
fig.subplots_adjust(top=0.8)
figure_details = fig.add_subplot(211)
figure_details.set_ylabel('mV')
figure_details.set_xlabel('seconds')
figure_details.set_title('ECG Signal')
figure_details.plot(time[window_start:window_end] ,data.ECG[window_start:window_end])# [0:500] exlusive 0:499
plt.show()

#plot first 2 seconds samples
fig = plt.figure(figsize=(12,8))
fig.subplots_adjust(top=0.8)
figure_details = fig.add_subplot(211)
figure_details.set_ylabel('mV')
figure_details.set_xlabel('seconds')
figure_details.set_title('ECG Signal')
figure_details.plot(time[window_start:2*window_end] ,data.ECG[window_start:2*window_end])
plt.show()

#plot third second samples
#change window_start
window_start= 2*window_end
window_end= 3*window_end
fig = plt.figure(figsize=(12,8))
fig.subplots_adjust(top=0.8)
figure_details = fig.add_subplot(211)
figure_details.set_ylabel('mV')
figure_details.set_xlabel('seconds')
figure_details.set_title('ECG Signal')
figure_details.plot(time[window_start:window_end] ,data.ECG[window_start:window_end])
plt.show()

"""Q1: Creat a function that takes secondNumber, windowSize, and smaplingRate then returns a tuple of windowStart, windowEnd

Examples:


*    Case1 show the 4th second
*    Case2 show the half of the 4th second
*    Case3 show the last 2 seconds

<hr>Case1: input: 4, 1sec, 500HZ
output: (1500, 2000)

<hr>Case2: input: 4, 0.5 sec, 500HZ
output: (1500, 1750)

<hr>Case3: input: 9, 2 sec, 500HZ
output: (4000 ,5000)



"""

def getwindowBorders(secondNumber, windowSize, samplingRate):
  #writ your code
    window_start=(secondNumber-1)*samplingRate
    x=windowSize*samplingRate
    window_End=window_start+x
    return window_start,window_End
    pass

#Compare Your Result
#Case 1
fs=500
window_start,window_End= getwindowBorders(4,1,fs)
print(window_start,window_End)
fig = plt.figure(figsize=(12,8))
fig.subplots_adjust(top=0.8)
figure_details = fig.add_subplot(211)
figure_details.set_ylabel('mV')
figure_details.set_xlabel('seconds')
figure_details.set_title('ECG Signal')
figure_details.plot(time[window_start:window_End] ,data.ECG[window_start:window_End])
plt.show()

#Compare Your Result
#Case 2
window_start,window_End= getwindowBorders(4,0.5,fs)
print(window_start,window_End)
fig = plt.figure(figsize=(12,8))
fig.subplots_adjust(top=0.8)
figure_details = fig.add_subplot(211)
figure_details.set_ylabel('mV')
figure_details.set_xlabel('seconds')
figure_details.set_title('ECG Signal')
figure_details.plot(time[window_start:window_End] ,data.ECG[window_start:window_End])
plt.show()

#Compare Your Result
#Case 3
window_start,window_End= getwindowBorders(9,2,fs)
print(window_start,window_End)
fig = plt.figure(figsize=(12,8))
fig.subplots_adjust(top=0.8)
figure_details = fig.add_subplot(211)
figure_details.set_ylabel('mV')
figure_details.set_xlabel('seconds')
figure_details.set_title('ECG Signal')
figure_details.plot(time[window_start:window_End] ,data.ECG[window_start:window_End])
plt.show()

"""**Part 4:** HeartPy Library"""

!pip install heartpy

import heartpy as hp

#applying low pass filter in order to attenuate frequincies above 50 hz
filteredSignal = hp.filter_signal(data.ECG, cutoff =10, sample_rate = fs, order = 1, filtertype='lowpass')

#plot and compare orginal signal to filtered signal

fig = plt.figure(figsize=(12,8))
fig.subplots_adjust(top=0.8)
figure_details = fig.add_subplot(211)
figure_details.set_ylabel('mV')
figure_details.set_xlabel('seconds')
figure_details.set_title('ECG Signal')
figure_details.plot(time,data.ECG)
figure_details.plot(time,filteredSignal)
plt.show()

"""Q2: Apply a notch filter to the ECG signal to supress 0.05Hz frequency then show your result by plotting as above <br>
Note: this frequency may be due to respiration or the motion of the patients or the instruments.
"""

# Write your Code
import pandas as pd
data= pd.read_csv("/samples.csv")
data= pd.read_csv("/samples.csv", skiprows=[0])
data = data.rename(columns = {data.columns[0]:"Time",data.columns[1]:"ECG",data.columns[2]:"ECGFiltered"})
import matplotlib.pyplot  as plt
import numpy as np
time= np.arange(0,10, 0.002)
time2=data.Time.map(lambda x: x.replace("'", ""))
time3=time2.map(lambda x:x.split(":"))
time4 = time3.map(lambda x:x[1])
time5= time4.map(lambda x:float(x))
import heartpy as hp
newfilteredsignal=hp.filter_signal(data.ECG, cutoff = 0.05, sample_rate = 500.0, filtertype='notch')
fig=plt.figure(figsize=(12,8))
figure_details= fig.add_subplot(211)
figure_details.set_ylabel('mv')
figure_details.set_xlabel('seconds')
figure_details.set_title('ECG signal')
figure_details.plot(time,data.ECG)
figure_details.plot(time,newfilteredsignal)
plt.show()

"""Q3: Apply high pass filter to attenuate frequencies below 15 hz and show your result"""

import pandas as pd
data= pd.read_csv("/samples.csv")
data= pd.read_csv("/samples.csv", skiprows=[0])
data = data.rename(columns = {data.columns[0]:"Time"	,data.columns[1]:"ECG",data.columns[2]:"ECGFiltered"})

import numpy as np
time= np.arange(0,10, 0.002)
time2=data.Time.map(lambda x: x.replace("'", ""))
time3=time2.map(lambda x:x.split(":"))
time4 = time3.map(lambda x:x[1])
time5= time4.map(lambda x:float(x))
import heartpy as hp
new_filteredsignal =hp.filter_signal(data.ECG, cutoff = 15, sample_rate = 500.0, order = 3, filtertype='highpass')
import matplotlib.pyplot  as plt
fig=plt.figure(figsize=(12,8))
figure_details= fig.add_subplot(211)
figure_details.set_ylabel('mv')
figure_details.set_xlabel('seconds')
figure_details.set_title('ECG signal')
figure_details.plot(time,data.ECG)
figure_details.plot(time,new_filteredsignal)
plt.show()

"""
Q4: Apply a smoothing filter to the ECG signal then show your result <br>


"""

#write your Code
import pandas as pd
data= pd.read_csv("/samples.csv")
data= pd.read_csv("/samples.csv", skiprows=[0])
data = data.rename(columns = {data.columns[0]:"Time"	,data.columns[1]:"ECG",data.columns[2]:"ECGFiltered"})

import numpy as np
time= np.arange(0,10, 0.002)
time2=data.Time.map(lambda x: x.replace("'", ""))
time3=time2.map(lambda x:x.split(":"))
time4 = time3.map(lambda x:x[1])
time5= time4.map(lambda x:float(x))
import heartpy as hp
new_filteredsignal_1 =hp.smooth_signal(data.ECG,sample_rate=500,window_length=50,polyorder=2)
import matplotlib.pyplot  as plt
fig=plt.figure(figsize=(12,8))
figure_details= fig.add_subplot(211)
figure_details.set_ylabel('mv')
figure_details.set_xlabel('seconds')
figure_details.set_title('ECG signal')
figure_details.plot(time,data.ECG)
figure_details.plot(time,new_filteredsignal_1)
plt.show()

#Calculted measures
wd, m = hp.process(data.ECGFiltered,fs)

plt.figure(figsize=(20,4))
hp.plotter(wd, m)

for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))

"""Q5: Calaculate the following from Data.ECG"""

#find the maximum value using numpy library
import numpy
maximum_value = numpy.max(data.ECG)
print(maximum_value)

#implement a function that returns the maximum value then compare your result with numpy library
import pandas as pd
data= pd.read_csv("/samples.csv")
data= pd.read_csv("/samples.csv", skiprows=[0])
data = data.rename(columns = {data.columns[0]:"Time"	,data.columns[1]:"ECG",data.columns[2]:"ECGFiltered"})

import numpy as np
time= np.arange(0,10, 0.002)
time2=data.Time.map(lambda x: x.replace("'", ""))
time3=time2.map(lambda x:x.split(":"))
time4 = time3.map(lambda x:x[1])
time5= time4.map(lambda x:float(x))

# df = pd.DataFrame(data [data.columns[0]:"Time",data.columns[1]:"ECG",data.columns[2]:"ECGFiltered"})

# data = pd.read_csv('/samples.csv')
data.dropna(inplace=True)
shows = pd.DataFrame(data['ECG'].head())

shows.sort_values(by=['ECG'])

lgtlength = shows['ECG'].idxmax()

max_value = shows.loc[lgtlength, 'ECG']

print("The Largest Number in smtlgtarr Numpy Array = ", max_value)

data['ECG']

#find the minimum value using numpy library
import numpy
minimum_value = numpy.min(data.ECG)
print(minimum_value)

#implement a function that returns the minimum value then compare your result with numpy library

import pandas as pd
data= pd.read_csv("/samples.csv")
data= pd.read_csv("/samples.csv", skiprows=[0])
data = data.rename(columns = {data.columns[0]:"Time"	,data.columns[1]:"ECG",data.columns[2]:"ECGFiltered"})

import numpy as np
time= np.arange(0,10, 0.002)
time2=data.Time.map(lambda x: x.replace("'", ""))
time3=time2.map(lambda x:x.split(":"))
time4 = time3.map(lambda x:x[1])
time5= time4.map(lambda x:float(x))

#df = pd.DataFrame(data [data.columns[0]:"Time",data.columns[1]:"ECG",data.columns[2]:"ECGFiltered"})

# data = pd.read_csv('/samples.csv')
data.dropna(inplace=True)
shows = pd.DataFrame(data['ECG'].head())

shows.sort_values(by=['ECG'])

min_value = shows['ECG'].iloc[0]
print("The Smallest Number in smtlgtarr Numpy Array = ", min_value)

#find the mean using numpy library
import numpy
mean_value = numpy.mean(data.ECG)
print(mean_value)

#implement a function that returns the mean then compare your result with numpy library
import pandas as pd
data= pd.read_csv("/samples.csv")
#implement a function that returns the mean then compare your result with numpy library
import pandas as pd
data= pd.read_csv("/samples.csv")
data= pd.read_csv("/samples.csv", skiprows=[0])
data = data.rename(columns = {data.columns[0]:"Time"	,data.columns[1]:"ECG",data.columns[2]:"ECGFiltered"})
def calculate_mean(data):
    total_sum = sum(data['ECG'])
    num_elements = len(data['ECG'])
    mean = total_sum / num_elements
    return mean
calculate_mean(data)

#Calculate the median using numpy library
import numpy
median_value = numpy.median(data.ECG)
print(median_value)

#implement a function that returns the median then compare your result with numpy library
def calculate_median(data):
    """
    Calculates the median of a list of numbers.
    """
    # Sort the data:
    sorted_data = sorted(data)

    # Get the length of the data:
    n = len(sorted_data)

    # Calculate the median:
    if n % 2 == 0:
        # If the length of the data is even, the median is the average of the two middle values
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        median = (mid1 + mid2) / 2
    else:
        # If the length of the data is odd, the median is the middle value
        median = sorted_data[n // 2]

    return median

# Calculate the median using the custom function
custom_median = calculate_median(data['ECG'])

# Calculate the median using NumPy
numpy_median = np.median(data['ECG'])

# Compare the results
print("Median calculated using custom function:", custom_median)
print("Median calculated using NumPy:", numpy_median)

calculate_median(data)