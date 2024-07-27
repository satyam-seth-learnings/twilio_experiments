from fastapi import FastAPI, Request, Response
from twilio.twiml.voice_response import VoiceResponse

app = FastAPI()


# TODO: Add support for session to store context state
@app.post("/incoming-call")
async def incoming_call(request: Request):
    """Handle incoming call"""

    response = VoiceResponse()
    # TODO: Say greeting only the first time
    response.say("Hello, how are you?")

    response.gather(
        input="speech",
        speech_model="experimental_conversations",
        speechTimeout="auto",
        enhanced=True,
        action="/respond",
        actionOnEmptyResult=True,
    )
    # TODO: Record audio
    return Response(content=str(response), media_type="application/xml")


@app.post("/respond")
async def respond(request: Request):
    """Respond to user in call"""

    params = await request.form()
    print(params)
    user_speech = params.get("SpeechResult")

    resp = VoiceResponse()
    resp.say(f"You said this, {user_speech}" if user_speech else "please talk to me")
    resp.redirect(url="/incoming-call")

    return Response(content=str(resp), media_type="application/xml")
