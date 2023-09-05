import openai

def TranscriptGenerator(text):
    openai.api_key = '----your--openai--api--key----'
    # calling chatgpt openai
    response = openai.Completion.create(

    engine="text-davinci-003",
    # prompt to convert the text into a conversation between sales person and user.
    prompt=f""" {text}

    This is a conversation between a Sales person working at Crio talking to a user. Divide and provide the transcript of hte conversation. 

    Make the output of the transcription this way -  

    Sales person: 
    User:
    Sales person:
    User:

    in this way. """,
    max_tokens=100,
        temperature=0.6
    )

    transcript = response.choices[0].text.strip()

    # sample transcript
    # transcript = """Me: Hello, Good morning, am I speaking to Rohan? User: Yes. Me: Hey Rohan, this is Vishwajeet here from Crio. How's your day going so far? User: It's good, thanks. How can I help you? Me: That's great to hear, Rohan. I noticed that you've shown some interest in our Crio learning programs. I'd love to get to know you a bit better and understand your goals and aspirations in the tech industry. Could you tell me a bit about your background and what you're looking to achieve? User: Sure, Vishwajeet. I currently work as a Manual Tester, but I've been thinking about making a switch to a career as a Full-Stack Developer. I want to upskill myself and land a job in a top tech company. Me: That's fantastic to hear, Rohan. Making that kind of transition can be both challenging and rewarding. Crio's programs are specifically designed to help professionals like you gain the skills and experience needed to excel in the tech industry. Have you had a chance to explore our platform or take advantage of our free demo trial? User: Not yet, I've been considering it. But I'm also concerned about the time commitment and whether it's worth it. Me: I completely understand your concerns, Rohan. It's important to make informed decisions. Our "Learn By Doing" approach is all about hands-on, practical learning that is optimized for real-world industry challenges. To address your specific needs, I'd like to ask, what are your biggest goals when it comes to transitioning to a Full-Stack Developer role? Is it about acquiring specific skills, building a portfolio, or securing a job with a higher CTC? User: Well, all of those are important to me, but I'm most concerned about getting a better CTC after completing the course. Me: That's a very reasonable goal, Rohan. Many of our alumni have successfully made significant career advancements and enjoyed increased earnings after completing our programs. We offer dedicated career support and coaching to help you achieve that. But before we go any further, let's ensure that our courses align with your expectations and career goals. Can you share with me your current skill level and any prior experience in tech, so we can explore which of our tracks—Full-Stack, Backend, or QA Automation—might be the best fit for you? User: I have some programming knowledge, mainly in Python, and I've done some basic web development. I'm looking for a comprehensive program that covers both frontend and backend development. Me: Thanks for sharing that, Rohan. It sounds like our Fellowship Full-Stack Program could be an excellent fit for you. It covers both frontend and backend development and will help you build a professional portfolio. Additionally, we provide 1:1 career coaching sessions and mock interviews to enhance your chances of securing a higher-paying job. Would you like to know more about the specific courses, program structure, or any other details? User: Yes, I'd like more information about the program structure and the learning experience. Me: Absolutely, Rohan. I'd be happy to walk you through the program details and explain how our "work-like" Micro-Experiences can make a significant difference in your learning journey. Also, if you have any questions or concerns at any point, please don't hesitate to ask. We're here to provide you with all the information you need to make an informed decision. User: Thanks, Vishwajeet. I appreciate your willingness to help. I'm really interested in the Fellowship Full-Stack Program. Can you tell me more about the program structure and how it works? Me: Of course, Rohan. The Fellowship Full-Stack Program is a comprehensive 9-month course that provides you with a deep understanding of both frontend and backend development. You'll work on real-world projects curated from the industry, gaining hands-on experience that is crucial for landing a job as a Full-Stack Developer. The program is divided into modules that cover various technologies, and you'll have access to a supportive community, mentors, and technical teams to assist you throughout your learning journey. We believe in the "Learn By Doing" approach, so you'll be actively working on projects, solving problems, and building a GitHub portfolio that will impress recruiters. As a working professional with 2 years of experience, your case is quite common among our students. Many of them have successfully transitioned into higher-paying roles after completing our programs. We offer 1:1 career coaching sessions, live mock interviews with industry experts, and guidance to help you update your LinkedIn, GitHub, and resume to make a strong impression on potential employers. Moreover, our team is dedicated to helping you during the placement phase to ensure you secure a job with a higher CTC. Does this program structure align with your career goals, Rohan? User: It sounds promising, Vishwajeet. But I'm concerned about the time commitment. I have a full-time job, and I need to manage my work-life balance. Me: I completely understand your concern, Rohan. Balancing work and learning can be challenging, but our program is designed with working professionals in mind. You'll have the flexibility to learn at your own pace, and our course materials are accessible 24/7, allowing you to fit your studies around your job. Additionally, our mentors and support teams are available to help you with any questions or challenges you encounter along the way. We're committed to ensuring that you have a positive learning experience without compromising your work-life balance. Could you share more about your daily schedule and any specific time constraints you might have? This will help us better understand how to tailor the program to your needs. User: Well, my work hours are typically from 9 AM to 6 PM, and I often have some additional tasks to complete in the evening. I'm concerned about finding time for the coursework. Me: Thank you for sharing your schedule, Rohan. It's important to have a clear picture of your commitments. With your work hours, you should still be able to make progress in the program, especially since you can access the materials at your convenience. To help you manage your time effectively, we also provide guidance on setting up a study routine and managing your workload. Many of our students have successfully balanced their full-time jobs and the program by dedicating a few focused hours each day to learning. If you'd like, I can connect you with one of our mentors who can offer advice on time management and share their experiences as working professionals who've completed the program. Would that be helpful to you, Rohan? User: Yes, that would be great, Vishwajeet. I'd appreciate some guidance on how to juggle my job and the coursework effectively. Me: Wonderful, Rohan. I'll arrange for one of our mentors to reach out to you soon to discuss time management strategies and provide further insights. They'll be a valuable resource as you embark on this learning journey. In the meantime, is there anything else you'd like to know or any specific questions or concerns you have about the Fellowship Full-Stack Program or the overall learning experience at Crio? User: Not at the moment, Vishwajeet. You've been very informative and helpful. I'll await the mentor's call and do some more research on my end. Thank you for your time and assistance. Me: You're very welcome, Rohan. I'm glad I could assist you today. Don't hesitate to reach out if you have any more questions in the future, and best of luck with your decision-making process. Have a great day!"""
    return transcript
