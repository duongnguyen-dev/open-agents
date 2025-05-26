import os
import aiohttp
from typing import Optional
from langchain_core.tools import BaseTool
from langchain_core.tools.base import ArgsSchema
from pydantic import BaseModel, Field

class FetchCurrentWeatherDataFromCityNameInput(BaseModel):
    city_name: str = Field(description="The city name")
    lang: str = Field(description="The output language which use the same language as the input prompt")

class FetchCurrentWeatherDataFromCityNameTool(BaseTool):
    name: str = "fetch_current_weather_data_from_city_name"
    description: str = "Get current weather data given the city name."
    args_schema: Optional[ArgsSchema] = FetchCurrentWeatherDataFromCityNameInput
    return_direct: bool = True
    
    def _run(self):
        pass
    
    async def _arun(
        self, city_name: str, lang: str
    ):
        """Get current weather data given the city name asynchronously."""
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&lang={lang}&appid={os.environ.get('OPENWEATHERMAP_API_KEY')}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()