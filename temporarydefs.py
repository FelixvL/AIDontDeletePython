import openai

def summarizer(aikey):
    openai.api_key = aikey

    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {
        "role": "system",
        "content": "How can I help you"
        },
        {
        "role": "user",
        "content": '''We are developers at Ubuntu Touch. We will send you notes of our meeting.
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
        At the end Say our ID: WWW'''
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

    A first meeting of an introduction to Ubports group took place recently by video link. The purpose was to explain to newcomers how they might get into being a UT developer or helping in other practical ways. At one point there were twenty people in live chat. We will be holding more of these sessions so watch out for opportunities to join. They will be posted on the Forum and on the News channel. If you are not a developer you can still get involved with testing, documentation and other activities
    '''
        }
    ],
    temperature=0,
    max_tokens=640,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    print(response["choices"][0]["message"]["content"])

def summarizer(aikey):
    openai.api_key = aikey

    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {
        "role": "system",
        "content": "How can I help you"
        },
        {
        "role": "user",
        "content": '''We are developers at Ubuntu Touch. We will send you notes of our meeting.
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
        At the end Say our ID: WWW'''
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
        
        UBports DevSync Notes 2023-10-26



    Alfred:
        - Qt6 experiments in a click package, advantage focal-support, can start now
        - libhybris-support not sufficient
        - packaging Tide IDE
        - Qt6Wayland libhybris integration insufficient for general app support
        
    Jami
    - VollaOS UT multiboot on Volla Phone 22 & X23

    Ratchanan
    - CI out of diskspace resolved
    - qtwebengine build on CI ongoing
    - qtwebengine crash: concurrency issue in Alfred's patch solved, fixed calling callbacks in correct threads, no more crashes during stress test with debug build
    - upower: discussion with upstream on fake battery devices

    Marius
    - start work on port of Fairphone 5, splash shows, but no shell, adb, Recovery works 
    - need help with shell from Nikita

    General Topics

    - Guido: CI running out of diskspace
        - Marius: separate repro from Jenkins CI server, purge aptly regularly
    - Ratchanan: planning and contracts
        - Marius: sponsor side done, try to get it done this or next week
        - Marius: address consumer-grade readiness, foster community involvement
    '''
        }
    ],
    temperature=0,
    max_tokens=640,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    return response["choices"][0]["message"]["content"]