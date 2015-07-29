        <script type="text/javascript">
            YUI().use('json-parse', 'json-stringify', 'node', 'cookie', 'event', function (Y) {
                var favourites;
                try {
                    favourites = Y.JSON.parse(Y.Cookie.get("favourites")) || {};
                } catch (e) {
                    favourites = {};
                }
                console.log('favourites ' + Y.JSON.stringify(favourites));

                Y.all("img.fav-icon").each(function (img, idx, list) {
                    var show_id = img.ancestor('div.program-post').get('id');

                    if (show_id in favourites && favourites[show_id]) {
                        img.set('src', 'http://raiom.no/tdconf-test-program/ico/star_sel.png');
                    }
                });

                // Handle favourite icon clicked
                var favourite = Y.all(".favourite");
                favourite.on("click", function (e) {
                    var show_id = e.currentTarget.ancestor('div.program-post').get('id');

                    var img = e.currentTarget.one('img');
                    if (show_id in favourites && favourites[show_id]) {
                        favourites[show_id] = false;
                        img.set('src', 'http://raiom.no/tdconf-test-program/ico/star_unsel.png');
                    } else {
                        favourites[show_id] = true;
                        img.set('src', 'http://raiom.no/tdconf-test-program/ico/star_sel.png');
                    }
                    Y.Cookie.set('favourites', Y.JSON.stringify(favourites), { expires: new Date("January 12, 2025") });
                });

                // Handle expand clicked
                var expand = Y.all(".expand");
                expand.on("click", function (e) {
                    var program = e.currentTarget.ancestor('div.program-post');
                    var img     = program.one('img.expand-icon');
                    var talk    = program.one('div.program-talk');
                    var hidden = talk.hasClass('hidden');

                    if (hidden) {
                        talk.removeClass('hidden');
                        img.set('src', 'http://raiom.no/tdconf-test-program/ico/arrow-up.png');
                    } else {
                        talk.addClass('hidden');
                        img.set('src', 'http://raiom.no/tdconf-test-program/ico/arrow-down.png');
                    }
                });
            });
        </script>
