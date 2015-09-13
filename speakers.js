
        <script type="text/javascript">
            YUI().use('event-base', 'event', 'node', function (Y) {

                var shuffle = function(array) {
                    var currentIndex = array.length, temporaryValue, randomIndex;

                    // While there remain elements to shuffle...
                    while (0 !== currentIndex) {

                        // Pick a remaining element...
                        randomIndex = Math.floor(Math.random() * currentIndex);
                        currentIndex -= 1;

                        // And swap it with the current element.
                        temporaryValue = array[currentIndex];
                        array[currentIndex] = array[randomIndex];
                        array[randomIndex] = temporaryValue;
                    }

                    return array;
                }

                Y.on('domready', function () {
                    var speaker_list = Y.one("#speaker-list");
                    console.log('dom ready ' + speaker_list);
                    shuffle(speakers);

                    for (var i = 0; i < speakers.length; i++) {
                        var s = speakers[i];
                        var entity = "";
                        entity += "<a href='" + s.link + "'>";
                        entity += "  <img width='180px' src='" + s.image + "'>";
                        entity += "  <h5>" + s.author + "</h5>";
                        entity += "  <span>" + s.short_title + "</span>";
                        entity += "</a>";
                        speaker_list.append(entity);
                        // program.id program.image program.title
                        // program.abstract program.author program.about
                    }
                });

            });
        </script>

