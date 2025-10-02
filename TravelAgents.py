from crewai import Agent
from TravelTools import search_web_tool
from crewai import LLM
import os
from dotenv import load_dotenv
import streamlit as st
from crewai import LLM
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

GOOGLE_API_KEY=st.secrets['GOOGLE_API_KEY']
# GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

llm=LLM(
    model='gemini/gemini-2.5-flash',
    api_key=GOOGLE_API_KEY
)

# Agents
guide_expert = Agent(
    role="City Local Guide Expert",
    goal=
    "Provides information on things to do in the city based on user interests.",
    backstory="A local expert passionate about sharing city experiences.",
    tools=[search_web_tool],
    # verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)

location_expert = Agent(
    role="Travel Trip Expert",
    goal="Provides travel logistics and essential information.",
    backstory=
    "A seasoned traveler who knows everything about different cities.",
    tools=[search_web_tool],
    # verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)

planner_expert = Agent(
    role="Travel Planning Expert",
    goal="Compiles all gathered information to create a travel plan.",
    backstory="An expert in planning seamless travel itineraries.",
    tools=[search_web_tool],
    # verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)