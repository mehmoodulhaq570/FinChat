import chainlit as cl
from embedchain import Pipeline as App

# This will handle the start of the chat and file upload
@cl.on_chat_start
async def on_chat_start():
    app = App.from_config(config_path="config.yml")

    # Send an initial welcome message
    await cl.Message(content="Welcome to FinChat! You can upload a PDF file of an Earnings Report (max 10 MB) for analysis.").send()

    # Ask user to upload a file (PDF)
    files = await cl.AskFileMessage(
        content="Please upload an Earnings Report (PDF file) to get started!",
        accept=["application/pdf"],
        max_size_mb="10",
        max_files=1
    ).send()

    # Check if the file is uploaded and process it
    if files:
        text_file = files[0]

        # Notify the user about the upload status
        progress_msg = await cl.Message(content=f"⏳ Uploading {text_file.name}... Please wait.").send()

        # Add the file to the app's knowledge database
        app.add(text_file.path, data_type='pdf_file')
        cl.user_session.set("app", app)

        # Once the upload is complete, notify the user
        await cl.Message(content=f"""
            ✅ **File '{text_file.name}'** successfully uploaded and added to the knowledge database!

            You can upload another file by typing **'upload the next file'** when you're ready.
            """).send()

    else:
        # Handle if no file was uploaded
        await cl.Message(content="❌ No file was uploaded. Please try again.").send()

# This will handle the reception of a new message and only upload the next file if the user asks
@cl.on_message
async def on_message(message: cl.Message):
    if "upload the next file" in message.content.lower():
        # Ask user to upload the next file (PDF)
        files = await cl.AskFileMessage(
            content="Please upload the next Earnings Report (PDF file).",
            accept=["application/pdf"],
            max_size_mb="10",
            max_files=1
        ).send()

        if files:
            text_file = files[0]

            # Notify the user about the upload status
            progress_msg = await cl.Message(content=f"⏳ Uploading {text_file.name}... Please wait.").send()

            # Add the file to the app's knowledge database
            app = cl.user_session.get("app")
            app.add(text_file.path, data_type='pdf_file')
            cl.user_session.set("app", app)

            # Once the upload is complete, notify the user
            await cl.Message(content=f"✅ File '{text_file.name}' successfully uploaded and added to the knowledge database!").send()

            # Display the PDF to the user
            elements = [
                cl.Pdf(name="pdf", display="inline", path=text_file.path, page=1)
            ]
            await cl.Message(content="Your PDF file:", elements=elements).send()

            # Inform the user that they can upload another file
            await cl.Message(content="You can upload another file by typing 'upload the next file' when you're ready.").send()

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
