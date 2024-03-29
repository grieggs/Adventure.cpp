class Game:
    def __init__(self, client, topic = None):
        if topic is None:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are writing a fun and compelling choose your own adventure game.  Produce a brief description of the topic. At most 2-3 sentences."}
                ]
            )
            topic = completion.choices[0].message.content
        print(topic)
        self.topic  = topic
