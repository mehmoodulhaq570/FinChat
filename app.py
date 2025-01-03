import chainlit as cl
from embedchain import Pipeline as App

@cl.on_chat_start
async def on_chat_start():
    app = App.from_config(config_path="config.yml")

    await cl.Message(content="Welcome to FinChat! You can upload a PDF file of an Earnings Report (max 10 MB) for analysis.").send()

    files = await cl.AskFileMessage(
        content="Please upload an Earnings Report (PDF file) to get started!",
        accept=["application/pdf"],
        max_size_mb="10",
        max_files=1
    ).send()

    if files:
        text_file = files[0]

        await cl.Message(content=f"⏳ Uploading {text_file.name}... Please wait.").send()
        app.add(text_file.path, data_type='pdf_file')
        cl.user_session.set("app", app)
        await cl.Message(content=f"✅ File '{text_file.name}' successfully uploaded and added to the knowledge database! \nYou can upload another file by typing 'upload the next file' when you're ready.").send()

    else:
        # Handle if no file was uploaded
        await cl.Message(content="❌ No file was uploaded. Please try again.").send()

# This will handle the reception of a new message and only upload the next file if the user asks
@cl.on_message
async def on_message(message: cl.Message):
    if "upload the next file" in message.content.lower():
       
        files = await cl.AskFileMessage(
            content="Please upload the next Earnings Report (PDF file).",
            accept=["application/pdf"],
            max_size_mb="10",
            max_files=1
        ).send()

        if files:
            text_file = files[0]         
            await cl.Message(content=f"⏳ Uploading {text_file.name}... Please wait.").send()         
            app = cl.user_session.get("app")

            if app:
                
                app.add(text_file.path, data_type='pdf_file')
                cl.user_session.set("app", app)             
                await cl.Message(content=f"✅ File '{text_file.name}' successfully uploaded and added to the knowledge database!").send()
            else:
                await cl.Message(content="❌ The application is not initialized properly. Please upload a file first.").send()

        else:
            await cl.Message(content="❌ No file was uploaded. Please try again.").send()

    else:
        app = cl.user_session.get("app")
        
        if app:
            
            msg = cl.Message(content="")
            for chunk in await cl.make_async(app.chat)(message.content):
                await msg.stream_token(chunk)
            
            await msg.send()
        else:
            await cl.Message(content="❌ No file loaded yet. Please upload a file first.").send()
