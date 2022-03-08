import time
import asyncio

async def delivery(name: str, mealtime: float):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 식사 완료, {mealtime}시간 소요")
    print(f"{name} 그릇 수거 완료")
    
async def main():
    await asyncio.gather(
        delivery("A", 5),
        delivery("B", 4),
        delivery("C", 3),
    )


if __name__=="__main__":
    asyncio.run(main())
