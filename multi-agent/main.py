from agent import myAgent
import chainlit as cl
import asyncio

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Welcome to the Ammar Multi-Agent System! How can I assist you?").send()

@cl.on_message
async def main(message: cl.Message):
    user_input = message.content
    response = await myAgent(user_input)  # pass user_input to myAgent

    await cl.Message(content=f"{response}").send()
