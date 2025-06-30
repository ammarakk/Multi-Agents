from agents import Agent,Runner, set_tracing_disabled,OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI

load_dotenv()
set_tracing_disabled(True)

provider = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",  # Remove /openai/
)

model=OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=provider,
)
#Web developer agent
web_dev= Agent(
    name="Web Developer ",
    instructions="Build responsive and performant websites using modern frmworks",
    model=model,
    handoff_description="handoff to a web developer  if the task is related to web development",
)

#Mobile developer agent
mobile_dev= Agent(
    name="Mobile App Developer Expert",
    instructions="Develop cross-platform mobile apps using modern frameworks",
    model=model,
    handoff_description="handoff to a mobile app developer if the task is related to mobile development",
)

#Marketing agent
marketing= Agent(
    name="Marketing Expert Agent",
    instructions="Create and execute marketing strategies to promote products Lauches",
    model=model,
    handoff_description="handoff to a marketing agent if the task is related to marketing",
)

#Manager
#Main Agent that delegates tasks to other agents
async def myAgent(user_input):
    manager= Agent(
        name="Manager",
        instructions="You will chat with the user and delegate tasks to the appropriate agent based on the user's request. If the task is related to web development, handoff to the Web Developer Expert. If the task is related to mobile development, handoff to the Mobile App Developer Expert. If the task is related to marketing, handoff to the Marketing Expert.",
        model=model,
        handoffs=[web_dev, mobile_dev, marketing],
    )

    response=await Runner.run(
        manager,
        input=user_input)
    return response.final_output

