# Open pipeline.py and add this import to the top:
from dalio_sovereign_strength_index.engines.engine_reserves import ReserveCurrencyEngine

# Append it inside your __init__ setup list like this:
class MacroDataPipeline:
    def __init__(self):
        self.engines = [
            WorldBankDataEngine(),
            FredDataEngine(),
            ReserveCurrencyEngine() # Built-in modular scaling!
        ]
# ... [rest of pipeline.py code stays exactly the same]
