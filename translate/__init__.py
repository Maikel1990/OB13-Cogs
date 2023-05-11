import json
from pathlib import Path
from .translate import Translate

async def setup(bot):
    with open(Path(__file__).parent / "info.json") as fp:
        __red_end_user_data_statement__ = json.load(fp)["end_user_data_statement"]
    
    await bot.add_cog(Translate(bot))
