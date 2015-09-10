#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json
import urllib

base_url = 'http://2015.trondheimdc.no/test-program'

def write_raw(f, raw):
    f.write(raw)

def write_line(f, line):
    indent = "        "
    write_raw(f, '%s%s\n' % (indent, line))

def write_file(f, file):
    with open(file) as i:
        for line in i.readlines():
            write_raw(f, line)

def speaker_page():
    f = open('speakers.html', 'w')

    if os.path.isfile('header.html.stub'):
        write_file(f, 'header.html.stub')
    else:
        write_raw( f, header)

    write_file(f, "speakers.css")

    speakers = programs[:]
    for s in speakers:
        short_title = ''
        for word in s['title'].split(" "):
            if len("%s %s" % (short_title, word)) > 45:
                short_title += '...'
                break
            short_title += ' ' + word

        s['short_title'] = short_title

    write_raw( f, header)
    write_line(f, '<script type="text/javascript">')
    write_line(f, '  var speakers = %s' % json.dumps(speakers))
    write_line(f, '</script>')

    write_raw( f, '\n')
    write_line(f, '<h2>Speakers 2014</h2>')
    write_raw( f, '\n')
    write_line(f, '<h5>***THIS PAGE IS JUST FOR TESTING PURPOSES. STAY TUNED FOR THE REAL PROGRAM***</h5>')
    write_raw( f, '\n')

    write_line(f, '<div id="speaker-list" class="speaker-list clearfix"></div>')

    write_file(f, "speakers.js")

    if os.path.isfile('footer.html.stub'):
        write_file(f, 'footer.html.stub')
    else:
        write_raw( f, footer)

def program_page():
    f = open('index.html', 'w')

    if os.path.isfile('header.html.stub'):
        write_file(f, 'header.html.stub')
    else:
        write_raw( f, header)

    write_file(f, "program.css")

    write_raw( f, '\n')
    write_line(f, '<h2>Program 2014</h2>')
    write_raw( f, '\n')
    write_line(f, '<h5>***THIS PAGE IS JUST FOR TESTING PURPOSES. STAY TUNED FOR THE REAL PROGRAM***</h5>')
    write_raw( f, '\n')
    write_line(f, '<table class="program-top"><tr>')
    write_line(f, '<td class="program-notification">Merk: Denne siden bruker cookies for å huske dine favoritter. Trykk på stjernen(e) for å merke dine favoritter.</td>')
    write_line(f, '<td class="expand-all"><img src="s/ic_expand_more_white_24dp_2x.png"></td>')
    write_line(f, '</tr></table>')

    for show_time in show_times:
        write_line(f, '<section class="program-time %s">' % show_time[4])
        write_line(f, '    <h4  class="program-time">%s - %s %s</h4>' % (show_time[1], show_time[2], show_time[3]))

        for room in xrange(1,6):
            for program in programs:
                id = program['id']
                if show_time[0] !=      id[0:4]: continue
                if room         != int(id[8: ]): continue

                post_url = '%s/#f%s' % (base_url, id)
                face_url = 'https://www.facebook.com/dialog/feed?%s' % urllib.urlencode({
                    'app_id':       '1170433749639697',
                    'redirect_uri': post_url,
                    'display':      'page',
                    'link':         post_url,
                    'picture':      program['image'],
                    'name':         program['title'],
                    'description':  program['abstract'],
                    'caption':      '%s #tdconf 2015' % show_time[1],
                    })


                write_raw( f, '\n')
                write_line(f, '    <div id="f%s" class="program-post">' % id)
                write_line(f, '        <table class="program-header">')
                write_line(f, '            <tr>')
                write_line(f, '                <th class="favourite">')
                write_line(f, '                    <div>Sal&nbsp;%s</div>' % room)
                write_line(f, '                    <img class="fav-icon" src="s/ic_star_border_white_24dp_1x.png">')
                write_line(f, '                </th>')
                write_line(f, '                <td class="expand">')
                write_line(f, '                    <div class="program-title">')
                write_line(f, '                        %s' % (program['title']))
                write_line(f, '                    </div>')
                write_line(f, '                    <div class="post-author">')
                write_line(f, '                        %s' % (program['author']))
                write_line(f, '                    </div>')
                write_line(f, '                </td>')
                write_line(f, '                <td class="expand expand-icon">')
                write_line(f, '                    <img class="expand-icon" src="s/ic_expand_more_white_24dp_1x.png">')
                write_line(f, '                </td>')
                write_line(f, '            </tr>')
                write_line(f, '        </table>')
                write_line(f, '        <div class="program-talk hidden">')
                write_line(f, '            <img class="program-img" src="%s">' % program['image'])
                if program['abstract'] != '':
                    write_line(f, '            %s' % ''.join(['<p>%s</p>' % i for i in program['abstract'].split('\n')]))
                else:
                    print 'No abstract for %s' % program['title']
                if program['about'] != '':
                    write_line(f, '            %s' % ''.join(['<p>%s</p>' % i for i in program['about'].split('\n')]))
                else:
                    print 'No about for %s' % program['title']
                write_line(f, '            <p class="program-footer">')
                if program['twitter'] != '':
                    write_line(f, '              <a href="https://twitter.com/intent/follow?screen_name=%s"><img class="program-social" src="s/twitter_grey.png">follow</a>  |' % program['twitter'])
                write_line(f, '              <a href="%s"><img class="program-social" src="s/facebook.png">share</a> |' % (face_url))
                write_line(f, '              <a href="%s">Sal&nbsp;%s - %s</a>' % (post_url, room, show_time[1]))
                write_line(f, '            </p>')
                write_line(f, '        </div>')
                write_line(f, '    </div>')

        write_line(f, '</section>')
        write_raw( f, '\n\n')

    write_file(f, "program.js")

    if os.path.isfile('footer.html.stub'):
        write_file(f, 'footer.html.stub')
    else:
        write_raw( f, footer)

show_times = [
        ['0800', '08:00', '09:00', 'Registrering',  'sep'],
        ['0900', '09:00', '09:10', 'Intro',         ''],
        ['0910', '09:10', '10:00', 'Keynote',       ''],
        ['1000', '10:00', '10:15', 'Pause',         'sep'],
        ['1015', '10:15', '10:45', '',               ''],
        ['1045', '10:45', '11:00', 'Pause',         'sep'],
        ['1100', '11:00', '11:30', '',               ''],
        ['1130', '11:30', '12:45', 'Lunsj',         'sep'],
        ['1245', '12:45', '13:10', '',               ''],
    ]

programs = [
        {'id': '0900_sal1', 'title': "Vel valgte ord og dagen er i gang!",                                  'author': "Selda Ekiz",                             'twitter': 'monlilli',      'image': "http://raiom.no/tdconf-test-program/img/Speaker_picture-Selda-Ekiz-400x400.jpg",                  'abstract': "",                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      'about': "Selda Ekiz er kjent fra NRKs Newton og Barn Ingen Adgang og har en mastergrad i Fysikk fra UiB. Med andre ord har hun et diplom på “nerd”. Hun elsker internett og mener at verden hadde vært et mye bedre sted om folk hadde virkelig utnyttet nettet for det den er lagd for: spre kunnskap"},
        {'id': '0910_sal1', 'title': "The better parts (EN)",                                               'author': "Douglas Crockford",                      'twitter': '',              'image': "http://raiom.no/tdconf-test-program/img/Speaker_Picture-DouglasCrockford_Feb2013-400x400.jpeg",   'abstract': "This talk is about using programming languages more effectively, and using that experience to create and select better programming languages. There are bad practices in software development that are so old and well established that it is difficult to recognize the problems they cause. There will be a review of the new good parts in ES6. JSON will also be mentioned.",                                                                                                                                   'about': "Doulas Crockford is a senior JavaScript Architect and well known for introducing and maintaining JSON format. He’s a well known presenter and author of several books. He’s a former chief architect at Yahoo and now at PayPal. <a href='http://www.crockford.com/'>Check out his homepage for more information.</a>"},
        {'id': '1015_sal1', 'title': "Challenges and opportunities in the changing digital landscape",      'author': "Stefania Montagna",                      'twitter': 's_montagna',    'image': "http://raiom.no/tdconf-test-program/img/Linkedin_Picture_StefaniaMontagna-400x400.jpg",           'abstract': "The changing digital landscapes challenges developers to think differently. Audience fragmentation, the increasing use of digital technologies beyond the screen and the high level of competition in the digital landscape offers tremendous opportunities and also relevant challenges to anyone trying to make it in this space. The talk will explore how Google is looking to support developers, both technically and from a business perspective, in their strive to develop for the world of tomorrow.",    'about': "Stefania Montagna is a Strategic Partner Manager in Google’s Online Partnership Group, focusing on the Nordics. Stefaniaspecializes in sales of revenue-generating solutions for publishers and app developers. She has previously contributed to maintaining the Google Blog “Inside AdWords” for Norway, and has organized several Google events in Norway and Sweden."},
        {'id': '1015_sal2', 'title': "Introduction to bluetooth low energy – Overview and radio (EN)(1/2)", 'author': "Carles Cufi",                            'twitter': 'carlescufi',    'image': "http://raiom.no/tdconf-test-program/img/1acd14a-2-400x400.jpg",                                   'abstract': "The presentation will focus on the basics of Bluetooth Low Energy, including a brief overview of the radio, a concise description of all layers in the protocol stack and their inner workings as well as current applications and development platforms offered by my Norwegian employer and IC design company Nordic Semiconductor.",                                                                                                                                                                             'about': "Starting at Parrot in Paris with version 1.0 of the Bluetooth specification, I wrote one of the first protocol stacks to be shipped on a commercial product, and have been involved with the development and implementation of Bluetooth devices and systems ever since. I am currently employed by Nordic Semiconductor, where I am responsible for the APIs offered by the protocol stack on the nRF51 series."},
        {'id': '1015_sal3', 'title': "Among the sleep, En drøm blir virkelig",                              'author': "Adrian Tingstad Husby",                  'twitter': 'AdrianTingHus', 'image': "http://raiom.no/tdconf-test-program/img/adrian-400x400.jpg",                                      'abstract': "Våren 2011 leverte en gjeng studenter bacheloroppgaven sin ‘Among the Sleep’. Den lille prototypen av et dataspill hadde allerede da motatt støtte for vidreutvikling, men ingen av studentene ante egentlig hva de begikk seg ut på. Etter tre år ble spillet til sist ble gitt ut 29. mai i år. Blant annet The Guardian og New York Times har siden delt sin entusiasme rundt spillet. Hvordan tok det form?",                                                                                                   'about': "Adrian er ‘potet’ og alt-mulig-mann i Krillbite Studio. Under utviklingen av Among the Sleep har han jobbet med alt fra markedsføring og spilldesign, til lyddesign og administrativt arbeid."},
        {'id': '1015_sal4', 'title': "Managing CSS projects with ITCSS (EN)",                               'author': "Harry Roberts",                          'twitter': 'csswizardry',   'image': "http://raiom.no/tdconf-test-program/img/harry-400x400.jpg",                                       'abstract': "",                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      'about': "Harry is a Consultant Front-end Architect, designer, developer, writer and speaker from the UK. Previously a Senior Developer at BSkyB, he now helps tech teams all over the world build better products. He specialises in authoring and scaling large front-ends; he writes on the subjects of maintainability, architecture, performance, OOCSS and more at csswizardry.com; he is the lead and sole developer of inuitcss, a powerful, scalable, Sass-based, BEM, OOCSS framework; he Tweets at @csswizardry."},
        {'id': '1015_sal5', 'title': "The lower cog challenge (EN)(1/2)",                                   'author': "Niall Merrigan and Glenn F. Henriksen",  'twitter': '',              'image': "http://raiom.no/tdconf-test-program/img/Niall_Glenn-400x400.jpg",                                 'abstract': "This isn’t a cage match, this is a TopGear style challenge between the old dog and the not so old dog. In this session, Niall will defend WebForms while Glenn shouts about MVC and they will show how the two fare in a set of grueling technical challenges… Expect the two presenters to trade insults while trying to show the technical superiority of their chosen stack.",                                                                                                                                   'about': "Niall is the Head of Custom Software Development in Capgemini Stavanger,He is also a Microsoft ASP.NET MVP, and general rugby nut (which means he shouts a lot). He has a passion for web technologies, security and whiskey which can lead to some interesting discussions. He can be found on twitter as @nmerrigan and hosts a blog at certsandprogs.com\nGlenn F. Henriksen har byttet kode mot mat i ca 15 år og for tiden jobber han som mentor, evangelist og utvikler hos Capgemini Stavanger. Her får han sjangsen til å utforske nye verktøy, prosesser og teknologi og å stadig forbedre måten han og hans kollegaer jobber med kode, oppgaver og prosjekter. Han er levende opptatt av kunnskapsformidling og har blitt utpekt som ASP.NET MVP av Microsoft."},
        {'id': '1100_sal1', 'title': "{{ angularjs.title }}",                                               'author': "Christian Skar",                         'twitter': 'skarchr',       'image': "http://raiom.no/tdconf-test-program/img/skarchr-400x400.jpg",                                     'abstract': "Du har kanskje hørt om AngularJS? Du tenkte kanskje også “Herregud, ikke enda et JavaScript-rammeverk”. Da er denne talken noe for deg. I løpet av 30 minutter skal vi demonstrere de egenskapene og funksjonene som gjør rammeverket så populært.",                                                                                                                                                                                                                                                                'about': "Lokal fersk systemutvikler som har oppholdt seg for det meste i .NET verden de siste to årene. Er over gjennomsnittet interessert i design, prototyping og front-end utvikling. Liker å utforske ny teknologi og fortelle kolleger om dem."},
        {'id': '1100_sal2', 'title': "Introduction to Bluetooth low energy – Protocol stack and applications (EN)(2/2)", 'author': "Carles Cufi",               'twitter': 'carlescufi',    'image': "http://raiom.no/tdconf-test-program/img/1acd14a-2-400x400.jpg",                                   'abstract': "The presentation will focus on the basics of Bluetooth Low Energy, including a brief overview of the radio, a concise description of all layers in the protocol stack and their inner workings as well as current applications and development platforms offered by my Norwegian employer and IC design company Nordic Semiconductor.",                                                                                                                                                                             'about': "Starting at Parrot in Paris with version 1.0 of the Bluetooth specification, I wrote one of the first protocol stacks to be shipped on a commercial product, and have been involved with the development and implementation of Bluetooth devices and systems ever since. I am currently employed by Nordic Semiconductor, where I am responsible for the APIs offered by the protocol stack on the nRF51 series."},
        {'id': '1100_sal3', 'title': "How HTML5 missed its graduation day (EN)",                            'author': "Christian Heilman",                      'twitter': 'codepo8',       'image': "http://raiom.no/tdconf-test-program/img/chrisheilmann-400x400.jpg",                               'abstract': "",                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      'about': "Chris Heilmann has dedicated a lot of his time making the web better. Originally coming from a radio journalism background, he built his first web site from scratch around 1997 and spent the following years working on lots of large, international web sites. He then spent a few years in Yahoo building products and explaining and training people and is now at Mozilla. Chris wrote and contributed to six books on web development and wrote many articles and hundreds of blog posts."},
        {'id': '1100_sal4', 'title': "Dysfunksjonelle utviklingsteam",                                      'author': "Sondre Bjellås",                         'twitter': 'sondreb',       'image': "http://raiom.no/tdconf-test-program/img/Sondre_small-400x400.jpg",                                'abstract': "Hva er det som skjer når man plasserer forskjellige individer i en gruppen sammen for å utvikle IT-løsninger? Har vi glemt at et team består av individer, når vi forsøker å bruke metodikk og verktøy for å få et dysfunksjonelt team til å prestere bedre? Hvordan kan man skape et bedre og mer positivt utviklingsmiljø?",                                                                                                                                                                                      'about': "Med over 16 års erfaring med systemutvikling, har jeg begynt å få en forståelse for hva som fungerer bra og dårlig med utviklingsteam. Erfaring fra mange store og små prosjekter i Norge og utlandet, jobber som konsulent i Kristiansand for Deepmind."},
        {'id': '1100_sal5', 'title': "The lower cog challenge (EN)(2/2)",                                   'author': "Niall Merrigan and Glenn F. Henriksen",  'twitter': '',              'image': "http://raiom.no/tdconf-test-program/img/Niall_Glenn-400x400.jpg",                                 'abstract': "Niall is the Head of Custom Software Development in Capgemini Stavanger,He is also a Microsoft ASP.NET MVP, and general rugby nut (which means he shouts a lot). He has a passion for web technologies, security and whiskey which can lead to some interesting discussions. He can be found on twitter as @nmerrigan and hosts a blog at <a href='http://certsandprogs.com'>certsandprogs.com</a>",                                                                                                                'about': "Glenn F. Henriksen har byttet kode mot mat i ca 15 år og for tiden jobber han som mentor, evangelist og utvikler hos Capgemini Stavanger. Her får han sjangsen til å utforske nye verktøy, prosesser og teknologi og å stadig forbedre måten han og hans kollegaer jobber med kode, oppgaver og prosjekter. Han er levende opptatt av kunnskapsformidling og har blitt utpekt som ASP.NET MVP av Microsoft."},
        {'id': '1245_sal1', 'title': "Creating adaptive experiences (EN)",                                  'author': "Avi Itzkovitch",                         'twitter': 'xgmedia',       'image': "http://raiom.no/tdconf-test-program/img/Avi-Edit-400x400.jpg",                                    'abstract': "How do we utilize sensor and user data to create experiences in the digital world? We all know that smart devices have sensors, but how can we use this as a resource to acquire information about the user and his environment? And how can we use this information to design a better user experience that is both unobtrusive and transparent? The simple answer: we create adaptive systems.",                                                                                                                  'about': "Avi (@xgmedia) is a longtime interactive and web design professional with thirteen years of experience. He is an avid enthusiast of technology and is often invited to speak about emerging design and UX trends. Avi is currently working as an Independent UI/UX Consultant at his studio, XG Media and is the Founder of UX Salon (@uxsalon), an international UX Design conference in Tel-Aviv."},
        {'id': '1245_sal2', 'title': "The magic of regular expressions",                                    'author': "Rustam Mehmandarov",                     'twitter': 'rmehmandarov',  'image': "http://raiom.no/tdconf-test-program/img/Rustam-400x400.png",                                      'abstract': "De er overalt, de er magiske og deres kunnskap kan hjelpe deg å skille deg ut fra mengden. De er også raske og kan spare deg for mye unødvendig knot. Ønsker du å forstå dem, og lære å bruke dem riktig? Har du lyst til å beseire monstre som etterlater spor [stacktraces] i loggfilene dine, eller ønsker du å kunne takle navnekonvensjoner i koden din bedre? Kanskje vil du bare bedre forstå besvergelser som har blitt skrevet av andre?\nI dette foredraget vil vi ta et dypere dykk inn i regulære uttrykk, deres bruk og ikke minst ta en titt på noen praktiske eksempler. Vi vil starte med en kort introduksjon til den mystiske verden av regulære uttrykk og friske opp våre kunnskaper om disse før vi fortsetter videre til mer avanserte emner som grupper, greed og backtracking. Interaktiv presentasjon med masse demoer.", 'about': "Rustam Mehmandarov har en mastergrad fra Institutt for Informatikk, UiO. Han har over 8 års erfaring som utvikler, teknisk prosjektleder og leveranseansvarlig i både store og små prosjekter. Han har interesse for smidig utvikling, webutvikling, arkitektur og geografiske informasjonssystemer. Han er også en guru på både Linux og Windows. På fritiden er han veldig glad i å trene, når han ikke sitter og koder i Python eller Java. Han snakker også ofte på forskjellige konferanser som JavaZone, NDC, Boosterconf og diverse faglige events på universiteter over hele Norge."},
        {'id': '1245_sal3', 'title': "Papirflytting eller integrasjon? La systemene snakke sammen!",        'author': "Anita Skylstad",                         'twitter': 'anitaskylstad', 'image': "http://raiom.no/tdconf-test-program/img/Anita10x15_ny_klippet-400x400.jpg",                       'abstract': "Jakten på det perfekte systemet ender ofte opp med noe midt i mellom. Løsninger tilpasset hvert enkelt fagområde, som dekker alle behov og gjør alle fornøyde, men ikke laget for å samarbeide. Så hva er det midt i mellom som gjør at ting allikevel ser ut til å fungere? Folk! Manuell aktivitet mellom systemer kan og BØR automatiseres. Få et innblikk i hvorfor og hvordan papirflytterne kan avløses.",                                                                                                    'about': "Anita jakter på de løsningene som gir mest tilbake til brukerne. Brukerne skal aldri føle seg motarbeidet når de bruker sine arbeidsverktøy. Hvis behovene ikke er støttet så er heller ikke systemet ferdig. Forenkling og digitalisering er hennes daglige visjon. Som programmerer og systemutvikler har Anita beveget seg fra Java til .NET og inn i en verden med C#, WCF og BizTalk."},
        {'id': '1245_sal4', 'title': "Bluetooth low energy on Android",                                     'author': "Vegar Westerlund",                       'twitter': 'vegarwe',       'image': "http://raiom.no/tdconf-test-program/img/2013-05-22_14-52-58_DSC_6319-400x400.jpg",                'abstract': "Bluetooth Low energy is one of the key technologies enabling IoT. A key difference between Bluetooth and other wireless standards is that it even defines application uses-cases (as adapted profiles). In this session we will look at the new Bluetooth Low energy API’s in Android L and learn how to use them to implement these adopted profiles as well as other gotchas with the API.",                                                                                                                      'about': "Vegar Westerlund is an embedded tester and developer working for Conceptos Consulting in Trondheim. He has developed on embedded Linux, done testing for ESA on Galileo (satellite navigation system) and is currently working for Nordic Semiconductor with Bluetooth low energy on their ARM based nRF51 series. He is also active in the Meetup community here in Trondheim and an organiser for XP meetup."},
        {'id': '1245_sal5', 'title': "Hvordan jobbe bedre som team i smidig utvikling?",                    'author': "Torgeir Dingsøyr",                       'twitter': '',              'image': "http://raiom.no/tdconf-test-program/img/torgeir_dingsoyr_1200px-400x400.jpg",                     'abstract': "Smidige metoder har ført til at systemutvikling gjennomføres i små, selvstyrte team. Vi finner mange råd om hvordan arbeidet bør gjennomføres i smidige metoder, men hvordan rimer disse rådene med forskning på teamarbeid fra andre felt? I dette foredraget vil jeg vise en modell for teameffektivitet, hvilke faktorer scrum setter fokus på, og hva et team bør jobbe med i tillegg.",                                                                                                                        'about': "Torgeir arbeider med prosessforbedring og kunnskapsforvaltning i programvarebedrifter som seniorforsker i SINTEF. Spesielt har han fokusert på smidige utviklingsmetoder, teamarbeid i systemutvikling og bruk av intranettverktøy for læring mellom prosjekter. Han er medforfatter på boka “Praktisk prosessforbedring – en håndbok for IT-bedrifter” på Fagbokforlaget."},
]

header = """
<!doctype html>

<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Test program</title>

        <script src="http://yui.yahooapis.com/3.18.1/build/yui/yui-min.js"></script>

        <style>
            /* Debugging
            */
            .hidden    { display: none; }

            html {
                background-color: #01131C;
                color: #eee;
            }
            a {
                color: #00ff80;
            }

            /*
            .favourite { border: 1px solid green; }
            .expand    { border: 1px solid red; }
            .show      { border: 1px solid yellow; }
            */
        </style>

    </head>

    <body>
"""
footer = """
    </body>
</html>
"""

if __name__ == "__main__":
    program_page()
    speaker_page()
