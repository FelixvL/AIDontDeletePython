from openai import OpenAI

def summarizer(aikey, inputtext):
    print("in functie summarizer")
    client = OpenAI(api_key=aikey)
    invoer = inputtext
    messagesfirst = [
        {
        "role": "system",
        "content": "How can I help you"
        },
        {
        "role": "user",
        "content": '''
        I want you to answer me in HTML format only.
        End your response with YYY
        No intro no outro. I will use your response immediately in my DOM, with innerHTML.
        '''
        },
        {
        "role": "user",
        "content": '''
        We are developers at Ubuntu Touch. We will send you notes of our meeting.
        During the meeting they answered the follwing questions:
        What you have been working on? What can be unblocked for you?

        Could you write a long read blog post, which provides information per topic which we mention, 
        explain what there is to tell about the mentioned subjects'''
        },
        {
        "role": "system",
        "content": "ok"
        },
        {
        "role": "user",
        "content": '''
        Mention each member as a separate title.
        Make only factual statements, dont make things up.
        The audience is quite technical.
        Therefor we like you to explain the technical terms quite comprehensive.
        '''
        },
        {
        "role": "system",
        "content": "ok, could you give me an example of the style which you like me to write in"
        },
        {
        "role": "user",
        "content": '''
        This is an example of style of writing which we like.
        Of course you should not use this in our blog post.
        Volla Phone are one of our long time sponsors and they are offering a chance to win a Volla 22. In addition they are donating €10 to Ubports for every phone sold with UT pre-installed.
        A first meeting of an introduction to Ubports group took place recently by video link. The purpose was to explain to newcomers how they might get into being a UT developer or helping in other practical ways. At one point there were twenty people in live chat. We will be holding more of these sessions so watch out for opportunities to join. They will be posted on the Forum and on the News channel. If you are not a developer you can still get involved with testing, documentation and other activities.
        A build of UT has been merged, for Pinephones and PineTab 2.
        A memory fault in VideoRecorder has been fixed. This will put an end to some crashes while watching video. Rachanan had to dig deep into libhybris to figure out what was going wrong. Alfred fixed a bug related to video decoding in the browser so that has also contributed to stability. The next OTA should contain a lot of browser improvements, including hardware optimisation. 4K videos will now work nicely on more powerful devices.'''
        },
        {
        "role": "system",
        "content": '''Thanks for the example, please give me your notes now about which i can write the blog'''
        },
        {
        "role": "user",
        "content": '''These are the notes you should only write about: 
        '''+inputtext+'''

    '''
        }
    ]
    print(messagesfirst)
    response = client.chat.completions.create(
    model="gpt-4",
    messages=messagesfirst,
    temperature=0.7,
    max_tokens=2096,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )

    return response.choices[0].message.content 


def summarizer_per_persoon(aikey, inputtext):
    algemeen_en_personen_los = inputtext.split("@@@")
    lijst_personen = algemeen_en_personen_los[1].split("|||")
    antwoord_text = ""
    for persoon in lijst_personen:
        antwoord_text += call_naar_chatGPT(aikey, persoon) + "<hr><hr>"
        print("========")
        print(antwoord_text)
        
    return antwoord_text

def call_naar_chatGPT(aikey, inputtext):
    client = OpenAI(api_key=aikey)
    messagesfirst = [
        {
        "role": "user",
        "content": '''
            I want you to answer me in HTML format only.
            No intro no outro. I will use your response immediately in my DOM, with innerHTML.
        '''
        },{
        "role": "user",
        "content": '''
        We are developers at Ubuntu Touch. We will send you notes of our meeting.
        During the meeting they answered the follwing questions:
        What you have been working on? What can be unblocked for you?

        Could you write a long read blog post, which provides information per topic which we mention, 
        explain what there is to tell about the mentioned subjects'''
        },
        {
        "role": "system",
        "content": "ok, could you give me an example of the style which you like me to write in"
        },
        {
        "role": "user",
        "content": '''
        We gave this as input:
Muhammad
	* Work on VoLTE, get plugins working
	* systemd units from within apps
		* Ratchanan: maybe implement background task as account-polld plugin?
	* work on fixing screen rotation and geometry being wrong in landscape orientation (mouse pointer clicks don't arrive where you click, but elsewhere)
	* Transition to apparmor v4 for 24.4.x?        
    
    This was supperb output:
    Muhammad
Muhammad has been heavily investing his time and efforts into working on Voice over Long-Term Evolution (VoLTE). His prime focus is on getting the plugins operational to ensure smooth and efficient communication over the LTE network.

Moreover, he is delving into systemd units from within applications. This particular task has opened up a discussion with Ratchanan, who suggested that perhaps the background task could be implemented as an account-polld plugin. This approach could potentially enhance the efficiency and performance of the background tasks running within the applications.

Muhammad is also actively working on rectifying the issues related to screen rotation and geometry in landscape orientation. Currently, there seems to be a problem where mouse pointer clicks do not register at the clicked location but elsewhere. This is a significant issue that impacts the user experience, and Muhammad is committed to resolving it.

Finally, Muhammad is considering transitioning to AppArmor v4 for 24.4.x. AppArmor is a crucial Linux kernel security module that helps to protect the system by enforcing security policies. A transition to version 4 could potentially bring about improved security measures and optimisations.
   ''' 
    },
        {
        "role": "system",
        "content": '''Thanks for the example, please give me your notes now about which i can write the blog'''
        },{
        "role": "user",
        "content": '''
        Make only factual statements, dont make things up.
        The audience is quite technical.
        Therefor we like you to explain the technical terms quite comprehensive.
        These are the notes you should only write about for this person:
         
        '''+inputtext+'''

        '''
        }


    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messagesfirst,
        temperature=0.7,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return response.choices[0].message.content 


