from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Thanksgiving Recipe API")

# Thanksgiving recipe data
recipe = {
    "name": "Classic Roast Turkey with Herb Butter",
    "servings": "8-10 people",
    "prep_time": "30 minutes",
    "cook_time": "3-4 hours",
    "ingredients": [
        "1 whole turkey (12-14 lbs)",
        "1/2 cup butter, softened",
        "2 tablespoons fresh rosemary, chopped",
        "2 tablespoons fresh thyme, chopped",
        "2 tablespoons fresh sage, chopped",
        "4 cloves garlic, minced",
        "2 onions, quartered",
        "2 carrots, chopped",
        "2 celery stalks, chopped",
        "4 cups chicken or turkey broth",
        "Salt and black pepper to taste",
        "1 lemon, halved",
    ],
    "instructions": [
        "Preheat oven to 325°F (165°C).",
        "Remove turkey from refrigerator 1 hour before cooking to bring to room temperature.",
        "Pat turkey dry with paper towels inside and out.",
        "Mix softened butter with rosemary, thyme, sage, and minced garlic.",
        "Carefully loosen the skin from the breast meat and spread half the herb butter under the skin.",
        "Rub the remaining herb butter all over the outside of the turkey.",
        "Season generously with salt and pepper inside and out.",
        "Stuff the cavity with quartered onions, lemon halves, and a handful of fresh herbs.",
        "Place chopped carrots, celery, and remaining onions in the bottom of a roasting pan.",
        "Place turkey on top of vegetables, breast side up.",
        "Pour broth into the bottom of the pan (not over the turkey).",
        "Tent turkey loosely with aluminum foil.",
        "Roast for about 3-4 hours (approximately 15 minutes per pound).",
        "Remove foil during the last 45 minutes to brown the skin.",
        "Turkey is done when internal temperature reaches 165°F in the thickest part of the thigh.",
        "Let turkey rest for 20-30 minutes before carving.",
        "Use pan drippings to make gravy if desired.",
    ],
    "tips": [
        "Don't skip the resting time - it helps the juices redistribute!",
        "Baste every 30-45 minutes for extra moist meat.",
        "Use a meat thermometer for best results.",
        "Save the carcass to make delicious turkey stock!",
    ],
}


@app.get("/", response_class=HTMLResponse)
async def home():
    """Home page with beautiful recipe display"""
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Thanksgiving Recipe</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            body {{
                font-family: 'Georgia', serif;
                background: linear-gradient(135deg, #f5e6d3 0%, #d4a574 100%);
                min-height: 100vh;
                padding: 20px;
                line-height: 1.6;
            }}
            .container {{
                max-width: 800px;
                margin: 0 auto;
                background: white;
                border-radius: 20px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.1);
                padding: 40px;
            }}
            h1 {{
                color: #8b4513;
                font-size: 2.5em;
                margin-bottom: 10px;
                text-align: center;
            }}
            .emoji {{
                font-size: 3em;
                text-align: center;
                margin: 20px 0;
            }}
            .meta {{
                display: flex;
                justify-content: space-around;
                margin: 30px 0;
                padding: 20px;
                background: #fff8f0;
                border-radius: 10px;
            }}
            .meta-item {{
                text-align: center;
            }}
            .meta-label {{
                font-weight: bold;
                color: #8b4513;
                font-size: 0.9em;
            }}
            .meta-value {{
                color: #555;
                margin-top: 5px;
            }}
            h2 {{
                color: #8b4513;
                margin: 30px 0 15px 0;
                font-size: 1.8em;
                border-bottom: 3px solid #d4a574;
                padding-bottom: 10px;
            }}
            ul {{
                list-style-position: inside;
                margin-left: 20px;
            }}
            li {{
                margin: 10px 0;
                color: #333;
            }}
            ol {{
                margin-left: 20px;
            }}
            ol li {{
                margin: 15px 0;
                padding-left: 10px;
            }}
            .tips {{
                background: #fff8f0;
                padding: 20px;
                border-radius: 10px;
                border-left: 4px solid #d4a574;
                margin-top: 20px;
            }}
            .api-link {{
                text-align: center;
                margin-top: 30px;
                padding: 20px;
                background: #f0f0f0;
                border-radius: 10px;
            }}
            .api-link a {{
                color: #8b4513;
                text-decoration: none;
                font-weight: bold;
                padding: 10px 20px;
                background: white;
                border-radius: 5px;
                display: inline-block;
                margin: 5px;
                transition: transform 0.2s;
            }}
            .api-link a:hover {{
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="emoji">🦃</div>
            <h1>{recipe['name']}</h1>
            
            <div class="meta">
                <div class="meta-item">
                    <div class="meta-label">SERVINGS</div>
                    <div class="meta-value">{recipe['servings']}</div>
                </div>
                <div class="meta-item">
                    <div class="meta-label">PREP TIME</div>
                    <div class="meta-value">{recipe['prep_time']}</div>
                </div>
                <div class="meta-item">
                    <div class="meta-label">COOK TIME</div>
                    <div class="meta-value">{recipe['cook_time']}</div>
                </div>
            </div>

            <h2>Ingredients</h2>
            <ul>
                {''.join([f'<li>{ingredient}</li>' for ingredient in recipe['ingredients']])}
            </ul>

            <h2>Instructions</h2>
            <ol>
                {''.join([f'<li>{instruction}</li>' for instruction in recipe['instructions']])}
            </ol>

            <div class="tips">
                <h2 style="margin-top: 0;">Pro Tips</h2>
                <ul style="margin-left: 0;">
                    {''.join([f'<li>{tip}</li>' for tip in recipe['tips']])}
                </ul>
            </div>

            <div class="api-link">
                <p>API Endpoints:</p>
                <a href="/recipe">Get Recipe JSON</a>
                <a href="/docs">View API Docs</a>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content


@app.get("/recipe")
async def get_recipe():
    """Get the recipe as JSON"""
    return recipe


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "Happy Thanksgiving!"}

