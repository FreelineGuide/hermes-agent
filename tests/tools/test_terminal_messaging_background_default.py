"""A messaging surface defaults an undeclared terminal call to background."""

from tools.terminal_tool import _messaging_background_default_enabled


def _patch_session(monkeypatch, *, messaging: bool, async_delivery: bool):
    from gateway import session_context

    monkeypatch.setattr(session_context, "session_is_messaging_surface", lambda: messaging)
    monkeypatch.setattr(session_context, "async_delivery_supported", lambda: async_delivery)


def test_messaging_surface_enables_background_default(monkeypatch):
    _patch_session(monkeypatch, messaging=True, async_delivery=True)
    assert _messaging_background_default_enabled() is True


def test_non_messaging_surface_keeps_foreground_default(monkeypatch):
    _patch_session(monkeypatch, messaging=False, async_delivery=True)
    assert _messaging_background_default_enabled() is False


def test_session_without_async_delivery_keeps_foreground_default(monkeypatch):
    _patch_session(monkeypatch, messaging=True, async_delivery=False)
    assert _messaging_background_default_enabled() is False
