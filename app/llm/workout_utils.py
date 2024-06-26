def workout_user_msg(session, typeOfWorkout) -> str:
    user_msg = f""" 
    I am {session['age']} years old 
    I am a {session['sex']} 
    I currently weighs {session['current_weight']} pounds, 
    I am {session['height']} cm tall, 
    {f"I have the following physical impediments: {session['physical_impediments']}" if session.get("physical_impediments") else ""}, 
    My Weight goal is {session['ideal_weight']} pounds,
    You will only suggest workouts of type {typeOfWorkout},
    My body goal is: {session['body_goal']}"""

    user_message = {"role": "user", "content": user_msg}

    return user_message


def workout_system_msg() -> str:
    system_msg = """
    You are an expert in exercise science designed to output workout plans in JSON.
    You will take in user input and output the exercises in the exact following format, with the exact same order of days of the week. Keep in mind the pysical impediments. No exercise should involve any injured body part:
    ---
      {
      "week": {
          "monday": [
              {
                  "muscleGroup": "<You choose>",
                  "exercises": [
                      {
                          "name": "<Name of exercise>",
                          "equipment": "<required equipment>",
                          "instructions": "<exercise instructions>"
                      },
                      {
                          "name": "<Name of exercise>",
                          "equipment": "<required equipment>",
                          "instructions": "<exercise instructions>"
                      }
                  ]
              }
          ],
          "tuesday": [
              {
                  "muscleGroup": "<You choose>",
                  "exercises": [
                      {
                          "name": "<Name of exercise>",
                          "equipment": "<required equipment>",
                          "instructions": "<exercise instructions>"
                      },
                      {
                          "name": "<Name of exercise>",
                          "equipment": "<required equipment>",
                          "instructions": "<exercise instructions>"
                      }
                  ]
              }
          ],
          "wednesday":...
          ...
          "saturday": "rest day",
          "sunday": "rest day"
      }
    }
    """
    system_message = {"role": "system", "content": system_msg}
    return system_message
