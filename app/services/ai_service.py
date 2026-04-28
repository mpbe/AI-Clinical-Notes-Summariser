from config import Config
from openai import OpenAI

client = OpenAI(api_key=Config.OPENAI_API_KEY)

def summarise_clinical_notes(notes):

    ai_prompt = f"""
    You are an expert in clinical medicine and UK clinical coding standards.

    Analyse the following clinical notes and return a clearly structured response.
    
    INPUT:
    {notes}
    
    OUTPUT FORMAT:
    
    --- SUMMARY ---
    Provide a concise clinical summary of the case.
    
    --- KEY CONDITIONS ---
    List the key diagnoses, co-morbidities, and relevant clinical findings.
    
    --- DIAGNOSES ---
    Provide a bullet-point list of diagnoses and co-morbidities.
    
    --- PROCEDURES ---
    Provide a bullet-point list of procedures performed (aligned with OPCS-4 standards where applicable).
    
    --- CODING ---
    Provide:
    - ICD-10 (UK) codes relevant to the diagnoses
    - OPCS-4 codes relevant to the procedures
    
    Ensure the output is clear, structured, and consistently formatted.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "you are a precise medical data assistant"},
            {"role": "user", "content": ai_prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content