import os

from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM


# --------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# --------------------------------------------------

load_dotenv()


# --------------------------------------------------
# GET GEMINI API KEY
# --------------------------------------------------

def get_gemini_api_key():

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is missing. "
            "Please add your Gemini API key to the .env file."
        )

    return api_key


# --------------------------------------------------
# CREATE EMAIL CREW
# --------------------------------------------------

def create_email_crew():

    # Get API key
    gemini_api_key = get_gemini_api_key()


    # --------------------------------------------------
    # GEMINI LLM
    # --------------------------------------------------

    llm = LLM(
        model="gemini/gemini-3.6-flash",
        api_key=gemini_api_key,
        temperature=0.7
    )


    # ==================================================
    # AGENT 1 - EMAIL STRATEGIST
    # ==================================================

    strategist = Agent(

        role="Email Communication Strategist",

        goal=(
            "Analyze the user's email requirements and "
            "develop the best communication strategy."
        ),

        backstory=(
            "You are an expert communication strategist "
            "with extensive knowledge of professional email "
            "writing, business communication, academic "
            "communication, persuasion, audience analysis "
            "and email etiquette."
        ),

        llm=llm,

        verbose=True,

        allow_delegation=False
    )


    # ==================================================
    # AGENT 2 - EMAIL WRITER
    # ==================================================

    writer = Agent(

        role="Professional Email Writer",

        goal=(
            "Write a clear, natural, personalized and "
            "effective email based on the communication "
            "strategy."
        ),

        backstory=(
            "You are an experienced professional email writer. "
            "You specialize in academic, business, professional, "
            "customer service, recruitment and personal emails. "
            "You adapt writing style according to the recipient, "
            "tone, formality and purpose."
        ),

        llm=llm,

        verbose=True,

        allow_delegation=False
    )


    # ==================================================
    # AGENT 3 - EMAIL REVIEWER
    # ==================================================

    reviewer = Agent(

        role="Email Quality Reviewer",

        goal=(
            "Review the generated email and produce a "
            "polished final version."
        ),

        backstory=(
            "You are a meticulous professional editor. "
            "You specialize in grammar, clarity, tone, "
            "professionalism, persuasion, conciseness "
            "and effective email structure."
        ),

        llm=llm,

        verbose=True,

        allow_delegation=False
    )


    # ==================================================
    # TASK 1 - STRATEGY
    # ==================================================

    strategy_task = Task(

        description="""

        Analyze the user's email requirements.

        EMAIL TYPE:
        {email_type}

        RECIPIENT TYPE:
        {recipient}

        RECIPIENT NAME:
        {recipient_name}

        SENDER NAME:
        {sender_name}

        PURPOSE:
        {purpose}

        IMPORTANT POINTS:
        {key_points}

        TONE:
        {tone}

        FORMALITY:
        {formality}

        EMAIL LENGTH:
        {length}

        LANGUAGE:
        {language}

        CALL TO ACTION:
        {call_to_action}

        ADDITIONAL INSTRUCTIONS:
        {additional_instructions}


        Develop a communication strategy for the email.

        Include:

        1. Main objective
        2. Target audience
        3. Recommended structure
        4. Important information
        5. Recommended tone
        6. Call to action
        7. Information that should be avoided
        8. Personalization opportunities

        Do not invent information.
        """,

        expected_output=(
            "A detailed but concise email communication strategy."
        ),

        agent=strategist
    )


    # ==================================================
    # TASK 2 - WRITE EMAIL
    # ==================================================

    writing_task = Task(

        description="""

        Using the communication strategy from the strategist,
        write the complete email.

        Follow these requirements:

        - Use the requested tone.
        - Follow the requested formality.
        - Respect the requested length.
        - Use the requested language.
        - Include all important points.
        - Include the requested call to action.
        - Personalize the email when recipient information
          is available.
        - Do not invent facts.
        - Do not mention artificial intelligence.
        - Do not mention CrewAI.
        - Do not include explanations outside the email.

        Return the result in this format:

        SUBJECT:
        <email subject>

        BODY:
        <email body>
        """,

        expected_output=(
            "A complete email containing a subject and body."
        ),

        agent=writer,

        context=[strategy_task]
    )


    # ==================================================
    # TASK 3 - REVIEW EMAIL
    # ==================================================

    review_task = Task(

        description="""

        Review the email created by the writer.

        Carefully check:

        - Grammar
        - Spelling
        - Sentence structure
        - Clarity
        - Tone
        - Formality
        - Professionalism
        - Repetition
        - Personalization
        - Call to action
        - Overall readability

        Fix any problems you find.

        Preserve the original meaning.

        Do not introduce unsupported facts.

        Return ONLY the final polished email.

        Use this format:

        SUBJECT:
        <final subject>

        BODY:
        <final email body>
        """,

        expected_output=(
            "A polished final email with subject and body."
        ),

        agent=reviewer,

        context=[
            strategy_task,
            writing_task
        ]
    )


    # ==================================================
    # CREATE CREW
    # ==================================================

    crew = Crew(

        agents=[
            strategist,
            writer,
            reviewer
        ],

        tasks=[
            strategy_task,
            writing_task,
            review_task
        ],

        process=Process.sequential,

        verbose=True
    )


    return crew