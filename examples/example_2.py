from src.notion_webhook.server import Server, Handler, WebhookHandler
from src.notion_webhook.db import TokenDatabase

import os

db = TokenDatabase(os.getenv("DB_PATH", "tokens.db"))
if db.check_first_run():
    token_id, token = db.create_token()
    print(token)

webhook_handler = Handler(WebhookHandler(db).webhook_handler)

server = Server(
    addr=os.getenv("HOST", "0.0.0.0"),
    port=int(os.getenv("PORT", 8000)),
    handlers={"/webhook": webhook_handler}, 
    app_name=os.getenv("APP_NAME", "NotionWebhookServer")
)

server.start()