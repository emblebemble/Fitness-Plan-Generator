def generate_prompt(goal, diet_goal, diet_type, include_cardio, gym_days, cardio_days, fitness_level, location):
    """
    Generates a structured and detailed training and dietary plan with HTML table formatting for frontend display.
    Includes calories for each meal and uses expert-recommended gym exercises tailored to the user's goal.

    Parameters:
    - goal: The user's training goal (e.g., 'weight loss', 'muscle gain', 'endurance', 'strength').
    - diet_goal: The user's dietary goal (e.g., 'fat loss', 'muscle gain').
    - diet_type: The type of diet the user follows (e.g., 'vegan', 'keto').
    - include_cardio: Whether to include cardio in the plan (True or False).
    - gym_days: The number of days the user goes to the gym per week.
    - cardio_days: The number of days the user does cardio per week.
    - fitness_level: The training will substantially depend on this parameter. The amount of excercises and sets within for gym. For Cardio the intensity and time will be lower.
    - location: This will impact ingredients selection for diet so to reflect local recomendations for best ingredietns and if required prices.
    


    Returns:
    - A formatted string that serves as the prompt to be sent to OpenAI.
    """
    prompt = f"""
    I need a structured and detailed training and dietary plan, based on professional workout routines, particularly from sites like Muscle and Strenghth.
    - My training goal is: {goal}.
    - My diet goal is: {diet_goal}.
    - I prefer a {diet_type} diet.
    - Include cardio plan: {include_cardio}.
    - I can go to the gym: {gym_days} days a week.
    - I can do cardio: {cardio_days} days a week.
    - My fitness level is: {fitness_level}.
    - My preferred training location is: {location}.

    **Please provide the output in the following format (use HTML tables for workout, cardio, and meal plans):**

    1. **Summary:** A short paragraph summarizing the plan.
    2. **Workout Plan:**  
        - Ensure the plan is based on real top rated plans for example from sites like Muscle and Strength etc.  
        - Ensure excercises and number of sets are tailored for the user's skill. 
        - Adjust sets, reps, and rest periods according to the goal:
          - For **muscle gain**: Use optimal repetition and sets quantities are provided to ensure maximum muscle gains for the user skill level. Also ensure the rest time between sets is optimal for the goal.
          - For **strength**: Use optimal repetition and sets quantities are provided to ensure maximum strenghth gains considering the user skill level. Also ensure the rest time between sets is optimal for the goal.
          - For **endurance**: Use optimal repetition and sets quantities are provided to ensure maximum endurance gains considering the user skill level. Also ensure the rest time between sets is optimal for the goal.
        - Example format: (Monday: Gym, Tuesday: Cardio, Wednesday: Rest, etc.)
        - Avoid trainings on Weekend especially on Sunday. 
        - Ensure if sum of selected Cardio days and Gym days training days is higher than number of week days that the trainings have both elements on same day.
        - Ensure Cardio has 2 options for the same day for example: Cycling 1 hour or running 20 minutes. and the quantities should depend on skill level,
        - Ensure diet plan is for 5 days both working and non working is clarly indicated and number of calories higher the higher is intesity of given day training.

     Example:
    <table border="1">
        <tr><th>Day</th><th>Exercise</th><th>Sets</th><th>Repetitions</th><th>Rest</th></tr>
        <tr><td>Monday</td><td>Squat</td><td>4</td><td>6-8</td><td>2 min</td></tr>
        <tr><td>Tuesday</td><td>Cycling 60 min</td><td>or</td><td>Running 20 minutes</td><td>-</td></tr>
    </table>
    
    3. **Meal Plan:**
        - Provide a unique meal plan for each day of the week, adjusting for gym and cardio days.
        - Include meal, food items, portion sizes, and estimated calories for each meal. 
        - add total caloriess per day at the end of each day.

    Example:
    <table border="1">
        <tr><th>Day</th><th>Meal</th><th>Foods</th><th>Portion Sizes</th><th>Calories</th></tr>
        <tr><td>Monday</td><td>Breakfast</td><td>Oats, Peanut Butter</td><td>1 cup, 2 tbsp</td><td>350</td></tr>
        <tr><td>Tuesday</td><td>Lunch</td><td>Grilled Chicken, Salad</td><td>150g, 2 cups</td><td>400</td></tr>
    </table>

    4. **Ingredient Properties and Nutritional Content:** Include a table that lists the ingredients, their medicinal or anti-inflammatory properties, and their macronutrient content (protein, carbs, fat).

    Example:
    <table border="1">
        <tr><th>Ingredient</th><th>Properties</th><th>Protein (g)</th><th>Carbs (g)</th><th>Fat (g)</th><th>Calories</th></tr>
        <tr><td>Chicken Breast</td><td>High in protein, Anti-inflammatory</td><td>25</td><td>0</td><td>3</td><td>165</td></tr>
        <tr><td>Spinach</td><td>Rich in iron, Anti-inflammatory</td><td>2</td><td>3</td><td>0</td><td>23</td></tr>
    </table>

    
    """
    return prompt
