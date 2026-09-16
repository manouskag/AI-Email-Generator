from src.email_crew import create_email_crew


def generate_email(
    email_type,
    recipient,
    recipient_name,
    sender_name,
    purpose,
    key_points,
    tone,
    formality,
    length,
    language,
    call_to_action,
    additional_instructions
):

    # Create CrewAI crew
    crew = create_email_crew()


    # --------------------------------------------------
    # INPUTS FOR CREWAI
    # --------------------------------------------------

    inputs = {

        "email_type": email_type,

        "recipient": recipient,

        "recipient_name": recipient_name,

        "sender_name": sender_name,

        "purpose": purpose,

        "key_points": key_points,

        "tone": tone,

        "formality": formality,

        "length": length,

        "language": language,

        "call_to_action": call_to_action,

        "additional_instructions": additional_instructions
    }


    # --------------------------------------------------
    # START CREW
    # --------------------------------------------------

    result = crew.kickoff(
        inputs=inputs
    )


    # Return final result
    return str(result)