# References

- [Twilio Blog Link](https://www.twilio.com/en-us/blog/integrate-openai-chatgpt-twilio-programmable-voice-functions)

- [Twilio Serverless](https://www.twilio.com/docs/serverless)

- [Twilio Voice Twiml Say Text Speech](https://www.twilio.com/docs/voice/twiml/say/text-speech)

- [Twilio Voice Twiml Gether Input](https://www.twilio.com/docs/voice/twiml/gather#input)

- [Twilio Serverless Function Console](https://console.twilio.com/us1/develop/functions)

- [AWS Polly](https://aws.amazon.com/polly/)

- [SSML](https://cloud.google.com/text-to-speech/docs/ssml)

# Steps

- [Get Twilio Account SID and Auth Token](https://console.twilio.com/)

- [Get Open API Key](https://platform.openai.com/api-keys)

- Install [Twilio Cli](https://www.twilio.com/docs/twilio-cli/getting-started/install)

- Install [Twilio Serverless Toolkit](https://www.twilio.com/docs/labs/serverless-toolkit)

- Creating a new Serverless project

    ```sh
    twilio serverless:init <project-name>
    ```

- Install [openai](https://www.npmjs.com/package/openai) package

- Deploy Twilio Serverless function

    ```sh
    twilio serverless:deploy
    ```

- List all numbers

    ```sh
    twilio phone-numbers:list
    ```

- Assign number to serverless function

    ```sh
    twilio phone-numbers:update <PN SID> –voice-url=<The URL for the /transcribe Function>
    ```