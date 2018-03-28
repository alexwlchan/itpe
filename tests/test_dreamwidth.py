# -*- encoding: utf-8

import pytest

from itpe import dreamwidth as dreamwidth_usernames


@pytest.mark.parametrize('input_str, expected', [
    # Strings without a site prefix default to Dreamwidth.
    ('dog', '<user name=dog>'),
    ('fish', '<user name=fish>'),
    ('horse', '<user name=horse>'),
    ('gerbil', '<user name=gerbil>'),
])
def test_render_user_links(input_str, expected):
    assert dreamwidth_usernames.render_user_links(input_str) == expected
