# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import numpy as np
# import threading
# import random
# import time

# class MyDataClass():

#     def __init__(self):

#         self.XData = [0]
#         self.YData = [0]


# class MyPlotClass():

#     def __init__(self, dataClass):

#         self._dataClass = dataClass

#         self.hLine, = plt.plot(0, 0)

#         self.ani = FuncAnimation(plt.gcf(), self.run, interval = 1000, repeat=True)


#     def run(self, i):  
#         print("plotting data")
#         self.hLine.set_data(self._dataClass.XData, self._dataClass.YData)
#         self.hLine.axes.relim()
#         self.hLine.axes.autoscale_view()


# class MyDataFetchClass(threading.Thread):

#     def __init__(self, dataClass):

#         threading.Thread.__init__(self)

#         self._dataClass = dataClass
#         self._period = 0.25
#         self._nextCall = time.time()


#     def run(self):

#         while True:
#             print("updating data")
#             # add data to data class
#             self._dataClass.XData.append(self._dataClass.XData[-1] + 1)
#             self._dataClass.YData.append(random.randint(0, 256))
#             # sleep until next execution
#             self._nextCall = self._nextCall + self._period;
#             time.sleep(self._nextCall - time.time())


# data = MyDataClass()
# plotter = MyPlotClass(data)
# fetcher = MyDataFetchClass(data)

# fetcher.start()
# plt.show()
# #fetcher.join()


import matplotlib.pyplot as plt
import matplotlib.animation as animation

from matplotlib import style
import numpy as np
import time
import pickle
from termcolor import colored, cprint



def animate(i):
	with open('example', 'rb') as f:
		vi, vo, tc, state = pickle.load(f)
	ax1.clear()
	ax2.clear()
	ax3.clear()
	ax1.imshow(vi)
	ax2.imshow(vo)
	ax3.imshow(tc)
	if state!='NOMINAL':
		color = 'red'
	else:
		color = 'green'
	ax1.set_title('Reality, STATUS: {}'.format(state), color=color)
	ax2.set_title('Decoded, STATUS: {}'.format(state), color=color)
	ax3.set_title('Top cam, STATUS: {}'.format(state), color=color)




if __name__ == "__main__":
	fig = plt.figure(figsize=(10,5))
	fig.suptitle('REAL TIME VISUALS', weight='bold')
	ax1 = fig.add_subplot(1,3,1)
	ax2 = fig.add_subplot(1,3,2)
	ax3 = fig.add_subplot(1,3,3)

	ani = animation.FuncAnimation(fig, animate, interval=250)
	plt.show()

