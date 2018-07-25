from collections import Hashable

import capybara
from capybara.exceptions import ExpectationNotMet
from capybara.helpers import expects_none, matches_count
from capybara.selector import selectors
from capybara.queries.selector_query import SelectorQuery
from capybara.queries.style_query import StyleQuery
from capybara.queries.text_query import TextQuery


class MatchersMixin(object):
    def has_selector(self, *args, **kwargs):
        """
        Checks if a given selector is on the page or a descendant of the current node. ::

            page.has_selector("p#foo")
            page.has_selector("xpath", ".//p[@id='foo']")

        By default it will check if the expression occurs at least once, but a different number can
        be specified. ::

            page.has_selector("p.foo", count=4)

        This will check if the expression occurs exactly 4 times.

        It also accepts all options that :meth:`find_all` accepts, such as ``text`` and
        ``visible``. ::

            page.has_selector("li", text="Horse", visible=True)

        ``has_selector`` can also accept XPath expressions generated by the ``xpath-py`` package::

            from xpath import dsl as x

            page.has_selector("xpath", x.descendant("p"))

        Args:
            *args: Variable length argument list for :class:`SelectorQuery`.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            bool: If the expression exists.
        """

        try:
            self.assert_selector(*args, **kwargs)
            return True
        except ExpectationNotMet:
            return False

    def has_no_selector(self, *args, **kwargs):
        """
        Checks if a given selector is not on the page or a descendant of the current node. Usage is
        identical to :meth:`has_selector`.

        Args:
            *args: Variable length argument list for :class:`SelectorQuery`.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            bool: Whether it doesn't exist.
        """

        try:
            self.assert_no_selector(*args, **kwargs)
            return True
        except ExpectationNotMet:
            return False

    def has_style(self, styles, **kwargs):
        """
        Checks if an element has the specified CSS styles. ::

            element.has_style({"color": "rgb(0,0,255)", "font-size": re.compile(r"px")})

        Args:
            styles (Dict[str, str | RegexObject]): The expected styles.

        Returns:
            bool: Whether the styles match.
        """

        try:
            self.assert_style(styles, **kwargs)
            return True
        except ExpectationNotMet:
            return False

    def has_all_of_selectors(self, selector, *locators, **kwargs):
        """
        Checks if allof the provided selectors are present on the given page or descendants of the
        current node. If options are provided, the assertion will check that each locator is present
        with those options as well (other than ``wait``). ::

            page.assert_all_of_selectors("custom", "Tom", "Joe", visible="all")
            page.assert_all_of_selectors("css", "#my_dif", "a.not_clicked")

        It accepts all options that :meth:`find_all` accepts, such as ``text`` and ``visible``.

        The ``wait`` option applies to all of the selectors as a group, so all of the locators must
        be present within ``wait`` (defaults to :data:`capybara.default_max_wait_time`) seconds.

        If the given selector is not a valid selector, the first argument is assumed to be a locator
        and the default selector will be used.

        Args:
            selector (str, optional): The name of the selector to use. Defaults to
                :data:`capybara.default_selector`.
            *locators (str): Variable length list of locators.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.
        """

        try:
            self.assert_all_of_selectors(selector, *locators, **kwargs)
            return True
        except ExpectationNotMet:
            return False

    def has_none_of_selectors(self, selector, *locators, **kwargs):
        """
        Checks if none of the provided selectors are present on the given page or descendants of the
        current node. If options are provided, the assertion will check that each locator is present
        with those options as well (other than ``wait``). ::

            page.assert_none_of_selectors("custom", "Tom", "Joe", visible="all")
            page.assert_none_of_selectors("css", "#my_div", "a.not_clicked")

        It accepts all options that :meth:`find_all` accepts, such as ``text`` and ``visible``.

        The ``wait`` option applies to all of the selectors as a group, so none of the locators must
        be present with ``wait`` (defaults to :data:`capybara.default_max_wait_time`) seconds.

        If the given selector is not a valid selector, the first argument is assumed to be a locator
        and the default selector will be used.

        Args:
            selector (str, optional): The name of the selector to use. Defaults to
                :data:`capybara.default_selector`.
            *locators (str): Variable length list of locators.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.
        """

        try:
            self.assert_none_of_selectors(selector, *locators, **kwargs)
            return True
        except ExpectationNotMet:
            return False

    def matches_selector(self, *args, **kwargs):
        """
        Checks if the current node matches the given selector.

        Args:
            *args: Variable length argument list for :class:`SelectorQuery`.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            bool: Whether it matches.
        """

        try:
            self.assert_matches_selector(*args, **kwargs)
            return True
        except ExpectationNotMet:
            return False

    def not_match_selector(self, *args, **kwargs):
        """
        Checks if the current node does not match the given selector. Usage is identical to
        :meth:`has_selector`.

        Args:
            *args: Variable length argument list for :class:`SelectorQuery`.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            bool: Whether it doesn't match.
        """

        try:
            self.assert_not_match_selector(*args, **kwargs)
            return True
        except ExpectationNotMet:
            return False

    def assert_selector(self, *args, **kwargs):
        """
        Asserts that a given selector is on the page or a descendant of the current node. ::

            page.assert_selector("p#foo")

        By default it will check if the expression occurs at least once, but a different number can
        be specified. ::

            page.assert_selector("p.foo", count=4)

        This will check if the expression occurs exactly 4 times. See :meth:`find_all` for other
        available result size options.

        If a ``count`` of 0 is specified, it will behave like :meth:`assert_no_selector`; however,
        use of that method is preferred over this one.

        It also accepts all options that :meth:`find_all` accepts, such as ``text`` and
        ``visible``. ::

            page.assert_selector("li", text="Horse", visible=True)

        ``assert_selector`` can also accept XPath expressions generated by the ``xpath-py``
        package::

            from xpath import dsl as x

            page.assert_selector("xpath", x.descendant("p"))

        Args:
            *args: Variable length argument list for :class:`SelectorQuery`.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            True

        Raises:
            ExpectationNotMet: The given selector did not match.
        """

        query = SelectorQuery(*args, **kwargs)

        @self.synchronize(wait=query.wait)
        def assert_selector():
            result = query.resolve_for(self)

            if not (result.matches_count and
                    (len(result) > 0 or expects_none(query.options))):
                raise ExpectationNotMet(result.failure_message)

            return True

        return assert_selector()

    def assert_style(self, styles, **kwargs):
        """
        Asserts that an element has the specified CSS styles. ::

            element.assert_style({"color": "rgb(0,0,255)", "font-size": re.compile(r"px")})

        Args:
            styles (Dict[str, str | RegexObject]): The expected styles.

        Returns:
            True

        Raises:
            ExpectationNotMet: The element doesn't have the specified styles.
        """

        query = StyleQuery(styles, **kwargs)

        @self.synchronize(wait=query.wait)
        def assert_style():
            if not query.resolves_for(self):
                raise ExpectationNotMet(query.failure_message)

            return True

        return assert_style()

    def assert_all_of_selectors(self, selector, *locators, **kwargs):
        """
        Asserts that all of the provided selectors are present on the given page or descendants of
        the current node. If options are provided, the assertion will check that each locator is
        present with those options as well (other than ``wait``). ::

            page.assert_all_of_selectors("custom", "Tom", "Joe", visible="all")
            page.assert_all_of_selectors("css", "#my_dif", "a.not_clicked")

        It accepts all options that :meth:`find_all` accepts, such as ``text`` and ``visible``.

        The ``wait`` option applies to all of the selectors as a group, so all of the locators must
        be present within ``wait`` (defaults to :data:`capybara.default_max_wait_time`) seconds.

        If the given selector is not a valid selector, the first argument is assumed to be a locator
        and the default selector will be used.

        Args:
            selector (str, optional): The name of the selector to use. Defaults to
                :data:`capybara.default_selector`.
            *locators (str): Variable length list of locators.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.
        """

        wait = kwargs['wait'] if 'wait' in kwargs else capybara.default_max_wait_time

        if not isinstance(selector, Hashable) or selector not in selectors:
            locators = (selector,) + locators
            selector = capybara.default_selector

        @self.synchronize(wait=wait)
        def assert_all_of_selectors():
            for locator in locators:
                self.assert_selector(selector, locator, **kwargs)

            return True

        return assert_all_of_selectors()

    def assert_none_of_selectors(self, selector, *locators, **kwargs):
        """
        Asserts that none of the provided selectors are present on the given page or descendants of
        the current node. If options are provided, the assertion will check that each locator is
        present with those options as well (other than ``wait``). ::

            page.assert_none_of_selectors("custom", "Tom", "Joe", visible="all")
            page.assert_none_of_selectors("css", "#my_div", "a.not_clicked")

        It accepts all options that :meth:`find_all` accepts, such as ``text`` and ``visible``.

        The ``wait`` option applies to all of the selectors as a group, so none of the locators must
        be present with ``wait`` (defaults to :data:`capybara.default_max_wait_time`) seconds.

        If the given selector is not a valid selector, the first argument is assumed to be a locator
        and the default selector will be used.

        Args:
            selector (str, optional): The name of the selector to use. Defaults to
                :data:`capybara.default_selector`.
            *locators (str): Variable length list of locators.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.
        """
        wait = kwargs['wait'] if 'wait' in kwargs else capybara.default_max_wait_time

        if not isinstance(selector, Hashable) or selector not in selectors:
            locators = (selector,) + locators
            selector = capybara.default_selector

        @self.synchronize(wait=wait)
        def assert_none_of_selectors():
            for locator in locators:
                self.assert_no_selector(selector, locator, **kwargs)

            return True

        return assert_none_of_selectors()

    def assert_no_selector(self, *args, **kwargs):
        """
        Asserts that a given selector is not on the page or a descendant of the current node. Usage
        is identical to :meth:`assert_selector`.

        Query options such as ``count``, ``minimum``, and ``between`` are considered to be an
        integral part of the selector. This will return True, for example, if a page contains 4
        anchors but the query expects 5::

            page.assert_no_selector("a", minimum=1)  # Found, raises ExpectationNotMet
            page.assert_no_selector("a", count=4)    # Found, raises ExpectationNotMet
            page.assert_no_selector("a", count=5)    # Not Found, returns True

        Args:
            *args: Variable length argument list for :class:`SelectorQuery`.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            True

        Raises:
            ExpectationNotMet: The given selector matched.
        """

        query = SelectorQuery(*args, **kwargs)

        @self.synchronize(wait=query.wait)
        def assert_no_selector():
            result = query.resolve_for(self)

            if result.matches_count and (
                   len(result) > 0 or expects_none(query.options)):
                raise ExpectationNotMet(result.negative_failure_message)

            return True

        return assert_no_selector()

    refute_selector = assert_no_selector
    """ Alias for :meth:`assert_no_selector`. """

    def assert_matches_selector(self, *args, **kwargs):
        """
        Asserts that the current node matches a given selector. ::

            node.assert_matches_selector("p#foo")
            node.assert_matches_selector("xpath", "//p[@id='foo']")

        It also accepts all options that :meth:`find_all` accepts, such as ``text`` and
        ``visible``. ::

            node.assert_matches_selector("li", text="Horse", visible=True)

        Args:
            *args: Variable length argument list for :class:`SelectorQuery`.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            True

        Raises:
            ExpectationNotMet: If the selector does not match.
        """

        query = SelectorQuery(*args, **kwargs)

        @self.synchronize(wait=query.wait)
        def assert_matches_selector():
            result = query.resolve_for(self.find_first("xpath", "./parent::*", minimum=0) or self.query_scope)

            if self not in result:
                raise ExpectationNotMet("Item does not match the provided selector")

            return True

        return assert_matches_selector()

    def assert_not_match_selector(self, *args, **kwargs):
        """
        Asserts that the current node does not match a given selector. See
        :meth:`assert_matches_selector`.

        Args:
            *args: Variable length argument list for :class:`SelectorQuery`.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            True

        Raises:
            ExpectationNotMet: If the selector matches.
        """

        query = SelectorQuery(*args, **kwargs)

        @self.synchronize(wait=query.wait)
        def assert_not_match_selector():
            result = query.resolve_for(self.find_first("xpath", "./parent::*", minimum=0) or self.query_scope)

            if self in result:
                raise ExpectationNotMet("Item matched the provided selector")

            return True

        return assert_not_match_selector()

    refute_matches_selector = assert_not_match_selector
    """ Alias for :meth:`assert_not_match_selector`. """

    def matches_xpath(self, xpath, **kwargs):
        """
        Checks if the current node matches the given XPath expression.

        Args:
            xpath (str | xpath.expression.Expression): The XPath expression to match against the
                current node.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Return:
            bool: Whether it matches.
        """

        return self.matches_selector("xpath", xpath, **kwargs)

    def not_match_xpath(self, xpath, **kwargs):
        """
        Checks if the current node does not match the given XPath expression.

        Args:
            xpath (str | xpath.expression.Expression): The XPath expression to match against the
                current node.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Return:
            bool: Whether it doesn't match.
        """

        return self.not_match_selector("xpath", xpath, **kwargs)

    def matches_css(self, css, **kwargs):
        """
        Checks if the current node matches the given CSS selector.

        Args:
            css (str): The CSS selector to match against the current node.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Return:
            bool: Whether it matches.
        """

        return self.matches_selector("css", css, **kwargs)

    def not_match_css(self, css, **kwargs):
        """
        Checks if the current node does not match the given CSS selector.

        Args:
            css (str): The CSS selector to match against the current node.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Return:
            bool: Whether it doesn't match.
        """

        return self.not_match_selector("css", css, **kwargs)

    def has_xpath(self, query, **kwargs):
        """
        Checks if a given XPath expression is on the page or a descendant of the current node. ::

            session.has_xpath(".//p[@id='foo']")

        ``has_xpath`` can also accept XPath expressions generated by the ``xpath-py`` package::

            from xpath import dsl as x

            session.has_xpath(x.descendant("p"))

        Args:
            query (str): An XPath expression.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Return:
            bool: If the expression exists.
        """

        return self.has_selector("xpath", query, **kwargs)

    def has_no_xpath(self, path, **kwargs):
        """
        Checks if a given XPath expression is not on the page or a descendant of the current node.
        Usage is identical to :meth:`has_xpath`.

        Args:
            path (str): An XPath expression.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Return:
            bool: If the expression does not exist.
        """

        return self.has_no_selector("xpath", path, **kwargs)

    def has_css(self, path, **kwargs):
        """
        Checks if a given CSS selector is on the page or a descendant of the current node. ::

            page.has_css("p#foo")

        By default it will check if the selector occurs at least once, but a different number can
        be specified. ::

            page.has_css("p#foo", count=4)

        This will check if the selector occurs exactly 4 times.

        It also accepts all options that :meth:`find_all` accepts, such as ``text`` and
        ``visible``. ::

            page.has_css("li", text="Horse", visible=True)

        Args:
            path (str): A CSS selector.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Return:
            bool: If the selector exists.
        """

        return self.has_selector("css", path, **kwargs)

    def has_no_css(self, path, **kwargs):
        """
        Checks if a given CSS selector is not on the page or a descendant of the current node.
        Usage is identical to :meth:`has_css`.

        Args:
            path (str): A CSS Selector.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Return:
            bool: If the selector does not exist.
        """

        return self.has_no_selector("css", path, **kwargs)

    def has_button(self, locator, **kwargs):
        """
        Checks if the page or current node has a button with the given text, value, or id.

        Args:
            locator (str): The text, value, or id of a button to check for.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            bool: Whether it exists.
        """

        return self.has_selector("button", locator, **kwargs)

    def has_no_button(self, locator, **kwargs):
        """
        Checks if the page or current node has no button with the given text, value, or id.

        Args:
            locator (str): The text, value, or id of a button to check for.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            bool: Whether it doesn't exist.
        """

        return self.has_no_selector("button", locator, **kwargs)

    def has_checked_field(self, locator, **kwargs):
        """
        Checks if the page or current node has a radio button or checkbox with the given label,
        value, or id, that is currently checked.

        Args:
            locator (str): The label, name, or id of a checked field.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            bool: Whether it exists.
        """

        kwargs["checked"] = True
        return self.has_selector("field", locator, **kwargs)

    def has_no_checked_field(self, locator, **kwargs):
        """
        Checks if the page or current node has no radio button or checkbox with the given label,
        value, or id that is currently checked.

        Args:
            locator (str): The label, name, or id of a checked field.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            bool: Whether it doesn't exist.
        """

        kwargs["checked"] = True
        return self.has_no_selector("field", locator, **kwargs)

    def has_field(self, locator, **kwargs):
        """
        Checks if the page or current node has a form field with the given label, name, or id.

        For text fields and other textual fields, such as textareas and HTML5 email/url/etc. fields,
        it's possible to specify a ``value`` argument to specify the text the field should contain::

            page.has_field("Name", value="Jonas")

        Args:
            locator (str): The label, name, or id of a field to check for.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            bool: Whether it exists.
        """

        return self.has_selector("field", locator, **kwargs)

    def has_no_field(self, locator, **kwargs):
        """
        Checks if the page or current node has no form field with the given label, name, or id. See
        :meth:`has_field`.

        Args:
            locator (str): The label, name, or id of a field to check for.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            bool: Whether it doesn't exist.
        """

        return self.has_no_selector("field", locator, **kwargs)

    def has_link(self, locator, **kwargs):
        """
        Checks if the page or current node has a link with the given text or id.

        Args:
            locator (str): The text or id of a link to check for.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            bool: Whether it exists.
        """

        return self.has_selector("link", locator, **kwargs)

    def has_no_link(self, locator, **kwargs):
        """
        Checks if the page or current node has no link with the given text or id.

        Args:
            locator (str): The text or id of a link to check for.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            bool: Whether it doesn't exist.
        """

        return self.has_no_selector("link", locator, **kwargs)

    def has_select(self, locator, **kwargs):
        """
        Checks if the page or current node has a select field with the given label, name, or id.

        It can be specified which option should currently be selected::

            page.has_select("Language", selected="German")

        For multiple select boxes, several options may be specified::

            page.has_select("Language", selected=["English", "German"])

        It's also possible to check if the exact set of options exists for this select box::

            page.has_select("Language", options=["English", "German", "Spanish"])

        You can also check for a partial set of options::

            page.has_select("Language", with_options=["English", "German"])

        Args:
            locator (str): The label, name, or id of a select box.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            bool: Whether it exists.
        """

        return self.has_selector("select", locator, **kwargs)

    def has_no_select(self, locator, **kwargs):
        """
        Checks if the page or current node has no select field with the given label, name, or id.
        See :meth:`has_select`.

        Args:
            locator (str): The label, name, or id of a select box.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            bool: Whether it doesn't exist.
        """

        return self.has_no_selector("select", locator, **kwargs)

    def has_table(self, locator, **kwargs):
        """
        Checks if the page or current node has a table with the given id or caption::

            page.has_table("People")

        Args:
            locator (str): The id or caption of a table.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            bool: Whether it exists.
        """

        return self.has_selector("table", locator, **kwargs)

    def has_no_table(self, locator, **kwargs):
        """
        Checks if the page or current node has no table with the given id or caption. See
        :meth:`has_table`.

        Args:
            locator (str): The id or caption of a table.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            bool: Whether it doesn't exist.
        """

        return self.has_no_selector("table", locator, **kwargs)

    def has_unchecked_field(self, locator, **kwargs):
        """
        Checks if the page or current node has a radio button or checkbox with the given label,
        value, or id, that is currently unchecked.

        Args:
            locator (str): The label, name, or id of an unchecked field.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            bool: Whether it exists.
        """

        kwargs["checked"] = False
        return self.has_selector("field", locator, **kwargs)

    def has_no_unchecked_field(self, locator, **kwargs):
        """
        Checks if the page or current node has no radio button or checkbox with the given label,
        value, or id, that is currently unchecked.

        Args:
            locator (str): The label, name, or id of an unchecked field.
            **kwargs: Arbitrary keyword arguments for :class:`SelectorQuery`.

        Returns:
            bool: Whether it doesn't exist.
        """

        kwargs["checked"] = False
        return self.has_no_selector("field", locator, **kwargs)

    def assert_text(self, *args, **kwargs):
        """
        Asserts that the page or current node has the given text content, ignoring any HTML tags.

        Args:
            *args: Variable length argument list for :class:`TextQuery`.
            **kwargs: Arbitrary keyword arguments for :class:`TextQuery`.

        Returns:
            True

        Raises:
            ExpectationNotMet: If the assertion hasn't succeeded during the wait time.
        """

        query = TextQuery(*args, **kwargs)

        @self.synchronize(wait=query.wait)
        def assert_text():
            count = query.resolve_for(self)

            if not (matches_count(count, query.options) and
                    (count > 0 or expects_none(query.options))):
                raise ExpectationNotMet(query.failure_message)

            return True

        return assert_text()

    def assert_no_text(self, *args, **kwargs):
        """
        Asserts that the page or current node doesn't have the given text content, ignoring any
        HTML tags.

        Args:
            *args: Variable length argument list for :class:`TextQuery`.
            **kwargs: Arbitrary keyword arguments for :class:`TextQuery`.

        Returns:
            True

        Raises:
            ExpectationNotMet: If the assertion hasn't succeeded during the wait time.
        """

        query = TextQuery(*args, **kwargs)

        @self.synchronize(wait=query.wait)
        def assert_no_text():
            count = query.resolve_for(self)

            if matches_count(count, query.options) and (
                   count > 0 or expects_none(query.options)):
                raise ExpectationNotMet(query.negative_failure_message)

            return True

        return assert_no_text()

    def has_text(self, *args, **kwargs):
        """
        Checks if the page or current node has the given text content, ignoring any HTML tags.

        Whitespaces are normalized in both the node's text and the passed text parameter. Note that
        whitespace isn't normalized in a passed regular expression as normalizing whitespace in a
        regular expression isn't easy and doesn't seem to be worth it.

        By default it will check if the text occurs at least once, but a different number can be
        specified. ::

            page.has_text("lorem ipsum", between=range(2, 5))

        Args:
            *args: Variable length argument list for :class:`TextQuery`.
            **kwargs: Arbitrary keyword arguments for :class:`TextQuery`.

        Returns:
            bool: Whether it exists.
        """

        try:
            return self.assert_text(*args, **kwargs)
        except ExpectationNotMet:
            return False

    has_content = has_text
    """ Alias for :meth:`has_text`. """

    def has_no_text(self, *args, **kwargs):
        """
        Checks if the page or current node does not have the given text content, ignoring any HTML
        tags and normalizing whitespace.

        Args:
            *args: Variable length argument list for :class:`TextQuery`.
            **kwargs: Arbitrary keyword arguments for :class:`TextQuery`.

        Returns:
            bool: Whether it doesn't exist.
        """

        try:
            return self.assert_no_text(*args, **kwargs)
        except ExpectationNotMet:
            return False

    has_no_content = has_no_text
    """ Alias for :meth:`has_no_text`. """
