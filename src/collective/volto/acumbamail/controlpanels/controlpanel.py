from collective.volto.acumbamail import _
from collective.volto.acumbamail.interfaces import IAcumbamailSettings
from plone.app.registry.browser import controlpanel


class AcumbamailSettingsForm(controlpanel.RegistryEditForm):
    schema = IAcumbamailSettings
    label = _("Acumbamail Settings")
    description = _("Define the credentials and connection parameters for Acumbamail service.")  # noqa: E501


class AcumbamailControlPanel(controlpanel.ControlPanelFormWrapper):
    form = AcumbamailSettingsForm
