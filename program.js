        <script type="text/javascript">
            YUI().use('event-base', 'json-parse', 'json-stringify', 'node', 'cookie', 'event', function (Y) {
                // Keep all favourited shows
                var favourites;

                // Favourite all from cookie
                Y.on('domready', function () {
                    try {
                        favourites = Y.JSON.parse(Y.Cookie.get("favourites")) || {};
                    } catch (e) {
                        favourites = {};
                    }
                    //console.log('favourites ' + Y.JSON.stringify(favourites));

                    Y.all("img.fav-icon").each(function (img, idx, list) {
                        var show_id = img.ancestor('div.program-post').get('id');

                        if (show_id in favourites && favourites[show_id]) {
                            img.set('src', 'http://raiom.no/tdconf-test-program/ico/ic_star_white_24dp_1x.png');
                        }
                    });

                });

                // Handle favourite icon clicked
                Y.all(".favourite").on("click", function (e) {
                    var show_id = e.currentTarget.ancestor('div.program-post').get('id');

                    var img = e.currentTarget.one('img');
                    if (show_id in favourites && favourites[show_id]) {
                        favourites[show_id] = false;
                        img.set('src', 'http://raiom.no/tdconf-test-program/ico/ic_star_border_white_24dp_1x.png');
                    } else {
                        favourites[show_id] = true;
                        img.set('src', 'http://raiom.no/tdconf-test-program/ico/ic_star_white_24dp_1x.png');
                    }
                    Y.Cookie.set('favourites', Y.JSON.stringify(favourites), { expires: new Date("January 12, 2025") });
                });

                // Expand post based on program node
                var expand = function(program) {
                    var img     = program.one('img.expand-icon');
                    var talk    = program.one('div.program-talk');
                    var hidden = talk.hasClass('hidden');

                    if (hidden) {
                        talk.removeClass('hidden');
                        img.set('src', 'http://raiom.no/tdconf-test-program/ico/ic_expand_less_white_24dp_1x.png');
                    } else {
                        talk.addClass('hidden');
                        img.set('src', 'http://raiom.no/tdconf-test-program/ico/ic_expand_more_white_24dp_1x.png');
                    }
                }

                // Expand post based on url anchor hash
                Y.on('domready', function () {
                    if (window.location.hash.length > 0) {
                        var show_id = window.location.hash.substring(1);
                        console.log('show_id ' + show_id);
                        expand(Y.one("#" + show_id));
                    }
                });

                // Handle expand clicked
                Y.all(".expand").on("click", function (e) {
                    expand(e.currentTarget.ancestor('div.program-post'));
                });

                // Handle expand-all clicked
                Y.all(".expand-all").on("click", function (e) {
                    var img     = e.currentTarget.one('img');
                    var talks   = Y.all("div.program-talk");
                    var imgs    = Y.all("img.expand-icon");

                    var hidden = true;
                    if (! e.currentTarget.hasClass('expanded')) {
                        e.currentTarget.addClass('expanded');
                        talks.removeClass('hidden');
                        imgs.set('src', 'http://raiom.no/tdconf-test-program/ico/ic_expand_less_white_24dp_1x.png');
                        img.set('src', 'http://raiom.no/tdconf-test-program/ico/ic_expand_less_white_24dp_2x.png');
                    } else {
                        e.currentTarget.removeClass('expanded');
                        talks.addClass('hidden');
                        imgs.set('src', 'http://raiom.no/tdconf-test-program/ico/ic_expand_more_white_24dp_1x.png');
                        img.set('src', 'http://raiom.no/tdconf-test-program/ico/ic_expand_more_white_24dp_2x.png');
                    }
                });
            });
        </script>
