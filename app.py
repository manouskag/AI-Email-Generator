import streamlit as st

from src.email_generator import generate_email

from src.prompts import (
    TONES,
    FORMALITY_LEVELS,
    EMAIL_LENGTHS,
    RECIPIENT_TYPES,
    LANGUAGES,
    EMAIL_TYPES
)


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(

    page_title="AI Email Studio",

    page_icon="✉️",

    layout="wide"
)


# ==================================================
# HEADER
# ==================================================

st.title("✉️ AI Email Generator")


st.divider()


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.header("⚙️ Email Settings")


    email_type = st.selectbox(
        "Email Type",
        EMAIL_TYPES
    )


    recipient = st.selectbox(
        "Recipient Type",
        RECIPIENT_TYPES
    )


    recipient_name = st.text_input(
        "Recipient Name",
        placeholder="Example: Dr. Sarah Johnson"
    )


    sender_name = st.text_input(
        "Your Name",
        placeholder="Example: Melissa"
    )


    tone = st.selectbox(
        "Tone",
        TONES
    )


    formality = st.selectbox(
        "Formality",
        FORMALITY_LEVELS
    )


    length = st.selectbox(
        "Email Length",
        EMAIL_LENGTHS
    )


    language = st.selectbox(
        "Language",
        LANGUAGES
    )


# ==================================================
# MAIN AREA
# ==================================================

st.subheader("📝 Email Information")


purpose = st.text_input(

    "Email Purpose",

    placeholder=(
        "Example: Request a two-day extension "
        "for my assignment"
    )
)


key_points = st.text_area(

    "Important Points",

    height=180,

    placeholder=(
        "Enter the important information that "
        "the email should contain..."
    )
)


call_to_action = st.text_input(

    "Call To Action",

    placeholder=(
        "Example: Please let me know if my request "
        "can be approved."
    )
)


additional_instructions = st.text_area(

    "Additional Instructions",

    height=120,

    placeholder=(
        "Example: Keep the email respectful "
        "and avoid sounding demanding."
    )
)


# ==================================================
# GENERATE EMAIL BUTTON
# ==================================================

generate_button = st.button(

    "✨ Generate Email",

    type="primary",

    use_container_width=True
)


# ==================================================
# GENERATION
# ==================================================

if generate_button:

    # -----------------------------------------------
    # VALIDATION
    # -----------------------------------------------

    if not purpose.strip():

        st.warning(
            "Please enter the purpose of the email."
        )

    elif not key_points.strip():

        st.warning(
            "Please enter the important points."
        )

    else:

        # -------------------------------------------
        # CALL CREWAI
        # -------------------------------------------

        with st.spinner(
            "🤖 CrewAI agents are working..."
        ):

            try:

                result = generate_email(

                    email_type=email_type,

                    recipient=recipient,

                    recipient_name=recipient_name,

                    sender_name=sender_name,

                    purpose=purpose,

                    key_points=key_points,

                    tone=tone,

                    formality=formality,

                    length=length,

                    language=language,

                    call_to_action=call_to_action,

                    additional_instructions=(
                        additional_instructions
                    )
                )


                # Save result
                st.session_state[
                    "generated_email"
                ] = result


            except Exception as error:

                st.error(
                    f"Something went wrong:\n\n{error}"
                )


# ==================================================
# DISPLAY GENERATED EMAIL
# ==================================================

if "generated_email" in st.session_state:

    st.divider()

    st.subheader("📧 Generated Email")


    result = st.session_state[
        "generated_email"
    ]


    st.text_area(

        "Email",

        value=result,

        height=450
    )


    # -----------------------------------------------
    # DOWNLOAD
    # -----------------------------------------------

    st.download_button(

        label="📥 Download Email",

        data=result,

        file_name="generated_email.txt",

        mime="text/plain",

        use_container_width=True
    )