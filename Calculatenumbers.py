import pyttsx3
import speech_recognition as sr
import re

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",185)

def Speak(audio):
    engine.say(audio)
    engine.runAndWait()

def simple_math(expression):
    """Simple math evaluator as backup"""
    try:
        # Clean and prepare expression
        expression = expression.replace("x", "*")
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")
        
        # Basic validation - only allow numbers, operators, and spaces
        if re.match(r'^[0-9+\-*/.() ]+$', expression):
            result = eval(expression)
            return str(result)
        else:
            return None
    except:
        return None

def WolfRamAlpha(query):
    """Try WolframAlpha first, fallback to simple math"""
    try:
        import wolframalpha
        apikey = "KL5J6YK6VY"  # WolframAlpha API key
        requester = wolframalpha.Client(apikey)
        requested = requester.query(query)
        answer = next(requested.results).text
        print(f"📊 WolframAlpha result: {answer}")
        return answer
    except ImportError:
        print("⚠️ WolframAlpha not available, using simple calculator")
        return simple_math(query)
    except StopIteration:
        print("❌ No WolframAlpha result, trying simple math")
        return simple_math(query)
    except Exception as e:
        print(f"❌ WolframAlpha error: {e}, trying simple math")
        return simple_math(query)

def Calc(query):
    Term = str(query).strip()
    print(f"🧮 Calculating: {Term}")
    
    if not Term:
        Speak("Please tell me what you want to calculate.")
        return
    
    # Clean up the query
    Term = Term.replace("jarvis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("times","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("add","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("subtract","-")
    Term = Term.replace("divide","/")
    Term = Term.replace("divided by","/")
    
    Final = str(Term).strip()
    
    if not Final:
        Speak("Please provide a calculation to solve.")
        return
        
    # Try calculation
    result = WolfRamAlpha(Final)
    
    if result:
        print(f"✅ Answer: {result}")
        Speak(f"The answer is {result}")
    else:
        # Try very basic math as last resort
        try:
            if any(op in Final for op in ['+', '-', '*', '/']):
                basic_result = eval(Final)
                print(f"✅ Basic calculation: {basic_result}")
                Speak(f"The answer is {basic_result}")
            else:
                Speak("I couldn't solve that calculation. Please try a simpler expression like 2 plus 3.")
        except:
            Speak("Sorry, I couldn't calculate that. Please try again with a simpler expression.")