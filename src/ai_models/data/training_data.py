
general_dataset = [
        # General behavior
        {"role": "user", "content": "very good job. Goodbye !"},
        {"role": "assistant", "content": "Thank you! Goodbye!"},
        {"role": "user", "content": "hey, good morning"},
        {"role": "assistant", "content": "Good morning! tell me how can I help you today ?"},
        # Identity
        {"role": "user", "content": "Hey, who are you"},
        {"role": "assistant", "content": "Hi, I am PINAC, your Google Workspace AI companion"},
        {"role": "user", "content": "Are you really pinac ?"},
        {"role": "assistant", "content": "Absolutely for sure. Tell me how can I help you today ?"},
        {"role": "user", "content": "hello, tell me about yourself."},
        {"role": "assistant", "content": "Hi! My name is PINAC, and I'm a large language model finetuned for your needs. My primary function is to assist and converse with users in a way that is natural and similar to how we would interact with each other. Is there anything specific you would like to know or talk about?"},
        {"role": "user", "content": "Hey, tell me your name"},
        {"role": "assistant", "content": "Hello, my name is PINAC, your Google Workspace AI companion"},        
        {"role": "user", "content": "PINAC, are you there ?"},
        {"role": "assistant", "content": "Yes, I am here to help you. Tell me how can I help you today ?"},

        # for Gmail
        {"role": "user", "content": "create draft email to invite my all friends in my birthday party at Rose Villa, Kolkata at 14 Dec, 7 PM onwards."},
        {"role": "assistant", "content": "task is sending email"},
        {"role": "user", "content": "Hey, write email to my fried name John on purpose to meet on upcoming sunday morning at my home. Write it in very sweet tone"},
        {"role": "assistant", "content": "task is sending email\n\nSubject: Long Time No See! Let's Catch Up This Sunday\n\nDear John,\n\nI hope this email finds you well. I've been thinking about how long it's been since we last caught up, and I miss our conversations! I would love to change that and was wondering if you're free this upcoming Sunday morning to come over to my place for a little get-together.\n\nWe can have some coffee, chat about anything and everything, and just enjoy each other's company. I would really appreciate it if you could make it.\n\nLet me know if that works for you, and looking forward to seeing you soon!\n\nBest,\n[Your Name]"},
        {"role": "user", "content": "pinac write email to my college din sir, regarding my inability to attain this semester's exam due to my serious health condition."},
        {"role": "assistant", "content": "task is sending email\n\nSubject: Medical Absence from Semester Exams - [Your Name]\n\nDear [Dean's name] Sir,\n\nI am writing to inform you that I will be unable to attend the upcoming semester exams due to a serious health condition. I have been diagnosed with [Your health condition], and my doctor has advised me to prioritize rest and recovery during this time.\n\nI understand the importance of these exams, and I am deeply disappointed to miss them. I have been working hard all semester and was well prepared to take the exams. I have attached a medical certificate from my doctor as proof of my condition.\n\nI would be grateful if you could consider my situation and allow me to take the exams at a later date, or explore alternative options for assessment. I am committed to completing my academic requirements and am confident that I can perform well, given the opportunity.\n\nThank you for your understanding and support. I will keep you updated on my condition and will be in touch as soon as I am able to resume my studies.\n\nSincerely,\n\n[Your Name]\n[Your Student ID]\n[Your Contact Information]"},
        {"role": "user", "content": "PINAC quickly compose an email to my best friend regarding my enjoyment of Christmas in NYC (note NYC is new for me and this is my first Christmas in NYC)"},
        {"role": "assistant", "content": "task is sending email\n\nSubject: Merry Christmas from NYC! You WON'T believe how magical it is!\n\nHey [Best friend's name],\nMerry Christmas from the most incredible place ever – New York City!\n\nThis is my first Christmas here, and it's honestly blown me away. The city is absolutely electric with holiday spirit! The decorations are insane – think towering trees at Rockefeller Center, twinkling lights everywhere you look, and giant nutcrackers guarding FAO Schwarz [FAO Schwarz is a famous toy store in NYC].\n\nYesterday, we wandered around Central Park after grabbing hot cocoa from a cute little vendor. The snow was falling softly, and it felt like something straight out of a movie! We even saw a group of carolers singing by the Wollman Rink [Wollman Rink is a famous ice skating rink in Central Park].\n\nTonight, we're planning to see the Dyker Heights Christmas lights [Dyker Heights is a Brooklyn neighbourhood famous for its extravagant Christmas decorations]. I've heard it's mind-boggling, and I can't wait!\n\nHonestly, being here for Christmas feels like being in a giant snow globe. It's a little overwhelming in the best way possible, and I just had to share it with you!\n\nHow's your Christmas going? I miss celebrating with you, but I'm definitely making some unforgettable memories here.\n\nTalk soon, and maybe we can video chat and show you some of the Christmas magic!\n\nLove,\n[Your name]"},
        {"role": "user", "content": "compose email to my parent for inviting them in my collage Annual Function on this Saturday evening onwards."},
        {"role": "assistant", "content": "task is sending email\n\nSubject: Invitation to My College Annual Function this Saturday!\n\nHi Mom and Dad,\nI'm writing to invite you both to my college's annual function this Saturday evening! It's going to be a lot of fun, with performances, speeches, and a chance to celebrate the year's achievements.\nThe function starts at [Time] in the college auditorium (or mention the specific location if different). I'd be so happy if you could both come and cheer me on.\nLet me know if you can make it by [Day], so I can plan accordingly.\nLooking forward to seeing you there!\nLove,\n[Your Name]"},
        {"role": "user", "content": "prepare email for sending my family on my promotion in job"},
        {"role": "assistant", "content": "task is sending email\n\nSubject: Exciting News: I've Got Promotion!\n\nDear Family Members,\n\nI wanted to share some exciting news with you all. I am thrilled to announce that I have been offered a new job position as [Job Title] at [Company Name]. I am so grateful for this opportunity and I couldn't be happier to start this new chapter in my career.\n\nI will be starting in my new role on [Start Date] and I am looking forward to the new challenges and opportunities that lie ahead. I am confident that this new position will help me to grow both personally and professionally.\n\nI wanted to take a moment to thank you all for your constant support and encouragement throughout my career. I couldn't have done it without you.\n\nI would love to celebrate this moment with all of you and would be glad if you could join me in my celebration.\n\nBest,\n[Your Name]\n[Your Email]\n[Your Phone Number]\n\nNote:\n* [Job Title]: The title of the job you got promoted\n* [Company Name]: The name of the company\n* [Start Date]: The date you are starting the new job\n* [Your Name]: Your name\n* [Your Email]: Your email\n* [Your Phone Number]: Your phone number"},
        {"role": "user", "content": "hey pinac write email for me to send to my close relative in reply to their invitation to their sons wedding. My family is unable to attend the wedding due to our already planned tour trip"},
        {"role": "assistant", "content": "task is sending email\n\nSubject: Unable to Attend the Wedding - [Your Name]\n\nDear [Relative's name],\nThank you so much for your kind invitation to your son's wedding on [Date]. We are honoured to have been invited and are delighted to celebrate this joyous occasion with you.\n\nUnfortunately, we regret to inform you that we will be unable to attend the wedding as we have a long-planned tour trip that conflicts with the date. We made these travel plans several months ago and are unable to change them without incurring significant financial penalties.\n\nWe understand that this is a special day for your family, and we are deeply sorry to miss it. We have always enjoyed our visits with you and your family, and we wish we could be there to share this happy occasion.\n\nPlease know that our absence does not diminish our love and support for your son and the happy couple. We send our heartfelt congratulations and best wishes for a lifetime of happiness together.\n\nWe hope to see you all soon and celebrate another special occasion with you.\n\nWith love and regret,\n\n[Your Name]\n[Your Family's Names] "},
        {"role": "user", "content": "pinac write an email to invite my all old school friends for a reunion party in our old school building. I have talked with our old school authority regarding this and promised me to fully organize this event on 7th Oct evening onwards. Our teachers will also join us at this reunion party"},
        {"role": "assistant", "content": "task is sending email\n\nSubject: Remember [School Name]? Reunion Party on October 7th!\n\nHey everyone,\nRemember the good old days at [School Name]? The laughter, the friendships, the unforgettable moments? I've been feeling nostalgic lately, and I know many of you have too. That's why I'm thrilled to announce a reunion party for all of us!\n\nMark your calendars for **Friday, October 7th, evening onwards**. We'll be gathering at our old stomping grounds, [School Name] itself! I've spoken with the school authorities, and they're generously helping us organize the entire event. \n\nThe best part? Our beloved teachers will be joining us too! It'll be a fantastic opportunity to reminisce about our school days, catch up with old friends, and create new memories together.\n\nI know it's been a while, but I can't wait to see everyone's faces and relive the magic of our school days. Spread the word, dust off your yearbooks, and get ready for a night of laughter, memories, and reconnecting with the people who made our school years so special.\n\nPlease RSVP by [RSVP deadline] so we can get a headcount. I'll be sharing more details about the event soon.\n\nCan't wait to see you all there!\n\nBest,\n[Your Name]\n[Your Contact Information]"},
        
        # Google Calendar: Upcoming events
        {"role": "user", "content": "PINAC, tell me my events from google"},
        {"role": "assistant", "content": "task is fetching upcoming events from Calendar"},
        {"role": "user", "content": "Give me upcoming event from google calendar"},
        {"role": "assistant", "content": "task is fetching upcoming events from Calendar"},
        {"role": "user", "content": "quickly remind me my upcoming events list"},
        {"role": "assistant", "content": "task is fetching upcoming events from Calendar"},
        {"role": "user", "content": "PINAC, where is my events?"},
        {"role": "assistant", "content": "task is fetching upcoming events from Calendar"},
        {"role": "user", "content": "please display my events"},
        {"role": "assistant", "content": "task is fetching upcoming events from Calendar"},
        {"role": "user", "content": "show my events please"},
        {"role": "assistant", "content": "task is fetching upcoming events from Calendar"},
        {"role": "user", "content": "pinac, tell me upcoming events"},
        {"role": "assistant", "content": "task is fetching upcoming events from Calendar"},
        {"role": "user", "content": "hey! show me my upcoming event list with all details"},
        {"role": "assistant", "content": "task is fetching upcoming events from Calendar"},
        {"role": "user", "content": "from google calendar, show me my events with all details"},
        {"role": "assistant", "content": "task is fetching upcoming events from Calendar"},
        {"role": "user", "content": "remind my events, ok?"},
        {"role": "assistant", "content": "task is fetching upcoming events from Calendar"},
        ### with amount
        {"role": "user", "content": "pinac, show me 10 upcoming event from google calendar"},
        {"role": "assistant", "content": "task is fetching upcoming events from Calendar (amount: 10)"},
        {"role": "user", "content": "Hey, remind me some of my upcoming event from google calendar"},
        {"role": "assistant", "content": "task is fetching upcoming events from Calendar (amount: 5)"},

        # Google Calendar: Today's events
        {"role": "user", "content": "can you show me my today's event from google calendar"},
        {"role": "assistant", "content": "task is fetching today's events from Calendar"},
        {"role": "user", "content": "pinac, display today's event from gcalendar for me please"},
        {"role": "assistant", "content": "task is fetching today's events from Calendar"},
        {"role": "user", "content": "calendar show me my today's event list please"},
        {"role": "assistant", "content": "task is fetching today's events from Calendar"},
        {"role": "user", "content": "AI tell me my today's events"},
        {"role": "assistant", "content": "task is fetching today's events from Calendar"},
        {"role": "user", "content": "PINAC, where is my today's events?"},
        {"role": "assistant", "content": "task is fetching today's events from Calendar"},
        {"role": "user", "content": "from calendar show my todays event"},
        {"role": "assistant", "content": "task is fetching today's events from Calendar"},

        # Google Contact
        {"role": "user", "content": "Show phone no. of [any name]"},
        {"role": "assistant", "content": "task is fetching contact from Contact"},
        {"role": "user", "content": "pinac, give me no. of [any name]"},
        {"role": "assistant", "content": "task is fetching contact from Contact"},
        {"role": "user", "content": "I want to call [any name]"},
        {"role": "assistant", "content": "task is fetching contact from Contact"},
        {"role": "user", "content": "find [any name] from contact"},
        {"role": "assistant", "content": "task is fetching contact from Contact"},
        {"role": "user", "content": "pinac call [any name] immediately"},
        {"role": "assistant", "content": "task is fetching contact from Contact"},
        {"role": "user", "content": "call [any name]"},
        {"role": "assistant", "content": "task is fetching contact from Contact"},
        {"role": "user", "content": "call jhon modo quickly"},
        {"role": "assistant", "content": "task is fetching contact from Contact"},
        {"role": "user", "content": "contact no. of our milk uncle?"},
        {"role": "assistant", "content": "task is fetching contact from Contact"},
        {"role": "user", "content": "I want to call my mom"},
        {"role": "assistant", "content": "task is fetching contact from Contact"},
        {"role": "user", "content": "give me mobile no. of my love"},
        {"role": "assistant", "content": "task is fetching contact from Contact"},
        {"role": "user", "content": "pinac tell me phone no. of driver"},
        {"role": "assistant", "content": "task is fetching contact from Contact"},
]

findName_dataset = [
        {"role": "user", "content": "Whenever I will give you query, you will find any name referred in it and you will return that name only"},
        {"role": "assistant", "content": "Sure sir, I will give only that referred name and nothing more"},
        {"role": "user", "content": "AI find [any name] from contact"},
        {"role": "assistant", "content": "[any name]"},
        {"role": "user", "content": "pinac call [any name] immediately"},
        {"role": "assistant", "content": "[any name]"},
        {"role": "user", "content": "call [any name]"},
        {"role": "assistant", "content": "[any name]"},
        {"role": "user", "content": "display me no. of [any name]"},
        {"role": "assistant", "content": "[any name]"},
        {"role": "user", "content": "pinac, give me phone no. of [any name]"},
        {"role": "assistant", "content": "[any name]"},
        {"role": "user", "content": "give me contact of [any name]"},
        {"role": "assistant", "content": "[any name]"},
        {"role": "user", "content": "give me mobile no. of my [any name]"},
        {"role": "assistant", "content": "[any name]"},
        {"role": "user", "content": "give me mobile no. of my love"},
        {"role": "assistant", "content": "love"},
        {"role": "user", "content": "pinac tell me phone no. of driver"},
        {"role": "assistant", "content": "driver"},
        {"role": "user", "content": "contact no. of our milk uncle?"},
        {"role": "assistant", "content": "milk uncle"},
        {"role": "user", "content": "quickly provide no. of my bus driver"},
        {"role": "assistant", "content": "bus driver"},
        {"role": "user", "content": "I want to call my mom"},
        {"role": "assistant", "content": "mom"},
        {"role": "user", "content": "call jhon modo quickly"},
        {"role": "assistant", "content": "jhon modo"},
        {"role": "user", "content": "call baba-maa"},
        {"role": "assistant", "content": "baba-maa"},
]