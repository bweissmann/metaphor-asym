from metaphor_python import Metaphor
from dotenv import load_dotenv
import os

load_dotenv()

def metaphor():
    return Metaphor(os.getenv("METAPHOR_API_KEY"))
