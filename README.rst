swot
----

If you have a product or service and offer **academic discounts**,
there's a good chance there's some manual component to the approval
process. Perhaps ``.edu`` email addresses are automatically approved
because, for the most part at least, they're associated with American
post-secondary educational institutions. Perhaps ``.ac.uk`` email
addresses are automatically approved because they're guaranteed to
belong to British universities and colleges. Unfortunately, not every
country has an education-specific TLD (Top Level Domain) and plenty of
schools use ``.com`` or ``.net``.

Swot is a community-driven or crowdsourced library for verifying that
domain names and email addresses are tied to a legitimate university of
college - more specifically, an academic institution providing higher
education in tertiary, quaternary or any other kind of post-secondary
education in any country in the world.

Installation
------------

Install swot with pip::

    pip install swot

Usage
-----
::

    >>> import swot

    >>> swot.is_academic("student@rutgers.edu") 
    True
    >>> swot.is_academic("coolboy1998@hotmail.com") 
    False

    # Url's work as well
    >>> swot.is_academic("https://www.brown.edu")
    True
    >>> swot.is_academic("http://web.mit.edu:8080") 
    True

    # We can also get school names
    >>> swot.get_school_name("ze@cornell.edu") 
    ["Cornell University"] 
    >>> swot.get_school_name("harvard.edu") 
    ["Harvard University"]
