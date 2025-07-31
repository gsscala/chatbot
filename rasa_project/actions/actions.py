from typing import Any, Dict, List
import pandas as pd
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from ..database.FoodFinder import FoodFinder

food = FoodFinder()

class ActionConsultarNutrientes(Action):
    def name(self) -> str:
        return "action_consultar_nutrientes"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict) -> List[Dict[str, Any]]:
        if not food.state:
            dispatcher.utter_message(text="Desculpe, não estou conseguindo acessaro banco de dados nutricionais agora")
            return []
        food_name = tracker.get_slot("alimento")
        if not food_name:
            dispatcher.utter_message(text="Sobre qual alimento você quer saber?")
            return []
    
        try:
            resultados = food.findfood(food_name)
            if not resultados:
                dispatcher.utter_message(text=f"Não encontrei informações para {food_name}. Tem certeza de que digitou certo?")
                return []
            if len(resultados) > 1:
                dispatcher.utter_message(text=f"Encontrei resultados para os seguintes alimentos:")
                foods = ["\n- " + food for food in resultados.index.tolist()]
                dispatcher.utter_message(text="".join(foods))
                dispatcher.utter_message(text=f"Mas imagino que você queira saber sobre {resultados.index.tolist()[0]}:\n")
            resultado = resultados.iloc[0]
            for nutrient, value in resultado.items():
                dispatcher.utter_message(text=f"{nutrient}: {value}")
            
        except Exception as e:
            print(e)
        return []