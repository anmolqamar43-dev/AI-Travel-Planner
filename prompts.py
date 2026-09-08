def format_traveler_data(data):
    """
    Convert traveler information into a clean text format.
    """

    return f"""
Traveler Name: {data["name"]}
Destination: {data["destination"]}
Number of Days: {data["days"]}
Budget: {data["budget"]}
Interests: {data["interests"]}
Travel Style: {data["travel_style"]}
"""


def zero_shot_prompt(data):
    """
    Zero-Shot Prompting:
    No examples are provided.
    """

    traveler = format_traveler_data(data)

    return f"""
You are an expert AI Travel Planner.

Create a personalized travel itinerary for the following traveler.

{traveler}

Your task is to:

1. Analyze the traveler's preferences.
2. Suggest suitable places to visit.
3. Create a day-by-day itinerary.
4. Recommend activities matching the traveler's interests.
5. Keep the recommendations suitable for the travel style.
6. Consider the available budget.
7. Provide estimated costs where reasonable.
8. Make the itinerary practical and easy to follow.

Use the following format:

TRAVEL SUMMARY
Name:
Destination:
Days:
Budget:
Interests:
Travel Style:

RECOMMENDED PLACES
- Place 1
- Place 2
- Place 3

DAY-BY-DAY ITINERARY

Day 1:
Activities:
Estimated Cost:

Day 2:
Activities:
Estimated Cost:

Continue for all travel days.

BUDGET SUMMARY
Estimated Total:
Remaining Budget:

IMPORTANT:
- Do not invent exact prices with false certainty.
- Clearly label costs as estimates.
- If the budget appears unrealistic, politely mention it.
- Keep the response useful and concise.
"""


def few_shot_prompt(data):
    """
    Few-Shot Prompting:
    Provides examples before asking Gemini to solve
    the new travel planning problem.
    """

    traveler = format_traveler_data(data)

    return f"""
You are an expert AI Travel Planner.

Below are examples showing how travel itineraries should be created.

========================
EXAMPLE 1
========================

Traveler:
Name: Sarah
Destination: Istanbul
Days: 3
Budget: $600
Interests: History, Food
Travel Style: Family

Sample Itinerary:

Day 1:
Visit Hagia Sophia and the Blue Mosque.
Enjoy traditional Turkish food in the evening.

Day 2:
Visit Topkapi Palace.
Explore the Grand Bazaar.
Try local Turkish dishes.

Day 3:
Take a Bosphorus cruise.
Visit a local market.
Enjoy a relaxed dinner.

The plan focuses on history and food while keeping
the activities suitable for a family trip.

========================
EXAMPLE 2
========================

Traveler:
Name: Daniel
Destination: Bangkok
Days: 4
Budget: $700
Interests: Food, Shopping, Culture
Travel Style: Friends

Sample Itinerary:

Day 1:
Explore local street-food markets.
Visit popular cultural areas.

Day 2:
Visit major temples and cultural attractions.

Day 3:
Spend time shopping at major markets and malls.

Day 4:
Enjoy local food and explore the city.

The plan focuses on food, shopping and culture
while matching the travel style.

========================
EXAMPLE 3
========================

Traveler:
Name: Emma
Destination: Bali
Days: 5
Budget: $900
Interests: Nature, Beaches, Adventure
Travel Style: Solo

Sample Itinerary:

Day 1:
Relax at the beach and explore the local area.

Day 2:
Visit a natural attraction and enjoy outdoor activities.

Day 3:
Explore waterfalls and surrounding nature.

Day 4:
Enjoy an adventure activity.

Day 5:
Relax and explore local markets.

The plan prioritizes nature, beaches and adventure.

========================
NEW TRAVELER
========================

Now create a personalized travel itinerary for:

{traveler}

Follow the general structure and style demonstrated
in the examples, but create completely new recommendations
appropriate for this traveler.

Your response must include:

TRAVEL SUMMARY

RECOMMENDED PLACES

DAY-BY-DAY ITINERARY

BUDGET SUMMARY

IMPORTANT:
- Personalize the recommendations.
- Consider the budget.
- Consider the number of days.
- Match the traveler's interests.
- Match the travel style.
- Costs should be presented as estimates.
"""


def structured_reasoning_prompt(data):
    """
    Structured Reasoning Prompting.

    We ask Gemini to follow a planning process but do NOT
    request hidden chain-of-thought.
    """

    traveler = format_traveler_data(data)

    return f"""
You are an expert AI Travel Planner.

Create a personalized travel itinerary for:

{traveler}

Use the following structured planning process:

Step 1:
Analyze the traveler's interests and travel style.

Step 2:
Consider the available budget and avoid recommending
activities that are clearly outside the budget.

Step 3:
Consider the total number of travel days.

Step 4:
Select attractions and activities that best match
the traveler's preferences.

Step 5:
Organize the selected activities into a practical
day-by-day itinerary.

Step 6:
For each major recommendation, provide a SHORT
explanation of why it was selected.

Do NOT reveal hidden reasoning or chain-of-thought.
Only provide concise explanations for your recommendations.

Use this final format:

================================
TRAVELER SUMMARY
================================

Name:
Destination:
Days:
Budget:
Interests:
Travel Style:

================================
RECOMMENDED PLACES
================================

1. Place:
Why it was selected:

2. Place:
Why it was selected:

3. Place:
Why it was selected:

================================
DAY-BY-DAY ITINERARY
================================

Day 1:

Morning:
Activity:

Afternoon:
Activity:

Evening:
Activity:

Estimated Cost:
Why these activities:

Day 2:

Morning:
Activity:

Afternoon:
Activity:

Evening:
Activity:

Estimated Cost:
Why these activities:

Continue for all travel days.

================================
BUDGET SUMMARY
================================

Estimated Accommodation:
Estimated Food:
Estimated Transportation:
Estimated Activities:
Estimated Other Expenses:

Estimated Total:
Estimated Remaining Budget:

================================
TRAVEL TIPS
================================

Provide 3-5 useful travel tips.

IMPORTANT:
- Prices are estimates and may change.
- Do not claim exact current prices unless verified.
- Make the itinerary practical.
- Keep the recommendations aligned with the traveler's preferences.
"""