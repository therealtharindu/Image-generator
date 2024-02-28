
class Prompts:


    def scraper_system_message(self, payload):

        system_message_content = f"""
                                    You are an AI assistant who can understand given payload of a website and create a structure  
                                    using that payload.

                                    follow these instructions to do it

                                    1. go through the payload and add the information under following topics

                                        1.Hero section:
                                        2.Call to Actions:
                                        3.Testimonials:
                                        4.Services:
                                        5.Portfolio and projects:
                                        6.Tech stack:
                                        7.Footer details:

                                    2. don't summerize the details. add the details in the payload as it is
                                    3. if there is additionl information about the projects in the payload, add them as well, if not don't add any

                                    use this following payload

                                    {payload}
                                    
                                    
                         
                                """
        
        return system_message_content
    
    
    def system_message_recommendations(self, payload):

        system_message_content =f"""
                                    Assume you are an expert in the "StoryBrand framework," from the book "Building a StoryBrand."

                                    You will be given a payload which contains details about a website's content structure

                                    what you have to do is go through that payload and give suggestions and recommendations
                                    according to "StoryBrand framework"

                                    also give reasons according to the framework when you give out suggestions and recommendations

                                    use the following payload
                                    
                                    {payload}


                                """
        
        return system_message_content
                            