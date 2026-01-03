# -------------------------------
# Primitive Functions
# -------------------------------

def extractData(userProfile, keys):
    return {key: userProfile.get(key) for key in keys}


def lookupValue(table, key, field):
    return table.get(key, {}).get(field, 1)


def applyFormula(formula, variables):
    return eval(formula, {}, variables)


# -------------------------------
# Complex Function: Premium Calculator
# -------------------------------

def premium_calculator(userProfile, ratesTable, riskTable):

    data = extractData(userProfile, ['age', 'location', 'coverage'])
    age = data['age']
    location = data['location']
    coverage = data['coverage']

    baseRate = lookupValue(ratesTable, location, 'baseRate')
    riskMultiplier = lookupValue(riskTable, age, 'riskMultiplier')

    premium = applyFormula(
        'base * risk * coverage * 0.01',
        {
            'base': baseRate,
            'risk': riskMultiplier,
            'coverage': coverage
        }
    )

    return round(premium, 2)


# -------------------------------
# LLM Function Definition
# -------------------------------

def create_quote(name, profession, premium, tone):
    """
    Function called by LLM to generate final quote
    """
    return (
        f"{name}, investing ₹{premium} today is a step toward long-term security. "
        f"As a {profession}, this choice reflects foresight, responsibility, and confidence."
    )


# -------------------------------
# LLM Prompt + Function Calling Simulation
# -------------------------------

def llm_generate_quote(userProfile, premium):
    """
    Simulates LLM prompt + function calling
    """

    prompt = f"""
    Generate a personalized insurance quote.

    User Details:
    Name: {userProfile['name']}
    Profession: {userProfile['profession']}
    Premium Amount: ₹{premium}

    Instructions:
    - Choose an appropriate tone
    - Keep it under 40 words
    - Return a function call to create_quote
    """

    # ---- LLM "Reasoning" (Simulated) ----
    if premium < 5000:
        tone = "encouraging"
    elif premium < 10000:
        tone = "motivational"
    else:
        tone = "reassuring"

    # ---- LLM Function Call ----
    quote = create_quote(
        name=userProfile['name'],
        profession=userProfile['profession'],
        premium=premium,
        tone=tone
    )

    return {
        "tone": tone,
        "quote": quote,
        "llm_prompt_used": prompt.strip()
    }


# -------------------------------
# Sample Data
# -------------------------------

userProfile = {
    "name": "Pradeep",
    "age": 22,
    "location": "India",
    "coverage": 500000,
    "profession": "engineering student"
}

ratesTable = {
    "India": {"baseRate": 1.2},
    "USA": {"baseRate": 1.8}
}

riskTable = {
    18: {"riskMultiplier": 1.1},
    22: {"riskMultiplier": 1.3},
    30: {"riskMultiplier": 1.6}
}


# -------------------------------
# Execution
# -------------------------------

premium_amount = premium_calculator(userProfile, ratesTable, riskTable)
llm_result = llm_generate_quote(userProfile, premium_amount)

print(f"Premium Amount: ₹{premium_amount}")
print(f"Quote Tone: {llm_result['tone']}")
print(f"Personalized Quote: {llm_result['quote']}")
