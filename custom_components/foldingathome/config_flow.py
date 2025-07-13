import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN, DEFAULT_HOST, DEFAULT_PORT, DEFAULT_PROXY_HOST

class FoldingAtHomeConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input:
            return self.async_create_entry(title="F@H", data=user_input)

        schema = vol.Schema({
            vol.Required("use_proxy", default=False): bool,
            vol.Optional("host", default="127.0.0.1"): str,
            vol.Optional("port", default=7396): int,
            vol.Optional("proxy_host", default=DEFAULT_PROXY_HOST): str,
        })
        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)