import openai
from openai import OpenAI
import os
from dotenv import load_dotenv

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI() 

def get_ai_recommendation(height: float, weight: float, activity_level: str) -> str:
    prompt = f"""
You are a certified fitness and nutrition expert.
The user has the following profile:
- Height: {height} cm
- Weight: {weight} kg
- Activity Level: {activity_level}

Based on this, provide:
1. Estimated daily calorie requirement
2. Fitness routine recommendation
3. Full-day personalized meal plan (breakfast, lunch, dinner)
4. Health or lifestyle tips
Format the output with proper HTML tags like <ul>, <li>, <strong>, <br> to make it look good on a website with proper linebreaks.
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=600,
            temperature=0.7
        )
        content = response.choices[0].message.content
        # print(content)
        return content
    except Exception as e:
        print("Error occurred:", e)
        return None

