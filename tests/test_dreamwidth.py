# -*- encoding: utf-8
"""Unit tests for itpe.dreamwidth."""

from mock import patch, MagicMock
import pytest

from itpe.dreamwidth import render_user_links


class TestUserLinks(object):

    def setup_method(self, method):
        self.cprint = patch('termcolor.cprint', new=MagicMock())
        self.cprint.start()

    def teardown_method(self):
        self.cprint.stop()

    @pytest.mark.parametrize('user_str, expected', [
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

        # Strings with a non-dw/ prefix do include a site= attribute
        ('tw/snake', '<user name=snake site=twitter.com>'),
        ('ao3/newt', '<user name=newt site=archiveofourown.org>'),
        ('tm/staff', '<user name=staff site=tumblr.com>'),
        ('tum/iguana', '<user name=iguana site=tumblr.com>'),

        # Comma-separated strings render correctly
        ('lion, ff/tiger',
         '<user name=lion>, <user name=tiger site=fanfiction.net>'),
        ('panther, cheetah, puma',
         '<user name=panther>, <user name=cheetah>, <user name=puma>'),
        ('lj/lynx,',
         '<user name=lynx site=livejournal.com>'),

        # Ampersand-separated strings render correctly
        ('rhino &', '<user name=rhino>'),
        ('pin/hippo & elephant',
         '<user name=hippo site=pinboard.in> & <user name=elephant>'),

        # Strings with commas and ampersands render correctly
        ('fish, squid & clam',
         '<user name=fish>, <user name=squid> & <user name=clam>'),
    ])
    def test_rendering_user_string(self, user_str, expected):
        """User strings are rendered correctly."""
        assert render_user_links(user_str) == expected

    @pytest.mark.parametrize('bad_user_str', [
        # Strings with >1 slash
        'parrot/budgie/parakeet',
        'cat//mouse',

        # Strings with an unknown site prefix
        'nope/turtle',
        'bad/tortoise',
        '/reptile',
    ])
    def test_rendering_bad_string(self, bad_user_str):
        """Malformed strings trigger a ValueError."""
        with pytest.raises(ValueError):
            render_user_links(bad_user_str)
