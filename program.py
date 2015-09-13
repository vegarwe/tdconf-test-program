#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import csv
import sys
import json
import urllib

base_url = 'http://2015.trondheimdc.no/program'

def read_input(input_file):
    input = []
    with open(input_file, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            if row[0] == 'Vurdering': continue
            if row[2] == '': continue
            input.append({
                'id': row[2],
                'title': row[8],
                'author': row[5],
                'twitter': row[18],
                'image': row[12],
                'abstract': row[9],
                'about': row[10]
            })
    #print repr(input)

    return input

def write_raw(f, raw):
    f.write(raw)

def write_line(f, line):
    indent = "        "
    write_raw(f, '%s%s\n' % (indent, line))

def write_file(f, file):
    with open(file) as i:
        for line in i.readlines():
            write_raw(f, line)

def speaker_page(programs):
    f = open('speakers.html', 'w')

    if os.path.isfile('header.html.stub'):
        write_file(f, 'header.html.stub')
    else:
        write_raw( f, header)
    write_line(f, '        <!-- Copy from here...... -->')

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
        s['link'] = '%s/#f%s' % (base_url, s['id'])
        print s['image']
        if s['image'] != '':
            img = '.'.join(s['image'].split('/')[-1].split(".")[:-1])
            s['image'] = "http://static.trondheimdc.no/uploads/2015/cropped/" + img + "_cropped.jpg"

    write_line(f, '<script type="text/javascript">')
    write_line(f, '  var speakers = %s' % json.dumps(speakers))
    write_line(f, '</script>')

    write_raw( f, '\n')
    write_line(f, '<h2>Speakers 2015</h2>')
    write_raw( f, '\n')

    write_line(f, '<div id="speaker-list" class="speaker-list clearfix"></div>')

    write_file(f, "speakers.js")

    write_line(f, '        <!-- To here.............. -->')
    if os.path.isfile('footer.html.stub'):
        write_file(f, 'footer.html.stub')
    else:
        write_raw( f, footer)

def program_page(programs):
    f = open('index.html', 'w')

    if os.path.isfile('header.html.stub'):
        write_file(f, 'header.html.stub')
    else:
        write_raw( f, header)
    write_line(f, '        <!-- Copy from here...... -->')

    write_file(f, "program.css")

    write_raw( f, '\n')
    write_line(f, '<h2>Program 2015</h2>')
    write_raw( f, '\n')
    write_line(f, '<table class="program-top"><tr>')
    write_line(f, '<td class="program-notification">Merk: Denne siden bruker cookies for å huske dine favoritter. Trykk på stjernen(e) for å merke dine favoritter.</td>')
    write_line(f, '<td class="expand-all"><img src="http://static.trondheimdc.no/uploads/2015/s/ic_expand_more_white_24dp_2x.png"></td>')
    write_line(f, '</tr></table>')

    for show_time in show_times:
        write_line(f, '<section class="program-time %s">' % show_time[4])
        write_line(f, '    <h4  class="program-time">%s - %s %s</h4>' % (show_time[1], show_time[2], show_time[3]))

        for room in xrange(1,6):
            for program in programs:
                id = program['id']
                if show_time[0] !=      id[0:4]: continue
                if room         != int(id[8: ]): continue

                post_url = '#f%s' % (id)
                full_url = '%s/#f%s' % (base_url, id)
                face_url = 'https://www.facebook.com/dialog/feed?%s' % urllib.urlencode({
                    'app_id':       '1170433749639697',
                    'redirect_uri': full_url,
                    'display':      'page',
                    'link':         full_url,
                    'picture':      program['image'],
                    'name':         program['title'],
                    'description':  program['abstract'],
                    'caption':      '%s #tdconf 2015' % show_time[1],
                    })
                if program['image']:
                    image_tag = '<img class="program-img" src="%s">' % program['image']
                else:
                    image_tag = ''
                    print 'No image for    %s -- %s' % (program['author'], program['title'])
                if program['abstract'] != '':
                    abstract_tag = ''.join(['<p>%s</p>' % i for i in program['abstract'].split('\n')])
                else:
                    abstract_tag = ''
                    print 'No abstract for %s -- %s' % (program['author'], program['title'])
                if program['about'] != '':
                    about_tag = ''.join(['<p>%s</p>' % i for i in program['about'].split('\n')])
                else:
                    about_tag = ''
                    print 'No about for    %s -- %s' % (program['author'], program['title'])

                twitter_tag = ''
                if program['twitter'] != '':
                    twitter_tag = '<a href="https://twitter.com/intent/follow?screen_name=%s"><img class="program-social" src="http://static.trondheimdc.no/uploads/2015/s/twitter_grey.png">follow</a>  |' % program['twitter']


                write_raw( f, '\n')
                write_line(f, '    <div id="f%s" class="program-post">' % id)
                write_line(f, '        <table class="program-header">')
                write_line(f, '            <tr>')
                write_line(f, '                <th class="favourite">')
                write_line(f, '                    <div>Sal&nbsp;%s</div>' % room)
                write_line(f, '                    <img class="fav-icon" src="http://static.trondheimdc.no/uploads/2015/s/ic_star_border_white_24dp_1x.png">')
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
                write_line(f, '                    <img class="expand-icon" src="http://static.trondheimdc.no/uploads/2015/s/ic_expand_more_white_24dp_1x.png">')
                write_line(f, '                </td>')
                write_line(f, '            </tr>')
                write_line(f, '        </table>')
                write_line(f, '        <div class="program-talk hidden">')
                write_line(f, '            %s' % image_tag)
                write_line(f, '            %s' % abstract_tag)
                write_line(f, '            %s' % about_tag)
                write_line(f, '            <p class="program-footer">')
                write_line(f, '              %s' % twitter_tag)
                write_line(f, '              <a href="%s"><img class="program-social" src="http://static.trondheimdc.no/uploads/2015/s/facebook.png">share</a> |' % (face_url))
                write_line(f, '              <a href="%s">Sal&nbsp;%s - %s</a>' % (post_url, room, show_time[1]))
                write_line(f, '            </p>')
                write_line(f, '        </div>')
                write_line(f, '    </div>')

        write_line(f, '</section>')
        write_raw( f, '\n\n')

    write_file(f, "program.js")

    write_line(f, '        <!-- To here.............. -->')
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
        ['1130', '11:30', '11:45', 'Pause',         'sep'],
        ['1145', '11:45', '12:15', '',               ''],
        ['1215', '12:15', '13:15', 'Lunsj',          ''],
        ['1315', '13:15', '14:00', '',               ''],
        ['1400', '14:00', '14:15', 'Pause',          ''],
        ['1415', '14:15', '14:45', '',               ''],
        ['1445', '14:45', '15:00', 'Pause',          ''],
        ['1500', '15:00', '15:30', '',               ''],
        ['1530', '15:30', '15:45', 'Pause m/mat',    ''],
        ['1545', '15:45', '16:15', '',               ''],
        ['1615', '16:15', '16:30', 'Pause',          ''],
        ['1630', '16:30', '17:00', '',               ''],
        ['1700', '17:00', '17:15', 'Pause',          ''],
        ['1715', '17:15', '18:05', 'Closing session',''],
        ['1805', '18:05', '18:15', 'Outro',          ''],
        ['1815', '18:15', '01:00', 'TDConf party',   ''],
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
    input = read_input('kjoreplan_2015.csv')
    program_page(input)
    speaker_page(input)
    #import kjoreplan_sample
    #program_page(kjoreplan_sample.programs)
    #speaker_page(kjoreplan_sample.programs)
