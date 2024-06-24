# How to run

- Create virtual enticement

  ```bash
  python3 -m venv .venv
  ```

- Activate virtual enticement

  ```bash
  source .venv/bin/activate
  ```

- Install requirements

  ```bash
  pip install -r requirements.txt
  ```

- Run fast api server in dev mode

  ```bash
  fastapi dev main.py
  ```

- [Setup ngrok](https://dashboard.ngrok.com/get-started/setup/linux)

- Run ngrok

  ```bash
  ngrok http 8000
  ```

- [Configure your webhook URL](https://www.twilio.com/console/phone-numbers/incoming)

  ![webhook-config](screenshots/webhook-config.png)

# Reference

- [Blog](https://www.aporia.com/learn/how-to-build-llm-based-phone-assistants-with-openai-twilio-aporia/)

- [TwiML™ for Programmable Voice Doc](https://www.twilio.com/docs/voice/twiml)
