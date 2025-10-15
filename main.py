from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from openai import OpenAI
from typing import List

app = FastAPI(title="Thanksgiving Recipe API")


# Pydantic models for chat
class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]
    api_key: str

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
                <p>Explore More:</p>
                <a href="/chat">💬 Chat with AI</a>
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


@app.get("/chat", response_class=HTMLResponse)
async def chat_page():
    """Chat interface page"""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chat with GPT-4o</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
            }
            .container {
                max-width: 900px;
                margin: 0 auto;
                background: white;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                overflow: hidden;
                display: flex;
                flex-direction: column;
                height: calc(100vh - 40px);
            }
            .header {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 20px 30px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .header h1 {
                font-size: 1.8em;
                font-weight: 600;
            }
            .back-link {
                color: white;
                text-decoration: none;
                padding: 8px 16px;
                background: rgba(255,255,255,0.2);
                border-radius: 8px;
                transition: background 0.3s;
            }
            .back-link:hover {
                background: rgba(255,255,255,0.3);
            }
            .api-key-section {
                padding: 20px 30px;
                background: #f8f9fa;
                border-bottom: 1px solid #e9ecef;
            }
            .api-key-section.hidden {
                display: none;
            }
            .input-group {
                display: flex;
                gap: 10px;
                align-items: center;
            }
            .input-group input {
                flex: 1;
                padding: 12px 16px;
                border: 2px solid #dee2e6;
                border-radius: 10px;
                font-size: 1em;
                transition: border-color 0.3s;
            }
            .input-group input:focus {
                outline: none;
                border-color: #667eea;
            }
            .btn {
                padding: 12px 24px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 1em;
                font-weight: 600;
                cursor: pointer;
                transition: transform 0.2s, box-shadow 0.2s;
            }
            .btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
            }
            .btn:active {
                transform: translateY(0);
            }
            .btn:disabled {
                opacity: 0.5;
                cursor: not-allowed;
                transform: none;
            }
            .chat-container {
                flex: 1;
                overflow-y: auto;
                padding: 30px;
                background: #ffffff;
            }
            .message {
                margin-bottom: 20px;
                display: flex;
                animation: fadeIn 0.3s;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
            .message.user {
                justify-content: flex-end;
            }
            .message-content {
                max-width: 70%;
                padding: 12px 18px;
                border-radius: 18px;
                line-height: 1.5;
            }
            .message.user .message-content {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border-bottom-right-radius: 4px;
            }
            .message.assistant .message-content {
                background: #f1f3f5;
                color: #212529;
                border-bottom-left-radius: 4px;
            }
            .message.system .message-content {
                background: #fff3cd;
                color: #856404;
                max-width: 100%;
                text-align: center;
                border-radius: 10px;
            }
            .input-section {
                padding: 20px 30px;
                background: #f8f9fa;
                border-top: 1px solid #e9ecef;
            }
            .message-input-group {
                display: flex;
                gap: 10px;
            }
            .message-input-group textarea {
                flex: 1;
                padding: 12px 16px;
                border: 2px solid #dee2e6;
                border-radius: 10px;
                font-size: 1em;
                font-family: inherit;
                resize: none;
                min-height: 50px;
                max-height: 150px;
                transition: border-color 0.3s;
            }
            .message-input-group textarea:focus {
                outline: none;
                border-color: #667eea;
            }
            .send-btn {
                align-self: flex-end;
                min-width: 100px;
            }
            .typing-indicator {
                display: none;
                padding: 12px 18px;
                background: #f1f3f5;
                border-radius: 18px;
                border-bottom-left-radius: 4px;
                width: fit-content;
            }
            .typing-indicator.active {
                display: block;
            }
            .typing-indicator span {
                display: inline-block;
                width: 8px;
                height: 8px;
                border-radius: 50%;
                background: #adb5bd;
                margin: 0 2px;
                animation: bounce 1.4s infinite;
            }
            .typing-indicator span:nth-child(2) {
                animation-delay: 0.2s;
            }
            .typing-indicator span:nth-child(3) {
                animation-delay: 0.4s;
            }
            @keyframes bounce {
                0%, 60%, 100% { transform: translateY(0); }
                30% { transform: translateY(-10px); }
            }
            .error {
                color: #dc3545;
                padding: 10px;
                background: #f8d7da;
                border-radius: 8px;
                margin-top: 10px;
            }
            .api-key-status {
                display: none;
                padding: 10px;
                background: #d1e7dd;
                color: #0f5132;
                border-radius: 8px;
                margin-top: 10px;
            }
            .api-key-status.show {
                display: block;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>💬 Chat with GPT-4o</h1>
                <a href="/" class="back-link">← Back to Recipe</a>
            </div>
            
            <div class="api-key-section" id="apiKeySection">
                <div class="input-group">
                    <input 
                        type="password" 
                        id="apiKeyInput" 
                        placeholder="Enter your OpenAI API Key (sk-...)"
                        autocomplete="off"
                    >
                    <button class="btn" onclick="setApiKey()">Start Chatting</button>
                </div>
                <div id="apiKeyStatus" class="api-key-status"></div>
            </div>

            <div class="chat-container" id="chatContainer">
                <div class="message system">
                    <div class="message-content">
                        👋 Welcome! Enter your OpenAI API key above to start chatting with GPT-4o.
                        <br><small>Your API key is never stored on our servers.</small>
                    </div>
                </div>
            </div>

            <div class="typing-indicator" id="typingIndicator">
                <span></span>
                <span></span>
                <span></span>
            </div>

            <div class="input-section">
                <div class="message-input-group">
                    <textarea 
                        id="messageInput" 
                        placeholder="Type your message here..."
                        disabled
                        onkeypress="handleKeyPress(event)"
                    ></textarea>
                    <button class="btn send-btn" onclick="sendMessage()" id="sendBtn" disabled>Send</button>
                </div>
                <div id="errorMessage" class="error" style="display: none;"></div>
            </div>
        </div>

        <script>
            let apiKey = '';
            let messages = [];

            function setApiKey() {
                const input = document.getElementById('apiKeyInput');
                const key = input.value.trim();
                
                if (!key) {
                    showError('Please enter an API key');
                    return;
                }
                
                if (!key.startsWith('sk-')) {
                    showError('Invalid API key format. Should start with sk-');
                    return;
                }
                
                apiKey = key;
                document.getElementById('apiKeySection').classList.add('hidden');
                document.getElementById('messageInput').disabled = false;
                document.getElementById('sendBtn').disabled = false;
                document.getElementById('messageInput').focus();
                
                // Clear welcome message
                document.getElementById('chatContainer').innerHTML = '';
                
                showApiKeyStatus('API key set! You can now start chatting.');
            }

            function showApiKeyStatus(message) {
                const status = document.getElementById('apiKeyStatus');
                status.textContent = message;
                status.classList.add('show');
                setTimeout(() => status.classList.remove('show'), 3000);
            }

            function handleKeyPress(event) {
                if (event.key === 'Enter' && !event.shiftKey) {
                    event.preventDefault();
                    sendMessage();
                }
            }

            async function sendMessage() {
                const input = document.getElementById('messageInput');
                const message = input.value.trim();
                
                if (!message) return;
                
                // Add user message to UI
                addMessage('user', message);
                messages.push({ role: 'user', content: message });
                
                // Clear input
                input.value = '';
                input.style.height = 'auto';
                
                // Show typing indicator
                const indicator = document.getElementById('typingIndicator');
                indicator.classList.add('active');
                
                // Disable send button
                const sendBtn = document.getElementById('sendBtn');
                sendBtn.disabled = true;
                
                try {
                    const response = await fetch('/api/chat', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            messages: messages,
                            api_key: apiKey
                        })
                    });
                    
                    const data = await response.json();
                    
                    if (!response.ok) {
                        throw new Error(data.detail || 'Failed to get response');
                    }
                    
                    // Add assistant message
                    addMessage('assistant', data.message);
                    messages.push({ role: 'assistant', content: data.message });
                    
                    hideError();
                    
                } catch (error) {
                    showError(error.message);
                } finally {
                    indicator.classList.remove('active');
                    sendBtn.disabled = false;
                    input.focus();
                }
            }

            function addMessage(role, content) {
                const container = document.getElementById('chatContainer');
                const messageDiv = document.createElement('div');
                messageDiv.className = `message ${role}`;
                
                const contentDiv = document.createElement('div');
                contentDiv.className = 'message-content';
                contentDiv.textContent = content;
                
                messageDiv.appendChild(contentDiv);
                container.appendChild(messageDiv);
                
                // Scroll to bottom
                container.scrollTop = container.scrollHeight;
            }

            function showError(message) {
                const errorDiv = document.getElementById('errorMessage');
                errorDiv.textContent = message;
                errorDiv.style.display = 'block';
            }

            function hideError() {
                document.getElementById('errorMessage').style.display = 'none';
            }

            // Auto-resize textarea
            document.getElementById('messageInput').addEventListener('input', function() {
                this.style.height = 'auto';
                this.style.height = Math.min(this.scrollHeight, 150) + 'px';
            });
        </script>
    </body>
    </html>
    """
    return html_content


@app.post("/api/chat")
async def chat(request: ChatRequest):
    """Chat endpoint that communicates with OpenAI GPT-4o"""
    try:
        # Initialize OpenAI client with user's API key
        client = OpenAI(api_key=request.api_key)
        
        # Create chat completion
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": msg.role, "content": msg.content} for msg in request.messages],
            temperature=0.7,
            max_tokens=1000
        )
        
        # Extract the assistant's message
        assistant_message = response.choices[0].message.content
        
        return {
            "message": assistant_message,
            "model": "gpt-4o"
        }
        
    except Exception as e:
        error_message = str(e)
        if "invalid_api_key" in error_message or "Incorrect API key" in error_message:
            raise HTTPException(status_code=401, detail="Invalid API key. Please check your OpenAI API key.")
        elif "insufficient_quota" in error_message:
            raise HTTPException(status_code=429, detail="API quota exceeded. Please check your OpenAI account.")
        else:
            raise HTTPException(status_code=500, detail=f"Error: {error_message}")

