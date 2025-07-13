print("🔍 Starting ELI5 test...")
print("📁 File is running!")

try:
    import os
    print("✅ os imported")
    
    from groq import Groq
    print("✅ Groq imported")
    
    from dotenv import load_dotenv
    print("✅ dotenv imported")
    
    # Load your API key from .env file
    load_dotenv()
    print("✅ .env file loaded")
    
    # Check if API key exists
    api_key = os.getenv("GROQ_API_KEY")
    if api_key:
        print(f"✅ API key found! Length: {len(api_key)} characters")
    else:
        print("❌ No API key found!")
        exit()
    
    print("🤖 Creating Groq client...")
    client = Groq(api_key=api_key)
    print("✅ Groq client created successfully")
    
    # Try different models (current ones that should work)
    models_to_try = [
        "llama-3.1-8b-instant",
        "llama-3.1-70b-versatile", 
        "gemma2-9b-it",
        "llama3-8b-8192"
    ]
    
    for model in models_to_try:
        try:
            print(f"🚀 Trying model: {model}")
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": "Explain what a dog is like I'm 5 years old"}
                ],
                max_tokens=100
            )
            
            print(f"✅ SUCCESS with model: {model}")
            print("📝 Response received:")
            print("-" * 50)
            print(response.choices[0].message.content)
            print("-" * 50)
            break  # Stop trying other models if this one works
            
        except Exception as model_error:
            print(f"❌ {model} failed: {model_error}")
            continue
    
except Exception as e:
    print(f"❌ Error occurred: {e}")
    print(f"❌ Error type: {type(e)}")

print("🏁 Test completed!")