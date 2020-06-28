# -*- coding: utf-8 -*-

def example1():
	import threading
	import time

	# 对于IO密集型来说，用多线程比较省时间，因为此时对cpu来说没有任务，那它就会切换到其他线程去执行任务
	def sleeping():
		time.sleep(0.05)

	# 对于CPU密集型来说，用多线程没有时间上的优势，因为此时对cpu来说有任务，那它不会会切换到其他线程去执行任务，要等到该任务完成才切换
	# 相当与顺序执行
	def calc():
		s = 0
		for i in range(1000000):
			s += i

	def main1():
		for i in range(100):
			# sleeping()
			calc()

	def main2():
		thread_list = []
		for i in range(100):
			# t = threading.Thread(target=sleeping)
			t = threading.Thread(target=calc)
			t.start()
			thread_list.append(t)

		for t in thread_list:
			t.join()

	start = time.time()
	main1()
	end = time.time()
	print('单线程耗时：{:.4f}s'.format(end - start))
	
	start = time.time()
	main2()
	end = time.time()
	print('多线程耗时：{:.4f}s'.format(end - start))

# 异步编程
def example2():
	import asyncio
	import time

	async def shop(delay, what):
		print(what)
		await asyncio.sleep(delay)
		print("...Out")

	async def calc(what):
		print(what)
		s = 0
		for i in range(100000000):
			s += i
		print("res: {}".format(s // 100000000))


	async def main():
		print(time.ctime(), "Start.")
		await asyncio.gather(
			shop(5, 'buy cloth ...'),
			shop(3, 'buy mobile ...'),
			calc('calc sum ...')
		)
		print(time.ctime(), "End.")

	asyncio.run(main())

example2()
