from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import re

# Load environment variables
load_dotenv()

app = FastAPI(title="Diet Recipe App")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class RecipeRequest(BaseModel):
    diet_type: str  # "vegetarian", "vegan", or "no_restrictions"

class RecipeResponse(BaseModel):
    name: str
    description: str
    ingredients: list[str]
    instructions: list[str]
    prep_time: str
    servings: str

@app.get("/")
async def home():
    """Root endpoint"""
    return {
        "message": "Diet Recipe API", 
        "status": "healthy",
        "frontend": "http://localhost:3000"
    }

@app.post("/recipe", response_model=RecipeResponse)
async def generate_recipe(request: RecipeRequest):
    """Generate a recipe based on diet type using GPT-4"""
    
    diet_type_lower = request.diet_type.lower()
    if diet_type_lower not in ["vegetarian", "vegan", "no_restrictions"]:
        raise HTTPException(
            status_code=400, 
            detail="Diet type must be 'vegetarian', 'vegan', or 'no_restrictions'"
        )
    
    try:
        # Create diet-specific description
        diet_description = {
            "vegetarian": "vegetarian (no meat, but includes dairy and eggs)",
            "vegan": "vegan (plant-based only, no animal products)",
            "no_restrictions": "with no dietary restrictions (all ingredients welcome)"
        }[diet_type_lower]
        
        # Create prompt for OpenAI
        prompt = f"""Please provide a simple and delicious {diet_description} dinner recipe.

Return the recipe in the following JSON format:
{{
    "name": "Recipe Name",
    "description": "Brief description of the dish",
    "prep_time": "30 minutes",
    "servings": "4 servings",
    "ingredients": ["ingredient 1", "ingredient 2", ...],
    "instructions": ["step 1", "step 2", ...]
}}

Make it simple and easy to follow for a weeknight dinner. Be specific with measurements."""
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful cooking assistant who provides clear, simple, and delicious recipes. Always respond with valid JSON."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=800,
            temperature=0.7
        )
        
        recipe_text = response.choices[0].message.content
        
        # Try to extract JSON from the response
        try:
            # Remove markdown code blocks if present
            recipe_text = re.sub(r'^```json\s*', '', recipe_text.strip())
            recipe_text = re.sub(r'\s*```$', '', recipe_text.strip())
            
            recipe_data = json.loads(recipe_text)
            
            # Ensure all required fields are present
            return RecipeResponse(
                name=recipe_data.get("name", "Delicious Recipe"),
                description=recipe_data.get("description", "A wonderful meal"),
                ingredients=recipe_data.get("ingredients", []),
                instructions=recipe_data.get("instructions", []),
                prep_time=recipe_data.get("prep_time", "30 minutes"),
                servings=recipe_data.get("servings", "4 servings")
            )
        except json.JSONDecodeError:
            # Fallback if JSON parsing fails
            raise HTTPException(
                status_code=500, 
                detail="Failed to parse recipe from AI response"
            )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recipe: {str(e)}")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

