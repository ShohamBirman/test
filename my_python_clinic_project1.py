import re
import random
import time
import streamlit as st


def parse_input(user_input):
    """
    Parses user input and determines the appropriate response based on predefined patterns.
    Args:
    - user_input (str): The user's input
    Returns:
    - str: The response generated by the appropriate function based on the detected pattern,
           or the default response if no pattern is matched.
    """
    # Regular expressions for different input patterns
    negation_pattern = re.compile(r"\b(no|not)\b", re.IGNORECASE)
    affirmation_pattern = re.compile(r"\b(?:yes|sure|indeed|certainly)\b", re.IGNORECASE)
    question_pattern = re.compile(r".*\?$")
    repetitions_pattern = re.compile(r"(\b(yes it is)|(no it is not)|(no it isn't)\b)", re.IGNORECASE)
    personal_statement_pattern = re.compile(
        r"\b(i think\b|\bin my idea\b|\bmy opinion is\b|\bi believe\b|\bin my view\b|\bmy experience with\b)",
        re.IGNORECASE)
    dismissal_pattern = re.compile(
        r"\b(i don('*)t believe\b|\bi don('*)t agree\b|\not convinced\b|\bdisagreed\b|\bi find it hard to accept\b)\b",
        re.IGNORECASE)
    never_always_pattern = re.compile(r"\b(never|always)\b", re.IGNORECASE)
    too_it_will_pattern = re.compile(r"too\s+([A-Za-z]+)|it will\s+([A-Za-z]+)", re.IGNORECASE)
    emotions_pattern = re.compile(
        r"\b(i feel|feeling|annoying|infuriating|irritating|frustrating|amazing|exciting|"
        r"joyful|happy|positive|uplifting|sad|angry|confused)\b", re.IGNORECASE)
    absolute_keyword = re.compile(r"\b(impossible|absolutely|everyone knows)\b", re.IGNORECASE)
    futility_keyword = re.compile(r"\b(pointless|silly|sense)\b", re.IGNORECASE)
    you_are_pattern = re.compile(
        r"you are\s+([A-Za-z]+)|you(\'*)re\s+([A-Za-z]+)|you are not\s+([A-Za-z]+)|you(\'*)re not\s+([A-Za-z]+)",
        re.IGNORECASE)
    dont_understand_pattern = re.compile(r"\b(don('*)t you understand(\?*))|(you don('*)t understand)\b", re.IGNORECASE)
    right_wrong_pattern = re.compile(r"\b(right|wrong)\b", re.IGNORECASE)
    agreement_with_doubt_pattern = re.compile(r"\b(agree, but|agree, although)\b", re.IGNORECASE)
    agreement_pattern = re.compile(r"\b(i agree\b|\bi see\b|\bagreed\b)", re.IGNORECASE)
    preferences_pattern = re.compile(r"\b(i prefer\b|\bi like\b|\bi dislike\b)\b", re.IGNORECASE)
    comparison_pattern = re.compile(r"\b(better than\b|\bworse than\b|\bsimilar to\b)\b", re.IGNORECASE)
    complexity_pattern = re.compile(r"\b(but what if\b|\bconsidering the complexities\b)", re.IGNORECASE)
    unexplored_areas_pattern = re.compile(r"\b(i haven('*)t considered\b|\bwhat about\b)", re.IGNORECASE)
    future_implications_pattern = re.compile(r"\b(in the future\b|\bwill lead to\b|\bconsequences will be\b)\b",
                                             re.IGNORECASE)
    seeking_advice_pattern = re.compile(r"\b(what should i do\b|\bany suggestions\b|\bwhat do you think\b)\b",
                                        re.IGNORECASE)

    # Conditions to match the pattern and call the correct function for the responses
    if re.search(repetitions_pattern, user_input):
        return handle_repetitions(user_input)
    elif re.search(you_are_pattern, user_input):
        match = re.search(you_are_pattern, user_input)
        return handle_you_are_pattern(match)
    elif re.search(negation_pattern, user_input):
        return handle_negation(user_input)
    elif re.search(affirmation_pattern, user_input):
        return handle_affirmation(user_input)
    elif re.search(question_pattern, user_input):
        return handle_question(user_input)
    elif re.search(personal_statement_pattern, user_input):
        return handle_personal_statement(user_input)
    elif re.search(dismissal_pattern, user_input):
        return handle_dismissal_pattern(user_input)
    elif re.search(never_always_pattern, user_input):
        return handle_never_always(user_input)
    elif re.search(too_it_will_pattern, user_input):
        match = re.search(too_it_will_pattern, user_input)
        return handle_too_it_will(match)
    elif re.search(emotions_pattern, user_input):
        return handle_emotions(user_input)
    elif re.search(absolute_keyword, user_input):
        return handle_absolute_keyword(user_input)
    elif re.search(futility_keyword, user_input):
        return handle_futility(user_input)
    elif re.search(dont_understand_pattern, user_input):
        return handle_dont_understand(user_input)
    elif re.search(right_wrong_pattern, user_input):
        return handle_right_wrong(user_input)
    elif re.search(agreement_with_doubt_pattern, user_input):
        return handle_agreement_doubt_pattern(user_input)
    elif re.search(agreement_pattern, user_input):
        return handle_agreement_pattern(user_input)
    elif re.search(preferences_pattern, user_input):
        return handle_preferences_pattern(user_input)
    elif re.search(comparison_pattern, user_input):
        return handle_comparison_pattern(user_input)
    elif re.search(complexity_pattern, user_input):
        return handle_complexity_pattern(user_input)
    elif re.search(unexplored_areas_pattern, user_input):
        return handle_unexplored_areas_pattern(user_input)
    elif re.search(future_implications_pattern, user_input):
        return handle_future_implications_pattern(user_input)
    elif re.search(seeking_advice_pattern, user_input):
        return handle_seeking_advice_pattern(user_input)

    return handle_default_case()  # Default case


# Function to handle the default case
def handle_default_case():
    """
    Handles the default case when no specific pattern matches.
    """
    responses = [
        "Could you provide more context for that statement?",
        "I'm curious to hear more. What led you to this perspective?",
        "Can you elaborate more?"
    ]
    return random.choice(responses)


def handle_negation(user_input):
    """
    Handles responses when the user expresses negation in their input; (Pattern: no|not).
    Args:
    - user_input (str): The user's input
    Returns:
    - str: A randomly chosen response from a predefined set
    """
    responses = [
        "I hear you, but have you considered the alternative?",
        "Sometimes a 'no' is just a 'yes' waiting to be discovered. What do you think?",
        "What if your 'not' is the key to unlocking a hidden truth?"
    ]
    return random.choice(responses)


def handle_affirmation(user_input):
    """
    Handles responses when the user expresses affirmation in their input.
    (Pattern: yes|sure|indeed|certainly).
    Args:
    - user_input (str): The user's input
    Returns:
    - str: A randomly chosen response from a predefined set
    """
    responses = [
        "That's an interesting standpoint. What led you to that conclusion?",
        "Indeed, but what if there's an alternative perspective?",
        "Yes, but have you considered the beauty of uncertainty?",
        "Interesting perspective! Can you convince me more?",
        "Is it really, or are we just agreeing to disagree?",
        "How can you be so sure? Have you considered the opposite option?"
    ]
    return random.choice(responses)


def handle_question(user_input):
    """
    Handles responses when the user asks a question; (Pattern: "?").
    Args:
    - user_input (str): The user's input
    Returns:
    - str: A randomly chosen response from a predefined set
    """
    responses = [
        "What if the answer is hidden in the question itself?",
        "How often do you find yourself pondering such questions?",
        "Why do you think that is?",
        "Good question! What's your take on it?",
        "Let's figure it out together, what do you think?"
    ]
    return random.choice(responses)


def handle_repetitions(user_input):
    """
    Handles responses when the user's input involves repetitions like 'yes it is' or 'no it isn't'.
    Args:
    - user_input (str): The user's input
    Returns:
    - str or None: A randomly chosen response from a predefined set if a repetition pattern is detected, otherwise None
    """
    if "yes it is" in user_input.strip().lower():
        responses = [
            "No it isn't!",
            "This feels like déjà vu. Or is it just a spirited agreement?",
            "Yes it is, no it isn't, the dance of contradictions!"
        ]
        return random.choice(responses)
    elif "no it is not" in user_input.strip().lower() or "no it isn't" in user_input.strip().lower():
        responses = [
            "Yes it is!",
            "Yes it is, no it isn't, the dance of contradictions!"
        ]
        return random.choice(responses)
    return None


def handle_personal_statement(user_input):
    """
    Handles responses when the user makes a personal statement or expresses their viewpoint.
    (Pattern: I think|in my idea|my opinion is|I believe|in my view|my experience with)
    Args:
    - user_input (str): The user's input
    Returns:
    - str: A randomly chosen response from a predefined set
    """
    responses = [
        "I appreciate your viewpoint! Let's explore it further.",
        "Interesting, can you elaborate more?",
        "Have you considered the opposite opinion?",
        "Interesting perspective. Can you provide more details or examples to support your view?",
        "Your opinion matters! What led you to form that particular viewpoint?",
        "Personal experiences add richness to the conversation. How has this shaped your perspective?",
        "Your viewpoint is unique. Can you share more about your personal experiences in this context?"
    ]
    return random.choice(responses)


def handle_dismissal_pattern(user_input):
    """
    Handles responses when the user's input indicates a dismissal or disagreement.
    (Pattern: I don't believe|I don't agree|not convinced|disagreed|I find it hard to accept)
    Args:
    - user_input (str): The user's input
    Returns:
    - str: A randomly chosen response from a predefined set
    """
    responses = [
        "What would it take to convince you, I wonder?",
        "What if it's just a different way of thinking?",
        "To agree or not to agree, that is the question.",
        "Not convinced? Well, I'll put on my most convincing argument hat!",
        "A touch of disagreement adds flavor to the conversation. Tell me more about your position",
        "I sense skepticism in the air. Shall we agree to disagree?",
        "Interesting. Let's explore the differences in our perspectives."
    ]
    return random.choice(responses)


def handle_never_always(user_input):
    """
    Handles responses when the user's input includes expressions like 'never' or 'always'.
    Args:
    - user_input (str): The user's input
    Returns:
    - str or None: A randomly chosen response from a predefined set if a 'never' or 'always' pattern is detected,
     otherwise None
    """
    if "never" in user_input.strip().lower():
        responses = [
            "Never? Isn't it a bit harsh to use such a final word?",
            "Never say never, unless you're saying never say never.",
            "Never is a strong word. Are there no circumstances where this might not hold true?",
            "Life is full of surprises. Can we consider scenarios where 'never' might not be accurate?"
        ]
        return random.choice(responses)
    elif "always" in user_input.strip().lower():
        responses = [
            "Always? Isn't life full of exceptions?",
            "Always? Isn't that a bit too definitive?",
            "Always is a strong word. Are there no gray areas?"
        ]
        return random.choice(responses)
    return None


def handle_too_it_will(match):
    """
    Handles responses when the user's input indicates a situation involving 'too' or 'it will'.
    Args:
    - match (re.Match): A regex match object
    Returns:
    - str or None: A response generated based on the matched groups in the regex pattern, or None if no match is found
    """
    if match.group(1):
        return f"Too {match.group(1)}, or just a bit more than what you prefer?"
    elif match.group(2):
        return f"Will it {match.group(2)}, or is that just a possibility you're considering?"
    return None


def handle_emotions(user_input):
    """
    Handles responses when the user's input involves expressions related to emotions.
    Args:
    - user_input (str): The user's input
    Returns:
    - str: A response based on detected emotional keywords in the user's input
    """
    annoying = ['infuriating', 'irritating', 'frustrating', 'angry', 'annoying']
    positives = ['amazing', 'exciting', 'joyful', 'happy', 'positive', 'uplifting']
    if "sad" in user_input.strip().lower():
        return f"I sense a touch of sadness. What's on your mind?"
    elif "confused" in user_input.strip().lower():
        return f"Confusion can be intriguing. Let's untangle the thoughts together."
    elif any(annoy in user_input for annoy in annoying):
        keyword_retort = user_input.split()[0]
        return f"{keyword_retort}, or just mildly irritating in a delightful way?"
    elif any(positive in user_input for positive in positives):
        return f"Positive vibes! What's bringing joy to your argumentative world?"
    else:
        return f"Interesting emotions you're expressing. Care to share more?"


def handle_absolute_keyword(user_input):
    """
    Handles responses when the user's input includes absolute expressions like:
    'impossible'|'everyone knows'|'absolutely'.
    Args:
    - user_input (str): The user's input
    Returns:
    - str or None: A randomly chosen response from a predefined set if an absolute keyword pattern is detected,
     otherwise None
    """
    if "impossible" in user_input.strip().lower():
        responses = [
            "Impossible? Isn't life full of unexpected possibilities and surprises?",
            "Impossible is just a challenge for the imagination."
        ]
        return random.choice(responses)
    elif "everyone knows" in user_input.strip().lower():
        return "If everyone knows it, how come we're still discussing about that?"
    elif "absolutely" in user_input.strip().lower():
        return "Absolutely, or just slightly off from another angle?"
    return None


def handle_futility(user_input):
    """
    Handles responses when the user's input includes expressions related to futility,
    such as 'pointless'|'silly'|'sense'(=refers to 'make no sense').
    Args:
    - user_input (str): The user's input
    Returns:
    - str or None: A randomly chosen response from a predefined set if a futility keyword pattern is detected,
     otherwise None
    """
    if "pointless" in user_input.strip().lower():
        responses = [
            "Pointless, or just challenging in an unexpected way?",
            "On the contrary, it's full of points. Can you see them?"
        ]
        return random.choice(responses)
    elif "sense" in user_input.strip().lower():
        responses = [
            "But what if it makes sense and the world is confused?",
            "Well, sometimes making sense is overrated"
        ]
        return random.choice(responses)
    elif "silly" in user_input.strip().lower():
        responses = [
            "Have you considered the opposite?",
            "Is 'silly' not a matter of perspective?"
        ]
        return random.choice(responses)
    return None


def handle_you_are_pattern(match):
    """
    Handles responses when the user's input includes patterns like 'you are'|'you're'|'you are not'|'you're not'.
    Args:
    - match (re.Match): The match object obtained from applying the 'you_are_pattern' regex
    Returns:
    - str or None: A response generated based on the detected pattern, otherwise None
    """
    if match.group(1):
        return f"Am I, or is it you who is {match.group(1)}?"
    elif match.group(2):
        return f"Am I, or is it you who is {match.group(2)}?"
    elif match.group(3):
        return f"Am I, or is it you who is {match.group(3)}?"
    elif match.group(4):
        return f"Am I, or is it you who is {match.group(4)}?"
    return None


def handle_dont_understand(user_input):
    """
    Handles responses when the user's input indicates a lack of understanding.
    (Pattern: don't you understand|you don't understand)
    Args:
    - user_input (str): The user's input
    Returns:
    - str or None: A randomly chosen response from a predefined set if a 'don't understand' pattern is detected,
    otherwise None
    """
    responses = [
        "Is understanding the same as agreeing?"
        "Ah, the classic 'you don't understand.' Enlighten me, what am I missing?",
        "I hear you. Help me understand better.",
        "Understanding is subjective. Help me see it from your angle. What am I not getting?",
    ]
    return random.choice(responses)


def handle_right_wrong(user_input):
    """
    Handles responses when the user's input includes expressions related to 'right' or 'wrong'.
    Args:
    - user_input (str): The user's input
    Returns:
    - str or None: A randomly chosen response from a predefined set if a 'right' or 'wrong' pattern is detected,
    otherwise None
    """
    if "right" in user_input.strip().lower():
        responses = [
            "Have you considered the opposite opinion?",
            "Rightness in the air! What factors contribute to this assertion of correctness?",
            "Right, you say? Let's dive into the details of why you think so."
        ]
        return random.choice(responses)
    elif "wrong" in user_input.strip().lower():
        responses = [
            "Or perhaps it's just an unconventional right?",
            "Why do you believe it's wrong?",
            "Convince me with your 'wrong'!"
        ]
        return random.choice(responses)
    return None


def handle_agreement_doubt_pattern(user_input):
    """
    Handles responses when the user's input includes expressions of agreement with doubt.
    (Pattern: agree, but|agree, although)
    Args:
    - user_input (str): The user's input
    Returns:
    - str or None: A randomly chosen response from a predefined set if an agreement with doubt pattern is detected,
    otherwise None
    """
    responses = [
        "Agreeing with a hint of skepticism. What aspects make you hesitant?",
        "Interesting perspective. What reservations do you have despite the agreement?"
    ]
    return random.choice(responses)


def handle_agreement_pattern(user_input):
    """
    Handles responses when the user's input indicates agreement.
    (Pattern: i agree|i see|agreed)
    Args:
    - user_input (str): The user's input
    Returns:
    - str or None: A randomly chosen response from a predefined set if an agreement pattern is detected, otherwise None
    """
    responses = [
        "Glad we found common ground! What other points do you think we align on?",
        "Acknowledging the point! How do you think this agreement influences our overall discussion?",
        "Great to find common ground. What other aspects of our conversation resonate with you?"
    ]
    return random.choice(responses)


def handle_preferences_pattern(user_input):
    """
    Handles responses when the user's input includes expressions related to personal preferences.
    (Pattern: i prefer|i like|i dislike)
    Args:
    - user_input (str): The user's input
    Returns:
    - str or None: A randomly chosen response from a predefined set if a preferences pattern is detected, otherwise None
    """
    responses = [
        "Preferences play a role. What influences your preferences in this context?",
        "Interesting preferences! How do they shape your overall stance on this matter?"
    ]
    return random.choice(responses)


def handle_comparison_pattern(user_input):
    """
    Handles responses when the user's input includes expressions related to comparisons.
    (Pattern: better than|worse than|similar to)
    Args:
    - user_input (str): The user's input
    Returns:
    - str or None: A randomly chosen response from a predefined set if a comparison pattern is detected, otherwise None
    """
    responses = [
        "Comparisons bring depth. What factors do you see contributing to this comparison?",
        "Interesting choice of comparison. How does it impact your overall viewpoint?"
    ]
    return random.choice(responses)


def handle_complexity_pattern(user_input):
    """
    Handles responses when the user's input includes expressions related to the complexity of the discussion.
    (Pattern: but what if|considering the complexities)
    Args:
    - user_input (str): The user's input
    Returns:
    - str or None: A randomly chosen response from a predefined set if a complexity pattern is detected, otherwise None
    """
    responses = [
        "Adding layers to the discussion. How do these complexities shape your overall viewpoint?",
        "Complex scenarios indeed. Let's delve deeper into the intricacies of your argument."
    ]
    return random.choice(responses)


def handle_unexplored_areas_pattern(user_input):
    """
    Handles responses when the user's input includes expressions related to unexplored areas in the discussion.
    (Pattern: i haven't considered|what about)
    Args:
    - user_input (str): The user's input
    Returns:
    - str or None: A randomly chosen response from a predefined set if an unexplored areas pattern is detected,
    otherwise None
    """
    responses = [
        "Unexplored territories! What prompted you to think about this aspect we haven't discussed?",
        "Interesting point. Let's venture into the areas we haven't covered. What else comes to mind?"
    ]
    return random.choice(responses)


def handle_future_implications_pattern(user_input):
    """
    Handles responses when the user's input includes expressions related to future implications.
    (Pattern: in the future|will lead to|consequences will be)
    Args:
    - user_input (str): The user's input
    Returns:
    - str or None: A randomly chosen response from a predefined set if a future implications pattern is detected,
    otherwise None
    """
    responses = [
        "Looking ahead! How do you envision these future implications unfolding?",
        "Future consequences are crucial. What considerations should we keep in mind?"
    ]
    return random.choice(responses)


def handle_seeking_advice_pattern(user_input):
    """
    Handles responses when the user's input indicates seeking advice.
    (Pattern: what should I do|any suggestions|what do you think)
    Args:
    - user_input (str): The user's input
    Returns:
    - str or None: A randomly chosen response from a predefined set if a seeking advice pattern is detected,
    otherwise None
    """
    responses = [
        "Seeking advice? Let's explore different perspectives together. What options are you considering?",
        "I'm here to help. What specific advice or insights are you looking for in this situation?"
    ]
    return random.choice(responses)


# Function to handle the main argument session
def main():
    """
    Main function to run the argument clinic session.
    """

    st.title('Welcome to the Python Argument Clinic!')
    st.write(f'''Here is a sample conversation to give you an idea of the interaction at the clinic:

    User: "I think this is silly."
    Clinic: "Have you considered the opposite?"
    User: "Yes, but it's still silly."
    Clinic: "Is 'silly' not a matter of perspective?"
    ''')

    start_argument = st.text_input("Would you like to start an argument? (yes/no): ").strip().lower()
    if start_argument.strip().lower() == "yes":
        # User input for the duration of the argument
        argue_time = st.number_input("How many minutes would you like to argue? (enter the number of minutes): ", min_value=1, max_value=60, step=1)
        start_time = time.time() / 60
        end_time = start_time + argue_time  # Calculate the end time
        if not argue_time:
            pass
        else:
            st.write("\nThe Argument Clinic is open! What is your first argument? ")
            st.write("\n**(Note: you can type 'exit' to end the argument at any point you want.)\n")

        # Main argument session loop
        while time.time() / 60 < end_time:
            user_input = st.text_input("User: ").strip().lower()

            if user_input.lower().strip() == "exit":
                break

            response = parse_input(user_input)
            st.write(f"Clinic: {response}")  # Print the response

            if time.time() / 60 >= end_time:
                break

        st.write("The argument clinic session is over, Thanks for participating.\nHave a great day!")


if __name__ == "__main__":  # This block executes when the script is run as the main program.
    main()