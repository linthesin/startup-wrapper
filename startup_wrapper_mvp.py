import streamlit as st
import openai
import datetime

# Set your OpenAI API key here or use environment variables
openai.api_key = "YOUR_API_KEY"

# --- Functions ---
def run_market_research(idea):
    prompt = f"""
    You are a market research analyst. Given a product idea, generate:
    - A brief market overview
    - Top 5 competitors with a 1-sentence summary each
    - Target customer personas
    - Recent trends in the space

    Idea: {idea}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

def run_daily_journal(entry):
    prompt = f"""
    You are a startup mentor helping founders reflect on their daily work. Based on the journal entry below, summarize:
    - Key accomplishments
    - Lessons learned
    - Challenges mentioned
    - Suggestions or encouragement

    Journal Entry: {entry}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )
    return response.choices[0].message.content

# --- Streamlit App ---
st.title("🚀 Startup Assistant")

option = st.sidebar.selectbox("Choose a tool:", ["Market Research Bot", "Daily Startup Journal"])

if option == "Market Research Bot":
    st.header("📊 Market Research Bot")
    idea = st.text_area("Describe your startup idea:")
    if st.button("Run Research") and idea:
        with st.spinner("Analyzing market..."):
            output = run_market_research(idea)
        st.markdown("---")
        st.subheader("Market Research Summary")
        st.write(output)

elif option == "Daily Startup Journal":
    st.header("📝 Daily Startup Journal")
    today = datetime.date.today()
    entry = st.text_area("What's on your mind today?", key=today)
    if st.button("Generate Summary") and entry:
        with st.spinner("Reflecting..."):
            output = run_daily_journal(entry)
        st.markdown("---")
        st.subheader("Reflection Summary")
        st.write(output)
