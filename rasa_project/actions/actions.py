from typing import Any, Dict, List
import pandas as pd
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from database.FoodFinder import FoodFinder

food = FoodFinder()

class ActionConsultarNutrientes(Action):
    def name(self) -> str:
        return "action_consultar_nutrientes"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict) -> List[Dict[str, Any]]:
        if not food.state:
            dispatcher.utter_message(text="Desculpe, não estou conseguindo acessar o banco de dados nutricionais agora.")
            print("[DEBUG] FoodFinder state is False")
            return []

        food_name = tracker.get_slot("alimento")
        
        if not food_name:
            dispatcher.utter_message(text="Sobre qual alimento você quer saber?")
            print("[DEBUG] Slot 'alimento' is not set.")
            return []

        try:
            resultados = food.findfood(food_name)
            if resultados is None or resultados.empty:
                dispatcher.utter_message(text=f"Não encontrei informações para {food_name}. Tem certeza de que digitou certo?")
                print(f"[DEBUG] No results found for: {food_name}")
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
            dispatcher.utter_message(text=f"Ocorreu um erro ao buscar informações: {e}")
            print(f"[ERROR] Exception in action_consultar_nutrientes: {e}")
        return []