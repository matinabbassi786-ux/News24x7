import python_weather

import asyncio
import os


async def main() -> None:
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    
    weather = await client.get('New York')
    return {
        "temperature":weather.temperature,
        "humidity":weather.humidity,
        "feels_like":weather.feels_like,
        "feels_like":weather.feels_like,
        "description":weather.description,
        "datetime":weather.datetime,
        
    }
    


if __name__ == '__main__':
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  
    q  = asyncio.run(main())
    # print(q['temperature'])
