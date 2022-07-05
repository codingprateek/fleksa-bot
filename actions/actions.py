# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from datetime import datetime
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.sides import show_sides

class ActionTriggerOrder(Action):

    def name(self) -> Text:
        return "action_trigger_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sides = show_sides()
        dispatcher.utter_message(response="utter_sides", sides=sides)

        return []

class ActionPlaceOrder(Action):

    def name(self) -> Text:
        return "action_place_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        order_name = tracker.latest_message['text']
        dispatcher.utter_message(response = "utter_order_placed", order_name = order_name)

        return []

class ActionCancelOrder(Action):

    def name(self) -> Text:
        return "action_cancel_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        id = tracker.latest_message['text']
        dispatcher.utter_message(response = "utter_id", id=id)

        return []

class ActionServings(Action):
    def name(self) -> Text:
        return "action_servings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                selected_serving = tracker.latest_message['text']
                dispatcher.utter_message(response = "utter_serving", selected_serving = selected_serving)

                return []

class ActionDateTime(Action):
    def name(self) -> Text:
        return "action_booking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                datetime = tracker.latest_message['text']
                dispatcher.utter_message(response = "utter_final_booking", datetime = datetime)

                return []
