## manage csv loading first
import os
import pandas as pd

class DataLoader:
    def __init__(self, data_dir):
        self.data_dir = data_dir
    
    def load_csv(self, symbol, file_format = "csv"):
        file_path = os.path.join(self.data_dir, f"{symbol}.{file_format}")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found for {symbol} @ {file_path}")
        df = pd.read_csv(file_path, parse_dates = ["datetime"], index_col = "datetime")
        df.sort_index(inplace = True)
        return df
    
    def list_symbols(self):
        files = os.listdir(self.data_dir)
        symbols = [f.split(".") for f in files if f.endswith(".csv")]
        return symbols
    