# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# class ActionTellSum(Action):
#
#     def name(self) -> Text:
#         return "action_tell_sum"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         number1 = tracker.get_slot("addend_1")
#         number2 = tracker.get_slot("addend_2")
#         dispatcher.utter_message(text=f"The sum of {number1} and {number2} is {float(number1) + float(number2)}")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCheckLoanOptions(Action):
    def name(self) -> Text:
        return "action_check_loan_options"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        year_slot = tracker.get_slot("year")
        if not year_slot:
            dispatcher.utter_message(text="Please provide your car's year (e.g., 2005, 2015).")
            return []

        try:
            year_int = int(str(year_slot).strip())
        except ValueError:
            dispatcher.utter_message(text="Year should be a number (e.g., 2005, 2015).")
            return []

        # Eligible companies
        if year_int < 2005:
            eligible_companies = ["MoGo", "Flex Capital"]
            dispatcher.utter_message(
                text="Your car can only be financed through MoGo and Flex Capital."
            )
        else:
            eligible_companies = ["Silk Bank", "Central", "Flex Capital", "MoGo", "Dizi"]
            dispatcher.utter_message(
                text="Your car can be financed by any partner company. The best terms are with Silk Bank."
            )

        return []


class ActionCheckAge(Action):
    def name(self) -> Text:
        return "action_check_age"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        age = tracker.get_slot("age")

        if not age:
            dispatcher.utter_message(text="how old are you?")
            return []

        try:
            age_int = int(str(age).strip())
        except ValueError:
            dispatcher.utter_message(text="Age must be in numbers, please enter again.")
            return []

        if age_int >= 22:
            dispatcher.utter_message(text="✅ All companies will review your application.")
        elif age_int == 21:
            dispatcher.utter_message(text="⚠️ All companies are considering it, except Dizi.")
        elif age_int >= 18:
            dispatcher.utter_message(text="⚠️ Only Flex Capital will review your application.")
        else:
            dispatcher.utter_message(text="⚠️ Your application will not be considered because you are not of legal age.")

        return []



