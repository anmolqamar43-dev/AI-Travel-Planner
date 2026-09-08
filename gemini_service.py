import os
import time

from dotenv import load_dotenv
from google import genai

from prompts import (
    zero_shot_prompt,
    few_shot_prompt,
    structured_reasoning_prompt,
)

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY is missing from .env file")

client = genai.Client(api_key=GEMINI_API_KEY)

MODEL_NAME = "gemini-3.5-flash"


def generate_travel_plan(data, technique):

    # Select prompt
    if technique == "zero-shot":
        prompt = zero_shot_prompt(data)

    elif technique == "few-shot":
        prompt = few_shot_prompt(data)

    elif technique == "structured":
        prompt = structured_reasoning_prompt(data)

    else:
        raise ValueError("Invalid prompting technique")

    # Retry settings
    max_retries = 3
    delays = [2, 5, 10]

    for attempt in range(max_retries + 1):

        try:
            print(f"Calling Gemini... attempt {attempt + 1}")

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            print("Gemini response received successfully.")

            return response.text

        except Exception as e:

            error_message = str(e)

            print("\n========== GEMINI ERROR ==========")
            print(error_message)
            print("==================================\n")

            # Retry temporary/server errors
            if (
                "503" in error_message
                or "UNAVAILABLE" in error_message
                or "500" in error_message
                or "502" in error_message
                or "504" in error_message
            ):

                if attempt < max_retries:

                    print(
                        f"Gemini temporarily unavailable. "
                        f"Retrying in {delays[attempt]} seconds..."
                    )

                    time.sleep(delays[attempt])
                    continue

            raise RuntimeError(
                f"Gemini API error: {error_message}"
            )