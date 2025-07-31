import pandas as pd

class FoodFinder:
    def __init__(self, filepath='../database/alimentos.csv'):
        cols = [
            'Descrição dos alimentos',
            'Energia (kcal)',
            'Proteína (g)',
            'Lipídeos (g)',
            'Carboidrato (g)',
            'Fibra Alimentar (g)'
        ]
        
        self.state = True
        
        try:
            self.df = pd.read_csv(filepath, sep=';', usecols=cols, index_col='Descrição dos alimentos')
            
        except Exception as e:
            self.state = False
            print(e)

    def findfood(self, food_name:str):
        if not self.state:
            print("Dataframe não inicializado")
            return
        
        try:
            bool_series = self.df.index.str.lower() == food_name.lower()
            return self.df.loc[bool_series]
        
        except Exception as e:
            print(e)