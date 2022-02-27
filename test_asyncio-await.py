import asyncio

async def main():
	print('hello,'.capitalize())
	x = input('what is your name?  >>> ' )
	await asyncio.sleep(5)
	print(':'*20)
	await asyncio.sleep(3)
	res = x 
	print(res.upper(), end='')
	print(' owns detechtive.app')
	
async def x():
    await asyncio.sleep(2)
    
print('console chat'.upper())
asyncio.run(x())
	
asyncio.run(main())


