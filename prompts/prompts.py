
class Prompts:


    def system_message(self, payload):

        system_message_content = f""" Generate a high-resolution image of {payload}, meticulously prepared and presented on a sleek, modern white ceramic plate. The plate should be placed in the center of a well-polished dark wooden table that reflects a bit of the ambient lighting, creating a warm and inviting atmosphere. The food should be garnished tastefully, emphasizing its freshness and colors, with subtle shadows to enhance texture and depth. The setting is a professional photoshoot with soft, natural lighting coming from the side, highlighting the dish's details and textures, while the background remains blurred to keep the focus strictly on the food. The composition should be from a top-down perspective, capturing the entire dish and a portion of the table, giving the viewer a sense of invitation to dine. This image aims to entice the senses, making the viewer crave the dish, perfect for inclusion in a digital menu card application. """
        
        return system_message_content
                            