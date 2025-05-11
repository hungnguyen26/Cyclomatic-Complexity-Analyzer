import google.generativeai as genai
import ast
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key is not set in the environment variables.")

genai.configure(api_key=api_key)

def get_refactor_suggestion(func_node, full_code):
    try:
        func_code = ast.get_source_segment(full_code, func_node)

        prompt = f"""Đây là một hàm Python, hãy phân tích và gợi ý cách refactor chi tiết nếu cần:
```python
{func_code}
```"""

        response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Lỗi Gemini: {e}"

