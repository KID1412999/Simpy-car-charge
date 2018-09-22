import simpy
import random
count=0#充电次数
def car(env, name, bcs, driving_time, charge_duration):
	global count
	parking_duration=1
	while True:
		print('%s 开始行驶 %d' % (name, env.now))
		yield env.timeout(driving_time)
		print('%s 开始停车 %d' % (name, env.now))
		#yield env.timeout(parking_duration)
		with bcs.request() as req:
			yield req
			print('%s 开始充电 %s' % (name, env.now))
			yield env.timeout(charge_duration)
			print('%s 停止充电 %s' % (name, env.now))
			count+=1
			print('累计充电次数'+str(count))
def charge(env):
	yield env.timeout(3)
env=simpy.Environment()
bcs=simpy.Resource(env, capacity=3)
for i in range(10):#生成100辆电动汽车
	env.process(car(env, 'Car %d' % i, bcs,random.randint(1,8),random.randint(8,10)))
env.run(until=100)

		
