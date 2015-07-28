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
                    var list_id = img.ancestor().get('id');

                    if (list_id in favourites && favourites[list_id]) {
                        img.set('src', 'http://raiom.no/tdconf-test-program/star_sel.png');
                    }
                });

                // Handle favourite icon clicked
                var favourite = Y.all(".favourite");
                favourite.on("click", function (e) {
                    var list_id = e.currentTarget.get('id');

                    var img = e.currentTarget.get('children');
                    if (list_id in favourites && favourites[list_id]) {
                        favourites[list_id] = false;
                        img.set('src', 'http://raiom.no/tdconf-test-program/star_unsel.png');
                    } else {
                        favourites[list_id] = true;
                        img.set('src', 'http://raiom.no/tdconf-test-program/star_sel.png');
                    }
                    Y.Cookie.set('favourites', Y.JSON.stringify(favourites), { expires: new Date("January 12, 2025") });
                });

                // Handle expand clicked
                var expand = Y.all(".expand");
                expand.on("click", function (e) {
                    var list_id     = e.currentTarget.get('id');
                    var show_id     = 'p' + list_id.substring(1);

                    var img         = e.currentTarget.one('img');
                    var show        = Y.one('#' + show_id);

                    var hidden = show.hasClass('hidden');
                    if (hidden) {
                        show.removeClass('hidden');
                        img.set('src', 'http://raiom.no/tdconf-test-program/arrow-up.png');
                    } else {
                        show.addClass('hidden');
                        img.set('src', 'http://raiom.no/tdconf-test-program/arrow-down.png');
                    }
                });

                // Handle kebab clicked
                var expand = Y.all(".kebab-icon");
                expand.on("click", function (e) {
                    console.log('kebab');
                });
            });
        </script>
