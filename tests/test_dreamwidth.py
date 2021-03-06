# -*- encoding: utf-8

import pytest

from itpe import dreamwidth as dreamwidth_usernames


@pytest.mark.parametrize('input_str, expected', [
    # Strings with spaces or special phrases are skipped
    (' ', ''),
    ('fish cakes', 'fish cakes'),
    ('anonymous', 'anonymous'),
    ('anonymous cat', 'anonymous cat'),

    # Strings without a site prefix default to Dreamwidth
    ('dog', '<user name=dog>'),
    ('fish', '<user name=fish>'),
    ('horse', '<user name=horse>'),
    ('gerbil', '<user name=gerbil>'),

    # Strings with the dw/ prefix don't include a site= attribute
    ('dw/ferret', '<user name=ferret>'),
    ('dw/rabbit', '<user name=rabbit>'),
    ('dw/bunny', '<user name=bunny>'),

    # Strings with non-dw/ prefixes include a site= attribute
    ('tw/snake', '<user name=snake site=twitter.com>'),
    ('ao3/newt', '<user name=newt site=archiveofourown.org>'),
    ('tum/iguana', '<user name=iguana site=tumblr.com>'),
    ("tm/iguana", "<user name=iguana site=tumblr.com>"),

    # Comma-separated strings render correctly
    ('lion, ff/tiger', '<user name=lion>, <user name=tiger site=fanfiction.net>'),
    ('panther, cheetah, puma', '<user name=panther>, <user name=cheetah>, <user name=puma>'),
    ('lj/lynx,', '<user name=lynx site=livejournal.com>'),

    # Ampersand-separated strings render correctly
    ('rhino &', '<user name=rhino>'),
    ('pin/hippo & elephant', '<user name=hippo site=pinboard.in> & <user name=elephant>'),

    # Strings with commas and ampersands render correctly
    ('fish, squid & clam', '<user name=fish>, <user name=squid> & <user name=clam>'),
])
def test_render_user_links(input_str, expected):
    assert dreamwidth_usernames.render_user_links(input_str) == expected


@pytest.mark.parametrize('bad_input_str', [
    # Strings with >1 slash
    'parrot/budgie/parakeet',
    'cat///mouse',

    # Strings with an unknown site prefix
    'nope/turtle',
    'bad/tortoise',
    '/reptile',
])
def test_bad_strings_are_valueerror(bad_input_str):
    with pytest.raises(ValueError):
        dreamwidth_usernames.render_user_links(bad_input_str)
